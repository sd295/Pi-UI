import os
import pygame
from pygame.locals import QUIT
import subprocess
import time

# Change the directory to a new path
new_directory = "d:/pi os/pi os"
os.chdir(new_directory)

# Print the current working directory to verify the change
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

pygame.init()
screen = pygame.display.set_mode((860, 860))  # Set the new screen size
pygame.display.set_caption("Booting Animation")
images = []
for i in range(10):  # Adjust the range based on the number of images
    image = pygame.image.load(f"boot_0.png").convert_alpha()
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
total_frames = 1 * 24 * 4  # 2 minutes * 60 seconds/minute * 4 frames/second

# Load the font for displaying the text
font = pygame.font.Font(None, 80)

while frame_index < total_frames:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Clear the screen

    # Draw the current image
    image = images[frame_index % len(images)]
    screen.blit(image, (0, (860 - new_height) // 2))  # Center the image vertically

    # Draw the text "pi" at the center of the screen
    text = font.render("pi os 0.0.0.3.1 ", True, (255, 255, 255))
    text_rect = text.get_rect(center=(430, 430))  # Center the text
    screen.blit(text, text_rect)

    # Display the loading dots
    loading_dots = "." * (frame_index % 4)
    loading_text = font.render(loading_dots, True, (255, 255, 255))
    loading_text_rect = loading_text.get_rect(center=(430, 500))  # Center the loading dots
    screen.blit(loading_text, loading_text_rect)

    pygame.display.update()

    # Update the frame index
    frame_index += 1

    # Adjust the frame rate (e.g., 4 frames per second)
    clock.tick(4)

# Wait for the animation to finish
time.sleep(24)  # Adjust the sleep duration if needed

# Open the homescreen.py file
current_dir = os.getcwd()
open_file_path = r"D:/pi os/pi os/homescreen.py"

# Replace the following line with the correct path to the Python interpreter
path_to_python_interpreter = "C:/Users/psori/AppData/Local/Microsoft/WindowsApps/python3.11.exe"
subprocess.Popen([path_to_python_interpreter, open_file_path])

# Quit pygame
pygame.quit()
exit()