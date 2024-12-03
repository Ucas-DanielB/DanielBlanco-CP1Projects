print("This quiz will be worth your entire grade, and is about sports ")

score = 0

print("when an attacker is behind the defender and receives a pass in soccer, what is the illegal move called? ")
question1 = input('''A: offside
B: foul
C: hold
D: handball\n''')

if question1 == "A" or question1 == "offside":
    print("you got this correct!")
    score += 1 
    print("You got", score, "answer correct!")
else:
    print(score)
    print("you got it wrong. You will now receive an easier question. ")

    print("How many points do you get from every basket in basketball? ")
    ez_question1 = input('''    A: 1
    B: 3                   
    C: 2
    D: 4\n''')

    if ez_question1 == "C" or 2:
        score += 1
        print(score)
        print("Nice you got it right! Onto the next question. ")
    else:
        print("aww you still got that wrong. guess we will just move on. ")


print("In volleyball, are you allowed to kick the ball without it being illegal? ")
question2 = input('''A: Yes, as long as you can hold the ball in your feet.
B: No, you cannot kick it.
C: Yes, the ball can touch any part as long as it's not a hold.
D: No, you will be disqualified .\n''')

if question2 == "C" or question1 == "Yes":
    print("You're so right!")
    score += 1
    print("You got", score, "answer correct!")
else:
    print(score)
    print("you got it wrong. You will now receive an easier question. ")
    
    print("What sport does Lebron James play? ")
    ez_question2 = input('''    A: Football
    B: Soccer                   
    C: Basketball
    D: Volleyball\n''')

    if ez_question2 =="C" or "Basketball":
        score += 1
        print("You got", score, "answer correct!")
        print("Wow now you get it! ")
    else:
        print("You got it wrong, but it's ok! there is a chance to get the others correct! ")


print("In Baseball, what do you call the person that throws the ball towards the batter? ")
question3 = input('''A: Thrower
B: Receiver
C: Caller
D: Pitcher\n''')

if question3 == "D" or question3 == "Pitcher":
    print("That is correct! ")
    score += 1
    print("you got", score, "answer correct!")
else:
    print("You have",score, "answers correct")
    print("you got it wrong, but I will give you another question to redeem yourself.")

    print("What do you call the person that swings the bat?(HINT: It is hidden inside of the first question)")
    ez_question3 = input('''A: Swinger
    B: Batter
    C: Hitter
    D: Home run\n''')
    if ez_question3 == "B" or ez_question3 == "Batter":
        print("That is correct! ")
        score += 1
        print("you got", score, "answer correct!")
    else:
        print("You got it wrong, but don't worry! there is a chance to gain more points. ")


print("What is the one sport that has a world cup every four years ")
question4 = input('''A: Soccer
B: Football
C: Volleyball
D: Basketball\n''')

if question4 == "A" or question4 == "Soccer":
    print("Nice you got it right? ")
    score += 1
    print("you got", score, "answer correct!")
else:
    print("You have", score, "answers correct")
    print("You got it wrong, but I am required to give you another easier question.")

    print("What is the name of the tool you use to play golf")
    ez_question4 = input('''A: Batter
    B: Hitter
    C: Putter
    D: Launcher\n''')
    if ez_question4 == "C" or ez_question4 == "Putter":
        print("Wow you're right! ")
        score += 1
        print("you got", score, "answers correct!")
    else:
        print("You got it wrong, do not worry though, this is a judgment free zone.")


print("In soccer, is slide tackling someone and hitting their legs first illegal? ")
question5 = input ('''A: Yes, if they hit the opponents legs first
B: No, it does not matter if they hit the enemy's legs or the ball first 
C: Depends on the players intent
D: No, it is not illegal at all\n''')

if question5 == "A" or question5 == "yes, if they hit the opponents legs first":
    print("Wow you got this right!")
    score += 1
    print("You got", score, "answer correct!")
else:
    print("You have",score, "answers correct")
    print("You got this wrong, but since you are my favorite student, I will give you another easier question.")

    print("If you shoot outside of the three point line in Basketball, how many points do you get? ")
    ez_question5 = input('''A: 3
B: 2
C: 5
D: 6\n''')
if ez_question5 == "3" or ez_question5 == "Three":
	print("Wow you got this right! ")
	score += 1
	print("you got", score, "answers correct")
else:
	print("You have", score, "answers correct")
	print("This is the end of the test, depending on your score, you either passed or failed.")