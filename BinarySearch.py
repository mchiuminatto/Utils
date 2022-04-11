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

    def find_exact_asc_iter_any(self, x: any, A: list) -> int:
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
            elif  x > A[mid]:
                left = mid + 1  # element could be on the right side
            else:
                right = mid - 1  # element could be on the left side

        return -1

    def find_exact_asc_iter_first(self, x: any, A: list) -> int:
        """
        Finds the first occurrence of x in the array, in case there are more than one

        Args:
            x: Value to be found
            A: Array where to search the value for.

        Returns:
            i: Array index where the value was found

        """

        _left = 0
        _right = len(A) - 1
        _result = -1
        while _left <= _right:
            mid = _left + (_right - _left) // 2  # (high + low) can lead to overflow
            if x == A[mid]:
                _result = mid
                _right = mid - 1
            elif x > A[mid]:
                _left = mid + 1  # element could be on the right side
            else:
                _right = mid - 1  # element could be on the left side

        return _result

    def find_exact_asc_iter_last(self, x: any, A: list) -> int:
        """
        Finds the last occurrence of x in the array, in case it there is more than one

        Args:
            x: Value to be found
            A: Array where to search the value for.

        Returns:
            i: Array index where the value was found

        """

        _left = 0
        _right = len(A) - 1
        _result = -1
        while _left <= _right:
            mid = _left + (_right - _left) // 2  # (high + low) can lead to overflow
            # print("Left ", _left, "Right ", _right, "Mid ", mid, "A[mid]", A[mid], "Result ", _result)
            if x == A[mid]:
                _result = mid
                _left = mid + 1
            elif x > A[mid]:
                _left = mid + 1  # element could be on the right side
            else:
                _right = mid - 1  # element could be on the left side

        return _result

    def count_instances(self, x: any, A: list)->(int, int, int):
        """
        Count instances of x found in A

        Args:
            x: value to be found and counted
            A: Array where to search in

        Returns:

            n: number is instances, -1 if none is found.
            first: first position where x was found
            last: last position where x was found

        """
        _first = self.find_exact_asc_iter_first(x, A)
        if _first == -1:
            return 0, -1, -1
        else:
            _last = self.find_exact_asc_iter_last(x, A)
        return _last - _first + 1, _first, _last

    def find_next_match(self, x: any, A: list)-> (bool, int):

        """
        Performs a search of x in A. If found, returns True and a position
        whe it was found. If not found, returns False and the position where should
        be inserted.

        Args:
            x: Value to search for
            A: List where to search on

        Returns:

            result: Boolean indicating True if value is found, and False if the value is ot found.
                 n: Position where the value was found (result = True) or position where the value
                    should be inserted (result = False)

        """

        left: int = 0
        right: int = len(A) - 1
        result: bool = False
        mid: int = -1

        if x < A[left]: return (result, 0)
        if x > A[right]: return (result, len(A))

        while (left <= right):
            mid = right - (right - left) // 2
            if x == A[mid]:
                result = True
                break
            elif x < A[mid]:
                right = mid - 1
            else:
                left =mid + 1

        return (result, mid)

    def find_next_match_desc(self, x: any, A: list)-> (bool, int):

        """
        Performs a search of x in A. If found, returns True and a position
        whe it was found. If not found, returns False and the position where should
        be inserted.

        Args:
            x: Value to search for
            A: List where to search on

        Returns:

            result: Boolean indicating True if value is found, and False if the value is ot found.
                 n: Position where the value was found (result = True) or position where the value
                    should be inserted (result = False)

        """

        left: int = 0
        right: int = len(A) - 1
        mid: int = -1

        if x > A[left]: return (False, 0)
        if x < A[right]: return (False, len(A))

        while (left <= right):
            mid = right - (right - left) // 2
            if x == A[mid]:
                return (True, mid)
            elif x < A[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return (False, mid + 1)

