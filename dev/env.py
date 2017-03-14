"""for environment-checking tasks"""

def is_python2():
    try:
        print("💩")
        return False
    except SyntaxError:
        return True
