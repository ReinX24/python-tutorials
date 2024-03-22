import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        # ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombieRandom:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults and random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()

class MyZombieBrains2:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break



class MyZombieShotGun2:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotGun = 0
        while diceRollResults is not None:
            shotGun += diceRollResults['shotgun']

            if shotGun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombie1To4ThenShotGun:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        runRec = 4
        diceRollResults = zombiedice.roll()
        shotGun = 0
        while diceRollResults is not None and runRec > 0:
            shotGun += diceRollResults['shotgun']
            runRec -= 1
            if shotGun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombiesMoreShotGunThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotGun = 0
        brains = 0
        while diceRollResults is not None:
            shotGun += diceRollResults['shotgun']
            brains += diceRollResults['brains']

            if shotGun <= brains:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    # MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
    MyZombieRandom(name='Random Bot'),
    MyZombieBrains2(name='Brain 2 Bot'),
    MyZombieShotGun2(name='ShotGun 2 Bot'),
    MyZombie1To4ThenShotGun(name='Pre Minded Bot'),
    MyZombiesMoreShotGunThanBrains(name='More ShotGun Zombie Bot'),
)
# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
