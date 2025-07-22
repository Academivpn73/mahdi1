#!/data/data/com.termux/files/usr/bin/bash

echo "📢 @Academii73 | SMS Bomber Installer for Termux"

# نصب پیش‌نیازها
pkg update -y && pkg install python -y
pip install requests --quiet

# دانلود و اجرای فایل اصلی
curl -fsSL https://raw.githubusercontent.com/Academivpn73/mahdi1/main/mah.py -o mah.py
python mah.py
