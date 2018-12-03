
f = open('./input/aoc2017_01.txt', 'r')

data = f.readlines()

def part_1(dat):
    nums = ''.join(dat)
    captcha = 0
    for i in range(len(nums)):
        if i == len(nums)-1:
            if nums[i] == nums[0]:
                captcha += int(nums[i])
        elif nums[i] == nums[i+1]:
            captcha += int(nums[i])
    return captcha

def part_2(dat):
    nums = ''.join(dat)
    captcha = 0
    for i in range(len(nums)):
        if i >= len(nums)/2:
            if nums[i] == nums[i-int(len(nums)/2)]:
                captcha += int(nums[i])
        elif nums[i] == nums[i+int(len(nums)/2)]:
            captcha += int(nums[i])
    return captcha

print(part_1(data))
print(part_2(data))
