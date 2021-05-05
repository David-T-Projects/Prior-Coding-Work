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

global light_armor
light_armor = 0

global medium_armor
medium_armor = 0

global heavy_armor
heavy_armor = 0

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
        


        lang2 = randint(1,17)
        if lang2 == 1:
            acrobatics = 1
            return "acrobatics"
        if lang2 == 2:
           animal_handling = 1
           return "animal_handling"
        if lang2 == 3:
           arcana = 1
           return "arcana"
        if lang2 == 4:
           deception = 1
           return " deception"
        if lang2 == 5:
           history = 1
           return "history"
        if lang2 == 6:
          insight = 1
          return "insight"
        if lang2 == 7:
           intimidation = 1
           return "intimidatio"
        if lang2 == 8:
           investigation = 1
           return  "investigation"
        if lang2 == 9:
           medicine = 1
           return "medicine"
        if lang2 == 10:
           nature = 1
           return "nature"
        if lang2 == 11:
           preception = 1
           return "preception"
        if lang2 == 12:
           performance = 1
           return "[erformance"
        if lang2 == 13:
           persuasion = 1
           return "persuasion"
        if lang2 == 14:
            religion = 1
            return "religion"
        if lang2 == 15:
            sleight_of_hand = 1
            return "sleight_of_hand"
        if lang2 == 16:
            stealth = 1
            return "stealth"
        if lang2 == 17:
            survival = 1
            return "survival"
        if lang2 == 18:
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
 

