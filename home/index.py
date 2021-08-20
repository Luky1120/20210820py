from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

#자기 자신의 파일명으로 객체 생성
app=Flask(__name__)

LED=8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)

#클라이언트가 URI로 "/"를 요청하면 아래있는 뷰함수가 자동 호출
@app.route("/")
def helloworld():
    return render_template("index.html")

@app.route("/led/on")
def led_on():
    try:
        GPIO.output(8,GPIO.HIGH)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(8,GPIO.LOW)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"

#자신의 파일을 직접 실행시켜 app.run()를 호출, 서버 실행
if __name__ =="__main__":
    app.run(host="0.0.0.0")