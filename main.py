import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Check against common weak passwords
    common_passwords = ['password123', '123456', 'qwerty', 'letmein']
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ Password is too common. Choose a unique password.")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

# Function to generate a strong password
def generate_strong_password():
    # Define characters for a strong password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*"

    # Combine all character sets
    all_characters = uppercase + lowercase + digits + special_characters

    # Generate a strong password with a random combination
    password = ''.join(random.choice(all_characters) for i in range(12))

    return password

st.title(" Password Strength Meter 🔐")
password = st.text_input("Enter your password:")

if password:
    strength_message, feedback = check_password_strength(password)

    st.subheader(strength_message)

    if feedback:
        for message in feedback:
            st.write(message)

    if strength_message == "❌ Weak Password - Improve it using the suggestions above.":
        st.subheader("🔑 Suggested Strong Password:")
        suggested_password = generate_strong_password()
        st.write(f"{suggested_password}")
