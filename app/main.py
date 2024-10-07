from typing import Dict, Any
from app.knights import Knight
from app.battle import Battle


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def setup_knights(config: Dict) -> None:
    lancelot = Knight(**config["lancelot"])  # передача всіх параметрів
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])

    lancelot.apply_potion()
    arthur.apply_potion()
    mordred.apply_potion()
    red_knight.apply_potion()

    return lancelot, arthur, mordred, red_knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    lancelot, arthur, mordred, red_knight = setup_knights(knights_config)

    battle1 = Battle(lancelot, mordred)
    battle2 = Battle(arthur, red_knight)

    result1 = battle1.fight()
    result2 = battle2.fight()

    return {**result1, **result2}


print(battle(KNIGHTS))
