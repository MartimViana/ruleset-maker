import bobTheCoder as btc

# Defining essential rules

# Exemplar ruleset
rules = {
	'className' : 'Rules',
	'classType' : 'meta',
	'systemName' : '"Wannabe Dungeons and Dragons"',
	'authorName' : '"Martim Viana"',
	'primaryAttributes' : ['strength', 'dexterity', 'constitution', 'inteligence', 'wisdom', 'charisma'],
	'secondaryAttributes' : {'athletics' : 'strength', 'swim' : 'strength'}

}

Character_meta = {
	'className': 'Character',
	'classType': 'meta',
	'name' : 'name',
	'playerName' : 'playerName',
	'attribute' : 'attribute',
}


# Generate code
btc.newBlock(rules)
btc.newBlock(Character_meta)