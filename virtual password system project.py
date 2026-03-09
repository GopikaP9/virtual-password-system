import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Virtual Password System", layout="centered")

# Initialize session state for variables
if 'attempts_count' not in st.session_state:
    st.session_state.attempts_count = 0
if 'entered_password' not in st.session_state:
    st.session_state.entered_password = ""
if 'chars' not in st.session_state:
    st.session_state.chars = list("0123456789ABC@#*")
    random.shuffle(st.session_state.chars)

real_password = "2006"

st.title("🛡️ Virtual Password System")
st.write("Enter your password using the secure keypad below:")

# Display current entered password (as stars)
display_text = "*" * len(st.session_state.entered_password)
st.subheader(f"Password: {display_text}")

# Button functions
def press(char):
    st.session_state.entered_password += str(char)

def clear_entry():
    st.session_state.entered_password = ""

def check_password():
    if st.session_state.entered_password == real_password:
        st.success("✅ Access Granted!")
        st.balloons()
        st.session_state.attempts_count = 0
    else:
        st.session_state.attempts_count += 1
        remaining = 3 - st.session_state.attempts_count
        if st.session_state.attempts_count >= 3:
            st.error("🚫 System Locked! Too many wrong attempts.")
            st.session_state.entered_password = ""
        else:
            st.warning(f"❌ Wrong Password! {remaining} attempts remaining.")
            st.session_state.entered_password = ""

# Create Grid Layout for Keypad
cols = st.columns(4)
for i, char in enumerate(st.session_state.chars):
    if cols[i % 4].button(char, key=f"btn_{char}"):
        press(char)
        st.rerun()

st.divider()

# Action Buttons
col1, col2 = st.columns(2)
if col1.button("🗑️ Clear", use_container_width=True):
    clear_entry()
    st.rerun()

if col2.button("🔓 Login", use_container_width=True):
    check_password()


