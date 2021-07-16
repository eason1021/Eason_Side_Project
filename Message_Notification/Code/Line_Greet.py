import sys #Adding parameter
import requests #Line notify requests
import datetime #Catch the time
from pathlib import Path #Get the file path
from LunarSolarConverter import LunarSolarConverter #Transform Solar calendar to Lunar calendar
import random #Random pick picture

stat = sys.argv[1]
HBD = ['4-1', '8-7','10-21']
year = int(datetime.datetime.now().strftime('%Y'))
month = int(datetime.datetime.now().strftime('%m'))
day = int(datetime.datetime.now().strftime('%d'))
#token = 'e7988bsdlLb9uWEIXzMekiDo3eEATPNlQUcxrjoJF45'
token = 'ghhkqN68IH0wtvIYXjGTsSMmzBtPjb9eMQeTC0nQzgY'

def Gwawa_Greet(stat, year, month, day):
    if stat == 'Morning':
        image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/Morning').glob('*.png'))
        rand_num = random.randint(0, len(image) - 1)
        message = '早安，我的好友。'
        image = image[rand_num]
        return message, image
    elif stat == 'Noon':
        image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/Noon').glob('*.png'))
        rand_num = random.randint(0, len(image) - 1)
        image = image[rand_num]
        message = '中午好，記得吃午餐哦!'
        return message, image
    elif stat == 'Night':
        image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/Night').glob('*.png'))
        rand_num = random.randint(0, len(image) - 1)
        image = image[rand_num]
        message = '晚上好，記得休息呦。'
        return message, image
    elif stat == 'Concern':
        image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/Concern').glob('*.png'))
        rand_num = random.randint(0, len(image) - 1)
        image = image[rand_num]
        message = '認同請分享'
        return message, image
    elif stat == 'Festival':
        converter = LunarSolarConverter.LunarSolarConverter()
        solar = LunarSolarConverter.Solar(year, month, day)
        lunar = vars(converter.SolarToLunar(solar))
        lunarMonth = lunar['lunarMonth']
        lunarDay = lunar['lunarDay']
        #Solar
        if month == 1 and day == 1:
            image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/NewYear').glob('*.png'))
            rand_num = random.randint(0, len(image) - 1)
            image = image[rand_num]
            message = '新年快樂'
            return message, image
        elif day == 14:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            image = '/home/eason/文件/Code_space/Gwawa/Image/Val.png'
            message = '情人節快樂'
            return message, image
        elif month == 4 and day == 4:
            image = '/home/eason/文件/Code_space/Gwawa/Image/Kid.png'
            message = '兒童節快樂'
            return message, image
        elif month == 10 and day == 10:
            image = '/home/eason/文件/Code_space/Gwawa/Image/Double_ten.png'
            message = '國慶日快樂'
            return message, image
        elif month == 12 and day == 25:
            image = '/home/eason/文件/Code_space/Gwawa/Image/Merry.png'
=======
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Val.png'
            message = '情人節快樂'
            return message, image
        elif month == 4 and day == 4:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Kid.png'
            message = '兒童節快樂'
            return message, image
        elif month == 10 and day == 10:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Double_ten.png'
            message = '國慶日快樂'
            return message, image
        elif month == 12 and day == 25:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Merry.png'
>>>>>>> ee0c6836a07c869e756bfcd3d05d3d546a4084dd
=======
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Val.png'
            message = '情人節快樂'
            return message, image
        elif month == 4 and day == 4:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Kid.png'
            message = '兒童節快樂'
            return message, image
        elif month == 10 and day == 10:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Double_ten.png'
            message = '國慶日快樂'
            return message, image
        elif month == 12 and day == 25:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Merry.png'
>>>>>>> ee0c6836a07c869e756bfcd3d05d3d546a4084dd
=======
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Val.png'
            message = '情人節快樂'
            return message, image
        elif month == 4 and day == 4:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Kid.png'
            message = '兒童節快樂'
            return message, image
        elif month == 10 and day == 10:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Double_ten.png'
            message = '國慶日快樂'
            return message, image
        elif month == 12 and day == 25:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Merry.png'
