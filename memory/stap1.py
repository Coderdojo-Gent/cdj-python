import random

symbolen = [
    "\U0001F609",  # winking face
    "\U0001F922",  # nauseated face
    "\U0001F636",  # face without mouth
    "\U0001F913",  # nerd face
    "\U0001F971",  # yawning face
    "\U0001F61B",  # face with tongue
    "\U0001F631",  # face screaming in fear
    "\U0001F633",  # flushed face
    "\U0001F60E",  # smiling face with sunglasses
    "\U0001F973",  # partying face
    "\U0001F976",  # cold face
    "\U0001F975",  # hot face
]

# lijst uitbreiden met zichzelf:
symbolen.extend(symbolen)

# lijst in willekeurige volgorde zetten
random.shuffle(symbolen)

# test: hoe zie de lijst er nu uit?
print(symbolen)
