code = 16
if code == 1:
	class Dog():
		def __init__(self,breed,name,spots):
			self.breed = breed
			self.name = name
			self.spots = spots
			
		def display_breed (self):
			print(self.breed)
			
	koko = Dog('lab', 'kokko', 'no spots')
	doberman= Dog ("huskie", 'totto', 'spots')
	print (type(koko))
	koko.display_breed()
	
elif code == 2:
	print("i want to print %s text here." %'some \tmore')
	print ("i want to print %r text here." % 'some \tmore')
	print ("i wrote %s programs today" %2.75)
	print ("i read %d pages toady" %99.87)

elif code ==3:
	class Animal():
		def __init__(self,breed,colour):
			self.breed = breed
			self.colour = colour
		def eat(self):
			print ("i am eating veggies")
		def who_am_i (self):
			print ("i am a pet")
			
	class Dog (Animal):
		def __init__(self,breed,colour):
			Animal.__init__(self,breed,colour)
			print ("i am a dog")
			
		def bark (self):
			print ("woof!")
			
	myanimal = Animal("huskie","grey")
	print (myanimal.breed,myanimal.colour)
	mydog = Dog("labrador","black")
	print (mydog.breed, mydog.colour)
	print (mydog.who_am_i())
	print (mydog.bark())
	print (mydog.eat())
	# example of class inheritence
	
elif code == 4:
	class Dog ():
		def __init__(self,name):
			self.name = name
			
		def speak(self):
			return (self.name + " says woof!")
			
	class Cat ():
		def __init__(self,name):
			self.name = name
			
		def speak(self):
			return (self.name + " says meow!")
	koko = Dog("koko")
	print (koko.name)
	sweety = Cat ("sweety")
	print (sweety.name)
	print (koko.speak())
	print (sweety.speak())
	
	for pet in [koko,sweety]:
		print (pet.speak())
		print (type(pet))
	def pet_speak(pet):
		print (pet.speak())
	pet_speak(koko)
	pet_speak(sweety)
	# example of class polymorphism
	
elif code == 5:
	class Book():
		def __init__(self,title,author,pages):
			self.title = title
			self.author = author
			self.pages = pages
		def __str__(self):
			return f"{self.title} by {self.author}"
		def __len__(self):
			return self.pages
		def __del__(self):
			print ("book has been deleted")
	b = Book("python","Hose",200)
	print (str(b))
	print (len(b))
	del (b)
	print (str (b))
	#special/magic/dundar mathods in OOPS
	
elif code == 6:
	def ask_for_int():
		while True:
			try:
				result = int(input("please provide a number: "))
			except:
				print ("input entered is not a number")
			else:
				print("thanks! we got an integer")
				break
			finally:
				print("either u r right or u can try again!!")
	ask_for_int()
	
elif code == 7:
	try:
		for i in [2,4,6]:
			print (i**2)
	
	except:
		print("please try again with correct input")
		
elif code == 8:
	try:
		x=5 
		y=0
		z = x/y
		print (z)
	except ZeroDivisionError:
		print ("denominator can not be zero")
	finally:
		print ("all done")
		
elif code == 9:
	def func():
		while True:
			try:
				a = int(input("please provide a number: "))
				print (a**2)
			
			except:
				print ("input entered is not a number")
			
			else:
				print ("well done!!")
				break
	func()

elif code == 10:
	from collections import Counter
	mylist = [1,1,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5]
	list2 = ['a','a','a',10,10,10,10,2,2,2,2,3]
	string1 = "my name is Meghali and her name is Mishka"
	c= Counter(list2)
	print (list(c))
	print (set (c))
	print (sum(c.values()))
	print (Counter(mylist).most_common(3))
	print (Counter(list2))
	print (Counter(string1.lower().split()))
	#application of Counter function from Collections module
	
elif code == 11:
	d = {'a': 10, 'b': 20}
	print (d)
	d= defaultdict(lambda: 0)
	d['right']= 100
	print (d)
	print (d['wrong'])
	print (d)
			
