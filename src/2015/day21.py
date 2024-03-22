
class Unit:
    """
    Class to generalize a unit/player
    
    Args:
        hp (int): Hit points
        dmg (int): Damage value from weapon/rings
        defense (int): Defense value from armor/rings
        spend (int): Total currency spent for equipment

    Attributes:
        weapon (str): Weapon name
        armor (str): Armor name
        rings (list[str]): List of rings used (max of 2)
        store (dict): Dict containing available items
    """
    def __init__(self, hp: int = 0 , 
                 dmg: int = 0, 
                 defense: int = 0, 
                 spend: int = 0) -> None:
        self.hp = hp
        self.dmg = dmg
        self.defense = defense
        self.spend = spend

        self.weapon: str = ''
        self.armor: str = ''
        self.rings: list[str] = []

        self.store: dict = {
            'Dagger':{
                'type': 'weapon',
                'dmg': 4,
                'defense': 0,
                'cost': 8
            },
            'Shortsword':{
                'type': 'weapon',
                'dmg': 5,
                'defense': 0,
                'cost': 10
            },
            'Warhammer':{
                'type': 'weapon',
                'dmg': 6,
                'defense': 0,
                'cost': 25
            },
            'Longsword':{
                'type': 'weapon',
                'dmg': 7,
                'defense': 0,
                'cost': 40
            },
            'Greataxe':{
                'type': 'weapon',
                'dmg': 8,
                'defense': 0,
                'cost': 74
            },
            'Leather':{
                'type': 'armor',
                'dmg': 0,
                'defense': 1,
                'cost': 13
            },
            'Chainmail':{
                'type': 'armor',
                'dmg': 0,
                'defense': 2,
                'cost': 31
            },
            'Splintmail':{
                'type': 'armor',
                'dmg': 0,
                'defense': 3,
                'cost': 53
            },
            'Bandedmail':{
                'type': 'armor',
                'dmg': 0,
                'defense': 4,
                'cost': 75
            },
            'Platemail':{
                'type': 'armor',
                'dmg': 0,
                'defense': 5,
                'cost': 102
            },
            'Damage +1':{
                'type': 'ring',
                'dmg': 1,
                'defense': 0,
                'cost': 25
            },
            'Damage +2':{
                'type': 'ring',
                'dmg': 2,
                'defense': 0,
                'cost': 50
            },
            'Damage +3':{
                'type': 'ring',
                'dmg': 3,
                'defense': 0,
                'cost': 100
            },
            'Defense +1':{
                'type': 'ring',
                'dmg': 0,
                'defense': 1,
                'cost': 20
            },
            'Defense +2':{
                'type': 'ring',
                'dmg': 0,
                'defense': 2,
                'cost': 40
            },
            'Defense +3':{
                'type': 'ring',
                'dmg': 0,
                'defense': 3,
                'cost': 80
            },
        }
    
    def equip(self, item:str) -> None:
        """
        Function for equipping items based on the item catalog.
        Only 1 weapon and armor is allowed. For rings, up to 2 
        but no duplicates.

        Args:
            item (str): Name of the item to be availed
        """
        if item == '':
            return
        type = self.store[item]['type']
        if type == 'weapon':
            self.remove_item(self.weapon)
            self.weapon = item
        elif type == 'armor':
            self.remove_item(self.armor)
            self.armor = item
        elif type == 'ring':
            if item in self.rings:
                return
            elif len(self.rings) >= 2:
                self.remove_item(self.rings[0])
            self.rings.append(item)

        self.dmg += self.store[item]['dmg']
        self.defense += self.store[item]['defense']
        self.spend += self.store[item]['cost']
    
    def remove_item(self, item:str) -> None:
        """
        Removing items and their stats.

        Args:
            item (str): The item to be removed
        """
        
        if self.weapon == '' or self.armor == '':
            return
        type = self.store[item]['type']
        if type == 'weapon':
            self.weapon = ''
        if type == 'armor':
            self.armor = ''
        if type == 'ring':
            self.rings.pop(0)
        self.dmg -= self.store[item]['dmg']
        self.defense -= self.store[item]['defense']
        self.spend -= self.store[item]['cost']

    def show_items(self) -> None:
        """
        Function to view the current equipment and stats of unit
        """
        
        print()
        print(f'HP: {self.hp}')
        print(f'Weapon: {self.weapon}')
        print(f'Armor: {self.armor}')
        print(f'Rings: {self.rings}')
        print(f'Dmg: {self.dmg}')
        print(f'Def: {self.defense}')
        print(f'Spent: {self.spend}')
        print()

def fight(p1: Unit, p2: Unit) -> str:
    """
    For making the two units (player and boss) fight and 
    determining an outcome. P1 always hits first

    Args:
        p1 (Unit): Player 1
        p2 (Unit): Player 2 or Boss

    Returns:
        str: Outcome of fight either win or lose from p1 pov
    """

    while p1.hp > 0 or p2.hp > 0:

        # print(p1.hp, p2.hp)

        dmg_to_p2 = p1.dmg - p2.defense 
        p2.hp -= dmg_to_p2 if dmg_to_p2 > 0 else 1

        if p2.hp <= 0:
            print(f'Player wins spending {p1.spend}')
            return 'win'
        
        dmg_to_p1 = p2.dmg - p1.defense 
        p1.hp -= dmg_to_p1 if dmg_to_p1 > 0 else 1

        if p1.hp <= 0:
            print(f'Boss wins with player spending {p1.spend}')
            return 'lose'

def list_items(store: dict) -> list:
    """
    Utility function for listing the items 

    Args:
        store (dict): dict containing the info on each available item

    Returns:
        list: containing each weapon type's available items
    """
    weapons = []
    armors = ['']
    rings = ['', '']
    for m, n in store.items():
        if n['type'] == 'weapon':
            weapons.append(m)
        elif n['type'] == 'armor':
            armors.append(m)
        elif n['type'] == 'ring':
            rings.append(m)

    return [weapons, armors, rings]
    

if __name__ == '__main__':
    """
    Boss stats:

    Hit Points: 103
    Damage: 9
    Armor: 2
    """
    test_player = Unit()
    item_list = list_items(test_player.store)
    
    # For each item combination, make them fight and get the min or max
    # spend value depending on what is being asked
    spends_win = {}
    spends_lose = {}
    for weap in item_list[0]:
        for armor in item_list[1]:
            for ring1 in item_list[2]:
                for ring2 in item_list[2]:

                    combination = [weap, armor, ring1, ring2]

                    Player = Unit(hp=100)
                    Boss = Unit(hp=103, dmg=9, defense=2)
                    Player.equip(weap)
                    Player.equip(armor)
                    Player.equip(ring1)
                    Player.equip(ring2)
                    outcome = fight(Player, Boss)

                    if outcome == 'win':
                        spends_win[str(combination)] = Player.spend
                    
                    elif outcome == 'lose':
                        spends_lose[str(combination)] = Player.spend
    
    ## Part 1
    print()
    print(min(spends_win.items(), key=lambda x: x[1]))

    ## Part 2
    print()
    print(max(spends_lose.items(), key=lambda x: x[1]))
   




    
