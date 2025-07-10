def longest_increasing_subsequence(nums):
    result = []
    for index, number in enumerate(nums):
        print(index, number)
        sub_seq = [number]
        for num in nums[index+1:]:
            if num > sub_seq[-1]:
                sub_seq.append(num)
        result.append(sub_seq)
    return result

def count_triplets(nums, k):
    """

    """
    for index, data in enumerate(nums):
        if len(nums) < index + 3:
            print("Processing complete")
            print(index, data)
            return
        print(nums[index] + nums[index + 1] + nums[index + 2])
        if nums[index] + nums[index + 1] + nums[index + 2] == k:
            return nums[index], nums[index + 1],  nums[index + 2]



if __name__ == '__main__':
    nums = [4,5,6,1,3,4,2,1,1]
    k = 6
    print(count_triplets(nums, k))


# if __name__ == '__main__':
#     nums = [10, 9, 2, 5, 3, 3, 7, 101, 18]
#     longest_increasing_subsequence(nums)
#     print(nums)
#     print(longest_increasing_subsequence(nums))


