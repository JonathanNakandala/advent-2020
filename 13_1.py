def load_data() -> list:
    with open("data/data_13.txt") as data_file:
        data_string = data_file.read()
    data_array = data_string.split("\n")
    start_timestamp = int(data_array[0])
    busses = data_array[1].split(",")
    busses = [int(x) for x in busses if x != "x"]
    return start_timestamp, busses


def generate_bus_timetable(busses):
    timestamps = []
    for bus in busses:
        time = 0
        end = 5000000
        times = []
        while time < end:

            times.append(time)

            time += bus

        timestamps.append({"bus": bus, "times": times})
    return timestamps



def find_earliest_bus(timetables, start):
    def check_time(time):
        if time > start:
            return True
        else: False
    possibilites = []
    for timetable in timetables:
        earliest_time = next(time for time in timetable['times'] if check_time(time))
        possibilites.append({"bus": timetable['bus'], "time": earliest_time })
    
    smallest = 99999999999999999999999
    bus = 0
    for possibility in possibilites:
        if possibility['time'] < smallest:
            smallest = possibility['time']
            bus =  possibility['bus']
    return bus, smallest

def calculate_answer(start, arrival, bus):
    return (arrival - start) * bus
    

start_timestamp, busses = load_data()
timetables = generate_bus_timetable(busses)
earliest_bus, arrival_time = find_earliest_bus(timetables, start_timestamp)

answer = calculate_answer(start_timestamp, arrival_time, earliest_bus)
print(earliest_bus, arrival_time)
print(answer)