import requests
from tkinter import *

window = Tk()
window.geometry('250x200')
label = Label(text="HOW MUCH KM : ")
label.grid(column=0, row=0)
entry = Entry(width=20)
entry.grid(column=1, row=0)
entry.focus()
from datetime import datetime

# para = {
#     "token":"Pukale@123", "username":"shreekantsuhas", "agreeTermsOfService":"yes", "notMinor":"yes"
# }
# response = requests.post(url="https://pixe.la/v1/users", json=para)
# print(response.text)

# 2
para = {
    "id": "ashree", "name": "shree", "unit": "km", "type": "float", "color": "shibafu"
}
head = {
    'X-USER-TOKEN': 'Pukale@123'
}


# response = requests.post(url="https://pixe.la/v1/users/shreekantsuhas/graphs", json=para, headers=head)
# print(response.text)

# 3
def submit():
    now = datetime.now().date()
    distance = entry.get()
    j = {
        "date": now.strftime('%Y%m%d'),
        "quantity": distance
    }
    response = requests.post(url="https://pixe.la/v1/users/shreekantsuhas/graphs/ashree", headers=head, json=j)
    print(response.text)


button = Button(text="SUBMIT", command=submit)
button.grid(column=1, row=1)

window.mainloop()
