#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    direc = dir(hidden_4)
    void = "__"
    for i in range(0, len(direc)):
        if void not in direc[i]:
            print(direc[i])
