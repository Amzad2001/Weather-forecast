import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date 


api_key = "f1f8c75b410e75c455b5d3132d0e14c6"
position = [300, 430, 555, 690, 825]

# uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham"]
# us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
india_list = ["Nellore", "Delhi", "Mumbai", "jaipur", "Chennai"]
country_list=[india_list]
for country in country_list:
    image = Image.open("post.png")
    draw= ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=50)
    content = "Latest weather report"
    color = 'rgb(255,255,255)'
    (x,y) = (50,50) 

    draw.text((x,y),content,color, font=font)

    font = ImageFont.truetype('inter.ttf',size=50)
    content = date.today().strftime("%A - %B %d, %y")
    color = 'rgb(255,255,255)'
    (x,y) = (50,135)
    draw.text((x,y),content,color ,font=font)
    index=0
    for city in country:
         url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
         response = requests.get(url)
         data = json.loads(response.text)
        #  print(data)

         font = ImageFont.truetype('inter.ttf',size=50)
         content = 'city'
         color= 'rgb(0,0,0)'
         (x, y) = (135, position[index])
         draw.text((x, y), city, color, font = font) 

         font = ImageFont.truetype('inter.ttf', size= 50)
         content = str(data['main']['temp']) + "\u00b0"
         color = 'rgb(255,255,255)'
         (x, y) = (600,position[index])
         draw.text((x, y),content,color,font = font)

         font = ImageFont.truetype('inter.ttf', size =50)
         content = str(data['main']['humidity']) + "%"
         color= 'rgb(255,255,255)'
         (x,y) = (800, position[index])
         draw.text((x,y),content,color,font = font)


         index+=1
    
    # image.show(str(date.today()) + country[0] + ".png")




    image.save(str(date.today()) + country[0] + ".png")
    image_pdf = image.convert("RGB")
    image_pdf.save(str(date.today()) + country[0]+ ".pdf")



# response = requests.get(url)
# data = json.loads(response.text)
# print(data)

# image = Image.open("post.png")
# draw = ImageDraw.Draw(image)

# font = ImageFont.truetype('Inter.ttf',size=50)
# content = "latest weather forecast"
# color = 'rgb(255, 255,255)'
# draw.text((55,50), content, color, font= font)
# image.save("test.png ")