>>>>>>> ee0c6836a07c869e756bfcd3d05d3d546a4084dd
            message = '聖誕快樂'
            return message, image
        #Lunar
        elif lunarMonth == 1 and lunarDay == 1:
            image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/NewYear').glob('*.png'))
            rand_num = random.randint(0, len(image) - 1)
            image = image[rand_num]
            message = '新年快樂'
            return message, image
        elif lunarMonth == 1 and lunarDay == 15:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            image = '/home/eason/文件/Code_space/Gwawa/Image/Lantern.png'
            message = '元宵節快樂，記得吃花生湯圓哦'
            return message, image
        elif lunarMonth == 5 and lunarDay == 5:
            image = '/home/eason/文件/Code_space/Gwawa/Image/Dragon.png'
            message = '端午節快樂，南部粽好吃'
            return message, image
        elif lunarMonth == 7 and lunarDay == 7:
            image = '/home/eason/文件/Code_space/Gwawa/Image/Double_seven.png'
            message = '七夕快樂'
            return message, image
        elif lunarMonth == 8 and lunarDay == 15:
            image = '/home/eason/文件/Code_space/Gwawa/Image/Moon.png'
=======
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Lantern.png'
            message = '元宵節快樂，記得吃花生湯圓哦'
            return message, image
        elif lunarMonth == 5 and lunarDay == 5:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Dragon.png'
            message = '端午節快樂，南部粽好吃'
            return message, image
        elif lunarMonth == 7 and lunarDay == 7:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Double_seven.png'
            message = '七夕快樂'
            return message, image
        elif lunarMonth == 8 and lunarDay == 15:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Moon.png'
>>>>>>> ee0c6836a07c869e756bfcd3d05d3d546a4084dd
=======
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Lantern.png'
            message = '元宵節快樂，記得吃花生湯圓哦'
            return message, image
        elif lunarMonth == 5 and lunarDay == 5:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Dragon.png'
            message = '端午節快樂，南部粽好吃'
            return message, image
        elif lunarMonth == 7 and lunarDay == 7:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Double_seven.png'
            message = '七夕快樂'
            return message, image
        elif lunarMonth == 8 and lunarDay == 15:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Moon.png'
>>>>>>> ee0c6836a07c869e756bfcd3d05d3d546a4084dd
=======
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Lantern.png'
            message = '元宵節快樂，記得吃花生湯圓哦'
            return message, image
        elif lunarMonth == 5 and lunarDay == 5:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Dragon.png'
            message = '端午節快樂，南部粽好吃'
            return message, image
        elif lunarMonth == 7 and lunarDay == 7:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Double_seven.png'
            message = '七夕快樂'
            return message, image
        elif lunarMonth == 8 and lunarDay == 15:
            image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Moon.png'
>>>>>>> ee0c6836a07c869e756bfcd3d05d3d546a4084dd
            message = '中秋節快樂，烤肉烤肉'
            return message, image
        else :
            return False, False
    elif stat == 'Mom':
        image = '/Users/yiming/Documents/Code_space/Gwawa/Image/Festival/Mom.png'
        message = '母親節快樂'
        return message, image
    elif stat == 'HBD':
        date = str(month) + '-' + str(day)
        if date in HBD:
            image = list(Path('/home/eason/文件/Code_space/Gwawa/Image/HBD').glob('*.png'))
            rand_num = random.randint(0, len(image) - 1)
            image = image[rand_num]
            message = '生日快樂'
            return message, image
        else :
            return False, False

def Line_Notify(token, message, img):
    headers = {"Authorization": "Bearer " + token}
    param = {'message': message}
    image = {'imageFile' : open(str(img), 'rb')}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = param, files = image)
    return r.status_code

message, image = Gwawa_Greet(stat, year, month, day)

if message != False :
    Line_Notify(token, message, image)