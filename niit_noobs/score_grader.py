score = raw_input("Enter your score: ")
score = int(score)

if score < 45:
	print "You had an F. Get serious!"
elif 45 < score < 55:
	print "You had a C. Fair enough."
elif 55 < score < 70:
	print "You had a B. Getting good."
else:
	print "You had an A. Awesome!"
