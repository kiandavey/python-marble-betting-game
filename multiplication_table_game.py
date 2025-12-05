import random, time

print("+---------- MULTIPLICATION TABLE GAME ----------+")
try:
    max_num = int(input("Enter the max number to use (ex: 12 for 12x12): "))
    if max_num < 1:
        max_num = 12
        print("Invalid number. Defaulting to 12.")
except ValueError:
    max_num = 12
    print("Invalid input. Defaulting to 12.")

questions = []
answers = []

for i in range(1, max_num + 1):
    for j in range(1, max_num + 1):
        question_str = f"What is {i} x {j}? : "
        questions.append(question_str)
        answers.append(str(i * j)) 

question_answer = list(zip(questions, answers))
print(f"Generated {len(question_answer)} unique questions up to {max_num}x{max_num}.")

try:
    number_questions = int(input("How many questions do you want to be asked? : "))
except ValueError:
    number_questions = 10
    print("Invalid input. Defaulting to 10 questions.")

correct_answers = 0
wrong_answers = 0

questions_answers_log = [] 
answer_times = []          
total_start_time = time.time() 

for i in range(number_questions):
    random_pair = random.choice(question_answer)
    questions_answers_log.append(random_pair)

    question = random_pair[0] 
    correct_answer = random_pair[1] 
    
    start_time = time.time()
    
    try:
        user_input_str = input(f"{i + 1}. {question}")
        user_answer = user_input_str.strip()
    except EOFError: 
        user_answer = ""
        
    end_time = time.time()
    
    time_taken = end_time - start_time
    answer_times.append(time_taken)

    if user_answer == correct_answer:
        print("✅ Correct!")
        correct_answers += 1
    else:
        print(f"❌ Wrong. The answer was {correct_answer}")
        wrong_answers += 1

total_end_time = time.time()
total_quiz_duration = total_end_time - total_start_time

print("")
print("+------------------- RESULTS -------------------+")
print(f"Correct Answer/s : {correct_answers}")
print(f"Wrong Answer/s : {wrong_answers}")
print(f"% Correct : {(correct_answers / number_questions) * 100:.2f}%")
print(f"Total Score : {correct_answers}/{number_questions}")

print("")
print("+----------------- TIME ANALYSIS ---------------+")
print(f"Total quiz duration: {total_quiz_duration:.2f} seconds")
if answer_times:
    average_time = sum(answer_times) / len(answer_times)
    print(f"Average time per question: {average_time:.2f} seconds")
else:
    print("No time data available.")

print("")
print("+------------- QUESTIONS & ANSWERS -------------+")
for index, (pair, time_taken) in enumerate(zip(questions_answers_log, answer_times)):
    question_text, correct_answer_text = pair
    print(f"{index + 1}. Q: {question_text.strip()} | A: {correct_answer_text} | Time: {time_taken:.2f}s")