import json
from datetime import date

# خواندن اطلاعات قیمت‌ها
def load_data():
    with open("nerkh_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

# ذخیره اطلاعات قیمت‌ها
def save_data(data):
    with open("nerkh_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# نمایش قیمت‌ها
def show_prices(data):
    print("نام:", data["api_name"])
    print("آخرین بروزرسانی:", data["last_update"])
    print("واحد:", data["currency"])
    print("دلار:", data["prices"]["usd"]["price"], "تومان")
    print("بیت کوین:", data["prices"]["bitcoin"]["price"], "تومان")

# تغییر قیمت
def update_price(data, item):
    new_price = int(input("قیمت جدید را وارد کنید: "))
    data["prices"][item]["price"] = new_price

    # ثبت تاریخ بروزرسانی فقط به صورت روز
    data["last_update"] = str(date.today())

    save_data(data)
    print("قیمت با موفقیت بروزرسانی شد!")

# اجرای برنامه
data = load_data()

while True:
    print("\nNerkh API Manager")
    print("1. نمایش قیمت‌ها")
    print("2. تغییر قیمت دلار")
    print("3. تغییر قیمت بیت کوین")
    print("4. خروج")

    choice = input("انتخاب: ")

    if choice == "1":
        show_prices(data)

    elif choice == "2":
        update_price(data, "usd")

    elif choice == "3":
        update_price(data, "bitcoin")

    elif choice == "4":
        break

    else:
        print("گزینه اشتباه است!")
