tictak = [["...", "...", "..."], ["...", "...", "..."], ["...", "...", "..."]]


def print_puzzle():
    for i in range(len(tictak)):
        print(tictak[i])
        print(" -------------------")


print_puzzle()
for _ in range(9):
    player = input("Which player are playing(O or X): ").upper()
    if player == "O" or player == "X":
        place = input("Select the cell you want to mark it: ")
        i = int(place[0]) - 1
        j = int(place[1]) - 1
        if tictak[i][j] == "...":
            tictak[i][j] = player
        else:
            print("please choose an empty one to fill")
    else:
        print("please enter a valid player O or X")
    print_puzzle()
