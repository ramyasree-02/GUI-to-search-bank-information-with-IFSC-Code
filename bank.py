# import modules
from tkinter import *
from tkinter import messagebox
import requests

def getifsc():
	try:
		IFSC_Code = e.get()
		URL = "https://ifsc.razorpay.com/"
		result = requests.get(URL+IFSC_Code).json()
		Centre.set(result['CENTRE'])
		CITY.set(result['CITY'])
		STATE.set(result['STATE'])
		DISTRICT.set(result['DISTRICT'])
		ADDRESS.set(result['ADDRESS'])
		BRANCH.set(result['BRANCH'])
		BANKCODE.set(result['BANKCODE'])
		MICR.set(result['MICR'])
		BANK.set(result['BANK'])
		IFSC.set(result['IFSC'])
	except Exception as err:
		print(err)
		messagebox.showerror("showerror", "Something wrong")


# object of tkinter
# and background set for light grey
master = Tk()
master.title("Bank Details - by Ramya")
master.configure(bg='lavender')

# Variable Classes in tkinter
Centre = StringVar()
CITY = StringVar()
STATE = StringVar()
DISTRICT = StringVar()
ADDRESS = StringVar()
BRANCH = StringVar()
MICR = StringVar()
BANK = StringVar()
BANKCODE = StringVar()
IFSC = StringVar()


# Creating label for each information
# name using widget Label
Label(master, text="Enter IFSC Code :", bg="deep sky blue").grid(row=0, sticky=W)
Label(master, text="Bank Name :", bg="deep sky blue").grid(row=1, sticky=W)
Label(master, text="BRANCH :", bg="royalblue1").grid(row=2, sticky=W)
Label(master, text="BANKCODE :", bg="royalblue1").grid(row=3, sticky=W)
Label(master, text="Centre :", bg="deep sky blue").grid(row=4, sticky=W)
Label(master, text="CITY :", bg="deep sky blue").grid(row=5, sticky=W)
Label(master, text="STATE :", bg="royalblue1").grid(row=6, sticky=W)
Label(master, text="DISTRICT :", bg="royalblue1").grid(row=7, sticky=W)
Label(master, text="ADDRESS :", bg="deep sky blue").grid(row=8, sticky=W)
Label(master, text="MICR :", bg="deep sky blue").grid(row=9, sticky=W)
Label(master, text="IFSC :", bg="royalblue1").grid(row=10, sticky=W)


# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=BANK,
	bg="deep sky blue").grid(row=1, column=1, sticky=W)
Label(master, text="", textvariable=Centre,
	bg="royalblue1").grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=BANKCODE, 
    bg="royalblue1").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=BRANCH,
    bg="deep sky blue").grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=CITY,
	bg="deep sky blue").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=STATE,
	bg="royalblue1").grid(row=6, column=1, sticky=W)
Label(master, text="", textvariable=DISTRICT,
	bg="royalblue1").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=ADDRESS,
	bg="deep sky blue").grid(row=8, column=1, sticky=W)
Label(master, text="", textvariable=MICR, 
	bg="deep sky blue").grid(row=9, column=1, sticky=W)
Label(master, text="", textvariable=IFSC, 
	bg="royalblue1").grid(row=10, column=1, sticky=W)


e = Entry(master)
e.grid(row=0, column=1,sticky=W)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show",bg = "green", command=getifsc)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5, sticky=W)
mainloop()
