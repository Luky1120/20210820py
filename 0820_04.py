#OLED디스플레이에 표시 실습
import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw,ImageFont
import Adafruit_BMP.BMP085 as BMP085

#OLED 128*64(i2c_address=연결된 OLED주소) 인스턴스 disp생성
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

disp.begin()
disp.clear()
disp.display()

#OLED의 크기를 가져와 draw객체에 image인스턴스를 그려준다.
width=disp.width
height=disp.height
image=Image.new("1",(width,height))

draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0,fill=0)

padding=-2
top=padding
bottom=height-padding
x=0
font=ImageFont.load_default()

#BMP180센서의 인스턴스 생성
sensor=BMP085.BMP085()

while True:
	temp=sensor.read_temperature()
	pressure=sensor.read_pressure()
	altitude=sensor.read_altitude()
	
	#측정값 출력(터미널)
	print("Temp={0:0.2f}*C".format(temp))
	print("Pressure={0:0.2f} Pa".format(pressure))
	print("Al.Titude={0:0.2f} m".format(altitude))
	
	#draw객체에 텍스트를 그려준다.
	draw.text((x,top),"Temp={0:0.2f}*C".format(temp), font=font, fill=255)
	draw.text((x,top+8),"Pressure={0:0.2f} Pa".format(pressure), font=font, fill=255)
	draw.text((x,top+16),"Al.Titude={0:0.2f} m".format(altitude), font=font, fill=255)
	
	#OLED에 화면표시
	disp.image(image)
	disp.display()
	
	#딜레이 2초
	time.sleep(2)
