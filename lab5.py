"""Demonstrate class of fighters"""
class Fighter:
    """
    Represents a fighter in the game.

    Attributes:
    - name: A string representing the name of the fighter.
    - health: An integer representing the health points of the fighter.
    - damage_per_attack: An integer representing the damage inflicted per attack by the fighter.
    """


    def __init__(self, name, health, damage_per_attack):
        """
        Initializes a Fighter object with a name, health, and damage per attack.

        Args:
        - name: A string representing the name of the fighter.
        - health: An integer representing the health points of the fighter.
        - damage_per_attack: An integer representing the damage inflicted per attack by the fighter.
        """
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def get_name(self):
        """
        Get the name of the fighter.

        Returns:
        - A string representing the name of the fighter.
        """
        return self.name

    def get_health(self):
        """
        Get the current health of the fighter.

        Returns:
        - An integer representing the health points of the fighter.
        """
        return self.health

    def get_damage_per_attack(self):
        """
        Get the damage per attack of the fighter.

        Returns:
        - An integer representing the damage inflicted per attack by the fighter.
        """
        return self.damage_per_attack

    def is_dead(self):
        """
        Check if the fighter is dead.

        Returns:
        - A boolean value indicating whether the fighter's health is less than or equal to 0.
        """
        return self.health <= 0


class Fight:
    """
    Represents a fight between two fighters.

    Attributes:
    - fighter1: A Fighter object representing the first fighter.
    - fighter2: A Fighter object representing the second fighter.
    """

    def __init__(self, fighter1, fighter2):
        """
        Initializes a Fight object between two fighters.

        Args:
        - fighter1: A Fighter object representing the first fighter.
        - fighter2: A Fighter object representing the second fighter.
        """
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def attack(self, attacker, target):
        """
        Simulates an attack by one fighter on another.

        Args:
        - attacker: A Fighter object representing the attacker.
        - target: A Fighter object representing the target of the attack.
        """
        target.health -= attacker.get_damage_per_attack()

    def check_draw(self):
        """
        Checks if the fight results in a draw.

        Returns:
        - A boolean value indicating whether the fight is a 
        draw based on fighters' health and damage per attack.
        """
        return (
            self.fighter1.get_health() == self.fighter2.get_health()
            and self.fighter1.get_damage_per_attack() == self.fighter2.get_damage_per_attack()
        )

    def start_fight(self):
        """
        Initiates the fight between two fighters and determines the winner.

        Returns:
        - If the fight is a draw: A string indicating "Draw".
        - If there is a winner: A tuple containing the name of the winner and the loser.
        """
        if self.check_draw():
            result1 = "Draw"
        else:
            while not self.fighter1.is_dead() and not self.fighter2.is_dead():
                self.attack(self.fighter1, self.fighter2)
                if not self.fighter2.is_dead():
                    self.attack(self.fighter2, self.fighter1)

            if self.fighter1.is_dead():
                result1 = (self.fighter2.get_name(), self.fighter1.get_name())

        return result1

# if __name__ == "__main__":
#     # Create two fighters
#     usyk = Fighter("Oleksandr Usyk", 60, 20)
#     dybua = Fighter("Dybua Den", 65, 20)

#     # Start the fight between the fighters
#     fight = Fight(usyk, dybua)
#     result = fight.start_fight()

#     # Determine and print the result of the fight
#     if result == "Draw":
#         print("Draw")
#     else:
#         winner, loser = result
#         print(f"The winner is {winner}")
#         print(f"The loser is {loser}")
