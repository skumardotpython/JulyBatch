def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary(email):

    print("I am ordinary")


ordinary()
# ord = ordinary
#
# inn = make_pretty(ord)
# inn()