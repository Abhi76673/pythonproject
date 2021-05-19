from tkinter import *
root = Tk()
root.geometry("1350x700+0+0")

def getvals():


    print("Accepted")
# Headind
Label(root , text="Covid_19 vaccine Regration Form" , font="arial 44 bold" ,fg="red" ).grid(row=0, column=2)

# Sub Heading

Label(root, text="covid_19 vaccine purchase", font="arial 24 bold", fg="orange").grid(row=1 ,column=1)

Label(root, text="If you purchase get fast free Home Delivery" , font="arial 18 bold", fg="black").grid(row=2, column=2)

Label(root, text="covid_19 vaccine JUST INR ₹18 ",font="arial 38 bold ",fg="green").grid(row=12,column=2)

# Field Name
name =Label(root, text="Name", font="arial 10 bold")

father_name =Label(root, text="Father_Name", font="arial 10 bold")
mother_name =Label(root, text="Mother_Name", font="arial 10 bold")
age =Label(root, text="Age", font="arial 10 bold")
gender =Label(root, text="Gender", font="arial 10 bold")
address =Label(root, text="Address", font="arial 10 bold")
aadhar_no=Label(root, text="Aadhar_No", font="arial 10 bold")
phone_no =Label(root, text="Phone_No", font="arial 10 bold")
emergency =Label(root, text="Emergency", font="arial 10 bold", fg="blue")
paymentmode=Label(root, text="Paymentmode", font="arial 10 bold")



# Packing Fields
name.grid(row=40, column=1)
father_name.grid(row=41, column=1)
mother_name.grid(row=42, column=1)
age.grid(row=43, column=1)
gender.grid(row=44, column=1)
address.grid(row=45, column=1)
aadhar_no.grid(row=46, column=1)
phone_no.grid(row=47, column=1)
emergency.grid(row=48, column=1)
paymentmode.grid(row=49, column=1)


# Variable for storing Data
namevalue =StringVar
father_namevalue =StringVar
mother_namevalue =StringVar
agevalue =StringVar
gendervalue =StringVar
addressvalue =StringVar
aadhar_novalue =StringVar
phone_novalue =StringVar
emergencyvalue =StringVar
paymentmodevalue =StringVar
checkvalue =IntVar


# Creating entry fields
nameentry =Entry(root, textvariable =namevalue)
father_nameentry =Entry(root, textvariable =father_namevalue)
mother_nameentry =Entry(root, textvariable =mother_namevalue)
ageentry =Entry(root, textvariable =agevalue)
genderentry =Entry(root, textvariable =gendervalue)
addressentry =Entry(root, textvariable =addressvalue)
aadhar_noentry =Entry(root, textvariable =aadhar_novalue)
phone_noentry =Entry(root, textvariable =phone_novalue)
emergencyentry =Entry(root, textvariable =emergencyvalue)
paymentmodeentry =Entry(root, textvariable =paymentmodevalue)


# Packing entry fields
nameentry.grid(row=40, column=2)
father_nameentry.grid(row=41, column=2)
mother_nameentry.grid(row=42, column=2)
ageentry.grid(row=43, column=2)
genderentry.grid(row=44, column=2)
addressentry.grid(row=45, column=2)
aadhar_noentry.grid(row=46, column=2)
phone_noentry.grid(row=47, column=2)
emergencyentry.grid(row=48, column=2)
paymentmodeentry.grid(row=49, column=2)


# Creating Checkbox
checkbtn = Checkbutton(text = "remember me?", variable= checkvalue)
checkbtn.grid(row=60, column= 2)

# Submit button
Button(text="submit",font="arial 15 bold"  , fg="dark orange", command=getvals).grid(row=61, column=2)




root.mainloop()
