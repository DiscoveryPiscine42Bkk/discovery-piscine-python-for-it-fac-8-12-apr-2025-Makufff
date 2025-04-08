#!/usr/bin/env python3

def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family))

family = {
		"florian": "red",
		"marie": "blond",
		"virginie": "brunette",
		"david": "red",
		"franck": "red"
	}

print(find_the_redheads(family))
