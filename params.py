class Params:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    # Player start params
    PLAYER_START_X = SCREEN_WIDTH // 2
    PLAYER_START_Y = SCREEN_HEIGHT // 2
    #Player max params
    MAX_PLAYER_SPEED = 500
    MAX_PLAYER_SIZE = 200
    #Player min params
    PLAYER_RADIUS = 40
    PLAYER_SPEED = 100
    #Player increment
    PLAYER_SPEED_INCREMENT = 5
    PLAYER_SIZE_INCREMENT = 2

    # Food parameters
    FOOD_SIZE = 20

    # Trap parameters
    MIN_TRAP_SIZE = 40
    MAX_TRAP_SIZE = 150

    # Other game parameters
    FPS = 30
    CHRONO_START_TIME = 10
    SCORE_INCREMENT = 1

    # Colors
    FOOD_COLOR = (255, 0, 0)
    TRAP_COLOR = (0, 0, 255)  
    PLAYER_COLOR = (0, 255, 0)
    WHITE = (255, 255, 255)
    
    DIFFICULTY_SETTINGS = {
        "EASY": {"TrapCount": 2, "FoodCount": 5, "DecrementAmount": 2},
        "NORMAL": {"TrapCount": 3, "FoodCount": 3, "DecrementAmount": 3},
        "HARD": {"TrapCount": 4, "FoodCount": 2, "DecrementAmount": 4},
    }
