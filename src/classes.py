import random

class Survivors():
    def __init__(self):
        self.survivors = {
            "Ada Wong": ["Low Profile", "Reactive Healing", "Wiretap"],
            "Adam Francis": ["Autodidact", "Deliverance", "Diversion"],
            "Alan Wake": ["Boon: Illumination", "Champion of Light", "Deadline"],
            "Ace Visconti": ["Ace in the Hole", "Open-Handed", "Up the Ante"],
            "Ashley J. Williams": ["Buckle Up", "Flip-Flop", "Mettle of Man"],
            "Cheryl Mason": ["Blood Pact", "Repressed Alliance", "Soul Guard"],
            "Claudette Morel": ["Botany Knowledge", "Empathy", "Self-Care"],
            "Dwight Fairfield": ["Bond", "Prove Thyself", "Leader"],
            "Ellen Ripley": ["Chemical Trap", "Light-Footed", "Lucky Star"],
            "Felix Richter": ["Built to Last", "Desperate Measures", "Visionary"],
            "Gabriel Soma": ["Made for This", "Scavenger", "Troubleshooter"],
            "Haddie Kaur": ["Inner Focus", "Overzealous", "Residual Manifest"],
            "Jake Park": ["Calm Spirit", "Iron Will", "Saboteur"],
            "Jeffrey 'Jeff' Johansen": ["Aftercare", "Breakdown", "Distortion"],
            "Jane Romero": ["Head On", "Poised", "Solidarity"],
            "Jill Valentine": ["Blast Mine", "Counterforce", "Resurgence"],
            "Jonah Vasquez": ["Boon: Exponential", "Corrective Action", "Overcome"],
            "Kate Denson": ["Boil Over", "Dance With Me", "Windows of Opportunity"],
            "Laurie Strode": ["Decisive Strike", "Object of Obsession", "Sole Survivor"],
            "Leon Scott Kennedy": ["Bite the Bullet", "Flashbang", "Flashbang"],
            "Meg Thomas": ["Adrenaline", "Quick & Quiet", "Sprint Burst"],
            "Mikaela Reid": ["Boon: Circle of Healing", "Boon: Shadow Step", "Clairvoyance"],
            "Nancy Wheeler": ["Better Together", "Fixated", "Inner Strength"],
            "Nea Karlsson": ["Balanced Landing", "Streetwise", "Urban Evasion"],
            "Nicolas Cage": ["Dramaturgy", "Plot Twist", "Scene Partner"],
            "Quentin Smith": ["Pharmacy", "Vigil", "Wake Up!"],
            "Rebecca Chambers": ["Better than New", "Hyperfocus", "Reassurance"],
            "Renato Lyra": ["Background Player", "Blood Rush", "Teamwork: Collective Stealth"],
            "Sable Ward": ["Invocation: Weaving Spiders", "Strength in Shadows", "Wicked"],
            "Steve Harrington": ["Babysitter", "Camaraderie", "Second Wind"],
            "Detective David Tapp": ["Detective's Hunch", "Stake Out", "Tenacity"],
            "Thalita Lyra": ["Cut Loose", "Friendly Competition", "Teamwork: Power of Two"],
            "Vittorio Toscano": ["Fogwise", "Potential Energy", "Quick Gambit"],
            "William 'Bill' Overbeck": ["Borrowed Time", "Left Behind", "Unbreakable"],
            "Yoichi Asakawa": ["Boon: Dark Theory", "Empathic Connection", "Parental Guidance"],
            "Yui Kimura": ["Any Means Necessary", "Breakout", "Lucky Break"],
            "Yun-Jin Lee": ["Fast Track", "Self-Preservation", "Smash Hit"],
            "Zarina Kassir": ["For the People", "Off the Record", "Red Herring"],
            "Élodie Rakoto": ["Appraisal", "Deception", "Power Struggle"],
            "David King": ["Dead Hard", "No Mither", "We're Gonna Live Forever"],
            "Feng Min": ["Alert", "Lithe", "Technician"],
            "All": ["Dark Sense", "Deja Vu", "Hope", "Kindred", "Lightweight", "No One Left Behind", "Plunderer's Instinct", "Premonition", "Resilience", "Slippery Meat", "Small Game", "Spine Chill", "This Is Not Happening", "We'll Make It"]
        }
        
    def randomizePerk(self, amount: int, exclude: str = None):  
        chosen_perks = []
        chosen_chars = []
        self.tempSurvivor = self.survivors.copy()
        if exclude:    
            for survivors in exclude:
                if survivors in self.tempSurvivor:
                    del self.tempSurvivor[survivors]
    
        for _ in range(int(amount)):
            character, perks = random.choice(list(self.tempSurvivor.items()))
            chosen_perk = random.choice(perks)
            chosen_perks.append(chosen_perk)
            chosen_chars.append(character)

        return chosen_perks, chosen_chars
    
    def randomizeSurvivor(self, amount: int, exclude: str = None):   
        chosen_chars = []
        self.tempSurvivor = self.survivors.copy()
        del self.tempSurvivor["All"]
        if exclude:    
            for survivors in exclude:
                if survivors in self.tempKiller:
                    del self.tempSurvivor[survivors]

        for _ in range(int(amount)):
            character, perks = random.choice(list(self.tempSurvivor.items()))
            chosen_chars.append(character)
        return chosen_chars
        
