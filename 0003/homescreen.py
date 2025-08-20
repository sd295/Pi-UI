import pygame
from pygame import QUIT

pygame.init()
screen = pygame.display.set_mode((860, 860))
pygame.display.set_caption("Booting Animation")

images = []
for i in range(10):  # Adjust the range based on the number of images
    image = pygame.image.load(f"boot_0.png").convert_alpha()
    original_width, original_height = image.get_size()
    aspect_ratio = original_width / original_height
    new_height = int(860 / aspect_ratio)
    resized_image = pygame.transform.scale(image, (860, new_height))
    images.append(resized_image)

clock = pygame.time.Clock()
frame_index = 0
total_frames = 2 * 1 * 1  # 2 minutes * 60 seconds/minute * 60 frames/second
clock.tick(4)

while frame_index < total_frames:
    for event in pygame.event.get():
        if event.type == QUIT:
            break  # Exit the loop instead of quitting pygame

    # Rest of the code...