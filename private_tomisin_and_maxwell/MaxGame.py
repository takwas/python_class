


# global variables
name = ''
score = 0
ans = True
qst = [
       ['What is your name?', 'Max', 'Tom', 'Tos', 'Jam'],
       ['What is bla bla bla?', 'Bla', 'Dah', 'Fah', 'Sah'],
       #[],
       #[],
       #[]
       ]
num_q=0


def get_name(disp):
	m_name = raw_input(disp)
	return m_name


def greet(name):
	print
	print 'Hello', name, '!'
	print 'Welcome to ---'
	print '' # instructions


def print_q(q_num):
	print '\tQuestion', (q_num+1), '\b:\t', qst[q_num][0]
	print
	print '\t\tA.', qst[q_num][1], ' B.', qst[q_num][2], ' C.', qst[q_num][3],' D.', qst[q_num][4]
	print


def get_ans():
	opt = raw_input('(Hint: Select an option)\nAns:  ')
	
	if opt=='A':
		ans = True
	else:
		ans = False
		

def end_game():
	print ' GAME OVER! '
	### check score and grade user


def run_game():
	print
	num_q= len(qst)
	name = get_name('Enter your name: ')
	greet(name)
	
	for i in range(num_q):
		print_q(i)
		get_ans()
		
		if(ans==False):
			end_game()
			break
			
	end_game()   


def run():
    run_game()
    
    
if __name__ == '__main__':
    run()



### meyiwa007@yahoo.co.uk

