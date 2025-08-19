import pygame
import sys
import math

# Initialize the pygame.font module
pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define the font
font = pygame.font.Font(None, 36)

# Define the buttons
buttons = [
    [(10, 10), (80, 100), "7"],
    [(10, 110), (80, 120), "8"],
    [(10, 120), (80, 130), "9"],
    [(10, 130), (80, 140), "/"],
    [(90, 10), (170, 100), "4"],
    [(90, 110), (170, 120), "5"],
    [(90, 120), (170, 130), "6"],
    [(90, 130), (170, 140), "*"],
    [(180, 10), (250, 100), "1"],
    [(180, 110), (250, 120), "2"],
    [(180, 120), (250, 130), "3"],
    [(180, 130), (250, 140), "-"],
    [(260, 10), (310, 100), "0"],
    [(260, 110), (310, 120), "."],
    [(260, 120), (310, 130), "+"],
    [(270, 135), (290, 155), "="]
]\

# Define the current number and the operator
current_number = ""
operator = None

# Define the memory_value and the memory_operation
memory_value = 0
memory_operation = None

# Set the window size
# Set the window size
window_width = 660
window_height = 960
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Advanced Calculator")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button[2] == "=":
                    try:
                        result = eval(current_number)
                        current_number = str(result)
                    except Exception as e:
                        print(e)
                        current_number = "Error"
                        break

                elif button[2] in ["+", "-", "*", "/"]:
                    if operator is not None:
                        try:
                            result = eval(current_number)
                            current_number = str(result)
                        except Exception as e:
                            print(e)
                            current_number = "Error"
                            break

                    operator = button[2]
                    current_number += " " + operator + " "

                elif button[2] in ["MC", "MS", "MR", "M+", "M-"]:
                    if button[2] == "MC":
                        memory_value = 0
                        memory_operation = None
                    elif button[2] == "MS":
                        memory_value = 0
                    elif button[2] == "MR":
                        memory_value = memory_value
                    elif button[2] == "M+":
                        memory_value += int(current_number)
                        current_number = str(memory_value)
                    elif button[2] == "M-":
                        memory_value -= int(current_number)
                        current_number = str(memory_value)

                elif button[2] in ["SQRT", "SIN", "COS", "TAN", "PI"]:
                                    try:
                                        result = eval(button[2] + "(" + current_number + ")")
                                        current_number = str(result)
                                    except Exception as e:
                                        print(e)
                                        current_number = "Error"
                                        break

                else:
                    x, y = button[0]
                    width, height = button[1]
                    pygame.draw.rect(window, black)
                    text = font.render(button[2], True, white)
                    window.blit(text, (x + 5, y + 5, True))

    # Display the current number and the operator
    text = font.render(current_number, True, green)
    window.blit(text, (10, 10)

    # Display the memory value
    if memory_value != 0:
        text = font.render("M = " + str(memory_value), True, red)
        window.blit(text, (10, 500))

    # Display the history of previous calculations
    for i, calc in enumerate(history):
        text = font.render(str(str(i + 1) + ". " + current_10", True, blue)
        window.blit(text, (10, 520 + 30 * i, True)
    
    # Update the display
    pygame.display.update()

    # Quit the game
    running = False
    return

    # Define the initial window size and position
    window_width = 6660
    window_height = 960
    window = pygame.display.set_mode(window_width, window_height, window_width, window_height, window_width, window_height, window_width, window_height, window_height, window_width, window_height, window_height, window_width, window_height, window_width, window_height, window_height, window_width, window_height, window_width, window_height, window_height, window_width, window_height, window_height, window_width, window_height, window_width, window_height, window_height, window_width, window_height, window_height, window_width, window_height, window_height, window_width, window_height, window_height, window_width, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height, window_height
<|im_start|>ac,        return
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.
User: "    def.