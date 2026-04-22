import streamlit as st

def footer_home():

    st.markdown("""
        <div style="
            margin-top:2rem;
            display:flex;
            justify-content:center;
            align-items:center;
        ">
            <div style="
                padding:12px 28px;
                border-radius:18px;
                background:linear-gradient(135deg, #ffffff25, #ffffff10);
                backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.18);
                box-shadow:0 8px 24px rgba(0,0,0,0.18);
            ">
                <p style="
                    margin:0;
                    font-weight:700;
                    font-size:18px;
                    color:white;
                    letter-spacing:0.4px;
                ">
                    ✨ Created by Vaibhav Soni
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown("""
        <div style="
            margin-top:2rem;
            display:flex;
            justify-content:center;
            align-items:center;
        ">
            <div style="
                padding:12px 28px;
                border-radius:18px;
                background:linear-gradient(135deg, #ffffff25, #ffffff10);
                backdrop-filter:blur(12px);
                border:1px solid rgba(255,255,255,0.18);
                box-shadow:0 8px 24px rgba(0,0,0,0.18);
            ">
                <p style="
                    margin:0;
                    font-weight:700;
                    font-size:18px;
                    color:black;
                    letter-spacing:0.4px;
                ">
                    ✨ Created by Vaibhav Soni
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)