elif code == 12:
		# use of re module for RegEx (regular expressions)
		txt = "the tiger is the national animal of the country"
		import re
		s = bool(re.search("^the.*national$",txt))
		#to check whether string starts with 'the' and ends with 'country' using re module
		print (s)
		x = re.findall("the",txt)
		print (x)
		#to return a list of all "the" in the string
		y = re.search("the",txt) 
		print (y.start())
		#to print index position of first "the" using search & start function
		z = re.split("the",txt,2)
		print (z)
		# to return a list of text at each match in a string using split function
		p = re.sub("the","a",txt,1)
		print (p)
		# replace the match keyword with the text of ur choice using sub () function
		
elif code == 13:
	import re
	def main():
		txt = "The quick brown fox jumps over the lazy dog"
    
		# print the list of 'o' present in the string txt
		print (re.findall("o", txt))
		
		# print the index of first occurrence of 'h' in the string txt using search function
		print ((re.search("h",txt)).start())
		
		# convert the first 3 white-space character into '#' and print the changed txt
		print (re.sub("\s",'#',txt,3))
		return 0

	if __name__ == '__main__':
		main()

elif code == 14:
	def main():
		from functools import reduce 

		# Use map to print the square of each numbers 
		my_ints = [4, 6, 3, 9, 2, 8, 12]
		print (list(map(lambda x: x**2, my_ints)))
    
		# Use filter to print only the names that are less than or equal to seven letters
		my_names = ["scaler", "interviewbit", "rishabh", "student", "course"]
		print (list(filter(lambda x: len(x)<=7, my_names)))
	
		# Use reduce to print the product of these numbers
		my_numbers = [4, 6, 9, 23, 5]
		print(reduce(lambda x,y: x*y, my_numbers))
		
		return 0

	if __name__ == '__main__':
		main()
		
elif code == 15:
		
	def username_chk(username):
			alpha = "abcdefghijklmnopqrstuvwxyz"
			numeric = "1234567890"
			special = "-_"
			for i in username:
				if i in alpha:
					continue
				elif i in numeric:
					continue
				elif i in special:
					continue
				else:
					print ("username is not valid")
					return False
			return True
			
	def websitename_chk(website_name):
			alpha = "abcdefghijklmnopqrstuvwxyz"
			numeric = "1234567890"	
			print (alpha)
			for i in website_name:
				if i in alpha:
					continue
				elif i in numeric:
					continue
				else:
					print ("websitename is not valid")
					return False
			return True
		
	def extension_chk (extension):
			if (len(extension) <= 3):
				return True
			else:
				return False
	
	def main():
		email_id = input('enter an email id to check its validity: ')
		username = email_id.split('@')[0]
		website_name = email_id.split('@')[1].split(".")[0]
		extension = email_id.split('@')[1].split(".")[1]
		if username_chk(username) and websitename_chk(website_name) and extension_chk(extension):
			print ("Emailid is valid")
		else:
			print("emailid is not valid")
			
	if __name__ == "__main__":
		
		main()
		
elif code == 16:
		
	def username_chk(username):
			alpha = "abcdefghijklmnopqrstuvwxyz"
			numeric = "1234567890"
			special = "-_"
			for i in username:
				if i in alpha:
					continue
				elif i in numeric:
					continue
				elif i in special:
					continue
				else:
					print ("username is not valid for j")
					return False
			return True
			
	def websitename_chk(website_name):
			alpha = "abcdefghijklmnopqrstuvwxyz"
			numeric = "1234567890"	
			for i in website_name:
				if i in alpha:
					continue
				elif i in numeric:
					continue
				else:
					print ("websitename is not valid for j")
					return False
			return True
		
	def extension_chk (extension):
			if (len(extension) <= 3):
				return True
			else:
				return False
	
	def email_validate(email_id):
		username = email_id.split('@')[0]
		website_name = email_id.split('@')[1].split(".")[0]
		extension = email_id.split('@')[1].split(".")[1]
		if username_chk(username) and websitename_chk(website_name) and extension_chk(extension):
			return email_id
		else:
			pass
	

	def main():
		x = int(input ("enter no of email ids: "))
		ls_email = []
		for i in range (x):
			j= global(i+1)
			y = input ("enter no. {} email id: ".format (j+1))
			ls_email.append(y)
			
		
		valid_emailid = print(list(filter(email_validate,ls_email)))
	if __name__ == "__main__":
		
		main()