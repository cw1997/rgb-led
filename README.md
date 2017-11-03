# rgb-led
一个共阳极RGB LED的调色器，使用jscolor进行网页选色，然后实时通过Websocket传输到后端python脚本中，脚本通过GPIO的PWM脉宽调制实现对RGB亮度的控制，最终混合出制定颜色。

# 注意事项
- 使用之前请正确修改websocket.py和index.html里面的各项参数，包括监听端口，IP地址以及RGB LED的GPIO针脚（使用wPi针脚命名，具体请在shell下执行gpio readall查询物理针脚对应的wPi针脚）。
- rgb.py只适用于共阳极RGB发光二极管，如果是共阴极，请重写该模块。
