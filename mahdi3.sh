#!/data/data/com.termux/files/usr/bin/bash

echo "📢 @Academii73 | SMS Bomber Installer for Termux"

# نصب پیش‌نیازها
pkg update -y && pkg install python -y
pip install requests --quiet

# دانلود فایل پایتون
curl -fsSL https://raw.githubusercontent.com/Academivpn73/mahdi1/main/mahdi2.py -o mahdi2.py

# بررسی وجود فایل
if [ ! -f "mahdi2.py" ]; then
    echo "⛔ فایل mahdi2.py پیدا نشد! لینک رو بررسی کن."
    exit 1
fi

# اجرا
python3 mahdi2.py
