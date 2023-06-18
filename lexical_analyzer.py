def analyze(input_string):
    """
    accepted states = 69, 70, 71
    """
    ptr = 0
    state = 1
    while state != -1 and ptr < len(input_string):
        c = input_string[ptr]
        if state == 1:
            if c == "i":        state = 2
            elif c in "!=":     state = 3
            elif c == ":":      state = 69
            elif c in "><":     state = 70
            elif c in "qrst":   state = 71
            elif c == "p":      state = 72
            else:               state = -1
        elif state == 2:
            if c == "f":        state = 69
            else:               state = -1
        elif state == 3:
            if c == "=":        state = 69
            else:               state = -1
        elif state == 4:
            if c == "s":        state = 5
            else:               state = -1
        elif state == 5:
            if c == "s":        state = 69
            else:               state = -1
        elif state == 69:
            state = -1
        elif state == 70:
            if c == "=":        state = 69
            else:               state = -1
        elif state == 71:
            if c == ":":        state = 69
            else:               state = -1
        elif state == 72:
            if c == "a":        state = 4
            elif c in "pqrst":  state = 71
            else:               state = -1

        ptr += 1 if state != -1 else 0

    return state >= 69, ptr
