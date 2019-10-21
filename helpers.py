from random import randint


def random_element(a):
    return a[randint(0, len(a) - 1)]


def get_comment():
    n = randint(1, 4)

    attributes = ["cool", "kool", "nice", "GREAT", "awesome", "gorgeous", "good", "super"]
    photos = ["photo", "pic", "photography", "picture", "work", "job"]
    suffixes = ["", ":)", ":" + n * ")", ":" + n * "D", n * "he", n * "!", "...", ".", "lol", "he he"]
    pronouns = ["that's", "this is", "it's", "that is", "it is"]
    prefixes = ["", "Wow", "hey", n * "o" + "h", "w" + n * "o" + "w", "BRAVO!"]

    prefix = random_element(prefixes)
    pronoun = random_element(pronouns)
    attribute = random_element(attributes)
    photo = random_element(photos)
    suffix = random_element(suffixes)

    return "{} {} a {} {} {}".format(prefix, pronoun, attribute, photo, suffix)
