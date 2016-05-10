from collections import Counter
for k,v in sorted( Counter(raw_input()).most_common(3), key = lambda x: (-x[1],x[0])):
    print k,v