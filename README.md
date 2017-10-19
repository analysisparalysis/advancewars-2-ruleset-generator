# advancewars-2-ruleset-generator
This is a small Python script script for generating a random ruleset for the Gameboy Advance game Advance Wars 2.
The game features a versus mode, where you can pick any non-campaign map and choose the teams, COs, and other rules.
I created this simple script to help with exploring the breadth of gameplay experience allowed by the various rulesets.
The script is basically just <code>random.choice()</code> called on the relevant data structures.
Run with <code>'python rollAWrules.py'</code>

A full list of the randomly selected elements:



<h2>Maps</h2>

<h3>Classic</h3> "bean island", "crater isle", "triangles", "ball islands", "coral lagoon", "puzzle trio", "fist peninsula", "deer harbor", "alara range", "lost river", "volcano isle", "turtle atoll", "squash island", "cube keys", "mirror islands", "shark strait", "royal channel"

<h3>Versus</h3> 'little island', 'sun canal', 'beaker river', 'star islands', 'eon springs', 'portal bridge', 'sabre range', 'asphalt maze', 'cog isle','zero wood', 'switchback', 'ruby keys', 'rainy haven', 'rail strait', 'tribe islands', 'vision bridge', 'piston dam', 'hat harbor', 'swan cove','go islands', 'hourglass isle'

<h3>Pre-deployed</h3> 'brace range', 'river range', 'moon isle', 'mint plateau', 'jewel canal', 'wrench island', 'rapid ferry', 'bundle city', 'scarab road', 'pointing river', 'liaison wood', 'delta heights', 'poem cape', 'blue lake', 'coil range', 'leaf haven', 'battle cube', 'big daddy', 'grid as    sault', 'crossroad'

<h3>Three Player</h3> 'pyramid cape', 'bead islands', 'clover keys', 'keyhole cove', 'fork river', 'mantis river', 'channel city', 'ink canal', 'shield hills', 'peril maze', 'gem creek', 'glass heights', "devil's inlet", 'shear port', "liar's cove", 'nail canal', 'atlas river', 'eel channels', 'jab peninsula', 'thorn islands', 'portsmouth', 'archipelagos', "wyrm's eye", 'knotted keys'

<h3>Four Player</h3> 'four corners', 'rocket cape', 'crop river', 'tween isle', 'rival islands', 'loop road', 'plus canal', 'islas five', 'patriot cove','web river', 'cap narrows', 'jay islands', 'chain canal', 'spring lakes', 'tatter river', 'island x', 'alakule', 'traitor river', 'fable hills','south cape', 'glory islands', 'pipe maze', 'lock ridge', 'heartland', 'badlands'

<h3>War Room</h3> 'spann island', 'moji island', 'duo falls', 'sole harbor', 'pivot isle', "land's end", 'kita straight', 'point stormy', 'ridge island', 'mial's hope', 'bounty river', 'toil ferry', 'twin isle', 'dire range', 'egg islands', 'terra maw', 'stamp islands', 'rivers four', 'ring islands', 'last mission', 'pay dirt', 'long road', 'nest egg', 'the trident', 'banker hills', 'missile plains', 'lost basin', 'risky vale', 'the ring', 'strong land']

<h2>Commanding Officers</h2>
"andy", "nell", "sturm", "hawke", "adder", "lash", "flak", "jess", "drake", "eagle", "sensei", "sonja", "kanbei", "colin", "grit", "olaf", "sami", "max", "hachi"

<h2>Other rules</h2>

Team alignment: a, b, c, d

Fog: on/off

Weather: random/clear/rain/snow

Funds per property: 1000 - 9500 (in increments of 500)

Turns until end: off / 5 - 99

Properties needed to win: off / 6 - 37

CO powers enabled: off/on
