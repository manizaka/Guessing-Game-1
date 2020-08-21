hint = ""
que = input("Enter the name: ").lower()
for letter in range(0, len(que)):
    if que[letter] == " ":
        hint = hint + " "
    else:
        hint = hint + "*"
print("Hidden word: " + hint)
l = 0
for x in hint:
    if x == "*":
        l += 1
    else:
        l = l
frm = 0
lim = l
while frm < l:
    try:
        tr = ""
        print("Chances left: " + str(l-frm))
        guess = input("Guess the alphabet in " + "'" + hint + "': ").lower()
        if len(guess) > 1:
            print("===>>Enter one alphabet!!!<<==")
        else:
            thi = hint
            for letter in range(0, len(que)):
                if guess[0] == que[letter]:
                    tr = tr + guess[0]
                else:
                    tr = tr + hint[letter]
                if tr == thi:
                    frm += 1
            if frm == l:
                print("You lose!")
                print("Hidden word is " + que)
            elif tr == que:
                print("Yon won!")
                print("That's right, it's " + tr.upper())
                frm = l
            hint = tr
            if frm != l:
                print("Hidden word: " + tr)
    except:
        print("You didn't enter alphabet!")