"""Exercise 4: List Utility Functions"""

__author__: str = '730577151'

def all(list: list[int], match: int) -> bool:
    length: int = len(list)
    n: int = 0
    while n < length:
        if match == list[n]:
         return True
        n = n + 1
    return False

def max(list: list[int]) -> int:
   if len(list) == 0:
      raise ValueError("max() arg is an empty list")
   maximum = list[0]
   n = 0
   while n < len(list):
      if input[n] > maximum:
         maximum = input[n]
      n = n + 1
   return maximum


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
   if len(list_1) != len(list_2):
      return False
   n = 0
   while n < len(list_1):
      if list_1[n] != list_2[n]:
         return False
      n = n + 1
   return True