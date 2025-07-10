my_dictionaries = {}
 

def add_student():
    while True:
      student_name = input ("What is your name? ")
      student_score = int (input ("What is your score? "))
      my_dictionaries[student_name] = {'score': student_score}
      if student_score <= 20:
        print ("failed")        
      else:
        print("student passed")
      print(my_dictionaries)
      answer = input("Do you want to add another student? y/n  ")  
      if answer.lower() == "n":
             break 
add_student()
