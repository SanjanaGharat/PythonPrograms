#program to create madlib
def mad_lib(*args):
    story = f"{Celebrity} was casually strolling through the {place}, wearing a {adjective} pair of shoes and carrying a bag full of {food}. Meanwhile, a group of {number} {animal}s were {verb}ing {adverb} nearby."

    return story


# Example usage:
Celebrity = input("Enter a Celebrity: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
food = input("Enter an food: ")
number = input("Enter an number: ")
animal = input("Enter an animal: ")
verb = input("Enter an verb: ")
adverb = input("Enter an adverb: ")
result = mad_lib(Celebrity,place,adjective,food,number,animal,verb,adverb)
print(result)

