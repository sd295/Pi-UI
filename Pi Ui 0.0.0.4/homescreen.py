import subprocess
import pygame
import os
from pygame import QUIT
new_directory = "d:/pi os/pi os"
os.chdir(new_directory)

# Open the calculatorlogo.py file
current_dir = os.getcwd()
open_file_path = r"D:/pi os/pi os/calculatorlogo.html"

# Replace the following line with the correct path to the Python interpreter
path_to_python_interpreter = "C:/Users/psori/AppData/Local/Microsoft/WindowsApps/python3.11.exe"

pygame.init()
screen = pygame.display.set_mode((660, 960))  # Set the new screen size
pygame.display.set_caption("Booting Animation")
images = []
for i in range(10):  # Adjust the range based on the number of images
    image = pygame.image.load(f"piui0004WALL.png").convert_alpha()
    # Calculate the new height based on the desired width and the original aspect ratio
    original_width, original_height = image.get_size()
    aspect_ratio = original_width / original_height
    new_height = int(860 / aspect_ratio)
    # Resize the image to the new size (860xnew_height)
    resized_image = pygame.transform.scale(image, (860, new_height))
    images.append(resized_image)
clock = pygame.time.Clock()
frame_index = 0

# Calculate the number of frames to display for 2 minutes
total_frames = 90000 * 2400000000 * 4000  # 2 minutes * 60 seconds/minute * 4 frames/second

# Load the font for displaying the text
font = pygame.font.Font(None, 80)

# Add a button to the screen
button_rect = pygame.Rect(300, 700, 100, 50)

# Draw the button
pygame.draw.rect(screen, (255, 255, 255), button_rect)
pygame.draw.polygon(screen, (0, 0, 0), ((button_rect.centerx, button_rect.centery), (button_rect.left + 50, button_rect.centery), (button_rect.right - 50, button_rect.centery)))

# Main game loop
while frame_index < total_frames:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit

    screen.fill((0, 0, 0))  # Clear the screen

    # Display the loading dots

    pygame.display.update()

    # Update the frame index
    frame_index += 1

    # Adjust the frame rate (e.g., 4 frames per second)
    clock.tick(4)

    # Check if the button is being clicked
    if pygame.mouse.get_pressed()[0] and button_rect.collidepoint(pygame.mouse.get_pos()):
        # Open the specified file
        open_file_path = "D:/pi os/pi os/homescreen.py"
        path_to_python_interpreter = "C:/Users/psori/AppData/Local/Microsoft/WindowsApps/python3.11.exe"

        # Replace the following line with the correct path to the Python interpreter
        # path_to_python_interpreter = "C:/Users/psori/AppData/Local/Microsoft/WindowsApps/python3.11.exe"

        # Use the subprocess module to open the specified file
        subprocess.Popen([path_to_python_interpreter, open_file_path])

# Display the button on the screen
pygame.display.update() 

def close_window():
    pygame.quit()
    exit()
    
close_window() 
if pygame.WINDOWCLOSE == close_window():
    pygame.quit()
    exit()
    
