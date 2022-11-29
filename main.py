import streamlit as st
import io
from PIL import Image, ImageDraw, ImageFont


st.set_page_config(page_title="Lexicon Certification", page_icon=None,
                   layout="centered", initial_sidebar_state="collapsed", menu_items=None)


background = Image.open("./banner.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=True)


names = [
    "Adarsh Pandey",
    "Saiteja Kusuma",
    "Lakkakula Lavanya",
    "Aluvala Naga Vinay",
    "Kadiyam Bhavajeet",
    "Sneha Vellelath",
    "Nemaliga Rohith",
    "Muthineni Saketh",
    "Rishika katta",
    "Sasmita reddy",
    "Jamalpur Rashmitha",
    "Sri harini",
    "Kethireddy.Dhanushya",
    "Jarupula Indhu Priya",
    "P. Saranya",
    "Kiranmai",
    "Nithya Reddy",
    "Sruthi masuram",
    "Gogula Likhitha",
    "Pattapu keerthi",
    "PEDDA GOLLA GANESH",
    "B.Arshitha",
    "G.GLORY",
    "PEDDAKOTLA RAHUL",
    "Singaraju Nikhil",
    "ROHIT KUMAR",
    "GODA DEEPIKA",
    "Ch.Daalivardhan",
    "D karthikeya",
    "Gande saikiran",
    "Vuthunoori Rahul",
    "M.Swathi",
    "GAMPA SRUJANKUMAR",
    "Pulukanti Laxmi Deepak",
    "Motapalukula Manoj",
    "Ganesh Rathod",
    "R.SAI THARUN REDDY",
    "A S Deekshitha",
    "Raghu Ghanapuram",
    "Ujjwal Shivacharya",
    "Syed Ikram",
    "Engari sripadha Reddy",
    "Ajith krishna",
    "pavan",
    "Marrapu Jaswanth",
    "Vemula Saikrishna",
    "Mahesh Ratnaparkhe",
    "Sai Raj",
    "E.Sankeerth",
    "K. Sanith Kumar",
    "Gummadi sai kiran",
    "G.Sai tharun",
    "S. Javahar reddy",
    "T. BHANU PRASAD",
    "Sri Vishal Lanka",
    "B. Sai Teja",
    "NALAMALAPU SATISH REDDY",
    "P.venkata ganesh",
    "Mallela Abhinaya",
    "Mohd Ateeq Ur Rahman",
    "Mannem divya",
    "Nadella Vishnu Sai",
    "Adithya Rao",
    "Naveesh Odela",
    "MD ABRAR AHMED",
    "Shivani Gajula",
    "Tanniru karthik",
    "Allaboina Reshma",
    "P.Gopi nath",
    "Giriboina Shivani Devi",
    "VEGGALAM GNANESHWAR",
    "B Ankitha",
    "Y. Rohith",
    "Lokesh",
    "K Lalitha Aradhini",
    "M Kundan Sai",
    "RACHA NIKHIL",
    "Ch Supriya",
    "B Rishi Raj",
    "A KRISHNA SAI NITHIN",
    "Gummadi Dushyanth",
    "G Harshitha Sri Sai",
    "Akkati Sreeja",
    "T J V S NAGARJUNA",
    "TALARI ANUSHA",
    "Srisuma kurapati",
    "A Jahnavi madhu lavanya",
    "K NANDI VARDHAN REDDY",
    "Sree Harshita",
    "Amuktha Kotamsetty",
    "Goutham Earaboina",
    "Musham prashanthi",
    "K.sreedevi",
    "Shravani",
    "Saimaniteja",
    "MINKOORI RITESH KUMAR",
    "K.Santosh",
    "K. Harshitha",
    "N. Shirisha",
    "S. Karthik",
    "G.Parthiv Kumar",
    "Rahul Vamsi",
    "I. Nithin",
    "G. Bhupal"
  ]


PATH = "./template.png"


font = ImageFont.truetype("Lora-VariableFont_wght.ttf", 80)
name = st.selectbox("Search your name to get the certificate", names)
name = name.title()
im = Image.open(PATH)
d = ImageDraw.Draw(im)

W, H = im.size
w, h = d.textsize(name, font=font)
print(w, h)
d.text(((((W-w)/2), ((H - h)/2 +100))),
       name, fill=(30, 102, 126), font=font)
if st.button("Get Certificate"):
    ioData = io.BytesIO()
    im.save(ioData, format='PNG', quality='keep')
    finalImage = ioData.getvalue()
    st.image(finalImage)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    '''<br><br><div style="text-align: center"><small> GDSC IARE Tech | November 2022 </small></div>''', unsafe_allow_html=True)

