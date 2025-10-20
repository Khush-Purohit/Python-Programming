def demo_decorator(inner):
    def wrapper(*args):
        word = args[0]
        word = word.upper()
        return inner(word)
    return wrapper



@demo_decorator
def display_greet(words):
    print(words)

display_greet("Hello!! so nice to be with you!!")