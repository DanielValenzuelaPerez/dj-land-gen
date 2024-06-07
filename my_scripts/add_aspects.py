from generators.models import Aspect, AspectElement

# Run from shell with command: exec(open('my_scripts/add_aspects.py').read())

anaspect = {
    'mind': ["Flow","Crossroads","Lightning","Static","Transmissions","Nerves","Change","Radio","Salt","Plasma","Choice(s)","Thought","Brain(s)","Idea(s)","Inspiration","Books","Maze(s)","Labyrinth(s)","Electricity","Neurons","Spark(s)","Insight","Wisdom","Truth","Think","Ponder","Study","Scrolls","Memory","Logic","Puzzle(s)","Learn","Answers","Solutions","Conscious","Aware","Reeds","Gylphs","Thought","Symbol(s)","Data","Links","Connections","Mementos"],
    'light': ["Gleam","Magnification","Gambling","Treasure","Mirrors","Marble","Glass","Charts","Star(s)","Books","Tarot","Cards","Dice","Maps","Sun(s)","Insight","Fortune","Chance","Illusion","Mist","Flash","Glitter","Sparkle","Shine","Radiance","Dream(s)","Myth","Mirage(s)","Fantasy","Vision","Eyes","Clover","Bright(ness)","Clarity","Windows","Reflection","Crystal","Twilight","BlackJack","Poker","Chance","Game(s)"],
    'life': ["Gardens","Vines","Glass","Nobility","Thorns","Feasts","Rebellion","Mass","Fragility","Roots","Trees","Flower(s)","Forest(s)","Vegetation","Water","Greenery","Refresh","Renew","Invigorate","Flora","Inlets","Deltas","Rivers","Silt","Soil","Zest","Seedlings","Sprouts","Timber","Peaks","Summits","Crowns","Zeniths","Loam","Hawthorne","Snowdrops","Thaw","Spring","Woodland Creatures","Adorable Fluffy Bunnies"],
    'heart': ["Paint","Trees","Spirits","Engines","Vapors","Wool","Clouds","Steams","Arrows","Temper","Pillows","Art","Friendship","Trust","Security","Passion","Love","Morals","Morality","Conscience","Empathy","Kindness","Comfort","Pillars","Anima","Gatherings","Parties","Myrtle","Frenzy","Roots","Desire","Notes","Candles","Dance","Marble"],
    'blood': ["Pulse","Haze","Magma","Castles","Conquest","Brick","Ichor","Flesh","Brimstone","Sulfur","Veins","Heart(s)","Arteries","Muscles","Pulse","History","Bonds","Mortality","War","Arete","Growth","Bone","Limbs","Bonds","Thirst","Bloom","Teeth","Tempest","Idols","Lines","Royalty","Connections","Knives","Water","Entrails","Hands","Sight","Fields","Crowns","Reach","Sweat","Tears","Garnet","Obsidian","Chains"],
    'breath': ["Wind","Gale","Dunes","Grease","Spires","Storms","Fog","Clouds","Windmills","Flags","Winds","Gust(s)","Storm(s)","Roads","Airplanes","Breeze","Zephyr","Flags","Tempest","Turbulence","Typhoon(s)","Flow","Travel","Flight","Birds","Gases","Spirit","Up","Sky","Loft","Ice","Hail","Dust","Mist","Fans","Feathers","Lightning","Shifts/Shifting","Kites"],
    'doom': ["Rust","Rust","Fire","Char","Infernos","Meteors","Courts","Temples","Clay","Cannons","Undead","Graves","Ruins","Sickness","Infection","Pain","Fear","Apocalypse","Gore","Suspense","Entropy","Disorder","End","Decrees","Fortune","Judgement","Sleep","Rivers","Hemlock","Alleys","Night","Crossroads"],
    'time': ["Gears","Clockwork","Meldoy","Quartz","Decay","Pendulums","Bells","Rhythm","Tides","Cycles","Hourglasses","Obelisks","Sundials","Dials","Pace","Pattern","Tempo","Beat","Flow","Chronology","Infinity","Age","Hands","Alarm(s)","Wheel(s)","Tables","Charts","Dates","Calendar(s)","Schedule","Routine","Stars","Rotation","Records"],
    'hope': ["Sunlight","Gospel","Churches","Crosses","Reverence","Halls","Mausoleums","Hymns","Choirs","worship","Bells","Angels","Glass","Belief","Inspiration","Peace","Calming","Spires","Faith","Relic(s)","Prayer","Rebuild","Share","Cliffs","Heihts","Pinnacles","Cups","Castles","Roses","Dawn","Gold","Unicorns","Doves","Feasts","Sugar","Changes","Shifts","Inspiration","Spark(s)","Stars"],
    'rage': ["Riots","Mirth","Martyrs","Slums","Slime","Nails","Smoke","Alleyways","Balloons","Icicles","Monsters","Demons","Tension","Pressure","Chaos","Discord","Pain","Suspicion","Anger","Mistrust","Hate","Terror","Outbursts","Violence","Onslaught","Slaughter","Explosive","Destruction","Chagrin","Ire","Choler","Fury","Storm","Passion","Fools","Bulls","Cadmium","Curses","Sludge"],
    'void': ["Emptiness","Chasms","Desolation","Abyss","Silence","Lack","Depths","Stillness","Statues","Chambers","Mirrors","Holes","Caves","Valleys","Peaks","Tunnels","Anti-Matter","Darkness","Artifacts",'Intangibility','Unconscious','Existential','Might','Depths','Nadir','Locusts','Deserts','Islands','Circles','Space','Snow','Frost','Thundra','Weightlessness'],
    'space': ["frogs"]
}

for aspect_name, elements in anaspect.items():
    # Create or get the class
    my_class, created = Aspect.objects.get_or_create(name=aspect_name)

    for element in elements:
        # Create each element associated with the class
        AspectElement.objects.create(name=element, aspect_name=my_class)
