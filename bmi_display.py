from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import math
#from tkinter import Radiobutton
class bmi():
	def __init__(self,root):
		self.root=root
		self.gender=IntVar()
		self.gender.set(0)
		#defaulttext
		height_default= StringVar()
		height_default.set("cms")
		weight_default=StringVar()
		weight_default.set("kg")
		self.height_entry=Entry(self.root,width=25,textvariable=height_default,justify=RIGHT)
		self.weight_entry=Entry(self.root,width=25,textvariable=weight_default,justify=RIGHT)
		self.age_entry=Entry(self.root,justify=RIGHT)

		self.temp_label=Label(self.root,text=" ")
		self.temp_label.grid(row=5,columnspan=2,sticky=W)

		self.bmi_label=Label(self.root,text=" ")
		self.bmi_label.grid(row=6,columnspan=3)

		self.image_label=Label(self.root,image="")
		self.image_label.grid(row=7,columnspan=3,rowspan=3)

		
	def display_mainmenu(self):
		self.root.geometry("350x350")
		self.root.title("BMI Calculator")

		
		#making labels for BMI
		age_label=Label(self.root,text="Age   ")
		age_label.grid(row=0,column=0,sticky=W,pady=5)

		gender_label=Label(self.root,text="Gender")
		gender_label.grid(row=1,column=0,sticky=W,pady=5)

		height_label=Label(self.root,text="Height")
		height_label.grid(row=2,column=0,sticky=W)

		weight_label=Label(self.root,text="Weight")
		weight_label.grid(row=3,column=0,sticky=W)

		
		#making entry for BMI
		
		self.age_entry.grid(row=0,column=1,columnspan=2,pady=5)
		self.age_entry.bind("<Button-1>",self.delete_text)
		self.age_entry.bind("<Key>",lambda event:self.integer_checker(event,age_checker=True))

		male_radiobutton=Radiobutton(self.root,text="Male",variable=self.gender,value=0,command=lambda:self.deselect_radiobutton)
		male_radiobutton.grid(row=1,column=1)
		female_radiobutton=Radiobutton(self.root,text="Female",variable=self.gender,value=1,command=lambda:self.deselect_radiobutton)
		female_radiobutton.grid(row=1,column=2)
		
		
		self.height_entry.grid(row=2,column=1,padx=30,pady=5,columnspan=2)
		self.height_entry.bind("<Button-1>",self.delete_text)
		self.height_entry.bind("<Key>",self.integer_checker)
		#fordefault

		
		self.weight_entry.grid(row=3,column=1,pady=5,columnspan=2)
		self.weight_entry.bind("<Button-1>",self.delete_text)
		self.weight_entry.bind("<Key>",self.integer_checker)
		#making buttons for calculations
		calculate_button=Button(self.root,text="Calculate",background="blue",command=partial(self.calculate_BMI))
		calculate_button.grid(row=4,column=1)

		
		clear_button=Button(self.root,text="Clear",background="grey",command=lambda:self.clear_BMI())
		clear_button.grid(row=4,column=2)
		self.root.mainloop()

	def calculate_BMI(self):
		if self.temp_label['text']==" " and self.age_entry.get()!="" and self.weight_entry.get()!='kg' and self.height_entry.get()!='cms':
			age=int(self.age_entry.get())
			weight=self.weight_entry.get()
			height=self.height_entry.get()
			if self.gender.get()==0:
				gender="Males"
			else:
				gender="Females"
			BMI=int(weight)/(int(height)/100)**2
			BMI=round(BMI,3)
			with open("./text_files/bmi_chart.txt") as fp:
				fp_list=list(fp)
				if fp_list[2][:7]==gender:
					if age>int(fp_list[17][:2]):
						observed_BMI=round(float(fp_list[17][-12:-3]),3)
					elif age<int(fp_list[3][:1]):
						observed_BMI=12.117
					else:
						for i in range(3,17):
							words=fp_list[i].split('\t')#splitting lines)
							if age==int(words[0]):
								observed_BMI=float(words[-1])
								break
					
				if fp_list[18][:5]==gender:
					if age>int(fp_list[33][:2]):
							observed_BMI=round(float(fp_list[33][-11:-3]),3)
					elif age<int(fp_list[19][:1]):
						observed_BMI=14.238
					else:
						for i in range(19,33):
							words=fp_list[i].split('\t')
							if age==int(words[0]):
								observed_BMI=round(float(words[-1]),3)
								break
				print(str(BMI)+"empty")
				text="Your BMI is "+str(BMI)
				
				
				BMI=math.floor(BMI)
				observed_BMI=math.floor(observed_BMI)
				
				if BMI<=observed_BMI+1 and BMI>=observed_BMI:
					self.bmi_label.config(foreground="SpringGreen3")
					image=Image.open("./image_files/fit.png")
					text=text+"\nCongratulations!You are Fit"
					print("Fit")
				elif BMI>observed_BMI+1 and BMI<=observed_BMI+4:
					self.bmi_label.config(foreground="light salmon")
					image=Image.open("./image_files/overweight.png")
					text=text+"\nOh No!You are Overweight"
					print("Overweight")
				elif BMI>observed_BMI+4 and BMI<=observed_BMI+10:
					self.bmi_label.config(foreground="indian red")
					image=Image.open("./image_files/obese.png")
					text=text+"\nYou should exercise!You are Obese"
					photo=ImageTk.PhotoImage(image)
					print("Obese")
				elif BMI>observed_BMI+10:
					self.bmi_label.config(foreground="red4")
					image=Image.open("./image_files/moribdly_obese.png")
					text=text+"\nYou should diet!You are Morbidly Obese"
					print("Morbidly Obese")
				elif BMI<observed_BMI:
					self.bmi_label.config(foreground="OliveDrab1")
					image=Image.open("./image_files/underweight.png")
					text=text+"\nEat More!You are Underweight"
					print("Underweight")
				print(observed_BMI)
				self.bmi_label.config(text=text)
				image = image.resize((75, 150), Image.ANTIALIAS)
				photo=ImageTk.PhotoImage(image)
				self.image_label.config(image=photo)
				self.image_label.image=photo


		else:
			self.temp_label.config(text="Please check your input",foreground="red")

	


	def clear_BMI(self):
		self.height_entry.delete(0,END)
		self.weight_entry.delete(0,END)
		self.age_entry.delete(0,END)
		height_default= StringVar()
		height_default.set("cms")
		weight_default=StringVar()
		weight_default.set("kg")
		self.temp_label.config(text=" ")
		self.height_entry.config(textvariable=height_default)
		self.weight_entry.config(textvariable=weight_default)
		self.bmi_label.config(text=" ")
		self.image_label.config(image="")

	


	def delete_text(self,event):
		event.widget.delete(0,END)
		return None

	



	def integer_checker(self,event,age_checker=False):
		input=event.widget.get()
		if event.keysym=="BackSpace":
			input=input[:-1]
		else:
			input=input+event.char
		#print(input+"test")

		if input.isdigit() or not input:
			if age_checker==True and int(input)>120 or int(input)<0:
				self.temp_label.config(text="Age too large",foreground="red")
			else:
				self.temp_label.config(text=" ")
		else:
			self.temp_label.config(text="Invalid Integer",foreground="red")


	def deselect_radiobutton():
		if self.gender.get()==0:
			female_radiobutton.deselect()
			print("yes")
		if self.gender.get()==1:
			male_radiobutton.deselect()
			print("no")

root=Tk()
ob=bmi(root)
ob.display_mainmenu()

