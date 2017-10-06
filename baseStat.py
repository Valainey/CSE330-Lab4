import re
import sys, os


if len(sys.argv) < 2:
    sys.exit("Usage: %s filename" % sys.argv[0])
filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

f = open(filename, "r")	
players = {} 
pat3 = re.compile('^(.+)\sbatted\s(\d)\stimes.+(\d)\shits.+ runs')
for line in f:
	r3 =pat3.match(line)
	if r3:
		name = r3.group(1)
		bats = int(r3.group(2))
		hits = int(r3.group(3))
		if name in players:
			# increment the bats and hits                      
			players[name][1] += bats
			players[name][2] += hits
		else:
			# Add to dict players 
			players[name] = [name, bats, hits]

f.close()
score ={} #matching and save the inform
#sorting and round from hightest to lowest
for name in players:
    batAverage = round(float(players[name][2]) / float(players[name][1]), 3)
    #score.append(batAverage)
    score[players[name][0]] = batAverage
best=sorted(score.items(), reverse=True, key= lambda batAverage:batAverage[1]) #matching from highest to lowest
for item in best:
    print item[0],':',"%.3f" %item[1]