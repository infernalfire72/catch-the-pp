import sys
import argparse

from osu_parser.beatmap import Beatmap
from osu.ctb.difficulty import Difficulty
from ppCalc import calculate_pp

def calculate(beatmap, acc, mods, x=0):
	#Yes... this be my test file (Will remove when project is done)
	beatmap = Beatmap(beatmap)
	difficulty = Difficulty(beatmap, int(mods))
	if x is None:
		x = 0
	
	return calculate_pp(difficulty, float(acc), beatmap.max_combo, int(x))

	
parser = argparse.ArgumentParser(description="osu!catch pp calculator")
parser.add_argument('-b','--map', help="map", required=True)
parser.add_argument('-a','--accuracy', help="acc", required=True)
parser.add_argument('-m','--mods', help="mods", required=True)
parser.add_argument('-x','--xcount', help="misses", required=False)

args = parser.parse_args()

print(calculate(args.map, args.accuracy, args.mods, args.xcount))