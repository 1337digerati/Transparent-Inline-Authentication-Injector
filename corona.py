import database
import sunspot
import wrapper

def main():
	db = database('F:\Dropbox\My Dropbox\programming\python\db')
	
	add =[input("---Add---\nWebsite:"), input("\nPassword:")]
	db.add(add)
	
	data = db.pull([input("Search: ")])
	
	self.debug ('Data:', data)
	
	self.debug ("Trying to wrap")
	#w = wrapper("SuperSecretPassword")
	
	self.debug ('done')
	
main()	