import requests
import json
import re

api_request = requests.get("https://api.hypixel.net/v2/skyblock/bazaar").content

bazaar_pricing = json.loads(api_request)

enchantments = {}

enchantment_crafting_limits = {
    "ENCHANTMENT_PROTECTION": [1,5],
    "ENCHANTMENT_TURBO_COCO": [1,5],
    "ENCHANTMENT_CORRUPTION": [1,5],
    "ENCHANTMENT_CAYENNE": [4,5],
    "ENCHANTMENT_ENDER_SLAYER": False,
    "ENCHANTMENT_FIRE_ASPECT": False,
    "ENCHANTMENT_TURBO_CACTUS": [1,5],
    "ENCHANTMENT_SHARPNESS": False,
    "ENCHANTMENT_BIG_BRAIN": [3,5],
    "ENCHANTMENT_THUNDERLORD": False,
    "ENCHANTMENT_TURBO_MELON": [1,5],
    "ENCHANTMENT_MANA_STEAL": [1,3],
    "ENCHANTMENT_STRONG_MANA": [1,10],
    "ENCHANTMENT_HARDENED_MANA": [1,10],
    "ENCHANTMENT_TURBO_WARTS": [1,5],
    "ENCHANTMENT_EXPERIENCE": [1,3],
    "ENCHANTMENT_PALEONTOLOGIST": [1,5],
    "ENCHANTMENT_MANA_VAMPIRE": [1,10],
    "ENCHANTMENT_DELICATE": False,
    "ENCHANTMENT_PROSECUTE": [1,5],
    "ENCHANTMENT_CASTER": [1,5],
    "ENCHANTMENT_RESPITE": [1,5],
    "ENCHANTMENT_OVERLOAD": [1,5],
    "ENCHANTMENT_FIRE_PROTECTION": [1,5],
    "ENCHANTMENT_HARVESTING": [1,5],
    "ENCHANTMENT_DEDICATION": [1,3],
    "ENCHANTMENT_TRUE_PROTECTION": False,
    "ENCHANTMENT_LUCK_OF_THE_SEA": [1,5],
    "ENCHANTMENT_SMARTY_PANTS": [1,5],
    "ENCHANTMENT_LURE": [1,5],
    "ENCHANTMENT_FEROCIOUS_MANA": [1,10],
    "ENCHANTMENT_MAGNET": [1,5],
    "ENCHANTMENT_PESTERMINATOR": [1,5],
    "ENCHANTMENT_PROJECTILE_PROTECTION": [1,5],
    "ENCHANTMENT_CHAMPION": False,
    "ENCHANTMENT_DRAGON_HUNTER": [1,5],
    "ENCHANTMENT_CHARM": [1,5],
    "ENCHANTMENT_IMPALING": [1,3],
    "ENCHANTMENT_QUANTUM": [3,5],
    "ENCHANTMENT_REPLENISH": False,
    "ENCHANTMENT_TURBO_WHEAT": [1,5],
    "ENCHANTMENT_SILK_TOUCH": False,
    "ENCHANTMENT_SUGAR_RUSH": [1,3],
    "ENCHANTMENT_GROWTH": False,
    "ENCHANTMENT_EFFICIENCY": False,
    "ENCHANTMENT_FEATHER_FALLING": [6,10],
    "ENCHANTMENT_SMOLDERING": [1,5],
    "ENCHANTMENT_CRITICAL": [1,5],
    "ENCHANTMENT_TOXOPHILITE": False,
    "ENCHANTMENT_AIMING": [1,5],
    "ENCHANTMENT_FROST_WALKER": False,
    "ENCHANTMENT_THUNDERBOLT": False,
    "ENCHANTMENT_BLAST_PROTECTION": False,
    "ENCHANTMENT_ICE_COLD": [1,5],
    "ENCHANTMENT_COMPACT": False,
    "ENCHANTMENT_VENOMOUS": False,
    "ENCHANTMENT_CURSE_OF_VANISHING": False,
    "ENCHANTMENT_PRISTINE": [1,5],
    "ENCHANTMENT_LIFE_STEAL": False,
    "ENCHANTMENT_SMELTING_TOUCH": False,
    "ENCHANTMENT_PISCARY": False,
    "ENCHANTMENT_TURBO_MUSHROOMS": [1,5],
    "ENCHANTMENT_TABASCO": [2,3],
    "ENCHANTMENT_PUNCH": False,
    "ENCHANTMENT_PIERCING": False,
    "ENCHANTMENT_TITAN_KILLER": False,
    "ENCHANTMENT_POWER": False,
    "ENCHANTMENT_ANGLER": False,
    "ENCHANTMENT_THORNS": False,
    "ENCHANTMENT_VAMPIRISM": False,
    "ENCHANTMENT_CULTIVATING": False,
    "ENCHANTMENT_EXPERTISE": False,
    "ENCHANTMENT_CHANCE": False,
    "ENCHANTMENT_GREEN_THUMB": [1,5],
    "ENCHANTMENT_KNOCKBACK": False,
    "ENCHANTMENT_FIRST_STRIKE": False,
    "ENCHANTMENT_TURBO_PUMPKIN": [1,5],
    "ENCHANTMENT_DEPTH_STRIDER": False,
    "ENCHANTMENT_BLESSING": False,
    "ENCHANTMENT_SNIPE": False,
    "ENCHANTMENT_RESPIRATION": False,
    "ENCHANTMENT_REFLECTION": [1,5],
    "ENCHANTMENT_TRIPLE_STRIKE": False,
    "ENCHANTMENT_PROSPERITY": [1,5],
    "ENCHANTMENT_HECATOMB": False,
    "ENCHANTMENT_COUNTER_STRIKE": False,
    "ENCHANTMENT_WITHER_HUNTER": False,
    "ENCHANTMENT_SPIKED_HOOK": False,
    "ENCHANTMENT_LETHALITY": False,
    "ENCHANTMENT_CLEAVE": False,
    "ENCHANTMENT_REJUVENATE": [3,5],
    "ENCHANTMENT_VICIOUS": [3,5],
    "ENCHANTMENT_TURBO_CARROT": [1,5],
    "ENCHANTMENT_GIANT_KILLER": False,
    "ENCHANTMENT_AQUA_AFFINITY": False,
    "ENCHANTMENT_TURBO_CANE": [1,5],
    "ENCHANTMENT_FORTUNE": False,
    "ENCHANTMENT_FLAME": False,
    "ENCHANTMENT_DIVINE_GIFT": False,
    "ENCHANTMENT_FRAIL": False,
    "ENCHANTMENT_SYPHON": False,
    "ENCHANTMENT_EXECUTE": False,
    "ENCHANTMENT_INFINITE_QUIVER": [6,10],
    "ENCHANTMENT_SMITE": False,
    "ENCHANTMENT_LOOTING": False,
    "ENCHANTMENT_SCAVENGER": False,
    "ENCHANTMENT_CUBISM": False,
    "ENCHANTMENT_SUNDER": [1,5],
    "ENCHANTMENT_TRANSYLVANIAN": [4,5],
    "ENCHANTMENT_LUCK": False,
    "ENCHANTMENT_TURBO_POTATO": [1,5],
    "ENCHANTMENT_BANE_OF_ARTHROPODS": False
}

