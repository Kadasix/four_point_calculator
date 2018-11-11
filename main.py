# Grade Calculator
import math
import sys
import time

print("Welcome to the Grade Calculator. This only works on a 4-point scale.")
print("Input all grades in the following format:")
print("If it's one grade, input the only the letter A, B, C, D, or F. Ignore any X grades. Enter Z grades as an F.")
print("If it's more than one grade, please input the grade in the format \"X N\", where X is the letter grade and N is the number of grades it is worth.")

possible_grades = ["F", "D", "C", "B", "A"]

def manual_input(existing_points, existing_grades): # Allows user to manually input all grades. Returns total points, number of grades
  print("DO NOT ENTER ACTUAL EXTRA CREDIT GRADES YET! If for any reason you screwed up, enter \"undo\" to remove your previous grade. Enter \"end\" to move to calculations.")
  total_points = existing_points
  grades = existing_grades
  previous_points = 0
  previous_grades = 0
  print("\n")
  print("Begin entering grades:")

  while True:
    instruction = input(">>").upper()
    if instruction[0] in possible_grades:
      if len(instruction) == 1:
        previous_points = possible_grades.index(instruction)
        previous_grades = 1
        total_points = total_points + previous_points
        grades = grades + 1
      elif instruction[1] == " ":
        previous_points = (possible_grades.index(instruction[0])) * int(instruction[2:])
        previous_grades = int(instruction[2:])
        total_points = total_points + previous_points
        grades = grades + int(instruction[2:])
      else:
        print("Invalid command.")

    elif instruction == "UNDO":
      total_points = total_points - previous_points
      grades = grades - previous_grades
      print("Note that you may not undo consecutive times.")
    elif instruction == "END":
      break
    else:
      print("Invalid command.")

  EC_points = int(input("Insert your number of extra credit points. (For example, 6 EC As are 6*4 = 24 extra credit points."))
  total_points = total_points + EC_points

  return total_points, grades

def request_grades():
  print("\n Please select one way to input grades:")
  print("X - Mostly automated. You'll need to know your current grade and the number of grades in.")
  print("Z - Fully manual. If you want to input all your grades.")
  choice = input("Input one letter:").upper()
  if choice == "X":
    average = float(input("What's your current grade in the class?"))
    grades = int(input("How many grades are in the gradebook?"))
    points = round(average * grades, 0)
    return points, grades
  if choice == "Z":
    return manual_input(0, 0)

while True:
  time.sleep(0.5)
  print("-----------------------")
  print("Please select one option:")
  print("A - \"How many A's do I need to get some grade in this class?\"")
  print("B - \"How many Z's can I afford to get to maintain some grade in this class?")
  print("C - \"What will my grade in the class be after receiving these grades?\"")
  print("D - About the creator.")
  print("E - Quit program.")
  choice = input("Input one letter:").upper()

  if choice == "A": # How many A's are needed?
    points, grades = request_grades()
    desired_grade = float(input(("\n What's your desired numberical score in this class? (Ex. A ==> 3.50)")))
    if desired_grade >= 4.00:
      print("Sorry, that's impossible. Try again. You trying to pull something?")
      continue
    elif points/grades < desired_grade:
      required_A = math.ceil((desired_grade * grades - points)/(4-desired_grade))
      print("You will need", required_A, "A(s) in order to get a", desired_grade, ".")
    else:
      print("You already have your desired grade. You may be looking for option B.")

  if choice == "B": ## Z calculator
    points, grades = request_grades()
    desired_grade = float(input(("\n What's your desired numberical score in this class? (Ex. A ==> 3.50)")))
    if desired_grade <= 0.00:
      print("Sorry, that's impossible. Try again. You trying to pull something?")
      continue
    elif points/grades > desired_grade:
      needed_Z = math.floor((points - (desired_grade * grades)) / desired_grade)
      print("You can afford", needed_Z, "Z(s) in order to maintain a", desired_grade, ".")
    else:
      print("You're already behind your desired grade. You may be looking for option A.")

  if choice == "C": ## Impact on Grade
    points, grades = request_grades()
    print("\n Please input the grades you would get: \n")
    new_points, new_grades = manual_input(points, grades)
    new_average = round(new_points/new_grades, 2)
    print("After those grades have been put in, you would have a", new_average, ".")

  if choice == "D":
    print("\n This Grade Calculator, v.0.1, was created solely by Vincent Li. While I initially created this solely for MPSH, I hope that this calculator will find use elsewhere.")
    print("I'd like to give my thanks to Adonis Borges, Daniel Fein, Lindsey Yang, and Benjamin Goldstein for putting this idea in my head. Thank you for you support, truely.")
    time.sleep(5)

  if choice == "E":
    sys.quit()
