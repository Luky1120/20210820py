#조이스틱 실습
import spidev
import time

#SPI 인스턴스 spi생성
spi= spidev.SpiDev()
#라즈베리와 SPI통신 시작하기
spi.open(0,0) #open(bus, device)
#SPI 통신 속도 설정
spi.max_speed_hz=100000

#딜레이 시간(센서 측정 간격)
delay=0.5
#MCP3008 채널 중 센서에 연결한 채널 설정
sw_channel=0
vrx_channel=1
vry_channel=2

#0~7까지 8개의 채널에서 SPI데이터를 읽어 옵니다.
def readadc(adcnum):
	if adcnum > 7 or adcnum<0:
		return -1
	r=spi.xfer2([1,(8+adcnum)<<4,0])
	data=((r[1]&3)<<8)+r[2]
	return data

while True:
	sw_val=readadc(sw_channel)
	vrx_pos=readadc(vrx_channel)
	vry_pos=readadc(vry_channel)
	
	print("x : %d, y : %d, sw : %d"%(vrx_pos,vry_pos,sw_val))
	time.sleep(delay)

