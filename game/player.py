import pygame

class Player:
    def __init__(self, x, y, imageR, imageL, camera_x):
        self.imageR = imageR
        self.imageL = imageL
        self.image = self.imageR  # Inicialmente usar la imagen derecha
        self.rect = self.image.get_rect(topleft=(x, y))

        # Posición real (float)
        self.pos_x = float(x)
        self.pos_y = float(y)

        # Movimiento
        self.velocity_x = 0
        self.velocity_y = 0

        self.speed = 3
        self.jump_force = -10
        self.gravity = 0.5

        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()

        self.velocity_x = 0

        if keys[pygame.K_a]:
            self.velocity_x = -self.speed

        if keys[pygame.K_d]:
            self.velocity_x = self.speed

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_force

    def apply_gravity(self):
        self.velocity_y += self.gravity

    def move_horizontal(self, platforms):
        self.pos_x = min(max(0,self.pos_x +  self.velocity_x), 3000 - self.rect.width)
        self.rect.x = int(self.pos_x)

        if self.velocity_x > 0:
            self.image = self.imageR    
        elif self.velocity_x < 0:
            self.image = self.imageL

        for platform in platforms:
            if self.rect.colliderect(platform):

                if self.velocity_x > 0:
                    self.rect.right = platform.left
                elif self.velocity_x < 0:
                    self.rect.left = platform.right

                self.pos_x = self.rect.x

    def move_vertical(self, platforms):
        self.pos_y += self.velocity_y
        self.rect.y = int(self.pos_y)

        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform):

                if self.velocity_y > 0:
                    self.rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True

                elif self.velocity_y < 0:
                    self.rect.top = platform.bottom
                    self.velocity_y = 0

                self.pos_y = self.rect.y

    def update(self, platforms):
        self.handle_input()
        self.apply_gravity()
        self.move_horizontal(platforms)
        self.move_vertical(platforms)

    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))

    
    def change_image(self, image):
        self.image = image
