class Weapon:
    def __init__(self, number_of_bullets):
        self.bullets = number_of_bullets

    def shoot(self):
        if self.bullets:
            self.bullets -= 1
            return 'shooting...'
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)