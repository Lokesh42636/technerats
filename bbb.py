from datetime import date,datetime
from gtts import gTTS
import os
items={"056044006034":{"name":"Lays","price":10,"date1":"2022,3,21"},
            "8901491502030":{"name":"Lays green","price":10,"date1":"2023,7,21"},
            "8901491502047":{"name":"Lays red","price":10,"date1":"2023,3,21"},
            }
total=0
bill=[]
date2=date.today()
while True:
        print("scan your barcode")
        value=input()
        end_code="9781492090793"
        if value==end_code:
            print("shopping done")
            break
        for key in items.keys():
            if key==value:
                item=items[key]
                d=item['date1']
                list=[i for i in map(int,d.split(','))]
                date4=datetime.strptime(d, '%Y,%m,%d').date()
                n=(date4-date2).days
                if n<=0 or n<=5:
                    mytext = "This product is expired"
                    language = "en"
                    b = gTTS(text=mytext, lang=language, slow=False)
                    b.save("cc1.mp3")
                    os.system("start cc1.mp3")
                    break
                else:
                    print(f"this is:{item['name']},price is:{item['price']}")
                    total+=item['price']
                    bill.append(item)
                    break
        else:
            print("item not found",value)
print("Sno  item  price  date1")
for i , item in enumerate(bill):
    print(f"{i}  {item[ 'name' ]}  {item[ 'price' ]}  {item[ 'date1' ]}")
print(f'\nyour total cost is :Rs.{total}')
