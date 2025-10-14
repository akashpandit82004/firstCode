# #create  a programe to data time 
# import time
# t=time.strftime('%H:%m:%S')
# hour=int(time.strftime('%H'))
# hour=int(input("enter the hour:"))
# print(hour)
# if hour>=0 and hour<12:
#     print("good morning")
# elif hour>=12 and hour<17:
#     print("good afternoon sir")
# elif hour>=17 and hour<0:
#     print("good night sir")
 

# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
# KBC style quiz program using lists

# List of questions
# KBC Game in Python

Questions = [
    "Q1. Which is the capital of India?",
    "Q2. Who is known as the Father of the Nation?",
    "Q3. Which planet is known as the Red Planet?",
    "Q4. Who wrote the national anthem of India?",
    "Q5. Which is the largest mammal in the world?",
    "Q6. What is the currency of Japan?",
    "Q7. Who was the first Prime Minister of India?",
    "Q8. Which is the smallest continent in the world?",
    "Q9. Who invented the light bulb?",
    "Q10. Which is the national flower of India?"
]

Options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. B. R. Ambedkar", "D. Subhash Chandra Bose"],
    ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
    ["A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Sarojini Naidu", "D. Lata Mangeshkar"],
    ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Shark"],
    ["A. Yen", "B. Yuan", "C. Dollar", "D. Peso"],
    ["A. Lal Bahadur Shastri", "B. Jawaharlal Nehru", "C. Mahatma Gandhi", "D. Rajendra Prasad"],
    ["A. Australia", "B. Europe", "C. Antarctica", "D. South America"],
    ["A. Alexander Graham Bell", "B. Nikola Tesla", "C. Thomas Edison", "D. Albert Einstein"],
    ["A. Lotus", "B. Rose", "C. Sunflower", "D. Jasmine"]
]

answers = ["B", "A", "C", "B", "B", "A", "B", "A", "C", "A"]  # Correct answers

print("✨ Welcome to KBC (Kaun Banega Crorepati) ✨\n")

score = 0

for i in range(len(Questions)):
    print(Questions[i])
    for option in Options[i]:
        print(option)

    user_ans = input("Your Answer (A/B/C/D): ").strip().upper()

    if user_ans == answers[i]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {answers[i]}.\n")

print("🎉 Thank you for playing KBC!")
print(f"🏆 Your Final Score: {score}/10")






