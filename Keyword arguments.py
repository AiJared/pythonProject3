def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian blue' ):
    print("-- This parrot wouldint", action, end= '')
    print("If you put", voltage, "volts through it.")
    print("-- lovely plumage the", type)
    print("-- It's", state, "!")
    # Calling the Function
parrot(1000) # 1 positional argument
parrot(voltage=1000) # 1 keyword argument
parrot(voltage=1000000, action= 'VOOOOOM') # 2 Keyword arguments
parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
parrot('one million', 'bereft of life', 'jump') # 3 positional arguments
parrot('a thousand', state= 'pushing up the diasies') # 1 positional argument 1 keyword argument

