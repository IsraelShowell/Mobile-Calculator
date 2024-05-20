# Creator: Israel Showell
# Start Date: 5/19/2024
# End Date: 5/19/2024
# Project: Moblie Calculator
# Version: 1.10

# Description:
"""
This is a basic calculator application that I made to practice app development and using the Kivy library!
I also practiced using Google Colab, an Online Jupyter Notebook that provides free access to computing resources!
Google Colab ensures that the conversion process would be smooth, due to the amount of space it would take to install the used libraries.

I developed this application using Kivy documentation and an awesome tutorial from Tech2 etc!
Check out his Youtube at this link!
https://www.youtube.com/@Tech2etc

The icons I used in this application came from these links!
Main Icon:
Image by <a href="https://pixabay.com/users/blendertimer-9538909/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7832583">Daniel Roberts</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7832583">Pixabay</a>

Splash Icon:
Image by <a href="https://pixabay.com/users/caffeinesystem-1979991/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1555910">Rachel C</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1555910">Pixabay</a>
"""

#These are the libaries I used to create the GUI and to detect input
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math


class MainApp(App):

    #Build Constructor
    def build(self):

        #Changes the icon for the app
        self.icon = "calculatormain.png"

        #Stores the operators
        self.operators = ["/","*","+","-","(",")","^","!"]

        #Remembers the last button and operator used
        self.last_was_operator = None
        self.last_button = None

        #Controls the main layout of the application
        main_layout = BoxLayout(orientation = "vertical")

        #The solution field is the black screen we see!
        #Its bg is black, fg is white, it has only one line, input starts at the right side, font size is 56, and the text cannot be selected by a user
        self.solution = TextInput(background_color = "black", foreground_color = "white", multiline=False, halign="right", font_size=56, readonly=True)
        

        #Adds the main layout to the app as a widget
        main_layout.add_widget(self.solution)

        #These are the buttons that render on the app
        #I can change the order of the buttons just by changes numbers here
        buttons = [
            ["9", "8", "7", "/"],
            ["6", "5", "4", "*"],
            ["3", "2", "1", "+"],
            [".", "0", "C", "-"],
            ["(",")","^","!"],
            ]


        #This adds the buttons onto the main screen
        #Think of this as a 2D array.
        #The first loop controls the row of buttons
        #and the second loop controls the column of each row
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color="grey",
                    pos_hint={"center_x":0.5,"center_y":0.5},
                )
                #This binds each button to the on_button_press function 
                button.bind(on_press=self.on_button_press)
                #Adds the button to h_layout
                h_layout.add_widget(button)
                
            #Adds each h_layout to the main layout.
            main_layout.add_widget(h_layout)

        #This adds the equal button to the main layout
        equal_button = Button(
            text ="=", font_size=30, background_color="grey",
            pos_hint={"center_x":0.5,"center_y":0.5},
        )

        #Binds the equal button to a function
        equal_button.bind(on_press=self.on_solution)

        #Adds the equal button to the main_layout
        main_layout.add_widget(equal_button)

        #Ends the build function and returns the main layout
        return main_layout

    #Start of the button press function
    def on_button_press(self, instance):
        #Creates the variables for the start of the program
        #Also serves as the inital starting point
        current = self.solution.text
        button_text = instance.text

        #Checks if the clear button has been pressed
        if button_text == 'C':
            self.solution.text = ""
        #Adds the format for exponents
        elif button_text == '^':
            self.solution.text = self.solution.text + "**"
            
        #Calculates the factorial of a number
        elif button_text == '!':
            self.solution.text = str(math.factorial(eval(self.solution.text)))
            
        else:
            #This checks to see if there are 2 operators at one time.
            # E.G: 1 + +. We want to make sure that doesn't happen
            if current and (self.last_was_operator and button_text in self.operators):
                #Makes sure that you can still put an operator after )
                if button_text == ")":
                    new_text = current + button_text
                    self.solution.text = new_text
                else:
                    return
            #Stops user from entering in a operator as the first value, unless its a (
            elif current == "" and button_text in self.operators:
                if button_text == "(":
                    new_text = current + button_text
                    self.solution.text = new_text
                else:
                    return
            #If the above conditions are false, then the program will add
            #the button text to the screen
            else:
                #What is currently on the screen + the value from the pressed button
                new_text = current + button_text
                self.solution.text = new_text

        #This clears the variables 
        self.last_button = button_text
        self.last_was_operator = ""

    #Start of the solution function
    def on_solution(self, instance):

        #Sets text equal to what ever is in the solution field
        text = self.solution.text
        i = 0
        
        #Checks if there is text in the field
        if text:
            #Checks to see if there is a leading zero, and if there is, remove it
            while i < len(text):
                if text[i] == '0':
                    self.solution.text = text.replace("0","")
                    i+=1
                else:
                    break
                
            #Checks to see if there is any input after cleaning the zeros!
            if self.solution.text:
                #Eval takes the entire string and solves the problem.
                #Eval usually stores input as a number
                #Eval can run malicious code however, so I may change this later.
                try:
                    solution = str(eval(self.solution.text))
            
                    self.solution.text = solution
            
                    #Clears the variable after each calculation!
                    self.last_was_operator = ""

                #You cna't divide by zero! >:(
                except ZeroDivisionError:
                    return
                    
            else:
                #Returns nothing if there is no text
                return
        #Returns nothing if there is no text
        else:
            return
        
#Runs the app
if __name__ == "__main__":
    app = MainApp()
    app.run()
