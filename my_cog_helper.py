def say_hi_helper(*args):
    if len(args) == 2 and str(args[0]).lower() == 'hello' and str(args[1]).lower() == 'there':
        return 'General Kenobi'
    else:
        return 'Hello there.'
