#program to read age of student and check weather
#student is eligible or not eligible for vote
name=raw_input('enter name')
a=int(input('enter age'))
if a>=18:
    print 'Hi',name
    print 'you are eligible to vote'
else:
    print 'sorry',name
    print 'you are not eligible to vote'

#Expected otput
    #enter name sanjay
    #enter age 17
    #you are eligible to vote

#original output
    #enter name Sanjay
    #enter age 17
    #you are not eligible to vote
