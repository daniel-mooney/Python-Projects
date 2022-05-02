# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
# For example, Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
import time

def find_boundings(heights: list[int], index: int) -> tuple[int, int]:
    left_bound = index
    left_up = False
    right_bound = index
    right_up = False
    
    # Find left bound
    for i in range(index, -1, -1):
        if heights[i] > heights[index]:
            left_up = True
        
        if left_up and heights[i] < heights[i+1]:
            left_bound = i + 1
            break
    
    # Find right bound
    for i in range(index, len(heights)):
        if heights[i] > heights[index]:
            right_up = True
        
        if right_up and heights[i] < heights[i-1]:
            right_bound = i - 1
            break
    
    return (left_bound, right_bound)


def calculate_water_held(heights: list[int], left: int, right: int) -> int:
    water_held = 0
    water_level = min(heights[left], heights[right])

    for i in range(left + 1, right):
        if heights[i] < water_level:
            water_held += water_level - heights[i]

    return water_held


def trapping_rainwater(heights: list[int]) -> int:
    
    water_trapped = 0

    i = 0
    while i < len(heights):
        left, right = find_boundings(heights, i)

        if left == i or right == i:
            i += 1
            continue
        
        water_trapped += calculate_water_held(heights, left, right)
        i = right
    
    return water_trapped


def main() -> None:
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    water_trapped = trapping_rainwater(heights)

    print(water_trapped)


if __name__ == "__main__":
    tic = time.time()    
    main()
    toc = time.time()

    print(f"Completed in {toc - tic:.4f} seconds")