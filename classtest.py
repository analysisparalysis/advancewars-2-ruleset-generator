import random

data = {
'factions' : ['a', 'b', 'c', 'd'],
	'commandingOfficers' : ["andy", "nell", "sturm", "hawke", "adder", "lash", "flak", "jess", "drake", "eagle", "sensei", "sonja", "kanbei", "colin", "grit", "olaf", "sami", "max", "hachi"],
	'classic' : ["bean island", "crater isle", "triangles", "ball islands", "coral lagoon", "puzzle trio", "fist peninsula", "deer harbor", "alara range", "lost river", "volcano isle", "turtle atoll", "squash island", "cube keys", "mirror islands", "shark strait", "royal channel"],
	'versus' : ['little island', 'sun canal', 'beaker river', 'star islands', 'eon springs', 'portal bridge', 'sabre range', 'asphalt maze', 'cog isle', 'zero wood', 'switchback', 'ruby keys', 'rainy haven', 'rail strait', 'tribe islands', 'vision bridge', 'piston dam', 'hat harbor', 'swan cove', 'go islands', 'hourglass isle'],
	'predeployed' : ['brace range', 'river range', 'moon isle', 'mint plateau', 'jewel canal', 'wrench island', 'rapid ferry', 'bundle city', 'scarab road', 'pointing river', 'liaison wood', 'delta heights', 'poem cape', 'blue lake', 'coil range', 'leaf haven', 'battle cube', 'big daddy', 'grid assault', 'crossroad'],
	'threePlayer' : ['pyramid cape', 'bead islands', 'clover keys', 'keyhole cove', 'fork river', 'mantis river', 'channel city', 'ink canal', 'shield hills', 'peril maze', 'gem creek', 'glass heights', "devil's inlet", 'shear port', "liar's cove", 'nail canal', 'atlas river', 'eel channels', 'jab peninsula', 'thorn islands', 'portsmouth', 'archipelagos', "wyrm's eye", 'knotted keys'],
	'fourPlayer' : ['four corners', 'rocket cape', 'crop river', 'tween isle', 'rival islands', 'loop road', 'plus canal', 'islas five', 'patriot cove', 'web river', 'cap narrows', 'jay islands', 'chain canal', 'spring lakes', 'tatter river', 'island x', 'alakule', 'traitor river', 'fable hills', 'south cape', 'glory islands', 'pipe maze', 'lock ridge', 'heartland', 'badlands'],
	'warRoom' : ['spann island', 'moji island', 'duo falls', 'sole harbor', 'pivot isle', "land's end", 'kita straight', 'point stormy', 'ridge island', "mial's hope", 'bounty river', 'toil ferry', 'twin isle', 'dire range', 'egg islands', 'terra maw', 'stamp islands', 'rivers four', 'ring islands', 'last mission', 'pay dirt', 'long road', 'nest egg', 'the trident', 'banker hills', 'missile plains', 'lost basin', 'risky vale', 'the ring', 'strong land'],
	'mapStrings' : ['classic', 'versus', 'predeployed', 'threePlayer', 'fourPlayer', 'warRoom'],
}

ruleSet = {
	'fogOfWar': [0, 1],
	'weather' : ["clear", "rain", "snow", "random"],
	'funds' : range(1000, 10000, 500),
	'turn' : range(5, 100),
	'capt' : range(6, 48),
	'co1' : data['commandingOfficers'],
	'co2' : data['commandingOfficers'],
	'co3' : data['commandingOfficers'],
	'co4' : data['commandingOfficers'],
	'co1 faction' : data['factions'],
	'co2 faction' : data['factions'],
	'co3 faction' : data['factions'],
	'co4 faction' : data['factions'],
}

mapsPlayed = {
	'classic':,
	'versus':,
	'warRoom':,
	'predeployed':,
	'threePlayer':,
	'fourPlayer':,
}

for key in ruleSet:
	print key, random.choice(ruleSet[key])
mapCategory = random.choice(data['mapStrings'])
nextMap = random.choice(data[mapCategory])
print mapCategory
print nextMap
