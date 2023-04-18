from src.helpers.nums_helpers import lower_common_multiple_array


class NumsService:
    def get_lower_common_multiple(self, nums: list[int]):
        return {
            f"The lower common multiple for array {nums} is":
            lower_common_multiple_array(nums)
        }

    def next_mumber(self, num: int):
        return {
            f"The number next to {num} is": num+1
        }
