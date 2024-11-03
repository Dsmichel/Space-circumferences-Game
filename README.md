# Space Circumferences Game

This is a space-themed game project developed in Python using the PyGame library. The objective of the game is to destroy as many enemy circles as possible, advancing through increasingly challenging levels. Each level increases the number of enemies and their speed, and the player must avoid collisions to keep their circle safe.

## Table of Contents
1. [Game Features](#game-features)
2. [Instructions](#instructions)
3. [Game Modes](#game-modes)
4. [Code Structure](#code-structure)
5. [Requirements](#requirements)
6. [Running the Game](#running-the-game)

## Game Features

- Mouse control for the player’s circle.
- Shooting by clicking the left mouse button.
- Score and level displayed in the upper-right corner.
- Progressive difficulty: each level adds more enemies and increases their speed.
- Custom background image.
- Four game modes: menu, game, pause (after clearing a level), and game over.

## Instructions

- **Move the circle**: Control the circle by moving the mouse.
- **Shoot**: Left-click to shoot projectiles at enemies.
- **Avoid Collisions**: Make sure enemies do not collide with your circle. If they do, the game is over.

## Game Modes

The game includes the following modes:

1. **Menu**: Displays the game title and instructions. Press `SPACE` to start.
2. **Game**: Control the circle, shoot enemies, and avoid collisions. Each defeated enemy increases the score.
3. **Pause**: Appears after completing a level, congratulating the player and prompting them to press `SPACE` to advance to the next level.
4. **Game Over**: Shows the final score and level reached after the player’s circle collides with an enemy. Press `SPACE` to return to the menu and restart the game.

## Code Structure

The project is organized with the following primary functions:

- **menu()**: Draws the menu screen and displays instructions.
- **game()**: Runs the main gameplay, controlling the circle’s position, projectiles, and collision detection.
- **pause()**: Shows a pause screen after clearing a level.
- **game_over()**: Displays the game-over screen when the player loses.
- **generate_enemies()**: Generates a list of enemies at the start of each level.
- **update_enemies()**: Updates the position of the enemies, respawning them at the top if they reach the bottom of the screen.
- **check_collisions()**: Checks for collisions between projectiles and enemies, as well as between the player and enemies.

## Requirements

- Python 3.x
- PyGame
- random

To install PyGame, run "pip install pygame"
