## COM口数据转input
##### 将COM口获取到的数据转化成键盘input输入，主要为了解决接口为COM口的扫码枪扫描中文乱码的问题
***
监听COM口，获取全部byte数据，将其转化为utf-8或者gbk中文输出到鼠标光标输入处

环境：
+ Python 3.4

依赖：
+ pywin32
+ pyserial 2.7
+ pyperclip
+ pykeyboard  模拟键盘操作
+ pyinstaller 打包.exe可执行程序
