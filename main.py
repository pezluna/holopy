import holopy
import pprint

con = holopy.old_connect()

schedule = holopy.old_beautify(con)

pprint.pprint(schedule)

ccon = holopy.connect()

for c in ccon:
    for cc in ccon[c]:
        print(cc.getInfo())