class Killers():
    def __init__(self):
        self.killers = {
            "All": ["Bitter Murmur", "Deerstalker", "Distressing", "Hex: NOED", "Hex: Thrill of the Hunt", "Insidious", "Iron Grasp", "Scourge Hook: Monstrous Shine", "Shattered Hope", "Sloppy Butcher", "Spies from the Shadows", "Unrelenting", "Whispers"],
            "Artist": ["Grim Embrace", "Hex: Pentimento", "Scourge Hook: Pain Resonance"],
            "Blight": ["Dragon's Grip", "Hex: Blood Favour", "Hex: Undying"],
            "Cannibal": ["Barbacue & Chilli", "Franklin's Demise", "Knock Out"],
            "Cenobite": ["Deadlock", "Hex: Plaything", "Scourge Hook: Gift of Pain"],
            "Clown": ["Bamboozle", "Coulrophobia", "Pop Goes the Weasel"],
            "Deathslinger": ["Dead Man's Switch", "Gearhead", "Hex: Retribution"],
            "Demogorgon": ["Cruel Limits", "Mindbreaker", "Surge"],
            "Doctor": ["Monitor & Abuse", "Overcharge", "Overwhelming Presence"],
            "Dredge": ["Darkness Revealed", "Dissolution", "Septic Touch"],
            "Executioner": ["Deathbound", "Forced Penance", "Trail of Torment"],
            "Ghost Face": ["Furtivae Chase", "I'm All Ears", "Thrilling Tremors"],
            "Good Guy": ["Batteries Included", "Friends 'til the End", "Hex: Two Can Play"],
            "Hag": ["Hex: Devour Hope", "Hex: Ruin", "Hex: The Third Seal"],
            "Hillbilly": ["Enduring", "Lightborn", "Tinkerer"],
            "Huntress": ["Beast of Prey", "Hex: Huntress Lullaby", "Territorial Imperative"],
            "Knight": ["Hex: Face the Darkness", "Hubris", "Nowhere to Hide"],
            "Legion": ["Discordance", "Iron Maiden", "Mad Grit"],
            "Mastermind": ["Awakened Awareness", "Superior Anatomy", "Terminus"],
            "Nemesis": ["Eruption", "Hysteria", "Lethal Pursuer"],
            "Nightmare": ["Blood Warden", "Fire Up", "Remember Me"],
            "Nurse": ["Nurse's Calling", "Stridor", "Thanatophobia"],
            "Oni": ["Blood Echo", "Nemesis", "Zanshin Tactics"],
            "Onryõ": ["Call of Brine", "Merciless Storm", "Scourge Hook: Floods of Rage"],
            "Pig": ["Make Your Choice", "Scourge Hook: Hangman's Trick", "Surveillance"],
            "Plague": ["Corrupt Intervention", "Dark Devotion", "Infectious Fright"],
            "Shape": ["Dying Light", "Play with Your Food", "Save the Best for Last"],
            "Singularity": ["Forced Hesitation", "Genetic Limits", "Machine Learning"],
            "Skull Merchant": ["Game Afoot", "Leverage", "THWACK!"],
            "Spirit": ["Hex: Haunted Ground", "Rancor", "Spirit Fure"],
            "Trapper": ["Agitation", "Brutal Strength", "Unnerving Presence"],
            "Trickster": ["Hex: Crowd Control", "No Way Out", "Starstruck"],
            "Twins": ["Coup de Grâce", "Hoarder", "Oppression"],
            "Unkown": ["Unbound", "Undone", "Unforeseen"],
            "Wraith": ["Bloodhound", "Predator", "Shadowborn"],
            "Xenomorph": ["Alien Instinct", "Rapid Brutality", "Ultimate Weapon"],
        }
        
    def randomizePerk(self, amount: int, exclude: str = None):  
        chosen_perks = []
        chosen_chars = []
        self.tempKiller = self.killers.copy()
        if exclude:    
            for killer in exclude:
                if killer in self.tempKiller:
                    del self.tempKiller[killer]
    
        for _ in range(int(amount)):
            character, perks = random.choice(list(self.tempKiller.items()))
            chosen_perk = random.choice(perks)
            chosen_perks.append(chosen_perk)
            chosen_chars.append(character)

        return chosen_perks, chosen_chars
    
    def randomizeKiller(self, amount: int, exclude: str = None):   
        chosen_chars = []
        self.tempKiller = self.killers.copy()
        del self.tempKiller["All"]
        if exclude:    
            for killer in exclude:
                if killer in self.tempKiller:
                    del self.tempKiller[killer]

        for _ in range(int(amount)):
            character, perks = random.choice(list(self.tempKiller.items()))
            chosen_chars.append(character)
        return chosen_chars
