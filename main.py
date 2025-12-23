import streamlit as st

# Page configuration
st.set_page_config(
    page_title="श्रीनाथ नागरिक सहकारी बँक",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #d4145a 0%, #fbb034 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .bank-title {
        color: white;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .tagline {
        color: white;
        text-align: center;
        font-size: 18px;
        margin-top: 10px;
    }
    .service-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
        border-left: 5px solid #d4145a;
    }
    .feature-box {
        background: linear-gradient(135deg, #fff5e6 0%, #ffe6e6 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    .contact-info {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header with logo
col1, col2, col3 = st.columns([1, 6, 1])
with col3:
    st.markdown("### 🏦")  # Logo placeholder - you can replace with actual logo using st.image()

with col2:
    st.markdown("""
        <div class="main-header">
            <h1 class="bank-title">क्रांती नागरिक सहकारी बँक</h1>
            <p class="tagline">तुमच्या विश्वासाचं बँक | Your Trusted Banking Partner</p>
        </div>
    """, unsafe_allow_html=True)

# Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 मुख्यपृष्ठ", "💼 सेवा", "📊 व्याजदर", "ℹ️ माहिती", "📞 संपर्क"])

with tab1:
    st.markdown("## आमच्याबद्दल")
    st.write("""
    क्रांती नागरिक सहकारी बँक ही एक विश्वासार्ह आणि ग्राहकोन्मुख बँक आहे. 
    आम्ही तुमच्या आर्थिक गरजा पूर्ण करण्यासाठी विविध बँकिंग सेवा पुरवतो.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-box">
                <h3>💰 सुरक्षित ठेवी</h3>
                <p>तुमची बचत सुरक्षित ठेवा आणि चांगला व्याज मिळवा</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-box">
                <h3>🏠 कर्ज सुविधा</h3>
                <p>गृहकर्ज, वाहन कर्ज आणि वैयक्तिक कर्ज</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-box">
                <h3>📱 डिजिटल बँकिंग</h3>
                <p>ऑनलाईन बँकिंग सुविधा</p>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("## आमच्या सेवा")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="service-card">
                <h3>💵 बचत खाते</h3>
                <ul>
                    <li>नियमित बचत खाते</li>
                    <li>चालू खाते</li>
                    <li>मुदत ठेव योजना</li>
                    <li>आवर्ती ठेव योजना</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="service-card">
                <h3>🏦 कर्ज सुविधा</h3>
                <ul>
                    <li>गृहकर्ज</li>
                    <li>वाहन कर्ज</li>
                    <li>वैयक्तिक कर्ज</li>
                    <li>व्यवसाय कर्ज</li>
                    <li>शेती कर्ज</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="service-card">
                <h3>💳 अन्य सुविधा</h3>
                <ul>
                    <li>एटीएम / डेबिट कार्ड</li>
                    <li>मोबाइल बँकिंग</li>
                    <li>इंटरनेट बँकिंग</li>
                    <li>लॉकर सुविधा</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="service-card">
                <h3>📄 विमा योजना</h3>
                <ul>
                    <li>जीवन विमा</li>
                    <li>आरोग्य विमा</li>
                    <li>वाहन विमा</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("## व्याजदर")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ठेवींवरील व्याजदर")
        st.markdown("""
            <div class="service-card">
                <table style="width:100%">
                    <tr>
                        <th>ठेव प्रकार</th>
                        <th>व्याजदर (%)</th>
                    </tr>
                    <tr>
                        <td>बचत खाते</td>
                        <td>4.00%</td>
                    </tr>
                    <tr>
                        <td>मुदत ठेव (1 वर्ष)</td>
                        <td>6.50%</td>
                    </tr>
                    <tr>
                        <td>मुदत ठेव (2-3 वर्षे)</td>
                        <td>7.00%</td>
                    </tr>
                    <tr>
                        <td>आवर्ती ठेव</td>
                        <td>6.75%</td>
                    </tr>
                </table>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### कर्जावरील व्याजदर")
        st.markdown("""
            <div class="service-card">
                <table style="width:100%">
                    <tr>
                        <th>कर्ज प्रकार</th>
                        <th>व्याजदर (%)</th>
                    </tr>
                    <tr>
                        <td>गृहकर्ज</td>
                        <td>8.50%</td>
                    </tr>
                    <tr>
                        <td>वाहन कर्ज</td>
                        <td>9.00%</td>
                    </tr>
                    <tr>
                        <td>वैयक्तिक कर्ज</td>
                        <td>11.00%</td>
                    </tr>
                    <tr>
                        <td>शेती कर्ज</td>
                        <td>7.00%</td>
                    </tr>
                </table>
            </div>
        """, unsafe_allow_html=True)
    
    st.info("📌 व्याजदर बदलण्याच्या अधीन आहेत. कृपया नवीनतम दरांसाठी बँकेशी संपर्क साधा.")

with tab4:
    st.markdown("## बँकेची माहिती")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="service-card">
                <h3>आमची बाब</h3>
                <p>आम्ही प्रामाणिक, पारदर्शक आणि ग्राहकोन्मुख सेवा पुरवण्यास वचनबद्ध आहोत.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="service-card">
                <h3>कार्यवेळ</h3>
                <p><strong>सोमवार - शुक्रवार:</strong> सकाळी 10:00 ते संध्याकाळी 5:00</p>
                <p><strong>शनिवार:</strong> सकाळी 10:00 ते दुपारी 2:00</p>
                <p><strong>रविवार:</strong> बंद</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="service-card">
                <h3>महत्वाच्या सूचना</h3>
                <ul>
                    <li>खाते उघडण्यासाठी KYC कागदपत्रे आवश्यक</li>
                    <li>मुदत ठेवींवर कर्ज सुविधा उपलब्ध</li>
                    <li>नामांकन सुविधा अनिवार्य</li>
                    <li>व्याजदर त्रैमासिक संयुक्त</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("## आमच्याशी संपर्क साधा")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="contact-info">
                <h3>📍 पत्ता</h3>
                <p>क्रांती नागरिक सहकारी बँक<br>
                मुख्य शाखा<br>
                [तुमचा पत्ता येथे टाका]<br>
                महाराष्ट्र, भारत</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="contact-info">
                <h3>📞 संपर्क</h3>
                <p><strong>फोन:</strong> +91-XXXXXXXXXX<br>
                <strong>ईमेल:</strong> info@krantibank.com<br>
                <strong>वेबसाइट:</strong> www.krantibank.com</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📝 चौकशी फॉर्म")
        with st.form("contact_form"):
            name = st.text_input("नाव")
            phone = st.text_input("फोन नंबर")
            email = st.text_input("ईमेल")
            message = st.text_area("संदेश")
            
            submitted = st.form_submit_button("पाठवा")
            if submitted:
                st.success("धन्यवाद! आम्ही लवकरच तुमच्याशी संपर्क साधू.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>© 2024 क्रांती नागरिक सहकारी बँक. सर्व हक्क राखीव.</p>
        <p>RBI परवानगी क्रमांक: XXXXX | DICGC विमा</p>
    </div>
""", unsafe_allow_html=True)
