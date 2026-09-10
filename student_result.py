import sys
def calculate_result(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    if mark1 >= 40 and mark2 >= 40 and mark3 >= 40 and average >= 40:
        result = "PASS"
    else:
        result = "FAIL"
    return total, average, result
if __name__ == "__main__":
    mark1 = int(sys.argv[1])
    mark2 = int(sys.argv[2])
    mark3 = int(sys.argv[3])
    total, average, result = calculate_result(mark1, mark2, mark3)
    print("=================================")
    print("Student Result")
    print("=================================")
    print(f"Subject 1 Marks : {mark1}")
    print(f"Subject 2 Marks : {mark2}")
    print(f"Subject 3 Marks : {mark3}")
    print(f"Total Marks     : {total}")
    print(f"Average Marks   : {average:.2f}")
    print(f"Result          : {result}")
    print("=================================")