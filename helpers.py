from random import randint


def random_element(a):
    return a[randint(0, len(a) - 1)]


def get_comment():
    n = randint(1, 4)

    prefixes = ["", "Wow", "hey", n * "o" + "h", "w" + n * "o" + "w", "BRAVO!"]
    pronouns = ["that's", "this is", "it's", "that is", "its"]
    attributes = ["a good", "a cool", "kool", "a nice", "GREAT", "an awesome", "gorgeous", "so good", "super"]
    photos = ["photo", "pic", "photography", "picture", "work", "shot", "image", "piece of art"]
    suffixes = ["", " :)", " :" + n * ")", " :" + n * "D", " " + n * "he", n * "!", "...", ".", " lol", " he he"]

    prefix = random_element(prefixes)
    pronoun = random_element(pronouns)
    attribute = random_element(attributes)
    photo = random_element(photos)
    suffix = random_element(suffixes)

    return "{} {} {} {}{}".format(prefix, pronoun, attribute, photo, suffix)
