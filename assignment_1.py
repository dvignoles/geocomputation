"""
Assignment 1 Geocomputation Spring 2022 Hunter College
Daniel Vignoles
"""


if __name__ == "__main__":
    # pre-sorting for median
    nums = sorted([1, 2, 46, 72, 7, 168, 44, 3, 3, 3, 5, 2, 22, 222, 79, 100, 250])

    # 1 - Mean
    mysum = 0
    for n in nums:
        mysum += n

    mean = mysum / len(nums)
    print(f"Mean: {mean}")

    # 2 - Variance
    # list comprehension used for "loop"
    variance = sum([(x - mean) ** 2 for x in nums]) / (len(nums) - 1)
    print(f"Variance: {variance}")

    # 3 - Median
    if len(nums) % 2 == 1:
        # odd case (int always rounds down)
        median = nums[int(len(nums) / 2)]
    else:
        # even case (average two middle values)
        median = (nums[len(nums) / 2] + nums[len(nums / 2) - 1]) / 2
    print(f"Median: {median}")

    # 4 - Mode
    num_counts = {}
    for n in nums:
        if n in num_counts:
            # already in dict
            num_counts[n] += 1
        else:
            # add new dict entry
            num_counts[n] = 1

    # max of dictionary via get method
    mode = max(num_counts, key=num_counts.get)
    print(f"Mode: {mode}")
