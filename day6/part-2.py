input_file = open("input.txt", "r")
time = int(input_file.readline().replace("Time:", "").strip().replace(" ", ""))
distance = int(input_file.readline().replace("Distance:", "").strip().replace(" ", ""))
input_file.close()

count_record_beat = 0
for i in range(0, time + 1):
    velocity = i
    time_remaining = time - velocity
    total_distance = time_remaining * velocity
    if total_distance > distance:
        count_record_beat += 1

print(count_record_beat)
