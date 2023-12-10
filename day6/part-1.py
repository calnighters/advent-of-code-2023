races = []
input_file = open("input.txt", "r")
times = input_file.readline().replace("Time:", "").strip().split()
distances = input_file.readline().replace("Distance:", "").strip().split()
for i in range(0, len(times)):
    races.append((int(times[i]), int(distances[i])))
input_file.close()

total = 1
for race in races:
    count_record_beat = 0
    record_distance = race[1]
    time = race[0]
    for i in range(0, time + 1):
        velocity = i
        time_remaining = time - velocity
        total_distance = time_remaining * velocity
        if total_distance > record_distance:
            count_record_beat += 1
    total *= count_record_beat

print(total)
