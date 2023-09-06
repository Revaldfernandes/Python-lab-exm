from PyPDF2 import Pdfwriter,PdfReader
num=int(input("enter page no you want to combine from multiple document"))
Pdf1=open('program.pdf','rb')
pdf2=open('aimlsyll.pdf','rb')
pdf_writer=Pdfwriter()
pdf_reader=PdfReader(Pdf1)
page=Pdf1_Reader.pages[num-1]
wpdf_writer.add_pages[page]
Pdf2_reader=PdfReader(pdf2)
page=pdf2.reader_pages[num-1]
pdf_writer.add_pages(page)
with open('output.pdf','wb')as output:
    pdf_writer.write(output)



///////////////////////////

import json


with open('weather_data.json') as f:
    data = json.load(f)


current_temp = data['main']['temp']
humidity = data['main']['humidity']
weather_desc = data['weather'][0]['description']


print(f"Current temperature: {current_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")

JSON FILE
{
  "coord": {
    "lon": -73.99,
    "lat": 40.73
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 15.45,
    "feels_like": 12.74,
    "temp_min": 14.44,
    "temp_max": 16.11,
    "pressure": 1017,
    "humidity": 64
  },
  "visibility": 10000,
  "wind": {
    "speed": 4.63,
    "deg": 180
  },
  "clouds": {
    "all": 1
  },
  "dt": 1617979985,
  "sys": {
    "type": 1,
    "id": 5141,
    "country": "US",
    "sunrise": 1617951158,
    "sunset": 1618000213
  },
  "timezone": -14400,
  "id": 5128581,
  "name": "New York",
  "cod": 200
}
