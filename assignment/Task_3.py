# Take 4 subjects of marks from user and print obtained marks and its percentage

sub_1 = int(input("Enter marks of first subject : ")) 
sub_2 = int(input("Enter marks of second subject : ")) 
sub_3 = int(input("Enter marks of third subject : ")) 
sub_4 = int(input("Enter marks of fourth subject : "))
total_marks = 400
marks_obtained = sub_1 + sub_2 + sub_3 + sub_4
print("Marks Obtained : " , marks_obtained) 
print("your Percentage is : " , (marks_obtained*100)/total_marks) 
