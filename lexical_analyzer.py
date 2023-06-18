def analyze(input_string):
    """
    accepted states = 69, 70, 71, 72
    """
    ptr = 0
    state = 1
    while state != -1 and ptr < len(input_string):
        c = input_string[ptr]
        if state == 1:
            if c == "i":        state = 2
            elif c in "!=":     state = 3
            elif c == "T":        state = 6
            elif c == "F":        state = 9
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
        elif state == 6:
            if c == "r":        state = 7
            else:               state = -1
        elif state == 7:
            if c == "u":        state = 8
            else:               state = -1
        elif state == 8:
            if c == "e":        state = 73
            else:               state = -1
        elif state == 9:
            if c == "a":        state = 10
            else:               state = -1
        elif state == 10:
            if c == "l":        state = 11
            else:               state = -1
        elif state == 11:
            if c == "s":        state = 12
            else:               state = -1
        elif state == 12:
            if c == "e":        state = 73
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
            elif c == ":":      state = 69
            else:               state = -1
        elif state == 73:
            if c == ":":        state = 69
            else:               state = -1

        ptr += 1 if state != -1 else 0

    return state >= 69, ptr