# regular expression pattern to extract the base enchantment name
pattern = re.compile(r"(ENCHANTMENT_[A-Z_]+)_\d+")

# iterate through the products in the bazaar pricing
for product_id, product_info in bazaar_pricing['products'].items():
    match = pattern.match(product_id)
    if match and "ULTIMATE" not in product_id:
        base_name = match.group(1)
        if base_name not in enchantments:
            enchantments[base_name] = {}
        enchantments[base_name][product_id] = product_info

#helper function, return # of enchant books
def calculate_books_needed(lower_level, higher_level):
    # Initialize the number of books needed
    books_needed = 1
    
    # Loop to calculate the number of books needed
    for level in range(lower_level, higher_level):
        books_needed *= 2
    
    return books_needed

#calculate margins for each craft
for base_name, levels in enchantments.items():
    lower_sell_price = -1
    lower_sell_volume = -1

    higher_buy_price = -1
    higher_buy_volume = -1

    # Error handling, skip bad crafts
    if base_name not in enchantment_crafting_limits:
        print("can't find", base_name)
        continue
    if enchantment_crafting_limits[base_name] == False:
        continue

    lower_level, higher_level = enchantment_crafting_limits[base_name]

    for product_id, product_info in levels.items():
        if product_id == f"{base_name}_{lower_level}": #lower enchant
            lower_buy_price = product_info["quick_status"]["sellPrice"]        
            lower_sell_volume = product_info["quick_status"]["buyMovingWeek"]
        if product_id == f"{base_name}_{higher_level}": #higher enchant
            higher_buy_price = product_info["quick_status"]["buyPrice"]
            higher_buy_volume = product_info["quick_status"]["sellMovingWeek"]

    needed_books = calculate_books_needed(lower_level, higher_level)

    total_buy_price = needed_books * lower_buy_price
    total_sell_price = higher_buy_price

    #skip small fish flips
    if total_buy_price < 1000:
        continue

    profit = total_sell_price - total_buy_price
    profit_margin = (profit / total_buy_price) * 100

    if profit > 1000000 and lower_sell_volume > 20 and higher_buy_volume > 20:
        print("")
        print("==== POTENTIAL FLIP ====")
        print(f"BUY: {needed_books} {base_name}_{lower_level} @ ${lower_buy_price:,.0f} || QUICKSELL (7d): {lower_sell_volume}")
        print(f"SELL: 1 {base_name}_{higher_level} @ ${higher_buy_price:,.0f} || QUICKBUY (7d): {higher_buy_volume}")
        print(f"TOTAL COST: ${total_buy_price:,.0f} || PROFIT: ${profit:,.0f} || PROFIT MARGIN: {round(profit_margin, 2)}%")