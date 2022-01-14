player_name = input('Ведите имя игрока')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}
enemy_name = input('Ведите имя врага')
enemy = {
    'name': enemy_name,
    'health': 100,
    'damage': 30,
    'armor': 1
}
def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

def get_damage(damage, armor):
    return damage / armor

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)