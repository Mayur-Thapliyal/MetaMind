import textwrap
from pathlib import Path
import google.generativeai as genai
from google import generativeai
GOOGLE_API_KEY="AIzaSyBJ51o9pit7RqRYCc2OiUb1k2tebHY8ktM"

genai.configure(api_key=GOOGLE_API_KEY)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content("What is the meaning of life?")
# print(response.text)
from PIL import Image 
# open method used to open different extension image file 
im = Image.open("./cake_img.jpeg")  
cookie_picture = [{
    'mime_type': 'image/jpeg',
    'data': im
}]
prompt = "Give me a recipe for this:"

response = model.generate_content(
    contents=[prompt, im]
)
print(response.text)