def druid_cantrip():
     choice = randint(1,17)
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
      }
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

    if PC_class == "Barbarian":

       hit_dice = "1d12 per barbarian level"
       first_lvl_hp = 12 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
           high_lvl_hp += randint(1,12)+ modifier(Constitution)
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
                         "Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again."
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
           feat4= ability_score_improvement()

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
           high_lvl_hp += randint(1,8)+ modifier(Constitution)
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
           class_equipment = "A lute"
       if equipment == 2:
           class_equipment3 = "Any musical instrument"
       class_equipment4 = "Leather armor and a dagger"
       
       class_feature1 = "You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations.\n Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability.\nIn addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one.\nSpell save DC = 8 + your proficiency bonus + your Charisma modifier\nSpell attack modifier = your proficiency bonus + your Charisma modifier\nYou can cast any bard spell you know as a ritual if that spell has the ritual tag.\nYou can use a musical instrument as a spellcasting focus for your bard spells."
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

       class_feature3 = ("You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6."
                         "\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails.Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time."
                         "You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.\n"
                         "Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.")
       if PC_level >= 2:
           class_feature4 = "Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus."
           class_feature5 = "Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance spend one or more Hit Dice to regain hit points at the end of the short rest, each of those creatures regains an extra 1d6 hit points.\nThe extra Hit Points increase when you reach certain levels in this class: to 1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th level."
           class_feature6 = "At 2nd level, if a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost."
           
           level_1_spell5 = bard_level_1()
           while level_1_spell1 == level_1_spell5 or  level_1_spell2 == level_1_spell5 or level_1_spell3 == level_1_spell5 or level_1_spell4 == level_1_spell5:
                level_1_spell5 = bard_level_1()


       if PC_level >= 3:
           class_feature8 = "At 3rd level, choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. At 10th level, you can choose another two skill proficiencies to gain this benefit."
           
           level_2_spell1 = bard_level_2()

           bard_school_choice = randint(1,11)

           if bard_school_choice == 1:
               PC_subclass = "College of Creation"
               class_feature7 = ("When you join the College of Creation at 3rd level, whenever you give a creature a Bardic Inspiration die, you can utter a note from the Song of Creation to create a Tiny mote of potential, which orbits within 5 feet of that creature. The mote is intangible and invulnerable, and it lasts until the Bardic Inspiration die is lost. The mote looks like a musical note, a star, a flower, or another symbol of art or life that you choose."
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
               class_feature7 = ("Starting at 3rd level, you are a master at saying the right thing at the right time. When you make a Charisma (Persuasion) or Charisma (Deception) check, you can treat a d20 roll of 9 or lower as a 10.\n"
                                 "Also at 3rd level, you can spin words laced with magic that unsettle a creature and cause it to doubt itself. As a bonus action, you can expend one use of your Bardic Inspiration and choose one creature you can see within 60 feet of you. Roll the Bardic Inspiration die. The creature must subtract the number rolled from the next saving throw it makes before the start of your next turn.")
               

           if bard_school_choice == 3:
               PC_subclass = "College of Glamour"
               class_feature7 = ("When you join the College of Glamour at 3rd level, you gain the ability to weave a song of fey magic that imbues your allies with vigor and speed.\n"
                                  "As a bonus action, you can expend one use of your Bardic Inspiration to grant yourself a wondrous appearance. When you do so, choose a number of creatures you can see and who can see you within 60 feet of you, up to a number equal to your Charisma modifier (minimum of one). Each of them gains 5 temporary hit points. When a creature gains these temporary hit points, it can immediately use its reaction to move up to its speed, without provoking opportunity attacks."
                                  "\nThe number of temporary hit points increases when you reach certain levels in this class, increasing to 8 at 5th level, 11 at 10th level, and 14 at 15th level."
                                  "\nStarting at 3rd level, you can charge your performance with seductive, fey magic. If you perform for at least 1 minute, you can attempt to inspire wonder in your audience by singing, reciting a poem, or dancing. At the end of the performance, choose a number of humanoids within 60 feet of you who watched and listened to all of it, up to a number equal to your Charisma modifier (minimum of one)\n"
                                  "Each target must succeed on a Wisdom saving throw against your spell save DC or be charmed by you. While charmed in this way, the target idolizes you, it speaks glowingly of you to anyone who speaks to it, and it hinders anyone who opposes you, avoiding violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies.\n"
                                  "If a target succeeds on its saving throw, the target has no hint that you tried to charm it. Once you use this feature, you can’t use it again until you finish a short or long rest.")

           if bard_school_choice == 4:
               PC_subclass = "College of Lore"
               class_feature7 = "You learn how to use your wit to distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the DM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed."
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
               class_feature7 = ("You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.\n"
                                "Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\n"
                                "Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack."
                                "In addition to either style, if you’re proficient with a simple or martial melee weapon, you can use it as a spellcasting focus for your bard spells.")

           if bard_school_choice == 6:
               PC_subclass = "College of Valor"
               medium_armor = 1
               shields = 1
               martial_weapons = 1
               class_feature7 = "You learn to inspire others in battle. A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses."

           if bard_school_choice == 7:
               PC_subclass = "College of Whispers"
               class_feature7 = ("When you join the College of Whispers at 3rd level, you gain the ability to make your weapon attacks magically toxic to a creature's mind. When you hit a creature with a weapon attack, you can expend one use of your Bardic Inspiration to deal an additional 2d6 psychic damage to that target. You can do so only once per round on your turn.\n"
                                "The psychic damage increases when you reach certain levels in this class, increasing to 3d6 at 5th level, 5d6 at 10th level, and 8d6 at 15th level.\n"
                                "At 3rd level, you learn to infuse innocent-seeming words with an insidious magic that can inspire terror. If you speak to a humanoid alone for at least 1 minute, you can attempt to seed paranoia and fear into its mind. At the end of the conversation, the target must succeed on a Wisdom saving throw against your spell save DC or be frightened of you or another creature of your choice. The target is frightened in this way for 1 hour, until it is attacked or damaged, or until it witnesses its allies being attacked or damaged."
                                "\nIf the target succeeds on its saving throw, the target has no hint that you tried to frighten it. Once you use this feature, you can’t use it again until you finish a short rest or long rest.")
         
           if bard_school_choice == 8:
               PC_subclass = "College of Spirits"
               class_feature7 = ("At 3rd level, you can reach out to spirits to guide you and others. You learn the Guidance cantrip, which doesn’t count against the number of bard cantrips you know. For you, it has a range of 60 feet when you cast it.\n"
                                 "At 3rd level, your practice of contacting spirits can employ special tools. You can use the following objects as a spellcasting focus for your bard spells: a candle, a crystal ball, a talking board, a tarokka deck, or a skull.\n"
                                 "At 3rd level, you reach out to spirits who tell their tales through you. While you are holding your Spiritual Focus, you can use a bonus action to expend one use of your Bardic Inspiration and roll on the Spirits’ Tales table using your Bardic Inspiration die to determine the tale told. You retain the tale in mind until you bestow the tale’s effect or you finish a short or long rest.\n"
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
               class_feature7 = ("When you join the College of Dirge Singers at 3rd level, you learn to strengthen the hearts of your troops and stir them to greatness. You learn the Guidance cantrip, which is considered a bard spell for you, but doesn’t count against your number of cantrips known.\Andditionally, as a bonus action, you can expend one use of your Bardic Inspiration to inspire multiple allies. When you do so, choose two creatures within 60 feet of you that can hear you. Each creature gains one Bardic Inspiration die.\nYour Bardic Inspiration die does not change at 5th level, but remains a d6; it becomes a d8 at 10th level, and a d10 at 15th level.\n"
                                "Also at 3rd level, you gain proficiency in either History or Performance. If you are already proficient in both of these skills, you gain proficiency in one of the following skills of your choice: Arcana, Intimidation, or Persuasion.\n In addition, choose either History or Performance. Your proficiency bonus is doubled for any ability check you make that uses that skill.")

           if bard_school_choice == 10:
               PC_subclass = "College of the Maestro"
               class_feature7 = ("When you join the College of the Maestro at 3rd level, you gain one additional use of your Bardic Inspiration feature.\nThis feature grants you another additional use of Bardic Inspiration at 6th level, and again at 14th level."
                                 "You've been trained in the bardic art of magically manipulating the sounds of combat into a concert of powerful melodies that can alter the very battlefield around you.\nWhen you select this bardic school at 3rd level, you learn 2 conducting techniques of your choice, shown below. All techniques require at least one free hand, baton, or wand to utilize. For these techniques to function, you must be able to see your target, and they must be able to hear you.\nYou learn 1 additional conducting technique of your choice at 6th and 14th level. Each time you learn a new technique, you can also replace one technique you know with a different one.\n"
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
               class_feature7 = ("When you join the College of Satire at 3rd level, you gain proficiency with thieves’ tools. You also gain proficiency in Sleight of Hand and one additional skill of your choice. If you are already proficient with thieves’ tools or in Sleight of Hand, choose another skill proficiency for each proficiency you already have.\n"
                                "At 3rd level, you master a variety of acrobatic techniques that allow you to evade danger. As a bonus action, you can tumble. When you tumble, you gain the following benefits for the rest of your turn:\n"
                                "You gain the benefits of taking the Dash and Disengage actions.\n"
                                "You gain a climbing speed equal to your current speed.\n"
                                "You take half damage from falling.\n")

       if PC_level >= 4:
           level_2_spell2 = bard_level_2()
           while level_2_spell1 == level_2_spell2:
               level_2_spell2 = bard_level_2()

           cantrip3 = bard_cantrip()
           while cantrip3 == cantrip2 or cantrip3 == cantrip1:
                cantrip3 = bard_cantrip()
           feat1 = ability_score_improvement()
           class_feature7 = "Whenever you reach a level in this class that grants the Ability Score Improvement feature (4,8,12,16,19), you can do one of the following, representing a change in focus as you use your skills and magic:\n1. Replace one of the skills you chose for the Expertise feature with one of your other skill proficiencies that isn't benefiting from Expertise.\n 2. Replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the bard spell list."

       if PC_level >= 5:
           
           PC_prof_bonus = 3
           level_3_spell1 = bard_level_3()
           class_feature8 = "Beginning when you reach 5th level, you regain all of your expended uses of Bardic Inspiration when you finish a short or long rest."

       if PC_level >= 6:
           class_feature9 = "At 6th level, you gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required)."

           level_3_spell2 = bard_level_3()

           while level_3_spell1 == level_3_spell2:
                 level_3_spell2 = bard_level_3()

           if bard_school_choice == 1:
               PC_subclass = "College of Creation"
               class_feature10 = ("By 6th level, as an action, you can target a Large or smaller nonmagical item you can see within 30 feet of you and animate it. The animate item uses the Dancing Item stat block, which uses your proficiency bonus (PB), The item is friendly to you and your companions and obeys your commands. It lives for 1 hour, until it is reduced to 0 hit points, or until you die."
                                 "\nIn combat, the item shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the item can take any action of its choice, not just Dodge.\n"
                                 "When you use your Bardic Inspiration feature, you can command the item as part of the same bonus action you use for Bardic Inspiration."
                                 "\nOnce you animate an item with this feature, you can't do so again until you finish a long rest, unless you expend a spell slot of 3rd level or higher to use this feature again. You can have only one item animated by this feature at a time; if you use this action and already have a dancing item from this feature, the first one immediately becomes inanimate.")

           if bard_school_choice == 2:
               PC_subclass = "College of Eloquence"
               class_feature10 = "At 6th level, your inspiring words are so persuasive that others feel driven to succeed. When a creature adds one of your Bardic Inspiration dice to its ability check, attack roll, or saving throw and the roll fails, the creature can keep the Bardic Inspiration die\nAlso at 6th level, you have gained the ability to make your speech intelligible to any creature. As an action, choose one or more creatures within 60 feet of you, up to a number equal to your Charisma modifier (minimum of one creature). The chosen creatures can magically understand you, regardless of the language you speak, for 1 hour.\nOnce you use this feature, you can't use it again until you finish a long rest, unless you expend a spell slot to use it again."

           if bard_school_choice == 3:
               PC_subclass = "College of Glamour"
               class_feature10 = ("At 6th level, you gain the ability to cloak yourself in a fey magic that makes others want to serve you. As a bonus action, you cast Command, without expending a spell slot, and you take on an appearance of unearthly beauty for 1 minute or until your concentration ends (as if you were concentrating on a spell). During this time, you can cast Command as a bonus action on each of your turns, without expending a spell slot.\n"
                                  "Any creature charmed by you automatically fails its saving throw against the Command you cast with this feature."
                                  "\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                                 
           if bard_school_choice == 4:
               PC_subclass = "College of Lore"
               class_feature10 = "At 6th level, you learn two spells of your choice from any class. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. The chosen spells count as bard spells for you but don't count against the number of bard spells you know."

           if bard_school_choice == 5:
               PC_subclass = "College of Swords"
               class_feature10 = "Starting at 6th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."

           if bard_school_choice == 6:
               PC_subclass = "College of Valor"
               class_feature10 = "Starting at 6th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."

           if bard_school_choice == 10:
               PC_subclass = "College of Whispers"
               class_feature10 = ("At 6th level, you gain the ability to adopt a humanoid's persona. When a humanoid dies within 30 feet of you, you can magically capture its shadow using your reaction. You retain this shadow until you use it or you finish a long rest.\n"
                                "You can use the shadow as an action. When you do so, it vanishes, magically transforming into a disguise that appears on you. You now look like the dead person, but healthy and alive. This disguise lasts for 1 hour or until you end it as a bonus action.\n"
                                "While you're in the disguise, you gain access to all information that the humanoid would freely share with a casual acquaintance. Such information includes general details on its background and personal life, but doesn't include secrets. The information is enough that you can pass yourself off as the person by drawing on its memories."
                                "\nAnother creature can see through this disguise by succeeding on a Wisdom (Insight) check contested by your Charisma (Deception) check. You gain a +5 bonus to your check.\nOnce you capture a shadow with this feature, you can't capture another one with it until you finish a short or long rest.")
         
           if bard_school_choice == 8:
               PC_subclass = "College of Spirits"
               class_feature10 = ("At 6th level, you can channel spirits to gain insights into magic. You can conduct an hour-long ritual channeling spirits (which can be done during a short or long rest) using your Spiritual Focus.\n"
                                 "You can conduct the ritual with a number of creatures equal to your proficiency bonus (including yourself). At the end of the ritual, you temporarily learn one spell of your choice from any class.\n"
                                 "The spell you choose must be of a level equal to the number of creatures that conducted the ritual or less, the spell must of a level you can cast, and it must be in the school of divination or necromancy. The chosen spell counts as a bard spell for you but doesn’t count against the number of bard spells you know.\n"
                                 "Once you perform the ritual, you can’t do so again until you start a long rest, and you know the chosen spell until you start a long rest.")
          
           if bard_school_choice == 9:
               PC_subclass = "College of the Dire Singer"
               class_feature10 = "Starting at 6th level, you excel at inspiring and directing soldiers in battle. When a creature that has a Bardic Inspiration die from you takes the Attack action on its turn, you can use your reaction to allow it an additional weapon attack. The creature rolls the Bardic Inspiration die, adding the number rolled to its weapon damage roll."

           if bard_school_choice == 10:
               PC_subclass = "College of the Maestro"
               class_feature10 = ("At 6th level, you can harness the beat of battle, whipping it into a frenzy of drums, chants, and glory. You can use your action to expend any number of uses of your Bardic Inspiration feature. For each expended use, you can immediately grant a Bardic Inspiration die to a creature other than yourself within 60 feet that you can see. A creature can have only one Bardic Inspiration die at a time.\nOnce you use this feature, you must finish a long rest before you can use it again.")

           if bard_school_choice == 11:
               PC_subclass = "College of Satire"
               class_feature10 = ("At 6th level, your ability to gather stories and lore gains a supernatural edge. You can cast Detect Thoughts up to a number of times equal to your Charisma modifier. You regain any expended uses of this ability after completing a long rest.\n"
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

             class_feature11 = "By  10th level, you have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any class, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.\nThe chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.\nYou learn two additional spells from any class at 14th level and again at 18th level."

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
               class_feature10 = "At 14th level, when you use your Performance of Creation feature, you can create more than one item at once. The number of items equals your Charisma modifier (minimum of two items). If you create an item that would exceed that number, you choose which of the previously created items disappears. Only one of these items can be of the maximum size you can create; the rest must be Small or Tiny.\nYou are no longer limited by gp value when creating items with Performance of Creation."


           if bard_school_choice == 2:
               PC_subclass = "College of Eloquence"
               class_feature10 = "At 14th level, when you successfully inspire someone, the power of your eloquence can now spread to someone else. When a creature within 60 feet of you adds one of your Bardic Inspiration dice to its ability check, attack roll, or saving throw and the roll succeeds, you can use your reaction to encourage a different creature (other than yourself) that can hear you within 60 feet of you, giving it a Bardic Inspiration die without expending any of your Bardic Inspiration uses.\nYou can use this reaction a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a long rest."

           if bard_school_choice == 3:
               PC_subclass = "College of Glamour"
               class_feature10 = ("At 14th level, your appearance permanently gains an otherworldly aspect that makes you look more lovely and fierce.\n"
                                  "In addition, as a bonus action, you can assume a magically majestic presence for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack you for the first time on a turn, the attacker must make a Charisma saving throw against your spell save DC. On a failed save, it can't attack you on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack you on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn."
                                  "\nOnce you assume this majestic presence, you can't do so again until you finish a short or long rest.")
                                 
           if bard_school_choice == 4:
               PC_subclass = "College of Lore"
               class_feature10 = "Starting at 14th level, when you make an ability check, you can expend one use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the DM tells you whether you succeed or fail."

           if bard_school_choice == 5:
               PC_subclass = "College of Swords"
               class_feature10 = "Starting at 14th level, whenever you use a Blade Flourish option, you can roll a d6 and use it instead of expending a Bardic Inspiration die."

           if bard_school_choice == 6:
               PC_subclass = "College of Valor"
               class_feature10 = "At 14th level, you have mastered the art of weaving spellcasting and weapon use into a single harmonious act. When you use your action to cast a bard spell, you can make one weapon attack as a bonus action"

           if bard_school_choice == 10:
               PC_subclass = "College of Whispers"
               class_feature10 = ("At 14th level, you gain the ability to weave dark magic into your words and tap into a creature’s deepest fears.\n"
                                "As an action, you magically whisper a phrase that only one creature of your choice within 30 feet of you can hear. The target must make a Wisdom saving throw against your spell save DC. It automatically succeeds if it doesn’t share a language with you or if it can’t hear you. On a successful saving throw, your whisper sounds like unintelligible mumbling and has no effect.\n"
                                "If the target fails its saving throw, it is charmed by you for the next 8 hours or until you or your allies attack or damage it. It interprets the whispers as a description of its most mortifying secret."
                                "\nWhile you gain no knowledge of this secret, the target is convinced you know it. While charmed in this way, the creature obeys your commands for fear that you will reveal its secret. It won’t risk its life for you or fight for you, unless it was already inclined to do so. It grants you favors and gifts it would offer to a close friend.\n"
                                "When the effect ends, the creature has no understanding of why it held you in such fear.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
         
           if bard_school_choice == 8:
               PC_subclass = "College of Spirits"
               class_feature10 = "At 14th level, your connection to spirits has become semipermanent. Whenever you use your Tales from Beyond feature, you can roll a d6 and use it instead of expending a Bardic Inspiration die. You still use your Bardic Inspiration die for the tale’s effect, without expending it."

           if bard_school_choice == 9:
               PC_subclass = "College of the Dire Singer"
               class_feature10 = "Starting at 14th level, you unflaggingly maintain the spirits and discipline of your unit. During your turn, you can use Countercharm as a bonus action. When you start a Countercharm performance, if any creature that gains its benefit is currently charmed or frightened, it can immediately make another saving throw against the effect that imposed the condition.\nIn addition, when a creature that gains the benefit of your Countercharm performance makes an ability check or saving throw, it can roll a d4 and add the number rolled to the ability check or saving throw."

           if bard_school_choice == 10:
               PC_subclass = "College of the Maestro"
               class_feature10 = "Upon reaching 14th level, you can begin conducting a mystical symphony as an action, distracting and capturing the minds of nearby creatures. For up to 10 minutes, any number of creatures you choose within 60 feet who can hear you have disadvantage on any saving throws against being charmed and against magical sleep.\nIn addition, affected targets have disadvantage on Wisdom (Perception) rolls that rely on sight or sound to detect targets other than you.\nIn combat, you must spend your action each turn to continue the performance or the effect ends. Once you use Virtuoso of Captivation, you must finish a short or long rest before you can use it again."

           if bard_school_choice == 11:
               PC_subclass = "College of Satire"
               class_feature10 = "At 14th level, you can expend one use of Bardic Inspiration after you fail an ability check, fail a saving throw, or miss with an attack roll. Roll a Bardic Inspiration die and add the number rolled to your attack, saving throw, or ability check, using the new result in place of the failed one.\nIf using this ability grants you a success on the attack, saving throw, or ability check, note the number you rolled on the Bardic Inspiration die. The DM can then apply that result as a penalty to an attack or check you make, and you cannot use this ability again until you suffer this drawback. When the DM invokes this penalty, describe an embarrassing gaffe or mistake you make as part of the affected die roll."

       if PC_level >= 15:
           level_8_spell1 = bard_level_8()

       if PC_level >= 16:
           feat5 = ability_score_improvement()

       if PC_level >= 17:
           PC_prof_bonus = 6
           level_9_spell1 = bard_level_9()

       if PC_level >= 19:
           feat6 = ability_score_improvement()
          
       if PC_level >= 20:
          class_feature12 = "At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, you regain one use."

    if PC_class == "Cleric":
       caster = "True"
       hit_dice = "1d8 per cleric level"
       first_lvl_hp = 8 + modifier(Constitution)

       hp_level = PC_level - 1
       high_lvl_hp = 0
       while hp_level != 0:
           high_lvl_hp += randint(1,8)+ modifier(Constitution)
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
       while cleric_subclass == 1 and level_1_spell1 == "Detect Magic":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 4 and level_1_spell1 == "Bane":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 5 and level_1_spell1 == "Command":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 6 and (level_1_spell1 == "Bless" or level_1_spell1 == "Cure Wounds"):
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 10 and level_1_spell1 == "Command":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 11 and level_1_spell1 == "Sanctuary":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 14 and level_1_spell1 == "Shield of Faith":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 15 and (level_1_spell1 == "Bless" or level_1_spell1 == "Guiding Bolt"):
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 16 and level_1_spell1 == "Shield of Faith":
           level_1_spell1 = cleric_level_1();

       while cleric_subclass == 17 and level_1_spell1 == "Bane":
           level_1_spell1 = cleric_level_1();
           
       while cleric_subclass == 20 and level_1_spell1 == "Command":
           level_1_spell1 = cleric_level_1();


       level_1_spell2 = cleric_level_1();
       while cleric_subclass == 1 and (level_1_spell2 == "Detect Magic" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 4 and (level_1_spell2 == "Bane" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 5 and (level_1_spell2 == "Command" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 6 and (level_1_spell2 == "Bless" or level_1_spell2 == "Cure Wounds" or  level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 10 and (level_1_spell2 == "Command" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 11 and (level_1_spell2 == "Sanctuary" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 14 and (level_1_spell2 == "Shield of Faith" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 15 and (level_1_spell2 == "Bless" or level_1_spell2 == "Guiding Bolt" or  level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 16 and (level_1_spell2 == "Shield of Faith" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while cleric_subclass == 17 and (level_1_spell2 == "Bane" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();
           
       while cleric_subclass == 20 and (level_1_spell2 == "Command"  or  level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

       while level_1_spell1 == level_1_spell2:
           level_1_spell2 = cleric_level_1();


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
        while cleric_subclass == 1 and (level_1_spell3 == "Detect Magic" or level_1_spell1 == level_1_spell2):
           level_1_spell2 = cleric_level_1();

        while cleric_subclass == 4 and (level_1_spell3 == "Bane" or level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 5 and (level_1_spell3 == "Command" or level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 6 and (level_1_spell3 == "Bless" or level_1_spell3 == "Cure Wounds" or  level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 10 and (level_1_spell3 == "Command" or level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 11 and (level_1_spell3 == "Sanctuary" or level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 14 and (level_1_spell3 == "Shield of Faith" or level_1_spell3 == level_1_spell2) or level_1_spell3 == level_1_spell1:
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 15 and (level_1_spell3 == "Bless" or level_1_spell3 == "Guiding Bolt" or  level_1_spell1 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 16 and (level_1_spell3 == "Shield of Faith" or level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while cleric_subclass == 17 and (level_1_spell3 == "Bane" or level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();
           
        while cleric_subclass == 20 and (level_1_spell3 == "Command"  or  level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1):
           level_1_spell3 = cleric_level_1();

        while level_1_spell3 == level_1_spell2 or level_1_spell3 == level_1_spell1:
           level_1_spell3 = cleric_level_1();







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

    #PC_class = class_selection();
    PC_class = "Bard"
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
    print("You have", hit_dice, "hit die")
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
    
    if caster == "True":
        print("Your known cantrips are:")
        print(cantrip1)
        print(cantrip2)
        print(cantrip3)
        print(cantrip4)
        print(cantrip5)
        print(cantrip6)
        print(cantrip7)
        print("Your known 1st level spells are:")
        print(level_1_spell1)
        print(level_1_spell2)
        print(level_1_spell3)
        print(level_1_spell4)
        print(level_1_spell5)
        print(level_1_spell6)
        print("Your known 2nd level spells are:")
        print(level_2_spell1)
        print(level_2_spell2)
        print(level_2_spell3)
        print("Your known 3rd level spells are:")
        print(level_3_spell1)
        print(level_3_spell2)
        print(level_3_spell3)
        print("Your known 4th level spells are:")
        print(level_4_spell1)
        print(level_4_spell2)
        print(level_4_spell3)
        print("Your known 5th level spells are:")
        print(level_5_spell1)
        print(level_5_spell2)
        print(level_5_spell3)
        print("Your known 6th level spells are:")
        print(level_6_spell1)
        print(level_6_spell2)
        print("Your known 7th level spells are:")
        print(level_7_spell1)
        print(level_7_spell2)
        print("Your known 8th level spells are:")
        print(level_8_spell1)
        print("Your known 9th level spells are:")
        print(level_9_spell1)


        print("Your feats are as follows")

        if PC_race == "Human" and human_feat != "":
            print(human_feat)

        if feat1 != "None" and feat1 != "":
            print(feat1)

        if feat2 != "None"and feat2 != "":
            print(feat2)

        if feat3 != "None"and feat3 != "":
            print(feat3)

        if feat4 != "None" and feat4 != "":
            print(feat4)

        if feat5 != "None"and feat5 != "":
            print(feat5)

        if feat6 != "None"and feat6 != "":
            print(feat6)

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


    feature = " "
    background_equipment = " "
    PC_subrace = ""
    race_feature1 = ""
    race_feature2 = ""
    race_feature3 = ""
    race_feature4 = ""
    race_feature5 = ""
    race_feature6 = ""
    race_feature7 = ""

    PC_hp = 0
    hit_dice = 0
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
    human_feat = ""
    feat1 = ""
    feat2 = ""
    feat3 = ""
    feat4 = ""
    feat5 = ""

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
    common =0
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
