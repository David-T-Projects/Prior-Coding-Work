##################################################################################
#D&D Random Character Sheet Generator
#Author: David Tollett
#Notes: Generates a randomized Character Sheet, all the user needs to input is a 
#desired level. Everything else is dynamically generated.
##################################################################################

import math
from random import *
global PC_prof_bonus
PC_prof_bonus = 2

global PC_str_savethrw
PC_str_savethrw = 0
global PC_dex_savethrw
PC_dex_savethrw = 0
global PC_con_savethrw
PC_con_savethrw = 0
global PC_int_savethrw
PC_int_savethrw = 0
global PC_wis_savethrw
PC_wis_savethrw = 0
global PC_cha_savethrw
PC_cha_savethrw = 0


global PC_str_mod
PC_str_mod = 0
global PC_dex_mod
PC_dex_mod = 0
global PC_con_mod
PC_con_mod = 0
global PC_int_mod
PC_int_mod = 0
global PC_wis_mod
PC_wis_mod = 0
global PC_cha_mod
PC_cha_mod = 0
global PC_hp
PC_hp = 0

global Strength
global Dexterity
global Constitution
global Intelligence
global Charisma
global Wisdom

Strength = 0
Dexterity = 0
Constitution = 0
Intelligence = 0
Charisma = 0
Wisdom = 0



global acrobatics 
acrobatics = 0
global athletics
athletics = 0
global animal_handling 
animal_handling = 0
global arcana 
arcana = 0
global deception
deception = 0
global history
history = 0
global insight
insight = 0
global intimidation
intimidation = 0
global investigation
investigation = 0
global medicine
medicine = 0
global nature
nature = 0
global preception
preception = 0
global performance
performance = 0
global persuasion
persuasion = 0
global religion
religion = 0
global sleight_of_hand
sleight_of_hand = 0
global stealth
stealth = 0
global survival
survival = 0

global common
global dwarvish
global elvish
global giant
global gnomish
global goblin
global halfing
global orc
global abyssal
global celestial
global draconic
global deep_speech
global infernal
global primordial
global sylvan
global undercommon
global aquan
global auran
global keldon
global druidic

            
common = 0
dwarvish = 0
elvish = 0
giant = 0
gnomish = 0
goblin = 0
halfing = 0
orc = 0
abyssal = 0
celestial = 0
draconic = 0
deep_speech = 0
infernal = 0
primordial = 0
sylvan = 0
undercommon = 0
aquan = 0
auran = 0
keldon = 0
druidic = 0

global artisan_tools
global disguise_kit
global forgery_kit
global gaming_set
global herbalism_kit
global musical_instrument
global navigator_tools
global poisoner_kit
global thief_tools
global vehicles_land
global vehicles_water


artisan_tools = 0
disguise_kit = 0
forgery_kit = 0
gaming_set = 0
herbalism_kit = 0
musical_instrument = 0
navigator_tools = 0
poisoner_kit = 0
thief_tools = 0
vehicles_land = 0
vehicles_water = 0

global light_armor
light_armor = 0

global medium_armor
medium_armor = 0

global heavy_armor
heavy_armor = 0

global simple_weapons
simple_weapons = 0

global martial_weapons
martial_weapons = 0

global battleaxe
battleaxe = 0

global handaxe
handaxe = 0

global light_hammer
light_hammer = 0

global war_hammer
war_hammer = 0

global shields
shields = 0

global rapier
rapier = 0

global shortsword
shortsword = 0

global hand_crossbow
hand_crowwbow = 0

global spear
spear = 0

global trident
trident = 0

global light_crossbow
light_crossbow = 0

global net
net = 0

global longsword
longsword = 0

global longbow
longbow = 0

global shortbow
shortbow = 0

global scimitar
scimitar = 0

global club
club = 0

global daggers
daggers = 0

global darts
darts = 0

global javelins
javelins = 0

global maces
maces = 0

global quarterstaffs
quarterstaffs  = 0

global sickles
sickles = 0

global slings
slings = 0

global size
size = ""

global speed
speed = 30

global feature 
feature = " "

global background_equipment
background_equipment = " "

global class_equipment
class_equipment = " "

global class_equipment2
class_equipment2 = " "

global class_equipment3
class_equipment3 = " "

global class_equipment4
class_equipment4 = " "

global class_equipment5
class_equipment5 = " "

global PC_subrace
PC_subrace = ""

global PC_subclass
PC_subclass = ""

global hit_dice
hit_dice = ""

global human_feat
human_feat = ""

global feat1
global feat2
global feat3
global feat4
global feat5
global feat6

feat1 = ""
feat2 = ""
feat3 = ""
feat4 = ""
feat5 = ""
feat6 = ""
feat7 = ""

global race_feature1
race_feature1 = ""
global race_feature2
race_feature2 = ""
global race_feature3
race_feature3 = ""
global race_feature4
race_feature4 = ""
global race_feature5
race_feature5 = ""
global race_feature6
race_feature6 = ""
global race_feature7
race_feature7 = ""

global class_feature1
class_feature1 = ""
global class_feature2
class_feature2 = ""
global class_feature3
class_feature3 = ""
global class_feature4
class_feature4 = ""
global class_feature5
class_feature5 = ""
global class_feature6
class_feature6 = ""
global class_feature7
class_feature7 = ""
global class_feature8
class_feature8 = ""
global class_feature9
class_feature9 = ""
global class_feature10
class_feature10 = ""
global class_feature11
class_feature11 = ""
global class_feature12
class_feature12 = ""
global class_feature13
class_feature13 = ""
global class_feature14
class_feature14 = ""
global class_feature15
class_feature15 = ""
global class_feature16
class_feature16 = ""
global class_feature17
class_feature17 = ""

global caster
caster = "False"

global cantrip1
global cantrip2
global cantrip3
global cantrip4
global cantrip5
global cantrip6
global cantrip7

cantrip1 = ""
cantrip2 = ""
cantrip3 = ""
cantrip4 = ""
cantrip5 = ""
cantrip6 = ""
cantrip7 = ""
global level_1_spell1
global level_1_spell2
global level_1_spell3
global level_1_spell4
global level_1_spell5
global level_1_spell6

level_1_spell1 = ""
level_1_spell2 = ""
level_1_spell3 = ""
level_1_spell4 = ""
level_1_spell5 = ""
level_1_spell6 = ""

global level_2_spell1
global level_2_spell2
global level_2_spell3


level_2_spell1 = ""
level_2_spell2 = ""
level_2_spell3 = ""


global level_3_spell1
global level_3_spell2
global level_3_spell3


level_3_spell1 = ""
level_3_spell2 = ""
level_3_spell3 = ""

global level_4_spell1
global level_4_spell2
global level_4_spell3


level_4_spell1 = ""
level_4_spell2 = ""
level_4_spell3 = ""


global level_5_spell1
global level_5_spell2
global level_5_spell3


level_5_spell1 = ""
level_5_spell2 = ""
level_5_spell3 = ""

global level_6_spell1
global level_6_spell2


level_6_spell1 = ""
level_6_spell2 = ""

global level_7_spell1
global level_7_spell2


level_7_spell1 = ""
level_7_spell2 = ""

global level_8_spell1
level_8_spell1 = ""

global level_9_spell1
level_9_spell1 = ""



def solo_skill():

        global acrobatics 
        global animal_handling 
        global arcana
        global athletics 
        global deception
        global history
        global insight
        global intimidation
        global investigation
        global medicine
        global nature
        global preception
        global performance
        global persuasion
        global religion
        global sleight_of_hand
        global stealth
        global survival
        


        skill1 = randint(1,17)

        while(1):
            if skill1 == 1 and acrobatics == 1:
               skill1 = randint(1,17)
                
            if skill1 == 2 and animal_handling == 1:
               skill1 = randint(1,17)
               
            if skill1 == 3 and arcana == 1:
               skill1 = randint(1,17)
               
            if skill1 == 4 and deception == 1:
               skill1 = randint(1,17)

            if skill1 == 5 and history == 1:
               skill1 = randint(1,17)

            if skill1 == 6 and insight == 1:
               skill1 = randint(1,17)

            if skill1 == 7 and intimidation == 1:
               skill1 = randint(1,17)

            if skill1 == 8 and investigation == 1:
               skill1 = randint(1,17)
   
            if skill1 == 9 and  medicine == 1:
               skill1 = randint(1,17)

            if skill1 == 10 and nature == 1:
               skill1 = randint(1,17)

            if skill1 == 11 and preception == 1:
               skill1 = randint(1,17)

            if skill1 == 12 and performance == 1:
               skill1 = randint(1,17)

            if skill1 == 13 and persuasion == 1:               
               skill1 = randint(1,17)

            if skill1 == 14 and religion == 1:
               skill1 = randint(1,17)

            if skill1 == 15 and sleight_of_hand == 1:
               skill1 = randint(1,17)

            if skill1 == 16 and stealth == 1:
               skill1 = randint(1,17)

            if skill1 == 17 and survival == 1:
               skill1 = randint(1,17)

            if skill1 == 18 and athletics == 1:
               skill1 = randint(1,17)

            else:
                break


       if skill1 == 1:
            acrobatics = 1
            return "acrobatics"
        if skill1 == 2:
           animal_handling = 1
           return "animal_handling"
        if skill1 == 3:
           arcana = 1
           return "arcana"
        if skill1 == 4:
           deception = 1
           return " deception"
        if skill1 == 5:
           history = 1
           return "history"
        if skill1 == 6:
          insight = 1
          return "insight"
        if skill1 == 7:
           intimidation = 1
           return "intimidatio"
        if skill1 == 8:
           investigation = 1
           return  "investigation"
        if skill1 == 9:
           medicine = 1
           return "medicine"
        if skill1 == 10:
           nature = 1
           return "nature"
        if skill1 == 11:
           preception = 1
           return "preception"
        if skill1 == 12:
           performance = 1
           return "[erformance"
        if skill1 == 13:
           persuasion = 1
           return "persuasion"
        if skill1 == 14:
            religion = 1
            return "religion"
        if skill1 == 15:
            sleight_of_hand = 1
            return "sleight_of_hand"
        if skill1 == 16:
            stealth = 1
            return "stealth"
        if skill1 == 17:
            survival = 1
            return "survival"
        if skill1 == 18:
            athletics = 1
            return "athletics"

def solo_lang():
        global common
        global dwarvish
        global elvish
        global giant
        global gnomish
        global goblin
        global halfing
        global orc
        global abyssal
        global celestial
        global draconic
        global deep_speech
        global infernal
        global primordial
        global sylvan
        global undercommon

        lang2 = randint(1,16)
        if lang2 == 1:
           common = 1
           return "common"
        if lang2 == 2:
           dwarvish = 1
           return "dwarvish"
        if lang2 == 3:
          elvish = 1
          return "elvish"
        if lang2 == 4:
           giant = 1
           return "giant"
        if lang2 == 5:
          gnomish = 1
          return "gnomish"
        if lang2 == 6:
          goblin = 1
          return "goblin"
        if lang2 == 7:
           halfing = 1
           return "halfling"
        if lang2 == 8:
           orc = 1
           return "orc"
        if lang2 == 9:
           abyssal = 1
           return "abyssal"
        if lang2 == 10:
           celestial = 1
           return "celestial"
        if lang2 == 11:
           draconic = 1
           return "draconic"
        if lang2 == 12:
           deep_speech = 1
           return "deep_speech"
        if lang2 == 13:
           infernal = 1
           return "infernal"
        if lang2 == 14:
            primordial = 1
            return "primordial"
        if lang2 == 15:
            sylvan = 1
            return "sylvan"
        if lang2 == 16:
            undercommon = 1
            return "undercommon"

def feat():
     choice = randint(1,93)
     feat_list = {
        1:"Actor",
        2:"Alert",
        3:"Artificer Initiate",
        4: "Athlete",
        5: "Charger",
        6: "Chef",
        7: "Crossbow Expert",
        8: "Crusher",
        9: "Defensive Duelist",
        10: "Dual Wielder",
        11: "Dungeon Delver",
        12: "Durable",
        13: "Eldritch Adept",
        14: "Elemental Adept",
        15: "Fey Touched",
        16: "Fighting Initiate",
        17: "Grappler",
        18: "Great Weapon Master",
        19: "Gunner",
        20: "Healer",
        21: "Heavily Armored",
        22: "Heavy Armor Master",
        23: "Inspiring Leader",
        24: "Keen Mind",
        25: "Lightly Armored",
        26: "Linguist",
        27: "Lucky",
        28:" Mage Slayer",
        29: "Magic Initiate",
        30:" Martial Adept",
        31: "Medium Armor Master",
        32: "Metamagic Adept",
        33: "Mobile",
        34: "Moderately Armored",
        35: "Mounted Combatant",
        36: "Observant",
        37: "Piercer",
        38: "Poisoner",
        39: "Polearm Master",
        40: "Resilient",
        41: "Ritual Caster",
        42: "Savage Attacker",
        43: "Sentinel",
        44: "Shadow Touched",
        45: "Sharpshooter",
        46:"Shield Master",
        47: "Skill Expert",
        48: "Skilled",
        49: "Skulker",
        50: "Slasher",
        51: "Spell Sniper",
        52: "Tavern Brawler",
        53: "Telekinetic",
        54: "Telepathic",
        55: "Tough",
        56: "War Caster",
        57: "Weapon Master",
        58: "Acrobat",
        59: "Alchemist",
        60: "Animal Handler",
        61: "Arcanist",
        62: "Blade Mastery",
        63: "Brawny",
        64: "Burglar",
        65: "Diplomat",
        66: "Empathic",
        67: "Fell Handed",
        68: "Flail Mastery",
        69: "Gourmand",
        70: "Greater Dragonmark",
        71: "Historian",
        72: "Investigator",
        73: "Master of Disguise",
        74: "Medic",
        75: "Menacing",
        76: "Metabolic Control",
        77: "Naturalist",
        78: "Perceptive",
        79: "Performer",
        80: "Practiced Expert",
        81: "Quick-Fingered",
        82: "Shield Training",
        83: "Silver-Tongued",
        84: "Spear Mastery",
        85: "Stealthy",
        86: "Survivalist",
        87: "Tandem Tactician",
        88: "Theologian",
        89: "Tower of Iron Will",
        90: "Tracker",
        91: "Wild Talent",
        92: "Servo Crafting",
        93: "Quicksmithing",
      }
     return feat_list[choice]

def statroll():

   die1 = randint(1,6)
   die2 = randint(1,6)
   die3 = randint(1,6)
   stat_total = die1 + die2 + die3
   return stat_total

def modifier(int):

    if int == 1:
        mod =-5
        return mod
    
    if int == 2 or int == 3:
        mod = -4
        return mod

    if int == 4 or int == 5:
        mod = -3
        return mod

    if int == 6 or int == 7:
        mod = -2
        return mod

    if int == 8 or int == 9:
        mod = -1
        return mod

    if int == 10 or int == 11:
        mod = 0
        return mod

    if int == 12 or int == 13:
        mod = 1
        return mod

    if int == 14 or int == 15:
        mod = 2
        return mod

    if int == 16 or int == 17:
        mod = 3
        return mod

    if int == 18 or int == 19:
        mod = 4
        return mod

    if int == 20 or int == 21:
        mod = 5
        return mod

    if int == 22 or int == 23:
        mod = 6
        return mod

    if int == 24 or int == 25:
        mod = 7
        return mod

    if int == 26 or int == 27:
        mod = 8
        return mod

    if int == 28 or int == 29:
        mod = 9
        return mod

    if int == 30:
        mod = 10
        return mod

def class_selection():
    choice = randint(1,11)
    
    classes = {
        1: "Barbarian",
        2: "Bard",
        3: "Cleric",
        4: "Druid",
        5: "Fighter",
        6: "Monk",
        7: "Paladin",
        8: "Ranger",
        9: "Rouge",
        10: "Sorcerer",
        11: "Warlock",
        12: "Wizard",
        }
    return classes[choice]

def race():
    choice = randint(1,9)

    races = {
        1: "Dragonborn",
        2: "Dwarf",
        3: "Elf",
        4: "Gnome",
        5: "Half-Elf",
        6: "Halfling",
        7: "Half-Orc",
        8: "Human",
        9: "Tiefling",}

    return races[choice]

def allingment():
    choice = randint(1,9)

    allingments = {
        1: "Lawful Good",
        2: "Lawful Neutral",
        3: "Lawful Evil",
        4: "Neutral Good",
        5: "True Neutral",
        6: "Neutral Evil",
        7: "Chaotic Good",
        8: "Chaotic Neutral",
        9: "Chaotic Evil",}
    return allingments[choice]
    

def background():
    choice = randint(1,14)

    backgrounds = {
        1: "Acolyte",
        2: "Charlatan",
        3: "Criminal/Spy",
        4: "Entertainer",
        5: "Folk Hero",
        6: "Urban Bounty Hunter",
        7: "Guild Artisan/Guild Merchant",
        8: "Hermit",
        9: "Knight/Noble",
        10: "Outlander",
        11: "Pirate/Sailor",
        12: "Sage",
        13: "Soldier",
        14: "Urchin",
        }

    if choice == 1:
        global insight 
        insight = 1
        global religion 
        religion = 1
        global feature
        feature = "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle.\nYou might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple."
        global background_equipment
        background_equipment = "A holy symbol, a prayer book/wheel, 5 sticks on incense, vestments, a set of common clothes, pouch of 15gp"

        lang1 = solo_lang()
        lang2 = solo_lang()
        while lang1 == lang2:
            lang2 = solo_lang()

        return backgrounds[1]

    if choice == 2:
        global deception 
        deception = 1
        global sleight_of_hand
        sleight_of_hand = 1

        feature = "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."

        background_equipment = "A set of fine clothes, a disguise kit, tools of the con of your choice(ten stopped bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke, and a belt pouch containing 15gp"

        global disguise_kit
        disguise_kit = 1

        global forgery_kit
        forgery_kit = 1
       
        return backgrounds[2]


    if choice == 3:
        deception = 1
        global stealth
        stealth = 1
        global gaming_set
        gaming_set = 1
        global thief_tools
        thief_tools = 1
        background_equipment = "A crowbar, a set of dark common clothes inccluding a hood, and a pouch containing 15gp"
        feature = "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."
        return backgrounds[3]

    if choice == 4:
        global acrobatics
        acrobatics = 1
        global performance
        performance = 1
        disguise_kit = 1
        global musical_instrument
        musical_instrument = 1
        background_equipment = "A musical instrument of your choice, favor of an admirer(love letter, lock of hair, or trinket), a costume, and a pouch containing 15gp"
        feature = "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."
        return backgrounds[4]

    if choice == 5:
        global animal_handling
        animal_handling = 1
        global survival
        survival = 1
        global artisan_tools
        artisan_tools = 1
        global vehicles_land
        vehicles_land = 1
        feature = "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."
        background_equipment = "A set of artisan's tools of your choice, a shovel, an iron pot, a set of common clothes, and a pouch containing 10 gp"
        return backgrounds[5]

    if choice == 6:
        skill1 = randint(1,4)
        skill2 = randint(1,4)
        while skill2 == skill1:
            skill2 = randint(1,4)

        if skill1 == 1:
            deception = 1
        if skill1 == 2:
            insight = 1
        if skill1 == 3:
            global persuasion
            persuasion = 1
        if skill1 == 4:
            stealth = 1

        if skill2 == 1:
            deception = 1
        if skill2 == 2:
            insight = 1
        if skill2 == 3:
            persuasion = 1
        if skill2 == 4:
            stealth = 1

        tool1 = randint(1,3)
        tool2 = randint(1,3)
        while tool2 == tool1:
            tool2 = randint(1,4)

        if tool1 == 1:
          thief_tools = 1
        if tool1 == 2:
            gaming_set = 1
        if tool1 == 3:
           musical_instrument = 1

        if tool2 == 1:
            thief_tools = 1
        if tool2 == 2:
            gaming_set = 1
        if tool2 == 3:
            musical_instrument = 1
        feature = "As a bounty hunter, you have strong and deep connections with dozens of people in the community. The background of these people might have them coming from a criminal and mafia underworld or the rough and rowdy street gang folks of the streets or the members of a high and noble society circle.\nThis connection is established whenever you visit a city as there is bound to be contact and interactions with people of that city, people you make connections with will be willing to give you high grade valuable information about the people and society there and the commonly visited yet important places in that area."
        return backgrounds[6]

    if choice == 7:
        background_option = randint(1,2)

        if background_option == 1:
            insight = 1
            persuasion = 1 
            artisan_tools = 1
            lang1 = solo_lang()

            feature = "As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings.\nGuilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers.\nYou must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces."
            background_equipment = " A set of artisan's tools (one of your choice), a letter of introduction from your guild, a set of traveler's clothes, and a belt pouch containing 15gp"

        if background_option == 2: #Merchant
            insight = 1
            persuasion = 1
            lang1 = solo_lang()

            tool_choice = randint(1,2)
            if tool_choice == 1:
                global navigator_tools
                navigator_tools = 1
               
            if tool_choice == 2:
                lang2 = solo_lang()
                while lang1 == lang2:
                    lang2 = solo_lang()
                
                feature = "As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings.\nGuilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers.\nYou must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces."
                background_equipment = " A mule and cart, a letter of introduction from your guild, a set of traveler's clothes, and a belt pouch containing 15gp"
            
        return backgrounds[7]

    if choice == 8:
        global medicine
        medicine = 1
        religion = 1
        global herbalism_kit
        herbalism_kit = 1
        solo_lang()

        background_equipment = " A scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, an herbalism kit, and 5gp"
        feature = "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society."

        return backgrounds[8]

    if choice == 9:

        persuasion = 1
        global history
        history = 1
        gaming_set = 1
        solo_lang()

        background_equipment = " A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25gp"

        feature_option = randint(1,2)

        if feature_option == 1:
            feature = "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."

        if feature_option == 2:
            feature = "You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused."


        return backgrounds[9]

    if choice == 10:

        global athletics
        athletics = 1
        survival = 1
        musical_instrument = 1
        solo_lang()

        background_equipment = " A staff, a hunting trap, a trophy from an animal you killed, a set of traveler's clothes, and a belt pouch containing 10gp"
        feature = "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."

        return backgrounds[10]

    if choice == 11:

        athletics = 1
        global pepreception
        preception = 1
        navigator_tools = 1
        global vehicles_water
        vehicles_water = 1
        background_equipment = " belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a small stone with a hole in the center,a set of common clothes, and a belt pouch containing 10gp "

        feature_option = randint(1,2)

        if feature_option == 1:
            feature = "When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your DM will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."

        if feature_option == 2:
            feature = "No matter where you go, people are afraid of you due to your reputation. When you are in a civilized settlement, you can get away with minor criminal offenses, such as refusing to pay for food at a tavern or breaking down doors at a local shop, since most people will not report your activity to the authorities."

        return backgrounds[11]

    if choice == 12:

        global arcana
        arcana = 1
        history = 1
        lang1 = solo_lang()
        lang2 = solo_lang()
        while lang2 == lang1:
            lang2 = solo_lang()
        
        background_equipment = "A bottle of ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10gp"
        feature = "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."

        return backgrounds[12]

    if choice == 13:

        athletics = 1
        global intimidation
        intimidation = 1
        gaming_set = 1
        vehicles_land = 1
        background_equipment = " An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a set of bone dice or deck of cards, a set of common clothes, and a pouch containing 10 gp"
        feature = "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."

        return backgrounds[13]

    if choice == 14:

        sleight_of_hand = 1
        stealth = 1
        disguise_kit = 1
        thief_tools = 1
        background_equipment = "A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, and a belt pouch containing 10gp"
        feature = "You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."
        return backgrounds[14]



def wizard_cantrip():
     choice = randint(1,33)
     cantrip_list = {
        1:"Acid Splash",
        2:"Blade Ward",
        3:"Booming Blade",
        4:"Chill Touch",
        5:"Control Flames",
        6:"Create Bonfire",
        7:"Dancing Lights",
        8:"Encode Thoughts",
        9:"Fire Bolt",
        10:"Friend",
        11:"Frostbite",
        12:"Green-Flame Blade",
        13:"Gust",
        14:"Infestation",
        15:"Light",
        16:"Lightning Lure",
        17:"Mage Hand",
        18:"Mending",
        19:"Message",
        20:"Mind Sliver",
        21:"Minor Illusion",
        22:"Mold Earth",
        23:"On/Off",
        24:"Poison Spray",
        25:"Prestidigitation",
        26:"Ray of Frost",
        27:"Sapping Sting",
        28:"Shape Water",
        29:"Shocking Grasp",
        30:"Sword Burst",
        31:"Thunderclap",
        32:"Toll the Dead",
        33:"True Strike",}
     return cantrip_list[choice]


def bard_cantrip():
     choice = randint(1,12)
     cantrip_list = {
        1:"Blade Ward",
        2:"Dancing Lights",
        3:"Friends",
        4:"Light",
        5:"Mage Hand",
        6:"Mending",
        7:"Message",
        8:"Minor Illusion",
        9:"Prestidigitation",
        10:"Thunderclap",
        11:"True Strike",
        12:"Vicious Mockery",}
     return cantrip_list[choice]

def bard_level_1():
     choice = randint(1,30)
     cantrip_list = {
        1:"Animal Friendship",
        2:"Bane",
        3:"Color Spray",
        4:"Command",
        5:"Comprehend Languages",
        6:"Cure Wounds",
        7:"Detect Magic",
        8:"Disguise Self",
        9:"Dissonant Whispers",
        10:"Distort Value",
        11:"Earth Tremor",
        12:"Faerie Fire",
        13:"Feather Fall",
        14:"Guiding Hand",
        15:"Healing Word",
        16:"Lightning Lure",
        17:"Heroism",
        18:"Identify",
        19:"Illusory Script",
        20:"Longstrider",
        21:"Puppet",
        22:"Sense Emotion",
        23:"Silent Image",
        24:"Sleep",
        25:"Speak with Animals",
        26:"Sudden Awakening",
        27:"Tasha's Hideous Laughter",
        28:"Thunderwave",
        29:"Unearthly Chorus",
        30:"Unseen Servant",}
     return cantrip_list[choice]

def bard_level_2():
     choice = randint(1,29)
     cantrip_list = {
        1:"Aid",
        2:"Animal Messenger",
        3:"Blindness/Deafness",
        4:"Calm Emotions",
        5:"Cloud of Daggers",
        6:"Crown of Madness",
        7:"Detect Thoughts",
        8:"Enhance Ability",
        9:"Enlarge/Reduce",
        10:"Enthrall",
        11:"Gift of Gab",
        12:"Heat Metal",
        13:"Hold Person",
        14:"Invisibility",
        15:"Knock",
        16:"Lesser Restoration",
        17:"Locate Animals or Plants",
        18:"Locate Object",
        19:"Magic Mouth",
        20:"Mirror Image",
        21:"Phantasmal Force",
        22:"Pyrotechnics",
        23:"See Invisibility",
        24:"Shatter",
        25:"Silence",
        26:"Skywrite",
        27:"Suggestion",
        28:"Warding Word",
        29:"Zone of Truth",}
     return cantrip_list[choice]

def bard_level_3():
     choice = randint(1,23)
     cantrip_list = {
        1:"Bestow Curse",
        2:"Catnap",
        3:"Clairvoyance",
        4:"Dispel Magic",
        5:"Enemies Abound",
        6:"Fast Friends",
        7:"Fear",
        8:"Feign Death",
        9:"Glyph of Warding",
        10:"Hypnotic Pattern",
        11:"Intellect Fortress",
        12:"Leomund's Tiny Hut",
        13:"Major Image",
        14:"Mass Healing Word",
        15:"Motivational Speech",
        16:"Nondetection",
        17:"Plant Growth",
        18:"Sending",
        19:"Slow",
        20:"Speak with Dead",
        21:"Speak with Plants",
        22:"Stinking Cloud",
        23:"Tongues",}
     return cantrip_list[choice]

def bard_level_4():
     choice = randint(1,10)
     cantrip_list = {
        1:"Charm Monster",
        2:"Compulsion",
        3:"Confusion",
        4:"Dimension Door",
        5:"Freedom of Movement",
        6:"Greater Invisibility",
        7:"Hallucinatory Terrain",
        8:"Locate Creature",
        9:"Phantasmal Killer",
        10:"Polymorph",}
     return cantrip_list[choice]

def bard_level_5():
     choice = randint(1,19)
     cantrip_list = {
        1:"Animate Objects",
        2:"Awaken",
        3:"Dominate Person",
        4:"Dream",
        5:"Geas",
        6:"Greater Restoration",
        7:"Hold Monster",
        8:"Legend Lore",
        9:"Mass Cure Wounds",
        10:"Mislead",
        11:"Modify Memory",
        12:"Planar Binding",
        13:"Raise Dead",
        14:"Rary's Telepathic Bond",
        15:"Scrying",
        16:"Seeming",
        17:"Skill Empowerment",
        18:"Synaptic Static",
        19:"Teleportation Circle",}
     return cantrip_list[choice]

def bard_level_6():
     choice = randint(1,8)
     cantrip_list = {
        1:"Eyebite",
        2:"Find the Path",
        3:"Guards and Wards",
        4:"Hero's Feast",
        5:"Mass Suggestion",
        6:"Otto's Irresistible Dance",
        7:"Programmed Illusion",
        8:"True Seeing",}
     return cantrip_list[choice]

def bard_level_7():
     choice = randint(1,12)
     cantrip_list = {
        1:"Dream of the Blue Veil",
        2:"Etherealness",
        3:"Forcecage",
        4:"Mirage Arcane",
        5:"Mordenkainen's Magnificent Mansion",
        6:"Mordenkainen's Sword",
        7:"Prismatic Spray",
        8:"Project Image",
        9:"Regenerate",
        10:"Resurrection",
        11:"Symbol",
        12:"Teleport",}
     return cantrip_list[choice]

def bard_level_8():
     choice = randint(1,6)
     cantrip_list = {
        1:"Antipathy/Sympathy",
        2:"Dominate Monster",
        3:"Feeblemind",
        4:"Glibness",
        5:"Mind Blank",
        6:"Power Word: Stun",}
     return cantrip_list[choice]

def bard_level_9():
     choice = randint(1,7)
     cantrip_list = {
        1:"Foresight",
        2:"Mass Polymorph",
        3:"Power Word: Heal",
        4:"Power Word: Kill",
        5:"Prismatic Wall",
        6:"Psychic Scream",
        7:"True Polymorph",}
     return cantrip_list[choice]


def cleric_cantrip():
     choice = randint(1,10)
     cantrip_list = {
        1:"Decompose",
        2:"Guidance",
        3:"Light",
        4:"Mending",
        5:"Resistance",
        6:"Sacred Flame",
        7:"Spare the Dying",
        8:"Thaumaturgy",
        9:"Toll the Dead",
        10:"Word of Radiance",
        }
     return cantrip_list[choice]

def cleric_level_1():
     choice = randint(1,17)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Magic",
        9:"Detect Poison and Disease",
        10:"Guiding Bolt",
        11:"Guiding Hand",
        12:"Healing Word",
        13:"Inflict Wounds",
        14:"Protection from Evil and Good",
        15:"Purify Food and Drink",
        16:"Sanctuary",
        17:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_arcana_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Poison and Disease",
        9:"Guiding Bolt",
        10:"Guiding Hand",
        11:"Healing Word",
        12:"Inflict Wounds",
        13:"Protection from Evil and Good",
        14:"Purify Food and Drink",
        15:"Sanctuary",
        16:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_grave_level_1():
     choice = randint(2,17)
     cantrip_list = {
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Magic",
        9:"Detect Poison and Disease",
        10:"Guiding Bolt",
        11:"Guiding Hand",
        12:"Healing Word",
        13:"Inflict Wounds",
        14:"Protection from Evil and Good",
        15:"Purify Food and Drink",
        16:"Sanctuary",
        17:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_ambition_level_1():
     choice = randint(2,17)
     cantrip_list = {
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Magic",
        9:"Detect Poison and Disease",
        10:"Guiding Bolt",
        11:"Guiding Hand",
        12:"Healing Word",
        13:"Inflict Wounds",
        14:"Protection from Evil and Good",
        15:"Purify Food and Drink",
        16:"Sanctuary",
        17:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_knowledge_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Create or Destroy Water",
        5:"Cure Wounds",
        6:"Detect Evil and Good",
        7:"Detect Magic",
        8:"Detect Poison and Disease",
        9:"Guiding Bolt",
        10:"Guiding Hand",
        11:"Healing Word",
        12:"Inflict Wounds",
        13:"Protection from Evil and Good",
        14:"Purify Food and Drink",
        15:"Sanctuary",
        16:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_order_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Create or Destroy Water",
        5:"Cure Wounds",
        6:"Detect Evil and Good",
        7:"Detect Magic",
        8:"Detect Poison and Disease",
        9:"Guiding Bolt",
        10:"Guiding Hand",
        11:"Healing Word",
        12:"Inflict Wounds",
        13:"Protection from Evil and Good",
        14:"Purify Food and Drink",
        15:"Sanctuary",
        16:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_mind_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Create or Destroy Water",
        5:"Cure Wounds",
        6:"Detect Evil and Good",
        7:"Detect Magic",
        8:"Detect Poison and Disease",
        9:"Guiding Bolt",
        10:"Guiding Hand",
        11:"Healing Word",
        12:"Inflict Wounds",
        13:"Protection from Evil and Good",
        14:"Purify Food and Drink",
        15:"Sanctuary",
        16:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_life_level_1():
     choice = randint(1,15)
     cantrip_list = {
        1:"Bane",
        2:"Ceremony",
        3:"Command",
        4:"Create or Destroy Water",
        5:"Detect Evil and Good",
        6:"Detect Magic",
        7:"Detect Poison and Disease",
        8:"Guiding Bolt",
        9:"Guiding Hand",
        10:"Healing Word",
        11:"Inflict Wounds",
        12:"Protection from Evil and Good",
        13:"Purify Food and Drink",
        14:"Sanctuary",
        15:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_peace_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Magic",
        9:"Detect Poison and Disease",
        10:"Guiding Bolt",
        11:"Guiding Hand",
        12:"Healing Word",
        13:"Inflict Wounds",
        14:"Protection from Evil and Good",
        15:"Purify Food and Drink",
        16:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_solidarity_level_1():
     choice = randint(1,15)
     cantrip_list = {
        1:"Bane",
        2:"Ceremony",
        3:"Command",
        4:"Create or Destroy Water",
        5:"Cure Wounds",
        6:"Detect Evil and Good",
        7:"Detect Magic",
        8:"Detect Poison and Disease",
        9:"Guiding Hand",
        10:"Healing Word",
        11:"Inflict Wounds",
        12:"Protection from Evil and Good",
        13:"Purify Food and Drink",
        14:"Sanctuary",
        15:"Shield of Faith",}
     return cantrip_list[choice]

def cleric_war_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Magic",
        9:"Detect Poison and Disease",
        10:"Guiding Bolt",
        11:"Guiding Hand",
        12:"Healing Word",
        13:"Inflict Wounds",
        14:"Protection from Evil and Good",
        15:"Purify Food and Drink",
        16:"Sanctuary",}
     return cantrip_list[choice]

def cleric_strength_level_1():
     choice = randint(1,16)
     cantrip_list = {
        1:"Bane",
        2:"Bless",
        3:"Ceremony",
        4:"Command",
        5:"Create or Destroy Water",
        6:"Cure Wounds",
        7:"Detect Evil and Good",
        8:"Detect Magic",
        9:"Detect Poison and Disease",
        10:"Guiding Bolt",
        11:"Guiding Hand",
        12:"Healing Word",
        13:"Inflict Wounds",
        14:"Protection from Evil and Good",
        15:"Purify Food and Drink",
        16:"Sanctuary",}
     return cantrip_list[choice]


def cleric_level_2():
     choice = randint(1,17)
     cantrip_list = {
        1:"Aid",
        2:"Augury",
        3:"Blindess/Deafness",
        4:"Calm Emotions",
        5:"Continual Flame",
        6:"Enhance Ability",
        7:"Find Traps",
        8:"Gentle Repose",
        9:"Hold Person",
        10:"Lesser Restoration",
        11:"Locate Object",
        12:"Prayer of Healing",
        13:"Protection from Poison",
        14:"Silence",
        15:"Spiritual Weapon",
        16:"Warding Bond",
        17:"Zone of Truth",}
     return cantrip_list[choice]

def cleric_level_3():
     choice = randint(1,26)
     cantrip_list = {
        1:"Animate Dead",
        2:"Aura of Vitality",
        3:"Beacon of Hope",
        4:"Bestow Curse",
        5:"Clairvoyance",
        6:"Create Food and Water",
        7:"Daylight",
        8:"Dispel Magic",
        9:"Fast Friends",
        10:"Feign Death",
        11:"Glyph of Warding",
        12:"Incite Greed",
        13:"Life Transference",
        14:"Magic Circle",
        15:"Mass Healing Word",
        16:"Meld Into Stone",
        17:"Motivational Speech",
        18:"Protection from Energy",
        19:"Remove Curse",
        20:"Revivify",
        21:"Sending",
        22:"Speak With Dead",
        23:"Spirit Guardians",
        24:"Spirit Shroud",
        25:"Tounges",
        26:"Water Walk",}
     return cantrip_list[choice]

def cleric_level_4():
     choice = randint(1,10)
     cantrip_list = {
        1:"Aura Of Life",
        2:"Aura Of Purity",
        3:"Banishment",
        4:"Control Water",
        5:"Death Ward",
        6:"Divination",
        7:"Freedom of Movement",
        8:"Guardian of Faith",
        9:"Locate Creature",
        10:"Stone Shape",
        }
     return cantrip_list[choice]

def cleric_level_5():
     choice = randint(1,16)
     cantrip_list = {
        1:"Commune",
        2:"Contagion",
        3:"Dawn",
        4:"Dispel Evil and Good",
        5:"Flame Strike",
        6:"Geas",
        7:"Greater Restoration",
        8:"Hallow",
        9:"Holy Weapon",
        10:"Insect Plague",
        11:"Legend Lore",
        12:"Mass Cure Wounds",
        13:"Planar Binding",
        14:"Raise Dead",
        15:"Scrying",
        16:"Summon Celestial",}
     return cantrip_list[choice]

def cleric_level_6():
     choice = randint(1,12)
     cantrip_list = {
        1:"Blade Barrier",
        2:"Create Undead",
        3:"Find the Path",
        4:"Forbiddance",
        5:"Harm",
        6:"Heal",
        7:"Heroes' Feast",
        8:"Otherwordly Form",
        9:"Planar Ally",
        10:"Sunbeam",
        11:"True Seeing",
        12:"Word of Recall",
        }
     return cantrip_list[choice]

def cleric_level_7():
     choice = randint(1,9)
     cantrip_list = {
        1:"Conjure Celestial",
        2:"Divine Word",
        3:"Etherealness",
        4:"Fire Storm",
        5:"Plane Shift",
        6:"Regenerate",
        7:"Ressurection",
        8:"Symbol",
        9:"Temple of the Gods",
        }
     return cantrip_list[choice]

def cleric_level_8():
     choice = randint(1,5)
     cantrip_list = {
        1:"Anti-Magic Field",
        2:"Control Weather",
        3:"Earthquake",
        4:"Holy Aura",
        5:"Sunburst",
        }
     return cantrip_list[choice]

def cleric_level_9():
     choice = randint(1,5)
     cantrip_list = {
        1:"Astral Projection",
        2:"Gate",
        3:"Mass Heal",
        4:"Power Word: Heal",
        5:"True Resurrection",
        }
     return cantrip_list[choice]

def druid_cantrip():
     choice = randint(1,18)
     cantrip_list = {
        1:"Control Flames",
        2:"Create Bonfire",
        3:"Druidcraft",
        4:"Frostbite",
        5:"Control Flames",
        6:"Guidance",
        7:"Gust",
        8:"Infestation",
        9:"Magic Stone",
        10:"Mending",
        11:"Mold Earth",
        12:"Poison Spray",
        13:"Primal Savagery",
        14:"Produce Flame",
        15:"Shape Water",
        16:"Thunderclap",
        15:"Resistance",
        16:"Shillelagh",
        17:"Thorn Whip",
        18:"Thunderclap",
      }
     return cantrip_list[choice]

def druid_level_1():
    choice = randint(1,24)
    cantrip_list = {
      1:"Absorb Elements",
      2:"Animal Friendship",
      3:"Beast Bond",
      4:"Charm Person",
      5:"Create or Destroy Water",
      6:"Cure Wounds",
      7:"Detect Magic",
      8:"Detect Poison and Disease",
      9:"Earth Tremor",
     10:"Entangle",
     11:"Faerie Fire",
     12:"Fog Cloud",
     13:"Goodberry",
     14:"Guiding Hand (UA)",
     15:"Healing Word",
     16:"Ice Knife",
     17:"Jump",
     18:"Longstrider",
     19:"Protection from Evil and Good",
     20:" Food and Drink",
     21:"Snare",
     22:"Speak with Animals",
     23:"Thunderwave",
     24:"Wild Cunning (UA)",}
    return cantrip_list[choice]

def druid_level_2():
    choice = randint(1,27)
    cantrip_list = {
        1:"Animal Messenger",
        2:"Augury",
        3:"Barkskin",
        4:"Beast Sense",
        5:"Continual Flame",
        6:"Darkvision",
        7:"Dust Devil",
        8:"Earthbind",
        9:"Enhance Ability",
        10:"Enlarge/Reduce",
        11:"Find Traps",
        12:"Flame Blade",
        13:"Flaming Sphere",
        14:"Gust of Wind",
        15:"Healing Spirit",
        16:"Heat Metal",
        17:"Hold Person",
        18:"Lesser Restoration",
        19:"Locate Animals or Plants",
        20:"Locate Object",
        21:"Moonbeam",
        22:"Pass Without Trace",
        23:"Protection from Poison",
        24:"Skywrite",
        25:"Spike Growth",
        26:"Summon Beast",
        27:"Warding Wind",}
    return cantrip_list[choice]

def druid_level_3():
    choice = randint(1,21)
    cantrip_list = {
        1:"Aura of Vitality",
        2:"Call Lightning",
        3:"Conjure Animals",
        4:"Daylight",
        5:"Dispel Magic",
        6:"Elemental Weapon",
        7:"Erupting Earth",
        8:"Feign Death",
        9:"Flame Arrows",
        10:"Meld into Stone",
        11:"Plant Growth",
        12:"Protection from Energy",
        13:"Revivify",
        14:"Sleet Storm",
        15:"Speak with Plants",
        16:"Summon Fey",
        17:"Tidal Wave",
        18:"Wall of Water",
        19:"Water Breathing",
        20:"Water Walk",
        21:"Wind Wall",}
    return cantrip_list[choice]

def druid_level_4():
    choice = randint(1,23)
    cantrip_list = {
        1:"Blight",
        2:"Charm Monster",
        3:"Confusion",
        4:"Conjure Minor Elementals",
        5:"Conjure Woodland Beings",
        6:"Control Water",
        7:"Divination",
        8:"Dominate Beast",
        9:"Elemental Bane",
        10:"Fire Shield",
        11:"Freedom of Movement",
        12:"Giant Insect",
        13:"Grasping Vine",
        14:"Guardian of Nature",
        15:"Hallucinatory Terrain",
        16:"Ice Storm",
        17:"Locate Creature",
        18:"Polymorph",
        19:"Stone Shape",
        20:"Stoneskin",
        21:"Summon Elemental",
        22:"Wall of Fire",
        23:"Watery Sphere",}
    return cantrip_list[choice]

def druid_level_5():
    choice = randint(1,20)
    cantrip_list = {
        1:"Antilife Shell",
        2:"Awaken",
        3:"Commune with Nature",
        4:"Cone of Cold",
        5:"Conjure Elemental",
        6:"Contagion",
        7:"Control Winds",
        8:"Geas",
        9:"Greater Restoration",
        10:"Insect Plague",
        11:"Maelstrom",
        12:"Mass Cure Wounds",
        13:"Planar Binding",
        14:"Reincarnate",
        15:"Scrying",
        16:"Summon Draconic Spirit",
        17:"Transmute Rock",
        18:"Tree Stride",
        19:"Wall of Stone",
        20:"Wrath Of Nature",}
    return cantrip_list[choice]

def druid_level_6():
    choice = randint(1,17)
    cantrip_list = {
        1:"Bones of the Earth",
        2:"Conjure Fey",
        3:"Druid Grove",
        4:"Find the Path",
        5:"Flesh to Stone",
        6:"Heal",
        7:"Heroes' Feast",
        8:"Investiture of Flame",
        9:"Investiture of Ice",
        10:"Investiture of Stone",
        11:"Investiture of Wind",
        12:"Move Earth",
        13:"Primordial Ward",
        14:"Sunbeam",
        15:"Transport via Plants",
        16:"Wall of Thorns",
        17:"Wind Walk",}
    return cantrip_list[choice]

def druid_level_7():
    choice = randint(1,8)
    cantrip_list = {
        1:"Draconic Transformation",
        2:"Fire Storm",
        3:"Mirage Arcane",
        4:"Plane Shift",
        5:"Regenerate",
        6:"Reverse Gravity",
        7:"Symbol",
        8:"Whirlwind",}
    return cantrip_list[choice]

def druid_level_8():
    choice = randint(1,8)
    cantrip_list = {
        1:"Animal Shapes",
        2:"Antipathy/Sympathy",
        3:"Control Weather",
        4:"Earthquake",
        5:"Feeblemind",
        6:"Incendiary Cloud",
        7:"Sunburst",
        8:"Tsunami",}
    return cantrip_list[choice]

def druid_level_9():
    choice = randint(1,4)
    cantrip_list = {
        1:"Foresight",
        2:"Shapechange",
        3:"Storm of Vengeance",
        4:"True Resurrection",}
    return cantrip_list[choice]

def paladin_level_1():
    choice = randint(1,16)
    cantrip_list = {
        1:"Bless",
        2:"Ceremony",
        3:"Command",
        4:"Compelled Duel",
        5:"Cure Wounds",
        6:"Detect Evil and Good",
        7:"Detect Magic",
        8:"Detect Poison and Disease",
        9:"Divine Favor",
        10:"Heroism",
        11:"Protection from Evil and Good",
        12:"Purify Food and Drink",
        13:"Searing Smite",
        14:"Shield of Faith",
        15:"Thunderous Smite",
        16:"Wrathful Smite",}
    return cantrip_list[choice]

def paladin_level_2():
    choice = randint(1,12)
    cantrip_list = {
        1:"Aid",
        2:"Branding Smite",
        3:"Find Steed",
        4:"Finv Vehicle (UA)",
        5:"Gentle Repose",
        6:"Lesser Restoration",
        7:"Locate Object",
        8:"Magic Weapon",
        9:"Prayer of Healing",
        10:"Protection from Poison",
        11:"Warding Bond",
        12:"Zone of Truth",}
    return cantrip_list[choice]

def paladin_level_3():
    choice = randint(1,11)
    cantrip_list = {
        1:"Aura of Vitality",
        2:"Blinding Smite",
        3:"Create Food and Water",
        4:"Crusader's Mantle",
        5:"Daylight",
        6:"Dispel Magic",
        7:"Elemental Weapon",
        8:"Magic Circle",
        9:"Remove Curse",
        10:"Revivify",
        11:"Spirit Shroud",}
    return cantrip_list[choice]

def paladin_level_4():
    choice = randint(1,7)
    cantrip_list = {
        1:"Aura of Life",
        2:"Aura of Purity",
        3:"Banishment",
        4:"Death Ward",
        5:"Find Greater Steed",
        6:"Locate Creature",
        7:"Staggering Smite",}
    return cantrip_list[choice]

def paladin_level_5():
    choice = randint(1,8)
    cantrip_list = {
        1:"Banishing Smite",
        2:"Circle of Power",
        3:"Destructive Wave",
        4:"Dispel Evil and Good",
        5:"Geas",
        6:"Holy Weapon",
        7:"Raise Dead",
        8:"Summon Celestial",}
    return cantrip_list[choice]

def ranger_level_1():
    choice = randint(1,21)
    cantrip_list = {
        1:"Absorb Elements",
        2:"Alarm",
        3:"Animal Friendship",
        4:"Beast Bond",
        5:"Cure Wounds",
        6:"Detect Magic",
        7:"Detect Poison and Disease",
        8:"Ensnaring Strike",
        9:"Entangle",
        10:"Fog Cloud",
        11:"Goodberry",
        12:"Hail of Thorns",
        13:"Hunter's Mark",
        14:"Jump",
        15:"Longstrider",
        16:"Searing Smite",
        17:"Snare",
        18:"Speak with Animals",
        19:"Sudden Awakening (UA)",
        20:"Wild Cunning (UA)",
        21:"Zephyr Strike",}
    return cantrip_list[choice]

def ranger_level_2():
    choice = randint(1,19)
    cantrip_list = {
        1:"Aid",
        2:"Animal Messenger",
        3:"Barkskin",
        4:"Beast Sense",
        5:"Cordon of Arrows",
        6:"Darkvision",
        7:"Enhance Ability",
        8:"Find Traps",
        9:"Gust of Wind",
        10:"Healing Spirit",
        11:"Lesser Restoration",
        12:"Locate Animals or Plants",
        13:"Locate Object",
        14:"Magic Weapon",
        15:"Pass Without Trace",
        16:"Protection from Poison",
        17:"Silence",
        18:"Spike Growth",
        19:"Summon Beast",}
    return cantrip_list[choice]

def ranger_level_3():
    choice = randint(1,17)
    cantrip_list = {
        1:"Conjure Animals",
        2:"Conjure Barrage",
        3:"Daylight",
        4:"Elemental Weapon",
        5:"Flame Arrows",
        6:"Flame Stride (UA)",
        7:"Lightning Arrow",
        8:"Meld into Stone",
        9:"Nondetection",
        10:"Plant Growth",
        11:"Protection from Energy",
        12:"Revivify",
        13:"Speak with Plants",
        14:"Summon Fey",
        15:"Water Breathing",
        16:"Water Walk",
        17:"Wind Wall",}
    return cantrip_list[choice]

def ranger_level_4():
    choice = randint(1,8)
    cantrip_list = {
        1:"Conjure Woodland Beings",
        2:"Dominate Beast",
        3:"Freedom of Movement",
        4:"Grasping Vine",
        5:"Guardian of Nature",
        6:"Locate Creature",
        7:"Stoneskin",
        8:"Summon Elemental",}
    return cantrip_list[choice]

def ranger_level_5():
    choice = randint(1,7)
    cantrip_list = {
        1:"Commune with Nature",
        2:"Conjure Volley",
        3:"Greater Restoration",
        4:"Steel Wind Strike",
        5:"Swift Quiver",
        6:"Tree Stride",
        7:"Wrath Of Nature",}
    return cantrip_list[choice]



def ability_score_improvement():
    global Strength
    global Dexterity
    global Constitution
    global Intelligence
    global Charisma
    global Wisdom
    abs= randint(1,3)
    if abs == 1:
         score_increase = randint(1,6)
         if score_increase == 1:
                    Strength +=2
         if score_increase == 2:
                    Dexterity += 2            
         if score_increase == 3:
                    Constitution += 2
         if score_increase == 4:
                    Charisma +=2
         if score_increase == 5:
                    Intelligence +=2
         if score_increase == 6:
                    Wisdom +=2

    if abs == 2:
         score_increase = randint(1,6)
         if score_increase == 1:
                    Strength +=1
         if score_increase == 2:
                    Dexterity += 1            
         if score_increase == 3:
                    Constitution += 1
         if score_increase == 4:
                    Charisma +=1
         if score_increase == 5:
                    Intelligence +=1
         if score_increase == 6:
                    Wisdom +=1

         score_increase2 = randint(1,6)
         while score_increase2 == score_increase:
             score_increase2 = randint(1,6)
         if score_increase2 == 1:
                    Strength +=1
         if score_increase2 == 2:
                    Dexterity += 1            
         if score_increase2 == 3:
                    Constitution += 1
         if score_increase2 == 4:
                    Charisma +=1
         if score_increase2 == 5:
                    Intelligence +=1
         if score_increase2 == 6:
                    Wisdom +=1

    if abs == 3:
       a = feat()
       return a
# Must be set equal to a feat to return the feat!!!!


def race_features(PC_race):

    if PC_race == "Dragonborn":

        ancestry = randint(1,10)
        
        global race_feature1

        if ancestry == 1:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest.\n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is black, and your breath attack is acid in a 5' by 30' line (Dex Save)")

        if ancestry == 2:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             ":The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest.\n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is blue, and your breath attack is lightning in a 5' by 30' line (Dex Save)")

        if ancestry == 3:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             " The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. \n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is brass, and your breath attack is fire in a 5' by 30' line (Dex Save)")

        if ancestry == 4:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. \n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is bronze, and your breath attack is lightning in a 5' by 30' line (Dex Save)")

        if ancestry == 5:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest.\n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is copper, and your breath attack is acid in a 5' by 30' line (Dex Save)")

        if ancestry == 6:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. \n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is gold, and your breath attack is fire in a 15' cone (Dex Save)")

        if ancestry == 7:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. \n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is green and your breath attack is posion in a 15' cone (Dex Save)")
        
        if ancestry == 8:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. \n"
                             "Instead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is red, and your breath attack is fire in a 15' cone (Dex Save)")

        if ancestry == 9:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\n"
                             "The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. HBInstead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is silver and your breath attack is cold in a 15' cone (Dex Save)")

        if ancestry == 10:
            race_feature1 = ("Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. HBInstead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest.\nYour dragon is white and your breath attack is cold in a 15' cone (Dex Save)")

        global common
        global draconic
        common == 1
        draconic == 1

        global race_feature2
        global race_feature3
        global Strength
        global Charisma
        global Constitution
        global Intelligence
        global speed
        global PC_subrace

        dragon_type = randint(1,3)

        speed = 30

        if dragon_type == 1:
            Strength += 2
            Charisma += 1
            race_feature2 = "You have resistance to the damage type associated with your ancestry."
            PC_subrace = "Dragonborn"

        if dragon_type == 2:
            Intelligence += 2
            Charisma += 1
            race_feature2 = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            race_feature3 = "When you make a Intimidation or Persuasion check, you can do so with advantage once per long rest."
            PC_subrace = "Draconblood"

        if dragon_type == 3:
            Strength +=2
            Constitution += 1
            race_feature2 = "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            race_feature3 = "When you take damage from a creature in range of a weapon you are wielding, you can use your reaction to make an attack against that creature. You can do this once per short or long rest."
            PC_subrace = "Ravenite"
        return 1
    
    if PC_race == "Dwarf":   

       global race_feature4

       speed = 25
       race_feature1 = "Heavy Armor does not slow you"
       race_feature2 = "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
       race_feature3 = "You have advantage on saving throws against poison, and you have resistance against poison damage."
       race_feature4 = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
       
       global battleaxe
       battleaxe = 1
       global handaxe
       handaxe = 1
       global light_hammer
       light_hammer = 1
       global war_hammer
       war_hammer = 1
       global artisan_tools
       artisan_tools = 1
       common = 1
       global dwarvish
       dwarvish = 1
       Constitution +=2


       dwarf_type = randint(1,5)
        
       if dwarf_type == 1:
           global Wisdom
           global race_feature5
           Wisdom += 1
           race_feature5 = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
           PC_subrace = "Hill Dwarf"

       if dwarf_type == 2:
           Strength += 2
           global light_armor
           light_armor = 1
           global medium_armor
           medium_armor = 1
           PC_subrace = "Mountain Dwarf"

       if dwarf_type == 3:
            Strength += 1
            global race_feature6
            global race_feature7
            race_feature2 = "You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            race_feature5 = "You have advantage on saving throws against illusions and against being charmed or paralyzed."
            race_feature6 = "When you reach 3rd level, you can cast the Enlarge/Reduce spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the Invisibility spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells."
            race_feature7 = "You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."
            PC_subrace = "Duergar (Gray Dwarf)"

       if dwarf_type == 4:
           Intelligence += 1
           race_feature5 = "Whenever you make an Intelligence (Investigation) check or an Ability Check involving Thieve's Tools, you can roll a d4 and add the number rolled to the total ability check."
           race_feature6 = "You can cast the Alarm and Mage Armor spells with this trait. Starting at 3rd level, you can also cast the Arcane Lock spell with it. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Intelligence is your Spellcasting Ability for these spells, and you don't require material components when you cast them with this trait."
           race_feature7 = "If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Warding Spells table are added to the spell list of your Spellcasting class.\nLevel 1. Alarm,Armor of Agathys\nLevel 2.Arcane Lock, Knock\nLevel 3.Glyph of Warding, Magic Circle\nLevel 4.Leomund's Secret Chest, Mordenkainen's Faithful Hound\nLevel 5.Antilife Shell"
           PC_subrace = "Mark of Warding Dwarf"

       if dwarf_type == 5:
           Wisdom += 1 
           race_feature5 = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
           race_feature6 = "You gain proficiency with two kinds of artisan’s tools of your choice. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. In addition, whenever you make an Intelligence (History) check related to the origin of any architectural construction, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
           PC_subrace = "Dwarf (Kaladesh)"

    if PC_race == "Elf":
        global Dexterity
        Dexterity +=2
        speed = 30
        race_feature1 = "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
        race_feature2 = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
        race_feature3 = "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is trance. While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."
        global preception
        preception = 1
        global elvish
        elvish = 1
        common = 1

        elf_type = randint(1,13)

        if elf_type == 1:
            Charisma +=1
            race_feature1 = "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            race_feature4 = "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight."
            race_feature5 = "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast the Faerie Fire spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Darkness spell onceand regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
            global rapier
            global shortsword
            global hand_crossbow
            rapier = 1
            shortsword = 1
            hand_crowwbow = 1
            PC_subrace = "Dark Elf"

        if elf_type == 2:
            race_feature4 = "Eladrin are elves native to the Feywild, a realm of beauty, unpredictable emotion, and boundless magic. An eladrin is associated with one of the four seasons and has coloration reminiscent of that season, which can also affect the eladrin's mood\nAutumn is the season of peace and goodwill, when summers harvest is shared with all.\nWinter is the season of contemplation and dolor, when the vibrant energy of the world slumbers.\nSpring is the season of cheerfulness and celebration, marked by merriment as winters sorrow passes.\nSummer is the season of boldness and aggression, a time of unfettered energy.\nWhen finishing a long rest, any eladrin can change their season. An eladrin might choose the season that is present in the world or perhaps the season that most closely matches the eladrin's current emotional state. For example, an eladrin might shift to autumn if filled with contentment, another eladrin could change to winter if plunged into sorrow, still another might be bursting with joy and become an eladrin of spring, and fury might cause an eladrin to change to summer."
            Charisma +=1
            race_feature5 = "As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest. When you reach 3rd level, your Fey Step gains an additional effect based on your season; if the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Charisma modifier. The effects are as follows:\nAutumn. Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it.\nWinter. When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.\nSpring. When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.\nSummer. Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage)."
            PC_subrace = "Eladrin"

        if elf_type == 3:

            Intelligence +=1
            slots = 1
            high_elf_cantrip = wizard_cantrip()
            race_feature4 = "You know the cantrip", high_elf_cantrip, ". Intelligence is your spellcasting ability for it"
            lang2 = solo_lang()
            PC_subrace = "High Elf"

        if elf_type == 4:
           Constitution += 1
           global spear
           global trident
           global light_crossbow
           global net
           spear = 1
           trident = 1
           light_crossbow = 1
           net = 1
           race_feature4 = "You have a swimming speed of 30 feet, and you can breathe air and water."
           race_feature5 = "Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed."
           global aquan
           aquan = 1
           PC_subrace = "Sea Elf"

        if elf_type == 5:
            Constitution += 1
            race_feature4 = "You have resistance to necrotic damage."
            race_feature5 = "As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest. Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent."
            PC_subrace = "Shadar-Kai"

        if elf_type == 6:
            Wisdom += 1
            global longsword
            global longbow
            global shortbow
            longsword = 1
            longbow = 1
            shortbow = 1
            shortsword = 1
            speed = 35
            race_feature4 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
            PC_subrace = "Wood Elf"

        if elf_type == 7:
            Wisdom += 1
            global insight
            insight = 1
            global investigation
            investigation = 1
            race_feature4 = "You know the Light cantrip. When you reach 3rd level, you can cast Sleep once, and it recharges after a long rest. When you reach 5th level, you can cast Invisibility (Self Only) once, and it recharges after a long rest. You do not need the material components required of the spells. Wisdom is your spellcasting ability for these spells."
            PC_subrace = "Pallid Elf"
        
        if elf_type == 8:
            Charisma += 1
            race_feature4 = "Whenever you roll a Dexterity (Stealth) check or a Charisma (Performance) check, roll a d4 and add the number rolled to the total ability check."
            race_feature5 = " You know the Minor Illusion cantrip. Starting at 3rd level, you can also cast the Invisibility spell with this trait. Once you cast either spell with this trait, you can't cast that spell again until you finish a long rest. Charisma is your Spellcasting Ability for these spells."
            race_feature6 = " If you have the Spellcasting or Pact Magic class features, the spells on the Mark of Shadow Spells table are added to the spell list of your spellcasting class:\n1.Disguise Self, Silent Image\n2.Darkness, Pass Without Trace\n3.Clairvoyance, Major Image\n4.Greater Invisibility, Hallucinatory Terrain\n5.Mislead"
            PC_subrace = "Mark of Shadow Elf"

        if elf_type == 9:
            race_feature4 = "You have a flying speed of 30 feet. To use this speed, you can't be wearing medium or heavy armor."
            global auran
            auran = 1
            PC_subrace = "Avariel Elf"

        if elf_type == 10:
            Strength += 1
            spear = 1
            longbow = 1
            shortbow = 1
            net = 1
            common = 0
            global sylvan
            sylvan = 1
            high_elf_cantrip = druid_cantrip()
            race_feature4 = "You know the cantrip", high_elf_cantrip, ". Wisdom is your spellcasting ability for it."
            PC_subrace = "Grugach Elf"

        if elf_type == 11:
            Wisdom += 1
            longsword = 1
            longbow = 1
            shortbow = 1
            shortsword = 1
            speed = 35
            race_feature4 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
            PC_subrace = "Bishtahar and Tirahar Elf"

        if elf_type == 12:
            Wisdom += 1
            longsword = 1
            longbow = 1
            shortbow = 1
            shortsword = 1
            high_elf_cantrip = druid_cantrip()
            race_feature4 = "You know the cantrip",high_elf_cantrip, ". Wisdom is your spellcasting ability for it."
            solo_lang()
            PC_subrace = "Vahadar Elf"


        if elf_type == 13:
            Dexterity-=2
            Wisdom +=2
            subrace = randint(1,3)

            if subrace == 1:
                Charisma +=1
                race_feature4 = "You gain proficiency in any combination of two skills or tools of your choice."
                PC_subrace = "Tajuru Nation Elf"

            if subrace == 2:
                Dexterity+=1
                longsword = 1
                longbow = 1
                shortbow = 1
                shortsword = 1
                speed = 35
                race_feature4 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
                PC_subrace = "Juraga Nation Elf"

            if subrace == 3:
                Strength += 1
                race_feature1 = "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
                race_feature4 = "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight."
                race_feature5 = "You know the chill touch cantrip. When you reach 3rd level, you can cast the hex spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Wisdom is your spellcasting ability for these spells."
                longsword = 1
                longbow = 1
                shortbow = 1
                shortsword = 1
                PC_subrace = "Mul Daya Nation Elf"

    if PC_race == "Gnome":
        Intelligence += 2
        speed = 25
        race_feature1 = "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
        race_feature2 = "You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."
        common = 1
        global gnomish
        gnomish = 1

        gnome_type = randint(1,4)

        if gnome_type == 1:
            Dexterity += 1
            race_feature3 = "You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it."
            race_feature4 = "Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."
            PC_subrace = "Forest Gnome"

        if gnome_type == 2:
            Constitution +=1
            artisan_tools = 1
            race_feature3 = " Whenever you make an Intelligence (History) check related to magical, alchemical, or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply."
            race_feature4 = "You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:\nClockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\nFire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.\nMusic Box. When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed\nAt your DM's discretion, you may make other objects with effects similar in power to these. The Prestidigitation cantrip is a good baseline for such effects."
            PC_subrace = "Rock Gnome"

        if gnome_type == 3:
            Dexterity += 1
            race_feature1 = "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            race_feature3 = "You have advantage on Dexterity (stealth) checks to hide in rocky terrain."
            PC_subrace = "Svirfneblin (Deep Gnome)"

        if gnome_type == 4:
            Charisma += 1
            race_feature3 = "Whenever you make an Intelligence (History) or an Ability Check involving Calligrapher's Supplies, you can roll a d4 and add the number rolled to the total ability check."
            race_feature4 = "You know the Message cantrip. You can also cast the Comprehend Languages spell with this trait. Starting at 3rd level, you can also cast the Magic Mouth spell with it. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Intelligence is your Spellcasting Ability for these spells."
            race_feature5 = "If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Warding Spells table are added to the spell list of your Spellcasting class.\nLevel 1. Comprehend Languages, Illusory Script\nLevel 2. Animal Messenger, Silence\nLevel 3.Sending, Tongues\nLevel 4. Arcane Eye, Divination\nLevel 5. Dream"
            PC_subrace = "Mark of Scribing Gnome"

    if PC_race == "Half-Elf":
        Charisma +=2
        speed = 30
        race_feature1 = "Thanks to your elven heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
        race_feature2 = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
        common = 1
        elvish = 1

        lang3 = solo_lang()
        while lang3 == "common" or lang3 == "elvish":
            lang3 = solo_lang()

        
        half_elf_type = randint(1,3)
        half_elf_type = 1
        if half_elf_type == 1:
            PC_subrace = "Half-Elf"
            increases = 2
            a = 0
            while increases != 0:
                score_increase = randint(1,5)
                
                while score_increase == a:
                    score_increase = randint(1,5)

                if score_increase == 1:
                    Strength +=1
                if score_increase == 2:
                    Dexterity += 1            
                if score_increase == 3:
                    Constitution += 1
                if score_increase == 4:
                    Wisdom +=1
                if score_increase == 5:
                    Intelligence +=1
                a = score_increase;
                increases -=1

            versatility = randint(1,7)
            
            if versatility == 1:
                a = solo_skill()
                b = solo_skill()
                if a == b:
                    b = solo_skill()
            if versatility == 2:
                longsword = 1
                longbow = 1
                shortbow = 1
                shortsword = 1

            if versatility == 3:
                high_elf_cantrip = wizard_cantrip()
                race_feature3 = "You know the cantrip", high_elf_cantrip, ". Intelligence is your spellcasting ability for it"

            if versatility == 4:
                speed = 35

            if versatility == 5:
                race_feature3 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."

            if versatility == 6:
                 race_feature3 = "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells."

            if versatility == 7:
                race_feature3 = "You have a swimming speed of 30 feet."

        if half_elf_type == 2:
            Wisdom += 2
            score_increase = randint(1,5)
            if score_increase == 1:
                    Strength +=1
            if score_increase == 2:
                    Dexterity += 1            
            if score_increase == 3:
                    Constitution += 1
            if score_increase == 4:
                    Charisma +=1
            if score_increase == 5:
                    Intelligence +=1

            race_feature3 = "Whenever you make a Intelligence (Investigation) or a Wisdom (Insight) check, you can roll a d4 and add the number rolled to the total ability check."
            race_feature4 = "You can cast the Detect Magic and the Detect Poison and Disease spells with this trait. Starting at 3rd level, you can also cast the See Invisibility spell with it. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Intelligence is your Spellcasting Ability for these spells, and you don't require material components for them."
            race_feature5 = " If you have the Spellcasting or Pact Magic class features, the spells on the Mark of Detection Spells table are added to the spell list of your spellcasting class:\n1. Detect Magic, Detect Poison and Disease\n2. Detect Thoughts, Find Traps\n3. Clairvoyance, Nondetection\n4. Arcane Eye,Divination\n5. Legend Lore"
            PC_subrace = "Mark of Detection Half Elf"


        if half_elf_type == 3:
             Charisma += 2
             Dexterity += 1  
             race_feature3 = " Whenever you make a Dexterity (Acrobatics) check or any Ability Check involving Navigator's Tools, you can roll a d4 and add the number rolled to the total ability check."
             race_feature4 = "You have resistance to Lightning damage."
             race_feature5 = "You know the Gust cantrip. Starting at 3rd level, you can also cast the Gust of Wind spell with it. Once you cast this spell with this trait, you can't cast that spell again until you finish a Long Rest. Charisma is your Spellcasting Ability for this spell."
             race_feature6 = " If you have the Spellcasting or Pact Magic class features, the spells on the Mark of Storm Spells table are added to the spell list of your spellcasting class:\n1. Feather Fall, Fog Cloud\n2. Gust of Wind, Levitate\n3. Sleet Storm, Wind Wall\n4. Conjure Minor Elementals, Control Water\n5. Conjure Elemental"
             PC_subrace = "Mark of Storm Half-Elf"
             
    if PC_race == "Halfling":
       Dexterity += 2
       speed = 25
       race_feature1 = "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1."
       race_feature2 = "You have advantage on saving throws against being frightened."
       race_feature3 = " You can move through the space of any creature that is of a size larger than yours. Your size is small"
       global halfing
       halfling = 1
       common = 1

       halfing_type = randint(1,6)

       if halfing_type == 1:
           PC_subrace = "Lightfoot Halfling"
           Charisma +=1
           race_feature4 = "You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you."

       if halfing_type == 2:
            PC_subrace = "Stout Halfling"
            Constitution +=1
            race_feature4 = "You have advantage on saving throws against poison, and you have resistance to poison damage."

       if halfing_type == 3:
           PC_subrace = "Ghostwise Halfling"
           Wisdom += 1
           race_feature4 = "You can speak telepathically to any creature within 30 feet of you. The creature understands you only if the two of you share a language. You can speak telepathically in this way to one creature at a time."

       if halfing_type == 4:
           PC_subrace = "Lotusden Halfling"
           Wisdom += 1
           race_feature4 = "You know the Druidcraft Cantrip. At 3rd level, you can cast the Entangle spell once per long rest. At 5th level, you can cast Spike Growth spell once per long rest. These spells don't require the material components normally required. Wisdom is your spellcasting ability for these spells."
           race_feature5 = "Ability checks made to track you are at disadvantage and you can move through difficult terrain made of non-magical plants and overgrowth without expending extra movement."

       if halfing_type == 5:
           PC_subrace = "Mark of Hospitality Halfling"
           Charisma +=1
           race_feature4 = "Whenever you roll a Charisma (Persuasion) check or an ability check involving Brewer's Tools or Cook's Utensils, roll a d4 and add the number rolled to the total ability check."
           race_feature5 = "You know the Prestidigitation cantrip. You can also cast Purify Food and Drink and Unseen Servant with this trait. Once you cast either spell with this trait, you can't cast that spell again until you finish a long rest. Charisma is your Spellcasting Ability for these spells."
           race_feature6 = " If you have the Spellcasting or Pact Magic class features, the spells on the Mark of Hospitality Spells table are added to the spell list of your spellcasting class.\n1. Goodberry, Sleep\n2. Aid, Calm Emotions\n3.Create Food and Water, Leomund's Tiny Hut\n4. Aura of Purity, Mordenkainen's Private Sanctum\n5. Hallow"

       if halfing_type == 6:
           PC_subrace = "Mark of Healing Halfling"
           Wisdom +=1
           race_feature4 = "Whenever you roll a Wisdom (Medicine) check or an ability check involving an Herbalism Kit, roll a d4 and add the number rolled to the total ability check."
           race_feature5 = "You can cast the Cure Wounds spell with this trait. Beginning at 3rd level, you can also cast the Lesser Restoration spell with this trait. Once you cast either spell with this trait, you can't cast that spell again until you finish a long rest. Wisdom is your Spellcasting Ability for these spells."
           race_feature6 = " If you have the Spellcasting or Pact Magic class features, the spells on the Mark of Healing Spells table are added to the spell list of your spellcasting class.\n1. Cure Wounds, Healing Word\n2. Lesser Restoration, Prayer of Healing\n3. Aura of Vitality, Mass Healing Word\n4. Aura of Purity, Aura of Life\n5. Greater Restoration"

    if PC_race == "Half-Orc":
        speed = 30
        half_orc_type = randint(1,2)

        if half_orc_type == 1:
            PC_subrace = "Half-Orc"
            Strength += 2
            Constitution += 1
            race_feature1 = "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            global intimidation
            intimidation = 1
            race_feature2 = "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."
            race_feature3 = "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."
            common = 1
            global orc
            orc = 1

        if half_orc_type == 2:
            PC_subrace = "Mark of Finding Half-Orc"
            Wisdom +=2
            race_feature1 = "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            race_feature2 = "Whenever you make a Wisdom (Perception) or a Wisdom (Survival) check, you can roll a d4 and add the number rolled to the total ability check."
            race_feature3 = "You can cast the Hunter's Mark spell with this trait. Starting at 3rd level, you can also cast the Locate Object spell with it. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Wisdom is your Spellcasting Ability for these spells."
            common = 1
            global goblin
            goblin = 1
            race_feature4 = "If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Finding Spells table are added to the spell list of your Spellcasting class.\n1. Faerie Fire, Longstrider\n2.Locate Animals or Plants, Locate Object\n3. Clairvoyance, Speak With Plants\n4. Divination, Locate Creature\n5. Commune With Nature"

    if PC_race == "Human":
        speed = 30
        common = 1
        solo_lang()

        human_type = randint(1,9)

        if human_type == 1:
            Strength += 1
            Dexterity += 1
            Constitution +=1
            Wisdom += 1
            Intelligence += 1
            Charisma += 1
            PC_subrace = "Normal"

        if human_type == 2:
            PC_subrace = "Normal"
            a = 0
            increases = 2
            while increases != 0:
                score_increase = randint(1,6)
                
                while score_increase == a:
                    score_increase = randint(1,5)

                if score_increase == 1:
                    Strength +=1
                if score_increase == 2:
                    Dexterity += 1            
                if score_increase == 3:
                    Constitution += 1
                if score_increase == 4:
                    Wisdom +=1
                if score_increase == 5:
                    Intelligence +=1
                if score_increase == 6:
                    Charisma += 1
                a = score_increase;
                increases -=1
            human_feat = feat()
            solo_skill()

        if human_type == 3:
            PC_subrace = "Mark of Finding Human"
            Wisdom += 2
            Constitution += 1
            race_feature1 = "You can see in dim light within 60ft. of you as if it were bright light, and in darkness as if it were dim light. You can't discern colors in darkness, only shades of grey."
            race_feature2 = "Whenever you make a Wisdom (Perception) or a Wisdom (Survival) check, you can roll a d4 and add the number rolled to the total ability check."
            race_feature3 = "You can cast the Hunter's Mark spell with this trait. Starting at 3rd level, you can also cast the Locate Object spell with it. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Wisdom is your Spellcasting Ability for these spells."
            common = 1
            goblin = 1
            race_feature4 = "If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Finding Spells table are added to the spell list of your Spellcasting class.\n1. Faerie Fire, Longstrider\n2.Locate Animals or Plants, Locate Object\n3. Clairvoyance, Speak With Plants\n4. Divination, Locate Creature\n5. Commune With Nature"

        if human_type == 4:
            PC_subrace = "Mark of Handling Human"
            Wisdom += 2
            score_increase = randint(1,5)
            if score_increase == 1:
                    Strength +=1
            if score_increase == 2:
                    Dexterity += 1            
            if score_increase == 3:
                    Constitution += 1
            if score_increase == 4:
                    Charisma +=1
            if score_increase == 5:
                    Intelligence +=1
         
            race_feature1 = "Whenever you make a Wisdom (Animal Handling) or a Intelligence (Nature) check, you can roll a d4 and add the number rolled to the total ability check."
            race_feature2 = " You can cast the Animal Friendship spell and the Speak With Animals with this trait, requiring no material components. Once you cast either spell with this trait, you can't cast that spell again until you finish a Long Rest. Wisdom is your Spellcasting Ability for these spells."
            race_feature3 = " Starting at 3rd level, you can target a Beast or a Monstrosity when you cast Animal Friendship or Speak With Animals, provided that the creature's intelligence is 3 or lower."
            race_feature4 = "If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Handling Spells table are added to the spell list of your Spellcasting class.\n1. Animal Friendship, Speak With Animals\n2. Beast Sense, Calm Emotions\n3. Beacon of Hope, Conjure Animals\n4. Aura of Life, Dominate Beast\n5. Awaken"

        if human_type == 5:
            PC_subrace = "Mark of Marking Human"
            Intelligence += 2
            score_increase = randint(1,5)
            if score_increase == 1:
                    Strength +=1
            if score_increase == 2:
                    Dexterity += 1            
            if score_increase == 3:
                    Constitution += 1
            if score_increase == 4:
                    Charisma +=1
            if score_increase == 5:
                    Wisdom +=1
            race_feature1 = "Whenever you make an Intelligence (Arcana) or an Ability Check involving Artisan's Tools, you can roll a d4 and add the number rolled to the total ability check."
            race_feature2 = "You gain proficiency in one type of Artisan's Tools of your choice."
            race_feature3 = "You learn the Mending cantrip. You can also cast the Magic Weapon spell with this trait. When you do so, the spell lasts for 1 hour and doesn't require concentration. Once you cast this spell with this trait, you can't cast that spell again until you finish a Long Rest. Intelligence is your Spellcasting Ability for these spells."
            race_feature4 = "If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Making Spells table are added to the spell list of your Spellcasting class.\n1. Identify, Tenser's Floating Disk\n2. Continual Flame, Magic Weapon\n3. Conjure Barrage, Elemental Weapon\n4. Fabricate,Stone Shape\n5. Creation"


        if human_type == 6:
            PC_subrace = "Mark of Passage Human"
            Dexterity += 2
            score_increase = randint(1,5)
            if score_increase == 1:
                    Strength +=1
            if score_increase == 2:
                     Intelligence += 1            
            if score_increase == 3:
                    Constitution += 1
            if score_increase == 4:
                    Charisma +=1
            if score_increase == 5:
                    Wisdom +=1

            speed =35
            race_feature1 = "Whenever you make an Dexterity (Acrobatics) or an Ability Check involving operating or maintaining a Land Vehicle, you can roll a d4 and add the number rolled to the total ability check."
            race_feature2 = "You can cast the Misty Step spell with this trait. Once you cast this spell with this trait, you can't cast that spell again until you finish a Long Rest. Dexterity is your Spellcasting Ability for these spells."
            race_feature3 = " If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Passage Spells table are added to the spell list of your Spellcasting class.\n 1.Expeditious Retreat, Jump\n2. Misty Step, Pass Without Trace\n3. Blink, Phantom Steed\n4. Dimension Door, Freedom of Movement\n5. Teleportation Circle"
        
        if human_type == 7:
            PC_subrace = "Mark of Sentinel Human"
            Constitution += 2
            score_increase = randint(1,5)
            if score_increase == 1:
                    Strength +=1
            if score_increase == 2:
                     Intelligence += 1            
            if score_increase == 3:
                     Dexterity += 1
            if score_increase == 4:
                    Charisma +=1
            if score_increase == 5:
                    Wisdom +=1

            speed =35
            race_feature1 = "Whenever you make an Wisdom (Insight) or a Wisdom (Perception) check, you can roll a d4 and add the number rolled to the total ability check."
            race_feature2 = " You can cast the Shield spell with this trait. Once you cast this spell with this trait, you can't cast that spell again until you finish a Long Rest. Wisdom is your Spellcasting Ability for these spells."
            race_feature3 = "Once a creature that you can see within 5ft of you is hit with an attack roll, you can use your reaction to swap places with the creature, and you are hit by the attack instead. Once you use this trait, you can't do so again until you finish a long rest."
            race_feature4 = " If you have the Spellcasting or Pact Magic class feature, the spells on the Mark of Passage Spells table are added to the spell list of your Spellcasting class.\n 1.Compelled Duel, Shield of Faith\n2. Warding Bond, Zone of Truth\n3. Counterspell, Protection From Energy\n4. Death Ward, Guardian of Faith\n5. Bigby's Hand"
    
        if human_type == 8:
            PC_subrace = "Keldon human"
            Strength += 2
            Constitution += 1
            common = 1 
            global keldon
            keldon = 1
            global athletics 
            athletics = 1
            global PC_str_savethrw
            PC_str_savethrw = 1
            race_feature1 = "You are naturally adapted to cold climates"

        if human_type == 9:
            common = 1
            a= solo_lang()
            while a == common:
                a = solo_lang
            province = randint(1,4) 
            
            if province == 1:
                PC_subrace = "Innistrad Human from the Gavony Province"
                Strength += 1
                Dexterity += 1
                Constitution += 1
                Wisdom += 1
                Intelligence += 1
                Charisma += 1
            
            if province == 2:
                PC_subrace = "Innistrad Human from the Kessig Province"
                Dexterity += 1
                Wisdom += 1
                global survival
                survival = 1
                speed = 40
                race_feature1 = "When you use the Dash action, difficult terrain doesn’t cost you extra movement on that turn."
                race_feature2 = "When you make a melee attack against a creature, you don’t provoke opportunity attacks from that creature for the rest of your turn, whether you hit or not."

            if province == 3:
                PC_subrace = "Innistrad Human from the Nephalia Province"
                Intelligence += 1
                Charisma += 1
                race_feature1 = "You gain proficiency in any combination of four skills or with four tools of your choice."

            if province == 4:
                PC_subrace = "Innistrad Human from the Stensia Province"
                Strength += 1
                Constitution += 1
                intimidation = 1
                race_feature1 = "Your hit point maximum increases by 2, and it increases by 2 every time you gain a level."

    if PC_race == "Tiefling":
        speed = 30
        Charisma += 2
        race_feature1 = "Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."
        race_feature2 = "You have resistance to fire damage."
        common = 1
        global infernal
        infernal = 1
        tiefling_type = randint(1,11)

        if tiefling_type == 1:
            PC_subrace = "Bloodline of Asmodeus Tiefling"
            Intelligence += 1
            race_feature3 = "You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Ray of Sickness spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Crown of Madness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 2:
            PC_subrace = "Bloodline of Baalzebul Tiefling"
            Intelligence += 1
            race_feature3 = "You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Ray of Sickness spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Crown of Madness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 3:
            PC_subrace = "Bloodline of Dispater Tiefling"
            Dexterity += 1
            race_feature3 = "You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Detect Thoughts spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 4:
            PC_subrace = "Bloodline of Fierna Tiefling"
            Wisdom += 1
            race_feature3 = "You know the Friends cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Suggestion spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 5:
             PC_subrace = "Bloodline of Glasya Tiefling"
             Dexterity += 1
             race_feature3 = "ou know the Minor Illusion cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Invisibility spell once as a 2nd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 6:
             PC_subrace = "Bloodline of Levistus Tiefling"
             Constitution += 1
             race_feature3 = "You know the Ray of Frost cantrip. Once you reach 3rd level, you can cast the Armor of Agathys spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 7:
            PC_subrace = "Bloodline of Mammon Tiefling"
            Intelligence += 1
            race_feature3 = " You know the Mage Hand cantrip. Once you reach 3rd level, you can cast the Tenser's Floating Disk spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Arcane Lock spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 8:
            PC_subrace = "Bloodline of Mephistopheles Tiefling"
            Intelligence += 1
            race_feature3 = " You know the Mage Hand cantrip. Once you reach 3rd level, you can cast the Burning Hands spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Flame Blade spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 9:
            PC_subrace = "Bloodline of Zariel Tiefling"
            Strength += 1
            race_feature3 = "You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Searing Smite spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

        if tiefling_type == 10:
            Charisma -= 2
            Dexterity += 2
            Intelligence += 1
            PC_subrace = "Variant Tiefling"
            tiefling_power = randint(1,3)
            if tiefling_power == 1:
                race_feature3 = "You know the Vicious Mockery cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Enthrall spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

            if tiefling_power == 2:
                race_feature3 = " Once you reach 3rd level, you can cast the Burning Hands spell once as a 2nd-level spell."

            if tiefling_power == 3:
                race_feature3 == "You have bat-like wings sprouting from your shoulders. You have a flying speed of 30 feet while you aren’t wearing heavy armor."


        if tiefling_type == 11:
            PC_subrace == "Abyssal Tiefling"
            Constitution += 1
            race_feature3 = "Each time you finish a long rest, you gain the ability to cast cantrips and spells randomly determined from a short list. At 1st level, you can cast a cantrip. When you reach 3rd level, you can also cast a 1st-level spell. At 5th level, you can cast a 2nd-level spell.\nYou can cast a spell gained from this trait only once until you complete your next long rest. You can cast a cantrip gained from this trait at will, as normal. For 1st-level spells whose effect changes if cast using a spell slot of 2nd level or higher, you cast the spell as if using a 2nd-level slot. Spells of 2nd level are cast as if using a 2nd-level slot.\nAt the end of each long rest, you lose the cantrips and spells previously granted by this feature, even if you did not cast them. You replace those cantrips and spells by rolling for new ones on the Abyssal Arcana Spells table. Roll separately for each cantrip and spell. If you roll the same spell or cantrip you gained at the end of your previous long rest, roll again until you get a different result.\n1st Level: Dancing Lights,True Strike,Light,Message,Spare the Dying,Prestidigtation\3rd LeveL: Burning Hands,Charm Person,Magic Missile,Cure Wounds,Tasha's Hideous Laughter,Thunderwave\n5th level: Alter Self,Darkness,Invisibility,Levitate,Mirror Image,Spider Climb"
            race_feature4 = "Your hit point maximum increases by half your level (minimum 1)."

def class_features(PC_class,PC_level):
    global PC_hp
    global hit_dice
    global class_feature1
    global class_feature2
    global class_feature3
    global class_feature4
    global class_feature5    
    global class_feature6
    global class_feature7
    global class_feature8
    global class_feature9
    global class_feature10
    global class_feature11
    global class_feature12
    global class_feature13
    global class_feature14
    global class_feature15
    global class_feature16
    global class_feature17
    global class_equipment
    global class_equipment2
    global class_equipment3
    global class_equipment4
    global class_equipment5
    global Strength
    global Dexterity
    global Constitution
    global Intelligence
    global Charisma
    global Wisdom
    global PC_subclass
    global PC_prof_bonus
    global feat1
    global feat2
    global feat3
    global feat4
    global feat5
    global feat6
    global feat7
    global cantrip1
    global cantrip2
    global cantrip3
    global cantrip4
    global cantrip5
    global cantrip6
    global cantrip7
    global level_1_spell1
    global level_1_spell2
    global level_1_spell3
    global level_1_spell4
    global level_1_spell5
    global level_1_spell6
    global level_2_spell1
    global level_2_spell2
    global level_2_spell3
    global level_3_spell1
    global level_3_spell2
    global level_3_spell3
    global level_4_spell1
    global level_4_spell2
    global level_4_spell3
    global level_5_spell1
    global level_5_spell2
    global level_5_spell3
    global level_6_spell1
    global level_6_spell2
    global level_7_spell1
    global level_7_spell2
    global level_8_spell1
    global level_9_spell1
    global caster
    global scimitar
    global heavy_armor
    global persuasion
    global performance

    if PC_class == "Barbarian":

       hit_dice = "1d12 per barbarian level"
       first_lvl_hp = 12 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
           temp = randint(1,12)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1
       
       PC_hp = first_lvl_hp + high_lvl_hp

       global light_armor
       light_armor = 1

       global medium_armor
       medium_armor = 1

       global shields
       shields = 1

       global simple_weapons
       simple_weapons = 1

       global martial_weapons
       martial_weapons = 1

       global PC_str_savethrw
       PC_str_savethrw = 1
       global PC_con_savethrw
       PC_con_savethrw = 1

       global animal_handling
       global athletics
       global intimidation
       global nature
       global preception
       global survival

       skill_prof = randint(1,6)

       if skill_prof == 1:
           animal_handling = 1
       
       if skill_prof == 2:
           athletics = 1

       if skill_prof == 3:
           intimidation = 1
       
       if skill_prof == 4:
           nature = 1

       if skill_prof == 5:
          preception = 1
       
       if skill_prof == 6:
           survival = 1

       skill_prof2 = randint(1,6)
       while skill_prof == skill_prof2:
           skill_prof2 = randint(1,6)

       if skill_prof2 == 1:
           animal_handling = 1
       
       if skill_prof2 == 2:
           athletics = 1

       if skill_prof2 == 3:
           intimidation = 1
       
       if skill_prof2 == 4:
           nature = 1

       if skill_prof2 == 5:
          preception = 1
       
       if skill_prof2 == 6:
           survival = 1

       equipment = randint(1,2)
       if equipment == 1:
           class_equipment = "A greataxe"
       if equipment == 2:
           class_equipment = "Any martial melee weapon"
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment2 = "two handaxes"
       if equipment == 2:
           class_equipment2 = "any simple weapon"
       class_equipment3 = "An explorer's pack and four javelins"

       class_feature1 = ("Rage: In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.\n"
                         "While raging, you gain the following benefits if you aren't wearing heavy armor:\n"
                         "You have advantage on Strength checks and Strength saving throws.\n"
                         "When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.\n"
                         "You have resistance to bludgeoning, piercing, and slashing damage.\n"
                         "If you are able to cast spells, you can't cast them or concentrate on them while raging.\n"
                         "Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.\n"
                         "Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.\n"
                         "Starting out, you get 2 rages. This increases to 3 at the third level, to 4 at the 6th level, to 5 at the 12th level, to 6 at the 17th level, to unlimited at level 20"
                         "Starting out, your damage bonus is 2. This increases to 3 at level 9, and to 4 at level 16")

       class_feature2 = "While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit."

       if PC_level >= 2:
           class_feature3 = "At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated."
           class_feature4 = "Reckless Attack: Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn."

       if PC_level >= 3:

           skill_prof3 = randint(1,6)
           while skill_prof3 == skill_prof2 or skill_prof3 == skill_prof:
            skill_prof3 = randint(1,6)

           if skill_prof3 == 1:
               animal_handling = 1
       
           if skill_prof3 == 2:
               athletics = 1

           if skill_prof3 == 3:
               intimidation = 1
       
           if skill_prof3 == 4:
               nature = 1

           if skill_prof3 == 5:
              preception = 1
       
           if skill_prof3 == 6:
               survival = 1

           primal_path_choice = randint(1,10)
       
           if primal_path_choice == 1:
               PC_subclass = "Path of the Ancestral Guardian"
               class_feature5 = "Starting when you choose this path at 3rd level, spectral warriors appear when you enter your rage. While you’re raging, the first creature you hit with an attack on your turn becomes the target of the warriors, which hinder its attacks.\nUntil the start of your next turn, that target has disadvantage on any attack roll that isn't against you, and when the target hits a creature other than you with an attack, that creature has resistance to the damage of the target’s attacks."

           if primal_path_choice == 2 and PC_race == "Dwarf":
               PC_subclass = "Path of the Battlerager"
               class_feature5 = ("When you choose this path at 3rd level, you gain the ability to use spiked armor as a weapon."
                                 "While you are wearing spiked armor and are raging, you can use a bonus action to make one melee weapon attack with your armor spikes against a target within 5 feet of you. If the attack hits, the spikes deal 1d4 piercing damage. You use your Strength modifier for the attack and damage rolls.\n"
                                 "Additionally, when you use the Attack action to grapple a creature, the target takes 3 piercing damage if your grapple check succeeds.")


           while primal_path_choice == 2 and PC_race != "Dwarf":
               primal_path_choice = randint(1,12)

           if primal_path_choice == 3:
               PC_subclass = "Path of the Beast"
               class_feature5 = ("Starting when you choose this path at 3rd level, when you enter your rage, you can transform, revealing the bestial power within you. Until the rage ends, you manifest a natural weapon. It counts as a simple melee weapon for you, and you add your Strength modifier to the attack and damage rolls when you attack with it, as normal.\n"
                                "You choose the weapon’s form each time you rage:\nBite. Your mouth transforms into a bestial muzzle or great mandibles (your choice). It deals 1d8 piercing damage on a hit. Once on each of your turns when you damage a creature with this bite, you regain a number of hit points equal to your proficiency bonus, provided you have less than half your hit points when you hit.\n"
                                "Claws. Each of your hands transforms into a claw, which you can use as a weapon if it’s empty. It deals 1d6 slashing damage on a hit. Once on each of your turns when you attack with a claw using the Attack action, you can make one additional claw attack as part of the same action.\n"
                                "Tail. You grow a lashing, spiny tail, which deals 1d8 piercing damage on a hit and has the reach property. If a creature you can see within 10 feet of you hits you with an attack roll, you can use your reaction to swipe your tail and roll a d8, applying a bonus to your AC equal to the number rolled, potentially causing the attack to miss you.")
    
           if primal_path_choice == 4:
               PC_subclass = "Path of the Berserker"
               class_feature5 = "Starting when you choose this path at 3rd level, you can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion."
               
           if primal_path_choice == 5:
               PC_subclass = "Path of the Storm Herald"
               class_feature5 = ("When you select this path at 3rd level, you emanate a stormy, magical aura while you rage. The aura extends 10 feet from you in every direction, but not through total cover.\n"
                                   "Your aura has an effect that activates when you enter your rage, and you can activate the effect again on each of your turns as a bonus action. Choose desert, sea, or tundra. Your aura's effect depends on that chosen environment, as detailed below. You can change your environment choice whenever you gain a level in this class.\n"
                                   "If your aura's effects require a saving throw, the DC equals 8 + your proficiency bonus + your Constitution modifier.\n"
                                   "Desert. When this effect is activated, all other creatures in your aura take 2 fire damage each. The damage increases when you reach certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, and 6 at 20th level."
                                   "Sea. When this effect is activated, you can choose one other creature you can see in your aura. The target must make a Dexterity saving throw. The target takes 1d6 lightning damage on a failed save, or half as much damage on a successful one. The damage increases when you reach certain levels in this class, increasing to 2d6 at 10th level, 3d6 at 15th level, and 4d6 at 20th level.\n"
                                   "Tundra. When this effect is activated, each creature of your choice in your aura gains 2 temporary hit points, as icy spirits inure it to suffering. The temporary hit points increase when you reach certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, and 6 at 20th level.\n")


           if primal_path_choice == 6:
               PC_subclass = "Path of the Totem Warrior"
               class_feature5 = ("Yours is a path that seeks attunement with the natural world, giving you a kinship with beasts. At 3rd level when you adopt this path, you gain the ability to cast the Beast Sense and Speak with Animals spells, but only as rituals.\n\n"
                                 "At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal\n"
                                 "At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.\n"
                                 "Your totem animal might be an animal related to those listed here but more appropriate to your homeland. For example, you could choose a hawk or vulture in place of an eagle.\n"
                                 "Bear. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.\n"
                                 "Eagle. While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.\n"
                                 "Elk. While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift."
                                 "Tiger. While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.\n"
                                 "Wolf. While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters."
                                 )
           if primal_path_choice == 7:
               PC_subclass = "Path of the Wild Magic"
               class_feature5 =("As an action, you can open your awareness to the presence of concentrated magic. Until the end of your next turn, you know the location of any spell or magic item within 60 feet of you that isn’t behind total cover.\n When you sense a spell, you learn which school of magic it belongs to."
                                 "The magical energy roiling inside you sometimes erupts from you. When you enter your rage, roll on the Wild Magic table to determine the magical effect produced.\nIf the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Constitution modifier."
                                 "1.Each creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d12 necrotic damage. You also gain temporary hit points equal to 1d12 plus your barbarian level.\n"
                                 "2.You teleport up to 30 feet to an unoccupied space you can see. Until your rage ends, you can use this effect again on each of your turns as a bonus action.\n"
                                 "3.An intangible spirit, which looks like a flumph or a pixie (your choice), appears within 5 feet of one creature of your choice that you can see within 30 feet of you. At the end of the current turn, the spirit explodes, and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 1d6 force damage. Until your rage ends, you can use this effect again, summoning another spirit, on each of your turns as a bonus action.\n"
                                 "4.A bolt of light shoots from your chest. Another creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d6 radiant damage and be blinded until the start of your next turn. Until your rage ends, you can use this effect again on each of your turns as a bonus action.\n"
                                 "5.Whenever a creature hits you with an attack roll before your rage ends, that creature takes 1d6 force damage, as magic lashes out in retribution.\n"
                                 "6.Until your rage ends, you are surrounded by multicolored, protective lights; you gain a +1 bonus to AC, and while within 10 feet of you, your allies gain the same bonus.\n"
                                 "7.Flowers and vines temporarily grow around you; until your rage ends, the ground within 15 feet of you is difficult terrain for your enemies.\n"
                                 "8. Magic infuses one weapon of your choice that you are holding. Until your rage ends, the weapon’s damage type changes to force, and it gains the light and thrown properties, with a normal range of 20 feet and a long range of 60 feet. If the weapon leaves your hand, the weapon reappears in your hand at the end of the current turn.\n")

           if primal_path_choice == 8:
               PC_subclass = "Path of the Zealot"
               class_feature5 = "Starting when you choose this path at 3rd level, you can channel divine fury into your weapon strikes. While you're raging, the first creature you hit on each of your turns with a weapon attack takes extra damage equal to 1d6 + half your Barbarian level.\nThe extra damage is necrotic or radiant; you choose the type of damage when you gain this feature.\nAt 3rd level, your soul is marked for endless battle. If a spell, such as Raise Dead, has the sole effect of restoring you to life (but not undeath), the caster doesn't need material components to cast the spell on you."

           if primal_path_choice == 9:
               PC_subclass = "Path of the Depths"
               class_feature5 =("At 3rd level when you adopt this path, you gain a swimming speed equal to your walking speed and gain the ability to breathe underwater.\nStarting when you choose this path at 3rd level, you manifest an extra appendage when you enter your rage. This weapon can appear as a kraken tentacle, a giant anchor, preternatural jaws, or something else based on your history.\n"
                                "As a bonus action, you can use this appendage to strike at one creature of your choice that you can see within 15 feet. The target must succeed on a Strength saving throw (DC equal to 8 + your proficiency bonus + your Strength modifier) or be pulled up to 10 feet in a straight line towards you.")

           if primal_path_choice == 10:
               PC_subclass = "Path of the Juggernaut"
               class_feature5 = ("Starting when you choose this path at 3rd level, your rage instills you with the strength to batter around your foes, making any battlefield your domain.\n"
                                "Once per turn while raging, when you damage a creature with a melee attack, you can force the target to make a Strength saving throw (DC 8 + your proficiency bonus + your Strength modifier). On a failure, you push the target 5 feet away from you, and you can choose to immediately move 5 feet into the target’s previous position.")

       if PC_level >= 4:
           feat1 = ability_score_improvement()

       if PC_level >= 5:
           class_feature6 = "You can attack twice whenever you take the Attack action on your turn.\n Your speed increases by 10 feet while you aren't wearing heavy armor"
           PC_prof_bonus = 3

       if PC_level >= 6:
            if primal_path_choice == 1:
               
               class_feature7 = ("Beginning at 6th level, the guardian spirits that aid you can provide supernatural protection to those you defend. If you are raging and a creature you can see within 30 feet of you takes damage, you can use your reaction to reduce that damage by 2d6.\n"
                                 "When you reach certain levels in this class, you can reduce the damage by more: by 3d6 at 10th level and by 4d6 at 14th level.")
            if primal_path_choice == 2 and PC_race == "Dwarf":
               
               class_feature7 = ("Beginning at 6th level, when you use Reckless Attack while raging, you also gain temporary hit points equal to your Constitution modifier (minimum of 1). They vanish if any of them are left when your rage ends.")
 
            if primal_path_choice == 3:
               class_feature7 = ("Beginning at 6th level, the feral power within you increases, causing the natural weapons of your Form of the Beast to count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.\nYou can also alter your form to help you adapt to your surroundings. When you finish a short or long rest, choose one of the following benefits, which lasts until you finish a short or long rest:\n"
                                "You gain a swimming speed equal to your walking speed, and you can breathe underwater.\n"
                                "You gain a climbing speed equal to your walking speed, and you can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
                                "When you jump, you can make a Strength (Athletics) check and extend your jump by a number of feet equal to the check’s total. You can make this special check only once per turn.")
    
            if primal_path_choice == 4:
               
               class_feature7 = "Beginning at 6th level, you can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage."
            
            if primal_path_choice == 5:
               PC_subclass = "Path of the Storm Herald"
               class_feature7 = ("At 6th level, the storm grants you benefits even when your aura isn't active. The benefits are based on the environment you chose for your Storm Aura.\n"
                                   "Desert. You gain resistance to fire damage, and you don’t suffer the effects of extreme heat, as described in the Dungeon Master's Guide. Moreover, as an action, you can touch a flammable object that isn't being worn or carried by anyone else and set it on fire."
                                   "Sea.You gain resistance to lightning damage, and you can breathe underwater. You also gain a swimming speed of 30 feet."
                                   "Tundra.  You gain resistance to cold damage, and you don’t suffer the effects of extreme cold, as described in the Dungeon Master's Guide. Moreover, as an action, you can touch water and turn a 5-foot cube of it into ice, which melts after 1 minute. This action fails if a creature is in the cube.")
            
            if primal_path_choice == 6:
               PC_subclass = "Path of the Totem Warrior"
               class_feature7 = ("At 6th level, you gain a magical benefit based on the totem animal of your choice. You can choose the same animal you selected at 3rd level or a different one.\n"
                                 "Bear.You gain the might of a bear. Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects.\n"
                                 "Eagle.You gain the eyesight of an eagle. You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks.\n"
                                 "Elk. Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated. The elk spirit helps you roam far and fast.\n"
                                 "Tiger. You gain proficiency in two skills from the following list: Athletics, Acrobatics, Stealth, and Survival. The cat spirit hones your survival instincts.\n"
                                 "Wolf. You gain the hunting sensibilities of a wolf. You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace.."
                                 )
            if primal_path_choice == 7:
               
               class_feature7 =("You can harness your wild magic to bolster yourself or a companion. As an action, you can touch one creature (which can be yourself ) and confer one of the following benefits of your choice to that creature:\n"
                                "For 10 minutes, the creature can roll a d3 whenever making an attack roll or an ability check and add the number rolled to the d20 roll.\n"
                                "Roll a d3. The creature regains one expended spell slot, the level of which equals the number rolled or lower (the creature’s choice). Once a creature receives this benefit, that creature can’t receive it again until after a long rest.\n"
                                "You can take this action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")


            if primal_path_choice == 8:
               PC_subclass = "Path of the Zealot"
               class_feature7 = "Starting at 6th level, the divine power that fuels your rage can protect you. If you fail a saving throw while raging, you can reroll it, and you must use the new roll. You can use this ability only once per rage."

            if primal_path_choice == 9:
               PC_subclass = "Path of the Depths"
               class_feature7 ="Beginning at 6th level, you can burst into water then materialize somewhere else as an action. You magically teleport along with any equipment you are wearing or carrying, up to 30 feet to an unoccupied space you can see. Before or after teleporting, you can make one attack, as part of your action. Moving in this way does not provoke opportunity attacks."

            if primal_path_choice == 10:
               PC_subclass = "Path of the Juggernaut"
               class_feature7 = "Beginning at 6th level, you can muster destructive force with your assault, shaking the core of even the strongest structures. All of your melee attacks gain the siege property (your attacks deal double damage to objects and structures). Your melee attacks against creatures of the construct type deal an additional 1d8 weapon damage."

       if PC_level >= 7:
           class_feature8 = "By 7th level, your instincts are so honed that you have advantage on initiative rolls.\nAdditionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn\nAt 7th level, as part of the bonus action you take to enter your rage, you can move up to half your speed."

       if PC_level >= 8:
           feat2 = ability_score_improvement()

       if PC_level >= 9:
           class_feature9 = "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.\nThis increases to two additional dice at 13th level and three additional dice at 17th level."
           PC_prof_bonus = 4

       if PC_level >= 10:
           skill_prof4 = randint(1,6)
           while skill_prof4 == skill_prof3 or skill_prof4 == skill_prof2 or skill_prof4 == skill_prof:
            skill_prof4 = randint(1,6)

           if skill_prof4 == 1:
               animal_handling = 1
       
           if skill_prof4 == 2:
               athletics = 1

           if skill_prof4 == 3:
               intimidation = 1
       
           if skill_prof4 == 4:
               nature = 1

           if skill_prof4 == 5:
              preception = 1
       
           if skill_prof4 == 6:
               survival = 1
          
           if primal_path_choice == 1:
               
               class_feature10 = ("At 10th level, you gain the ability to consult with your ancestral spirits. When you do so, you cast the Augury or Clairvoyance spell, without using a spell slot or material components. Rather than creating a spherical sensor, this use of Clairvoyance invisibly summons one of your ancestral spirits to the chosen location. Wisdom is your spellcasting ability for these spells.\n"
                                 "After you cast either spell in this way, you can’t use this feature again until you finish a short or long rest.")

           if primal_path_choice == 2 and PC_race == "Dwarf":
               
               class_feature10 = ("Beginning at 10th level, you can take the Dash action as a bonus action while you are raging.")
 
           if primal_path_choice == 3:
               class_feature10 = ("At 10th level, when you hit a creature with your natural weapons while you are raging, the beast within you can curse your target with rabid fury. The target must succeed on a Wisdom saving throw (DC equal to 8 + your Constitution modifier + your proficiency bonus) or suffer one of the following effects (your choice):\n"
                                "The target must use its reaction to make a melee attack against another creature of your choice that you can see.\n"
                                "Target takes 2d12 psychic damage.\n"
                                "You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")
    
           if primal_path_choice == 4:
               
               class_feature10 = ("Beginning at 10th level, you can use your action to frighten someone with your menacing presence. When you do so, choose one creature that you can see within 30 feet of you.\n"
                                  "If the creature can see or hear you, it must succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus + your Charisma modifier) or be frightened of you until the end of your next turn.\n"
                                  "On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you.\n"
                                  "If the creature succeeds on its saving throw, you can't use this feature on that creature again for 24 hours.")

           if primal_path_choice == 5:

               class_feature10 = ("At 10th level, you learn to use your mastery of the storm to protect others. Each creature of your choice has the damage resistance you gained from the Storm Soul feature while the creature is in your Storm Aura.")

           if primal_path_choice == 6:

               class_feature10 = ("At 10th level, you can cast the Commune with Nature spell, but only as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek.")
           if primal_path_choice == 7:
               
               class_feature10 =("At 10th level, when you are imperiled during your rage, the magic within you can lash out; immediately after you take damage or fail a saving throw while raging, you can use your reaction to roll on the Wild Magic table and immediately produce the effect rolled. This effect replaces your current Wild Magic effect.")


           if primal_path_choice == 8:
               PC_subclass = "Path of the Zealot"
               class_feature10 = "At 10th level, you learn to channel divine power to inspire zealotry in others. As a bonus action, you unleash a battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of you that can hear you gain advantage on attack rolls and saving throws until the start of your next turn.\nOnce you use this feature, you can’t use it again until you finish a long rest."

           if primal_path_choice == 9:
               PC_subclass = "Path of the Depths"
               class_feature10 =("At 10th level, you can manifest additional adaptations of the deep. Select one of the below adaptations you manifest, during a long rest you may replace your chosen manifestation with a new option from this list:\n"
                                  "Eyes of the Deep: You gain the ability to use echolocation. When you do so, you cast the True Seeing spell, without using a spell slot or material components. After you cast a spell in this way, you can’t use this feature again until you finish a short or long rest.\n"
                                  "Arms of the Deep: While raging, you now manifest two magical appendages, which may be tentacles, chains and anchors, animated rigging, or another grasping arm of your choice. When you use your dredge line ability, you can attempt a grapple with each of your appendages.\n"
                                  "Heart of the Deep: Now on your turn, you can use a bonus action to gain temporary hit points equal to 1d12 + your barbarian level. Once you use this feature, you must finish a short or long rest before you can use it again.\n"
                                  "Soul of the Deep: You are now immune to all effects that would cause you to be charmed or frightened.\n"
                                  "Armor of the Deep: Your skin hardens, increasing your Armor Class by 1.")

           if primal_path_choice == 10:
               PC_subclass = "Path of the Juggernaut"
               class_feature10 = "Upon reaching 10th level, you wade into armies of foes, great swings of your weapon striking any who threaten you. When you make a weapon attack while raging, you can make another attack as a bonus action with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon."

       if PC_level >= 11:
           class_feature11 = "Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.\nEach time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10."

       if PC_level >=12:
          feat3 = ability_score_improvement()

       if PC_level >= 13:
           PC_prof_bonus = 5

       if PC_level >= 14:
            if primal_path_choice == 1:
               
               class_feature12 = "(At 14th level, your ancestral spirits grow powerful enough to retaliate. When you use your Spirit Shield to reduce the damage of an attack, the attacker takes an amount of force damage that your Spirit Shield prevents."
               
            if primal_path_choice == 2 and PC_race == "Dwarf":
               
               class_feature12 = ("Starting at 14th level, when a creature within 5 feet of you hits you with a melee attack, the attacker takes 3 piercing damage if you are raging, aren't incapacitated, and are wearing spiked armor.")
 
            if primal_path_choice == 3:
               class_feature12 = ("At 14th level, the beast within you grows so powerful that you can spread its ferocity to others and gain resilience from them joining your hunt. When you enter your rage, you can choose a number of other willing creatures you can see within 30 feet of you equal to your Constitution modifier (minimum of one creature). You gain 5 temporary hit points for each creature that accepts this feature.\nUntil the rage ends, the chosen creatures can use the following benefit once on each of their turns: when the creature hits a target with an attack roll and deals damage to it, the creature can roll a d6 and gain a bonus to the damage equal to the number rolled."
                                  "\nYou can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")
                                
            if primal_path_choice == 4:
               
               class_feature12 = "Starting at 14th level, when you take damage from a creature that is within 5 feet of you, you can use your reaction to make a melee weapon attack against that creature."
            
            if primal_path_choice == 5:
               PC_subclass = "Path of the Storm Herald"
               class_feature12 = ("At 14th level, the power of the storm you channel grows mightier, lashing out at your foes. The effect is based on the environment you chose for your Storm Aura.\n"
                                   "Desert. Immediately after a creature in your aura hits you with an attack, you can use your reaction to force that creature to make a Dexterity saving throw. On a failed save, the creature takes fire damage equal to your Barbarian level.\n"
                                   "Sea. When you hit a creature in your aura with an attack, you can use your reaction to force that creature to make a Strength saving throw. On a failed save, the creature is knocked prone, as if struck by a wave.\n"
                                   "Tundra.  Whenever the effect of your Storm Aura is activated, you can choose one creature you can see in the aura. That creature must succeed on a Strength saving throw, or its speed is reduced to 0 until the start of your next turn, as magical frost covers it.")
            
            if primal_path_choice == 6:
               PC_subclass = "Path of the Totem Warrior"
               class_feature12 = ("At 14th level, you gain a magical benefit based on a totem animal of your choice. You can choose the same animal you selected previously or a different one.\n"
                                 "Bear.While you're raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.\n"
                                 "Eagle.While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft\n."
                                 "Elk. While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC 8 + your Strength bonus + your proficiency bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier.\n"
                                 "Tiger. While you're raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it.\n"
                                 "Wolf. While you're raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack."
                                 )
            if primal_path_choice == 7:
               
               class_feature12 =("At 14th level, whenever you roll on the Wild Magic table, you can roll the die twice and choose which of the two effects to unleash. If you roll the same number on both dice, you can ignore the number and choose any effect on the table.")


            if primal_path_choice == 8:
               PC_subclass = "Path of the Zealot"
               class_feature12 = "Beginning at 14th level, the divine power that fuels your rage allows you to shrug off fatal blows. While you're raging, having 0 hit points doesn’t knock you unconscious. You still must make death saving throws, and you suffer the normal effects of taking damage while at 0 hit points. However, if you would die due to failing death saving throws, you don’t die until your rage ends, and you die then only if you still have 0 hit points."

            if primal_path_choice == 9:
               PC_subclass = "Path of the Depths"
               class_feature12 ="At 14th level, when you use your ghostwater dive ability, you can choose to appear with a wave of tidal force. When you appear all creatures within 10 feet of you must make a Strength saving throw. On a failed save a creature takes 3d6 force damage and is knocked prone. On a successful save, a creature takes half damage and is not knocked prone."

            if primal_path_choice == 10:
               PC_subclass = "Path of the Juggernaut"
               class_feature12 = "Starting at 14th level, you can choose to become unstoppable when you enter a rage. If you do so, for the duration of the rage your speed cannot be reduced, and you are immune to the frightened, paralyzed, and stunned conditions. If you are frightened, paralyzed, or stunned, you can still take your bonus action to enter your rage and suspend the effects for the duration of the rage. When your rage ends, you suffer one level of exhaustion."

       if PC_level >= 15:
           class_feature13 = "Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it."

       if PC_level >= 16:
           feat4 = ability_score_improvement()

       if PC_level >= 17:
           PC_prof_bonus = 6

       if PC_level >= 18:
           class_feature14 = "Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total."

       if PC_level >= 19:
          feat5 = ability_score_improvement()

       if PC_level >= 20:
           class_feature15 = "At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24."
           Strength += 4
           Constitution += 4

    if PC_class == "Bard":

       caster = "True"
       hit_dice = "1d8 per bard level"
       first_lvl_hp = 8 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
           temp = randint(1,8)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1
       


       PC_hp = first_lvl_hp + high_lvl_hp
       global musical_instrument
       global rapier
       global shortsword
       global hand_crossbow
       global longsword
       shortsword = 1
       hand_crossbow = 1
       rapier = 1
       longsword = 1
       simple_weapons = 1
       musical_instrument = 1

       global PC_dex_savethrw
       PC_dex_savethrw = 1
       global PC_cha_savethrw
       PC_cha_savethrw = 1

       a = solo_skill()
       b = solo_skill()
       while b == a:
           b = solo_skill()
       c = solo_skill()
       while c == b or c == a:
           c = solo_skill()

       equipment = randint(1,3)
       if equipment == 1:
           class_equipment = "A rapier"
       if equipment == 2:
           class_equipment = "A longsword"
       if equipment == 3:
           class_equipment = "Any simple weapon"
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment2 = "A diplomat's pack"
       if equipment == 2:
           class_equipment2 = "An entertainers pack"
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment3 = "A lute"
       if equipment == 2:
           class_equipment3 = "Any musical instrument"
       class_equipment4 = "Leather armor and a dagger"
       
       class_feature1 = "Spellcasting: You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations.\n Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability.\nIn addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one.\nSpell save DC = 8 + your proficiency bonus + your Charisma modifier\nSpell attack modifier = your proficiency bonus + your Charisma modifier\nYou can cast any bard spell you know as a ritual if that spell has the ritual tag.\nYou can use a musical instrument as a spellcasting focus for your bard spells."
       cantrip1 = bard_cantrip()
       cantrip2 = bard_cantrip()
       while cantrip1 == cantrip2:
           cantrip2 = bard_cantrip()
       level_1_spell1 = bard_level_1()
       level_1_spell2 = bard_level_1()
       while level_1_spell1 == level_1_spell2:
           level_1_spell2 = bard_level_1()

       level_1_spell3 = bard_level_1()
       while level_1_spell1 == level_1_spell3 or  level_1_spell2 == level_1_spell3:
                level_1_spell3 = bard_level_1()

       level_1_spell4 = bard_level_1()
       while level_1_spell1 == level_1_spell4 or  level_1_spell2 == level_1_spell4 or level_1_spell3 == level_1_spell4:
                level_1_spell4 = bard_level_1()

       class_feature2 = ("Your spellcasting chart is shown below"
     "                                           Slot Types\n"
           "Level     Cantrips Known    Spells Known    1st     2nd     3rd     4th     5th     6th     7th     8th     9th\n"
           "  1             2                 4          2\n"
           "  2             2                 5          3\n"
           "  3             2                 6          4       2\n"
           "  4             3                 7          4       3\n"
           "  5             3                 8          4       3       2\n"
           "  6             3                 9          4       3       3\n"
           "  7             3                 10         4       3       3       1\n"
           "  8             3                 11         4       3       3       2\n"
           "  9             3                 12         4       3       3       3       1\n"
           "  10            4                 14         4       3       3       3       2\n"
           "  11            4                 15         4       3       3       3       2       1\n"
           "  12            4                 15         4       3       3       3       2       1\n"
           "  13            4                 16         4       3       3       3       2       1       1\n"
           "  14            4                 18         4       3       3       3       2       1       1\n"
           "  15            4                 19         4       3       3       3       2       1       1       1\n"
           "  16            4                 19         4       3       3       3       2       1       1       1\n"
           "  17            4                 20         4       3       3       3       2       1       1       1       1\n"
           "  18            4                 22         4       3       3       3       3       1       1       1       1\n"
           "  19            4                 22         4       3       3       3       3       2       1       1       1\n"
           "  20            4                 22         4       3       3       3       3       2       2       1       1\n")

       class_feature3 = ("Bardic Inspiration: You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6."
                         "\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails.Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time."
                         "You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.\n"
                         "Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.")
       if PC_level >= 2:
           class_feature4 = "Jack of All Trades: Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus."
           class_feature5 = "Song of Rest: Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance spend one or more Hit Dice to regain hit points at the end of the short rest, each of those creatures regains an extra 1d6 hit points.\nThe extra Hit Points increase when you reach certain levels in this class: to 1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th level."
           class_feature6 = "Magical Inspiration: At 2nd level, if a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost."
           
           level_1_spell5 = bard_level_1()
           while level_1_spell1 == level_1_spell5 or  level_1_spell2 == level_1_spell5 or level_1_spell3 == level_1_spell5 or level_1_spell4 == level_1_spell5:
                level_1_spell5 = bard_level_1()


       if PC_level >= 3:
           class_feature8 = "Expertise: At 3rd level, choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. At 10th level, you can choose another two skill proficiencies to gain this benefit."
           
           level_2_spell1 = bard_level_2()

           bard_school_choice = randint(1,11)

           if bard_school_choice == 1:
               PC_subclass = "College of Creation"
               class_feature7 = ("Note of Potential: When you join the College of Creation at 3rd level, whenever you give a creature a Bardic Inspiration die, you can utter a note from the Song of Creation to create a Tiny mote of potential, which orbits within 5 feet of that creature. The mote is intangible and invulnerable, and it lasts until the Bardic Inspiration die is lost. The mote looks like a musical note, a star, a flower, or another symbol of art or life that you choose."
                                 "\nWhen the creature uses the Bardic Inspiration die, the mote provides an additional effect based on whether the die benefits an ability check, an attack roll, or a saving throw, as detailed below:\n"
                                 "\nAbility Check. When the creature rolls the Bardic Inspiration die to add it to an ability check, the creature can roll the Bardic Inspiration die again and choose which roll to use, as the mote pops and emits colorful, harmless sparks for a moment."
                                 "\nAttack Roll. Immediately after the creature rolls the Bardic Inspiration die to add it to an attack roll against a target, the mote thunderously shatters. The target and each creature of your choice that you can see within 5 feet of it must succeed on a Constitution saving throw against your spell save DC or take thunder damage equal to the number rolled on the Bardic Inspiration die."
                                 "\nSaving Throw. Immediately after the creature rolls the Bardic Inspiration die and adds it to a saving throw, the mote vanishes with the sound of soft music, causing the creature to gain temporary hit points equal to the number rolled on the Bardic Inspiration die plus your Charisma modifier (minimum of 1 temporary hit point)."
                                 "\nAlso at 3rd level, as an action, you can channel the magic of the Song of Creation to create one nonmagical item of your choice in an unoccupied space within 10 feet of you. The item must appear on a surface or in a liquid that can support it. The gp value of the item can't be more than 20 times your bard level, and the item must be Medium or smaller. The item glimmers softly, and a creature can faintly hear music when touching it. The created item disappears after a number of hours equal to your proficiency bonus."
                                 "\nOnce you create an item with this feature, you can't do so again until you finish a long rest, unless you expend a spell slot of 2nd level or higher to use this feature again. You can have only one item created by this feature at a time; if you use this action and already have an item from this feature, the first one immediately vanishes."
                                 "\nThe size of the item you can create with this feature increases by one size category when you reach 6th level (Large) and 14th level (Huge)."                                
                                 )

           if bard_school_choice == 2:
               PC_subclass = "College of Eloquence"
               class_feature7 = ("Silver Tongue: Starting at 3rd level, you are a master at saying the right thing at the right time. When you make a Charisma (Persuasion) or Charisma (Deception) check, you can treat a d20 roll of 9 or lower as a 10.\n"
                                 "Unsettling Words: Also at 3rd level, you can spin words laced with magic that unsettle a creature and cause it to doubt itself. As a bonus action, you can expend one use of your Bardic Inspiration and choose one creature you can see within 60 feet of you. Roll the Bardic Inspiration die. The creature must subtract the number rolled from the next saving throw it makes before the start of your next turn.")
               

           if bard_school_choice == 3:
               PC_subclass = "College of Glamour"
               class_feature7 = ("Mantle of Inspiration: When you join the College of Glamour at 3rd level, you gain the ability to weave a song of fey magic that imbues your allies with vigor and speed.\n"
                                  "As a bonus action, you can expend one use of your Bardic Inspiration to grant yourself a wondrous appearance. When you do so, choose a number of creatures you can see and who can see you within 60 feet of you, up to a number equal to your Charisma modifier (minimum of one). Each of them gains 5 temporary hit points. When a creature gains these temporary hit points, it can immediately use its reaction to move up to its speed, without provoking opportunity attacks."
                                  "\nThe number of temporary hit points increases when you reach certain levels in this class, increasing to 8 at 5th level, 11 at 10th level, and 14 at 15th level."
                                  "\nEnthralling Performance: Starting at 3rd level, you can charge your performance with seductive, fey magic. If you perform for at least 1 minute, you can attempt to inspire wonder in your audience by singing, reciting a poem, or dancing. At the end of the performance, choose a number of humanoids within 60 feet of you who watched and listened to all of it, up to a number equal to your Charisma modifier (minimum of one)\n"
                                  "Each target must succeed on a Wisdom saving throw against your spell save DC or be charmed by you. While charmed in this way, the target idolizes you, it speaks glowingly of you to anyone who speaks to it, and it hinders anyone who opposes you, avoiding violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies.\n"
                                  "If a target succeeds on its saving throw, the target has no hint that you tried to charm it. Once you use this feature, you can’t use it again until you finish a short or long rest.")

           if bard_school_choice == 4:
               PC_subclass = "College of Lore"
               class_feature7 = "Cutting Words: You learn how to use your wit to distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the DM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed."
               a = solo_skill()
               b = solo_skill()
               while a == b:
                   b = solo_skill()
               c = solo_skill()
               while a == c or b == c:
                   c = solo_skill()

           if bard_school_choice == 5:
               PC_subclass = "College of Swords"
               scimitar = 1
               medium_armor = 1
               variant_feature = randint(1,2)
               
               if variant_feature == 1:
                    class_feature7 = ("Fighting Style: You adopt a particular style of fighting as your specialty. Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\n"                 
                                        "In addition, if you’re proficient with a simple or martial melee weapon, you can use it as a spellcasting focus for your bard spells.\n"
                                        "Blade Flourish: At 3rd level, you learn to conduct impressive displays of martial prowess and speed. Whenever you take the Attack action on your turn, your walking speed increases by 10 feet until the end of the turn, and if a weapon attack that you make as part of this action hits a creature, you can use one of the following Blade Flourish options of your choice. You can use only one Blade Flourish option per turn\n"
                                        "       Defensive Flourish. You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You also add the number rolled to your AC until the start of your next turn.\n"
                                        "       Slashing Flourish. You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit and to any other creature of your choice that you can see within 5 feet of you. The damage equals the number you roll on the Bardic Inspiration die.\n"
                                        "       Mobile Flourish. You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You can also push the target up to 5 feet away from you, plus a number of feet equal to the number you roll on that die. You can then immediately use your reaction to move up to your walking speed to an unoccupied space within 5 feet of the target")
               if variant_feature == 2:
                   class_feature7 = ("Fighting Style: You adopt a particular style of fighting as your specialty. Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.\n"                 
                                        "In addition, if you’re proficient with a simple or martial melee weapon, you can use it as a spellcasting focus for your bard spells.\n"
                                        "Blade Flourish: At 3rd level, you learn to conduct impressive displays of martial prowess and speed. Whenever you take the Attack action on your turn, your walking speed increases by 10 feet until the end of the turn, and if a weapon attack that you make as part of this action hits a creature, you can use one of the following Blade Flourish options of your choice. You can use only one Blade Flourish option per turn\n"
                                        "       Defensive Flourish. You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You also add the number rolled to your AC until the start of your next turn.\n"
                                        "       Slashing Flourish. You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit and to any other creature of your choice that you can see within 5 feet of you. The damage equals the number you roll on the Bardic Inspiration die.\n"
                                        "       Mobile Flourish. You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You can also push the target up to 5 feet away from you, plus a number of feet equal to the number you roll on that die. You can then immediately use your reaction to move up to your walking speed to an unoccupied space within 5 feet of the target")
               


           if bard_school_choice == 6:
               PC_subclass = "College of Valor"
               medium_armor = 1
               shields = 1
               martial_weapons = 1
               class_feature7 = "Combat Inspiration: You learn to inspire others in battle. A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses."

           if bard_school_choice == 7:
               PC_subclass = "College of Whispers"
               class_feature7 = ("Psychic Blades: When you join the College of Whispers at 3rd level, you gain the ability to make your weapon attacks magically toxic to a creature's mind. When you hit a creature with a weapon attack, you can expend one use of your Bardic Inspiration to deal an additional 2d6 psychic damage to that target. You can do so only once per round on your turn.\n"
                                "The psychic damage increases when you reach certain levels in this class, increasing to 3d6 at 5th level, 5d6 at 10th level, and 8d6 at 15th level.\n"
                                "Words of Terror: At 3rd level, you learn to infuse innocent-seeming words with an insidious magic that can inspire terror. If you speak to a humanoid alone for at least 1 minute, you can attempt to seed paranoia and fear into its mind. At the end of the conversation, the target must succeed on a Wisdom saving throw against your spell save DC or be frightened of you or another creature of your choice. The target is frightened in this way for 1 hour, until it is attacked or damaged, or until it witnesses its allies being attacked or damaged."
                                "\nIf the target succeeds on its saving throw, the target has no hint that you tried to frighten it. Once you use this feature, you can’t use it again until you finish a short rest or long rest.")
         
           if bard_school_choice == 8:
               PC_subclass = "College of Spirits"
               class_feature7 = ("Guiding Whispers: At 3rd level, you can reach out to spirits to guide you and others. You learn the Guidance cantrip, which doesn’t count against the number of bard cantrips you know. For you, it has a range of 60 feet when you cast it.\n"
                                 "Spiritual Focus: At 3rd level, your practice of contacting spirits can employ special tools. You can use the following objects as a spellcasting focus for your bard spells: a candle, a crystal ball, a talking board, a tarokka deck, or a skull.\n"
                                 "Tales from Beyond: At 3rd level, you reach out to spirits who tell their tales through you. While you are holding your Spiritual Focus, you can use a bonus action to expend one use of your Bardic Inspiration and roll on the Spirits’ Tales table using your Bardic Inspiration die to determine the tale told. You retain the tale in mind until you bestow the tale’s effect or you finish a short or long rest.\n"
                                 "You can use an action to choose one creature you can see within 30 feet of you (this can be you) to be the target of the tale’s effect. Once you do so, you can’t bestow the tale’s effect again until you roll it again. You can retain only one of these tales in mind at a time, and rolling on the Spirits’ Tales table immediately ends the effect of the previous tale. If the tale requires a saving throw, the DC equals your spell save DC.\n"
                                 "\n1. Beast: You recite the tale of a clever animal. For 1 minute, the target has advantage on Wisdom (Perception) checks and advantage on attack rolls against a creature if another enemy is within 5 feet of it, and that enemy isn’t incapacitated."
                                 "\n2. Warrior: You recount the story of a renowned duelist. Make a melee spell attack against the target as an attacking spectral warrior briefly appears in an unoccupied space within 5 feet of the target before vanishing. On a hit, the target takes force damage equal to two rolls of your Bardic Inspiration die + your Charisma modifier."
                                 "\n3. Friends: You recite the tale of friends who found each other in the afterlife. The target and another creature of its choice it can see within 5 feet of it regains hit points equal to a roll of your Bardic Inspiration die + your Charisma modifier"
                                 "\n4. Runaway: You tell the tale of an adventurer that could escape any confinement. The target can immediately use its reaction to teleport up to 30 feet to an unoccupied space it can see. When the target teleports, it can choose a number of creatures it can see within 30 feet of it up to your Charisma modifier (minimum of 1) to immediately use the same reaction."
                                 "\n5. Avenger: You recount the tale of an avenging knight. For 1 minute, whenever a creature the target can see within 30 feet of it is damaged by a creature, the target can use its reaction to deal force damage equal to a roll of your Bardic Inspiration die to the attacker."
                                 "\n6. Hero: You speak the tale of an epic hero. Choose a creature you can see within 30 feet of you. The target gains temporary hit points equal to a roll of your Bardic Inspiration die + your bard level. While it has these temporary hit points, the target’s walking speed increases by 10 feet."
                                 "\n7. Fey: You recount the tale of a mischievous fey. The target must succeed on a Wisdom saving throw or become charmed by you until the end of its next turn. The charmed target must use its action to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no other creature."
                                 "\n8. Dark Spirit: You speak a dreadful tale of a slayer in the dark. The target becomes invisible until the end of its next turn or until it hits a creature with an attack. If it hits a creature with an attack during this invisibility, that creature takes necrotic damage equal to a roll of your Bardic Inspiration die and is frightened of the target until the end of its next turn."
                                 "\n9. Giant: You speak of the deeds of a mighty giant. Each creature of the target’s choice it can see within 30 feet of it must make a Strength saving throw, taking force damage equal to two rolls of your Bardic Inspiration die on a failed save and is knocked prone. A creature that succeeds on its saving throw takes half as much damage and isn’t knocked prone."
                                 "\n10. Dragon: You breathe a poem of a wrathful dragon. The target magically spews fire from their mouth in a 30-foot cone. Each creature in that area must make a Dexterity saving throw, taking fire damage equal to three rolls of your Bardic Inspiration die on a failed save, or half as much damage on a successful one."
                                 "\n11. Celestial: You speak of the exalted deeds of a celestial. The target regains hit points equal to two rolls of your Bardic Inspiration die + your bard level, and you end one disease or a condition from the following list affecting the target: blinded, deafened, paralyzed, petrified, or poisoned."
                                 "\n12. Unknown: You utter an incomprehensible fable from a being beyond the stars. Choose a creature you can see within 30 feet of you. The target must succeed on an Intelligence saving throw or take psychic damage equal to three rolls of your Bardic Inspiration die, and the target is unable to speak any language for 1 minute.")

           if bard_school_choice == 9:
               PC_subclass = "College of the Dire Singer"
               class_feature7 = ("Broad Inspiration: When you join the College of Dirge Singers at 3rd level, you learn to strengthen the hearts of your troops and stir them to greatness. You learn the Guidance cantrip, which is considered a bard spell for you, but doesn’t count against your number of cantrips known.\Andditionally, as a bonus action, you can expend one use of your Bardic Inspiration to inspire multiple allies. When you do so, choose two creatures within 60 feet of you that can hear you. Each creature gains one Bardic Inspiration die.\nYour Bardic Inspiration die does not change at 5th level, but remains a d6; it becomes a d8 at 10th level, and a d10 at 15th level.\n"
                                "Keeper of History: Also at 3rd level, you gain proficiency in either History or Performance. If you are already proficient in both of these skills, you gain proficiency in one of the following skills of your choice: Arcana, Intimidation, or Persuasion.\n In addition, choose either History or Performance. Your proficiency bonus is doubled for any ability check you make that uses that skill.")

           if bard_school_choice == 10:
               PC_subclass = "College of the Maestro"
               class_feature7 = ("Battle Muse: When you join the College of the Maestro at 3rd level, you gain one additional use of your Bardic Inspiration feature.\nThis feature grants you another additional use of Bardic Inspiration at 6th level, and again at 14th level."
                                 "Symphony of Conflict: You've been trained in the bardic art of magically manipulating the sounds of combat into a concert of powerful melodies that can alter the very battlefield around you.\nWhen you select this bardic school at 3rd level, you learn 2 conducting techniques of your choice, shown below. All techniques require at least one free hand, baton, or wand to utilize. For these techniques to function, you must be able to see your target, and they must be able to hear you.\nYou learn 1 additional conducting technique of your choice at 6th and 14th level. Each time you learn a new technique, you can also replace one technique you know with a different one.\n"
                                 "\n1. Aria of Suspense (Ansia). You build an air of tension and paranoia with subtle, droning tones. As an action, you expend and roll a Bardic Inspiration die. For the next 10 minutes, any creatures of your choice within 60 feet cannot be surprised, and gain a bonus on saving throws against traps and environmental hazards equal to your Bardic Inspiration die roll."
                                 "\n2. Crash (Marcato). You learn how to harness and amplify the roar of a well-placed blow into a violent explosion of sound. When a creature other than yourself within 60 feet of you hits with an attack, you can use your reaction to expend and roll a Bardic Inspiration die. The target of the triggering attack must make a Strength saving throw against your Spell save DC or take thunder damage equal to half of the number you rolled and be knocked prone."
                                 "\n3. Dirge of Dread (Finale). You play a terrifying dirge to accompany a deathblow, striking fear into the hearts of your nearby enemies. When an ally brings a creature within 60 feet to 0 hitpoints, you can use your reaction to expend and roll a Bardic Inspiration die. Select a number of creatures within 15 feet of the triggering ally equal to half of the number rolled (minimum 1). Each target must make a Wisdom saving throw against your Spell save DC or become frightened of the triggering ally until the end of that ally's next turn. After the effect ends, or the save is successful, targeted creatures are immune to Dirge of Dread for the next 24 hours."
                                 "\n4. Dissonance (Discordia). Summoning a harsh, discordant tone, you muddle the mind of an opponent, lessening their defenses. When a creature within 60 feet is forced to make a saving throw, you can use your reaction to expend and roll a Bardic Inspiration die. You reduce their saving throw by half of the number rolled. You can use this feature after the creature makes its saving throw roll, but before the DM determines a success or failure."
                                 "\n5. Guiding Tone (Fermata). You drag a sharp, powerful chord through the mind of a creature, forcing it to suddenly stumble in a direction you wish. As a bonus action, you expend and roll a Bardic Inspiration die and select a creature other than yourself within 60 feet. The target must succeed on a Wisdom saving throw against your Spell save DC or take psychic damage equal to half of the number rolled and be pushed 10 feet in a direction you choose. A target can fail the saving throw voluntarily."
                                 "\n6. Hasten Tempo (Accelerando). Your manipulation of tempo and song can inspire others to act more quickly. You can use your Bonus action on your turn to choose one creature other than yourself within 60 feet. Expend and roll a Bardic Inspiration die, adding the number rolled to the creature's initiative and moving them up to the initiative order accordingly. If this would move them higher than you, they immediately take their turn after you finish this round. A creature cannot be affected by Hasten Tempo again until they've finished a short or long rest."
                                 "\n7. Hymm of Harmony (Armonia). The melodies surrounding your allies promote rapid recovery. When a creature that has a Bardic Inspiration die from you regains any hitpoints, they can expend and roll their inspiration die to regain additional hitpoints equal to the number rolled."
                                 "\n8. Majestic Anthem (Maestoso). Pulled from the chaos, you muster an uplifting melody that bolsters the resolve of your allies. You can expend and roll a Bardic Inspiration die as an action, and all other creatures you choose within 60 ft gain temporary hitpoints equal to the number rolled plus your Charisma modifier (minimum of 1). These temporary hitpoints last until the end of your next turn."
                                 "\n9. Resonance (Risonanza). You shape the harmonic vibrations of a weapon's movements into a dangerous, sonic enhancement. Using a bonus action, you can expend and roll a Bardic Inspiration die, choosing one weapon within 60 feet of you. Until the end of your next turn, all attacks with that weapon deal additional thunder damage equal to half of the number rolled (minimum of 1)."
                                 "\n10.Sprint (Presto). The song you conjure can stir the winds, pushing along those who require expedient travel. A creature that has a Bardic Inspiration die from you can expend and roll their inspiration to increase their speed for that turn. A roll of 1-4 increases their speed of 10 feet, a roll of 5-8 increases their speed by 15 feet, and a roll of 9-12 increases their speed by 20 feet.")

           if bard_school_choice == 11:
               PC_subclass = "College of Satire"
               class_feature7 = ("Bonus Proficiencies: When you join the College of Satire at 3rd level, you gain proficiency with thieves’ tools. You also gain proficiency in Sleight of Hand and one additional skill of your choice. If you are already proficient with thieves’ tools or in Sleight of Hand, choose another skill proficiency for each proficiency you already have.\n"
                                "Tumbling Fool: At 3rd level, you master a variety of acrobatic techniques that allow you to evade danger. As a bonus action, you can tumble. When you tumble, you gain the following benefits for the rest of your turn:\n"
                                "     You gain the benefits of taking the Dash and Disengage actions.\n"
                                "     You gain a climbing speed equal to your current speed.\n"
                                "     You take half damage from falling.\n")

       if PC_level >= 4:
           level_2_spell2 = bard_level_2()
           while level_2_spell1 == level_2_spell2:
               level_2_spell2 = bard_level_2()

           cantrip3 = bard_cantrip()
           while cantrip3 == cantrip2 or cantrip3 == cantrip1:
                cantrip3 = bard_cantrip()
           feat1 = ability_score_improvement()
           class_feature8 = "Bardic Versatility: Whenever you reach a level in this class that grants the Ability Score Improvement feature (4,8,12,16,19), you can do one of the following, representing a change in focus as you use your skills and magic:\n1. Replace one of the skills you chose for the Expertise feature with one of your other skill proficiencies that isn't benefiting from Expertise.\n 2. Replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the bard spell list."

       if PC_level >= 5:
           
           PC_prof_bonus = 3
           level_3_spell1 = bard_level_3()
           class_feature9 = "Font of Inspiration: Beginning when you reach 5th level, you regain all of your expended uses of Bardic Inspiration when you finish a short or long rest."

       if PC_level >= 6:
           class_feature10 = "Countercharm: At 6th level, you gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required)."

           level_3_spell2 = bard_level_3()

           while level_3_spell1 == level_3_spell2:
                 level_3_spell2 = bard_level_3()

           if bard_school_choice == 1:
               PC_subclass = "College of Creation"
               class_feature11 = ("Animating Performance: By 6th level, as an action, you can target a Large or smaller nonmagical item you can see within 30 feet of you and animate it. The animate item uses the Dancing Item stat block, which uses your proficiency bonus (PB), The item is friendly to you and your companions and obeys your commands. It lives for 1 hour, until it is reduced to 0 hit points, or until you die."
                                 "\nIn combat, the item shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the item can take any action of its choice, not just Dodge.\n"
                                 "When you use your Bardic Inspiration feature, you can command the item as part of the same bonus action you use for Bardic Inspiration."
                                 "\nOnce you animate an item with this feature, you can't do so again until you finish a long rest, unless you expend a spell slot of 3rd level or higher to use this feature again. You can have only one item animated by this feature at a time; if you use this action and already have a dancing item from this feature, the first one immediately becomes inanimate.")

           if bard_school_choice == 2:
               PC_subclass = "College of Eloquence"
               class_feature11 = "Unfailing Inspiration: At 6th level, your inspiring words are so persuasive that others feel driven to succeed. When a creature adds one of your Bardic Inspiration dice to its ability check, attack roll, or saving throw and the roll fails, the creature can keep the Bardic Inspiration die\nUniversal Speech: Also at 6th level, you have gained the ability to make your speech intelligible to any creature. As an action, choose one or more creatures within 60 feet of you, up to a number equal to your Charisma modifier (minimum of one creature). The chosen creatures can magically understand you, regardless of the language you speak, for 1 hour.\nOnce you use this feature, you can't use it again until you finish a long rest, unless you expend a spell slot to use it again."

           if bard_school_choice == 3:
               PC_subclass = "College of Glamour"
               class_feature11 = ("Mantle of Majesty: At 6th level, you gain the ability to cloak yourself in a fey magic that makes others want to serve you. As a bonus action, you cast Command, without expending a spell slot, and you take on an appearance of unearthly beauty for 1 minute or until your concentration ends (as if you were concentrating on a spell). During this time, you can cast Command as a bonus action on each of your turns, without expending a spell slot.\n"
                                  "Any creature charmed by you automatically fails its saving throw against the Command you cast with this feature."
                                  "\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                                 
           if bard_school_choice == 4:
               PC_subclass = "College of Lore"
               class_feature11 = "Additional Magical Secrets: At 6th level, you learn two spells of your choice from any class. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. The chosen spells count as bard spells for you but don't count against the number of bard spells you know."

           if bard_school_choice == 5:
               PC_subclass = "College of Swords"
               class_feature11 = "Extra Attack: Starting at 6th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."

           if bard_school_choice == 6:
               PC_subclass = "College of Valor"
               class_feature11 = "Starting at 6th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."

           if bard_school_choice == 10:
               PC_subclass = "College of Whispers"
               class_feature11 = ("Mantle of Whispers: At 6th level, you gain the ability to adopt a humanoid's persona. When a humanoid dies within 30 feet of you, you can magically capture its shadow using your reaction. You retain this shadow until you use it or you finish a long rest.\n"
                                "You can use the shadow as an action. When you do so, it vanishes, magically transforming into a disguise that appears on you. You now look like the dead person, but healthy and alive. This disguise lasts for 1 hour or until you end it as a bonus action.\n"
                                "While you're in the disguise, you gain access to all information that the humanoid would freely share with a casual acquaintance. Such information includes general details on its background and personal life, but doesn't include secrets. The information is enough that you can pass yourself off as the person by drawing on its memories."
                                "\nAnother creature can see through this disguise by succeeding on a Wisdom (Insight) check contested by your Charisma (Deception) check. You gain a +5 bonus to your check.\nOnce you capture a shadow with this feature, you can't capture another one with it until you finish a short or long rest.")
         
           if bard_school_choice == 8:
               PC_subclass = "College of Spirits"
               class_feature11 = ("Spirit Session: At 6th level, you can channel spirits to gain insights into magic. You can conduct an hour-long ritual channeling spirits (which can be done during a short or long rest) using your Spiritual Focus.\n"
                                 "You can conduct the ritual with a number of creatures equal to your proficiency bonus (including yourself). At the end of the ritual, you temporarily learn one spell of your choice from any class.\n"
                                 "The spell you choose must be of a level equal to the number of creatures that conducted the ritual or less, the spell must of a level you can cast, and it must be in the school of divination or necromancy. The chosen spell counts as a bard spell for you but doesn’t count against the number of bard spells you know.\n"
                                 "Once you perform the ritual, you can’t do so again until you start a long rest, and you know the chosen spell until you start a long rest.")
          
           if bard_school_choice == 9:
               PC_subclass = "College of the Dire Singer"
               class_feature11 = "Commanding Voice: Starting at 6th level, you excel at inspiring and directing soldiers in battle. When a creature that has a Bardic Inspiration die from you takes the Attack action on its turn, you can use your reaction to allow it an additional weapon attack. The creature rolls the Bardic Inspiration die, adding the number rolled to its weapon damage roll."

           if bard_school_choice == 10:
               PC_subclass = "College of the Maestro"
               class_feature11 = ("Frenetic Crescendo: At 6th level, you can harness the beat of battle, whipping it into a frenzy of drums, chants, and glory. You can use your action to expend any number of uses of your Bardic Inspiration feature. For each expended use, you can immediately grant a Bardic Inspiration die to a creature other than yourself within 60 feet that you can see. A creature can have only one Bardic Inspiration die at a time.\nOnce you use this feature, you must finish a long rest before you can use it again.")

           if bard_school_choice == 11:
               PC_subclass = "College of Satire"
               class_feature11 = ("Fool's Insight: At 6th level, your ability to gather stories and lore gains a supernatural edge. You can cast Detect Thoughts up to a number of times equal to your Charisma modifier. You regain any expended uses of this ability after completing a long rest.\n"
                                "If a creature resists your attempt to probe deeper and succeeds at its saving throw against your Detect Thoughts, it immediately suffers an embarrassing social gaffe. It might loudly pass gas, unleash a thunderous burp, trip and fall, or be compelled to tell a tasteless joke.")

       if PC_level >= 7:
           level_4_spell1 = bard_level_4()

       if PC_level >= 8:
           feat2 = ability_score_improvement()
           level_4_spell2 = bard_level_4()

           while level_4_spell1 == level_4_spell2:
                 level_4_spell2 = bard_level_4()
       
       if PC_level >= 9:
           level_5_spell1 = bard_level_5()
           PC_prof_bonus = 4

       if PC_level >= 10:
             cantrip4 = bard_cantrip()
             while cantrip4 == cantrip2 or cantrip4 == cantrip1 or cantrip4 == cantrip3:
                cantrip4 = bard_cantrip()

             class_feature12 = "Magical Secrets: By 10th level, you have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any class, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.\nThe chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.\nYou learn two additional spells from any class at 14th level and again at 18th level."

       if PC_level >= 11:
           level_6_spell1 = bard_level_6()

       if PC_level >= 12:
           feat3 = ability_score_improvement()

       if PC_level >= 13:
           PC_prof_bonus = 5 
           level_7_spell1 = bard_level_7()

       if PC_level >= 14:
           if bard_school_choice == 1:
               PC_subclass = "College of Creation"
               class_feature13 = "Creative Crescendo: At 14th level, when you use your Performance of Creation feature, you can create more than one item at once. The number of items equals your Charisma modifier (minimum of two items). If you create an item that would exceed that number, you choose which of the previously created items disappears. Only one of these items can be of the maximum size you can create; the rest must be Small or Tiny.\nYou are no longer limited by gp value when creating items with Performance of Creation."


           if bard_school_choice == 2:
               PC_subclass = "College of Eloquence"
               class_feature13 = "Infectious Inspiration: At 14th level, when you successfully inspire someone, the power of your eloquence can now spread to someone else. When a creature within 60 feet of you adds one of your Bardic Inspiration dice to its ability check, attack roll, or saving throw and the roll succeeds, you can use your reaction to encourage a different creature (other than yourself) that can hear you within 60 feet of you, giving it a Bardic Inspiration die without expending any of your Bardic Inspiration uses.\nYou can use this reaction a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a long rest."

           if bard_school_choice == 3:
               PC_subclass = "College of Glamour"
               class_feature13 = ("Unbreakable Majesty: At 14th level, your appearance permanently gains an otherworldly aspect that makes you look more lovely and fierce.\n"
                                  "In addition, as a bonus action, you can assume a magically majestic presence for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack you for the first time on a turn, the attacker must make a Charisma saving throw against your spell save DC. On a failed save, it can't attack you on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack you on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn."
                                  "\nOnce you assume this majestic presence, you can't do so again until you finish a short or long rest.")
                                 
           if bard_school_choice == 4:
               PC_subclass = "College of Lore"
               class_feature13 = "Peerless Skill: Starting at 14th level, when you make an ability check, you can expend one use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the DM tells you whether you succeed or fail."

           if bard_school_choice == 5:
               PC_subclass = "College of Swords"
               class_feature13 = "Master's Flourish: Starting at 14th level, whenever you use a Blade Flourish option, you can roll a d6 and use it instead of expending a Bardic Inspiration die."

           if bard_school_choice == 6:
               PC_subclass = "College of Valor"
               class_feature13 = "Battle Magic: At 14th level, you have mastered the art of weaving spellcasting and weapon use into a single harmonious act. When you use your action to cast a bard spell, you can make one weapon attack as a bonus action"

           if bard_school_choice == 10:
               PC_subclass = "College of Whispers"
               class_feature13 = ("Shadow Lore: At 14th level, you gain the ability to weave dark magic into your words and tap into a creature’s deepest fears.\n"
                                "As an action, you magically whisper a phrase that only one creature of your choice within 30 feet of you can hear. The target must make a Wisdom saving throw against your spell save DC. It automatically succeeds if it doesn’t share a language with you or if it can’t hear you. On a successful saving throw, your whisper sounds like unintelligible mumbling and has no effect.\n"
                                "If the target fails its saving throw, it is charmed by you for the next 8 hours or until you or your allies attack or damage it. It interprets the whispers as a description of its most mortifying secret."
                                "\nWhile you gain no knowledge of this secret, the target is convinced you know it. While charmed in this way, the creature obeys your commands for fear that you will reveal its secret. It won’t risk its life for you or fight for you, unless it was already inclined to do so. It grants you favors and gifts it would offer to a close friend.\n"
                                "When the effect ends, the creature has no understanding of why it held you in such fear.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
         
           if bard_school_choice == 8:
               PC_subclass = "College of Spirits"
               class_feature13 = "Mystical Connection: At 14th level, your connection to spirits has become semipermanent. Whenever you use your Tales from Beyond feature, you can roll a d6 and use it instead of expending a Bardic Inspiration die. You still use your Bardic Inspiration die for the tale’s effect, without expending it."

           if bard_school_choice == 9:
               PC_subclass = "College of the Dire Singer"
               class_feature13 = "Master Commander: Starting at 14th level, you unflaggingly maintain the spirits and discipline of your unit. During your turn, you can use Countercharm as a bonus action. When you start a Countercharm performance, if any creature that gains its benefit is currently charmed or frightened, it can immediately make another saving throw against the effect that imposed the condition.\nIn addition, when a creature that gains the benefit of your Countercharm performance makes an ability check or saving throw, it can roll a d4 and add the number rolled to the ability check or saving throw."

           if bard_school_choice == 10:
               PC_subclass = "College of the Maestro"
               class_feature13 = "Virtuoso of Captivation: Upon reaching 14th level, you can begin conducting a mystical symphony as an action, distracting and capturing the minds of nearby creatures. For up to 10 minutes, any number of creatures you choose within 60 feet who can hear you have disadvantage on any saving throws against being charmed and against magical sleep.\nIn addition, affected targets have disadvantage on Wisdom (Perception) rolls that rely on sight or sound to detect targets other than you.\nIn combat, you must spend your action each turn to continue the performance or the effect ends. Once you use Virtuoso of Captivation, you must finish a short or long rest before you can use it again."

           if bard_school_choice == 11:
               PC_subclass = "College of Satire"
               class_feature13 = "Fool's Luck:: At 14th level, you can expend one use of Bardic Inspiration after you fail an ability check, fail a saving throw, or miss with an attack roll. Roll a Bardic Inspiration die and add the number rolled to your attack, saving throw, or ability check, using the new result in place of the failed one.\nIf using this ability grants you a success on the attack, saving throw, or ability check, note the number you rolled on the Bardic Inspiration die. The DM can then apply that result as a penalty to an attack or check you make, and you cannot use this ability again until you suffer this drawback. When the DM invokes this penalty, describe an embarrassing gaffe or mistake you make as part of the affected die roll."

       if PC_level >= 15:
           level_8_spell1 = bard_level_8()

       if PC_level >= 16:
           feat5 = ability_score_improvement()

       if PC_level >= 17:
           PC_prof_bonus = 6
           level_9_spell1 = bard_level_9()

       #Level 18 is covered by magical secrets

       if PC_level >= 19:
           feat6 = ability_score_improvement()
          
       if PC_level >= 20:
          class_feature14= "Superior Inspiration: At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, you regain one use."

    if PC_class == "Cleric":
       caster = "True"
       hit_dice = "1d8 per cleric level"
       first_lvl_hp = 8 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
          temp = randint(1,8)+ modifier(Constitution)
          if temp < 0:
               temp = 0
          high_lvl_hp += temp
          hp_level -= 1
       
       PC_hp = first_lvl_hp + high_lvl_hp
       light_armor = 1
       medium_armor = 1
       shields = 1
       simple_weapons = 1

       global PC_wis_savethrw
       PC_wis_savethrw = 1
       PC_cha_savethrw = 1

       skill1 = randint(1,5)
       if skill1 == 1:
           history = 1
       if skill1 == 2:
            insight = 1
       if skill1 == 3:
            medicine = 1
       if skill1 == 4:
            persuasion = 1
       if skill1 == 5:
           religion = 1

       skill2 = randint(1,5)
       while skill1 == skill2:
           skill2 = randint(1,5)
       if skill1 == 1:
           history = 1
       if skill1 == 2:
            insight = 1
       if skill1 == 3:
            medicine = 1
       if skill1 == 4:
            persuasion = 1
       if skill1 == 5:
           religion = 1


      
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment = "A mace"
       if equipment == 2:
           class_equipment = "A Warhammer"
       equipment = randint(1,3)
       if equipment == 1:
           class_equipment2 = "Scale Mail"
       if equipment == 2:
           class_equipment2 = "Leather Armor"
       if equipment == 3:
           class_equipment2 = "Chain Mail"
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment3 = "A light crossbow and 20 bolts"
       if equipment == 2:
           class_equipment3 = "Any simple weapon"
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment4 = "A priest's pack"
       if equipment == 2:
           class_equipment4 = "An explorer's pack"
       class_equipment5 = "A shield and a holy symbol"

       cleric_subclass = randint(1,21)

       if cleric_subclass == 1:
           PC_subclass = "Arcana Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Detect Magic, Magic Missile "
                            "3. Magic Weapon,  Nystul's Magic Aura "
                            "5. Dispel Magic, Magic Circle "
                            "7. Arcane Eye, Leomund's Secret Chest "
                            "9. Planar Binding, Teleportation Circle")
           arcana = 1
           cantrip6 = wizard_cantrip();
           cantrip7 = wizard_cantrip();
           while cantrip6 == cantrip7:
               cantrip7 = wizard_cantrip();

       if cleric_subclass == 2:
           PC_subclass = "Death Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. False Life, Ray of Sickness "
                            "3. Blindness/Deafness, Ray of Enfeeblement "
                            "5. Animate Dead, Vampiric Touch "
                            "7. Blight, Death Ward "
                            "9. Antilife Shell, Cloudkill")
           martial_weapons = 1
           class_feature5 = "At 1st level, you learn one necromancy cantrip of your choice from any spell list. When you cast a necromancy cantrip that normally targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other.\n"

       if cleric_subclass == 3:
           PC_subclass = "Forge Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Identify, Searing Smite "
                            "3. Magic Weapon, Heat Metal "
                            "5. Elemental Weapon, Protection from Energy "
                            "7. Fabricate, Wall of Fire "
                            "9. Animate Objects, Creation")
           artisan_tools = 1
           heavy_armor = 1
           class_feature5 = "At 1st level, you gain the ability to imbue magic into a weapon or armor. At the end of a long rest, you can touch one nonmagical object that is a suit of armor or a simple or martial weapon. Until the end of your next long rest or until you die, the object becomes a magic item, granting a +1 bonus to AC if it’s armor or a +1 bonus to attack and damage rolls if it’s a weapon.\nOnce you use this feature, you can’t use it again until you finish a long rest."

       if cleric_subclass == 4:
           PC_subclass = "Grave Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Bane, False Life "
                            "3. Gentle Repose, Ray of Enfeeblement "
                            "5. Revivify, Vampiric Touch "
                            "7. Blight, Death Ward "
                            "9. Antilife Shell, Raise Dead")
           cantrip6 = "Spare the Dying"
           class_feature5 = ("At 1st level, you gain the ability to manipulate the line between life and death. When you would normally roll one or more dice to restore hit points with a spell to a creature at 0 hit points, you instead use the highest number possible for each die.\n"
                            "In addition, you learn the Spare the Dying cantrip, which doesn't count against the number of cleric cantrips you know. For you, it has a range of 30 feet, and you can cast it as a bonus action."
                            "\nAt 1st level, you gain the ability to occasionally sense the presence of the undead, whose existence is an insult to the natural cycle of life. As an action, you can open your awareness to magically detect undead. Until the end of your next turn, you know the location of any undead within 60 feet of you that isn't behind total cover and that isn't protected from divination magic. This sense doesn't tell you anything about a creature's capabilities or identity.\nYou can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a long rest.")
       if cleric_subclass == 5:
           PC_subclass = "Knowledge Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Command, Identify "
                            "3. Augury, Suggestion "
                            "5. Nondetection,, Speak with Dead "
                            "7. Arcane Eye, Confusion "
                            "9. Legend Lore, Scrying")
           class_feature5 = "At 1st level, you learn two languages of your choice. You also become proficient in your choice of two of the following skills: Arcana, History, Nature, or Religion.\nYour proficiency bonus is doubled for any ability check you make that uses either of those skills."

       if cleric_subclass == 6:
           PC_subclass = "Life Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Bless, Cure Wounds "
                            "3. Lesser Restoration, Spiritual Weapon "
                            "5. Beacon of Hope, Revivify "
                            "7. Death Ward, Guardian of Faith "
                            "9. Mass Cure Wounds, Raise Dead")
           heavy_armor = 1
           class_feature5 = "your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level."

       if cleric_subclass == 7:
           PC_subclass = "Light Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Burning Hands, Faerie Fire "
                            "3. Flaming Sphere, Scorching Ray "
                            "5. Daylight, Fireball "
                            "7. Guardian of Faith, Wall of Fire"
                            "9. Flame Strike, Scrying")
           class_feature5 = "Also at 1st level, you can interpose divine light between yourself and an attacking enemy. When you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses. An attacker that can't be blinded is immune to this feature.\nYou can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."

       if cleric_subclass == 9:
           PC_subclass = "Nature Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Animal Friendship, Speak with Animals "
                            "3. Barkskin, Spike Growth "
                            "5. Plant Growth, Wind Wall "
                            "7. Dominate Beast, Grasping Vine "
                            "9. Insect Plague, Tree Stride")
           heavy_armor = 1
           cantrip6 = druid_cantrip();
           bonus_skill = randint(1,3)
           if bonus_skill == 1:
               animal_handling = 1
           if bonus_skill == 2:
               nature = 1
           if bonus_skill == 3:
               survival = 1

       if cleric_subclass == 10:
           PC_subclass = "Order Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Command, Heroism "
                            "3. Hold Person, Zone of Truth "
                            "5. Mass Healing Word, Slow "
                            "7. Compulsion, Locate Creature "
                            "9. Commune, Dominate Person")
           heavy_armor = 1
           bonus_skill = randint(1,2)
           if bonus_skill == 1:
               intimidation = 1
           if bonus_skill == 2:
               persuasion = 1
           class_feature5 = "Starting at 1st level, you can invoke the power of law to embolden an ally to attack. If you cast a spell with a spell slot of 1st level or higher and target an ally with the spell, that ally can use their reaction immediately after the spell to make one weapon attack against a creature of your choice that you can see.\n If the spell targets more than one ally, you choose the ally who can make the attack."

       if cleric_subclass == 11:
           PC_subclass = "Peace Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Heroism, Sanctuary "
                            "3. Aid, Warding Bond "
                            "5. Beacon of Hope, Sending "
                            "7. Aura of Purity, Otiluke's Resilient Sphere"
                            "9. Greater Restoration, Rary's Telepathic Bond")
           bonus_skill = randint(1,3)
           if bonus_skill == 1:
              insight = 1
           if bonus_skill == 2:
              performance = 1
           if bonus_skill == 3:
              persuasion = 1

           class_feature5 = "Starting at 1st level, you can forge an empowering bond among people who are at peace with one another. As an action, you choose a number of willing creatures within 30 feet of you (this can include yourself) equal to your proficiency bonus. You create a magical bond among them for 10 minutes or until you use this feature again. While any bonded creature is within 30 feet of another, the creature can roll a d4 and add the number rolled to an attack roll, an ability check, or a saving throw it makes. Each creature can add the d4 no more than once per turn.\nYou can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
    

       if cleric_subclass == 12:
           PC_subclass = "Tempest Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Fog Cloud, Thunderwave"
                            "3. Gust of Wind, Shatter"
                            "5. Call Lightning, Sleet Storm"
                            "7. Control Water, Ice Storm"
                            "9. Destructive Wave, Insect Plague")
           martial_weapons = 1
           heavy_armor = 1
           class_feature5 = "Also at 1st level, you can thunderously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one.\nYou can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."

       if cleric_subclass == 13:
           PC_subclass = "Trickery Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Charm Person, Disguise Self"
                            "3. Mirror Image, Pass without Trace"
                            "5. Blink, Dispel Magic"
                            "7. Dimension Door, Polymorph"
                            "9. Dominate Person, Modify Memory")

           class_feature5 = "Starting when you choose this domain at 1st level, you can use your action to touch a willing creature other than yourself to give it advantage on Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use this feature again."

       if cleric_subclass == 13:
           PC_subclass = "Twilight Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Faerie Fire, Sleep "
                            "3. Moonbeam, See Invisibility "
                            "5. Aura of Vitality, Leomund's Tiny Hut "
                            "7. Aura of Life, Greater Invisibility "
                            "9. Circle of Power, Mislead")
           martial_weapons = 1
           heavy_armor = 1
           class_feature5 = "Starting at 1st level, You can see through the deepest gloom. You have darkvision out to a range of 300 feet. In that radius, you can see in dim light as if it were bright light and in darkness as if it were dim light.\nAs an action, you can magically share the darkvision of this feature with willing creatures you can see within 10 feet of you, up to a number of creatures equal to your Wisdom modifier (minimum of one creature). The shared darkvision lasts for 1 hour. Once you share it, you can't do so again until you finish a long rest, unless you expend a spell slot of any level to share it again.\n the night has taught you to be vigilant. As an action, you give one creature you touch (including possibly yourself) advantage on the next initiative roll the creature makes. This benefit ends immediately after the roll or if you use this feature again."


       if cleric_subclass == 14:
           PC_subclass = "War Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Divine Favor, Shield of Faith "
                            "3. Magic Weapon, Spiritual Weapon "
                            "5. Crusader's Mantle, Spirit Guardians "
                            "7. Freedom of Movement, Stoneskin"
                            "9. Flame Strike, Hold Monster")
           martial_weapons = 1
           heavy_armor = 1
           class_feature5 = "From 1st level, your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.\nYou can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."


       if cleric_subclass == 15:
           PC_subclass = "Soldarity Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Bless, Guiding Bolt "
                            "3. Aid, Warding Bond "
                            "5. Beacon of Hope, Crusader's Mantle "
                            "7. Aura of Life, Guardian of Faith "
                            "9. Circle of Power, Mass Cure Wounds")
           heavy_armor = 1
           class_feature5 = "Also at 1st level, when you take the Help action to aid an ally’s attack, you can make one weapon attack as a bonus action. You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain expended uses when you finish a long rest."

       if cleric_subclass == 16:
           PC_subclass = "Strength Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Divine Favor, Shield of Faith "
                            "3. Enhance Ability, Protection from Poison "
                            "5. Haste, Protection from Energy "
                            "7. Dominate Beast, Stoneskin "
                            "9. Destructive Wave, Insect Plague")
           heavy_armor = 1
           cantrip6 = druid_cantrip();
           bonus_skill = randint(1,4)
           if bonus_skill == 1:
               animal_handling = 1
           if bonus_skill == 2:
               nature = 1
           if bonus_skill == 3:
               survival = 1
           if bonus_skill == 4:
               athletics = 1

       if cleric_subclass == 17:
           PC_subclass = "Ambition Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Bane, Disguise Self "
                            "3. Mirror Image, Ray of Enfeeblement "
                            "5. Bestow Curse, Vampiric Touch "
                            "7. Death Ward, Dimension Door "
                            "9. Dominate Person, Modify Memory")
           class_feature5 = "When you choose this domain at 1st level, you can interpose divine light between yourself and an attacking enemy. When you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses. An attacker that can’t be blinded is immune to this feature.\nYou can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."

       if cleric_subclass == 18:
           PC_subclass = "Zeal Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Searing Smite, Thunderous Smite "
                            "3. Magic Weapon, Shatter "
                            "5. Haste, Fireball "
                            "7. Fire Shield (warm shield only), Freedom of Movement "
                            "9. Destructive Wave, Flame Strike")
           martial_weapons = 1
           heavy_armor = 1
           class_feature5 = "From 1st level, Hazoret delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.\nYou can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."

       if cleric_subclass == 19:
           PC_subclass = "Blood Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Sleep, Ray of Sickness "
                            "3. Ray of Enfeeblement, Crown of Madness"
                            "5. Haste, Slow "
                            "7. Blight, Stoneskin"
                            "9. Dominate Person, Hold Monster")
           martial_weapons = 1
           class_feature5 = "From 1st level, your divine magics draw the blood from inflicted wounds, worsening the agony of your nearby foes. When you use a spell of 1st level or higher to inflict damage to any creatures that have blood, those creatures suffer additional necrotic damage equal to 2 + the spell’s level."

       if cleric_subclass == 20:
           PC_subclass = "Mind Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Command, Dissonant Whispers "
                            "3. Detect Thoughts, Phantasmal Force "
                            "5. Enemies Abound, Fear "
                            "7. Confusion, Phantasmal Killer "
                            "9. Dominate Person, Telekinesis")
           class_feature5 = "Starting at 1st level, you can summon power from a well of mental energy at your core. When you make an ability check, you can choose to reroll it after you see the result, but before you know if it succeeds or fails. You get a bonus to this reroll equal to half of your cleric level (minimum of 1).\nYou can use this feature twice. You regain expended uses when you finish a short or long rest.\nAlso at 1st level, you learn to buffet your foes with mental power. When you cast a cleric spell or cantrip that inflicts radiant damage, you can choose to have it inflict psychic damage instead."

       if cleric_subclass == 21:
           PC_subclass = "Beauty Domain"
           class_feature4 = ("Your domain gives you the following spells at certian levels, independent of your known spell list:\n" 
                            "1. Charm Person, Heroism "
                            "3. Enthrall, Suggestion "
                            "5. Beacon of Hope, Hypnotic Pattern "
                            "7. Charm Monster, Compulsion "
                            "9. Dominate Person, Hold Monster")

           class_feature5 = "Starting at 1st level, your mere presence is enough to inspire hope and determination in others. When you complete a short or long rest, up to 12 allies of your choice gain temporary hit points equal to your Charisma modifier (minimum 1).\nWhen you select this domain at 1st level, you gain the ability to rebuke those who lash out at you in violence. As a reaction when a creature you can see within 30 feet of you inflicts damage, you force that creature to make a Wisdom save. On a failed saving throw, it takes psychic damage equal to the damage dealt. On a successful save, it takes half that damage.\nIf the creature made multiple attacks, select one attack to determine the damage dealt. If the creature used one or more effects that damaged multiple targets, choose the damage take by one of those targets from one of the effects.\nOnce you use this feature, you can't use it again until you complete a short or long rest."

       level_1_spell1 = cleric_level_1();
       if cleric_subclass == 1:
           level_1_spell1 = cleric_arcana_level_1();

       if cleric_subclass == 4:
           level_1_spell1 = cleric_grave_level_1();

       if cleric_subclass == 5:
           level_1_spell1 = cleric_knowledge_level_1();

       if cleric_subclass == 6:
           level_1_spell1 = cleric_life_level_1();

       if cleric_subclass == 10:
           level_1_spell1 = cleric_order_level_1();

       if cleric_subclass == 11:
           level_1_spell1 = cleric_peace_level_1();

       if cleric_subclass == 14:
           level_1_spell1 = cleric_war_level_1();

       if cleric_subclass == 15:
           level_1_spell1 = cleric_solidarity_level_1();

       if cleric_subclass == 16:
           level_1_spell1 = cleric_strength_level_1();

       if cleric_subclass == 17:
           level_1_spell1 = cleric_ambition_level_1();
           
       if cleric_subclass == 20:
           level_1_spell1 = cleric_mind_level_1();


       level_1_spell2 = cleric_level_1();
       if cleric_subclass == 1:
           level_1_spell2 = cleric_arcana_level_1();

       if cleric_subclass == 4:
           level_1_spell2 = cleric_grave_level_1();

       if cleric_subclass == 5:
           level_1_spell2 = cleric_knowledge_level_1();

       if cleric_subclass == 6:
           level_1_spell2 = cleric_life_level_1();

       if cleric_subclass == 10:
           level_1_spell2 = cleric_order_level_1();

       if cleric_subclass == 11:
           level_1_spell2 = cleric_peace_level_1();

       if cleric_subclass == 14:
           level_1_spell2 = cleric_war_level_1();

       if cleric_subclass == 15:
           level_1_spell2 = cleric_solidarity_level_1();

       if cleric_subclass == 16:
           level_1_spell2 = cleric_strength_level_1();

       if cleric_subclass == 17:
           level_1_spell2 = cleric_ambition_level_1();
           
       if cleric_subclass == 20:
           level_1_spell2 = cleric_mind_level_1();

       while level_1_spell1 == level_1_spell2:

           level_1_spell2 = cleric_level_1();
           if cleric_subclass == 1:
                level_1_spell2 = cleric_arcana_level_1();

           if cleric_subclass == 4:
               level_1_spell2 = cleric_grave_level_1();

           if cleric_subclass == 5:
               level_1_spell2 = cleric_knowledge_level_1();

           if cleric_subclass == 6:
               level_1_spell2 = cleric_life_level_1();

           if cleric_subclass == 10:
               level_1_spell2 = cleric_order_level_1();

           if cleric_subclass == 11:
               level_1_spell2 = cleric_peace_level_1();

           if cleric_subclass == 14:
               level_1_spell2 = cleric_war_level_1();

           if cleric_subclass == 15:
               level_1_spell2 = cleric_solidarity_level_1();

           if cleric_subclass == 16:
               level_1_spell2 = cleric_strength_level_1();

           if cleric_subclass == 17:
               level_1_spell2 = cleric_ambition_level_1();
           
           if cleric_subclass == 20:
               level_1_spell2 = cleric_mind_level_1();




       cantrip1 = cleric_cantrip();
       cantrip2 = cleric_cantrip();
       while cleric_subclass == 4 and cantrip1 == "Spare the Dying":
            cantrip1 = cleric_cantrip();
       while cantrip1 == cantrip2:
           cantrip2 = cleric_cantrip();
       while cleric_subclass == 4 and cantrip2 == "Spare the Dying":
            cantrip2 = cleric_cantrip();
       cantrip3 = cleric_cantrip();
       while cantrip1 == cantrip3 or cantrip2 == cantrip3 or (cleric_subclass == 4 and cantrip3 == "Spare the Dying"):
           cantrip3 = cleric_cantrip();

       if cleric_subclass == 7 and cantrip1 != "Light" and cantrip2 != "Light" and cantrip3 != "Light":
           cantrip6 = "Light"



       class_feature1 = ("As a conduit for divine power, you can cast cleric spells. Wisdom is your spellcasting ability for your cleric spells\n"
                         "The power of your spells comes from your devotion to your deity. You use your Wisdom whenever a cleric spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.\n"
                         "Spell save DC = 8 + your proficiency bonus + your Wisdom modifier. Spell attack modifier = your proficiency bonus + your Wisdom modifier. You can use a holy symbol as a spellcasting focus for your cleric spells.")
       class_feature2 = ("Your spellcasting chart is shown below"
     "                                                       Slot Types\n"
           "Level     Cantrips Known        1st     2nd     3rd     4th     5th     6th     7th     8th     9th\n"
           "  1             3                2\n"
           "  2             3                3\n"
           "  3             3                4       2\n"
           "  4             4                4       3\n"
           "  5             4                4       3       2\n"
           "  6             4                4       3       3\n"
           "  7             4                4       3       3       1\n"
           "  8             4                4       3       3       2\n"
           "  9             4                4       3       3       3       1\n"
           "  10            5                4       3       3       3       2\n"
           "  11            5                4       3       3       3       2       1\n"
           "  12            5                4       3       3       3       2       1\n"
           "  13            5                4       3       3       3       2       1       1\n"
           "  14            5                4       3       3       3       2       1       1\n"
           "  15            5                4       3       3       3       2       1       1       1\n"
           "  16            5                4       3       3       3       2       1       1       1\n"
           "  17            5                4       3       3       3       2       1       1       1       1\n"
           "  18            5                4       3       3       3       3       1       1       1       1\n"
           "  19            5                4       3       3       3       3       2       1       1       1\n"
           "  20            5                4       3       3       3       3       2       2       1       1\n")

       class_feature3 = "At 1st level, you choose a domain shaped by your choice of Deity and the gifts they grant you. Your choice grants you domain spells and other features when you choose it at 1st level. It also grants you additional ways to use Channel Divinity when you gain that feature at 2nd level, and additional benefits at 6th, 8th, and 17th levels.\n Each domain has a list of spells-its domain spells that you gain at the cleric levels noted in the domain description. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.\n"
       
       if PC_level >= 2:
       
           class_feature6 = ("At 2nd level, you gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.\n"
                        "When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC.\n"
                        "Turn Undead: As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.\nA turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action."
                        "Harness Divine Power: At 2nd level, you can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 2nd level, once; 6th level, twice; and 18th level, thrice. You regain all expended uses when you finish a long rest. "
                        )
           level_1_spell3 = cleric_level_1();
           if cleric_subclass == 1:
             level_1_spell3 = cleric_arcana_level_1();

           if cleric_subclass == 4:
               level_1_spell3 = cleric_grave_level_1();

           if cleric_subclass == 5:
               level_1_spell3 = cleric_knowledge_level_1();

           if cleric_subclass == 6:
               level_1_spell3 = cleric_life_level_1();

           if cleric_subclass == 10:
               level_1_spell3 = cleric_order_level_1();

           if cleric_subclass == 11:
               level_1_spell3 = cleric_peace_level_1();

           if cleric_subclass == 14:
               level_1_spell3 = cleric_war_level_1();

           if cleric_subclass == 15:
               level_1_spell3 = cleric_solidarity_level_1();

           if cleric_subclass == 16:
               level_1_spell3 = cleric_strength_level_1();

           if cleric_subclass == 17:
               level_1_spell3 = cleric_ambition_level_1();
           
           if cleric_subclass == 20:
               level_1_spell3 = cleric_mind_level_1();

           while level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1:

               level_1_spell3 = cleric_level_1();
               if cleric_subclass == 1:
                    level_1_spell3 = cleric_arcana_level_1();

               if cleric_subclass == 4:
                   level_1_spell3 = cleric_grave_level_1();

               if cleric_subclass == 5:
                   level_1_spell3 = cleric_knowledge_level_1();

               if cleric_subclass == 6:
                   level_1_spell3 = cleric_life_level_1();

               if cleric_subclass == 10:
                   level_1_spell3 = cleric_order_level_1();

               if cleric_subclass == 11:
                   level_1_spell3 = cleric_peace_level_1();

               if cleric_subclass == 14:
                   level_1_spell3 = cleric_war_level_1();

               if cleric_subclass == 15:
                   level_1_spell3 = cleric_solidarity_level_1();

               if cleric_subclass == 16:
                   level_1_spell3 = cleric_strength_level_1();

               if cleric_subclass == 17:
                   level_1_spell3 = cleric_ambition_level_1();
           
               if cleric_subclass == 20:
                   level_1_spell3 = cleric_mind_level_1();

           if cleric_subclass == 1:
               PC_subclass = "Arcana Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to abjure otherworldly creatures. \n"
                                 "As an action, you present your holy symbol, and one celestial, elemental, fey, or fiend of your choice that is within 30 feet of you must make a Wisdom saving throw, provided that the creature can see or hear you. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.\n"
                                 "A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly end its move in a space within 30 feet of you. It also can't take reactions. For its action, it can only use the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.\n"
                                 "After you reach 5th level, when a creature fails its saving throw against your Arcane Abjuration feature, the creature is banished for 1 minute (as in the Banishment spell, no concentration required) if it isn't on its plane of origin and its challenge rating is at or below a certain threshold, as shown on the Arcane Banishment table.\n"
                                 "  5th level: 1/2 or lower\n   8th level: 1 or lower\n   11th level: 2 or lower\n   14th level: 3 or lower\n   17th level: 4 or lower\n")

           if cleric_subclass == 2:
               PC_subclass = "Death Domain"
               class_feature7 = ("Starting at 2nd level, you can use Channel Divinity to destroy another creature's life force by touch. When you hit a creature with a melee attack, you can use Channel Divinity to deal extra necrotic damage to the target. The damage equals 5 + twice your cleric level.")
         
           if cleric_subclass == 3:
               PC_subclass = "Forge Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to create simple items. You conduct an hour-long ritual that crafts a nonmagical item that must include some metal: a simple or martial weapon, a suit of armor, ten pieces of ammunition, a set of tools, or another metal object. The creation is completed at the end of the hour, coalescing in an unoccupied space of your choice on a surface within 5 feet of you.\nThe thing you create can be something that is worth no more than 100 gp. As part of this ritual, you must lay out metal, which can include coins, with a value equal to the creation. The metal irretrievably coalesces and transforms into the creation at the ritual’s end, magically forming even nonmetal parts of the creation.\nThe ritual can create a duplicate of a nonmagical item that contains metal, such as a key, if you possess the original during the ritual.")
           
           if cleric_subclass == 4:
               PC_subclass = "Grave Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to mark another creature’s life force for termination. As an action, you choose one creature you can see within 30 feet of you, cursing it until the end of your next turn. The next time you or an ally of yours hits the cursed creature with an attack, the creature has vulnerability to all of that attack's damage, and then the curse ends.")
          
           if cleric_subclass == 5:
               PC_subclass = "Knowledge Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to tap into a divine well of knowledge. As an action, you choose one skill or tool. For 10 minutes, you have proficiency with the chosen skill or tool.")
           
           if cleric_subclass == 6:
               PC_subclass = "Life Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to heal the badly injured. As an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct.")
         
           if cleric_subclass == 7:
               PC_subclass = "Light Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to harness sunlight, banishing darkness and dealing radiant damage to your foes. As an action, you present your holy symbol, and any magical darkness within 30 feet of you is dispelled. Additionally, each hostile creature within 30 feet of you must make a Constitution saving throw. A creature takes radiant damage equal to 2d10 + your cleric level on a failed saving throw, and half as much damage on a successful one. A creature that has total cover from you is not affected. ")
           
           if cleric_subclass == 9:
               PC_subclass = "Nature Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to charm animals and plants. As an action, you present your holy symbol and invoke the name of your deity. Each beast or plant creature that can see you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is charmed by you for 1 minute or until it takes damage. While it is charmed by you, it is friendly to you and other creatures you designate.")
          
           if cleric_subclass == 10:
               PC_subclass = "Order Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to exert an intimidating presence over others. As an action, you present your holy symbol, and each creature of your choice that can see or hear you within 30 feet of you must succeed on a Wisdom saving throw or be charmed by you until the end of your next turn or until the charmed creature takes any damage. You can also cause any of the charmed creatures to drop what they are holding when they fail the saving throw.")
          
           if cleric_subclass == 11:
               PC_subclass = "Peace Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to make your very presence a soothing balm. As an action, you can move up to your speed, without provoking opportunity attacks, and when you move within 5 feet of any other creature during this action, you can restore a number of hit points to that creature equal to 2d6 + your Wisdom modifier (minimum of 1 hit point). A creature can receive this healing only once whenever you take this action.")
          
           if cleric_subclass == 12:
               PC_subclass = "Tempest Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to wield the power of the storm with unchecked ferocity. When you roll lightning or thunder damage, you can use your Channel Divinity to deal maximum damage, instead of rolling. ")
           
           if cleric_subclass == 13:
               PC_subclass = "Trickery Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to create an illusory duplicate of yourself. As an action, you create a perfect illusion of yourself that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The illusion appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the illusion up to 30 feet to a space you can see, but it must remain within 120 feet of you.\n For the duration, you can cast spells as though you were in the illusion's space, but you must use your own senses. Additionally, when both you and your illusion are within 5 feet of a creature that can see the illusion, you have advantage on attack rolls against that creature, given how distracting the illusion is to the target.")

           if cleric_subclass == 13:
               PC_subclass = "Twilight Domain"
               class_feature7 = ("At 2nd level, you can use your Channel Divinity to refresh your allies with soothing twilight. As an action, you present your holy symbol, and a sphere of twilight emanates from you. The sphere is centered on you, has a 30-foot radius, and is filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature (including you) ends its turn in the sphere, you can grant that creature one of these benefits: You grant it temporary hit points equal to 1d6 plus your cleric level or You end one effect on it causing it to be charmed or frightened.")
          
           if cleric_subclass == 14:
               PC_subclass = "War Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
          
           if cleric_subclass == 15:
               PC_subclass = "Soldarity Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to heal the badly injured. As an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can’t use this feature on an undead or a construct.")
           
           if cleric_subclass == 16:
               PC_subclass = "Strength Domain"
               class_feature7 = ("At 2nd level, you can use your Channel Divinity to enhance your physical might. When you make an attack roll, ability check, or saving throw using Strength, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the roll succeeds or fails.")
           
           if cleric_subclass == 17:
               PC_subclass = "Ambition Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to create an illusory duplicate of yourself. As an action, you create a perfect illusion of yourself that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The illusion appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the illusion up to 30 feet to a space you can see, but it must remain within 120 feet of you.\nFor the duration, you can cast spells as though you were in the illusion’s space, but you must use your own senses. Additionally, when both you and your illusion are within 5 feet of a creature that can see the illusion, you have advantage on attack rolls against that creature, given how distracting the illusion is to the target.")
          
           if cleric_subclass == 18:
               PC_subclass = "Zeal Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to channel your zeal into unchecked ferocity. When you roll fire or thunder damage, you can use your Channel Divinity to deal maximum damage instead of rolling. ")
          
           if cleric_subclass == 19:
               PC_subclass = "Blood Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to briefly control a creature’s actions against their will. As an action, you target a Large or smaller creature that has blood within 60 feet of you. That creature must succeed on a Constitution saving throw against your spell save DC or immediately move up to half of their movement in any direction of your choice and make a single weapon attack against a creature of your choice within range. Dead or unconscious creatures automatically fail their saving throw. At 8th level, you can target a Huge or smaller creature.")
           
           if cleric_subclass == 20:
               PC_subclass = "Mind Domain"
               class_feature7 = ("Beginning at 2nd level, you can use your Channel Divinity to disrupt a foe’s mind. When a creature within 30 feet of you has to make a Wisdom saving throw, you can use your reaction to impose disadvantage on it using your Channel Divinity. You must use this feature before you know the outcome of the roll. If the spell or effect that caused the Wisdom saving throw is not created by a spell you cast, you can also choose to deal psychic damage to the target, equal to half your cleric level, immediately before the target makes its saving throw. ")
           
           if cleric_subclass == 21:
               PC_subclass = "Beauty Domain"
               class_feature7 = ("Starting at 2nd level, you can use your Channel Divinity to quell the flame of violence. As an action, you force all creatures within 100 feet of you to make Charisma saving throws. Each creature that fails this save is charmed by every other creature that also failed the saving throw. This benefit lasts for one hour. While charmed by this ability, creatures consider all other creatures charmed by it to be their allies. They fight to defend them from attackers. While this ability persists, absent any threat, creatures charmed by it will rest, talk among themselves, share stories of their lives, create a communal feast using food and drink they carry, and generally act as if they are old friends, long separated and brought together again for a joyous reunion.")

       if PC_level >= 3:

           level_1_spell4 = cleric_level_1();
           if cleric_subclass == 1:
             level_1_spell4 = cleric_arcana_level_1();

           if cleric_subclass == 4:
               level_1_spell4 = cleric_grave_level_1();

           if cleric_subclass == 5:
               level_1_spell4 = cleric_knowledge_level_1();

           if cleric_subclass == 6:
               level_1_spell4 = cleric_life_level_1();

           if cleric_subclass == 10:
               level_1_spell4 = cleric_order_level_1();

           if cleric_subclass == 11:
               level_1_spell4 = cleric_peace_level_1();

           if cleric_subclass == 14:
               level_1_spell4 = cleric_war_level_1();

           if cleric_subclass == 15:
               level_1_spell4 = cleric_solidarity_level_1();

           if cleric_subclass == 16:
               level_1_spell4 = cleric_strength_level_1();

           if cleric_subclass == 17:
               level_1_spell4 = cleric_ambition_level_1();
           
           if cleric_subclass == 20:
               level_1_spell4 = cleric_mind_level_1();

           while level_1_spell4 == level_1_spell2 or level_1_spell4 == level_1_spell1 or level_1_spell4 == level_1_spell3:

               level_1_spell4 = cleric_level_1();
               if cleric_subclass == 1:
                    level_1_spell4 = cleric_arcana_level_1();

               if cleric_subclass == 4:
                   level_1_spell4 = cleric_grave_level_1();

               if cleric_subclass == 5:
                   level_1_spell4 = cleric_knowledge_level_1();

               if cleric_subclass == 6:
                   level_1_spell4 = cleric_life_level_1();

               if cleric_subclass == 10:
                   level_1_spell4 = cleric_order_level_1();

               if cleric_subclass == 11:
                   level_1_spell4 = cleric_peace_level_1();

               if cleric_subclass == 14:
                   level_1_spell4 = cleric_war_level_1();

               if cleric_subclass == 15:
                   level_1_spell4 = cleric_solidarity_level_1();

               if cleric_subclass == 16:
                   level_1_spell4 = cleric_strength_level_1();

               if cleric_subclass == 17:
                   level_1_spell4 = cleric_ambition_level_1();
           
               if cleric_subclass == 20:
                   level_1_spell4 = cleric_mind_level_1();
           
           level_2_spell1 = cleric_level_2();
           level_2_spell2 = cleric_level_2();

           while level_2_spell1 == level_2_spell2:
               level_2_spell2 = cleric_level_2();
       
       if PC_level >= 4:
           
           feat1 = ability_score_improvement();
           cantrip4 = cleric_cantrip();

           while cantrip4 == cantrip3 or cantrip4 == cantrip2 or cantrip4 == cantrip1:
               cantrip4 = cleric_cantrip();

           level_2_spell3 = cleric_level_2();

           while level_2_spell1 == level_2_spell3 or level_2_spell2 == level_2_spell3:
               level_2_spell3 = cleric_level_2();

           class_feature8 = "Whenever you reach a level in this class that grants the Ability Score Improvement feature (4,8,12,16,19), you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the cleric spell list."

       if PC_level >= 5:

           PC_prof_bonus = 3
           level_3_spell1 = cleric_level_3();
           level_3_spell2 = cleric_level_3();

           while  level_3_spell1 ==  level_3_spell2:
               level_3_spell2 = cleric_level_3();

           class_feature9 = "Starting at 5th level, when an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown in the table:\n Level 5: Cr 1/2\n Level 8: Cr 1\n Level 11: Cr 2\n Level 14: Cr 3\n Level 17: Cr 4"
           
       if PC_level >= 6:

           level_3_spell3 = cleric_level_3();

           while level_3_spell1 == level_3_spell3 or level_3_spell2 == level_3_spell3:
               level_3_spell3 = cleric_level_3();

           if cleric_subclass == 1:
               PC_subclass = "Arcana Domain"
               class_feature10 = ("Starting at 6th level, when you restore hit points to an ally with a spell of 1st level or higher, you can also end one spell of your choice on that creature. The level of the spell you end must be equal to or lower than the level of the spell slot you use to cast the healing spell.")

           if cleric_subclass == 2:
               PC_subclass = "Death Domain"
               class_feature10 = ("Starting at 6th level, your ability to channel negative energy becomes more potent. Necrotic damage dealt by your cleric spells and Channel Divinity options ignores resistance to necrotic damage.")

           if cleric_subclass == 3:
               PC_subclass = "Forge Domain"
               class_feature10 = ("Starting at 6th level, your mastery of the forge grants you special abilities: You gain resistance to fire damage and while wearing heavy armor, you gain a +1 bonus to AC.")
           
           if cleric_subclass == 4:
               PC_subclass = "Grave Domain"
               class_feature10 = ("At 6th level, you gain the ability to impede death’s progress. As a reaction when you or an ally that you can see within 30 feet of you suffers a critical hit, you can turn that attack into a normal hit. Any effects triggered by a critical hit are canceled. You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a long rest.")
          
           if cleric_subclass == 5:
               PC_subclass = "Knowledge Domain"
               class_feature10 = ("At 6th level, you can use your Channel Divinity to read a creature's thoughts. You can then use your access to the creature's mind to command it. As an action, choose one creature that you can see within 60 feet of you. That creature must make a Wisdom saving throw. If the creature succeeds on the saving throw, you can't use this feature on it again until you finish a long rest.\n"
                                 "If the creature fails its save, you can read its surface thoughts (those foremost in its mind, reflecting its current emotions and what it is actively thinking about) when it is within 60 feet of you. This effect lasts for 1 minute. During that time, you can use your action to end this effect and cast the Suggestion spell on the creature without expending a spell slot. The target automatically fails its saving throw against the spell.")

           if cleric_subclass == 6:
               PC_subclass = "Life Domain"
               class_feature10 = ("Beginning at 6th level, the healing spells you cast on others heal you as well. When you cast a spell of 1st level or higher that restores hit points to a creature other than you, you regain hit points equal to 2 + the spell's level.")
         
           if cleric_subclass == 7:
               PC_subclass = "Light Domain"
               class_feature10 = ("Starting at 6th level, you can also use your Warding Flare feature when a creature that you can see within 30 feet of you attacks a creature other than you.")

           if cleric_subclass == 9:
               PC_subclass = "Nature Domain"
               class_feature10 = ("Starting at 6th level, when you or a creature within 30 feet of you takes acid, cold, fire, lightning, or thunder damage, you can use your reaction to grant resistance to the creature against that instance of the damage.")
          
           if cleric_subclass == 10:
               PC_subclass = "Order Domain"
               class_feature10 = ("At 6th level, you become remarkably adept at channeling magical energy to compel others. If you cast a spell of the enchantment school using a spell slot of 1st level or higher, you can change the spell's casting time to 1 bonus action for this casting, provided the spell's casting time is normally 1 action. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.")

           if cleric_subclass == 11:
               PC_subclass = "Peace Domain"
               class_feature10 = ("Beginning at 6th level, the bond you forge between people helps them protect each other. When a creature affected by your Emboldening Bond feature is about to take damage, a second bonded creature within 30 feet of the first can use its reaction to teleport to an unoccupied space within 5 feet of the first creature. The second creature then takes all the damage instead.")
          
           if cleric_subclass == 12:
               PC_subclass = "Tempest Domain"
               class_feature10 = ("At 6th level, when you deal lightning damage to a Large or smaller creature, you can also push it up to 10 feet away from you.")
           
           if cleric_subclass == 13:
               PC_subclass = "Trickery Domain"
               class_feature10 = ("Starting at 6th level, you can use your Channel Divinity to vanish. As an action, you become invisible until the end of your next turn. You become visible if you attack or cast a spell.")

           if cleric_subclass == 13:
               PC_subclass = "Twilight Domain"
               class_feature10 = ("Starting at 6th level, you can draw on the mystical power of night to rise into the air. As a bonus action when you are in dim light or darkness, you can magically give yourself a flying speed equal to your walking speed for 1 minute. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")

           if cleric_subclass == 14:
               PC_subclass = "War Domain"
               class_feature10 = ("At 6th level, when a creature within 30 feet of you makes an attack roll, you can use your reaction to grant that creature a +10 bonus to the roll, using your Channel Divinity. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")

           if cleric_subclass == 15:
               PC_subclass = "Soldarity Domain"
               class_feature10 = ("At 6th level, when a creature within 30 feet of you makes an attack roll, you can use your reaction to grant that creature a +10 bonus to the roll, using your Channel Divinity. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
           
           if cleric_subclass == 16:
               PC_subclass = "Strength Domain"
               class_feature10 = ("At 6th level, when a creature within 30 feet of you makes an attack roll, ability check, or saving throw using Strength, you can use your reaction to grant that creature a +10 bonus to the roll, using your Channel Divinity. You make this choice after you see the roll, but before the DM says whether the roll succeeds or fail.")
           
           if cleric_subclass == 17:
               PC_subclass = "Ambition Domain"
               class_feature10 = ("Starting at 6th level, you can use your Channel Divinity to vanish. As an action, you become invisible until the end of your next turn. You become visible if you attack or cast a spell.")
          
           if cleric_subclass == 18:
               PC_subclass = "Zeal Domain"
               class_feature10 = ("At 6th level, when you deal thunder damage to a Large or smaller creature, you can also push it up to 10 feet away from you.")
          
           if cleric_subclass == 19:
               PC_subclass = "Blood Domain"
               class_feature10 = ("Starting at 6th level, you can use your Channel Divinity to focus on a sample of blood from a creature that is at least 2 ounces, and that has been spilt no longer than a week ago.\n"
                                 "As an action, you can focus on the blood of the creature to form a bond and gain information about their current circumstances. You know their approximate distance and direction from you, as well as their general state of health, as long as they are within 10 miles of you. You can maintain this effect as though you were concentrating on a spell for up to 1 hour.\n"
                                 "During your bond, you can spend an action to attempt to connect with the bonded creature’s senses. The target makes a Constitution saving throw against your spell save DC. If they succeed, the connection is resisted, ending the bond. You suffer 2d6 necrotic damage. Upon a failed saving throw, you can choose to either see through the eyes of or hear through their ears of the target for a number of rounds equal to your Wisdom modifier (minimum of 1). During this time, you are blind or deaf (respectively) with regard to your own senses. Once this connection ends, the Crimson Bond is lost ")

           if cleric_subclass == 20:
               PC_subclass = "Mind Domain"
               class_feature10 = ("Beginning at 6th level, your mental power increases, settling the minds of those around you with your mere presence. Whenever you or a friendly creature within 10 feet of you must make an Intelligence, Wisdom, or Charisma saving throw, the creature gains a +2 bonus to the saving throw. You must be conscious to grant this bonus.")

           if cleric_subclass == 21:
               PC_subclass = "Beauty Domain"
               class_feature10 = ("Starting at 6th level, the temporary hit points granted by your Beauty's Refuge ability increase to 5 + your Charisma modifier (minimum 1).")

       if PC_level >= 7:

           level_4_spell1 = cleric_level_4();

       if PC_level >= 8:
           feat2 = ability_score_improvement();
           level_4_spell2 = cleric_level_4();

           while  level_4_spell1 ==  level_4_spell2:
               level_4_spell2 = cleric_level_4();
           
           if cleric_subclass == 1:
               PC_subclass = "Arcana Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

           if cleric_subclass == 2:
               PC_subclass = "Death Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with necrotic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an a 1d8 necrotic damage to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 3:
               PC_subclass = "Forge Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with the fiery power of the forge. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 fire damage to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 4:
               PC_subclass = "Grave Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

           if cleric_subclass == 5:
               PC_subclass = "Knowledge Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

           if cleric_subclass == 6:
               PC_subclass = "Life Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 7:
               PC_subclass = "Light Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

           if cleric_subclass == 9:
               PC_subclass = "Nature Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 cold, fire, or lightning damage (your choice) to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 10:
               PC_subclass = "Order Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 psychic damage to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 11:
               PC_subclass = "Peace Domain"
               class_feature11 = ("At 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

           if cleric_subclass == 12:
               PC_subclass = "Tempest Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 thunder damage to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 13:
               PC_subclass = "Trickery Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with poison – a gift from your deity. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 poison damage to the target. When you reach 14th level, the extra damage increases to 2d8.")
         
           if cleric_subclass == 13:
               PC_subclass = "Twilight Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 psychic damage. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 14:
               PC_subclass = "War Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.")
          
           if cleric_subclass == 15:
               PC_subclass = "Soldarity Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 16:
               PC_subclass = "Strength Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 17:
               PC_subclass = "Ambition Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")
          
           if cleric_subclass == 18:
               PC_subclass = "Zeal Domain"
               class_feature11 = ("At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.")

           if cleric_subclass == 19:
               PC_subclass = "Blood Domain"
               class_feature11 = ("At 8th level, you can sacrifice a portion of your own vitality to recover expended spell slots. As an action, you recover spell slots that have a combined level equal to or less than half of your cleric level (rounded up), and none of the slots can be 6th level or higher. You immediately suffer 1d6 necrotic damage per spell slot level recovered. You can’t use this feature again until you finish a long rest.\n For example, if you are an 8th-level cleric, you can recover up to four levels of spell slots. You can recover a single 4th-level spell slot, two 2nd-level spell slots, a 3rd-level spell slot and a 1st level spell slot, or four 1st-level spell slots. You then suffer 4d6 damage.")

           if cleric_subclass == 20:
               PC_subclass = "Mind Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

           if cleric_subclass == 21:
               PC_subclass = "Beauty Domain"
               class_feature11 = ("Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip.")

       if PC_level >= 9:
           PC_prof_bonus = 4

           level_4_spell3 = cleric_level_4();

           while level_4_spell1 == level_4_spell3 or level_4_spell2 == level_4_spell3:
               level_4_spell3 = cleric_level_4();

           level_5_spell1 = cleric_level_5();

       if PC_level >= 10:

           class_feature12 = "Beginning at 10th level, you can call on your deity to intervene on your behalf when your need is great. Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest. At 20th level, your call for intervention succeeds automatically, no roll required."

           cantrip5 = cleric_cantrip();
           while cantrip5 == cantrip4 or cantrip5 == cantrip3 or  cantrip5 == cantrip2 or  cantrip5 == cantrip1:
              cantrip5 = cleric_cantrip();

           level_5_spell2 = cleric_level_5();
           while level_5_spell2 == level_5_spell1:
               level_5_spell2 = cleric_level_5();

       if PC_level >= 11:
          level_6_spell1 = cleric_level_6();

       if PC_level >= 12:
           feat3 = ability_score_improvement();

       if PC_level >= 13:
           PC_prof_bonus = 5
           level_7_spell1 = cleric_level_7();

       #Nothing new for 14

       if PC_level >= 15:
           level_8_spell1 = cleric_level_8();

       if PC_level >= 16:
           feat4 = ability_score_improvement();

       if PC_level >= 17:
           level_9_spell1 = cleric_level_9();
           PC_prof_bonus = 6
           if cleric_subclass == 1:
               PC_subclass = "Arcana Domain"
               class_feature13 = ("At 17th level, you choose four spells from the wizard spell list, one from each of the following levels: 6th, 7th, 8th, and 9th. You add them to your list of domain spells. Like your other domain spells, they are always prepared and count as cleric spells for you.")
         
           if cleric_subclass == 2:
               PC_subclass = "Death Domain"
               class_feature13 = ("Starting at 17th level, when you cast a necromancy spell of 1st through 5th level that targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other. If the spell consumes its material components, you must provide them for each target.")

           if cleric_subclass == 3:
               PC_subclass = "Forge Domain"
               class_feature13 = ("At 17th level, your blessed affinity with fire and metal becomes more powerful: You gain immunity to fire damage and while wearing heavy armor, you have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.")

           if cleric_subclass == 4:
               PC_subclass = "Grave Domain"
               class_feature13 = ("At 17th level, you can seize a trace of vitality from a parting soul and use it to heal the living. When an enemy you can see dies within 30 feet of you, you or one ally of your choice that is within 30 feet of you regains hit points equal to the enemy’s number of Hit Dice. You can use this feature only if you aren't incapacitated. Once you use it, you can't do so again until the start of your next turn.")

           if cleric_subclass == 5:
               PC_subclass = "Knowledge Domain"
               class_feature13 = ("Starting at 17th level, you can call up visions of the past that relate to an object you hold or your immediate surroundings. You spend at least 1 minute in meditation and prayer, then receive dreamlike, shadowy glimpses of recent events. You can meditate in this way for a number of minutes equal to your Wisdom score and must maintain concentration during that time, as if you were casting a spell. Once you use this feature, you can't use it again until you finish a short or long rest.\n"
                                  "Object Reading: Holding an object as you meditate, you can see visions of the object's previous owner. After meditating for 1 minute, you learn how the owner acquired and lost the object, as well as the most recent significant event involving the object and that owner. If the object was owned by another creature in the recent past (within a number of days equal to your Wisdom score), you can spend 1 additional minute for each owner to learn the same information about that creature.\n"
                                  "Area Reading: As you meditate, you see visions of recent events in your immediate vicinity (a room, street, tunnel, clearing, or the like, up to a 50-foot cube), going back a number of days equal to your Wisdom score. For each minute you meditate, you learn about one significant event, beginning with the most recent. Significant events typically involve powerful emotions, such as battles and betrayals, marriages and murders, births and funerals. However, they might also include more mundane events that are nevertheless important in your current situation.")

           if cleric_subclass == 6:
               PC_subclass = "Life Domain"
               class_feature13 = ("Starting at 17th level, when you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die. For example, instead of restoring 2d6 hit points to a creature, you restore 12.")

           if cleric_subclass == 7:
               PC_subclass = "Light Domain"
               class_feature13 = ("Starting at 17th level, you can use your action to activate an aura of sunlight that lasts for 1 minute or until you dismiss it using another action. You emit bright light in a 60-foot radius and dim light 30 feet beyond that. Your enemies in the bright light have disadvantage on saving throws against any spell that deals fire or radiant damage.")

           if cleric_subclass == 9:
               PC_subclass = "Nature Domain"
               class_feature13 = ("At 17th level, you gain the ability to command animals and plant creatures. While creatures are charmed by your Charm Animals and Plants feature, you can take a bonus action on your turn to verbally command what each of those creatures will do on its next turn.")

           if cleric_subclass == 10:
               PC_subclass = "Order Domain"
               class_feature13 = ("Starting at 17th level, enemies you designate for destruction wilt under the combined efforts of you and your allies. If you deal your Divine Strike damage to a creature on your turn, you can curse that creature until the start of your next turn. The next time one of your allies hits the cursed creature with an attack, the target also takes 2d8 psychic damage, and the curse ends. You can curse a creature in this way only once per turn.")

           if cleric_subclass == 11:
               PC_subclass = "Peace Domain"
               class_feature13 = ("At 17th level, the benefits of your Emboldening Bond and Protective Bond features now work when the creatures are within 60 feet of each other. Moreover, when a creature uses Protective Bond to take someone else's damage, the creature has resistance to that damage.")

           if cleric_subclass == 12:
               PC_subclass = "Tempest Domain"
               class_feature13 = ("At 17th level, you have a flying speed equal to your current walking speed whenever you are not underground or indoors.")

           if cleric_subclass == 13:
               PC_subclass = "Trickery Domain"
               class_feature13 = ("At 17th level, you can create up to four duplicates of yourself, instead of one, when you use Invoke Duplicity. As a bonus action on your turn, you can move any number of them up to 30 feet, to a maximum range of 120 feet.")

           if cleric_subclass == 13:
               PC_subclass = "Twilight Domain"
               class_feature13 = ("At 17th level, the twilight that you summon offers a protective embrace: you and your allies have half cover while in the sphere created by your Twilight Sanctuary.")

           if cleric_subclass == 14:
               PC_subclass = "War Domain"
               class_feature13 = ("At 17th level, you gain resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons.")
          
           if cleric_subclass == 15:
               PC_subclass = "Soldarity Domain"
               class_feature13 = ("Starting at 17th level, when you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die. For example, instead of restoring 2d6 hit points to a creature, you restore 12.")

           if cleric_subclass == 16:
               PC_subclass = "Strength Domain"
               class_feature13 = ("At 17th level, you gain resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks")

           if cleric_subclass == 17:
               PC_subclass = "Ambition Domain"
               class_feature13 = ("At 17th level, you can create up to four duplicates of yourself, instead of one, when you use Invoke Duplicity. As a bonus action on your turn, you can move any number of them up to 30 feet, to a maximum range of 120 feet.")
          
           if cleric_subclass == 18:
               PC_subclass = "Zeal Domain"
               class_feature13 = ("Starting at 17th level, you can delay death for an instant to perform a final heroic act. When you are reduced to 0 hit points by an attacker you can see, even if you would be killed outright, you can use your reaction to move up to your speed toward the attacker and make one melee weapon attack against it, as long as the movement brings it within your reach. You make this attack with advantage. If the attack hits, the creature takes an extra 5d10 fire damage and an extra 5d10 damage of the weapon’s type. You then fall unconscious and begin making death saving throws as normal, or you die if the damage you took would have killed you outright. Once you use this feature, you can’t use it again until you finish a long rest.")
               
           if cleric_subclass == 19:
               PC_subclass = "Blood Domain"
               class_feature13 = ("At 17th level, as an action, you can emit a powerful aura that extends 30 feet out from you. This aura pulses necrotic energy through the veins of nearby foes, causing them to burst and bleed. For 1 minute, any enemy creatures with blood that begin their turn within the aura or enter it for the first time on their turn immediately suffer 2d6 necrotic damage. Any enemy creature with blood that would regain hit points while within the aura only regains half of the intended number of hit points (rounded up). Once you use this feature, you can’t use it again until you finish a long rest.")
               
           if cleric_subclass == 20:
               PC_subclass = "Mind Domain"
               class_feature13 = ("Starting at 17th level, when you see an ally within 30 feet of you fail a saving throw, you can replace the roll with a 20, potentially changing the outcome. Once you use this feature, you can’t use it again until you finish a short or long rest.")

           if cleric_subclass == 21:
               PC_subclass = "Beauty Domain"
               class_feature13 = ("Starting at 17th level, you become an avatar of unearthly beauty. Your enemies attack with uncertainty, fearful of damaging the wondrous being they behold, while your magic draws upon your presence to augment its power. As a reaction, you can impose a penalty on a creature's attacks against you or on its saving throws against your spells and abilities. This benefit lasts until the end of the current turn The penalty equals your Charisma modifier (minimum 1).")
    
       if PC_level >= 18: 

           level_5_spell3 = cleric_level_5();
           while  level_5_spell3 == level_5_spell1 or level_5_spell3 == level_5_spell2:
               level_5_spell3 = cleric_level_5();

       if PC_level >= 19: 
            feat5 = ability_score_improvement();
            level_6_spell2 = cleric_level_6();
            while  level_6_spell2 == level_6_spell1:
               level_6_spell2 = cleric_level_6();

       if PC_level >= 20:
           level_7_spell2 = cleric_level_7();
           while  level_7_spell2 == level_7_spell1:
               level_7_spell2 = cleric_level_7();
     
    if PC_class == "Druid":
       caster = "True"
       hit_dice = "1d8 per druid level"
       first_lvl_hp = 8 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
           temp = randint(1,8)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1
       PC_hp = first_lvl_hp + high_lvl_hp       

       light_armor = 1
       medium_armor = 1
       shields = 1

       global club
       club = 1

       global daggers
       daggers = 1

       global darts
       darts = 1

       global javelins
       javelins = 1

       global maces
       maces = 1

       global quarterstaffs
       quarterstaffs  = 1

       global sickles
       sickles = 1

       global slings
       slings = 1

       global herbalism_kit
       herbalism_kit = 1

       global PC_int_savethrw
       PC_int_savethrw = 1
       PC_wis_savethrw = 1

       skill1 = randint(1,8)
       if skill1 == 1:
            arcana = 1
       if skill1 == 2:
            animal_handling = 1
       if skill1 == 3:
            medicine = 1
       if skill1 == 4:
            insight = 1
       if skill1 == 5:
           survival = 1
       if skill1 == 6:
           preception = 1
       if skill1 == 7:
            nature = 1
       if skill1 == 8:
           religion = 1

       skill2 = randint(1,8)
       while skill1 == skill2:
           skill2 = randint(1,8)
       if skill1 == 1:
            arcana = 1
       if skill1 == 2:
            animal_handling = 1
       if skill1 == 3:
            medicine = 1
       if skill1 == 4:
            insight = 1
       if skill1 == 5:
           survival = 1
       if skill1 == 6:
           preception = 1
       if skill1 == 7:
            nature = 1
       if skill1 == 8:
           religion = 1

       equipment = randint(1,2)
       if equipment == 1:
           class_equipment = "A Wooden Shield"
       if equipment == 2:
           class_equipment = "Any Simple weapon"

       equipment = randint(1,2)
       if equipment == 1:
           class_equipment2 = "A scimitar"
       if equipment == 2:
           class_equipment2 = "Any Simple melee weapon"
       class_equipment3 = "Leather armor, an explorer's pack, and a druidic focus"
       class_feature1 = "Druids will not wear armor or use shields made of metal. You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic.  "
       global druidic
       druidic = 1
       class_feature2 = ("Your spellcasting chart is shown below"
     "                                                       Slot Types\n"
           "Level     Cantrips Known        1st     2nd     3rd     4th     5th     6th     7th     8th     9th\n"
           "  1             2                2\n"
           "  2             2                3\n"
           "  3             2                4       2\n"
           "  4             3                4       3\n"
           "  5             3                4       3       2\n"
           "  6             3                4       3       3\n"
           "  7             3                4       3       3       1\n"
           "  8             3                4       3       3       2\n"
           "  9             3                4       3       3       3       1\n"
           "  10            4                4       3       3       3       2\n"
           "  11            4                4       3       3       3       2       1\n"
           "  12            4                4       3       3       3       2       1\n"
           "  13            4                4       3       3       3       2       1       1\n"
           "  14            4                4       3       3       3       2       1       1\n"
           "  15            4                4       3       3       3       2       1       1       1\n"
           "  16            4                4       3       3       3       2       1       1       1\n"
           "  17            4                4       3       3       3       2       1       1       1       1\n"
           "  18            4                4       3       3       3       3       1       1       1       1\n"
           "  19            4                4       3       3       3       3       2       1       1       1\n"
           "  20            4                4       3       3       3       3       2       2       1       1\n")
           
       cantrip1 = druid_cantrip();
       cantrip2 = druid_cantrip();
       while cantrip1 == cantrip2:
           cantrip2 = druid_cantrip();

       level_1_spell1 = druid_level_1();
       level_1_spell2 = druid_level_1();
       while level_1_spell1 == level_1_spell2:
           level_1_spell2 = druid_level_1();

       if PC_level >= 2:

          level_1_spell3 = druid_level_1();
          while level_1_spell3 == level_1_spell2 or  level_1_spell3 == level_1_spell1:
                level_1_spell3 = druid_level_1();
          class_feature3 = ("Wild Shape: Starting at 2nd level, you can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest. Your druid level determines the beasts you can transform into, as shown in the Beast Shapes table. At 2nd level, for example, you can transform into any beast that has a challenge rating of 1/4 or lower that doesn't have a flying or swimming speed.\n"
                            "Level 2: Max CR is 1/4, No flying or swimming speed\nLevel 4: Max CR is 1/2, no flying speed\nLevel 8: Max Cr is 1, no limitations\n"
                            "You can stay in a beast shape for a number of hours equal to half your druid level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die. While you are transformed, the following rules apply:\n"
                            "Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.\n"
                            "When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.\n"
                            "You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.\n"
                            "You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense\n"
                            "You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.\n")
          
          class_feature4 = "Wild Companion: At 2nd level, you gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the Find Familiar spell, without material components. When you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your druid level."

          druid_circle = randint(1,8)
          
          if druid_circle == 1:
              PC_subclass = "Circle of Dreams"
              class_feature5 = "Balm of the Summer Court: At 2nd level, you become imbued with the blessings of the Summer Court. You are a font of energy that offers respite from injuries. You have a pool of fey energy represented by a number of d6's equal to your druid level. As a bonus action, you can choose an ally you can see within 120 feet of you and spend a number of those dice equal to half your druid level or less. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent. You regain the expended dice when you finish a long rest."

          if druid_circle == 2:
              PC_subclass = "Circle of the Land"
              cantrip5 = druid_cantrip();
              while cantrip5 == cantrip1 or cantrip5 == cantrip2:
                  cantrip5 = druid_cantrip();
              circle = randint(1,8)
              if circle == 1:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Artic, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Hold Person, Spike Growth\n5th: Sleet Storm, Slow\n7th: Freedom of Movement, Ice Storm\n9th Commune with Nature, Cone of Cold")
              if circle == 2:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Coast, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Mirror Image, Misty Step\n5th: Water Breathing, Water Walk\n7th: Control Water, Freedom of Movement\n9th Conjure Elemental, Scrying")
              
              if circle == 3:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Desert, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Blur, Silence\n5th: Create Food and Water, Protection from Energy\n7th: Blight, Hallucinatory Terrain\n9th Insect Plague, Wall of Stone")
              if circle == 4:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Forest, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Barkskin, Spider Climb\n5th: Call Lightning, Plant Growthy\n7th: Divination, Freedom of Movement\n9th Commune with Nature, Tree Stride")
              if circle == 5:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Grassland, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Invisibility, Pass Without Trace\n5th: Daylight, Haste\n7th: Divination, Freedom of Movement\n9th Dream, Insect Plague")
              if circle == 6:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Mountain, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Spider Climb, Spike Growth\n5th: Lightning Bolt, Meld into Stone\n7th: Stone Shape, Stoneskin\n9th Passwall, Wall of Stone")
              if circle == 7:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Swamp, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Darkness, Melf's Acid Arrow\n5th: Water Walk, Stinking Cloud\n7th: Freedom of Movement, Locate Creature\n9th Insect Plague, Scrying")
              if circle == 8:
                  class_feature5 = ( "Natural Recovery: Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest. For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.\n"
                                "Circle Spells: Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Your land's spells, Underdark, are shown below. Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Spider Climb, Web\n5th: Gaseous Form, Stinking Cloud\n7th: Greater Invisibility, Stone Shape\n9th Cloudkill, Insect Plague")
              
          if druid_circle == 3:
              PC_subclass = "Circle of the Moon"
              class_feature5 = ("Combat Wild Shape: When you choose this circle at 2nd level, you gain the ability to use Wild Shape on your turn as a bonus action, rather than as an action. Additionally, while you are transformed by Wild Shape, you can use a bonus action to expend one spell slot to regain 1d8 hit points per level of the spell slot expended.")
        
          if druid_circle == 4:
              PC_subclass = "Circle of the Sherperd"
              class_feature5 = ("Speech of the Woods: At 2nd level, you gain the ability to converse with beasts and many fey. You learn to speak, read, and write Sylvan. In addition, beasts can understand your speech, and you gain the ability to decipher their noises and motions. Most beasts lack the intelligence to convey or understand sophisticated concepts, but a friendly beast could relay what it has seen or heard in the recent past. This ability doesn’t grant you any special friendship with beasts, though you can combine this ability with gifts to curry favor with them as you would with any nonplayer character."
                                "   Spirit Totem: Starting at 2nd level, you gain the ability to call forth nature spirits and use them to influence the world around you. As a bonus action, you can magically summon an incorporeal spirit to a point you can see within 60 feet of you. The spirit creates an aura in a 30-foot radius around that point. It counts as neither a creature nor an object, though it has the spectral appearance of the creature it represents. As a bonus action, you can move the spirit up to 60 feet to a point you can see. The spirit persists for 1 minute. Once you use this feature, you can’t use it again until you finish a short or long rest. The effect of the spirit’s aura depends on the type of spirit you summon from the options below.\n "
                                "   Bear Spirit: The bear spirit grants you and your allies its might and endurance. Each creature of your choice in the aura when the spirit appears gains temporary hit points equal to 5 + your druid level. In addition, you and your allies gain advantage on Strength checks and Strength saving throws while in the aura.\n"
                                "   Hawk Spirit: The hawk spirit is a consummate hunter, aiding you and your allies with its keen sight. When a creature makes an attack roll against a target in the spirit’s aura, you can use your reaction to grant advantage to that attack roll. In addition, you and your allies have advantage on Wisdom (Perception) checks while in the aura.\n"
                                "   Unicorn Spirit: The unicorn spirit lends its protection to those nearby. You and your allies gain advantage on all ability checks made to detect creatures in the spirit’s aura. In addition, if you cast a spell using a spell slot that restores hit points to any creature inside or outside the aura, each creature of your choice in the aura also regains hit points equal to your druid level.")
              sylvan = 1

          if druid_circle == 5:
              PC_subclass = "Circle of Spores"
              cantrip5 = "Chill Touch"
              class_feature5 = ("Halo of Spores: Starting at 2nd level, you are surrounded by invisible, necrotic spores that are harmless until you unleash them on a creature nearby. When a creature you can see moves into a space within 10 feet of you or starts its turn there, you can use your reaction to deal 1d4 necrotic damage to that creature unless it succeeds on a Constitution saving throw against your spell save DC. The necrotic damage increases to 1d6 at 6th level, 1d8 at 10th level, and 1d10 at 14th level.\n"
                                "Symbiotic Entity: Also at 2nd level, you gain the ability to channel magic into your spores. As an action, you can expend a use of your Wild Shape feature to awaken those spores, rather than transforming into a beast form, and you gain 4 temporary hit points for each level you have in this class. While this feature is active, you gain the following benefits: When you deal your Halo of Spores damage, roll the damage die a second time and add it to the total. Also, Your melee weapon attacks deal an extra 1d6 necrotic damage to any target they hit. These benefits last for 10 minutes, until you lose all these temporary hit points. or until you use your Wild Shape again."
                                "Circle Spells: Your symbiotic link to fungi and your ability to tap into the cycle of life and death grants you access to certain spells. At 2nd level, you learn the Chill Touch cantrip. At 3rd, 5th, 7th, and 9th level you gain access to the spells listed for that level in the Circle of Spores Spells table. Once you gain access to one of these spells, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\n"
                                "3rd: Blindness/Deafness, Gentle Repose\n5th: Animate Dead, Gaseous Form\n7th: Blight, Confusion\n9th Cloudkill, Contagion\n")
              
          if druid_circle == 6:
              PC_subclass = "Circle of Stars"
              class_feature5 = ("Star Map: At 2nd level, You've created a star chart as part of your heavenly studies. It is a Tiny object and can serve as a spellcasting focus for your druid spells. You determine its form by rolling on the Star Map table or by choosing one. While holding this map, you have the following benefits\n"
                                "You know the Guidance cantrip, you have the Guiding Bolt spell prepared. It counts as a druid spell for you, it doesn't count against the number of spells you can have prepared, and you can cast it without expending a spell slot. You can do so a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.\n "
                                "If you lose the map, you can perform a 1-hour ceremony to magically create a replacement. This ceremony can be performed during a short or long rest, and it destroys the previous map.\n"
                                "Map Forms: Roll 1 d6 to determine the map form: 1: A scroll covered with depictions of constellations\n2: A stone tablet with fine holes drilled through it\n3: A speckled owlbear hide, tooled with raised marks\n4: A collection of maps bound in an ebony cover\n5: A crystal that projects starry patterns when placed before a light\n6: Glass disks that depict constellations\n"
                                "Starry Form: At 2nd level, you gain the ability to harness constellations’ power to alter your form. As a bonus action, you can expend a use of your Wild Shape feature to take on a starry form, rather than transforming into a beast. While in your starry form, you retain your game statistics, but your body becomes luminous; your joints glimmer like stars, and glowing lines connect them as on a star chart. This form sheds bright light in a 10-foot radius and dim light for an additional 10 feet. The form lasts for 10 minutes. It ends early if you dismiss it (no action required), are incapacitated, die, or use this feature again. Whenever you assume your starry form, choose which of the following constellations glimmers on your body; your choice gives you certain benefits while in the form:\n"
                                "   Archer: A constellation of an archer appears on you. When you activate this form, and as a bonus action on your subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one creature within 60 feet of you. On a hit, the attack deals radiant damage equal to 1d8 + your Wisdom modifier.\n"
                                "   Chalice: A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that restores hit points to a creature, you or another creature within 30 feet of you can regain hit points equal to 1d8 + your Wisdom modifier.\n"
                                "   Dragon: A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a Constitution saving throw to maintain concentration on a spell, you can treat a roll of 9 or lower on the d20 as a 10.")


          if druid_circle == 7:
              PC_subclass = "Circle of Wildfire"
              class_feature5 = ("Circle Spells:When you join this circle at 2nd level, you have formed a bond with a wildfire spirit, a primal being of creation and destruction. Your link with this spirit grants you access to some spells when you reach certain levels in this class, as shown on the Circle of Wildfire Spells table. Once you gain access to one of these spells, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the Druid Spell List, the spell is nonetheless a druid spell for you.\n"
                                "2nd: Burning Hands, Cure Wounds\n3rd: Flaming Sphere, Scorching Ray\n5th: Plant Growth, Revivify\n7th: Aura of Life, Fire Shield\n9th Flame Strike, Mass Cure Wounds\n\n"
                                "Summon Wildfire Spirit: At 2nd level, You can summon the primal spirit bound to your soul. As an action, you can expend one use of your Wild Shape feature to summon your wildfire spirit, rather than assuming a beast form. The spirit appears in an unoccupied space of your choice that you can see within 30 feet of you. Each creature within 10 feet of the spirit (other than you) when it appears must succeed on a Dexterity saving throw against your spell save DC or take 2d6 fire damage.\n"
                                "The spirit is friendly to you and your companions and obeys your commands. See this creature's game statistics in the Wildfire Spirit stat block, which uses your proficiency bonus (PB) in several places. You determine the spirit's appearance. Some spirits take the form of a humanoid figure made of gnarled branches covered in flame, while others look like beasts wreathed in fire. In combat, the spirit shares your initiative count, but it takes its turn immediately after yours. The only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the spirit can take any action of its choice, not just Dodge. The spirit manifests for 1 hour, until it is reduced to 0 hit points, until you use this feature to summon the spirit again, or until you die.\n"
                                "Wildfire Spirit Stats: Small elemental, AC: 13 (Natural Armor) Hitpoints: 5 + 5 times your druid level Speed: 30ft. Fly 30 ft. (hover)\n"
                                "Str: 10 (+0)\nDex: 14 (+2)\nCon: 14 (+2)\n Int: 13 (+1)\n Wis 15 (+2)\nCha 11 (+0)\nDamage Immunities: Fire\nCondition Immunities: Charmed, Frightened, Grappled, Prone, Restrained\nSenses: Darkvision 60ft, Passive Perception 12\n Languages: Understands the languages you speak\n Proficiency Bonus: Equal your bonus\nActions: Flame Seed: Flame Seed. Ranged Weapon Attack: your spell attack modifier to hit, range 60 ft., one target you can see. Hit: 1d6 + PB fire damage\nFiery Teleportation: The spirit and each willing creature of your choice within 5 feet of it teleport up to 15 feet to unoccupied spaces you can see. Then each creature within 5 feet of the space that the spirit left must succeed on a Dexterity saving throw against your spell save DC or take 1d6 + PB fire damage.")

          if druid_circle == 8:
              PC_subclass = "Circle of the Forged"
              class_feature5 = ("Circle Forms: The rites of your circle grant you the ability to transform into more dangerous animal forms. Starting at 2nd level, you can use your Wild Shape to transform into a beast with a challenge rating as high as 1 (you ignore the Max. CR column of the Beast Shapes table, but must abide by the other limitations there). Starting at 6th level, you can transform into a beast with a challenge rating as high as your druid level divided by 3, rounded down."
                                "Skin of Steel: Starting at 2nd level, while you are transformed by Wild Shape, you gain the following benefits: You gain a +2 bonus to Armor Class, You have advantage on saving throws against being poisoned, and you have resistance to poison damage, You don’t need to eat, drink, or breathe., You are immune to disease., You don’t need to sleep, and magic can’t put you to sleep.\nWhile in beast form, your body is made from the same materials as a warforged; your muscles are rootlike tendrils protected by armored plates. It’s obvious to an observer that you are not a normal animal.")

       if PC_level >= 3:
           level_1_spell4 = druid_level_1();
           while level_1_spell4 == level_1_spell2 or  level_1_spell4 == level_1_spell1 or level_1_spell4 == level_1_spell3:
                level_1_spell4 = druid_level_1();
           level_2_spell1 = druid_level_2();
           level_2_spell2 = druid_level_2();
           while  level_2_spell1 == level_2_spell2:
                level_2_spell2 = druid_level_2();

       if PC_level >=4:
           feat1 = ability_score_improvement();
           class_feature6 = "Cantrip Versatility: Whenever you reach a level in this class that grants the Ability Score Improvement feature (4,8,12,16,19), you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the druid spell list."
           cantrip3 = druid_cantrip();
           while cantrip3 == cantrip1 or cantrip3 == cantrip2 or cantrip3 == cantrip5:
               cantrip3 = druid_cantrip();
           level_2_spell3 = druid_level_2();
           while level_2_spell3 == level_2_spell2 or  level_2_spell3 == level_2_spell1:
                level_2_spell3 = druid_level_2();

       if PC_level >= 5:
           PC_prof_bonus = 3
           level_3_spell1 = druid_level_3();
           level_3_spell2 = druid_level_3();
           while  level_3_spell1 == level_3_spell2:
                level_3_spell2 = druid_level_3();
            
       if PC_level >= 6:
          level_3_spell3 = druid_level_3();
          while level_3_spell3 == level_3_spell2 or  level_3_spell3 == level_3_spell1:
                level_3_spell3 = druid_level_3();

          if druid_circle == 1:
              class_feature7 = "Hearth of Moonlight and Shadow: At 6th level, home can be wherever you are. During a short or long rest, you can invoke the shadowy power of the Gloaming Court to help guard your respite. At the start of the rest, you touch a point in space, and an invisible, 30-foot-radius sphere of magic appears, centered on that point. Total cover blocks the sphere. While within the sphere, you and your allies gain a +5 bonus to Dexterity (Stealth) and Wisdom (Perception) checks, and any light from open flames in the sphere (a campfire, torches, or the like) isn't visible outside it. The sphere vanishes at the end of the rest or when you leave the sphere."
          
          if druid_circle == 2:
              class_feature7 = "Land's Stride: Starting at 6th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard. In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell."

          if druid_circle == 3:
              class_feature7 = "Primal Strike: Starting at 6th level, your attacks in beast form count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."

          if druid_circle == 4:
              class_feature7 = "Mighty Summoner: At 6th level, beasts and fey that you conjure are more resilient than normal. Any beast or fey summoned or created by a spell that you cast gains two benefits: The creature appears with more hit points than normal: 2 extra hit points per Hit Die it has and The damage from its natural weapons is considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks and damage."

          if druid_circle == 5:
              class_feature7 = "Fungal Infestation: At 6th level, your spores gain the ability to infest a corpse and animate it. If a beast or a humanoid that is Small or Medium dies within 10 feet of you, you can use your reaction to animate it, causing it to stand up immediately with 1 hit point. The creature uses the Zombie stat block in the Monster Manual. It remains animate for 1 hour, after which time it collapses and dies. In combat, the zombie's turn comes immediately after yours. It obeys your mental commands, and the only action it can take is the Attack action, making one melee attack. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest."

          if druid_circle == 6:
              class_feature7 = ("Cosmic Omen: When you reach 6th level, you learn to use your star map to divine the will of the cosmos. Whenever you finish a long rest, you can consult your Star Map for omens. When you do so, roll a die. Until you finish your next long rest, you gain access to a special reaction based on whether you rolled an even or an odd number on the die:\n"
                                "   Weal (even). Whenever a creature you can see within 30 feet of you is about to make an attack roll, a saving throw, or an ability check, you can use your reaction to roll a d6 and add the number rolled to the total.\n"
                                "   Woe (odd). Whenever a creature you can see within 30 feet of you is about to make an attack roll, a saving throw, or an ability check, you can use your reaction to roll a d6 and subtract the number rolled from the total.\n"
                                "You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")

          if druid_circle == 7:
               class_feature7 = "Enhanced Bond: At 6th level, the bond with your wildfire spirit enhances your destructive and restorative spells. Whenever you cast a spell that deals fire damage or restores hit points while your wildfire spirit is summoned, roll a d8, and you gain a bonus equal to the number rolled to one damage or healing roll of the spell. In addition, when you cast a spell with a range other than self, the spell can originate from you or your wildfire spirit."

          if druid_circle == 8:
              class_feature7 = ("Elemental Fury: Starting at 6th level, you gain the ability to imbue your attacks with elemental damage—charging your claws with electricity or unleashing flames from your fangs. When you use Wild Shape, choose one of the following damage types: acid, cold, fire, or lightning. While in your beast form, the first time you hit a creature with a melee attack on your turn, you can expend one spell slot to deal extra damage of that type to the target, in addition to the normal damage of the attack. The extra damage is 1d6 per level of the spell slot expended, to a maximum of 5d6. When you use this ability on a creature, your attack has an additional effect, determined by which damage type you selected when you used Wild Shape. If a creature is affected by this ability again in subsequent rounds, the effects do not stack, and the new duration replaces the old.\n"
                                "   Acid. The target must make a Constitution saving throw against your druid spell save DC. On a failed save, its AC is reduced for one minute by an amount equal to half your Wisdom modifier (minimum of 1). At the start of each of its turns for the next minute, the target can make another Constitution saving throw. On a successful save, the effect ends.\n"
                                "   Cold. At the start of each of its turns for 1 minute, the target must make a Constitution saving throw against your druid spell save DC. On a failed save, their movement speed is reduced to 0 and they have disadvantage on Strength and Dexterity checks. On a successful save, the effect ends.\n"
                                "   Fire. At the start of each of its turns for 1 minute, the target must make a Constitution saving throw against your druid spell save DC. On a failed save, it takes fire damage equal to your Wisdom modifier. On a successful save, the fire goes out. If the target or a creature within 5 feet of it uses an action to put out the flames, or if some other effect douses the flames (such as the target being submerged in water), the effect ends.\n"
                                "   Lightning. At the start of each of its turns for 1 minute, the target must make a Constitution saving throw against your druid spell save DC. On a failed save, it loses its reaction until the start of its next turn and the first attack that it makes on its turn is made at disadvantage. On a successful save, the effect ends.")

       if PC_level >= 7:
           level_4_spell1 = druid_level_4();

       if PC_level >= 8:
           feat2 = ability_score_improvement();
           level_4_spell2 = druid_level_4();
           while  level_4_spell1 == level_4_spell2:
                level_4_spell2 = druid_level_4();

       if PC_level >= 9:
          PC_prof_bonus = 4
          level_4_spell3 = druid_level_4();
          while level_4_spell3 == level_4_spell2 or  level_4_spell3 == level_4_spell1:
                level_4_spell3 = druid_level_4();
          level_5_spell1 = druid_level_5();

       if PC_level >= 10:
           level_5_spell2 = druid_level_5();
           while  level_5_spell1 == level_5_spell2:
                level_5_spell2 = druid_level_5();
           cantrip4 = druid_cantrip();
           while cantrip4 == cantrip1 or cantrip4 == cantrip2 or cantrip4 == cantrip3 or cantrip4 == cantrip5:
               cantrip4 = druid_cantrip();

           if druid_circle == 1:
               class_feature8 = "Hidden Paths: Starting at 10th level, you can use the hidden, magical pathways that some fey use to traverse space in a blink of an eye. As a bonus action on your turn, you can teleport up to 60 feet to an unoccupied space you can see. Alternatively, you can use your action to teleport one willing creature you touch up to 30 feet to an unoccupied space you can see. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest."

           if druid_circle == 2:
               class_feature8 = "Nature's Ward: When you reach 10th level, you can't be charmed or frightened by elementals or fey, and you are immune to poison and disease."

           if druid_circle == 3:
               class_feature8 = "Elemental Wild Shape: At 10th level, you can expend two uses of Wild Shape at the same time to transform into an air elemental, an earth elemental, a fire elemental, or a water elemental."

           if druid_circle == 4:
               class_feature8 = "Guardian Spirit: Beginning at 10th level, your Spirit Totem safeguards the beasts and fey that you call forth with your magic. When a beast or fey that you summoned or created with a spell ends its turn in your Spirit Totem aura, that creature regains a number of hit points equal to half your druid level."

           if druid_circle == 5:
                class_feature8 = "Spreading Spores: At 10th level, you gain the ability to seed an area with deadly spores. As a bonus action while your Symbiotic Entity feature is active, you can hurl spores up to 30 feet away, where they swirl in a 10-foot cube for 1 minute. The spores disappear early if you use this feature again, if you dismiss them as a bonus action, or if your Symbiotic Entity feature is no longer active. Whenever a creature moves into the cube or starts its turn there, that creature takes your Halo of Spores damage, unless the creature succeeds on a Constitution saving throw against your spell save DC. A creature can take this damage no more than once per turn. While the cube of spores persists, you can't use your Halo of Spores reaction."

           if druid_circle == 6:
                class_feature8 = "Twinkling Constellations: At 10th level, the constellations of your Starry Form improve. The 1d8 of the Archer and the Chalice becomes 2d8, and while the Dragon is active, you have a flying speed of 20 feet and can hover. Moreover, at the start of each of your turns while in your Starry Form, you can change which constellation glimmers on your body."

           if druid_circle == 7:
               class_feature8 = "Cauterizing Flames: At 10th level, you gain the ability to turn death into magical flames that can heal or incinerate. When a Small or larger creature dies within 30 feet of you or your wildfire spirit, a harmless spectral flame springs forth in the dead creature's space and flickers there for 1 minute. When a creature you can see enters that space, you can use your reaction to extinguish the spectral flame there and either heal the creature or deal fire damage to it. The healing or damage equals 2d10 + your Wisdom modifier. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."

           if druid_circle == 8:
               class_feature8 = "Adamantine Hide: Starting at 10th level, while you are transformed by Wild Shape, you gain resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks. In addition, you gain the ability to use Wild Shape as a reaction when you take damage, and the damage from that attack is applied to the hit points of your beast form."

       if PC_level >= 11:
           level_6_spell1 = druid_level_6();

       if PC_level >= 12:
           feat3 = ability_score_improvement();

       if PC_level >= 13:
           PC_prof_bonus = 5
           level_7_spell1 = druid_level_7();

       if PC_level >= 14:

           if druid_circle == 1:
               class_feature9 = "Walker in Dreams: At 14th level, the magic of the Feywild grants you the ability to travel mentally or physically through dreamlands. When you finish a short rest, you can cast one of the following spells, without expending a spell slot or requiring material components: Dream (with you as the messenger), Scrying, or Teleportation Circle. This use of Teleportation Circle is special. Rather than opening a portal to a permanent teleportation circle, it opens a portal to the last location where you finished a long rest on your current plane of existence. If you haven't taken a long rest on your current plane, the spell fails but isn't wasted. Once you use this feature, you can't use it again until you finish a long re"
    
           if druid_circle == 2:
               class_feature9 = "Nature's Sanctuary: When you reach 14th level, creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours. The creature is aware of this effect before it makes its attack against you."

           if druid_circle == 3:
               class_feature9 = "Thousand Forms: By 14th level, you have learned to use magic to alter your physical form in more subtle ways. You can cast the Alter Self spell at will."

           if druid_circle == 4:
               class_feature9 = "Faithful Summons: Starting at 14th level, the nature spirits you commune with protect you when you are the most defenseless. If you are reduced to 0 hit points or are incapacitated against your will, you can immediately gain the benefits of Conjure Animals as if it were cast with a 9th-level spell slot. It summons four beasts of your choice that are challenge rating 2 or lower. The conjured beasts appear within 20 feet of you. If they receive no commands from you, they protect you from harm and attack your foes. The spell lasts for 1 hour, requiring no concentration, or until you dismiss it (no action required). Once you use this feature, you can’t use it again until you finish a long rest."

           if druid_circle == 5:
               class_feature9 = "Fungal Body: At 14th level, the fungal spores in your body alter you: you can't be blinded, deafened, frightened, or poisoned, and any critical hit against you counts as a normal hit instead, unless you're incapacitated."

           if druid_circle == 6:
               class_feature9 = "Full of Stars: At 14th level, while in your Starry Form, you become partially incorporeal, giving you resistance to bludgeoning, piercing, and slashing damage."

           if druid_circle == 7:
               class_feature9 = "Blazing Revival: At 14th level, the bond with your wildfire spirit can save you from death. If the spirit is within 120 feet of you when you are reduced to 0 hit points and thereby fall unconscious, you can cause the spirit to drop to 0 hit points. You then regain half your hit points and immediately rise to your feet. Once you use this feature, you can't use it again until you finish a long rest."

           if druid_circle == 8:
               class_feature9 = "Constructed Perfection: Starting at 14th level, while you are transformed by Wild Shape, you can’t be charmed, frightened, paralyzed, petrified, or poisoned. In addition, you are immune to poison damage."

       if PC_level >= 15:
           level_8_spell1 = druid_level_8();
   
       if PC_level >= 16:
           feat4 = ability_score_improvement();

       if PC_level >= 17:
           PC_prof_bonus = 6
           level_9_spell1 = druid_level_9();

       if PC_level >= 18:
           level_5_spell3 = druid_level_5();
           while level_5_spell3 == level_5_spell2 or  level_5_spell3 == level_5_spell1:
                level_5_spell3 = druid_level_5();
           class_feature10 = "Timeless Body: Starting at 18th level, the primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year."
           class_feature11 = "Beast Spells: Beginning at 18th level, you can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components."

       if PC_level >= 19:
           feat5 = ability_score_improvement();
           level_6_spell2 = druid_level_6();
           while level_6_spell2 == level_6_spell1:
               level_6_spell2 = druid_level_6();

       if PC_level >= 20:
            class_feature12 = "Archdruid: At 20th level, you can use your Wild Shape an unlimited number of times. Additionally, you can ignore the verbal and somatic components of your druid spells, as well as any material components that lack a cost and aren't consumed by a spell. You gain this benefit in both your normal shape and your beast shape from Wild Shape."
            level_7_spell2 = druid_level_7();
            while level_7_spell2 == level_7_spell1:
               level_7_spell2 = druid_level_7();

    if PC_class == "Fighter":
        hit_dice = "1d10 per fighter level"
        first_lvl_hp = 10 + modifier(Constitution)
        hp_level = PC_level - 1
        high_lvl_hp = 0
        while hp_level != 0:
           temp = randint(1,10)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1
        PC_hp = first_lvl_hp + high_lvl_hp
        light_armor = 1
        medium_armor = 1
        heavy_armor = 1
        shields = 1
        simple_weapons = 1
        martial_weapons = 1

        PC_str_savethrw = 1
        PC_con_savethrw = 1

        skill1 = randint(1,8)
        if skill1 == 1:
           acrobatics = 1
        if skill1 == 2:
           animal_handling = 1
        if skill1 == 3:
             athletics = 1
        if skill1 == 4:
            history = 1
        if skill1 == 5:
           insight = 1
        if skill1 == 6:
            inintimidation = 1
        if skill1 == 7:
            precption = 1
        if skill1 == 8:
            survival = 1

        skill2 = randint(1,8)
        while skill1 == skill2:
            skill2 = randint(1,8)

        if skill2 == 1:
           acrobatics = 1
        if skill2 == 2:
           animal_handling = 1
        if skill2 == 3:
             athletics = 1
        if skill2 == 4:
            history = 1
        if skill2 == 5:
           insight = 1
        if skill2 == 6:
            inintimidation = 1
        if skill2 == 7:
            precption = 1
        if skill2 == 8:
            survival = 1

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment = "Chain Mail Armor"
        if equipment == 2:
            class_equipment = " leather armor, longbow, and 20 arrows"

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment2 = " A martial weapon and a shield "
        if equipment == 2:
            class_equipment2 = " Two martial weaponss"

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment3 = " A light crossbow and 20 bolts "
        if equipment == 2:
            class_equipment3 = " Two handaxes"

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment4 = " A dungeoneer's pack "
        if equipment == 2:
            class_equipment4 = " An explorer's packs"

        fighting_style = randint(1,14)

        if fighting_style == 1:
            class_feature1 = "Fighting Style: Archery: You gain a +2 bonus to attack rolls you make with ranged weapons."

        if fighting_style == 2:
            class_feature1 = "Fighting Style: Blind Fighting: You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you."

        if fighting_style == 3:
            class_feature1 = "Fighting Style: Defense: While you are wearing armor, you gain a +1 bonus to AC."
    
        if fighting_style == 4:
            class_feature1 = "Fighting Style: Dueling: When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon."

        if fighting_style == 5:
            class_feature1 = "Fighting Style: Great Weapon Fighting: When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit."

        if fighting_style == 6:
            class_feature1 = "Fighting Style: Interception: When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction."

        if fighting_style == 7:
            class_feature1 = "Fighting Style: Protection: When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield."

        if fighting_style == 8:
            class_feature1 = "Fighting Style: Superior Technique: You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.). You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest."

        if fighting_style == 9:
            class_feature1 = "Fighting Style: Thrown Weapon Fighting: You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll."

        if fighting_style == 10:
            class_feature1 = "Fighting Style: Two-Weapon Fighting: When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack."
    
        if fighting_style == 11:
            class_feature1 = "Fighting Style: Unarmed Fighting: Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."

        if fighting_style == 12:
            class_feature1 = "Fighting Style: Close Quarters Shooter (UA): When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks."

        if fighting_style == 13:
            class_feature1 = "Fighting Style: Mariner (UA): As long as you are not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class."

        if fighting_style == 14:
            class_feature1 = "Fighting Style: Tunnel Fighter (UA): As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach."

        class_feature2 = "Second Wind: You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again."

        if PC_level >= 2:
            class_feature3 = "Action Surge: Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn. "

        if PC_level >= 3:
            martial_archetype = randint(1,12)

            if martial_archetype == 1:
                PC_subclass = "Arcane Archer"
                class_feature4 = ("Arcane Archer Lore: At 3rd level, you learn magical theory or some of the secrets of nature – typical for practitioners of of this elven martial tradition. You choose to gain proficiency in either the Arcana or the Nature skill, and you choose to learn either the Prestidigitation or Druidcraft cantrip.\n" 
                                  "Arcane Shot: At 3rd level, you learn to unleash special magical effects with some of your shots. When you gain this feature, you learn two Arcane Shot options of your choice. Once per turn when you fire an arrow from a shortbow or longbow as part of the Attack action, you can apply one of your Arcane Shot options to that arrow. You decide to use the option when the arrow hits, unless the option doesn’t involve an attack roll. You have two uses of this ability, and you regain all expended uses of it when you finish a short or long rest. You gain an additional Arcane Shot option of your choice when you reach certain levels in this class: 7th, 10th, 15th, and 18th level. Each option also improves when you become an 18th-level fighter. If an option requires a saving throw, your Arcane Shot save DC equals 8 + your proficiency bonus + your Intelligence modifier.\n"
                                  "    Arcane Shot options:\n"
                                  "    Banishing Arrow. You use abjuration magic to try to temporarily banish your target to a harmless location in the Feywild. The creature hit by the arrow must also succeed on a Charisma saving throw or be banished. While banished in this way, its speed is 0, and it is incapacitated. At the end of its next turn, the target reappears in the space it vacated or in the nearest unoccupied space if that space is occupied. After you reach 18th level in this class, a target also takes 2d6 force damage when the arrow hits it.\n"
                                  "    Beguiling Arrow. Your enchantment magic causes this arrow to temporarily beguile its target. The creature hit by the arrow takes an extra 2d6 psychic damage, and choose one of your allies within 30 feet of the target. The target must succeed on a Wisdom saving throw, or it is charmed by the chosen ally until the start of your next turn. This effect ends early if the chosen ally attacks the charmed target, deals damage to it, or forces it to make a saving throw. The psychic damage increases to 4d6 when you reach 18th level in this class.\n"
                                  "    Bursting Arrow. You imbue your arrow with force energy drawn from the school of evocation. The arrow detonates after your attack. Immediately after the arrow hits the creature, the target and all other creatures within 10 feet of it take 2d6 force damage each. The force damage increases to 4d6 when you reach 18th level in this class.\n"
                                  "    Enfeebling Arrow. You weave necromantic magic into your arrow. The creature hit by the arrow takes an extra 2d6 necrotic damage. The target must also succeed on a Constitution saving throw, or the damage dealt by its weapon attacks is halved until the start of your next turn. The necrotic damage increases to 4d6 when you reach 18th level in this class.\n"
                                  "    Grasping Arrow. When this arrow strikes its target, conjuration magic creates grasping, poisonous brambles, which wrap around the target. The creature hit by the arrow takes an extra 2d6 poison damage, its speed is reduced by 10 feet, and it takes 2d6 slashing damage the first time on each turn it moves 1 foot or more without teleporting. The target or any creature that can reach it can use its action to remove the brambles with a successful Strength (Athletics) check against your Arcane Shot save DC. Otherwise, the brambles last for 1 minute or until you use this option again. The poison damage and slashing damage both increase to 4d6 when you reach 18th level in this class.\n"
                                  "    Piercing Arrow. You use transmutation magic to give your arrow an ethereal quality. When you use this option, you don’t make an attack roll for the attack. Instead, the arrow fires forward in a line, which is 1 foot wide and 30 feet long, before disappearing. The arrow passes harmlessly through objects, ignoring cover. Each creature in that line must make a Dexterity saving throw. On a failed save, a creature takes damage as if it were hit by the arrow, plus an extra 1d6 piercing damage. On a successful save, a target takes half as much damage. The piercing damage increases to 2d6 when you reach 18th level in this class.\n"
                                  "    Seeking Arrow. Using divination magic, you grant your arrow the ability to seek out your target, allowing the arrow to curve and twist its path in search of its prey. When you use this option, you don’t make an attack roll for the attack. Instead, choose one creature you have seen in the past minute. The arrow flies toward that creature, moving around corners if necessary and ignoring three-quarters cover and half cover. If the target is within the weapon’s range and there is a path large enough for the arrow to travel to the target, the target must make a Dexterity saving throw. On a failed save, it takes damage as if it were hit by the arrow, plus an extra 1d6 force damage, and you learn the target’s current location. On a successful save, the target takes half as much damage, and you don’t learn its location. The force damage increases to 2d6 when you reach 18th level in this class.\n"
                                  "    Shadow Arrow. You weave illusion magic into your arrow, causing it to occlude your foe’s vision with shadows. The creature hit by the arrow takes an extra 2d6 psychic damage, and it must succeed on a Wisdom saving throw or be unable to see anything farther than 5 feet away until the start of your next turn. The psychic damage increases to 4d6 when you reach 18th level in this class.")

            if martial_archetype == 2:
                PC_subclass = "Banneret"
                class_feature4 = "Rallying Cry: When you choose this archetype at 3rd level, you learn how to inspire your allies to fight on past their injuries. When you use your Second Wind feature, you can choose up to three creatures within 60 feet of you that are allied with you. Each one regains hit points equal to your fighter level, provided that the creature can see or hear you."

            if martial_archetype == 3:
                PC_subclass = "Battle Master"
                class_feature4 = ("When you choose this archetype at 3rd level, you learn maneuvers that are fueled by special dice called superiority dice.\nManeuvers: You learn three maneuvers of your choice. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack. You learn two additional maneuvers of your choice at 7th, 10th, and 15th level. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one.\nSuperiority Dice: You have four superiority dice, which are d8s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest. You gain another superiority die at 7th level and one more at 15th level.\n" 
                                  "Saving Throws: Some of your maneuvers require your target to make a saving throw to resist the maneuver's effects. The saving throw DC is calculated as follows: Maneuver save DC = 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice)\nYou also gain proficiency with one type of artisan's tools of your choice.\n    Maneuver list:\n"
                                  "    Ambush: When you make a Dexterity (Stealth) check or an initiative roll, you can expend one superiority die and add the die to the roll, provided you aren't incapacitated.\n"
                                  "    Bait and Switch: When you're within 5 feet of a creature on your turn, you can expend one superiority die and switch places with that creature, provided you spend at least 5 feet of movement and the creature is willing and isn't incapacitated. This movement doesn't provoke opportunity attacks. Roll the superiority die. Until the start of your next turn, you or the other creature (your choice) gains a bonus to AC equal to the number rolled.\n"
                                  "    Brace: When a creature you can see moves into the reach you have with the melee weapon you're wielding, you can use your reaction to expend one superiority die and make one attack against the creature, using that weapon. If the attack hits, add the superiority die to the weapon's damage roll.\n"
                                  "    Commander's Strike: When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll.\n"
                                  "    Commanding Presence: When you make a Charisma (Intimidation), a Charisma (Performance), or a Charisma (Persuasion) check, you can expend one superiority die and add the superiority die to the ability check.\n"
                                  "    Disarming Attack: When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it's holding. You add the superiority die to the attack's damage roll, and the target must make a Strength saving throw. On a failed save, it drops the object you choose. The object lands at its feet.\n"
                                  "    Distracting Strike: When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack's damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn.\n"
                                  "    Evasive Footwork: When you move, you can expend one superiority die, rolling the die and adding the number rolled to your AC until you stop moving.\n"
                                  "    Feinting Attack: You can expend one superiority die and use a bonus action on your turn to feint, choosing one creature within 5 feet of you as your target. You have advantage on your next attack roll against that creature before the end of your turn. If that attack hits, add the superiority die to the attack's damage roll.\n"
                                  "    Goading Attack: When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.\n"
                                  "    Grappling Strike: Immediately after you hit a creature with a melee attack on your turn, you can expend one superiority die and then try to grapple the target as a bonus action (see the Player's Handbook for rules on grappling). Add the superiority die to your Strength (Athletics) check.\n"
                                  "    Lunging Attack: When you make a melee weapon attack on your turn, you can expend one superiority die to increase your reach for that attack by 5 feet. If you hit, you add the superiority die to the attack's damage roll.\n"
                                  "    Maneuvering Attack: When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your comrades into a more advantageous position. You add the superiority die to the attack's damage roll, and you choose a friendly creature who can see or hear you. That creature can use its reaction to move up to half its speed without provoking opportunity attacks from the target of your attack.\n"
                                  "    Menacing Attack: When you hit a creature with a weapon attack, you can expend one superiority die to attempt to frighten the target. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, it is frightened of you until the end of your next turn\n"
                                  "    Parry: When another creature damages you with a melee attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your Dexterity modifier.\n"
                                  "    Precision Attack: When you make a weapon attack roll against a creature, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied.\n"
                                  "    Pushing Attack: When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you.\n"
                                  "    Quick Toss: As a bonus action, you can expend one superiority die and make a ranged attack with a weapon that has the thrown property. You can draw the weapon as part of making this attack. If you hit, add the superiority die to the weapon's damage roll.\n"
                                  "    Riposte: When a creature misses you with a melee attack, you can use your reaction and expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack's damage roll.\n"
                                  "    Sweeping Attack: When you hit a creature with a melee weapon attack, you can expend one superiority die to attempt to damage another creature with the same attack. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your superiority die. The damage is of the same type dealt by the original attack.\n"
                                  "    Tactical Assessment: When you make an Intelligence (Investigation), an Intelligence (History), or a Wisdom (Insight) check, you can expend one superiority die and add the superiority die to the ability check.\n"
                                  "    Trip Attack: When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you knock the target prone.\n")

            if martial_archetype == 4:
                PC_subclass = "Cavalier"
                class_feature4 = ("When you choose this archetype at 3rd level, you gain proficiency in one of the following skills of your choice: Animal Handling, History, Insight, Performance, or Persuasion. Alternatively, you learn one language of your choice.\n"
                                  "Born to the Saddle: Starting at 3rd level, your mastery as a rider becomes apparent. You have advantage on saving throws made to avoid falling off your mount. If you fall off your mount and descend no more than 10 feet, you can land on your feet if you’re not incapacitated. Finally, mounting or dismounting a creature costs you only 5 feet of movement, rather than half your speed."
                                  "\nUnwavering Mark: Starting at 3rd level, you can menace your foes, foiling their attacks and punishing them for harming others. When you hit a creature with a melee weapon attack, you can mark the creature until the end of your next turn. This effect ends early if you are incapacitated or you die, or if someone else marks the creature. While it is within 5 feet of you, a creature marked by you has disadvantage on any attack roll that doesn't target you. In addition, if a creature marked by you deals damage to anyone other than you, you can make a special melee weapon attack against the marked creature as a bonus action on your next turn. You have advantage on the attack roll, and if it hits, the attack's weapon deals extra damage to the target equal to half your fighter level. Regardless of the number of creatures you mark, you can make this special attack a number of times equal to your Strength modifier (a minimum of once), and you regain all expended uses of it when you finish a long rest.")

            if martial_archetype == 5:
                PC_subclass = "Champion"
                class_feature4 = "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."

            if martial_archetype == 6:
                PC_subclass = "Echo Knight"
                class_feature4 = ("Manifest Echo: At 3rd level, you can use a bonus action to magically manifest an echo of yourself in an unoccupied space you can see within 15 feet of you. This echo is a magical, translucent, gray image of you that lasts until it is destroyed, until you dismiss it as a bonus action, until you manifest another echo, or until you're incapacitated. Your echo has AC 14 + your proficiency bonus, 1 hit point, and immunity to all conditions. If it has to make a saving throw, it uses your saving throw bonus for the roll. It is the same size as you, and it occupies its space. On your turn, you can mentally command the echo to move up to 30 feet in any direction (no action required). If your echo is ever more than 30 feet from you at the end of your turn, it is destroyed.\n"
                                "As a bonus action, you can teleport, magically swapping places with your echo at a cost of 15 feet of your movement, regardless of the distance between the two of you. When you take the Attack action on your turn, any attack you make with that action can originate from your space or the echo's space. You make this choice for each attack. When a creature that you can see within 5 feet of your echo moves at least 5 feet away from it, you can use your reaction to make an opportunity attack against that creature as if you were in the echo's space.\n"
                                "Unleash Incarnation: At 3rd level, you can heighten your echo's fury. Whenever you take the Attack action, you can make one additional melee attack from the echo's position. You can use this feature a number of times equal to your Constitution modifier (a minimum of once). You regain all expended uses when you finish a long rest.")

            if martial_archetype == 7:
                PC_subclass = "Eldritch Knight"
                caster = "Half"

                cantrip1 = wizard_cantrip();
                cantrip2= wizard_cantrip();

                while cantrip1 == cantrip2:
                    cantrip2= wizard_cantrip();

                class_feature4 = ("Spellcasting: When you reach 3rd level, you augment your martial prowess with the ability to cast spells."
                                 "Your spellcasting chart is shown below\n"
                                 "                         Slot Types\n"
                                       "Level     Cantrips Known        1st     2nd     3rd     4th\n"
                                       "  3             2                3\n"
                                       "  4             2                3\n"
                                       "  5             2                4\n"
                                       "  6             2                4\n"
                                       "  7             2                4       2\n"
                                       "  8             2                4       2\n"
                                       "  9             2                4       2\n"
                                       "  10            3                4       3\n"
                                       "  11            3                4       3\n"
                                       "  12            3                4       3\n"
                                       "  13            3                4       3       2\n"
                                       "  14            3                4       3       2\n"
                                       "  15            3                4       3       2\n"
                                       "  16            3                4       3       3\n"
                                       "  17            3                4       3       3\n"
                                       "  18            3                4       3       3\n"
                                       "  19            3                4       3       3       1\n"
                                       "  20            3                4       3       3       1\n"
                                       "\n\n"
                               "Spells Known of 1st Level and Higher: You know three 1st-level wizard spells of your choice, two of which you must choose from the abjuration and evocation spells on the wizard spell list. The Spells Known column of the Eldritch Knight Spellcasting table shows when you learn more wizard spells of 1st level or higher. Each of these spells must be an abjuration or evocation spell of your choice, and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level. The spells you learn at 8th, 14th, and 20th level can come from any school of magic. Whenever you gain a level in this class, you can replace one of the wizard spells you know with another spell of your choice from the wizard spell list. The new spell must be of a level for which you have spell slots, and it must be an abjuration or evocation spell, unless you're replacing the spell you gained at 3rd, 8th, 14th, or 20th level from any school of magic.\n"
                               "Spellcasting Ability: Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one. Spell save DC = 8 + your proficiency bonus + your Intelligence modifier.Spell attack modifier = your proficiency bonus + your Intelligence modifier\n"
                               "Weapon Bond: At 3rd level, you learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond. Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand. You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two.")

            if martial_archetype == 8:
                PC_subclass = "Psi Warrior"
                class_feature4 = ("Psionic Power: At 3rd level, you harbor a wellspring of psionic energy within yourself. This energy is represented by your Psionic Energy dice, which are each a d6. You have a number of these dice equal to twice your proficiency bonus, and they fuel various psionic powers you have, which are detailed below. Some of your powers expend the Psionic Energy die they use, as specified in a power's description, and you can't use a power if it requires you to use a die when your dice are all expended. You regain all your expended Psionic Energy dice when you finish a long rest. In addition, as a bonus action, you can regain one expended Psionic Energy die, but you can't do so again until you finish a short or long rest.  When you reach certain levels in this class, the size of your Psionic Energy dice increases: at 5th level (d8), 11th level (d10), and 17th level (d12). The powers below use your Psionic Energy dice.\n"
                                "   Protective Field: When you or another creature you can see within 30 feet of you takes damage, you can use your reaction to expend one Psionic Energy die, roll the die, and reduce the damage taken by the number rolled plus your Intelligence modifier (minimum reduction of 1), as you create a momentary shield of telekinetic force.\n"
                                "   Psionic Strike: You can propel your weapons with psionic force. Once on each of your turns, immediately after you hit a target within 30 feet of you with an attack and deal damage to it with a weapon, you can expend one Psionic Energy die, rolling it and dealing force damage to the target equal to the number rolled plus your Intelligence modifier.\n"
                                "   Telekinetic Movement: You can move an object or a creature with your mind. As an action, you target one loose object that is Large or smaller or one willing creature, other than yourself. If you can see the target and it is within 30 feet of you, you can move it up to 30 feet to an unoccupied space you can see. Alternatively, if it is a Tiny object, you can move it to or from your hand. Either way, you can move the target horizontally, vertically, or both. Once you take this action, you can't do so again until you finish a short or long rest, unless you expend a Psionic Energy die to take it again.")

            if martial_archetype == 9:
                PC_subclass = "Rune Knight"
                global giant
                giant = 1
                class_feature4 = ("Bonus Proficiencies: You gain proficiency with smith’s tools\n"
                                  "Rune Carver: Starting at 3rd level, you can use magic runes to enhance your gear. You learn two runes of your choice, from among the runes described below, and each time you gain a level in this class, you can replace one rune you know with a different one from this feature. When you reach certain levels in this class, you learn additional runes, as shown in the Runes Known table."
                                  "Rune Table:\n    3rd level: 2 runes known\n    7th level: 3 runes known\n    10th level: 4 runes known\n    15th level: 5 runes known\n"
                                  "Whenever you finish a long rest, you can touch a number of objects equal to the number of runes you know, and you inscribe a different rune onto each of the objects. To be eligible, an object must be a weapon, a suit of armor, a shield, a piece of jewelry, or something else you can wear or hold in a hand. Your rune remains on an object until you finish a long rest, and an object can bear only one of your runes at a time. The following runes are available to you when you learn a rune. If a rune has a level requirement, you must be at least that level in this class to learn the rune. If a rune requires a saving throw, your Rune Magic save DC equals 8 + your proficiency bonus + your Constitution modifier.\n"
                                  "    Cloud Rune: This rune emulates the deceptive magic used by some cloud giants. While wearing or carrying an object inscribed with this rune, you have advantage on Dexterity (Sleight of Hand) checks and Charisma (Deception) checks. In addition, when you or a creature you can see within 30 feet of you is hit by an attack roll, you can use your reaction to invoke the rune and choose a different creature within 30 feet of you, other than the attacker. The chosen creature becomes the target of the attack, using the same roll. This magic can transfer the attack's effects regardless of the attack's range. Once you invoke this rune, you can't do so again until you finish a short or long rest.\n"
                                  "    Fire Rune: This rune's magic channels the masterful craftsmanship of great smiths. While wearing or carrying an object inscribed with this rune, your proficiency bonus is doubled for any ability check you make that uses your proficiency with a tool. In addition, when you hit a creature with an attack using a weapon, you can invoke the rune to summon fiery shackles: the target takes an extra 2d6 fire damage, and it must succeed on a Strength saving throw or be restrained for 1 minute. While restrained by the shackles, the target takes 2d6 fire damage at the start of each of its turns. The target can repeat the saving throw at the end of each of its turns, banishing the shackles on a success. Once you invoke this rune, you can't do so again until you finish a short or long rest.\n"
                                  "    Frost Rune: This rune's magic evokes the might of those who survive in the wintry wilderness, such as frost giants. While wearing or carrying an object inscribed with this rune, you have advantage on Wisdom (Animal Handling) checks and Charisma (Intimidation) checks. In addition, you can invoke the rune as a bonus action to increase your sturdiness. For 10 minutes, you gain a +2 bonus to all ability checks and saving throws that use Strength or Constitution. Once you invoke this rune, you can't do so again until you finish a short or long rest.\n"
                                  "    Stone Rune: This rune's magic channels the judiciousness associated with stone giants. While wearing or carrying an object inscribed with this rune, you have advantage on Wisdom (Insight) checks, and you have darkvision out to a range of 120 feet. In addition, when a creature you can see ends its turn within 30 feet of you, you can use your reaction to invoke the rune and force the creature to make a Wisdom saving throw. Unless the save succeeds, the creature is charmed by you for 1 minute. While charmed in this way, the creature has a speed of 0 and is incapacitated, descending into a dreamy stupor. The creature repeats the saving throw at the end of each of its turns, ending the effect on a success. Once you invoke this rune, you can't do so again until you finish a short or long rest.\n"
                                  "    Hill Rune (7th Level or Higher): This rune's magic bestows a resilience reminiscent of a hill giant. While wearing or carrying an object that bears this rune, you have advantage on saving throws against being poisoned, and you have resistance against poison damage. In addition, you can invoke the rune as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage for 1 minute. Once you invoke this rune, you can't do so again until you finish a short or long rest.\n"
                                  "    Storm Rune (7th Level or Higher): Using this rune, you can glimpse the future like a storm giant seer. While wearing or carrying an object inscribed with this rune, you have advantage on Intelligence (Arcana) checks, and you can't be surprised as long as you aren't incapacitated. In addition, you can invoke the rune as a bonus action to enter a prophetic state for 1 minute or until you're incapacitated. Until the state ends, when you or another creature you can see within 60 feet of you makes an attack roll, a saving throw, or an ability check, you can use your reaction to cause the roll to have advantage or disadvantage. Once you invoke this rune, you can't do so again until you finish a short or long rest.\n"
                                  "Giant Might: At 3rd level, you have learned how to imbue yourself with the might of giants. As a bonus action, you magically gain the following benefits, which last for 1 minute: If you are smaller than Large, you become Large, along with anything you are wearing. If you lack the room to become Large, your size doesn't change, Yu have advantage on Strength checks and Strength saving throws, amd once on each of your turns, one of your attacks with a weapon or an unarmed strike can deal an extra 1d6 damage to a target on a hit. You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses of it when you finish a long rest.")


            if martial_archetype == 10:
                PC_subclass = "Samurai"
                class_feature4 = ("Bonus Proficiency: When you choose this archetype at 3rd level, you gain proficiency in one of the following skills of your choice: History, Insight, Performance, or Persuasion. Alternatively, you learn one language of your choice.\n"
                                  "Fighting Spirit: Starting at 3rd level, your intensity in battle can shield you and help you strike true. As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain 5 temporary hit points. The number of hit points increases when you reach certain levels in this class, increasing to 10 at 10th level and 15 at 15th level. You can use this feature three times. You regain all expended uses of it when you finish a long rest.")


            if martial_archetype == 11:
                PC_subclass = "Renegade"
                global deception
                global sleight_of_hand

                #Accounts for Scoundrel's Wit
                if deception == 1:
                    sleight_of_hand = 1
                    persuasion = 1

                if persuasion == 1:
                    sleight_of_hand = 1
                    deception = 1

                if sleight_of_hand == 1:
                    persuasion = 1
                    deception = 1

                else:
                    skill_1_and_2 = randint(1,3)
                    if skill_1_and_2 == 1:
                        deception = 1
                        persuasion = 1

                    if skill_1_and_2 == 2:
                        deception = 1
                        sleight_of_hand = 1

                    if skill_1_and_2 == 3:
                        persuasion = 1
                        sleight_of_hand = 1

                class_feature4 = ("Gunfighter's Form: When you choose this archetype at 3rd level, you begin constructing a custom firearm that suits your unique brand of renegade style. This process begins by selecting the form upon which to base your weapon. Each form grants you a new ability and unlocks certain upgrades you can add to your weapon at higher levels. Choose one of the following options:\n"
                                  "     Pistoleer: Favoring speed and style over raw power, a renegade who adopts the Pistoleer form wields a small flintlock handgun. As an action on your turn, you can target a creature within 30 feet and shoot. Make a ranged attack roll against the target. You are proficient with the attack, and on a hit, the attack deals piercing damage equal to 1d6 + your Dexterity modifier. The number of shots you can fire during a single action increases when you reach higher levels in this subclass: two shots at 5th level, three shots at 11th level, and four shots at 20th level. The shots can target the same creature or different creatures. Make a separate attack roll for each shot.\n"
                                  "     Sniper: Armed with a large two-handed firearm, a renegade who adopts the Sniper form can inflict massive damage in a single shot. As an action on your turn, you can target a creature within 120 feet and shoot. Make a ranged attack roll against the target. You are proficient with the attack, and on a hit, the attack deals piercing damage equal to 1d10 + your Dexterity modifier. You deal extra damage while using this form when you reach higher levels, dealing damage equal to 2d10 + your Dexterity modifier at 5th level, 4d10 at 11th level, and 6d10 at 20th level.\n"
                                  "Weapon of Choice: Through a combination of salvaging stolen pieces of arcane technology and sheer rakish ingenuity, you can customize your firearm with various upgrades. When you choose this archetype at 3rd level, pick one minor upgrade and one major upgrade from the Firearm Upgrades list. If an upgrade has a prerequisite, you must meet that prerequisite in order to benefit from the upgrade. You gain one additional minor upgrade at 5th level, and one additional major upgrade at 10th level. Saving Throws: Some of these upgrades require your targets to make a saving throw to resist the effect. The saving throw DC is calculated as follows: Firearm Upgrade save DC = 8 + your proficiency bonus + your Charisma modifier"
                                  "Minor Upgrades:\n"
                                  "     Blade and Black Powder: Prerequisite: Pistoleer Form, You create a matching blade to accompany your firearm, rendering you a deadly opponent in both melee and ranged combat. Being within 5 feet of a hostile creature doesn’t impose disadvantage on your ranged attack rolls. Additionally, when you use your action to shoot using your Gunfighter Form, you can use your bonus action to strike at a creature within melee range. Make a melee attack roll. The attack roll uses your Dexterity modifier, and you are proficient with the attack. On a hit, the attack deals slashing damage equal to 1d6 + your Dexterity modifier.\n"
                                  "     Caliber Net: By repurposing some salvaged Hextech parts, you equip your gun with an arcane net meant to trap opponents. As an action, choose a creature within range of your firearm. The creature must succeed on a Strength saving throw or be restrained. At the end of each of its turns, the target can repeat this saving throw, ending the effect on a success. Once you use this feature, you cannot use it again until you finish a short or long rest.\n"
                                  "     Collateral Damage: Prerequisite: Sniper Form, You alter your ammunition to have explosive capabilities. When you hit a target with a successful attack from your firearm, all creatures within 5 feet of the target must succeed on a Dexterity saving throw or take 1d6 piercing damage.\n"
                                  "     Crosshairs: Prerequisite: 5th level, You equip your firearm with a targeting mechanism. If you haven't moved this turn, you can aim down your sights as a bonus action, reducing your speed to 0 and granting you advantage on all attacks you make using your Gunfighter's Form feature until the end of your turn.\n"
                                  "     Double-Barrel: Prerequisite: Sniper Form, 5th level, You add a second barrel to your firearm. When you use your Gunfighter Form, you can shoot twice during a single action, instead of once. The shots can target the same creature or different creatures. Make a separate attack roll for each shot.\n"
                                  "     Smoke Screen: As an action, you alter the firing mechanism of your gun to release a burst of ash and smoke. This cloud forms a 10-foot cube centered on a point of your choice within the firearm’s range, spreading around corners, and the area covered by this cube is considered heavily obscured. This smoke lasts for 10 minutes and cannot be dispersed. Once you use this feature, you cannot use it again until you finish a short or long rest.\n"
                                  "Major Upgrades:\n"
                                  "Barrage: As an action, you can fire a barrage of bullets. Each creature in a 15-foot cone originating from yourself must make a Dexterity saving throw, taking piercing damage equal to 3d10 + your Dexterity modifier on a failure and half as much on a success. Once you use this feature, you cannot use it again until you finish a short or long rest.\n"
                                  "Double Up: When you hit a creature with a successful ranged weapon attack with a firearm, you can immediately cause the bullet to hit another creature within 15 feet of the original target. The second target takes piercing damage equal to your Dexterity modifier (minimum of one). You can redirect a bullet in this way a number of times equal to your Charisma modifier, and regain all expended uses after a short or long rest\n"
                                  "Lightning Round: You equip your firearm with a volatile piece of stolen Hextech, allowing you to release a piercing bolt of electricity as an action on your turn. The lightning fires from you in a straight line that is 1 foot wide and 30 feet long. Each creature in the line must make a Dexterity saving throw, taking 3d8 lightning damage on a failure and half as much on a success. Once you use this feature, you cannot use it again until you finish a short or long rest.\n"
                                  "Trial by Fire: As a bonus action, you can charge your weapons with blazing force. Until the start of your next turn, whenever you make a successful attack, you deal extra fire damage equal to half your fighter level, rounded up. You can charge your weapons this way a number of times equal to your Charisma modifier (minimum of once), and regain all uses after a short or long rest.")

            
            if martial_archetype == 12:
                PC_subclass = "Gunslinger"
                class_feature4 = ("Firearm Proficiency: Starting when you choose this archetype at 3rd level, you gain proficiency with firearms, allowing you to add your proficiency bonus to attacks made with firearms.\n"
                                  "Gunsmith: Upon choosing this archetype at 3rd level, you gain proficiency with Tinker’s Tools. You may use them to craft ammunition at half the cost, repair damaged firearms, or even draft and create new ones (DM’s discretion). Some extremely experimental and intricate firearms are only available through crafting."
                                  "Firearm Properties: Firearms are a new and volatile technology, and as such bring their own unique set of weapon properties. Some properties are followed by a number, and this number signifies an element of that property. These properties replace the optional ones presented in the Dungeon Master’s Guide. Firearms are ranged weapons."
                                  "Adept Marksman: When you choose this archetype at 3rd level, you learn to perform powerful trick shots to disable or damage your opponents using your firearms.\n"
                                  "     Trick Shots. You learn two trick shots of your choice. Many maneuvers enhance an attack in some way. Each use of a trick shot must be declared before the attack roll is made. You can use only one trick shot per attack. You learn an additional trick shot of your choice at 7th, 10th, 15th, and 18th level. Each time you learn a new trick shot, you can also replace one trick shot you know with a different one.\n"
                                  "     Grit. You gain a number of grit points equal to your Wisdom modifier (minimum of 1). You regain 1 expended grit point each time you roll a 20 on the d20 roll for an attack with a firearm, or deal a killing blow with a firearm to a creature of significant threat (DM’s discretion). You regain all expended grit points after a short or long rest.\n"
                                  "     Saving Throws. Some of your trick shots require your targets to make a saving throw to resist the trick shot’s effects. The saving throw DC is calculated as follows: Trick shot save DC = 8 + your proficiency bonus + your Dexterity modifier\n"
                                  "Weapon Properties Table\n"
                                  "Name 	    Cost 	  Ammo 	     Damage 	     Weight 	Range 	  Properties\n"
                                  "Palm Pistol  50gp      2gp (20)   1d8 piercing    1 lb. 	    40/160 	  Light, reload 1, misfire 1\n"
                                  "Pistol 	    150 gp 	  4 gp (20)  1d10 piercing   3 lb. 	    60/240 	  Reload 4, misfire 1\n"
                                  "Musket 	    300 gp 	  5 gp (20)  1d12 piercing   10 lb. 	120/480   Two-handed, reload 1, misfire 2\n"
                                  "Pepperbox 	250 gp    4 gp (20)  1d10 piercing   5 lb. 	    80/320 	  Reload 6, misfire 2\n"
                                  "Blunderbuss 	300 gp 	  5 gp (5)   2d8 piercing 	 10 lb. 	15/60 	  Reload 1, misfire 2\n"
                                  "Bad News 	Crafted   10 gp (5)  2d12 piercing   25 lb. 	200/800   Two-handed, reload 1, misfire 3\n"
                                  "Hand Mortar 	Crafted   10 gp (1)  2d8 fire 	     10 lb. 	30/600 	  Reload 1, misfire 3, explosive\n\n"
                                  "Trick Shots Table\n"
                                  "     Bullying Shot: You can use the powerful blast and thundering sound of your firearm to shake the resolve of a creature. You can expend one grit point while making a Charisma (Intimidation) check to gain advantage on the roll.\n"
                                  "     Dazing Shot: When you make a firearm attack against a creature, you can expend one grit point to attempt to dizzy your opponent. On a hit, the creature suffers normal damage and must make a Constitution saving throw or suffer disadvantage on attacks until the end of their next turn.\n"
                                  "     Deadeye Shot: When you make a firearm attack against a creature, you can expend one grit point to gain advantage on the attack roll.\n"
                                  "     Disarming Shot: When you make a firearm attack against a creature, you can expend one grit point to attempt to shoot an object from their hands. On a hit, the creature suffers normal damage and must succeed on a Strength saving throw or drop 1 held object of your choice and have that object be pushed 10 feet away from you.\n"
                                  "     Forceful Shot: When you make a firearm attack against a creature, you can expend one grit point to attempt to trip them up and force them back. On a hit, the creature suffers normal damage and must succeed on a Strength saving throw or be pushed 15 feet away from you.\n"
                                  "     Piercing Shot: When you make a firearm attack against a creature, you can expend one grit point to attempt to fire through multiple opponents. The initial attack gains a +1 to the firearm’s misfire score. On a hit, the creature suffers normal damage and you make an attack roll with disadvantage against every creature in a line directly behind the target within your first range increment. Only the initial attack can misfire.\n"
                                  "     Violent Shot: When you make a firearm attack against a creature, you can expend one or more grit points to enhance the volatility of the attack. For each grit point expended, the attack gains a +2 to the firearm’s misfire score. If the attack hits, you can roll one additional weapon damage die per grit point spent when determining the damage.\n"
                                  "     Winging Shot: When you make a firearm attack against a creature, you can expend one grit point to attempt to topple a moving target. On a hit, the creature suffers normal damage and must make a Strength saving throw or be knocked prone.\n")

        if PC_level >= 4:
            feat1 = ability_score_improvement();
            class_feature5 = "Martial Versatility: Whenever you reach a level in this class that grants the Ability Score Improvement feature (4,6,8,12,14,16,19) you can do one of the following, as you shift the focus of your martial practice: Replace a fighting style you know with another fighting style available to fighters and/or If you know any maneuvers from the Battle Master archetype, you can replace one maneuver you know with a different maneuver."

        if PC_level >= 5:
            PC_prof_bonus = 3
            class_feature6 = "Extra Attack: Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class."

        if PC_level >= 6:
            feat2 = ability_score_improvement();

        if PC_level >= 7:

            if martial_archetype == 1:
                class_feature7 = ("Magic Arrow: At 7th level, you gain the ability to infuse arrows with magic. Whenever you fire a nonmagical arrow from a shortbow or longbow, you can make it magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. The magic fades from the arrow immediately after it hits or misses its target."
                                  "Curving Shot: At 7th level, you learn how to direct an errant arrow toward a new target. When you make an attack roll with a magic arrow and miss, you can use a bonus action to reroll the attack roll against a different target within 60 feet of the original target.")

            if martial_archetype == 2:
                class_feature7 = "Royal Envoy: At 7th level, you gain proficiency in the Persuasion skill. If you are already proficient in it, you gain proficiency in one of the following skills of your choice: Animal Handling, Insight, Intimidation, or Performance. Your proficiency bonus is doubled for any ability check you make that uses Persuasion. You receive this benefit regardless of the skill proficiency you gain from this feature."

            if martial_archetype == 3:
                class_feature7 = "Know Your Enemy: Starting at 7th level, if you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Strength, Dexterity, or Constitution score, Armor class, current hp, total class levels (if any), or fighter class levels, if any"

            if martial_archetype == 4:
                class_feature7 = "Warding Maneuver: At 7th level, you learn to fend off strikes directed at you, your mount, or other creatures nearby. If you or a creature you can see within 5 feet of you is hit by an attack, you can roll 1d8 as a reaction if you're wielding a melee weapon or a shield. Roll the die, and add the number rolled to the target's AC against that attack. If the attack still hits, the target has resistance against the attack's damage. You can use this feature a number of times equal to your Constitution modifier (a minimum of once), and you regain all expended uses of it when you finish a long rest."

            if martial_archetype == 5:
                class_feature7 = "Remarkable Athlete: Starting at 7th level, you can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."

            if martial_archetype == 6:
                class_feature7 = "Echo Avatar: Starting at 7th level, you can temporarily transfer your consciousness to your echo. As an action, you can see through your echo's eyes and hear through its ears. During this time, you are deafened and blinded. You can sustain this effect for up to 10 minutes, and you can end it at any time (requires no action). While your echo is being used in this way, it can be up to 1,000 feet away from you without being destroyed."

            if martial_archetype == 7:
                class_feature7 = "War Magic: Beginning at 7th level, when you use your action to cast a cantrip, you can make one weapon attack as a bonus action."

            if martial_archetype == 8:
                class_feature7 = "Telekinetic Adept: By the 7th level, You have mastered new ways to use your telekinetic abilities, detailed below.\nPsi-Powered Leap: As a bonus action, you can propel your body with your mind. You gain a flying speed equal to twice your walking speed until the end of the current turn. Once you take this bonus action, you can't do so again until you finish a short or long rest, unless you expend a Psionic Energy die to take it again.\nTelekinetic Thrust: When you deal damage to a target with your Psionic Strike, you can force the target to make a Strength saving throw against a DC equal to 8 + your proficiency bonus + your Intelligence modifier. If the save fails, you can knock the target prone or move it up to 10 feet in any direction horizontally."

            if martial_archetype == 9:
                class_feature7 = "Runic Shield: At 7th level, you learn to invoke your rune magic to protect your allies. When another creature you can see within 60 feet of you is hit by an attack roll, you can use your reaction to force the attacker to reroll the d20 and use the new roll. You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."

            if martial_archetype == 10:
                class_feature7 = "Elegant Courtier: Starting at 7th level, your discipline and attention to detail allow you to excel in social situations. Whenever you make a Charisma (Persuasion) check, you gain a bonus to the check equal to your Wisdom modifier. Your self-control also causes you to gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice)."

            if martial_archetype == 11:
                class_feature7 = "Cunning Shot: Starting at 7th level, you learn to exploit a foe’s weak spots, even if they appear to have none. The damage dealt by your firearm, including damage dealt via Firearm Upgrades, ignores resistances and immunities."

            if martial_archetype == 12:
                class_feature7 = "Quickdraw: When you reach 7th level, you add your proficiency bonus to your initiative. You can also stow a firearm, then draw another firearm as a single object interaction on your turn."

        if PC_level >= 8:
            feat3 = ability_score_improvement();

        if PC_level >= 9:
            PC_prof_bonus = 4
            class_feature8 = "Indomitable: Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."

        if PC_level >= 10:

            if martial_archetype == 1:
                class_feature9 = " "
                #Arcane Archer only gets a new shot type, no new skill

            if martial_archetype == 2:
                class_feature9 = "Inspiring Surge: Starting at 10th level, when you use your Action Surge feature, you can choose one creature within 60 feet of you that is allied with you. That creature can make one melee or ranged weapon attack with its reaction, provided that it can see or hear you. Starting at 18th level, you can choose two allies within 60 feet of you, rather than one."

            if martial_archetype == 3:
                class_feature9 = "Improved Combat Superiority: At 10th level, your superiority dice turn into d10s. At 18th level, they turn into d12s."

            if martial_archetype == 4:
                class_feature9 = "Hold the Line: At 10th level, you become a master of locking down your enemies. Creatures provoke an opportunity attack from you when they move 5 feet or more while within your reach, and if you hit a creature with an opportunity attack, the target's speed is reduced to 0 until the end of the current turn."

            if martial_archetype == 5:
                class_feature9 = "Additional Fighting Style: At 10th level, you can choose a second option from the Fighting Style class feature."

            if martial_archetype == 6:
                class_feature9 = "Shadow Martyr: Starting at 10th level, you can make your echo throw itself in front of an attack directed at another creature that you can see. Before the attack roll is made, you can use your reaction to teleport the echo to an unoccupied space within 5 feet of the targeted creature. The attack roll that triggered the reaction is instead made against your echo. Once you use this feature, you can't use it again until you finish a short or long rest."

            if martial_archetype == 7:
                class_feature9 = "Eldritch Strike: At 10th level, you learn how to make your weapon strikes undercut a creature's resistance to your spells. When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."

            if martial_archetype == 8:
                class_feature9 = "Guarded Mind: Starting at 10th level, the psionic energy flowing through you has bolstered your mind. You have resistance to psychic damage. Moreover, if you start your turn charmed or frightened, you can expend a Psionic Energy die and end every effect on yourself subjecting you to those conditions."

            if martial_archetype == 9:
                class_feature9 = "Great Stature: By 10th level, the magic of your runes permanently alters you. When you gain this feature, roll 3d4. You grow a number of inches in height equal to the roll. Moreover, the extra damage you deal with your Giant's Might feature increases to 1d8."

            if martial_archetype == 10:
                class_feature9 = "Tireless Spirit: Starting at 10th level, when you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."

            if martial_archetype == 11:
                class_feature9 = "Grin and Bear It: At 10th level, you can brace yourself in the heat of battle, even when gravely wounded. When you use your Second Wind feature, your AC gains a +1 bonus and your movement speed increases by 10 feet until the start of your next turn."

            if martial_archetype == 12:
                class_feature9 = "Rapid Repair: Upon reaching 10th level, you learn how to quickly attempt to fix a jammed gun. You can spend a grit point to attempt to repair a misfired (but not broken) firearm as a bonus action."

        #Level 11 just gives Extra attack x2

        if PC_level >= 12:
            feat4 = ability_score_improvement();

        if PC_level >= 13:
            PC_prof_bonus = 5

        if PC_level >= 14:
            feat5 = ability_score_improvement();

        if PC_level >= 15:
            if martial_archetype == 1:
                class_feature10 = "Ever-Ready Shot: Starting at 15th level, your magical archery is available whenever battle starts. If you roll initiative and have no uses of Arcane Shot remaining, you regain one use of it."

            if martial_archetype == 2:
                class_feature10 = "Bulwark: Beginning at 15th level, you can extend the benefit of your Indomitable feature to an ally. When you decide to use Indomitable to reroll an Intelligence, a Wisdom, or a Charisma saving throw and you aren't incapacitated, you can choose one ally within 60 feet of you that also failed its saving throw against the same effect. If that creature can see or hear you, it can reroll its saving throw and must use the new roll."

            if martial_archetype == 3:
                class_feature10 = "Relentless: Starting at 15th level, when you roll initiative and have no superiority dice remaining, you regain 1 superiority die."

            if martial_archetype == 4:
                class_feature10 = "Ferocious Charger: Starting at 15th level, you can run down your foes, whether you're mounted or not. If you move at least 10 feet in a straight line right before attacking a creature and you hit it with the attack, that target must succeed on a Strength saving throw (DC 8 + your proficiency bonus + your Strength modifier) or be knocked prone. You can use this feature only once on each of your turns."

            if martial_archetype == 5:
                class_feature10 = "Superior Critical: Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20."

            if martial_archetype == 6:
                class_feature10 = "Reclaim Potential: By 15th level, you've learned to absorb the fleeting magic of your echo. When an echo of yours is destroyed by taking damage, you can gain a number of temporary hit points equal to 2d6 + your Constitution modifier, provided you don't already have temporary hit points. You can use this feature a number of times equal to your Constitution modifier (a minimum of once). You regain all expended uses when you finish a long rest."

            if martial_archetype == 7:
                class_feature10 = "Arcane Charge: At 15th level, you gain the ability to teleport up to 30 feet to an unoccupied space you can see when you use your Action Surge. You can teleport before or after the additional action."

            if martial_archetype == 8:
                class_feature10 = "Bulwark of Force: At 15th level, you can shield yourself and others with telekinetic force. As a bonus action, you can choose creatures, which can include you, that you can see within 30 feet of you, up to a number of creatures equal to your Intelligence modifier (minimum of one creature). Each of the chosen creatures is protected by half cover for 1 minute or until you're incapacitated. Once you take this bonus action, you can't do so again until you finish a long rest, unless you expend a Psionic Energy die to take it again"

            if martial_archetype == 9:
                class_feature10 = "Master of Runes: At 15th level, you can invoke each rune you know from your Rune Carver feature twice, rather than once, and you regain all expended uses when you finish a short or long rest."

            if martial_archetype == 10:
                class_feature10 = "Rapid Strike: Starting at 15th level, you learn to trade accuracy for swift strikes. If you take the Attack action on your turn and have advantage on an attack roll against against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."

            if martial_archetype == 11:
                class_feature10 = "Right Gun for the Job: At 15th level, your skill with your firearm can adapt to any situation. When you finish a long rest, you can replace any of your Firearm Upgrades with a different one, though you cannot have more than two major upgrades equipped at a time. You must still meet the prerequisite of an upgrade in order to benefit from it."

            if martial_archetype == 12:
                class_feature10 = "Lightning Reload: Starting at 15th level, you can reload any firearm as a bonus action."

        if PC_level >= 16:
            feat6 = ability_score_improvement();

        if PC_level >= 17:
            PC_prof_bonus = 6

        if PC_level >= 18:

            if martial_archetype == 1:
               class_feature10 = ""
               #Arcane Shots get upgraded here, already inccluded

            if martial_archetype == 2:
                class_feature10 = ""
                #Inspiring Surge upgraded already

            if martial_archetype == 3:
                class_feature10 = ""
                #Nothing

            if martial_archetype == 4:
                class_feature10 = "Vigilant Defender: Starting at 18th level, you respond to danger with extraordinary vigilance. In combat, you get a special reaction that you can take once on every creature's turn, except your turn. You can use this special reaction only to make an opportunity attack, and you can't use it on the same turn that you take your normal reaction."

            if martial_archetype == 5:
                class_feature10 = "Survivor: At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."

            if martial_archetype == 6:
                class_feature10 = "Legion of One: At 18th level, you can use a bonus action to create two echos with your Manifest Echo feature, and these echoes can co-exist. If you try to create a third echo, the previous two echoes are destroyed. Anything you can do from one echo's position can be done from the other's instead. In addition, when you roll initiative and have no uses of your Unleash Incarnation feature left, you regain one use of that feature."

            if martial_archetype == 7:
                class_feature10 = "Improved War Magic: Starting at 18th level, when you use your action to cast a spell, you can make one weapon attack as a bonus action."

            if martial_archetype == 8:
                class_feature10 = "Telekinetic Master: By 18th level, your ability to move creatures and objects with your mind is matched by few. You can cast the Telekinesis spell, requiring no components, and your spellcasting ability for the spell is Intelligence. On each of your turns while you concentrate on the spell, including the turn when you cast it, you can make one attack with a weapon as a bonus action. Once you cast the spell with this feature, you can't do so again until you finish a long rest, unless you expend a Psionic Energy die to cast it again."

            if martial_archetype == 9:
                class_feature10 = "Runic Juggernaut: At 18th level, you learn how to amplify your rune-powered transformation. As a result, the extra damage you deal with the Giant's Might feature increases to 1d10. Moreover, when you use that feature, your size can increase to Huge, and while you are that size, your reach increases by 5 feet."

            if martial_archetype == 10:
                class_feature10 = "Strength Before Death: Starting at 18th level, your fighting spirit can delay the grasp of death. If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points. Once you use this feature, you can’t use it again until you finish a long rest."

            if martial_archetype == 11:
                class_feature10 = "Light ‘Em Up: At 18th level, you learn to channel the volatile force of your firearm’s black powder into a single concussive blast. As a bonus action, you can either throw or set down a small explosive. If thrown, the explosive has a range of 30 feet and detonates immediately on impact; if set down, the explosive can be detonated remotely from up to 60 feet away as another bonus action. hen detonated, each creature within a 15-foot radius of the explosive must make a Dexterity saving throw, taking 12d6 force damage on a failure and half as much on a success. The DC for this saving throw is equal to your Firearm Upgrade DC. Once you use this feature, you cannot use it again until you complete a short or long rest."

            if martial_archetype == 12:
                class_feature10 = "Vicious Intent: At 18th level, your firearm attacks score a critical hit on a roll of 19-20, and you regain a grit point on a roll of 19 or 20 on a d20 attack roll.\nHemorrhaging Critical: Upon reaching 18th level, whenever you score a critical hit on an attack with a firearm, the target additionally suffers half of the damage from the attack at the end of its next turn."

        if PC_level >= 19:
            #Level 19 is end, 20 gives extra attack x3
            feat7 = ability_score_improvement();
        
    if PC_class == "Monk":
       hit_dice = "1d8 per monk level"
       first_lvl_hp = 8 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
           temp = randint(1,8)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1

       PC_hp = first_lvl_hp + high_lvl_hp
       shortsword = 1
       simple_weapons = 1

       PC_dex_savethrw = 1
       PC_str_savethrw = 1

       skill1 = randint(1,6)
       if skill1 == 1:
           acrobatics = 1
       if skill1 == 2:
           religion = 1
       if skill1 == 3:
             athletics = 1
       if skill1 == 4:
            history = 1
       if skill1 == 5:
           insight = 1
       if skill1 == 6:
            stealth = 1

       skill2 = randint(1,6)
       while skill1 == skill2:
            skill2 = randint(1,6)

       if skill1 == 1:
           acrobatics = 1
       if skill1 == 2:
           religion = 1
       if skill1 == 3:
             athletics = 1
       if skill1 == 4:
            history = 1
       if skill1 == 5:
           insight = 1
       if skill1 == 6:
            stealth = 1


 
       equipment = randint(2,3)
       if equipment == 2:
           class_equipment = "A shortsword"
       if equipment == 3:
           class_equipment = "Any simple weapon"
       equipment = randint(1,2)
       if equipment == 1:
           class_equipment2 = "A dungeoneer's pack"
       if equipment == 2:
           class_equipment2 = "An explorer's pack"

       class_equipment3 = "10 darts"
       
       class_feature1 = "Unarmored Defense: Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.\nMartial Arts: At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property. You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield:\n  You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.\n   You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. (This die changes to a a d6 at level 5, a d8 at level 11, and a d10 at level 17)\n   When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn.\nCertain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon on the Weapons page."
          
       if PC_level >= 2:
            class_feature2 = "Ki: Starting at 2nd level, your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, starting at 2, and increasing by 1 for each level after 2. You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class. When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points. Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows: Ki save DC = 8 + your proficiency bonus + your Wisdom modifier\n  Flurry of Blows. Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.\n   Patient Defense. You can spend 1 ki point to take the Dodge action as a bonus action on your turn.\n    Step of the Wind. You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn.\nUnarmored Movement: Starting at 2nd level, your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases to 15ft at level 6, to 20ft at level 10, to 25ft at level 14, and to 30ft at level 18. At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move\nDedicated Weapon: Also at 2nd level, you train yourself to use a variety of weapons as monk weapons, not just simple melee weapons and shortswords. Whenever you finish a short or long rest, you can touch one weapon, focus your ki on it, and then count that weapon as a monk weapon until you use this feature again. The chosen weapon must meet these criteria: The weapon must be a simple or martial weapon, you must be proficient with it, and it must lack the heavy and speical properites"
            
       if PC_level >= 3:

           class_feature3 = "Deflect Missiles: Starting at 3rd level, you can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your monk level. If you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack with a range of 20/60 using the weapon or piece of ammunition you just caught, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack.\nKi-Fueled Attack: Also at 3rd level, if you spend 1 ki point or more as part of your action on your turn, you can make one attack with an unarmed strike or a monk weapon as a bonus action before the end of the turn."
           monk_tradition = randint(1,12)

           if monk_tradition == 1:
               PC_subclass = "Way of the Astral Self"
               class_feature4 = "Arms of the Astral Self: At 3rd level, your mastery of your ki allows you to summon a portion of your astral self. As a bonus action, you can spend 1 ki point to summon the arms of your astral self. When you do so, each creature of your choice that you can see within 10 feet of you must succeed on a Dexterity saving throw or take force damage equal to two rolls of your Martial Arts die. For 10 minutes, these spectral arms hover near your shoulders or surround your arms (your choice). You determine the arms' appearance, and they vanish early if you are incapacitated or die. While the spectral arms are present, you gain the following benefits: You can use your Wisdom modifier in place of your Strength modifier when making Strength checks and Strength saving throws, You can use the spectral arms to make unarmed strikes, When you make an unarmed strike with the arms on your turn, your reach for it is 5 feet greater than normal, and The unarmed strikes you make with the arms can use your Wisdom modifier in place of your Strength or Dexterity modifier for the attack and damage rolls, and their damage type is force."

           if monk_tradition == 2:
               PC_subclass = "Way of the Drunken Master"
               class_feature4 = ("Bonus Proficiencies: When you choose this tradition at 3rd level, you gain proficiency in the Performance skill if you don't already have it. Your martial arts technique mixes combat training with the precision of a dancer and the antics of a jester. You also gain proficiency with brewer's supplies if you don't already have it.\n"
                                 "Drunken Technique: At 3rd level, you learn how to twist and turn quickly as part of your Flurry of Blows. Whenever you use Flurry of Blows, you gain the benefit of the Disengage action, and your walking speed increases by 10 feet until the end of the current turn.")
               artisan_tools = 1
               performance =  1

           if monk_tradition == 3:
               PC_subclass = "Way of the Four Elements"
               class_feature4 = ("Disciple of the Elements: When you choose this tradition at 3rd level, you learn magical disciplines that harness the power of the four elements. A discipline requires you to spend ki points each time you use it. You know the Elemental Attunement discipline and one other elemental discipline of your choice. You learn one additional elemental discipline of your choice at 6th, 11th, and 17th level. Whenever you learn a new elemental discipline, you can also replace one elemental discipline that you already know with a different discipline.\n"
                                "Casting elemental spells. Some disiciplines allow you to cast spells. To cast one of these spells, you use its casting time and other rules, but you don't need to provide material components for it. Once you reach 5th level in this class, you can spend additional ki points to increase the level of an elemental discipline spell that you cast, provided that the spell has an enhanced effect at a higher level, as Burning Hands does. The spell's level increases by 1 for each additional ki point you spend. For example, if you are a 5th-level monk and use Sweeping Cinder Strike to cast Burning Hands, you can spend 3 ki points to cast it as a 2nd-level spell (the discipline's base cost of 2 ki points plus 1). The maximum number of ki points you can spend to cast a spell in this way (including its base ki point cost and any additional ki points you spend to increase its level) is determined by your monk level, as shown below:\n      Levels 5-8: 3 Ki points for a spell\n      Levels 9-12: 4 Ki points for a spell\n      Levels 13-16: 5 Ki points for a spell\n      Levels 17-20: 6 Ki points for a spell\n"
                                "Elemental Disciplines:\n"
                                "   Breath of Winter (Requires 17th level): You can spend 6 ki points to cast Cone of Cold.\n"
                                "   Clench of the North Wind (Requires 8th level): You can spend 3 ki points to cast Hold Person.\n"
                                "   Elemental Attunement: You can use your action to briefly control elemental forces within 30 feet of you, causing one of the following effects of your choice: Create a harmless, instantaneous sensory effect related to air, earth, fire, or water such as a shower of sparks, a puff of wind, a spray of light mist, or a gentle rumbling of stone, Instantaneously light or snuff out a candle, a torch, or a small campfire, Chill or warm up to 1 pound of nonliving material for up to 1 hour, Cause earth, fire, water, or mist that can fit within a 1-foot cube to shape itself into a crude form you designate for 1 minute.\n"
                                "   Eternal Mountain Defense (Requires 17th level): You can spend 5 ki points to cast Stoneskin, targeting yourself\n"
                                "   Fangs of the Fire Snake: When you use the Attack action on your turn, you can spend 1 ki point to cause tendrils of flame to stretch out from your fists and feet. Your reach with your unarmed strikes increases by 10 feet for that action, as well as the rest of the turn. A hit with such an attack deals fire damage instead of bludgeoning damage, and if you spend 1 ki point when the attack hits, it also deals an extra 1d10 fire damage\n"
                                "   Fist of Four Thunders: You can spend 2 ki points to cast Thunderwave.\n"
                                "   Fist of Unbroken Air: You can create a blast of compressed air that strikes like a mighty fist. As an action, you can spend 2 ki points and choose a creature within 30 feet of you. That creature must make a Strength saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can push the creature up to 20 feet away from you and knock it prone. On a successful save, the creature takes half as much damage, and you don't push it or knock it prone\n"
                                "   Flames of the Phoenix (Requires 11th level): You can spend 4 ki points to cast Fireball.\n"
                                "   Gong of the Summit (Requires 6th level): You can spend 3 ki points to cast Shatter.\n"
                                "   Mist Stance (Requires 11th level): You can spend 4 ki points to cast Gaseous Form, targeting yourself.\n"
                                "   Ride the Wind (Requires 11th level): You can spend 4 ki points to cast Fly, targeting yourself.\n"
                                "   River of Hungry Flame (Requires 17th level): You can spend 5 ki points to cast Wall of Fire.\n"
                                "   Rush of the Gale Spirits: You can spend 2 ki points to cast Gust of Wind.\n"
                                "   Shape the Flowing River: As an action, you can spend 1 ki point to choose an area of ice or water no larger than 30 feet on a side within 120 feet of you. You can change water to ice within the area and vice versa, and you can reshape ice in the area in any manner you choose. You can raise or lower the ice's elevation, create or fill in a trench, erect or flatten a wall, or form a pillar. The extent of any such changes can't exceed half the area's largest dimension. For example, if you affect a 30-foot square, you can create a pillar up to 15 feet high, raise or lower the square's elevation by up to 15 feet, dig a trench up to 15 feet deep, and so on. You can't shape the ice to trap or injure a creature in the area.\n"
                                "   Sweeping Cinder Strike: You can spend 2 ki points to cast Burning Hands.\n"
                                "   Water Whip: You can spend 2 ki points as an action to create a whip of water that shoves and pulls a creature to unbalance it. A creature that you can see that is within 30 feet of you must make a Dexterity saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can either knock it prone or pull it up to 25 feet closer to you. On a successful save, the creature takes half as much damage, and you don't pull it or knock it prone.\n"
                                "   Wave of Rolling Earth (Requires 17th level): You can spend 6 ki points to cast Wall of Stone.")

           if monk_tradition == 4:
               PC_subclass = "Way of the Kensei"
               class_feature4 = "Path of the Kensei: When you choose this tradition at 3rd level, your special martial arts training leads you to master the use of certain weapons. This path also includes instruction in the deft strokes of calligraphy or painting. You gain the following benefits:\n     Kensei Weapons. Choose two types of weapons to be your kensei weapons: one melee weapon and one ranged weapon. Each of these weapons can be any simple or martial weapon that lacks the heavy and special properties. The longbow is also a valid choice. You gain proficiency with these weapons if you don't already have it. Weapons of the chosen types are monk weapons for you. Many of this tradition's features work only with your kensei weapons. When you reach 6th, 11th, and 17th level in this class, you can choose another type of weapon – either melee or ranged – to be a kensei weapon for you, following the criteria above.\n     Agile Parry. If you make an unarmed strike as part of the Attack action on your turn and are holding a kensei weapon, you can use it to defend yourself if it is a melee weapon. You gain a +2 bonus to AC until the start of your next turn, while the weapon is in your hand and you aren’t incapacitated.\n     Kensei's Shot. You can use a bonus action on your turn to make your ranged attacks with a kensei weapon more deadly. When you do so, any target you hit with a ranged attack using a kensei weapon takes an extra 1d4 damage of the weapon’s type. You retain this benefit until the end of the current turn.\n     Way of the Brush. You gain proficiency with your choice of calligrapher's supplies or painter's supplies."

           if monk_tradition == 5:
               PC_subclass = "Way of the Long Death"
               class_feature4 = "Touch of Death: Starting when you choose this tradition at 3rd level, your study of death allows you to extract vitality from another creature as it nears its demise. When you reduce a creature within 5 feet of you to 0 hit points, you gain temporary hit points equal to your Wisdom modifier + your monk level (minimum of 1 temporary hit point)."

           if monk_tradition == 6:
               PC_subclass = "Way of Mercy"
               class_feature4 = "Implements of Mercy: When you choose this tradition at 3rd level, you gain proficiency in the Insight and Medicine skills, and you gain proficiency with the herbalism kit. You also gain a special mask, which you often wear when using the features of this subclass. You determine its appearance\nHands of Healing: At 3rd level, your mystical touch can mend wounds. As an action, you can spend 1 ki point to touch a creature and restore a number of hit points equal to a roll of your Martial Arts die + your Wisdom modifier. When you use your Flurry of Blows, you can replace one of the unarmed strikes with a use of this feature without spending a ki point for the healing.\nHands of Harm: At 3rd level, you use your ki to inflict wounds. When you hit a creature with an unarmed strike, you can spend 1 ki point to deal extra necrotic damage equal to one roll of your Martial Arts die + your Wisdom modifier. You can use this feature only once per turn."
               herbalism_kit = 1
               insight = 1
               medicine = 1

           if monk_tradition == 7:
               PC_subclass = "Way of the Open Hand"
               class_feature4 = "Open Hand Technique: Starting when you choose this tradition at 3rd level, you can manipulate your enemy's ki when you harness your own. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target: It must succeed on a Dexterity saving throw or be knocked prone or It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you or It can't take reactions until the end of your next turn."

           if monk_tradition == 8:
               PC_subclass = "Way of the Shadow"
               class_feature4 = "Shadow Arts: Starting when you choose this tradition at 3rd level, you can use your ki to duplicate the effects of certain spells. As an action, you can spend 2 ki points to cast Darkness, Darkvision, Pass without Trace, or Silence, without providing material components. Additionally, you gain the Minor Illusion cantrip if you don't already know it."

           if monk_tradition == 9:
               PC_subclass = "Way of the Sun Soul"
               class_feature4 = "Radiant Sun Bolt: Starting when you choose this tradition at 3rd level, you can hurl searing bolts of magical radiance. You gain a new attack option that you can use with the Attack action. This special attack is a ranged spell attack with a range of 30 feet. You are proficient with it, and you add your Dexterity modifier to its attack and damage rolls. Its damage is radiant, and its damage die is a d4. This die changes as you gain monk levels, matching the martial arts die. When you take the Attack action on your turn and use this special attack as part of it, you can spend 1 ki point to make the special attack twice as a bonus action. When you gain the Extra Attack feature, this special attack can be used for any of the attacks you make as part of the Attack action."

           if monk_tradition == 10:
               PC_subclass = "Way of the Cobalt Soul"
               class_feature4 = "Extract Aspects: Beginning at 3rd level when choosing this tradition, you can strike pressure points to extract crucial information about your foe, granting you insight about their combat ability. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you mark them as analyzed. Whenever an analyzed creature misses you with an attack, you can immediately use your reaction to make an unarmed melee attack against that creature. This benefit lasts until you finish a short or long rest. In addition, you learn the following attributes about the target: Damage Vulnerabilities, Damage Resistances, Damage Immunities, and Condition Immunities."

           if monk_tradition == 11:
               PC_subclass = "Way of the Living Weapon"
               class_feature4 = ("Fists of Bone and Steel: At 3rd level, when you choose this tradition, your Martial Arts damage die increases for unarmed strikes. You can roll a d6 in place of the normal damage for your unarmed strike. This die changes to a d8 at 5th level; a d10 at 11th level; and a d12 at 17th level. This increased damage can only be applied to an unarmed strike, and not to a monk weapon."
                                 "Martial Discipline: Starting at 3rd level, when you adopt this tradition, choose a discipline and gain its feature. When you reach 6th level, this slashing damage counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.\n"
                                 "     Forged Heart. Your unarmed strikes are considered adamantine weapons. In addition, when you hit a creature with an unarmed attack, you can spend 1 ki point to cause it to make a Strength saving throw. On a failed save, the creature takes 2d6 additional damage of the same type as the unarmed strike and can be pushed up to 15 feet away from you. On a successful save, the creature only takes 1d6 points of additional damage and is not pushed back.\n"
                                 "     Nightmare Shroud. When you hit a creature with an unarmed attack, you can spend 1 ki point to assail it with fear, causing it to make a Wisdom saving throw. On a failed save, it takes 1d6 points of psychic damage and becomes frightened of you until the end of your next turn. If a creature succeeds on this save, they are immune to the fear effect of this ability for 24 hours.\n"
                                 "     Traveler’s Blade. Your reach extends by 5 feet. Additionally, at the start of your turn you can expend up to 4 ki points to extend your reach further. For every point of ki you spend, your reach extends by an additional 5 feet until the end of your turn.\n"
                                 "     Weretouched. Once per turn, when you hit a creature with an unarmed attack, you can spend 1 ki point to rend your target and inflict deep bleeding wounds. At the start of each of the creature’s turns for the next minute, it takes 1d4 points of slashing damage from this effect. The effect ends early if the creature has one or more hit points restored, if any creature uses its action to expend one use of a healer’s kit, or makes a successful Wisdom (Medicine) check with a DC equal to your ki save DC.\n"
                                 "Mutable Strike: You have the power to alter your natural weapons, growing claws or reinforcing your fists. Starting at 3rd level, when you use Martial Arts to make an unarmed strike, you can choose whether you inflict slashing, bludgeoning, or piercing damage with the attack.")

           if monk_tradition == 12:
               PC_subclass = "Way of the Soul Knife"
               class_feature4 = ("Soul Knives: Starting when you choose this tradition at 3rd level, you can use your psionic energy to manifest blades that disrupt your foes’ minds. Your unarmed strikes deal your choice of psychic, piercing, slashing, or bludgeoning damage each time you hit. In addition, you can use a bonus action to increase the reach of your unarmed strikes by 30 feet until the end of your turn.\n"
                                 "Psychic Slash: At 3rd level, when you channel ki into your attacks you augment your soul knives to inflict devastating psionic blows. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows and that attack inflicts psychic damage, you can impose one of the following effects on the target:\n "
                                 "      Life Drain. You gain temporary hit points equal to half the damage your attack deals.\n"
                                 "      Invoke Terror. The target must succeed on a Wisdom saving throw or become frightened of you until the end of your next turn.\n"
                                 "      Invoke Wrath. The target suffers disadvantage on all attack rolls against targets other than you until the end of your next turn.\n"
                                 "      Astral Slide. You teleport the target up to 10 feet to a destination you can see.\n"
                                 "      Synaptic Overload. The target gains vulnerability to psychic damage until the end of your next turn.")

       if PC_level >= 4:
           class_feature5 = "Slow Fall: Beginning at 4th level, you can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your monk level.\nQuickened Healing: Also at 4th level, as an action, you can spend 2 ki points and roll a Martial Arts die. You regain a number of hit points equal to the number rolled plus your proficiency bonus."
           feat1 = ability_score_improvement();

       if PC_level >= 5:
           PC_prof_bonus = 3
           class_feature6 = "Extra Attack: eginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.\nStunning Strike: Starting at 5th level, you can interfere with the flow of ki in an opponent's body. When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn.\nFocused Aim: Also at 5th level, when you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit."

       if PC_level >= 6:
           class_feature7 = "Ki-Empowered Strikes: Starting at 6th level, your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."

           if monk_tradition == 1:
               class_feature8 = "Visage of the Astral Self: When you reach 6th level, you can summon the visage of your astral self. As a bonus action, or as part of the bonus action you take to activate Arms of the Astral Self, you can spend 1 ki point to summon this visage for 10 minutes. It vanishes early if you are incapacitated or die. The spectral visage covers your face like a helmet or mask. You determine its appearance. While the spectral visage is present, you gain the following benefits:\n      Astral Sight: You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet\n      Wisdom of the Spirit: You have advantage on Wisdom (Insight) and Charisma (Intimidation) checks\n      Word of the Spirit: When you speak, you can direct your words to a creature of your choice that you can see within 60 feet of you, making it so only that creature can hear you. Alternatively, you can amplify your voice so that all creatures within 600 feet can hear you."

           if monk_tradition == 2:
               class_feature8 = "Tipsy Sway: Starting at 6th level, you can move in sudden, swaying ways. You gain the following benefits\n    Leap to Your Feet: When you're prone, you can stand up by spending 5 feet of movement, rather than half your speed\n    Redirect Attack: When a creature misses you with a melee attack roll, you can spend 1 ki point as a reaction to cause that attack to hit one creature of your choice, other than the attacker, that you can see within 5 feet of you."

           if monk_tradition == 3:
               #Everything for Way of Four elements was covered at level 3
               class_feature8 = " "

           if monk_tradition == 4:
               class_feature8 = "One with the Blade: At 6th level, you extend your ki into your kensei weapons, granting you the following benefits\n      Magic Kensei Weapons: Your attacks with your kensei weapons count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage\n      Deft Strike: When you hit a target with a kensei weapon, you can spend 1 ki point to cause the weapon to deal extra damage to the target equal to your Martial Arts die. You can use this feature only once on each of your turns."

           if monk_tradition == 5:
               class_feature8 = "Hour of Reaping: At 6th level, you gain the ability to unsettle or terrify those around you as an action, for your soul has been touched by the shadow of death. When you take this action, each creature within 30 feet of you that can see you must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn."

           if monk_tradition == 6:
               class_feature8 = "Physician's Touch: Starting at 6th level, you can administer even greater cures with a touch, and if you feel it's necessary, you can use your knowledge to cause harm. When you use Hands of Healing on a creature, you can also end one disease or one of the following conditions affecting the creature: blinded, deafened, paralyzed, poisoned, or stunned. When you use Hands of Harm on a creature, you can subject that creature to the poisoned condition until the end of your next turn."

           if monk_tradition == 7:
               class_feature8 = "Wholeness of Body: At 6th level, you gain the ability to heal yourself. As an action, you can regain hit points equal to three times your monk level. You must finish a long rest before you can use this feature again."

           if monk_tradition == 8:
               class_feature8 = "Shadow Step: At 6th level, you gain the ability to step from one shadow into another. When you are in dim light or darkness, as a bonus action you can teleport up to 60 feet to an unoccupied space you can see that is also in dim light or darkness. You then have advantage on the first melee attack you make before the end of the turn."

           if monk_tradition == 9:
               class_feature8 = "Searing Arc Strike: At 6th level, you gain the ability to channel your ki into searing waves of energy. Immediately after you take the Attack action on your turn, you can spend 2 ki points to cast the Burning Hands spell as a bonus action. You can spend additional ki points to cast Burning Hands as a higher level spell. Each additional ki point you spend increases the spell's level by 1. The maximum number of ki points (2 plus any additional points) that you can spend on the spell equals half your monk level."

           if monk_tradition == 10:
               class_feature8 = "Mystical Erudition: Beginning at 6th level, you’ve undergone extensive training with the Cobalt Soul, teaching you extensively in history or lore from the monastery’s collected volumes. You learn one language of your choice, and you gain proficiency with one of the following skills of your choice: Arcana, History, Investigation, Nature, and Religion. If you already have proficiency in one of the listed skills, you can instead choose to double your proficiency bonus for any ability check you make that uses the chosen proficiency. You gain an additional language and an additional skill proficiency from the above list (with the ability to double the bonus of an existing proficiency from the list) at 11th and 17th level.\nExtort Truth: At 6th level, you can hit a hidden cluster of nerves on a creature with precision, temporarily causing them to become mentally malleable. If you hit a creature with an unarmed attack, you can spend 1 ki point to force them to make a Charisma saving throw. On a failed save, the creature is unable to speak a deliberate lie and all Charisma checks directed at the creature are made with advantage for up to 10 minutes. You know if they succeeded or failed on their saving throw. An affected creature is aware of the effect and can thus avoid answering questions to which it would normally respond with a lie. Such a creature can be evasive in its answers as long as the effect lasts."

           if monk_tradition == 11:
               class_feature8 = "Manifest Blow: Starting at 6th level, choose one of the following damage types when you finish a long rest: bludgeoning, piercing, slashing, cold, lightning, necrotic, psychic, or thunder. On your turn, the first creature you hit with an unarmed strike takes an additional 1d6 points of damage of that type. If you select bludgeoning, piercing, or slashing damage, it benefits from your Ki-Empowered Strikes class feature and counts as magical damage. Nightmare Shroud monks typically inflict psychic damage with this ability, Forged Heart monks enhance their bludgeoning damage, and Weretouched grow sharper claws. However, you can choose any damage type, regardless of your discipline(s)."

           if monk_tradition == 12:
               class_feature8 = "Aura Sight: At 6th level, you gain the ability to perceive the auras of other creatures. As an action, select a creature that you can see. That creature makes a Wisdom saving throw, though it has no knowledge that you forced it to attempt this saving throw. On a failed save, you learn if the creature shares any aspects of its alignment with you, its current hit points, and its current attitude and intentions toward you or one other creature, object, or location of your choice. In addition, for the next 24 hours or until you use this ability again, you can use an action to determine the creature’s distance and direction from you. If a creature succeeds on its saving throw against this ability, you cannot use this ability against that creature again until you complete a long rest."

       if PC_level >= 7:
           class_feature9 = "Evasion: At 7th level, your instinctive agility lets you dodge out of the way of certain area effects, such as a blue dragon's lightning breath or a fireball spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.\nStillness of Mind: Starting at 7th level, you can use your action to end one effect on yourself that is causing you to be charmed or frightened."

       if PC_level >= 8:
           feat2 = ability_score_improvement();

       if PC_level >= 9:
           PC_prof_bonus = 4
           
       if PC_level >= 10:
           class_feature10 = "Purity of Body: At 10th level, your mastery of the ki flowing through you makes you immune to disease and poison."

       if PC_level >= 11:

           if monk_tradition == 1:
                class_feature11 = "Body of the Astral Self: Starting at 11th level, when you have both your astral arms and visage summoned, you can cause the body of your astral self to appear (no action required). This spectral body covers your physical form like a suit of armor, connecting with the arms and visage. You determine its appearance. While the spectral body is present, you gain the following benefits:\n    Deflect Energy: When you take acid, cold, fire, force, lightning, or thunder damage, you can use your reaction to deflect it. When you do so, the damage you take is reduced by 1d10 + your Wisdom modifier (minimum reduction of 1).\n    Empowered Arms: Once on each of your turns when you hit a target with the Arms of the Astral Self, you can deal extra damage to the target equal to your Martial Arts die."

           if monk_tradition == 2:
                class_feature11 = "Drunkard's Luck: Starting at 11th level, you always seem to get a lucky bounce at the right moment. When you make an ability check, an attack roll, or a saving throw and have disadvantage, you can spend 2 ki points to cancel the disadvantage for that roll."

           if monk_tradition == 3:
               #Covered at level 3
                class_feature11 = " "

           if monk_tradition == 4:
                class_feature11 = "Sharpen the Blade: At 11th level, you gain the ability to augment your weapons further with your ki. As a bonus action, you can expend up to 3 ki points to grant one kensei weapon you touch a bonus to attack and damage rolls when you attack with it. The bonus equals the number of ki points you spent. This bonus lasts for 1 minute or until you use this feature again. This feature has no effect on a magic weapon that already has a bonus to attack and damage rolls."

           if monk_tradition == 5:
                class_feature11 = "Mastery of Death: Beginning at 11th level, you use your familiarity with death to escape its grasp. When you are reduced to 0 hit points, you can expend 1 ki point (no action required) to have 1 hit point instead."

           if monk_tradition == 6:
                class_feature11 = "Flurry of Healing and Harm: Starting at 11th level, you can now mete out a flurry of comfort and hurt. When you use Flurry of Blows, you can now replace each of the unarmed strikes with a use of your Hands of Healing, without spending ki points for the healing. In addition, when you make an unarmed strike with Flurry of Blows, you can use Hand of Harm with that strike without spending the ki point for Hands of Harm. You can still use Hands of Harm only once per turn."

           if monk_tradition == 7:
                class_feature11 = "Tranquility: Beginning at 11th level, you can enter a special meditation that surrounds you with an aura of peace. At the end of a long rest, you gain the effect of a Sanctuary spell that lasts until the start of your next long rest (the spell can end early as normal). The saving throw DC for the spell equals 8 + your Wisdom modifier + your proficiency bonus."

           if monk_tradition == 8:
                class_feature11 = "Cloak of Shadows: By 11th level, you have learned to become one with the shadows. When you are in an area of dim light or darkness, you can use your action to become invisible. You remain invisible until you make an attack, cast a spell, or are in an area of bright light."

           if monk_tradition == 9:
                class_feature11 = "Searing Sunburst: At 11th level, you gain the ability to create an orb of light that erupts into a devastating explosion. As an action, you magically create an orb and hurl it at a point you choose within 150 feet, where it erupts into a sphere of radiant light for a brief but deadly instant. Each creature in that 20-foot-radius sphere must succeed on a Constitution saving throw or take 2d6 radiant damage. A creature doesn't need to make the save if the creature is behind total cover that is opaque. You can increase the sphere's damage by spending ki points. Each point you spend, up to a maximum of 3, increases the damage by 2d6."

           if monk_tradition == 10:
                class_feature11 = "Mind of Mercury: Starting at 11th level, you’ve honed your awareness and reflexes through mental aptitude and pattern recognition. Once per turn, if you’ve already taken your reaction, you may spend 1 ki point to take an additional reaction."

           if monk_tradition == 11:
               class_feature11 = "Reflexive Adaptation: Starting at 11th level, when you make a Strength (Athletics) or Dexterity (Acrobatics) check, you can spend 1 ki point to roll an additional d20. You can choose to use this ability after you roll the check, but before the outcome is determined. You choose which of the d20s is used for the ability check, omitting the highest if this check was rolled with disadvantage. In addition, the extra damage dealt by the Manifest Blow class feature increases to 2d6."

           if monk_tradition == 12:
                class_feature11 = "Spectral Blades: At 11th level, you can cause your blades to phase through physical objects and defenses. Once during your turn, you can choose to forego one unarmed strike in place of forcing a creature within the reach of that attack to make a Dexterity saving throw against your ki save DC. On a failed saving throw, the creature takes psychic damage equal to that of your unarmed strike, or half that damage if it succeeds."

       if PC_level >= 12:
           feat3 = ability_score_improvement();

       if PC_level >= 13:
           PC_prof_bonus = 5
           class_feature12 = "Tongue of the Sun and Moon: Starting at 13th level, you learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say."

       if PC_level >= 14:
           class_feature13 = "Diamond Soul: Beginning at 14th level, your mastery of ki grants you proficiency in all saving throws. Additionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result."

       if PC_level >= 15:
           class_feature14 = "Timeless Body: At 15th level, your ki sustains you so that you suffer none of the frailty of old age, and you can't be aged magically. You can still die of old age, however. In addition, you no longer need food or water."

       if PC_level >= 16:
          feat4 = ability_score_improvement();

       if PC_level >= 17:

           PC_prof_bonus = 6

           if monk_tradition == 1:
               class_feature15 = "Awakened Astral Self: Starting at 17th level, your connection to your astral self is complete, allowing you to unleash its full potential. As a bonus action, you can spend 5 ki points to summon the arms, visage, and body of your astral self and awaken it for 10 minutes. This awakening ends early if you are incapacitated or die. While your astral self is awakened, you gain the following benefits:\n     Armor of the Spirit: You gain a +2 bonus to Armor Class\n     Astral Barrage: Whenever you use the Extra Attack feature to attack twice, you can instead attack three times if all the attacks are made with your astral arms."

           if monk_tradition == 2:
               class_feature15 = "Intoxicated Frenzy: At 17th level, you gain the ability to make an overwhelming number of attacks against a group of enemies. When you use your Flurry of Blows, you can make up to three additional attacks with it (up to a total of five Flurry of Blows attacks), provided that each Flurry of Blows attack targets a different creature this turn."

           if monk_tradition == 3:
               #Covered by level 3 check
               class_feature15 = " "

           if monk_tradition == 4:
               class_feature15 = "Unerring Accuracy: At 17th level, your mastery of weapons grants you extraordinary accuracy. If you miss with an attack roll using a monk weapon on your turn, you can reroll it. You can use this feature only once on each of your turns."

           if monk_tradition == 5:
               class_feature15 = "Touch of the Long Death: Starting at 17th level, your touch can channel the energy of death into a creature. As an action, you touch one creature within 5 feet of you, and you expend 1 to 10 ki points. The target must make a Constitution saving throw, and it takes 2d10 necrotic damage per ki point spent on a failed save, or half as much damage on a successful one."

           if monk_tradition == 6:
               class_feature15 = "Hand of Ultimate Mercy: By 17th level, Your mastery of life energy opens the door to the ultimate mercy. As an action, you can touch the corpse of a creature that died within the past 24 hours and expend 5 ki points. The creature then returns to life, regaining a number of hit points equal to 4d10 + your Wisdom modifier. If the creature died while subject to any of the following conditions, it revives with them removed: blinded, deafened, paralyzed, poisoned, and stunned. Once you use this feature, you can't use it again until you finish a long rest."

           if monk_tradition == 7:
               class_feature15 = "Quivering Palm: At 17th level, you gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your monk level. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage. You can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action."

           if monk_tradition == 8:
               class_feature15 = "Opportunist: At 17th level, you can exploit a creature's momentary distraction when it is hit by an attack. Whenever a creature within 5 feet of you is hit by an attack made by a creature other than you, you can use your reaction to make a melee attack against that creature."

           if monk_tradition == 9:
               class_feature15 = "Sun Shield: At 17th level, you become wreathed in a luminous, magical aura. You shed bright light in a 30-foot radius and dim light for an additional 30 feet. You can extinguish or restore the light as a bonus action. If a creature hits you with a melee attack while this light shines, you can use your reaction to deal radiant damage to the creature. The radiant damage equals 5 + your Wisdom modifier."

           if monk_tradition == 10:
               class_feature15 = "Debilitating Barrage: Upon reaching 17th level, you’ve gained the knowledge to temporarily lower a creature’s fortitude by striking a series of pressure points. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can spend 3 ki points to cause the creature to suffer a vulnerability to a damage type of your choice for 1 minute, or until they take damage of that type. A creature who is affected by this feature cannot be affected by it again for 24 hours."

           if monk_tradition == 11:
               class_feature15 = ("Perfect Form: At 17th level, you transform your body to become a weapon of war. You gain a feature based on a discipline of your choice. You can choose the same discipline you selected at 3rd level or a different one\n"
                                 "Forged Heart. When you are hit by an attack, you can use your reaction to add your Wisdom modifier (minimum of 1) to your AC, including against the triggering attack. This effect lasts until the start of your next turn.\n"
                                 "Nightmare Shroud. When you damage a creature with your Manifest Blow, excess psionic energy ripples to up to 3 different creatures of your choice within 30 feet. Those creatures take an amount of psychic damage equal to half of your monk level.\n"
                                 "Traveler’s Blade. When you deal piercing or slashing damage to a creature with an unarmed strike, it takes an additional 1d8 poison damage and must succeed on a Constitution saving throw against your ki save DC or be poisoned until the end of its next turn\n"
                                 "Weretouched. When you use your Flurry of Blows, you can make three unarmed strikes as a bonus action instead of two. You have advantage on these attacks.\n")

           if monk_tradition == 12:
               class_feature15 = "Psychic Form: At 17th level, you can transform your physical body into the same psychic energy that comprises your soul knives. As a bonus action, you assume a psychic form, which grants the following benefits: You have resistance to all damage, a fly speed of 30 ft, and You can move through other creatures and objects as if they were difficult terrain. You take 5 force damage if you end your turn inside an object. This benefit lasts for 1 minute. You cannot use it again until you complete a long rest."

       if PC_level >= 18:
           class_feature16 = "Empty Body: Beginning at 18th level, you can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage. Additionally, you can spend 8 ki points to cast the Astral Projection spell, without needing material components. When you do so, you can't take any other creatures with you."

       if PC_level >= 19:
           feat5 = ability_score_improvement();

       if PC_level >= 20:
           class_feature17 = "Perfect Self: At 20th level, when you roll for initiative and have no ki points remaining, you regain 4 ki points."

    if PC_class == "Paladin":
        caster = "Half"
        hit_dice = "1d10 per paladin level"
        first_lvl_hp = 10 + modifier(Constitution)
        hp_level = PC_level - 1
        high_lvl_hp = 0
        while hp_level != 0:
           temp = randint(1,10)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1
        PC_hp = first_lvl_hp + high_lvl_hp
        light_armor = 1
        medium_armor = 1
        heavy_armor = 1
        shields = 1
        simple_weapons = 1
        martial_weapons = 1

        PC_wis_savethrw = 1
        PC_cha_savethrw = 1

        skill1 = randint(1,6)
        if skill1 == 1:
           persuasion = 1
        if skill1 == 2:
           religion = 1
        if skill1 == 3:
            athletics = 1
        if skill1 == 4:
            medicine = 1
        if skill1 == 5:
           insight = 1
        if skill1 == 6:
            inintimidation = 1

        skill2 = randint(1,6)
        while skill1 == skill2:
            skill2 = randint(1,6)

        if skill2 == 1:
           persuasion = 1
        if skill2 == 2:
           religion = 1
        if skill2 == 3:
            athletics = 1
        if skill2 == 4:
            medicine = 1
        if skill2 == 5:
           insight = 1
        if skill2 == 6:
            inintimidation = 1
        
        equipment = randint(1,2)
        if equipment == 1:
            class_equipment = "A martial weapon and a shield"
        if equipment == 2:
            class_equipment = " Two martial weapons"

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment2 = " 5 Javelins "
        if equipment == 2:
            class_equipment2 = " Any simple melee weapon"

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment3 = " A priest's pack "
        if equipment == 2:
            class_equipment3 = " An explorer's packs"

        class_equipment4 = "Chain mail and a holy symbol"

        class_feature1 = "Divine Sense: The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell. You can use this feature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, you regain all expended uses.\nLay on Hands: Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to your paladin level x 5. As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in your pool. Alternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one. This feature has no effect on undead and constructs."

        if PC_level >= 2:

            level_1_spell1 = paladin_level_1();
            level_1_spell2 = paladin_level_1();

            while level_1_spell1 == level_1_spell2:
                level_1_spell2 = paladin_level_1();

            fighting_style = randint(1,12)
               
            if fighting_style == 1:
                class_feature2 = "Fighting Style: Blessed Warrior: You learn two cantrips of your choice from the cleric spell list. They count as paladin spells for you, and Charisma is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the cleric spell list.\n"

            if fighting_style == 2:
                class_feature2 = "Fighting Style: Blind Fighting: You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you."

            if fighting_style == 3:
                class_feature2 = "Fighting Style: Defense: While you are wearing armor, you gain a +1 bonus to AC."
    
            if fighting_style == 4:
                class_feature2 = "Fighting Style: Dueling: When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon."

            if fighting_style == 5:
                class_feature2 = "Fighting Style: Great Weapon Fighting: When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit."

            if fighting_style == 6:
                class_feature2 = "Fighting Style: Interception: When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction."

            if fighting_style == 7:
                class_feature2 = "Fighting Style: Protection: When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield."

            if fighting_style == 9:
                class_feature2 = "Fighting Style: Thrown Weapon Fighting: You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll."

            if fighting_style == 10:
                class_feature2 = "Fighting Style: Two-Weapon Fighting: When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack."
    
            if fighting_style == 11:
                class_feature2 = "Fighting Style: Unarmed Fighting: Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."

            if fighting_style == 12:
                class_feature2 = "Fighting Style: Close Quarters Shooter (UA): When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks."

            if fighting_style == 13:
                class_feature2 = "Fighting Style: Mariner (UA): As long as you are not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class."

            if fighting_style == 14:
                class_feature2 = "Fighting Style: Tunnel Fighter (UA): As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach."










            class_feature3 = ("Spellcasting: By 2nd level, you have learned to draw on divine magic through meditation and prayer to cast spells as a cleric does.\n"
                                 "Your spellcasting chart is shown below\n"
                                 "                         Slot Types\n"
                                       "Level       1st     2nd     3rd     4th     5th\n"
                                       "  1\n"
                                       "  2         2\n"
                                       "  3         3\n"
                                       "  4         3\n"
                                       "  5         4       2\n"
                                       "  6         4       2\n"
                                       "  7         4       3\n"
                                       "  8         4       3\n"
                                       "  9         4       3       2\n"
                                       "  10        4       3       2\n"
                                       "  11        4       3       3\n"
                                       "  12        4       3       3\n"
                                       "  13        4       3       3       1\n"
                                       "  14        4       3       3       1\n"
                                       "  15        4       3       3       2\n"
                                       "  16        4       3       3       2\n"
                                       "  17        4       3       3       3       1\n"
                                       "  18        4       3       3       3       1\n"
                                       "  19        4       3       3       3       2\n"
                                       "  20        4       3       3       3       2\n"
                                       "\n\n"
                               "Charisma is your spellcasting ability for your paladin spells, since their power derives from the strength of your convictions. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a paladin spell you cast and when making an attack roll with one."
                               "Spell save DC = 8 + your proficiency bonus + your Charisma modifier, Spell attack modifier = your proficiency bonus + your Charisma modifier. You can use a holy symbol as a spellcasting focus for your paladin spells.")

            class_feature4 = "Divine Smite: Starting at 2nd level, when you hit a creature with a melee weapon attack, you can expend one spell slot to deal radiant damage to the target, in addition to the weapon's damage. The extra damage is 2d8 for a 1st-level spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of 5d8. The damage increases by 1d8 if the target is an undead or a fiend, to a maximum of 6d8."

        if PC_level >= 3:
            level_1_spell3 = paladin_level_1();

            while level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1:
                level_1_spell3 = paladin_level_1();
          
            class_feature5 = "Divine Health: By 3rd level, the divine magic flowing through you makes you immune to disease.\nHarness Divine Power: Also at 3rd level, you can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 3rd level, once; 7th level, twice; and 15th level, thrice. You regain all expended uses when you finish a long rest.\nChannel Divinity: Your oath allows you to channel divine energy to fuel magical effects. Each Channel Divinity option provided by your oath explains how to use it. When you use your Channel Divinity, you choose which option to use. You must then finish a short or long rest to use your Channel Divinity again. Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your paladin spell save DC."
            

            paladin_oath = randint(1,10)

            if paladin_oath == 1:
                
                PC_subclass = "Oath of the Ancients"
                class_feature6 = ("The tenets of the Oath of the Ancients have been preserved for uncounted centuries. This oath emphasizes the principles of good above any concerns of law or chaos. Its four central principles are simple.\nTenets of the Ancients:\n     1. Kindle the Light: Through your acts of mercy, kindness, and forgiveness, kindle the light of hope in the world, beating back despair.\n     2. Shelter the Light: Where there is good, beauty, love, and laughter in the world, stand against the wickedness that would swallow it. Where life flourishes, stand against the forces that would render it barren.\n     3. Preserve Your Own Light: Delight in song and laughter, in beauty and art. If you allow the light to die in your own heart, you can't preserve it in the world.\n     4. Be the Light: Be a glorious beacon for all who live in despair. Let the light of your joy and courage shine forth in all your deeds.\n\n" 
                                  "Oath Spells:\n     3rd: Ensnaring Strike, Speak with Animals\n   5th: Moonbeam, Misty Step\n     9th: Plant Growth, Protection from Energy\n     13th:  	Ice Storm, Stoneskin\n     17th:  	Commune with Nature, Tree Stride\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Nature's Wrath. You can use your Channel Divinity to invoke primeval forces to ensnare a foe. As an action, you can cause spectral vines to spring up and reach for a creature within 10 feet of you that you can see. The creature must succeed on a Strength or Dexterity saving throw (its choice) or be restrained. While restrained by the vines, the creature repeats the saving throw at the end of each of its turns. On a success, it frees itself and the vines vanish\n     Turn the Faithless. You can use your Channel Divinity to utter ancient words that are painful for fey and fiends to hear. As an action, you present your holy symbol, and each fey or fiend within 30 feet of you that can hear you must make a Wisdom saving throw. On a failed save, the creature is turned for 1 minute or until it takes damage.\n"
                                  "A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action. If the creature's true form is concealed by an illusion, shapeshifting, or other effect, that form is revealed while it is turned.")

            if paladin_oath == 2:
                PC_subclass = "Oath of Conquest"
                class_feature6 = ("A paladin who takes this oath has the tenets of conquest seared on the upper arm.\nTenets of Conquest:\n     1. Douse the Flame of Hope. It is not enough to merely defeat an enemy in battle. Your victory must be so overwhelming that your enemies’ will to fight is shattered forever. A blade can end a life. Fear can end an empire.\n     2. Rule with an Iron Fist. Once you have conquered, tolerate no dissent. Your word is law. Those who obey it shall be favored. Those who defy it shall be punished as an example to all who might follow.\n     3. Strength Above All. You shall rule until a stronger one arises. Then you must grow mightier and meet the challenge, or fall to your own ruin.\n\n" 
                                  "Oath Spells:\n     3rd: Armor of Agathys, Command\n   5th: Hold Person, Spiritual Weapon\n     9th: Bestow Curse, Fear\n     13th: Dominate Beast, Stoneskin\n     17th: Cloudkill, Dominate Person\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Conquering Presence. You can use your Channel Divinity to exude a terrifying presence. As an action, you force each creature of your choice that you can see within 30 feet of you to make a Wisdom saving throw. On a failed save, a creature becomes frightened of you for 1 minute. The frightened creature can repeat this saving throw at the end of each of its turns, ending the effect on itself on a success.\n     Guided Strike. You can use your Channel Divinity to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.\n")
                                  
            if paladin_oath == 3:
                PC_subclass = "Oath of the Crown"
                class_feature6 = ("The tenets of the Oath of the Crown are often set by the sovereign to which their oath is sworn, but generally emphasize the following tenets.\nTenets of the Crown:\n     1. Law. The law is paramount. It is the mortar that holds the stones of civilization together, and it must be respected.\n     2. Loyalty. Your word is your bond. Without loyalty, oaths and laws are meaningless.\n     3. Courage. You must be willing to do what needs to be done for the sake of order, even in the face of overwhelming odds. If you don't act, then who will?\n     4.Responsibility. You must deal with the consequences of your actions, and you are responsible for fulfilling your duties and obligations\n\n" 
                                  "Oath Spells:\n     3rd: Command, Compelled Duel\n   5th: Warding Bond, Zone of Truth\n     9th: Aura of Vitality, Spirit Guardians\n     13th: Banishment, Guardian of Faith\n     17th: Circle of Power, Geas\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Champion Challenge. As a bonus action, you issue a challenge that compels other creatures to do battle with you. Each creature of your choice that you can see within 30 feet of you must make a Wisdom saving throw. On a failed save, a creature can't willingly move more than 30 feet away from you. This effect ends on the creature if you are incapacitated or die or if the creature is more than 30 feet away from you.\n     Turn the Tide. As a bonus action, you can bolster injured creatures with your Channel Divinity. Each creature of your choice that can hear you within 30 feet of you regains hit points equal to 1d6 + your Charisma modifier (minimum of 1) if it has no more than half of its hit points\n")
                                  
            if paladin_oath == 4:
                PC_subclass = "Oath of Devotion"
                class_feature6 = ("Though the exact words and strictures of the Oath of Devotion vary, paladins of this oath share these tenets.\nTenets of Devotion:\n     1. Honesty. Don't lie or cheat. Let your word be your promise.\n     2. Loyalty. Courage. Never fear to act, though caution is wise.\n     3. Compassion. Aid others, protect the weak, and punish those who threaten them. Show mercy to your foes, but temper it with wisdom.\n     4.Honor. Treat others with fairness, and let your honorable deeds be an example to them. Do as much good as possible while causing the least amount of harm.\n     5. Duty. Be responsible for your actions and their consequences, protect those entrusted to your care, and obey those who have just authority over you.\n\n" 
                                  "Oath Spells:\n     3rd: Protection from Evil and Good, Sanctuary\n   5th: Lesser Restoration, Zone of Truth\n     9th: Beacon of Hope, Dispel Magic\n     13th: Freedom of Movement, Guardian of Faith\n     17th: Commune, Flame Strike\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Sacred Weapon. As an action, you can imbue one weapon that you are holding with positive energy, using your Channel Divinity. For 1 minute, you add your Charisma modifier to attack rolls made with that weapon (with a minimum bonus of +1). The weapon also emits bright light in a 20-foot radius and dim light 20 feet beyond that. If the weapon is not already magical, it becomes magical for the duration. You can end this effect on your turn as part of any other action. If you are no longer holding or carrying this weapon, or if you fall unconscious, this effect ends.\n     Turn the Unholy. As an action, you present your holy symbol and speak a prayer censuring fiends and undead, using your Channel Divinity. Each fiend or undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.\n")
                    
            if paladin_oath == 5:
                PC_subclass = "Oath of Glory"
                class_feature6 = ("The tenets of the Oath of Glory drive a paladin to attempt heroics that might one day shine in legend.\nTenets of Glory:\n     1. Actions over Words. Strive to be known by glorious deeds, not words.\n     2. Challenges Are but Tests. Face hardships with courage, and encourage your allies to face them with you.\n     3. Hone the Body. Like raw stone, your body must be worked so its potential can be realized.\n     4. Discipline the Soul. You must marshal the discipline to overcome failings within yourself that threaten to dim the glory of you and your friends.\n\n" 
                                  "Oath Spells:\n     3rd: Guiding Bolt, Heroism\n   5th: Enhance Ability, Magic Weapon\n     9th: Haste, Protection From Energy\n     13th: Compulsion, Freedom Of Movement\n     17th: Commune, Flame Strike\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Peerless Athlete. As a bonus action, you can use your Channel Divinity to augment your athleticism. For the next 10 minutes, you have advantage on Strength (Athletics) and Dexterity (Acrobatics) checks; you can carry, push, drag, and lift twice as much weight as normal; and the distance of your long and high jumps increases by 10 feet (this extra distance costs movement as normal).\n     Inspiring Smite. Immediately after you deal damage to a creature with your Divine Smite feature, you can use your Channel Divinity as a bonus action and distribute temporary hit points to creatures of your choice within 30 feet of you, which can include you. The total number of temporary hit points equals 2d8 + your level in this class, divided among the chosen creatures however you like.\n")
                 
            if paladin_oath == 6:
                PC_subclass = "Oath of Redemption"
                class_feature6 = ("The tenets of the Oath of Redemption hold a paladin to a high standard of peace and justice.\nTenets of Glory:\n     1. Peace. Violence is a weapon of last resort. Diplomacy and understanding are the paths to long-lasting peace.\n     2. Innocence. All people begin life in an innocent state, and it is their environment or the influence of dark forces that drives them to evil. By setting the proper example, and working to heal the wounds of a deeply flawed world, you can set anyone on a righteous path.\n     3. Patience. Change takes time. Those who have walked the path of the wicked must be given reminders to keep them honest and true. Once you have planted the seed of righteousness in a creature, you must work day after day to allow it to survive and then flourish.\n     4. Wisdom. Your heart and mind must stay clear, for eventually you will be forced to admit defeat. While every creature can be redeemed, some are so far along the path of evil that you have no choice but to end their lives for the greater good. Any such action must be carefully weighed and the consequences fully understood, but once you have made the decision, follow through with it knowing your path is just.\n\n" 
                                  "Oath Spells:\n     3rd: Sanctuary, Sleep\n   5th: Calm Emotions, Hold Person\n     9th: Counterspell, Hypnotic Pattern\n     13th: Otiluke's Resilient Sphere, Stoneskin\n     17th: Hold Monster, Wall of Force\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Emissary of Peace. You can use your Channel Divinity to augment your presence with divine power. As a bonus action, you grant yourself a +5 bonus to Charisma (Persuasion) checks for the next 10 minutes.\n     Rebuke the Violent. You can use your Channel Divinity to rebuke those who use violence. Immediately after an attacker within 30 feet of you deals damage with an attack against a creature other than you, you can use your reaction to force the attacker to make a Wisdom saving throw. On a failed save, the attacker takes radiant damage equal to the damage it just dealt. On a successful save, it takes half as much damage.\n")
             
            if paladin_oath == 7:
                PC_subclass = "Oath of Vengeance"
                class_feature6 = ("The tenets of the Oath of Vengeance vary by paladin, but all the tenets revolve around punishing wrongdoers by any means necessary. Paladins who uphold these tenets are willing to sacrifice even their own righteousness to mete out justice upon those who do evil, so the paladins are often neutral or lawful neutral in alignment. The core principles of the tenets are brutally simple.\nTenets of Glory:\n     1. Fight the Greater Evil. Faced with a choice of fighting my sworn foes or combating a lesser evil, I choose the greater evil.\n     2. No Mercy for the Wicked. Ordinary foes might win my mercy, but my sworn enemies do not.\n     3. By Any Means Necessary. My qualms can't get in the way of exterminating my foes.\n     4. Restitution. If my foes wreak ruin on the world, it is because I failed to stop them. I must help those harmed by their misdeeds.\n\n" 
                                  "Oath Spells:\n     3rd: Bane, Hunter's Mark\n   5th: Hold Person, Misty Step\n     9th: Haste, Protection from Energy\n     13th: Banishment, Dimension Door\n     17th: Hold Monster, Scrying\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Abjure Enemy. As an action, you present your holy symbol and speak a prayer of denunciation, using your Channel Divinity. Choose one creature within 60 feet of you that you can see. That creature must make a Wisdom saving throw, unless it is immune to being frightened. Fiends and undead have disadvantage on this saving throw. n a failed save, the creature is frightened for 1 minute or until it takes any damage. While frightened, the creature's speed is 0, and it can't benefit from any bonus to its speed. On a successful save, the creature's speed is halved for 1 minute or until the creature takes any damage.\n     Vow of Enmity. As a bonus action, you can utter a vow of enmity against a creature you can see within 10 feet of you, using your Channel Divinity. You gain advantage on attack rolls against the creature for 1 minute or until it drops to 0 hit points or falls unconscious.\n")
            
            if paladin_oath == 8:
                PC_subclass = "Oath of the Watchers"
                class_feature6 = ("A paladin who assumes the Oath of the Watchers swears to safeguard mortal realms from otherwordly threats.\nTenets of the Watchers:\n     1. Vigilance. The threats you face are cunning, powerful, and subversive. Be ever alert for their corruption.\n     2. Loyalty. Never accept gifts or favors from fiends or those who truck with them. Stay true to your order, your comrades, and your duty.\n     3. Discipline. You are the shield against the endless terrors that lie beyond the stars. Your blade must be forever sharp and your mind keen to survive what lies beyond.\n\n" 
                                  "Oath Spells:\n     3rd: Alarm, Detect Magic\n   5th: Moonbeam, See Invisibility\n     9th: Counterspell, Nondetection\n     13th: Aura of Purity, Banishment\n     17th: Hold Monster, Scrying\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Watcher's Will You can use your Channel Divinity to invest your presence with the warding power of your faith. As an action, you can choose a number of creatures you can see within 30 feet of you, up to a number equal to your Charisma modifier (minimum of one creature). For 1 minute, you and the chosen creatures have advantage on Intelligence, Wisdom, and Charisma saving throws.\n     Abjure the Extraplanar You can use your Channel Divinity to castigate unworldly beings. As an action, you present your holy symbol and each aberration, celestial, elemental, fey, or fiend within 30 feet of you that can hear you must make a Wisdom saving throw. On a failed save, the creature is turned for 1 minute or until it takes damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly end its move in a space within 30 feet of you. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can take the Dodge action.\n")
                    
            if paladin_oath == 9:
                PC_subclass = "Oathbreaker"
                class_feature6 = ("Oath Spells:\n     3rd: Hellish Rebuke, Inflict Wounds\n   5th: Crown of Madness, Darkness\n     9th: Animate Dead, Bestow Curse\n     13th: Blight, Confusion\n     17th: Contagion, Dominate Person\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Control Undead. As an action, you target one undead creature you can see within 30 feet of you. The target must make a Wisdom saving throw. On a failed save, the target must obey your commands for the next 24 hours, or until you use this Channel Divinity option again. An undead whose challenge rating is equal to or greater than your paladin level is immune to this effect.\n     Dreadful Aspect. As an action, you channel the darkest emotions and focus them into a burst of magical menace. Each creature of your choice within 30 feet of you must make a Wisdom saving throw if it can see you. On a failed save, the target is frightened of you for 1 minute. If a creature frightened by this effect ends its turn more than 30 feet away from you, it can attempt another Wisdom saving throw to end the effect on it.\n")
                    
            if paladin_oath == 10:
                PC_subclass = "Oath of the Open Sea"
                class_feature6 = ("Tenets of Glory:\n     1. No Greater Life than a Life Lived Free. One should be free to chart their own path without oppression. Those who would exert their power to dominate others shall be smote.\n     2. Trust the Skies. The guidance of a strong breeze. The rumbling warnings of a coming storm. Nature is a source of portent and council that should be heeded.\n     3. Adapt like the Water. The waters of the ocean can shift around any obstacle or become an impassable one. They can carve around and reveal the secrets of the past or swallow the truth and hide it forever. To embrace this fluidity is to be ready for any challenge.\n     4.Explore the Uncharted. The world is filled with much mystery. Through the pursuit of these enigmatic ends, one can both uncover those who hide their dark deeds in shadow to be judged, and find the path to becoming something great.\n\n" 
                                  "Oath Spells:\n     3rd: Create or Destroy Water, Expeditious Retreat\n   5th: Augury, Misty Step\n     9th: Call Lightning, Tidal Wave\n     13th: Control Water, Freedom Of Movement\n     17th: Commune With Nature, Maelstrom\n\n"
                                  "Channel Divinity: When you take this oath at 3rd level, you gain the following two Channel Divinity options.\n     Marine Layer. As an action you can channel the sea to create a thick cloud of fog that surrounds you and heavily obscures the area for 20 feet in all directions, following you as you move. You and all creatures within 5 feet of you instead treat this fog as lightly obscured. This fog lasts for 10 minutes, spreads around corners and cannot be dispersed.\n     Fury of the Tides. As a bonus action, you can channel the powerful might of the waves to bolster your attacks for 1 minute. Once per turn for the duration, when you hit a creature with weapon attack, you can choose to push the target 10 feet away from you. If the target is pushed into an obstacle or another creature, they take additional bludgeoning damage equal to your Charisma modifier.\n")
            

        if PC_level >= 4:
            feat1 = ability_score_improvement();
            class_feature6 = "Martial Versatility: Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace a fighting style you know with another fighting style available to paladins. This replacement represents a shift of focus in your martial practice."

        if PC_level >= 5:

            PC_prof_bonus = 3
            level_1_spell4 = paladin_level_1();
            while level_1_spell4 == level_1_spell2 or  level_1_spell4 == level_1_spell1 or level_1_spell4 == level_1_spell3:
                level_1_spell4 = paladin_level_1();

            level_2_spell1 = paladin_level_2();
            level_2_spell2 = paladin_level_2();
            while level_2_spell1 == level_2_spell2:
                level_2_spell2 = paladin_level_2();

            class_feature7 = "Extra Attack: Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."

        if PC_level >= 6:

            class_feature8 = "Aura of Protection: Starting at 6th level, whenever you or a friendly creature within 10 feet of you must make a saving throw, the creature gains a bonus to the saving throw equal to your Charisma modifier (with a minimum bonus of +1). You must be conscious to grant this bonus. At 18th level, the range of this aura increases to 30 feet."

        if PC_level >= 7:

            level_2_spell3 = paladin_level_2();

            while level_2_spell3 == level_2_spell2 or level_2_spell3 == level_2_spell1:
                level_2_spell3 = paladin_level_2();

            if paladin_oath == 1:
                class_feature9 = "Aura of Warding: Beginning at 7th level, ancient magic lies so heavily upon you that it forms an eldritch ward. You and friendly creatures within 10 feet of you have resistance to damage from spells. At 18th level, the range of this aura increases to 30 feet."

            if paladin_oath == 2:
                class_feature9 = "Aura of Conquest: Starting at 7th level, you constantly emanate a menacing aura while you’re not incapacitated. The aura extends 10 feet from you in every direction, but not through total cover. If a creature is frightened of you, its speed is reduced to 0 while in the aura, and that creature takes psychic damage equal to half your paladin level if it starts its turn there. At 18th level, the range of this aura increases to 30 feet."

            if paladin_oath == 3:
                class_feature9 = "Divine Allegiance: Starting at 7th level, when a creature within 5 feet of you takes damage, you can use your reaction to magically substitute your own health for that of the target creature, causing that creature not to take the damage. Instead, you take the damage. This damage to you can't be reduced or prevented in any way."

            if paladin_oath == 4:
                class_feature9 = "Aura of Devotion: Starting at 7th level, you and friendly creatures within 10 feet of you can't be charmed while you are conscious. At 18th level, the range of this aura increases to 30 feet."

            if paladin_oath == 5:
                class_feature9 = "Aura of Alacrity: At 7th level, you emanate an aura that fills you and your companions with supernatural speed, allowing you to race across a battlefield in formation. Your walking speed increases by 10 feet. In addition, if you aren't incapacitated, the walking speed of any ally who starts their turn within 5 feet of you increases by 10 feet until the end of that turn. When you reach 18th level in this class, the range of the aura increases to 10 feet."

            if paladin_oath == 6:
                class_feature9 = "Aura of the Guardian: Starting at 7th level, you can shield your allies from harm at the cost of your own health. When a creature within 10 feet of you takes damage, you can use your reaction to magically take that damage, instead of that creature taking it. This feature doesn't transfer any other effects that might accompany the damage, and this damage can't be reduced in any way. At 18th level, the range of this aura increases to 30 feet."

            if paladin_oath == 7:
                class_feature9 = "Relentless Avenger: By 7th level, your supernatural focus helps you close off a foe's retreat. When you hit a creature with an opportunity attack, you can move up to half your speed immediately after the attack and as part of the same reaction. This movement doesn't provoke opportunity attacks."

            if paladin_oath == 8:
                class_feature9 = "Aura of the Sentinel: At 7th level, you emit an aura of alertness while you aren't incapacitated. When you and any creatures of your choice within 10 feet of you roll initiative, you all gain a bonus to initiative equal to your proficiency bonus. At 18th level, the range of this aura increases to 30 feet."

            if paladin_oath == 9:
                class_feature9 = "Aura of Hate: Starting at 7th level you, as well any fiends and undead within 10 feet of you, gain a bonus to melee weapon damage rolls equal to your Charisma modifier (minimum of +1). A creature can benefit from this feature from only one paladin at a time. At 18th level, the range of this aura increases to 30 feet."

            if paladin_oath == 10:
                class_feature9 = "Aura of Liberation: Starting at 7th level, you emanate an aura while you’re not incapacitated. You and any creature of your choice within 10 feet of you cannot be grappled or restrained, as well as ignore penalties on movement or attacks while underwater. Creatures that are already grappled or restrained when they enter the aura can spend 5 feet of movement to automatically escape nonmagical restraints. When you reach 18th level in this class, the range of the aura increases to 30 feet."

        if PC_level >= 8:
            feat2 = ability_score_improvement();

        if PC_level >= 9:
            PC_prof_bonus = 4
           
            level_3_spell1 = paladin_level_3();
            level_3_spell2 = paladin_level_3();
            while level_3_spell1 == level_3_spell2:
                level_3_spell2 = paladin_level_3();

        if PC_level >= 10:
            class_feature10 = "Aura of Courage: Starting at 10th level, you and friendly creatures within 10 feet of you can't be frightened while you are conscious. At 18th level, the range of this aura increases to 30 feet."

        if PC_level >= 11:
            level_3_spell3 = paladin_level_3();

            while level_3_spell3 == level_3_spell2 or level_3_spell3 == level_3_spell1:
                level_3_spell3 = paladin_level_3();

            class_feature11 = "Improved Divine Smite: By 11th level, you are so suffused with righteous might that all your melee weapon strikes carry divine power with them. Whenever you hit a creature with a melee weapon, the creature takes an extra 1d8 radiant damage."

        if PC_level >= 12:
            feat3 = ability_score_improvement();
            
        if PC_level >= 13:
            PC_prof_bonus = 5
            level_4_spell1 = paladin_level_4();

        if PC_level >= 14:
            class_feature12 = "Cleansing Touch: Beginning at 14th level, you can use your action to end one spell on yourself or on one willing creature that you touch. You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain expended uses when you finish a long rest."

        if PC_level >= 15:
            level_4_spell2 = paladin_level_4();
            while level_4_spell1 == level_4_spell2:
                level_4_spell2 = paladin_level_4();

            if paladin_oath == 1:
                class_feature13 = "Undying Sentinel: Starting at 15th level, when you are reduced to 0 hit points and are not killed outright, you can choose to drop to 1 hit point instead. Once you use this ability, you can't use it again until you finish a long rest. Additionally, you suffer none of the drawbacks of old age, and you can't be aged magically."

            if paladin_oath == 2:
                class_feature13 = "Scornful Rebuke: Starting at 15th level, those who dare to strike you are psychically punished for their audacity. Whenever a creature hits you with an attack, that creature takes psychic damage equal to your Charisma modifier (minimum of 1) if you’re not incapacitated."

            if paladin_oath == 3:
                class_feature13 = "Unyielding Saint: Starting at 15th level, you have advantage on saving throws to avoid becoming paralyzed or stunned."

            if paladin_oath == 4:
                class_feature13 = "Purity of Spirit: Beginning at 15th level, you are always under the effects of a Protection from Evil and Good spell."

            if paladin_oath == 5:
                class_feature13 = "Glorious Defense: When you reach 15th level, you can turn defense into a sudden strike. When you or another creature you can see within 10 feet of you is hit by an attack roll, you can use your reaction to grant a bonus to the target's AC against that attack, potentially causing it to miss. The bonus equals your Charisma modifier (minimum of +l). If the attack misses, you can make one weapon attack against the attacker as part of this reaction, provided the attacker is within your weapon's range. You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a long rest."

            if paladin_oath == 6:
                class_feature13 = "Protective Spirit: Starting at 15th level, a holy presence mends your wounds in combat. You regain hit points equal to 1d6 + half your paladin level if you end your turn in combat with fewer than half of your hit points remaining and you aren’t incapacitated."

            if paladin_oath == 7:
                class_feature13 = "Soul of Vengeance: Starting at 15th level, the authority with which you speak your Vow of Enmity gives you greater power over your foe. When a creature under the effect of your Vow of Enmity makes an attack, you can use your reaction to make a melee weapon attack against that creature if it is within range."

            if paladin_oath == 8:
                class_feature13 = "Vigilant Rebuke: At 15th level, you've learned how to chastise anyone who dares wield beguilements against you and your wards. Whenever you or a creature you can see within 30 feet of you succeeds on an Intelligence, a Wisdom, or a Charisma saving throw, you can use your reaction to deal 2d8 + your Charisma modifier force damage to the creature that forced the saving throw."

            if paladin_oath == 9:
                class_feature13 = "Supernatural Resistance: At 15th level, you gain resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons."

            if paladin_oath == 10:
                class_feature13 = "Stormy Waters: At 15th level, you can call crashing waters around you as a reaction whenever a creature enters or exits your melee range. The creature takes 1d12 bludgeoning damage and must succeed a Strength saving throw or be knocked prone."

        if PC_level >= 16:
            feat4 = ability_score_improvement();

        if PC_level >= 17:
            PC_prof_bonus = 6
            level_5_spell1 = paladin_level_5();

            level_4_spell3 = paladin_level_4();

            while level_4_spell3 == level_4_spell2 or level_4_spell3 == level_4_spell1:
                level_4_spell3 = paladin_level_4();
            
        #Nothing for level 18, already covered
        if PC_level >= 19:
            feat5 = ability_score_improvement();

            level_5_spell2 = paladin_level_5();

            while  level_5_spell2 ==  level_5_spell1:
                level_5_spell2 = paladin_level_5();

        if PC_level >= 20:

            if paladin_oath == 1:
                class_feature14 = "Elder Champion: At 20th level, you can assume the form of an ancient force of nature, taking on an appearance you choose. For example, your skin might turn green or take on a bark-like texture, your hair might become leafy or moss-like, or you might sprout antlers or a lion-like mane. Using your action, you undergo a transformation. For 1 minute, you gain the following benefits: At the start of each of your turns, you regain 10 hit points, whenever you cast a paladin spell that has a casting time of 1 action, you can cast it using a bonus action instead, and enemy creatures within 10 feet of you have disadvantage on saving throws against your paladin spells and Channel Divinity options. Once you use this feature, you can't use it again until you finish a long rest."

            if paladin_oath == 2:
                class_feature14 = "Invincible Conqueror: At 20th level, you gain the ability to harness extraordinary martial prowess. As an action, you can magically become an avatar of conquest, gaining the following benefits for 1 minute: You have resistance to all damage, when you take the Attack action on your turn, you can make one additional attack as part of that action, and your melee weapon attacks score a critical hit on a roll of 19 or 20 on the d20. Once you use this feature, you can’t use it again until you finish a long rest."

            if paladin_oath == 3:
                class_feature14 = "Exalted Champion: At 20th level, your presence on the field of battle is an inspiration to those dedicated to your cause. You can use your action to gain the following benefits for 1 hour: You have resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons, your allies have advantage on death saving throws while within 30 feet of you, you have advantage on Wisdom saving throws, as do your allies within 30 feet of you. This effect ends early if you are incapacitated or die. Once you use this feature, you can't use it again until you finish a long rest."

            if paladin_oath == 4:
                class_feature14 = "Holy Nimbus: At 20th level, as an action, you can emanate an aura of sunlight. For 1 minute, bright light shines from you in a 30-foot radius, and dim light shines 30 feet beyond that. Whenever an enemy creature starts its turn in the bright light, the creature takes 10 radiant damage. In addition, for the duration, you have advantage on saving throws against spells cast by fiends or undead. Once you use this feature, you can't use it again until you finish a long rest."

            if paladin_oath == 5:
                class_feature14 = "Living Legend: At 20th level, you can empower yourself with the legends — whether true or exaggerated — of your great deeds. As a bonus action, you gain the following benefits for 1 minute: You are blessed with an otherworldly presence, gaining advantage on all Charisma checks, once on each of your turns when you make a weapon attack and miss, you can cause that attack to hit instead, and if you fail a saving throw, you can use your reaction to reroll it. You must use this new roll. Once you use this feature, you can’t use it again until you finish a long rest, unless you expend a 5th-level spell slot to use it again."

            if paladin_oath == 6:
                class_feature14 = "Emissary of Redemption: At 20th level, you become an avatar of peace, which gives you the following benefits: You have resistance to all damage dealt by other creatures (their attacks, spells, and other effects). In addition, whenever a creature damages you, it takes radiant damage equal to half the amount it dealt to you. If you attack a creature, cast a spell on it, or deal damage to it by any means but this feature, neither benefit works against that creature until you finish a long rest."

            if paladin_oath == 7:
                class_feature14 = "Avenging Angel: At 20th level, you can assume the form of an angelic avenger. Using your action, you undergo a transformation. For 1 hour, you gain the following benefits: Wings sprout from your back and grant you a flying speed of 60 feet. In addition, you emanate an aura of menace in a 30-foot radius. The first time any enemy creature enters the aura or starts its turn there during a battle, the creature must succeed on a Wisdom saving throw or become frightened of you for 1 minute or until it takes any damage. Attack rolls against the frightened creature have advantage. Once you use this feature, you can't use it again until you finish a long rest."

            if paladin_oath == 8:
                class_feature14 = "Mortal Bulwark: At 20th level, you manifest a spark of divine power in defense of the mortal realms. As a bonus action, you gain the following benefits for 1 minute: You gain truesight with a range of 120 feet, you have advantage on attack rolls against aberrations, celestials, elementals, fey, and fiends, and when you hit a creature with an attack roll and deal damage to it, you can also force it to make a Charisma saving throw against your spell save DC. On a failed save, the creature is magically banished to its native plane of existence if it's currently not there. On a successful save, the creature can't be banished by this feature for 24 hours. Once you use this bonus action, you can't use it again until you finish a long rest, unless you expend a 5th-level spell slot to use it again."

            if paladin_oath == 9:
                class_feature14 = "Dread Lord: At 20th level, you can, as an action, surround yourself with an aura of gloom that lasts for 1 minute. The aura reduces any bright light in a 30-foot radius around you to dim light. Whenever an enemy that is frightened by you starts its turn in the aura, it takes 4d10 psychic damage. Additionally, you and any creatures of your choosing in the aura are draped in deeper shadow. Creatures that rely on sight have disadvantage on attack rolls against creatures draped in this shadow. While the aura lasts, you can use a bonus action on your turn to cause the shadows in the aura to attack one creature. Make a melee spell attack against the target. If the attack hits, the target takes necrotic damage equal to 3d10 + your Charisma modifier. After activating the aura, you can't do so again until you finish a long rest."

            if paladin_oath == 10:
                class_feature14 = "Mythic Swashbuckler: At 20th level, you learn to channel the spirits of historic sea captains to briefly become a paragon of heroic adventure. As an action, you embrace these spirits of the sea, gaining the following benefits for 1 minute: Climbing costs no additional movement, and you have advantage on Strength (Athletics) checks, if you are within 5 feet of a creature, and no other creatures are within 5 feet of you, you have advantage on your attacks against that creature, you can take the Dodge action as a bonus action, and you have advantage on all Dexterity ability checks and Dexterity saving throws against effects that you can see. nce you use this feature, you can’t use it again until you finish a long rest."

    if PC_class == "Ranger":    
       
        caster = "Half"
        hit_dice = "1d10 per ranger level"
        first_lvl_hp = 10 + modifier(Constitution)
        hp_level = PC_level - 1
        high_lvl_hp = 0
        while hp_level != 0:
           temp = randint(1,10)+ modifier(Constitution)
           if temp < 0:
               temp = 0
           high_lvl_hp += temp
           hp_level -= 1
        PC_hp = first_lvl_hp + high_lvl_hp

        light_armor = 1
        medium_armor = 1
        shields = 1
        simple_weapons = 1
        martial_weapons = 1

        PC_str_savethrw = 1
        PC_dex_savethrw = 1

        skill1 = randint(1,8)
        if skill1 == 1:
           stealth = 1
        if skill1 == 2:
           animal_handling = 1
        if skill1 == 3:
            athletics = 1
        if skill1 == 4:
            investigation = 1
        if skill1 == 5:
           insight = 1
        if skill1 == 6:
            nature = 1
        if skill1 == 7:
            precption = 1
        if skill1 == 8:
            survival = 1

        skill2 = randint(1,8)
        while skill1 == skill2:
            skill2 = randint(1,8)

        if skill2 == 1:
           stealth = 1
        if skill2 == 2:
           animal_handling = 1
        if skill2 == 3:
            athletics = 1
        if skill2 == 4:
            investigation = 1
        if skill2 == 5:
           insight = 1
        if skill2 == 6:
            nature = 1
        if skill2 == 7:
            precption = 1
        if skill2 == 8:
            survival = 1

        skill3 = randint(1,8)
        while skill3 == skill2 or skill3 == skill1:
            skill3 = randint(1,8)

        if skill3 == 1:
           stealth = 1
        if skill3 == 2:
           animal_handling = 1
        if skill3 == 3:
            athletics = 1
        if skill3 == 4:
            investigation = 1
        if skill3 == 5:
           insight = 1
        if skill3 == 6:
            nature = 1
        if skill3 == 7:
            precption = 1
        if skill3 == 8:
            survival = 1
        

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment = "scale mail"
        if equipment == 2:
            class_equipment = " leather armor"

        equipment = randint(1,2)
        if equipment == 1:
            class_equipment2 = " Two shortswords "
        if equipment == 2:
            class_equipment2 = " Two simple melee weapons"

            
        equipment = randint(1,2)
        if equipment == 1:
            class_equipment3 = " A dungeoneer's pack "
        if equipment == 2:
            class_equipment3 = " An explorer's packs"

        class_equipment4 = "A longbow and a quiver of 20 arrows"

        alt_feature = randint(1,2)

        if alt_feature == 1:
            class_feature1 = "Favored Enemy: Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy. Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies. You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them. When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all. You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."

        if alt_feature == 2:
            class_feature1 = "Favored Foe: When you hit a creature with an attack roll, you can call on your mystical bond with nature to mark the target as your favored enemy for 1 minute or until you lose your concentration (as if you were concentrating on a spell). The first time on each of your turns that you hit the favored enemy and deal damage to it, including when you mark it, you increase that damage by 1d4. You can use this feature to mark a favored enemy a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. This feature's extra damage increases when you reach certain levels in this class: to 1d6 at 6th level and to 1d8 at 14th level."

        alt_feature = randint(1,2)
        if alt_feature == 1:
            class_feature2 = "Natural Explorer: Also at 1st level, you are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you’re proficient in. While traveling for an hour or more in your favored terrain, you gain the following benefits:\n       Difficult terrain doesn’t slow your group’s travel.\n       Your group can’t become lost except by magical means.\n       Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n       If you are traveling alone, you can move stealthily at a normal pace.\n       When you forage, you find twice as much food as you normally would.\n       While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.\nYou choose additional favored terrain types at 6th and 10th level."  

        if alt_feature == 2:
            class_feature2 = "Deft Explorer: You are an unsurpassed explorer and survivor, both in the wilderness and in dealing with others on your travels. You gain the Canny benefit below, and you gain an additional benefit when you reach 6th level and 10th level in this class.\n       Canny (1st Level): Choose one of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make using the chosen skill. You can also speak, read, and write 2 additional languages of your choice.\n       Roving (6th Level): Your walking speed increases by 5, and you gain a climbing speed and a swimming speed equal to your walking speed.\n       Tireless (10th Level): As an action, you can give yourself a number of temporary hit points equal to 1d8 + your Wisdom modifier (minimum of 1 temporary hit point). You can use this action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. In addition, whenever you finish a short rest, your exhaustion level, if any, is decreased by 1."

        if PC_level >= 2:
            
            fighting_style = randint(1,12)

            if fighting_style == 1:
                class_feature3 = "Fighting Style: Archery. You gain a +2 bonus to attack rolls you make with ranged weapons.\n"

            if fighting_style == 2:
                class_feature3 = "Fighting Style: Blind Fighting: You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you."

            if fighting_style == 3:
                class_feature3 = "Fighting Style: Defense: While you are wearing armor, you gain a +1 bonus to AC."
    
            if fighting_style == 4:
                class_feature3 = "Fighting Style: Dueling: When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon."

            if fighting_style == 5:
                class_feature3 = "Fighting Style: Druidic Warrior. You learn two cantrips of your choice from the Druid spell list. They count as ranger spells for you, and Wisdom is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the Druid spell list."

            if fighting_style == 6:
                class_feature3 = "Fighting Style: Interception: When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction."

            if fighting_style == 7:
                class_feature3 = "Fighting Style: Protection: When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield."

            if fighting_style == 9:
                class_feature3 = "Fighting Style: Thrown Weapon Fighting: You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll."

            if fighting_style == 10:
                class_feature3 = "Fighting Style: Two-Weapon Fighting: When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack."
    
            if fighting_style == 11:
                class_feature3 = "Fighting Style: Unarmed Fighting: Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."

            if fighting_style == 12:
                class_feature3 = "Fighting Style: Close Quarters Shooter (UA): When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks."

            if fighting_style == 13:
                class_feature3 = "Fighting Style: Mariner (UA): As long as you are not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class."

            if fighting_style == 14:
                class_feature3 = "Fighting Style: Tunnel Fighter (UA): As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach."


            class_feature4 = ("Spellcasting: By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does.\nWisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one. Spell save DC = 8 + your proficiency bonus + your Wisdom modifier, Spell attack modifier = your proficiency bonus + your Wisdom modifier. At 2nd level, you can use a druidic focus as a spellcasting focus for your ranger spells. A druidic focus might be a sprig of mistletoe or holly, a wand or rod made of yew or another special wood, a staff drawn whole from a living tree, or an object incorporating feathers, fur, bones, and teeth from sacred animals.\n"
                              "Your spellcasting chart is shown below\n"
                                 "                         Slot Types\n"
                                       "Level       Spells Known           1st     2nd     3rd     4th     5th\n"
                                       "  1              \n"     
                                       "  2               2                2\n"
                                       "  3               3                3\n"
                                       "  4               3                3\n"
                                       "  5               4                4       2\n"
                                       "  6               4                4       2\n"
                                       "  7               5                4       3\n"
                                       "  8               5                4       3\n"
                                       "  9               6                4       3       2\n"
                                       "  10              6                4       3       2\n"
                                       "  11              7                4       3       3\n"
                                       "  12              7                4       3       3\n"
                                       "  13              8                4       3       3       1\n"
                                       "  14              8                4       3       3       1\n"
                                       "  15              9                4       3       3       2\n"
                                       "  16              9                4       3       3       2\n"
                                       "  17              10               4       3       3       3       1\n"
                                       "  18              10               4       3       3       3       1\n"
                                       "  19              11               4       3       3       3       2\n"
                                       "  20              11               4       3       3       3       2\n"
                                       "\n\n")
            level_1_spell1 = ranger_level_1();
            level_1_spell2 = ranger_level_1();
            while  level_1_spell1 == level_1_spell2:
                level_1_spell2 = ranger_level_1();

        if PC_level >= 3:
            level_1_spell3 = ranger_level_1();
            while level_1_spell3 == level_1_spell2 or  level_1_spell3 == level_1_spell1:
                    level_1_spell3 = ranger_level_1();

            alt_feature = randint(1,2)

            if alt_feature == 1:
                class_feature5 = "Primeval Awareness: Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn’t reveal the creatures’ location or number."

            if alt_feature == 2:
                 class_feature5 = "Primeval Awareness:You can focus your awareness through the interconnections of nature: you learn additional spells when you reach certain levels in this class if you don't already know them, as shown in the Primal Awareness Spells table. These spells don't count against the number of ranger spells you know. You can cast each of these spells once without expending a spell slot. Once you cast a spell in this way, you can't do so again until you finish a long rest.\n      Level 3: Speak with Animals, Level 5: Beast Sense, Level 9: Speak with Plants, Level 13: Locate Creature, Level 17: Commune with Nature"


            ranger_conclave = randint(1,7)

            if ranger_conclave == 1:
                PC_subclass = "Beast Master"
                variant_feature = randint(1,2)
                
                if variant_feature == 1:
                    class_feature6 = "Ranger's Companion: t 3rd level, you gain a beast companion that accompanies you on your adventures and is trained to fight alongside you. Choose a beast that is no larger than Medium and that has a challenge rating of 1/4 or lower (appendix D presents statistics for the hawk, mastiff, and panther as examples). Add your proficiency bonus to the beast’s AC, attack rolls, and damage rolls, as well as to any saving throws and skills it is proficient in. Its hit point maximum equals its normal maximum or four times your ranger level, whichever is higher. Like any creature, the beast can spend Hit Dice during a short rest.\n The beast obeys your commands as best as it can. It takes its turn on your initiative. On your turn, you can verbally command the beast where to move (no action required by you). You can use your action to verbally command it to take the Attack, Dash, Disengage, or Help action. If you don’t issue a command, the beast takes the Dodge action. Once you have the Extra Attack feature, you can make one weapon attack yourself when you command the beast to take the Attack action. While traveling through your favored terrain with only the beast, you can move stealthily at a normal pace.\nIf you are incapacitated or absent, the beast acts on its own, focusing on protecting you and itself. The beast never requires your command to use its reaction, such as when making an opportunity attack. If the beast dies, you can obtain another one by spending 8 hours magically bonding with another beast that isn’t hostile to you, either the same type of beast as before or a different one."

                if variant_feature == 2:
                    class_feature6 = "Primal Companion: You magically summon a primal beast, which draws strength from your bond with nature. The beast is friendly to you and your companions and obeys your commands. Choose its stat block-Beast of the Land, Beast of the Sea, or Beast of the Sky-which uses your proficiency bonus (PB) in several places. You also determine the kind of animal the beast is, choosing a kind appropriate for the stat block. Whatever kind you choose, the beast bears primal markings, indicating its mystical origin. In combat, the beast acts during your turn. It can move and use its reaction on its own, but the only action it takes is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. You can also sacrifice one of your attacks when you take the Attack action to command the beast to take the Attack action. If you are incapacitated, the beast can take any action of its choice, not just Dodge. If the beast has died within the last hour, you can use your action to touch it and expend a spell slot of 1st level or higher. The beast returns to life after 1 minute with all its hit points restored. When you finish a long rest, you can summon a different primal beast. The new beast appears in an unoccupied space within 5 feet of you, and you choose its stat block and appearance. If you already have a beast from this feature, it vanishes when the new beast appears. The beast also vanishes if you die."

            if ranger_conclave == 2:
                PC_subclass = "Fey Wanderer"
                class_feature6 = ("Fey Wanderer Magic: Starting at 3rd level, you learn an additional spell when you reach certain levels in this class, as shown in the Fey Wanderer Spells table. The spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know:\n      Level 3: Charm Person\n      Level 5: Misty Step\n      Level 9: Dispel Magic\n      Level 13: Dimension Door\n      Level 17: Mislead\nYou also possess a preternatural blessing from a fey ally or a place of fey power. Choose your blessing from the Feywild Gifts table or determine it randomly.\nGifts Table (d6): 1. Illusory butterflies flutter around you while you take a short or long rest. 2. Fresh, seasonal flowers sprout from your hair each dawn. 3. You faintly smell of cinnamon, lavender, nutmeg, or another comforting herb or spice. 4. Your shadow dances while no one is looking directly at it. 5. Horns or antlers sprout from your head. 6. Your skin and hair change color to match the season at each dawn."
                                  "Dreadful Strikes: At 3rd level, you can augment your weapon strikes with mind-scarring magic, drawn from the gloomy hollows of the Feywild. When you hit a creature with a weapon, you can deal an extra 1d4 psychic damage to the target, which can take this extra damage only once per turn. The extra damage increases to 1d6 when you reach 11th level in this class."
                                  "Otherworldly Glamour: Additionally at 3rd level, your fey qualities give you a supernatural charm. As a result, whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (minimum of +1).")
                
                
                if deception == 1 and performance == 1:
                    persuasion = 1

                if persuasion == 1 and deception == 1:
                    performance = 1

                if performance == 1 and persuasion == 1:
                    deception = 1

                else:
                    skill1 = randint(1,3)
                    if skill1 == 1:
                        deception = 1
                    if skill1 == 2:
                        performance = 1
                    if skill1 == 3:
                        persuasion = 1



            if ranger_conclave == 3:
                PC_subclass = "Gloom Stalker Conclave"
                class_feature6 = ("Gloom Stalker Magic: Starting at 3rd level, you learn an additional spell when you reach certain levels in this class, as shown in the Gloom Stalker Spells table. The spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know:\n      Level 3: Disguise Self\n      Level 5: Rope Trick\n      Level 9: Fear\n      Level 13: Greater Invisibility\n      Level 17: Seeming\n"
                                  "Dread Ambusher: At 3rd level, you master the art of the ambush. You can give yourself a bonus to your initiative rolls equal to your Wisdom modifier. At the start of your first turn of each combat, your walking speed increases by 10 feet, which lasts until the end of that turn. If you take the Attack action on that turn, you can make one additional weapon attack as part of that action. If that attack hits, the target takes an extra 1d8 damage of the weapon's damage type.\n"
                                  "Umbral Sight: At 3rd level, you gain darkvision out to a range of 60 feet. If you already have darkvision from your race, its range increases by 30 feet. You are also adept at evading creatures that rely on darkvision. While in darkness, you are invisible to any creature that relies on darkvision to see you in that darkness.")


            if ranger_conclave == 4:
                PC_subclass = "Horizon Walker Conclave"
                class_feature6 = ("Horizon Walker Magic: Starting at 3rd level, you learn an additional spell when you reach certain levels in this class, as shown in the Horizon Walker Spells table. The spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know:\n      Level 3: Protection from Evil and Good\n      Level 5: Misty Step\n      Level 9: Haste\n      Level 13: Banishment\n      Level 17: Teleportation Circle\n"
                                  "Detect Portal: At 3rd level, you gain the ability to magically sense the presence of a planar portal. As an action, you detect the distance and direction to the closest planar portal within 1 mile of you. Once you use this feature, you can't use it again until you finish a short or long rest.\n"
                                  "Planar Warrior: At 3rd level, you learn to draw on the energy of the multiverse to augment your attacks. As a bonus action, choose one creature you can see within 30 feet of you. The next time you hit that creature on this turn with a weapon attack, all damage dealt by the attack becomes force damage, and the creature takes an extra 1d8 force damage from the attack. When you reach 11th level in this class, the extra damage increases to 2d8.")

            if ranger_conclave == 5:
                PC_subclass = "Hunter Conclave"
                variant_feature = randint(1,3)
                if variant_feature == 1:
                    class_feature6 = "Hunter's Prey: Colossus Slayer. Your tenacity can wear down the most potent foes. When you hit a creature with a weapon attack, the creature takes an extra 1d8 damage if it’s below its hit point maximum. You can deal this extra damage only once per turn."
    
                if variant_feature == 2:
                    class_feature6 = "Hunter's Prey: Giant Killer. When a Large or larger creature within 5 feet of you hits or misses you with an attack, you can use your reaction to attack that creature immediately after its attack, provided that you can see the creature."
                
                if variant_feature == 3:
                    class_feature6 = "Hunter's Prey: Horde Breaker. Once on each of your turns when you make a weapon attack, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon."


            if ranger_conclave == 6:
                PC_subclass = "Monster Slayer Conclave"
                class_feature6 = ("Monster Slayer Magic: Starting at 3rd level, you learn an additional spell when you reach certain levels in this class, as shown in the Monster Slayer Spells table. The spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know:\n      Level 3: Protection from Evil and Good\n      Level 5: Zone of Truth\n      Level 9: Magic Circle\n      Level 13: Banishment\n      Level 17: Hold Monster\n"
                                  "Hunter's Sense: At 3rd level, you gain the ability to peer at a creature and magically discern how best to hurt it. As an action, choose one creature you can see within 60 feet of you. You immediately learn whether the creature has any damage immunities, resistances, or vulnerabilities and what they are. If the creature is hidden from divination magic, you sense that it has no damage immunities, resistances, or vulnerabilities. You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses of it when you finish a long rest."
                                  "Slayer's Prey: Starting at 3rd level, you can focus your ire on one foe, increasing the harm you inflict on it. As a bonus action, you designate one creature you can see within 60 feet of you as the target of this feature. The first time each turn that you hit that target with a weapon attack, it takes an extra 1d6 damage from the weapon. This benefit lasts until you finish a short or long rest. It ends early if you designate a different creature.")

            if ranger_conclave == 7:
                PC_subclass = "Swarmkeeper"
                class_feature6 = ("Gathered Swarm: At 3rd level, a swarm of intangible nature spirits has bonded itself to you and can assist you in battle. Until you die, the swarm remains in your space, crawling on you or flying and skittering around you within your space. You determine its appearance. Once on each of your turns, you can cause the swarm to assist you in one of the following ways, immediately after you hit a creature with an attack:\n    The attack's target takes 1d6 piercing damage from the swarm\n    The attack's target must succeed on a Strength saving throw against your spell save DC or be moved by the swarm up to 15 feet horizontally in a direction of your choice\n    You are moved by the swarm 5 feet horizontally in a direction of your choice\n\n"
                                  "Swarmkeeper Magic: Also at 3rd level, you learn the Mage Hand cantrip if you don't already know it. When you cast it, the hand takes the form of your swarming nature spirits. You also learn an additional spell of 1st level or higher when you reach certain levels in this class, as shown in the Swarmkeeper Spells table. Each spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know\n"
                                  "      Level 3: Faerie Fire, Mage Hand\n      Level 5:  	Web\n      Level 9: Gaseous Form\n      Level 13: Arcane Eye\n      Level 17: Insect Plague")
                cantrip1 = "Mage Hand"

        if PC_level >= 4:
            feat1 = ability_score_improvement();
            class_feature7 = "Martial Versatility: Whenever you reach a level in this class that grants the Ability Score Improvement feature (4,8,12,16,19), you can replace a fighting style you know with another fighting style available to rangers. This replacement represents a shift of focus in your martial practice."

        if PC_level >= 5:
            PC_prof_bonus = 3
            level_2_spell1 = ranger_level_2();
            class_feature8 = "Extra Attack: Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."

        #Lvl 6 covered earlier
        if PC_level >= 7:
            level_2_spell2 = ranger_level_2();
            while  level_2_spell1 == level_2_spell2:
                level_2_spell2 = ranger_level_2();

            if ranger_conclave == 1:
                class_feature9 = "Exceptional Training: Beginning at 7th level, on any of your turns when your beast companion doesn’t attack, you can use a bonus action to command the beast to take the Dash, Disengage, or Help action on its turn. In addition, the beast’s attacks now count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."

            if ranger_conclave == 2:
                class_feature9 = "Beguiling Twist: Beginning at 7th level, the magic of the Feywild guards your mind. You have advantage on saving throws against being charmed or frightened. In addition, whenever you or a creature you can see within 120 feet of you succeeds on a saving throw against being charmed or frightened, you can use your reaction to force a different creature you can see within 120 feet of you to make a Wisdom saving throw against your spell save DC. If the save fails, the target is charmed or frightened by you (your choice) for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a successful save."

            if ranger_conclave == 3:
                class_feature9 = "Iron Mind: By 7th level, you have honed your ability to resist the mind-altering powers of your prey. You gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice)."

            if ranger_conclave == 4:
                class_feature9 = "Ethereal Step: At 7th level, you learn to step through the Ethereal Plane. As a bonus action on your turn, you can cast the Etherealness spell with this feature, without expending a spell slot, but the spell ends at the end of the current turn. Once you use this feature, you can’t use it again until you finish a short or long rest."

            if ranger_conclave == 5:

                variant_feature = randint(1,3)
                if variant_feature == 1:
                    class_feature9 = "Defensive Tactics: Escape the Horde. Opportunity attacks against you are made with disadvantage."

                if variant_feature == 2:
                    class_feature9 = "Defensive Tactics: Multiattack Defense. When a creature hits you with an attack, you gain a +4 bonus to AC against all subsequent attacks made by that creature for the rest of the turn."

                if variant_feature == 3:
                    class_feature9 = "Defensive Tactics: Steel Will. You have advantage on saving throws against being frightened."


            if ranger_conclave == 6:
                class_feature9 = "Supernatural Defense: At 7th level, you gain extra resilience against your prey’s assaults on your mind and body. Whenever the target of your Slayer’s Prey forces you to make a saving throw and whenever you make an ability check to escape that target's grapple, add 1d6 to your roll."

            if ranger_conclave == 7:
                class_feature9 = "Writhing Tide: Beginning at 7th level, you can condense part of your swarm into a focused mass that lifts you up. As a bonus action, you gain a flying speed of 10 feet and can hover. This effect lasts for 1 minute or until you are incapacitated. You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."

        if PC_level >= 8:
            feat2 = ability_score_improvement();
            class_feature10 = "Land's Stride: Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard. n addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the Entangle spell."

        if PC_level >= 9:
            PC_prof_bonus = 4
            level_3_spell1 = ranger_level_3();


        if PC_level >= 10:
            variant_feature = randint(1,2)
            if variant_feature == 1:
                class_feature11 = "Hide in Plain Sight: Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage. Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit."

            if variant_feature == 2: 
                class_feature11 = "Nature's Veil: You draw on the powers of nature to hide yourself from view briefly. As a bonus action, you can magically become invisible, along with any equipment you are wearing or carrying, until the start of your next turn. You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."

        if PC_level >= 11:

            level_3_spell2 = ranger_level_3();
            while  level_3_spell1 == level_3_spell2:
                level_3_spell2 = ranger_level_3();
           

            if ranger_conclave == 1:
                class_feature12 = "Bestial Fury: Starting at 11th level, when you command your beast companion to take the Attack action, the beast can make two attacks, or it can take the Multiattack action if it has that action."

            if ranger_conclave == 2:
                class_feature12 = "Fey Reinforcements: At 11th level, the royal courts of the Feywild have blessed you with the assistance of fey beings: you know the spell Summon Fey. It doesn't count against the number of ranger spells you know, and you can cast it without a material component. You can also cast it once without using a spell slot, and you regain the ability to do so when you finish a long rest. Whenever you start casting the spell, you can modify it so that it doesn't require concentration. If you do so, the spell's duration becomes 1 minute for that casting."

            if ranger_conclave == 3:
                class_feature12 = "Stalker's Flurry: At 11th level, you learn to attack with such unexpected speed that you can turn a miss into another strike. Once on each of your turns when you miss with a weapon attack, you can make another weapon attack as part of the same action."

            if ranger_conclave == 4:
                class_feature12 = "Distant Strike: At 11th level, you gain the ability to pass between the planes in a blink of an eye. When you use the Attack action, you can teleport up to 10 feet before each attack to an unoccupied space you can see. If you attack at least two different creatures with the action, you can make one additional attack with it against a third creature."

            if ranger_conclave == 5:

                variant_feature = randint(1,2)
                if variant_feature == 1:
                    class_feature12 = "Multiattack: Volley. You can use your action to make a ranged attack against any number of creatures within 10 feet of a point you can see within your weapon’s range. You must have ammunition for each target, as normal, and you make a separate attack roll for each target"

                if variant_feature == 2:
                    class_feature12 = "Multiattack: Whirlwind Attack. You can use your action to make melee attacks against any number of creatures within 5 feet of you, with a separate attack roll for each target."


            if ranger_conclave == 6:
                class_feature12 = "Magic-User's Nemesis: At 11th level, you gain the ability to thwart someone else's magic. When you see a creature casting a spell or teleporting within 60 feet of you, you can use your reaction to try to magically foil it. The creature must succeed on a Wisdom saving throw against your spell save DC, or its spell or teleport fails and is wasted. Once you use this feature, you can't use it again until you finish a short or long rest."

            if ranger_conclave == 7:
                class_feature12 = "Mighty Swarm: At 11th level, your Gathered Swarm grows mightier in the following ways: The damage of Gathered Swarm increases to 1d8, if a creature fails its saving throw against being moved by the Gathered Swarm, you can also cause the swarm to knock the creature prone, and when you are moved by Gathered Swarm, it gives you half cover until the start of your next turn."


            
   

        if PC_level >= 12:
            feat3 = ability_score_improvement();

        if PC_level >= 13:
            PC_prof_bonus = 5
            level_4_spell1 = ranger_level_4();

        if PC_level >= 14:
            class_feature13 = "Vanish: Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail."

        if PC_level >= 15:
            level_4_spell2 = ranger_level_4();
            while  level_4_spell1 == level_4_spell2:
                level_4_spell2 = ranger_level_4();

            if ranger_conclave == 1:
                class_feature14 = "Share Spells: Beginning at 15th level, when you cast a spell targeting yourself, you can also affect your beast companion with the spell if the beast is within 30 feet of you."

            if ranger_conclave == 2:
                class_feature14 = "Misty Wanderer: When you reach 15th level, you can slip in and out of the Feywild to move in a blink of an eye: you can cast Misty Step without expending a spell slot. You can do so a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a long rest. In addition, whenever you cast Misty Step, you can bring along one willing creature you can see within 5 feet of you. That creature teleports to an unoccupied space of your choice within 5 feet of your destination space."

            if ranger_conclave == 3:
                class_feature14 = "Shadowy Dodge: Starting at 15th level, you can dodge in unforeseen ways, with wisps of supernatural shadow around you. Whenever a creature makes an attack roll against you and doesn't have advantage on the roll, you can use your reaction to impose disadvantage on it. You must use this feature before you know the outcome of the attack roll."

            if ranger_conclave == 4:
                class_feature14 = "Spectral Defense: At 15th level, your ability to move between planes enables you to slip through the planar boundaries to lessen the harm done to you during battle. When you take damage from an attack, you can use your reaction to give yourself resistance to all of that attack's damage on this turn."

            if ranger_conclave == 5:

                variant_feature = randint(1,3)
                if variant_feature == 1:
                    class_feature14 = "Superior Hunter's Defense: Evasion. When you are subjected to an effect, such as a red dragon’s fiery breath or a lightning bolt spell, that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail"

                if variant_feature == 2:
                    class_feature14 = "Superior Hunter's Defense: Stand Against the Tide. When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice."

                if variant_feature == 3:
                    class_feature14 = "Superior Hunter's Defense: Uncanny Dodge. When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you."


            if ranger_conclave == 6:
                class_feature14 = "Slayer's Counter: At 15th level, you gain the ability to counterattack when your prey tries to sabotage you. If the target of your Slayer’s Prey forces you to make a saving throw, you can use your reaction to make one weapon attack against the quarry. You make this attack immediately before making the saving throw. If the attack hits, your save automatically succeeds, in addition to the attack’s normal effects."

            if ranger_conclave == 7:
                class_feature14 = "Swarming Dispersal: When you reach 15th level, you can discorporate into your swarm, avoiding danger. When you take damage, you can use your reaction to give yourself resistance to that damage. You vanish into your swarm and then teleport to an unoccupied space that you can see within 30 feet of you, where you reappear with the swarm. You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."

        if PC_level >= 16:
            feat4 = ability_score_improvement();

        if PC_level >= 17:
            PC_prof_bonus = 6
            level_5_spell1 = ranger_level_5();

        if PC_level >= 18:
            class_feature15 = "Feral Senses: At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it. You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened."

            
        if PC_level >= 19:
            feat5 = ability_score_improvement();
            level_5_spell2 = ranger_level_5();
            while  level_5_spell1 == level_5_spell2:
                level_5_spell2 = ranger_level_5();


        if PC_level >= 20:
            class_feature16 = "Foe Slayer: At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied."




print ("Welcome to the Random Character Sheet Generator\n")  

print("What level do you want your character to start at?\nType the level number (Ex: 2)")

PC_level = int(input(""))
while 1:

    Strength = statroll()
    Dexterity = statroll()
    Constitution = statroll()
    Intelligence = statroll()
    Wisdom = statroll()
    Charisma = statroll()
   
    print("  ")
    print(Strength)
    print(Dexterity)
    print(Constitution)
    print(Intelligence)
    print(Wisdom)
    print(Charisma)

    PC_class = class_selection();
    #PC_class = "Ranger"
    PC_race = race()
    race_features(PC_race)
    PC_allignment = allingment()
    PC_background = background()
    class_features(PC_class,PC_level)

    print("Your charcter sheet is below\n\n\n")

#######################################################

    print("Your character is a level",PC_level, PC_subclass,PC_class)
    print("They are a", PC_subrace,PC_background, "with a", PC_allignment, "allignment")

    print("Stats: \n")
    print("Strength:",Strength)
    print("Dexterity:",Dexterity)
    print("Constitution:",Constitution)
    print("Intelligence:",Intelligence)
    print("Wisdom:",Wisdom)
    print("Charisma:",Charisma)

    print("Their health is:", PC_hp)
    print("You hit dice is ", hit_dice)
    print("Your base walking speed is",speed, "meters")
    print("Your Profciency Bonus is",PC_prof_bonus)

    print("You have advantage on the following saving throws")

    if PC_str_savethrw == 1:
        print("Strength")
    if PC_dex_savethrw == 1:
        print("Dexterity")
    if PC_con_savethrw == 1:
        print("Constitution")
    if PC_wis_savethrw == 1:
        print("Wisdom")
    if PC_int_savethrw == 1:
        print("Intelligence")
    if PC_cha_savethrw == 1:
        print("Charisma")
    
    print("Your stating equipment is:")
    print(background_equipment)
    print(class_equipment)
    print(class_equipment2)
    print(class_equipment3)
    print(class_equipment4)
    print(class_equipment5)
    
    print("Your race and background features are as follows:\n")
    print(feature)
    print(race_feature1)
    print(race_feature2)
    print(race_feature3) 
    print(race_feature4)
    print(race_feature5)
    print(race_feature6)
    print(race_feature7)
    print(class_feature1)
    print(class_feature2)
    print(class_feature3)
    print(class_feature4)
    print(class_feature5)
    print(class_feature6)
    print(class_feature7)
    print(class_feature8)
    print(class_feature9)
    print(class_feature10)
    print(class_feature11)
    print(class_feature12)
    print(class_feature13)
    print(class_feature14)
    print(class_feature15)
    print(class_feature16)
    print(class_feature17)
    
    if caster == "True":
        print("Your known cantrips (in addition to any granted by your class/race) are:")
        print(cantrip1)
        print(cantrip2)
        print(cantrip3)
        print(cantrip4)
        print(cantrip5)
        print(cantrip6)
        print(cantrip7)
        print("Your known 1st level spells (in addition to any granted by your class/race) are:")
        print(level_1_spell1)
        print(level_1_spell2)
        print(level_1_spell3)
        print(level_1_spell4)
        print(level_1_spell5)
        print(level_1_spell6)
        print("Your known 2nd level spells (in addition to any granted by your class/race)  are:")
        print(level_2_spell1)
        print(level_2_spell2)
        print(level_2_spell3)
        print("Your known 3rd level spells (in addition to any granted by your class/race) are:")
        print(level_3_spell1)
        print(level_3_spell2)
        print(level_3_spell3)
        print("Your known 4th level spells (in addition to any granted by your class/race) are:")
        print(level_4_spell1)
        print(level_4_spell2)
        print(level_4_spell3)
        print("Your known 5th level spells (in addition to any granted by your class/race) are:")
        print(level_5_spell1)
        print(level_5_spell2)
        print(level_5_spell3)
        print("Your known 6th level spells (in addition to any granted by your class/race) are:")
        print(level_6_spell1)
        print(level_6_spell2)
        print("Your known 7th level spells (in addition to any granted by your class/race) are:")
        print(level_7_spell1)
        print(level_7_spell2)
        print("Your known 8th level spells (in addition to any granted by your class/race) are:")
        print(level_8_spell1)
        print("Your known 9th level spells (in addition to any granted by your class/race) are:")
        print(level_9_spell1)


    if caster == "Half":
        print("Your known cantrips (in addition to any granted by your class/race) are:")
        print(cantrip1)
        print(cantrip2)
        print(cantrip3)
        print(cantrip4)
        print(cantrip5)
        print(cantrip6)
        print(cantrip7)
        print("Your known 1st level spells (in addition to any granted by your class/race) are:")
        print(level_1_spell1)
        print(level_1_spell2)
        print(level_1_spell3)
        print(level_1_spell4)
        print(level_1_spell5)
        print(level_1_spell6)
        print("Your known 2nd level spells (in addition to any granted by your class/race)  are:")
        print(level_2_spell1)
        print(level_2_spell2)
        print(level_2_spell3)
        print("Your known 3rd level spells (in addition to any granted by your class/race) are:")
        print(level_3_spell1)
        print(level_3_spell2)
        print(level_3_spell3)
        print("Your known 4th level spells (in addition to any granted by your class/race) are:")
        print(level_4_spell1)
        print(level_4_spell2)
        print(level_4_spell3)
        print("Your known 5th level spells (in addition to any granted by your class/race) are:")
        print(level_5_spell1)
        print(level_5_spell2)
        print(level_5_spell3)
        


    print("Your feats are as follows")

    if PC_race == "Human":
            print(human_feat)
    if feat1 != "":
        print(feat1)
    if feat2 != "":
        print(feat2)
    if feat3 != "":
        print(feat3)
    if feat4 != "":
        print(feat4)
    if feat5 != "":
        print(feat5)
    if feat6 != "":
        print(feat6)
    if feat7 != "":
        print(feat7)
    print("\n")

    print("Your Skill Proficinces are as follows:")

    if acrobatics == 1:
            print("acrobatics")
    if animal_handling == 1:
           print("animal_handling")
    if arcana == 1:
          print("arcana")
    if deception == 1:
           print(" deception")
    if history == 1:
           print("history")
    if insight == 1:
          print("insight")
    if intimidation == 1:
           print("intimidation")
    if investigation == 1:
           print("investigation")
    if medicine == 1:
           print("medicine")
    if nature == 1:
           print("nature")
    if preception == 1:
           print("preception")
    if performance == 1:
           print("performance")
    if persuasion == 1:
           print("persuasion")
    if religion == 1:
            print("religion")
    if sleight_of_hand == 1:  
            print("sleight_of_hand")
    if stealth == 1:
            print("stealth")
    if survival == 1:
            print("survival")
    if athletics == 1:
            print("athletics")

    print("Your known languages are:")

    if common == 1:
         print("common")
    if dwarvish == 1:
        print("dwarvish")
    if elvish == 1:
        print("elvish")
    if giant == 1:
        print("giant")
    if gnomish == 1:
        print("gnomish")
    if goblin == 1:
        print("goblin")
    if halfing == 1:
        print("goblin")
    if orc == 1:
        print("orc")
    if abyssal == 1:
        print("abyssal")
    if celestial == 1:
        print("celestial")
    if draconic == 1:
        print("draconic")
    if deep_speech == 1:
        print("deep_speech")
    if infernal == 1:
        print("infernal")
    if primordial == 1:
        print("primordial")
    if sylvan == 1:
        print("sylvan")
    if undercommon == 1:
        print("undercommon")
    if aquan == 1:
        print("aquan")
    if auran == 1:
        print("auran")
    if keldon == 1:
        print("keldon")
    if druidic == 1:
        print("druidic")


    feature = " "
    caster = " "
    background_equipment = " "
    PC_subrace = ""
    PC_subclass = ""
    race_feature1 = ""
    race_feature2 = ""
    race_feature3 = ""
    race_feature4 = ""
    race_feature5 = ""
    race_feature6 = ""
    race_feature7 = ""

    PC_hp = 0
    hit_dice = ""
    speed = 30
    PC_prof_bonus = 2
    
    PC_str_savethrw = 0
    PC_dex_savethrw = 0
    PC_con_savethrw = 0
    PC_int_savethrw = 0
    PC_wis_savethrw = 0
    PC_cha_savethrw = 0
    
    background_equipment= ""
    class_equipment= ""
    class_equipment2= ""
    class_equipment3= ""
    class_equipment4= ""
    class_equipment5= ""
    
    
    feature= ""
    race_feature1= ""
    race_feature2= ""
    race_feature3= "" 
    race_feature4= ""
    race_feature5= ""
    race_feature6= ""
    race_feature7= ""
    class_feature1= ""
    class_feature2= ""
    class_feature3= ""
    class_feature4= ""
    class_feature5= ""
    class_feature6= ""
    class_feature7= ""
    class_feature8= ""
    class_feature9= ""
    class_feature10= ""
    class_feature11= ""
    class_feature12= ""
    class_feature13= ""
    class_feature14= ""
    class_feature15 = ""
    class_feature16 = ""
    class_feature17 = ""
    human_feat = ""
    feat1 = ""
    feat2 = ""
    feat3 = ""
    feat4 = ""
    feat5 = ""
    feat6 = ""
    feat7 = ""

    acrobatics = 0     
    animal_handling =0
    arcana =0
    deception =0
    history =0
    insight =0
    intimidation =0
    investigation =0
    medicine =0
    nature =0
    preception =0
    performance =0
    persuasion =0
    religion =0
    sleight_of_hand =0  
    stealth =0
    survival =0
    athletics =0
    common =1
    dwarvish =0
    elvish =0
    giant =0
    gnomish =0
    goblin =0
    halfing =0
    orc =0
    abyssal =0
    celestial =0
    draconic =0
    deep_speech =0
    infernal =0
    primordial =0
    sylvan =0
    undercommon =0
    aquan =0
    auran =0
    keldon = 0
    druidic = 0

    cantrip1 = ""
    cantrip2 = ""
    cantrip3 = ""
    cantrip4 = ""
    cantrip5 = ""
    cantrip6 = ""
    cantrip7 = ""

    level_1_spell1 = ""
    level_1_spell2 = ""
    level_1_spell3 = ""
    level_1_spell4 = ""
    level_1_spell5 = ""
    level_1_spell6 = ""

    level_2_spell1 = ""
    level_2_spell2 = ""
    level_2_spell3 = ""

    level_3_spell1 = ""
    level_3_spell2 = ""
    level_3_spell3 = ""

    level_4_spell1 = ""
    level_4_spell2 = ""
    level_4_spell3 = ""

    level_5_spell1 = ""
    level_5_spell2 = ""
    level_5_spell3 = ""

    level_6_spell1 = ""
    level_6_spell2 = ""

    level_7_spell1 = ""
    level_7_spell2 = ""

    level_8_spell1 = ""

    level_9_spell1 = ""


    wait = input("Press any key to continue")
