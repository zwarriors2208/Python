l = "Echo echoes through the valley as the echo of the echo echoes off the walls, making the echo seem endless".split()

siz = len(l)

for i in range(0,siz):
    if i%2 != 0:
        l[i] = 'replaced'
    else:
        continue


l1 = " ".join(l)

print(l1)

# l = "Echo echoes through the valley as the echo of the echo echoes off the walls, making the echo seem endless".split()
# for i in range(0,len(l)):
#     if i%2 != 0:
#         l[i] = 'replaced'
#
# l1 = " ".join(l)
# print(l1)