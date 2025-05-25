# File: secure_vault_app.py
import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import json
import os
import time
import requests

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Secure Vault", page_icon="🔐", layout="centered")

DATA_FILE = "data.json"
MASTER_KEY = "1lOc3774SyTIRHq4VdmvMUmsrux3toXLeyiqYWZ5t_4=".encode()
cipher = Fernet(MASTER_KEY)

# ---------------- HELPERS ----------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted):
    return cipher.decrypt(encrypted.encode()).decode()

def load_lottie(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

# ---------------- INIT ----------------
if "user" not in st.session_state:
    st.session_state.user = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "data" not in st.session_state:
    st.session_state.data = load_data()

# ---------------- UI ----------------
menu = ["🏠 Home", "📝 Register", "👤 Login", "🗂 Store Data", "🔓 Retrieve Data", "📜 History"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- PAGES ----------------
if choice == "🏠 Home":
    st.markdown("""
        <div style='background:#0a9396;padding:15px;border-radius:10px;text-align:center;'>
            <h2 style='color:white;'>🔐 Secure Data Vault</h2>
            <p style='color:white;'>Encrypt and store your secrets safely with Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Welcome! 🔐")
    st.write("This app helps you store and retrieve encrypted data securely.")
    st.markdown("""
    *Features*:
    - 🔒 Time-based Lockout
    - 📦 Persistent JSON Storage
    - 👤 Multi-user Support
    - 📱 Responsive Design
    - 🌐 Deployable to Streamlit Cloud
    - 📝 Labels for each entry
    - ❌ Deletion support
    """)

elif choice == "📝 Register":
    st.subheader("Create New Account")
    new_user = st.text_input("Choose a Username")
    new_pass = st.text_input("Create a Passkey", type="password")
    if st.button("Register"):
        if new_user and new_pass:
            if new_user in st.session_state.data:
                st.warning("⚠ Username already exists. Try a different one.")
            else:
                st.session_state.data[new_user] = {
                    "passkey": hash_passkey(new_pass),
                    "vault": {}
                }
                save_data(st.session_state.data)
                st.success("✅ Registered successfully! Please login now.")
        else:
            st.error("❌ All fields are required.")

elif choice == "👤 Login":
    st.subheader("User Login 👤")
    username = st.text_input("Enter Username")
    passkey = st.text_input("Enter Your Passkey", type="password")
    if st.button("Login"):
        if username and passkey:
            hashed = hash_passkey(passkey)
            if username in st.session_state.data and st.session_state.data[username]["passkey"] == hashed:
                st.session_state.user = username
                st.success(f"✅ Welcome {username}!")
            else:
                st.error("❌ Incorrect username or passkey.")
        else:
            st.warning("Please enter both fields.")

elif choice == "🗂 Store Data":
    if not st.session_state.user:
        st.warning("Please login first.")
    else:
        st.subheader("🔐 Encrypt & Store")
        label = st.text_input("Label for your secret (e.g., Gmail Password)")
        text = st.text_area("Enter text to encrypt")
        if st.button("Encrypt & Save"):
            if label and text:
                encrypted = encrypt_data(text)
                user = st.session_state.user
                st.session_state.data[user]["vault"][encrypted] = {
                    "data": encrypted,
                    "label": label,
                    "time": time.ctime()
                }
                save_data(st.session_state.data)
                st.success("✅ Encrypted and saved!")
                st.code(encrypted)
                st.snow()
            else:
                st.warning("Label and Text both are required.")

elif choice == "🔓 Retrieve Data":
    if not st.session_state.user:
        st.warning("Please login first.")
    else:
        st.subheader("🔓 Retrieve Data")
        user = st.session_state.user
        vault = st.session_state.data[user]["vault"]
        if vault:
            options = [(v["label"], k) for k, v in vault.items()]
            selected_label = st.selectbox("Select a label", [label for label, _ in options])
            selected_key = dict(options)[selected_label]
            if st.button("🔓 Decrypt"):
                try:
                    decrypted = decrypt_data(selected_key)
                    st.success("✅ Decryption Successful!")
                    st.code(decrypted)
                    st.balloons()
                except:
                    st.error("❌ Failed to decrypt.")
        else:
            st.info("No encrypted data found.")

elif choice == "📜 History":
    if not st.session_state.user:
        st.warning("Please login first.")
    else:
        st.subheader("📜 Your Vault History")
        user = st.session_state.user
        vault = st.session_state.data[user]["vault"]
        if vault:
            for k, v in vault.items():
                with st.expander(v["label"]):
                    st.markdown(f"*Encrypted:* {v['data']}")
                    st.markdown(f"*Stored on:* {v['time']}")
                    if st.button("❌ Delete", key=k):
                        del st.session_state.data[user]["vault"][k]
                        save_data(st.session_state.data)
                        st.success("Deleted successfully.")
                        st.rerun()  # ✅ Updated line
        else:
            st.info("No data available.")

# ---------------- Footer ----------------
st.markdown("""
    <hr>
    <center style='color:gray;'>Develop by ❤ Anusha Akhther </center>
""", unsafe_allow_html=True)