import streamlit as st
import re
import string
import random

st.set_page_config(page_title="Password strength checker & generator",page_icon="🔐")
st.title("Password strength checker & Generator 🔐")
st.markdown('''
            ## Welcome to our cool password app!
            **Generate or Strengthen your password — securely and smartly.**
            ''')
on = st.toggle("Generate my password.")

if on:
    def generate_password(length,use_digits,use_special):
        characters=string.ascii_letters
        if use_digits:
            characters+=string.digits
        if use_special:
            characters+=string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
    
    length=st.slider('Set the range for your password',max_value=32,min_value=8)
    use_digits=st.checkbox('Include digits')
    use_special=st.checkbox('Include special characters')
    
    if st.button('Generate'):
        password=generate_password(length,use_digits,use_special)
        st.write(f'Password: `{password}`')
    
        

else:
 password = st.text_input("Enter your password",type="password")

 tips =  []
 score=0

 if password:
    if len(password)>=8:
        score+=1
    else:
        tips.append("❌Your password should atleast contain 8 chraacters")
        
    if re.search(r'[A-Z]',password):
        score+=1
    else:
        tips.append("❌Include at least one uppercase letter to increase complexity and enhance security")
    if re.search(r'[a-z]',password):
        score+=1
    else:
        tips.append("Include at least one lowercase letter to increase complexity and enhance security")
    if re.search(r'\d',password):
        score+=1
    else:
        tips.append("❌Incorporate numbers into your password to add complexity. ")
        
    if re.search(r'[@#$%*&}_;,]',password):
        score+=1
    else:
        tips.append("❌Add special characters (e.g., @, #, $, %) to make your password more secure and harder to crack")     
    if score==5:
        st.header("_Password_ is :green[strong]")
        st.markdown(f'<h4 style="color:	#2E8B57">Strength: {score*100/5}%</h4>', unsafe_allow_html=True)
        st.write("Review: Good, using that password is like locking your front door and keeping the key in a safety deposit box")
    elif 3 <= score <= 4:
        st.header("_Password_ is :blue[medium]")
        st.markdown(f'<h4 style="color:	#2E8B57">Strength: {score*100/5}%</h4>', unsafe_allow_html=True)
        st.write(" Review: Hmm, using that password is like locking your front door, but leaving the key under the mat.")
    else:
        st.header("_Password_ is :red[weak]")
        st.markdown(f'<h4 style="color:	#2E8B57">Strength: {score*100/5}%</h4>', unsafe_allow_html=True)
        st.write("Review: Oops, using that password is like leaving your key in the lock.")
        
        
    if tips:
        st.subheader('''
                    ⭐ Tips to strengthen your password
                    ''')
        for tip in tips:
            st.write(tip)





