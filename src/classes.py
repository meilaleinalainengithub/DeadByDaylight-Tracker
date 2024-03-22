import random

class Survivors():
    def __init__(self):
        self.survivors = {
            "Ada": ["Low Profile", "Reactive Healing", "Wiretap"],
            "Adam": ["Autodidact", "Deliverance", "Diversion"],
            "Alan": ["Boon: Illumination", "Champion of Light", "Deadline"],
            "Ace": ["Ace in the Hole", "Open-Handed", "Up the Ante"],
            "Ashley": ["Buckle Up", "Flip-Flop", "Mettle of Man"],
            "Cheryl": ["Blood Pact", "Repressed Alliance", "Soul Guard"],
            "Claudette": ["Botany Knowledge", "Empathy", "Self-Care"],
            "Dwight": ["Bond", "Prove Thyself", "Leader"],
            "Ellen": ["Chemical Trap", "Light-Footed", "Lucky Star"],
            "Felix": ["Built to Last", "Desperate Measures", "Visionary"],
            "Gabriel": ["Made for This", "Scavenger", "Troubleshooter"],
            "Haddie": ["Inner Focus", "Overzealous", "Residual Manifest"],
            "Jake": ["Calm Spirit", "Iron Will", "Saboteur"],
            "Jeff": ["Aftercare", "Breakdown", "Distortion"],
            "Jane": ["Head On", "Poised", "Solidarity"],
            "Jill": ["Blast Mine", "Counterforce", "Resurgence"],
            "Jonah": ["Boon: Exponential", "Corrective Action", "Overcome"],
            "Kate": ["Boil Over", "Dance With Me", "Windows of Opportunity"],
            "Laurie": ["Decisive Strike", "Object of Obsession", "Sole Survivor"],
            "Leon": ["Bite the Bullet", "Flashbang", "Flashbang"],
            "Meg": ["Adrenaline", "Quick & Quiet", "Sprint Burst"],
            "Mikaela": ["Boon: Circle of Healing", "Boon: Shadow Step", "Clairvoyance"],
            "Nancy": ["Better Together", "Fixated", "Inner Strength"],
            "Nea": ["Balanced Landing", "Streetwise", "Urban Evasion"],
            "Nicolas": ["Dramaturgy", "Plot Twist", "Scene Partner"],
            "Quentin": ["Pharmacy", "Vigil", "Wake Up!"],
            "Rebecca": ["Better than New", "Hyperfocus", "Reassurance"],
            "Renato": ["Background Player", "Blood Rush", "Teamwork: Collective Stealth"],
            "Sable": ["Invocation: Weaving Spiders", "Strength in Shadows", "Wicked"],
            "Steve": ["Babysitter", "Camaraderie", "Second Wind"],
            "Tapp": ["Detective's Hunch", "Stake Out", "Tenacity"],
            "Thalita": ["Cut Loose", "Friendly Competition", "Teamwork: Power of Two"],
            "Vittorio": ["Fogwise", "Potential Energy", "Quick Gambit"],
            "Bill": ["Borrowed Time", "Left Behind", "Unbreakable"],
            "Yoichi": ["Boon: Dark Theory", "Empathic Connection", "Parental Guidance"],
            "Yui": ["Any Means Necessary", "Breakout", "Lucky Break"],
            "Yun": ["Fast Track", "Self-Preservation", "Smash Hit"],
            "Zarina": ["For the People", "Off the Record", "Red Herring"],
            "Élodie": ["Appraisal", "Deception", "Power Struggle"],
            "David": ["Dead Hard", "No Mither", "We're Gonna Live Forever"],
            "Feng": ["Alert", "Lithe", "Technician"],
            "All": ["Dark Sense", "Deja Vu", "Hope", "Kindred", "Lightweight", "No One Left Behind", "Plunderer's Instinct", "Premonition", "Resilience", "Slippery Meat", "Small Game", "Spine Chill", "This Is Not Happening", "We'll Make It"]
        }
        
    def randomizePerk(self, amount: int, exclude: str = None):  
        chosen = []
        self.tempSurvivors = self.survivors
        if exclude:    
            for survivor in exclude:
                self.tempSurvivors.remove(survivor)
    
        for _ in range(int(amount)):
            character, perks = random.choice(list(self.tempSurvivors.items()))
            chosen_perk = random.choice(perks)
            chosen.append((character, chosen_perk))

        return chosen
    
    def randomizeSurvivor(self, exclude: str = None):   
        self.tempSurvivors = self.survivors
        if exclude:  
            for survivor in exclude:
                self.tempSurvivors.remove(survivor)
        return random.choice(self.tempSurvivors)
        
class Killers():
    def __init__(self):
        self.killers = {
            "Artist": [],
            "Blight": [],
            "Cannibal": [],
            "Cenobite": [],
            "Clown": [],
            "Deathslinger": [],
            "Demogorgon": [],
            "Doctor": [],
            "Executioner": [],
            "Ghost_Face": [],
            "Good_Guy": [],
            "Hag": [],
            "Huntress": [],
            "Knight": [],
            "Legion": [],
            "Mastermind": [],
            "Nightmare": [],
            "Nurse": [],
            "Oni": [],
            "Pig": [],
            "Plague": [],
            "Skull_Merchant": [],
            "Spirit": [],
            "Trapper": [],
            "Twins": [],
            "Trickster": [],
            "Unknown": [],
            "Wraith": [],
            "Xenomorph": [],
            "Onryō": [],
            "Dredge": [],
            "Nemesis": [],
            "Artist": [],
            "Blight": [],
            "Cannibal": [],
            "Cenobite": [],
            "Clown": [],
            "Deathslinger": [],
            "Demogorgon": [],
            "Doctor": [],
            "Executioner": [],
            "Ghost_Face": [],
            "Good_Guy": [],
            "Hag": [],
            "Huntress": [],
            "Knight": [],
            "Legion": [],
            "Mastermind": [],
            "Nightmare": [],
            "Nurse": [],
            "Oni": [],
            "Pig": [],
            "Plague": [],
            "Skull_Merchant": [],
            "Spirit": [],
            "Trapper": [],
            "Twins": [],
            "Trickster": [],
            "Unknown": [],
            "Wraith": [],
            "Xenomorph": [],
            "Onryō": [],
            "Dredge": [],
            "Nemesis": [],
        }
        
    def randomizePerk(self, amount: int, exclude: str = None):  
        chosen = []
        self.tempKiller = self.killers
        if exclude:    
            for killer in exclude:
                self.tempKiller.remove(killer)
    
        for _ in range(int(amount)):
            character, perks = random.choice(list(self.killers.items()))
            chosen_perk = random.choice(perks)
            chosen.append((character, chosen_perk))

        return chosen
    
    def randomizeKiller(self, exclude: str = None):
        if exclude:  
            self.tempKiller = self.killers
            for killers in exclude:
                self.tempKiller.remove(killers)
            return random.choice(self.killers)