import pygame

class NPC:
    def __init__(self, x, y, imageR, imageL, speed, camera_x):
        self.imageR = imageR
        self.imageL = imageL
        self.image = self.imageL  # Inicialmente usar la imagen derecha
        self.rect = self.image.get_rect(topleft=(x, y))

        # Posición real en float
        self.pos_x = float(x)
        self.pos_y = float(y)

        self.speed = speed
        self.direction = -1

        self.velocity_y = 0
        self.gravity = 0.5
        self.on_ground = False

    def move_horizontal(self, platforms):
        if self.direction == 1:
            self.image = self.imageR
        else:
            self.image = self.imageL

        self.pos_x += self.speed * self.direction
        self.rect.x = int(self.pos_x)

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.direction == 1:
                    self.rect.right = platform.left
                else:
                    self.rect.left = platform.right

                self.pos_x = self.rect.x  # Sincronizar float
                self.direction *= -1
                break

    def apply_gravity(self, platforms):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

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




    def handle_collisions(self, platforms):
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform):

                # Colisión vertical (caer sobre plataforma)
                if self.velocity_y > 0:
                    self.rect.bottom = platform.top - 5
                    self.velocity_y = 0
                    self.on_ground = True

                # Colisión horizontal
                if self.direction == 1:
                    self.rect.right = platform.left
                    self.direction = -1
                else:
                    self.rect.left = platform.right
                    self.direction = 1

    def update(self, platforms):
        self.move_horizontal(platforms)
        self.handle_collisions(platforms)
        self.apply_gravity(platforms)
        
    
    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
