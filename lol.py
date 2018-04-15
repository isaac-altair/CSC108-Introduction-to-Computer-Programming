file = open('lollypop.txt', 'r')
for line in file:
    if 'lol' in line:
        print(line.lower().strip())
file.close

new_file = open('output.txt', 'w')
new_file.write("lolly,\nlolly, lolly;\nlollypop, lollypop,\nooh lolly, lolly, lolly,\nlollypop!\nlol :-)\n")
new_file.close


