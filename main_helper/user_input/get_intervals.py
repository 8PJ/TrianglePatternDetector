def get_intervals(valid_intervals_org):
    valid_intervals = valid_intervals_org.copy()
    
    intervals = []
    input_interval = input(f"Please select an interval: ")

    while (input_interval != "" or len(intervals) < 1) and len(valid_intervals) > 0:
        if input_interval == "":
            input_interval = input(f"Please select at least one interval: ")
            continue

        if input_interval in valid_intervals:
            intervals.append(input_interval)
            valid_intervals.remove(input_interval)

            print(f"Currently selected intervals: {intervals}")

            if len(valid_intervals) > 0:
                input_interval = input(f"Please select an interval: ")
            else:
                break
        else:
            input_interval = input(f"Interval not valid. Please select one of {valid_intervals}: ")
            continue

    return intervals