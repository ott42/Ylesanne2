import pygame

# Initialize Pygame
pygame.init()

# Set the size of the window
size = (640, 480)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Shop Game")

# Load the images
seller_image = pygame.image.load("seller.png")
bg_shop_image = pygame.image.load("bgshop.jpg")
chat_image = pygame.image.load("chat.png")

# Draw the images
screen.blit(bg_shop_image, (1, 1))
screen.blit(seller_image, (10, 50))
screen.blit(chat_image, (525, 50))




# Update the screen
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Exit Pygame
pygame.quit()
