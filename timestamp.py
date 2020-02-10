from time import sleep,time,strftime,localtime
def timestamp():
    style="%a %I:%M:%S %p"
    return strftime(style,localtime(time()))
