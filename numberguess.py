import random
import tkinter as tk
from tkinter import messagebox
class NumberGuessingGame:
    #this class contains all the game  logic.
    def __init__(self,max_attempts=5,range_start=1,range_end=100): 
        #constructor
        #max no: of guesses upto 5, min no: in guessing range is 1 and  max no: in guessing range is 100
        self.max_attempts=max_attempts
        self.range_start=range_start
        self.range_end=range_end
        #method to initialize the state of game
        #sets up a new round by generating a new secret number and resetting no: of attempts
        self.reset_game()
    def reset_game(self):
        #secret number assigned btwn 1 to 100
        self.secret_number=random.randint(self.range_start,self.range_end)
        #initializes the no: of attempts left for player  to max allowed attempts
        self.attempts_left=self.max_attempts
        #print secret number to the console
        #for debugging purposes only
        #helps to see what's the secret number 
        print(f"Debug: New secret number is {self.secret_number}")
        #initialize the player's guess to none.
        #will be updated as soon a sthe user guess a number
        self.guess=None
        #process player's guess and priovides feedback based on guess
    def make_guess(self,guess):
        #check if the player's guess lies in the vaid range
        if not(self.range_start<=guess<=self.range_end ):
            return "Your guess is out of range!Please guess a number betrween {} and {}. ".format(self.range_start,self.range_end)
        #decrement the no: of chances by 1 
        self.attempts_left-=1
        #check if the guess is within 5 units off the secret number
        if abs(guess-self.secret_number)<=5:
            #check if the player's guess is less than the secret number
            if guess< self.secret_number:
                return "Very close! Too low! You have {} attempts left.".format(self.attempts_left)
            #check if the player's guess is greater than the secret number
            elif guess> self.secret_number:
                return "Very close! Too high! You have {} attempts left.".format(self.attempts_left)
        if guess< self.secret_number:
            return "Too low! You have {} attempts left.".format(self.attempts_left)
            #check if the player's guess is greater than the secret number
        elif guess> self.secret_number:
            return "Too high! You have {} attempts left.".format(self.attempts_left)
        else:
            return "Congragulations! You've guessed the number correctly"
    #checks if the game has ended or not
    def is_game_over(self):
        return self.attempts_left<=0 
        #indicate that player has no attemptrs left.
#class which handles the console version of the game.        
class ConsoleGame:
    #constructor definition
    def __init__(self) :
        #create an instance of NumberGuessingGae class
        #initializing the game logic
        self.game=NumberGuessingGame()
        self.play_game()
    #method to start the game    
    def play_game(self):
        print("Welcome to Guess the Number")
        print("I'm thinking of a number between 1 and 100.")
        print("You have {} attempts to guess it.".format(self.game.max_attempts))
        #loop that continues until game is over
        while not self.game .is_game_over():
            #possibly handle all exceptions
            try:
                guess=int(input("Enter your guess"))
                #pass the player's guess and store the feedback message
                feedback=self.game.make_guess(guess)
                print(feedback)
                if feedback.startswith("Congratulations"):
                    break
            except ValueError:
                print("Please enter a valid integer")
            if self.game.is_game_over():
                 print("Game over! The number was {}.".format(self.game.secret_number))
class GUI:   
    #constructor for gui class                    
    def __init__(self,master) :
        #assign the main window to an instance variable
        self.master=master
        self.master.title("Guess The Number")
        #initializing the game logic for gui
        #create an instance of Numberguessinggame
        self.game=NumberGuessingGame()
        self.create_widgets()
    #method for creating gui components    
    def create_widgets(self):
        #create a label widget
        self.label=tk.Label(self.master,text="Guess a number between 1 and 100: ")
        #applies vertical padding for spacing
        self.label.pack(pady=10)
        #creates a text box where the player can input their guess
        self.entry=tk.Entry(self.master)
        self.entry.pack(pady=10)
        #create a button call guess when clicked check)guess will 
        #be invoked to process the player's guess
        self.guess_button=tk.Button(self.master,text="Guess",command=self.check_guess)
        self.guess_button.pack(pady=10)
        self.reset_button=tk.Button(self.master,text="Reset Game",command=self.reset_game)
        self.reset_button.pack(pady=10)
        #widget to display feedback messages

        self.feedback_label=tk.Label(self.master,text="")
        self.feedback_label.pack(pady=10)
    # process the player's guess from gui   
    def check_guess(self):
        try:
            #retrieve's user guess and converts to integer
            guess=int(self.entry.get())
            #call make_guess passing the player's guess and storing feedback message
            feedback=self.game.make_guess(guess)
            #updates feedback label with the message returned by make_guess method
            self.feedback_label.config(text=feedback)
            if feedback.startswith("Congragulations"):
                messagebox.showinfo("Game Over","You've guessed the correct number")
                self.reset_game()
            if self.game.is_game_over():
                messagebox.showinfo("Game Over","The number was {}.".format(self.game.secret_number))
                self.reset_game()    


        except ValueError:
            self.feedback_label.config(text="Please Enter a Valid integer")
    def reset_game(self):
        """Reset the game state for a new round."""
        self.game.reset_game()
        self.feedback_label.config(text="")
        #clear the feedback label for new game
        self.entry.delete(0, tk.END)#clears the entry widget
if __name__ == "__main__":
    # Uncomment the line below to play the console version
    
    #ConsoleGame()

    # Play the GUI version
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()        








        



        




