import sys

def sol(address):
    input_data = open(address).read().strip()
    reports = input_data.split('\n')
    
    def is_safe(report):
        increasing = True
        decreasing = True

        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i+1])

            if diff < 1 or diff > 3:
                return False

            if report[i] > report[i+1]:
                increasing = False

            if report[i] < report[i+1]:
                decreasing = False

        return increasing or decreasing

    def can_be_safe_by_removing_one(report):
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]

            if is_safe(new_report):
                return True

        return False
    
    safe_reports_p1 = 0
    safe_reports_p2 = 0
    
    for report in reports:
        levels = list(map(int, report.split()))
        
        if is_safe(levels):
            safe_reports_p1 += 1
        
        if can_be_safe_by_removing_one(levels):
            safe_reports_p2 += 1
    
    print("Solution 1: " + str(safe_reports_p1))
    print("Solution 2: " + str(safe_reports_p2))


test_link = "test.txt"
real_link = "input.txt"
sol(test_link)
sol(real_link)
