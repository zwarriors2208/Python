s="Echo echoes through the valley as the echo of the echo echoes off the walls, making the echo seem endless"
s = s.lower()

# i is the index of repeated letter
i = s.find('echo')
l = [i]
while True:
    i = s.find('echo',i+1, len(s))
    if i > 0:
        l.append(i)
    else:
        break

s = s.replace('echo','rebound',1)
s = s.replace('echo','Reverberation ')
print(s)


# s="Echo echoes through the valley as the echo of the echo echoes off the walls, making the echo seem endless"
# s = s.lower()
# l=[]
# i=0
# while i>=0:
#     l.append(i)
#     i=s.find('echo',i+1,len(s))
#
# print(l)