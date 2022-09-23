import os
import platform

# pipreqs . --encoding=utf8 --force
# os.system("pip install -r requirements.txt")

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

ip = "0." * 4

if platform.system() != "Linux":
    os.system("python manage.py runserver")
else:
    # 重定向输出与重定向错误输出，且log.log不同于log.txt
    os.system("python manage.py runserver " + ip[:-1] + ":8000 >> log.log 2>&1 & \n")
    print("The backend is running!")