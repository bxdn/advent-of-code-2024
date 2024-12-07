
def is_possible(nums, goal, total, i = 1):
    if total > goal:
        return False
    if i == len(nums):
        return total == goal
    if is_possible(nums, goal, total + nums[i], i + 1):
        return True
    if is_possible(nums, goal, total * nums[i], i + 1):
        return True
    return is_possible(nums, goal, int(f'{total}{nums[i]}'), i + 1)

def process_line(raw_line):
    goal, num_str = raw_line.split(':')
    goal = int(goal)
    nums = list(map(int, num_str.split()))
    return nums, goal

lines = open('in.txt').readlines()
processed_lines = [process_line(line) for line in lines]
possible_goals = [goal for nums, goal in processed_lines if is_possible(nums, goal, nums[0])]
total = sum(possible_goals)
print(total)
