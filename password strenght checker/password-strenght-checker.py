# Basic password strength checker app using Streamlit
import streamlit as st
import re

# Page config
st.set_page_config(page_title="Password Strength Checker App", page_icon="🔒")

# Title & Description
st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the Ultimate Password Strength Checker! 👋🏻  
This app helps you create passwords that are *hard to crack* 🔐 and *easy to remember* 🧠.  
Let's make your online life safer! 🚀
""")

# User input
password = st.text_input("🔑 Enter your password:", type="password")
password_strength = st.empty()

feedback = []
score = 0

if password:
    # Password Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be *at least 8 characters* long. 📏")

    # Upper and Lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Use *both uppercase and lowercase letters*. 🔠")

    # Numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Include *at least one number*. 🔢")

    # Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add *special characters* like !@#$% for extra security. 💥")

    # Strength Result
    st.markdown("### 🔍 Password Strength Result:")
    if score == 4:
        st.success("✅ Your password is *strong*! 💪 Great job!")
    elif score == 3:
        st.warning("⚠ Your password is *medium*. Add more variety to make it stronger! 🔧")
    elif score == 2:
        st.warning("⚠ Your password is *weak*. Consider adding numbers, special characters, and using upper/lowercase. 🛠")
    else:
        st.error("❌ Your password is *very weak*! Please improve it. 🚫")

    # Show suggestions
    if feedback:
        st.markdown("### 🛡 Suggestions to Improve:")
        for tip in feedback:
            st.markdown(f"- {tip}")

else:
    st.info("💡 Please enter a password to check its strength.")