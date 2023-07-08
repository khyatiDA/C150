from tkinter import*
import random
window = Tk()

window.title("country capital")
window.geometry("600x600")
window.config(background="SandyBrown")

inputbox1= Entry(window)
inputbox1.place(relx = 0.5 , rely = 0.2 , anchor = CENTER)

inputbox2 = Entry(window)
inputbox2.place(relx = 0.5 , rely = 0.3, anchor = CENTER)


label_countryName = Label(window)
label_countryName.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)


label_cityName = Label(window)
label_cityName.place(relx = 0.5 , rely = 0.6, anchor = CENTER)


label_country_random = Label(window)
label_country_random.place(relx = 0.5 , rely = 0.8, anchor = CENTER)

label_countryList = Label(window)
label_countryList.place(relx = 0.5 , rely = 0.8, anchor = CENTER)

label_cityList = Label(window)
label_cityList.place(relx = 0.5 , rely = 0.8, anchor = CENTER)


label_city_random = Label(window)
label_city_random.place(relx = 0.5 , rely = 0.9 , anchor = CENTER)

countryList = []
cityList = []

def input():
    country = label_countryName.get()
    countryList.append(country)
    label_countryList["text"]="Country Name :" + str(countryList)

    city = label_cityName.get()
    cityList.append(city)
    label_cityList["text"]="Country Name :" + str(cityList)

def random1():
    length = len(countryList)
    random_number = random.randint(0 , length - 1)
    label_country_random['text'] = str(random_number)
    
    length = len(cityList)
    random_number = random.randint(0 , length - 1)
    label_city_random['text'] = str(random_number)


btn = Button(window , text = "Display Country And Capital Name" , command =input )   
btn.place(relx = 0.5 , rely = 0.4, anchor = CENTER)

btn = Button(window , text = "Display Country And City Name Randomly" , command =random1 )   
btn.place(relx = 0.5 , rely = 0.7, anchor = CENTER)
   
    

window.mainloop()


