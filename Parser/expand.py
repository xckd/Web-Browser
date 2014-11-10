# token format:
# ['exp', '+', 'exp', '-', 'b']

# utterance format:
# "exp"
# "exp a"
# "exp + exp"

# grammar format:
# [
# ("exp", ["exp", "+", "exp"]),
# ("exp", ["exp", "-", "exp"]),
# ("exp", ["(", "exp", ")"]),
# ("exp", ["num"]),
# ]

# Output: a list of all the newly possible token when
# the grammar is also taken into consideration.

grammar = [
("exp", ["exp", "+", "exp"]),
("exp", ["exp", "-", "exp"]),
("exp", ["(", "exp", ")"]),
("exp", ["num"])
]

inputsentence = ["exp", "a", "exp"] # this is the token according to the video.
utterances = [inputsentence]
# Note: + between two lists will use the elements of both the lists to create a new bigger list.

depth = 4

for dep in range (depth):
    for utterance in utterances:
        for i in range(len(utterance)):
            for rule in grammar:
                if utterance[i] == rule[0]:
                    utterances = utterances + [utterance[0:i] + rule[1] + utterance[i+1:]]

for utter in utterances:
    print utter
