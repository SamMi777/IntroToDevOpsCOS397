# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def bubble(int_list):
    """
    Sorts a list of integers in place using the bubble sort algorithm.

    This algorithm steps through the list, compares pairs of elements,
    and swaps them if they are not in the correct ascending order.

    Args:
        int_list (list): A list of integers to be sorted

    Returns:
        list: The sorted list of integers
    """
    n = len(int_list)
    if n <= 1:
        return int_list
    for i in range(n-1):
        for j in range(n-i-1):
            if int_list[j] > int_list[j+1]:
                int_list[j],int_list[j+1] = int_list[j+1], int_list[j]
    print("bubble sort")
    return int_list


def quick(int_list):
    """
    Sorts a list of integers in place using the quicksort algorithm

    This algorithm selects a pivot element from the list and uses the
    remaining elements to create two sub-arrays. The sub-arrays are then sorted
    recursively.

    Args:
        int_list (list): A list of integers to be sorted

    Returns:
        list: The sorted list of integers
    """
    n = len(int_list)
    if n <= 1:
        return int_list
    pivot = int_list[n // 2]
    left = [ i for i in int_list if i < pivot]
    middle = [i for i in int_list if i == pivot]
    right = [i for i in int_list if i > pivot]
    # print("quick sort")
    return quick(left) + middle + quick(right)


def insertion(int_list):
    """
    insertion docstring
    """