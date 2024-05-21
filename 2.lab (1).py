'''
ROCK, PAPER, SCISSORS PYTHON PROJECT UNIT 2
Ty Chan, Yasong Feng, Ray Xu
Team 7 8 wut
March 2023
'''

'''
FLOWCHART:
https://docs.google.com/drawings/d/197LHr8_c284qZbqjX9ihWQr7vlL23WQkHP1H3Sv6T6I/edit?usp=sharing
'''


'''
CODE:
'''

'''
Random module
'''
import random

'''
gorock  - Ray
Contract: Num → string

Description: Matches random number input with corresponding string and returns the string. 

Tests: 
gorock(0) → "You lost. I picked paper."
gorock(2) → "You won. I picked scissors.""
gorock(1) → "We drew. Very nice."
'''
def gorock(num):
    if num == 0:
        return "You lost. I picked paper."
    elif num == 2:
        return "You won. I picked scissors."
    else:
        return "We drew. Very nice."

'''
gopaper  - Yasong
Contract: Num → string

Description: Matches random number input with corresponding string and returns the string. 

Tests:
gopaper(0) -> “You lost. L. I might possibly replace your future job.”
gopaper(2) -> "You won. However, I’m not a sore loser, unlike you."
gopaper(1) -> "We drew. Very nice."
'''
def gopaper(num):
    if num == 0:
        return "You lost. L. I might replace your future job."
    elif num == 2:
        return "You won. I’m not a sore loser, unlike you."
    else:
        return "We drew. Very nice."

'''
goscissors - Ty
Contract: Num → string

Description: Matches random number input with corresponding string and returns the string. 

Tests:
goscissors(0) -> “You lost, I chose rock against scissors.”
goscissors(2) -> "You won. Paper loses to scissors."
goscissors(1) -> "We drew. Very nice."
'''     
def goscissors(num):
    if num == 0:
        return "You lost. I chose rock."
    elif num == 2:
        return "You won. Paper loses to scissors."
    else:
        return "We drew. Very nice."

'''
The original function shows the same statements regardless of win, loss, and draw ratio. 
The feedback was to show different statements depending on the ratio.
statements - Ray
Contract: 
Win → integer
Loss → integer
Draw → integer

Description: Prints the number of times player wins, loses, or draws.

Tests:
statements(1, 3, 2) →
You won 1 time(s)!
You lost 3 time(s)! Hah, sucker.
We drew 2 time(s)!

statements(3, 2, 1) →
You won  3  time(s)! Don't let it get to your head!
You lost 2 time(s)!
We drew 1 time(s)!

statements(1, 2, 3) →
You won 1 time(s)!
You lost 2 time(s)!
We drew 3 time(s)! We'll call it equal this time.

statements(2, 2, 2) →
You won 2 time(s)!
You lost 2 time(s)!
We drew 2 time(s)!
'''
def statements(win, loss, draw):
    if loss > win and loss > draw:
        print("You won " + str(win) + " time(s)!")
        print("You lost " + str(loss) + " time(s)! Hah, sucker.")
        print("We drew " + str(draw) + " time(s)!")
    elif win > loss and win > draw:
        print("You won " + str(win) + " time(s)! Don't let it get to your head!")
        print("You lost " + str(loss) + " time(s)!")
        print("We drew " + str(draw) + " time(s)!")
    elif draw > loss and draw > win:
        print("You won " + str(win) + " time(s)!")
        print("You lost " + str(loss) + " time(s)!")
        print("We drew " + str(draw) + " time(s)! We'll call it equal this time.")
    else:
        print("You won " + str(win) + " time(s)!")
        print("You lost " + str(loss) + " time(s)!")
        print("We drew " + str(draw) + " time(s)!")

'''
letsplay - Ray
Contract: integer + string -> string 
Variables: 
time 
Input from user
Determines how many times the game will play
n
Starts at 0
Counts up to time
	draw
Counts number of draws in gameplay
	win
Counts number of wins in gameplay
	loss
Counts number of losses in gameplay
	num 
Stores random number 0 - 2 every round of gameplay
choice 
Stores user input rock, paper, or scissor(s)

Description: Takes user’s desired number of plays, desired choice for each play at a time, then returns the result of the play. Repeats for the desired number of play times.  Finally, returns overall results (i.e. times won, lost, drawn).
Tests: 
letsplay() → gameplay
'''
def letsplay():
    time = input("How many times are we playin'? ")
    print("    ")
    n = 0
    draw = 0
    win = 0
    loss = 0
    while n < int(time):
        num = (random.randrange(0, 3))
        choice = input("Whatcha bettin' on? ")
        if choice == 'rock':
            print(gorock(num))
        elif choice == 'scissors' or choice == 'scissor':
            print(goscissors(num))
        else:
            print(gopaper(num))
        n += 1
        if num == 1:
            draw += 1
        elif num == 0:
            loss += 1
        else:
            win += 1
        print("    ")
    statements(win, loss, draw)
            
letsplay()
        

'''
REFLECTION:

1. How did you manage the work of the project?
- Broke down the game into smaller functions to more easily manage progress and to create the flowchart
- Asked for thoughts and comments everyday to document struggles and achievements
- Combined information from the flowchart and documentation to create code that is easy to understand and runs correctly

2. What hardships or challenges did you encounter?
- The game doesn’t return the correct corresponding string
- Finding a way to organize arrows in a way that’s easily understandable
- Documenting and writing a short, concise description for functions
- Implemented the flowchart shapes learned during class into the flowchart
- Figuring out if double or single quotation marks are used in code

3. What did you do to overcome these challenges?
- Asked Mr. Dillon for help
- Looked back and reviewed slides for reference
- Remembering to ask for thoughts and comments every day 

4. How did you go about changing your project based on user feedback?
- Our feedback was to display different texts depending on the results obtained from the game
- Flowchart didn’t need revision because none was needed
- Documentation needed revision

5. What is one thing that each person in the group is proud of?
- Making a visually appealing and easily understandable flowchart -Ty
- Document challenges we encountered and functions we worked on -Yasong
- Figuring out how and why we use secondary functions -Ray
- Finishing project in a timely manner -Ty
- Recording thoughts and comments everyday since the start of working on the project -Yasong
- Translating thought processes into physical code -Ray
'''

