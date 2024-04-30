import requests
import json
from PIL import Image, ImageFont, ImageDraw 
from datetime import date

api_key = "f1f8c75b410e75c455b5d3132d0e14c6" #Update Your API Here
position = [300, 430, 555, 690, 825]

uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham"]
india_list = ["Nellore", "Delhi", "Mumbai", "jaipur", "Chennai"]
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
country_list = [uk_list, india_list, us_list]

for country in country_list:
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=50)
    content = "Latest Weather Forecast"
    color = 'rgb(255, 255, 255)'
    (x, y) = (50,50)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=30)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255, 255, 255)' 
    (x, y) = (55,145)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
 
        font = ImageFont.truetype('Inter.ttf', size=50)
        content= "City name"
        color = 'rgb(0, 0, 0)'
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255, 255, 255)'
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255, 255, 255)'
        (x, y) = (820, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1
        
    # image.save(str(date.today()) + country[0] + ".png")
    # image_pdf = image.convert('RGB')
    # image_pdf.save(str(date.today()) + country[0] + ".pdf")
