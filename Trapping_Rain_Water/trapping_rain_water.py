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
    
    if left_up and left_bound == index:
        left_bound = 0
    
    # Find right bound
    for i in range(index, len(heights)):
        if heights[i] > heights[index]:
            right_up = True
        
        if right_up and heights[i] < heights[i-1]:
            right_bound = i - 1
            break
    
    if right_up and right_bound == index:
        right_bound = len(heights) - 1
    
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
    heights = [1,2,3,4,5,6,7,8,0,8]
    water_trapped = trapping_rainwater(heights)

    print(water_trapped)


if __name__ == "__main__":
    tic = time.time()    
    main()
    toc = time.time()

    print(f"Completed in {toc - tic:.4f} seconds")
