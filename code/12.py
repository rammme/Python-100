# 문제 12: 게임 캐릭터 클래스 만들기

class Wizard:
    def stat =(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()