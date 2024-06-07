from generators.models import MyClass, MyClassElement

# Run from shell with command: exec(open('my_scripts/add_classes.py').read())

aclass = {
    'bard': ['Joy', 'Phantasy', 'Chimes', 'Strum', 'Drums', 'Jokes', 'Masks', 'Facades', 'Tragedy', 'Comedy'],
    'heir': ['Magnets', 'Mysteries', 'Power', 'Aether', 'Vitae', 'Asceticism', 'Delay', 'Weight', 'Waterfalls', 'Cracks'],
    'maid': ['Dust', 'Specks', 'Motes', 'Hollows', 'Warrens', 'Dens', 'Cushions', 'Wings', 'Trays', 'Blankets'],
    'page': ['Plains', 'Expanse', 'Freedom', 'Crash', 'Burn', 'Candles', 'Wick', 'Flash', 'Fury', 'Mazes'],
    'witch': ['Frost', 'Brew', 'Cauldrons', 'Corks', 'Straw', 'Wires', 'Dolls', 'Pipes', 'Contraptions', 'Strands'],
    'rogue': ['Shrines', 'Pedestals', 'Charity', 'Surprises', 'Gifts', 'Simmer', 'Steam', 'Burials', 'Refuse', 'Junk'],
    'sylph': ['Rays', 'Chalk', 'Lead', 'Ink', 'Feathers', 'Presses', 'Print', 'Bindings', 'Paper', 'Ribbons'],
    'seer': ['Thought', 'Shelves', 'Spheres', 'Sight', 'Telescopes', 'Crystals', 'Paths', 'Marches', 'Inspection', 'Organization'],
    'prince': ['War', 'Blades', 'Barrels', 'Arks', 'Mud', 'Claws', 'Strife', 'Grief', 'Grip', 'Reticence'],
    'knight': ['Fortresses', 'Jails', 'Dungeons', 'Metal', 'Shells', 'Cages', 'Towers', 'Pits', 'Oubilletes', 'Chains'],
    'mage': ['Speakers', 'Senses', 'Insight', 'Pain', 'Hardship', 'Toil', 'Brains', 'Necrosis', 'Barbs', 'Spikes'],
    'thief': ['Maps', 'Centers', 'Holes', 'Cans', 'Tins', 'Games', 'Haunt', 'Desire', 'Spotlights', 'Frames']
}

for class_name, elements in aclass.items():
    # Create or get the class
    my_class, created = MyClass.objects.get_or_create(name=class_name)

    for element in elements:
        # Create each element associated with the class
        MyClassElement.objects.create(name=element, class_name=my_class)
