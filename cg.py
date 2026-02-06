import datetime
def year():
    today=datetime.date.today()
    print(today.year)
    name=input("Enter your name")
    address=input("Enter your address")
    year=int(input("Enter your year"))

    age=today.year-year
    if(age>=18):
        print("eligible")
    else:
        print("NOt eligible")
year()




