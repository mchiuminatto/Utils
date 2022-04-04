"""
This library is created to implement utilities around binary search like:

search with exact match
search with not exact match

Apply previous operations in reversed order arrays.

"""

class BinarySearch:

    def binary_search_exact_asc_rec(self, x: any, A: list, left: int, right: int) -> int:
        """
        Recursive implementation of binary search for an exact match on an ascending ordered array.

        Args:
            x: value to be found
            A: array where to search the value for
            left: low boundary of the array sub-array where to search for
            right: high boundary of the sub-array to search for

        Returns:
            index: position where tha value was found
            -1   : if the value was not found

        """
        # print('x=', x, 'In:', "left=", left, "right=", right, "A[low:high]", A[left:right + 1])

        if left>right:
            # value was not found and no more split is possible
            return -1

        if right == 0:
            return -1


        mid = (left + right) // 2
        # print("Mid ", mid)
        # print("A=", A, "A[mid]=", A[mid])

        if x == A[mid]:
            # value found at mid
            return mid

        # further splitting is possible so we decide where to split at
        if x > A[mid]:
            # search on right half
            # print('Right half', A[mid + 1: high + 1])
            return self.binary_search_exact_asc_rec(x, A, mid + 1, right)
        elif x < A[mid]:
            # search on the left half
            # print('Left half', A[low: mid])
            return self.binary_search_exact_asc_rec(x, A, left, mid)

    def binary_search_exact_asc_iter_any(self, x: any, A: list) -> int:
        """
        Finds element x in array A using binary search, returning any found (not necessarily the
        first or last one found

        Args:
            x: Value to be found
            A: Array where to search the value for.

        Returns:
            i: Array index where the value was found

        """

        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2 # (high + low) can lead to overflow
            if x == A[mid]:
                return mid  # element found
            if  x > A[mid]:
                left = mid + 1  # element could be on the right side
            else:
                right = mid - 1  # element could be on the left side

        return -1


    def binary_search_exclo_asc_rec(self, x: any, A: list, low: int, high: int) -> (bool, int):

        """
        Recursive implementation of binary search, for exact match and closer match if not found
        on an ascending ordered array

        Args:
            x: value to be found
            A: array where to search the value for
            low: low boundary of the array sub-array where to search for
            high: high boundary of the sub-array to search for

        Returns:
            found: Boolean indicating whether the value was found or not (True/False)
            index: If the value was found, is the index where the value was found otherwise is the
                   index value at right (or the first greater value).

                   Special Cases:
                   - if the value is lower than the first value of the list, index = 0.
                   - if the value is higher than the latest in the list, index = len(A)

        """
        print('In:', "low=", low, "high=", high, "A[low:high]", A[low:high + 1])
        mid = (low + high) // 2
        print("mid=", mid, "A=", A, "A[mid]=", A[mid])

        if x == A[mid]:
            # value found at mid position
            return (True, mid)
        if high == low:
            # value was not found and no more split is possible
            return (False, high)
        # further splitting is possible so we decide where to split at
        if x > A[mid]:
            # search on right half
            print('Right half', A[mid + 1: high + 1])
            return self.binary_search_exclo_asc_rec(x, A, mid + 1, high)
        elif x < A[mid]:
            # search on the left half
            print('Left half', A[low: mid])
            return self.binary_search_exclo_asc_rec(x, A, low, mid)
