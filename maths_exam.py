import random
import time

OPERATORS = ["+", "-", "*"]
minimum_number = 3
maximum_number = 12
total_problems = 10

def generate_problem():
  left = random.randint(minimum_number, maximum_number)
  right = random.randint(minimum_number, maximum_number)
  operator = random.choice(OPERATORS)

  question = str(left) +" " + operator +" " + str(right)
  answer = eval(question)
  return question, answer

wrong = 0
input("press any key to start!")
time.sleep(1)
print("ready...")
time.sleep(1)
print("Go !!")

start_time = time.time()

for i in range (total_problems):
  question, answer = generate_problem()
  while True:
    GUESS = input("Question"+str(i + 1)+" : "+ question+ " = ")
    if GUESS == str(answer):
      break
    else:
      wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
time.sleep(1)
print ("\nfinally, you finished in", total_time, "seconds")



