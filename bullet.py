""" bullet.py """
import pygame
from pygame.math import Vector2

from settings import Settings


class Bullet(pygame.sprite.Sprite):
    """A bullet fired by a player."""
    def __init__(self, start_pos, target_pos, damage, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/bullets/basic_bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=start_pos)
        self.position = Vector2(start_pos)
        self.target = Vector2(target_pos)
        self.speed = 5
        self.damage = damage
        self.velocity = self.calculate_velocity()
        self.sound = pygame.mixer.Sound(Settings().enemy_hit_sound)
        self.sound.play()

    def calculate_velocity(self):
        """Calculate the velocity of the bullet based on its target position"""
        direction = (self.target - self.position).normalize()
        velocity = direction * self.speed
        return velocity

    def update(self):
        """Update the position of the bullet"""
        self.position += self.velocity
        self.rect.center = self.position
        if self.position.distance_to(self.target) < 10 or not self.game.is_position_inside(self.position):
            self.kill()

    def is_position_inside(self, pos):
        """Check if the given position is inside the game screen"""
        return 0 <= pos.x <= self.game.settings.screen_width and 0 <= pos.y <= self.game.settings.screen_height
