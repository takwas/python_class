

pb = {'Max':'12345', 'Tom':'54321', 'Tos':'21543', 'Jam':'45321'}
#menu = {1:'Add Contacts', 2:'View Contacts'}


def view_cnts():	
	print "Viewing All Contacts..."
	for i in pb.keys():
		print "\t",i, ":-", pb[i]

def del_cnt():
	conf = raw_input("Are you sure you want to delete? (Yes/No): ")
	if(conf=="Yes"):
		del pb[name]

def add_cnt(name,num):
	while(True):
		if(pb.has_key(name)):
			ans = raw_input("Are you sure you want to overwrite? (Y/N): ")
			if(ans=="Y"):
				pb[name]=num
				break
			else:
				new_name = raw_input("Enter Name: ")
				name = new_name
		else:
			pb[name]=num
			break


def searc_cnt(name):
	if(pb.has_key(name)):
		print 'Contact Found'
		print "\t",name, ":-", pb[name]
	else:
		print 'Contact not Found'


def run():
	print 'Welcome to Phonebook Program Menu!'
	print 'Select an option'
	print '\t1. View contacts'
	print '\t2. Search Contact'
	print '\t3. Add Contact'
	print '\t4. Delete Contact'
	
	opt=int(raw_input('\n\t>_'))
	
	print
	
	if(opt==1):
		view_cnts()
	elif (opt==2):
		name2sch = raw_input("Enter contact's name:  ")
		searc_cnt(name2sch)
	elif(opt==3):
		name2add = raw_input("Enter contact's name:  ")
		num2add = raw_input("Enter contact's number:  ")
		add_cnt(name2add, num2add)
		print
		view_cnts()
	elif(opt==4):
		name2del = raw_input("Enter contact's name:  ")
		del_cnt(name2del)
	else:
		print 'Incorrect option selected!'



    
if __name__ == '__main__':
    run()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
