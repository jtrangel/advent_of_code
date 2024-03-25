class Unit:
    """
    Class to generalize a unit/player
    
    Args:
        hp (int): Hit points
        dmg (int): Damage value
        defense (int): Defense value
    """
    def __init__(self,
                 name: str, 
                 hp: int = 0,
                 mana: int = 0,  
                 dmg: int = 0, 
                 defense: int = 0) -> None:
        self.name = name
        self.hp = hp
        self.mana = mana
        self.dmg = dmg
        self.defense = defense

        self.effects: dict = {}   
    
    def parse_effects(self):
        """
        Effect parser at the start of rounds
        """
        for key, val in self.effects.items():
            if val > 0:
                self.effects[key] = val - 1
                take_effect(key, val, self)
            else:
                self.effects.pop(key)
                remove_effect(key, self)


class Boss(Unit):
    """
    Boss class
    """

    def __init__(self, 
                 name: str, 
                 hp: int = 0, 
                 dmg: int = 0) -> None:
        super().__init__(name=name, hp=hp, dmg=dmg)
    
    def attack(self, tgt:Unit):
        """
        Simple attack function

        Args:
            tgt (Unit): targeted unit
        """

        dmg_dealt = self.dmg - tgt.defense
        tgt.hp -= dmg_dealt if dmg_dealt > 0 else 1

        print(f'{self.name} attacks for {self.dmg} damage.')
    
    def show_stats(self) -> None:
        """
        Function to view the current stats of unit
        """
            
        print(f'- {self.name} has {self.hp} hp')

class Mage(Unit):
    """
    Class to define a Mage based on the unit class
    """

    def __init__(self, 
                 hp: int = 0, 
                 mana: int = 0,
                 name: str = '') -> None:
        super().__init__(hp=hp, mana=mana, name=name)

    def magic_missile(self, tgt: Unit) -> None:
        """
        Details for casting magic missile spell

        Args:
            tgt (Unit): Target the spell is casted on
        """
        
        dmg:int = 4
        cost:int = 53

        self.mana -= cost
        tgt.hp -= dmg

        print(f'{self.name} casts Magic Missile, dealing {dmg} damage.')
    
    def drain(self, tgt: Unit) -> None:
        """
        Details for casting drain spell

        Args:
            tgt (Unit): Target the spell is casted on
        """
        
        dmg:int = 2
        cost:int = 73
        heal:int = 2

        self.mana -= cost
        self.hp += heal
        tgt.hp -= dmg

        print(f'{self.name} casts Drain, dealing {dmg} damage, and healing {heal} hp.')
    
    def shield(self, tgt:Unit) -> None:
        """
        Details for casting drain spell

        Args:
            tgt (Unit): Target the spell is casted on
        """
        
        defense:int = 7
        cost:int = 73
        duration:int = 6 #turns

        self.mana -= cost
        tgt.effects.update({'shield': duration})

        print(f'{tgt.name} casts Shield, increasing armor by {defense}.')

    def poison(self, tgt: Unit) -> None:
        """
        Details for casting poison spell

        Args:
            tgt (Unit): Target the spell is casted on
        """
        
        cost:int = 173
        duration:int = 6 #turns

        self.mana -= cost
        tgt.effects.update({'poison': duration})

        print(f'{self.name} casts Poison on {tgt.name}.')
    
    def recharge(self, tgt:Unit) -> None:
        """
        Details for casting recharge spell

        Args:
            tgt (Unit): Target the spell is casted on
        """
        
        cost:int = 229
        duration:int = 5 #turns

        self.mana -= cost
        tgt.effects.update({'recharge': duration})

        print(f'{self.name} casts Recharge')
    
    def show_stats(self) -> None:
        """
        Function to view the current stats of unit
        """
            
        print(f'- {self.name} has {self.hp} hp, {self.defense} defense, {self.mana} mana')
    
###########################################

def take_effect(key:str, val:int, tgt:Unit) -> None:
    """
    Function to trigger effects. Used in parse_effects function

    Args:
        key (str): The effect name
        val (int): The number of turns left for the effect
        tgt (Unit): Target of the effect
    """
    
    if key == 'shield':
        defense:int = 7
        tgt.defense = defense

        print(f"Shield's timer is now {val}.")

    if key == 'poison':
        poison_dmg:int = 3
        tgt.hp -= poison_dmg

        print(f"Poison deals {poison_dmg} damage, its timer is now {val-1}.")

    if key == 'recharge':
        mana_regen:int = 101
        tgt.mana += mana_regen

        print(f'Recharge provides {mana_regen} mana; its timer is now {val-1}.')

def remove_effect(key:str, tgt: Unit):
    """
    Utility function for removing an effect. Only applies to static effects like Shield

    Args:
        key (str): The effect name
        tgt (Unit): Target of the effect
    """
    if key == 'shield':
        tgt.defense = 0


if __name__ == '__main__':
    """
    Hit Points: 58
    Damage: 9
    """

    # Player = Mage(name='Player', hp=10, mana=250)
    # Boss = Boss(name='Boss', hp=13, dmg=8)

    # #Player Turn
    # Player.show_stats()
    # Boss.show_stats()
    # Player.parse_effects()
    # Boss.parse_effects()
    # Player.poison(Boss)
    # print()

    # #Boss Turn
    # Player.show_stats()
    # Boss.show_stats()
    # Player.parse_effects()
    # Boss.parse_effects()
    # Boss.attack(Player)
    # print()

    # #Player Turn
    # Player.show_stats()
    # Boss.show_stats()
    # Player.parse_effects()
    # Boss.parse_effects()
    # Player.magic_missile(Boss)
    # print()

    # #Boss Turn
    # Player.show_stats()
    # Boss.show_stats()
    # Player.parse_effects()
    # Boss.parse_effects()
    # if Player.hp <=0 and Boss.hp > 0:
    #     print('Player dead')
    # if Boss.hp <=0 and Player.hp > 0:
    #     print('Boss dead')

    # print()


