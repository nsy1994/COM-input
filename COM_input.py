# -*- coding:utf-8 -*-

import time
import serial  # 串口通信
import pyperclip # 复制粘贴
from pykeyboard import PyKeyboard  # 模拟键盘

def rec(serial):
    while True:
        data = serial.readall()
        if data == '':
            continue
        else:
            break
        time.sleep(0.02)
    return data  
   
if __name__ == '__main__':
    s = input('请输入COM口号：')  
    try:
        serial = serial.Serial('COM' + s, 115200, timeout=0.5)
        print('\nCOM' + s + '口连接成功！')
        while True:
            data =rec(serial)
            if data != b'' :
                try:
                    data = data.decode('utf-8')
                except:
                    data = data.decode('gbk')
                data = data.split()
                for d in data:
                    pyperclip.copy(d)              # 复制串口上接收到数据
                    k = PyKeyboard()                       # 实例化虚拟键盘
                    k.press_keys([k.control_key, 'v'])     # 模拟键盘按ctrl+v键
                    time.sleep(0.05)
                    k.press_key(k.enter_key)      # 模拟键盘回车
                
    except:
        print('\n串口号错误！\n')
        time.sleep(20)
						