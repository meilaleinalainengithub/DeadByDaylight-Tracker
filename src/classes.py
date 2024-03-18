import random

class Survivors():
    def __init__(self):
        self.All = ["Dark Sense", "Deja Vu", "Hope", "Kindred", "Lightweight", "No One Left Behind", "Plunderer's Instinct", "Premonition", "Resilience", "Slippery Meat", "Small Game", "Spine Chill", "This Is Not Happening", "We'll Make It"]
        Ada = ["Low Profile", "Reactive Healing", "Wiretap"]
        Adam = ["Autodidact", "Deliverance", "Diversion"]
        Alan = ["Boon: Illumination", "Champion of Light", "Deadline"]
        Ace = ["Ace in the Hole", "Open-Handed", "Up the Ante"]
        Ashley = ["Buckle Up", "Flip-Flop", "Mettle of Man"]
        Cheryl = ["Blood Pact", "Repressed Alliance", "Soul Guard"]
        Claudette = ["Botany Knowledge", "Empathy", "Self-Care"]
        Dwight = ["Bond", "Prove Thyself", "Leader"]
        Ellen = ["Chemical Trap", "Light-Footed", "Lucky Star"]
        Felix = ["Built to Last", "Desperate Measures", "Visionary"]
        Gabriel = ["Made for This", "Scavenger", "Troubleshooter"]
        Haddie = ["Inner Focus", "Overzealous", "Residual Manifest"]
        Jake = ["Calm Spirit", "Iron Will", "Saboteur"]
        Jeff = ["Aftercare", "Breakdown", "Distortion"]
        Jane = ["Head On", "Poised", "Solidarity"]
        Jill = ["Blast Mine", "Counterforce", "Resurgence"]
        Jonah = ["Boon: Exponential", "Corrective Action", "Overcome"]
        Kate = ["Boil Over", "Dance With Me", "Windows of Opportunity"]
        Laurie = ["Decisive Strike", "Object of Obsession", "Sole Survivor"]
        Leon = ["Bite the Bullet", "Flashbang", "Flashbang"]
        Meg = ["Adrenaline", "Quick & Quiet", "Sprint Burst"]
        Mikaela = ["Boon: Circle of Healing", "Boon: Shadow Step", "Clairvoyance"]
        Nancy = ["Better Together", "Fixated", "Inner Strength"]
        Nea = ["Balanced Landing", "Streetwise", "Urban Evasion"]
        Nicolas = ["Dramaturgy", "Plot Twist", "Scene Partner"]
        Quentin = ["Pharmacy", "Vigil", "Wake Up!"]
        Rebecca = ["Better than New", "Hyperfocus", "Reassurance"]
        Renato = ["Background Player", "Blood Rush", "Teamwork: Collective Stealth"]
        Sable = ["Invocation: Weaving Spiders", "Strength in Shadows", "Wicked"]
        Steve = ["Babysitter", "Camaraderie", "Second Wind"]
        Tapp = ["Detective's Hunch", "Stake Out", "Tenacity"]
        Thalita = ["Cut Loose", "Friendly Competition", "Teamwork: Power of Two"]
        Vittorio = ["Fogwise", "Potential Energy", "Quick Gambit"]
        Bill = ["Borrowed Time", "Left Behind", "Unbreakable"]
        Yoichi = ["Boon: Dark Theory", "Empathic Connection", "Parental Guidance"]
        Yui = ["Any Means Necessary", "Breakout", "Lucky Break"]
        Yun = ["Fast Track", "Self-Preservation", "Smash Hit"]
        Zarina = ["For the People", "Off the Record", "Red Herring"]
        Élodie = ["Appraisal", "Deception", "Power Struggle"]
        David = ["Dead Hard", "No Mither", "We're Gonna Live Forever"]
        Feng = ["Alert", "Lithe", "Technician"]

        self.survivors = [Dwight, Meg, Claudette, Jake, Nea, Laurie, Ace, Bill, Feng, David, Kate, Quentin, 
                          Tapp, Adam, Jeff, Jane, Ashley, Nancy, Steve, Yui, Zarina, Cheryl, Felix, Élodie, 
                          Yun, Jill, Leon, Mikaela, Jonah, Yoichi, Haddie, Ada, Rebecca, Vittorio, Thalita,
                          Renato, Gabriel, Nicolas, Ellen, Alan, Sable]
        
    def randomizePerk(self, amount: int, exclude: list = None):
        if exclude:
            chosen = []    
            self.tempSurvivors = self.survivors
            for survivor in exclude:
                self.tempSurvivors.remove(survivor)
    
        for i in range(amount):
            character = random.randrange(self.survivors)
            chosen.append(random.randrange(character))

        return chosen
    
    def randomizeSurvivor(self, exclude: list = None):
        if exclude:  
            self.tempSurvivors = self.survivors
            for survivor in exclude:
                self.tempSurvivors.remove(survivor)
            return random.randrange(self.survivors)
        
class Killers():
    def __init__(self):
        Artist = []
        Blight = []
        Cannibal = []
        Cenobite = []
        Clown = []
        Deathslinger = []
        Demogorgon = []
        Doctor = []
        Executioner = []
        Ghost_Face = []
        Good_Guy = []
        Hag = []
        Huntress = []
        Knight = []
        Legion = []
        Mastermind = []
        Nightmare = []
        Nurse = []
        Oni = []
        Pig = []
        Plague = []
        Skull_Merchant = []
        Spirit = []
        Trapper = []
        Twins = []
        Trickster = []
        Unknown = []
        Wraith = []
        Xenomorph = []
        Onryō = []
        Dredge = []
        Nemesis = []

        self.killers = [Artist, Blight, Cannibal, Cenobite, Clown, Deathslinger, Demogorgon, Doctor, Executioner,
                        Ghost_Face, Good_Guy, Hag, Huntress, Knight, Legion, Mastermind, Nightmare, Nurse, Oni, Pig,
                        Plague, Skull_Merchant, Spirit, Trapper, Twins, Trickster, Unknown, Wraith, Xenomorph, Onryō,
                        Dredge, Nemesis]