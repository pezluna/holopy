import holopy
import pprint

# old style
con = holopy.old_connect()

schedule = holopy.old_beautify(con)

pprint.pprint(schedule)

# new style
ccon = holopy.connect()

for c in ccon:
    for cc in ccon[c]:
        print(cc.getInfo())
