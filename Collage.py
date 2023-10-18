import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import base64

st.title("Collage")

st.sidebar.header("Upload Images")
uploaded_images = st.sidebar.file_uploader("Upload Images for your collage",type=["jpg","png"],accept_multiple_files=True)

st.sidebar.header("Add Text")
text_input = st.sidebar.text_input("Enter text for your collage")

text_color = st.sidebar.color_picker("Text color","#ffffff")

st.subheader("Your Collage")

collage = st.empty()

def create_collage(images,text,color):
    num_cols = 3
    collage_width = 800
    image_width = collage_width//num_cols
    image_height= image_width
    collage_image = Image.new("RGB",(collage_width,image_height * ((len(images)-1)//num_cols + 1)))
    
    for i, image in enumerate(images):
        x = (i% num_cols)* image_width
        y = (i// num_cols)* image_height
        image = image.resize((image_width,image_height))
        collage_image.paste(image,(x,y))
    
    draw = ImageDraw.Draw(collage_image)
    font = ImageFont.load_default()
    x,y = 10,10
    draw.text((x,y),text,fill=color,font= font)
    
    collage_bytes = io.BytesIO()
    collage_image.save(collage_bytes,format = "PNG")
    return collage_image

if st.sidebar.button("Generate Collage"):
    images = [Image.open(image) for image in uploaded_images if image is not None]
    collage_text = text_input 
    collage_color = text_color
    collage_image = create_collage(images,collage_text,collage_color)
    collage.image(collage_image)
    
    