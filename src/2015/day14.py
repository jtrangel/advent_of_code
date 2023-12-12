from typing import List, Dict

def read(path) -> str:
    return open(path, "r").read()

# Part 1
def get_distance(data: str, time: int) -> List[List]:

    info: List = []

    for line in data.splitlines():
        n = line.split(" ")
        reindeer: str = n[0]
        speed: int = int(n[3])
        runTime: int = int(n[6])
        restTime: int = int(n[-2])

        t: int = 0
        cycleTime: int = 1
        dist: int = 0
        while t < time:
            t += 1
            # print(t)

            # running
            if cycleTime <= runTime:
                # print(f"run-{cycleTime}")
                dist += speed
                cycleTime += 1
            # resting
            elif (cycleTime > runTime) and (cycleTime <= (restTime + runTime)):
                # print(f"rest-{cycleTime}")
                cycleTime += 1
                if cycleTime > (restTime + runTime):
                    # print(f"reset-{cycleTime}")
                    cycleTime = 1

        info.append([reindeer, dist])

    return info

# Part 2
# Need to invert code earlier, where I keep track of all reindeer simultaneously

# Utility function to transform text data into usable array of info.
# Could have used Dict but this seems better given the number of data points.
def get_reindeer_stats(data: str) -> List[List]:

    info: List = []
    for line in data.splitlines():
        n = line.split(" ")
        reindeer: str = n[0]
        speed: int = int(n[3])
        runTime: int = int(n[6])
        restTime: int = int(n[-2])

        info.append([reindeer, speed, runTime, restTime])

    return info

def get_points(stats: List[List], time: int) -> Dict:

    t: int = 0
    cycleTime: Dict = {}
    rein_dists: Dict = {}
    points: Dict = {}
    while t < time:
        t += 1

        # For each reindeer, track what distance and cycletime they have
        # at every second
        for n in stats:
            reindeer: str = n[0]
            speed: int = int(n[1])
            runTime: int = int(n[2])
            restTime: int = int(n[3])

            # Initialize all dictionaries
            if t == 1:
                rein_dists[reindeer] = 0
                cycleTime[reindeer] = 1
                points[reindeer] = 0

            # running
            if cycleTime[reindeer] <= runTime:
                # if reindeer == 'Vixen':
                #     print(f"run-{cycleTime[reindeer]}")
                rein_dists[reindeer] += speed
                cycleTime[reindeer] += 1
            # resting
            elif (cycleTime[reindeer] > runTime) and (cycleTime[reindeer] <= (restTime + runTime)):
                # if reindeer == 'Vixen':
                #     print(f"rest-{cycleTime[reindeer]}")
                cycleTime[reindeer] += 1
                if cycleTime[reindeer] > (restTime + runTime):
                    # if reindeer == 'Vixen':
                    #     print(f"reset-{cycleTime[reindeer]}")
                    cycleTime[reindeer] = 1

        # Getting max distance, which tells us the reindeers in the lead
        lead = max(rein_dists.values())

        # Assign points to reindeers in the lead
        for key, val in rein_dists.items():
            if val == lead:
                points[key] += 1

    return points

if __name__ == "__main__":
    inpt = read("./inputs/day14.txt")

    # Part 1
    dists = get_distance(data=inpt, time=2503)
    max_dist = max([n[1] for n in dists])
    print(max_dist)

    # Part 2
    stats = get_reindeer_stats(data=inpt)
    points = get_points(stats=stats, time=2503)
    max_points = max(points.values())
    print(max_points)

