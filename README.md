# rgb-led
一个共阳极RGB LED的调色器，使用jscolor进行网页选色，然后实时通过Websocket传输到后端python脚本中，脚本通过GPIO的PWM脉宽调制实现对RGB亮度的控制，最终混合出制定颜色。
