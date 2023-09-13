#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        first_character = sentence[0]
        return (len(sentence), first_character)
