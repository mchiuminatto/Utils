from Test.TestBase import TestBase
from Utils.BinarySearch import BinarySearch
import numpy as np


class Tests(TestBase):

    def test_case_1(self):
        """
        Base case: search for an existing value in a small array exact mach
        Returns:
            5

        """
        _bs = BinarySearch()

        a = [1, 2, 3, 5, 7, 9, 12, 20]
        x = 9
        _res = _bs.binary_search_exact_asc_rec(x, a, 0, len(a)-1)
        if _res == 5: return True

    def test_case_2(self):
        """
        Base case: search for an NON existing value in a small array, exact mach. The value
        is lower than the array's first one.
        Returns:
            5

        """
        _bs = BinarySearch()

        A = [1, 2, 3, 5, 7, 9, 12, 20]
        x = -3
        _res = _bs.binary_search_exact_asc_rec(x, A, 0, len(A)-1)
        if _res == -1: return True

    def test_case_3(self):
        """
        Base case: search for an NON existing value in a small array, exact mach. The value
        is greater than the array's last one.
        Returns:
            5

        """
        _bs = BinarySearch()

        A = [1, 2, 3, 5, 7, 9, 12, 20]
        x = 50
        _res = _bs.binary_search_exact_asc_rec(x, A, 0, len(A)-1)
        if _res == -1: return True

    def test_case_4(self):
        """
        Massive test

        Returns:
            5

        """
        _bs = BinarySearch()

        A = list(np.random.randint(0,1000, 1000))
        A.sort()
        search_for = list(np.random.randint(0, 1000, 1000))
        _check = True
        for x in search_for:
            print("Processing ", x)
            _res = _bs.binary_search_exact_asc_rec(x, A, 0, len(A)-1)

            if _res == -1:
                try:
                    A.index(x)
                    _check = False
                except Exception as e:
                    _check = True
            else:
                _check = A.index(x) == _res
            if not _check:
                print("Error ", _res, A.index(x))
                return False

    def test_case_10(self):
        """
        Base case: search for an existing value in a small array exact mach
        Returns:
            5

        """
        _bs = BinarySearch()

        A = [1, 2, 3, 5, 7, 9, 12, 20]
        x = 9
        _res = _bs.find_exact_asc_iter_any(x, A)
        if _res == 5: return True

        return False

    def test_case_11(self):
        """
        Base case: search for an NON existing value in a small array, exact mach. The value
        is lower than the array's first one.
        Returns:
            5

        """
        _bs = BinarySearch()

        A = [1, 2, 3, 5, 7, 9, 12, 20]
        x = -3
        _res = _bs.find_exact_asc_iter_any(x, A)
        if _res == -1: return True

    def test_case_12(self):
        """
        Base case: search for an NON existing value in a small array, exact mach. The value
        is greater than the array's last one.
        Returns:
            5

        """
        _bs = BinarySearch()

        A = [1, 2, 3, 5, 7, 9, 12, 20]
        x = 50
        _res = _bs.find_exact_asc_iter_any(x, A)
        if _res == -1: return True

    def test_case_13(self):
        """
        Massive test, A set in in range 0 to 1000
        Values to look for are in the range -500 to 1500 so some values should not be found

        Returns:
            5

        """
        _bs = BinarySearch()
        _stat_found = 0
        _stat_not_found = 0

        A = list(np.random.randint(0,1000, 1000))
        A.sort()
        search_for = list(np.random.randint(-500, 1500, 100000))
        _check = True
        for x in search_for:
            _res = _bs.find_exact_asc_iter_any(x, A)
            if _res == -1:
                try:
                    A.index(x)
                    _check = False
                except Exception as e:
                    _stat_not_found += 1
                    _check = True
            else:
                indices = list([i for i, n in enumerate(A) if n == x])
                _check = _res in indices
                _stat_found += 1
            if not _check:
                print("Error ", _res, A.index(x), A)
                return False
        print("Found ", _stat_found, "Not found ", _stat_not_found)

        _test_2 = _stat_found != 0
        _test_3 = _stat_not_found != 0

        return _check and _test_2 and _test_3

    def test_case_14(self):
        """
        Massive test, A set in in range 0 to 1000
        Values to look for is a random subset of A set so all the values should be found

        Returns:
            5

        """
        _bs = BinarySearch()
        _stat_found = 0
        _stat_not_found = 0

        A = list(np.random.randint(0,1000, 1000))
        A.sort()
        B = list(np.random.randint(-500, 1500, 100000))
        search_for = set(A).intersection(set(B))
        _check = True
        for x in search_for:
            _res = _bs.find_exact_asc_iter_any(x, A)
            if _res == -1:
                try:
                    A.index(x)
                    _check = False
                except Exception as e:
                    _stat_not_found += 1
                    _check = True
            else:
                indices = list([i for i, n in enumerate(A) if n == x])
                _check = _res in indices
                _stat_found += 1
            if not _check:
                print("Error ", _res, A.index(x), A)
                return False
        print("Found ", _stat_found, "Not found ", _stat_not_found)

        _test_2 = _stat_found != 0
        _test_3 = _stat_not_found == 0

        return _check and _test_2 and _test_3

    def test_case_15(self):
        """
        Massive test, A set in in range 0 to 1000
        Values to look for are not in A so no value should be found

        Returns:
            5

        """
        _bs = BinarySearch()
        _stat_found = 0
        _stat_not_found = 0

        A = list(np.random.randint(0,1000, 1000))
        A.sort()
        B = list(np.random.randint(-500, 1500, 100000))
        search_for = set(B).difference(set(A))
        _check = True
        for x in search_for:
            _res = _bs.find_exact_asc_iter_any(x, A)
            if _res == -1:
                try:
                    A.index(x)
                    _check = False
                except Exception as e:
                    _stat_not_found += 1
                    _check = True
            else:
                indices = list([i for i, n in enumerate(A) if n == x])
                _check = _res in indices
                _stat_found += 1
            if not _check:
                print("Error ", _res, A.index(x), A)
                return False
        print("Found ", _stat_found, "Not found ", _stat_not_found)

        _test_2 = _stat_found == 0
        _test_3 = _stat_not_found != 0

        return _check and _test_2 and _test_3

    def test_case_20(self):
        """
        Finds the first occurrence of 5
        Returns:
            2

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 5, 5, 6, 7, 9, 12, 20]
        x = 5
        _res = _bs.find_exact_asc_iter_first(x, A)
        if _res == 2: return True

    def test_case_21(self):
        """
        Finds the first occurrence of 9
        Returns:
            7

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 5, 5, 6, 7, 9, 9, 20]
        x = 9
        _res = _bs.find_exact_asc_iter_first(x, A)
        if _res == 7: return True

    def test_case_22(self):
        """
        Finds the first occurrence of 9
        Returns:
            5

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 6, 7, 9, 12, 15, 18, 20]
        x = 9
        _res = _bs.find_exact_asc_iter_first(x, A)
        if _res == 5: return True

    def test_case_23(self):
        """
        Searches for a no existing element, greater then the right most
        Returns:
            -1

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 5, 5, 6, 7, 9, 9, 20]
        x = 25
        _res = _bs.find_exact_asc_iter_first(x, A)
        if _res == -1: return True

    def test_case_24(self):
        """
        Searches for a no existing element, lower than the leftmost
        Returns:
            -1

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 5, 5, 6, 7, 9, 9, 20]
        x = -10
        _res = _bs.find_exact_asc_iter_first(x, A)
        if _res == -1: return True

    def test_case_30(self):
        """
        Finds the first occurrence of 5
        Returns:
            2

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 5, 5, 6, 7, 9, 12, 20]
        x = 5
        _res = _bs.find_exact_asc_iter_last(x, A)
        if _res == 4: return True

    def test_case_31(self):
        """
        Finds the last occurrence of 9
        Returns:
            7

        """
        _bs = BinarySearch()

        A = [1, 2, 5, 5, 5, 6, 7, 9, 9, 20]
        x = 9
        _res = _bs.find_exact_asc_iter_last(x, A)
        print(_res)
        if _res == 8: return True

    def test_case_32(self):
        """
        Finds the first occurrence 2, with a block of 2's at the leftmost side

        Returns:
            5

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 6, 7, 9, 12, 15, 18, 20]
        x = 2
        _res = _bs.find_exact_asc_iter_first(x, A)
        if _res == 0: return True

    def test_case_33(self):
        """
        Finds the last occurrence 20, with a block of 20's at the rightmost side

        Returns:
            5

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 20
        _res = _bs.find_exact_asc_iter_last(x, A)
        if _res == 11: return True

    def test_case_40(self):
        """
        Finds the number of 5's in the array

        Returns:
            4,2,5

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 5
        _res = _bs.count_instances(x, A)

        _test_1 = _res[0] == 4
        _test_2 = _res[1] == 2
        _test_3 = _res[2] == 5

        return _test_1 and _test_2 and _test_3

    def test_case_41(self):
        """
        Finds the number of 2's in the array

        Returns:
            2, 0, 1

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 2
        _res = _bs.count_instances(x, A)

        _test_1 = _res[0] == 2
        _test_2 = _res[1] == 0
        _test_3 = _res[2] == 1

        return _test_1 and _test_2 and _test_3

    def test_case_42(self):
        """
        Finds the number of 20's in the array

        Returns:
            2, 0, 1

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 20
        _res = _bs.count_instances(x, A)

        _test_1 = _res[0] == 3
        _test_2 = _res[1] == 12
        _test_3 = _res[2] == 14

        return _test_1 and _test_2 and _test_3

    def test_case_43(self):
        """
        Try to find a non-existing value in the array A

        Returns:
            0, -1, -1

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 40
        _res = _bs.count_instances(x, A)

        print(_res)
        _test_1 = _res[0] == 0
        _test_2 = _res[1] == -1
        _test_3 = _res[2] == -1

        return _test_1 and _test_2 and _test_3

    def test_case_44(self):
        """
        Try to find a non-existing value in the array A

        Returns:
            0, -1, -1

        """
        _bs = BinarySearch()

        A = [2, 2,  5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 8
        _res = _bs.count_instances(x, A)

        _test_1 = _res[0] == 0
        _test_2 = _res[1] == -1
        _test_3 = _res[2] == -1

        return _test_1 and _test_2 and _test_3

    def test_case_50(self):
        """
        Match next: case 1: normal case, value within the array range

        Returns:
            False, 8

        """
        _bs = BinarySearch()

        A = [2, 2, 5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 19
        _res = _bs.find_next_match(x, A)
        _i = _res[1]

        print(_res, A[_i-1], x, A[_i]  )

        _test_1 = False
        if not _res[0]:

            _test_1 = (x > A[_i-1]) and (x < A[_i])



        return _test_1

    def test_case_51(self):
        """
        Match next: case 2: value is found

        Returns:
            False, 8

        """
        _bs = BinarySearch()

        A = [2, 2, 5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 5
        _res = _bs.find_next_match(x, A)

        print(_res)
        _test_1 = A[_res[1]] == x

        return _test_1

    def test_case_52(self):
        """
        Match next: special case: value lower than first element of a.

        Returns:
            False, 8

        """
        _bs = BinarySearch()

        A = [2, 2, 5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 1
        _res = _bs.find_next_match(x, A)

        print(_res)
        _test_1 = _res[1] == 0

        return _test_1

    def test_case_53(self):
        """
        Match next: special case: value lower than first element of a.

        Returns:
            False, 8

        """
        _bs = BinarySearch()

        A = [2, 2, 5, 5, 5, 5, 6, 7, 9, 12, 15, 18, 20, 20, 20]
        x = 30
        _res = _bs.find_next_match(x, A)

        print(_res)
        _test_1 = _res[1] == len(A)

        return _test_1

    # region descending arrays match and next

    def test_case_60(self):
        """
        Match next sorted descending :
        Normal case: value is missing but in the range of A's values

        Returns:
            False, 8

        """
        _bs = BinarySearch()

        A = [15, 14, 12, 12, 12, 8, 8, 7, 6, 3, 3]
        x = 10
        _res = _bs.find_next_match_desc(x, A)

        _i = _res[1]
        print(_i, A[_i-1], x, A[_i])
        _test_1 = (A[_i] < x) and  (A[_i] > x)

        return _test_1

    def test_case_61(self):
        """
        Match next sorted descending :
        Normal case: value is present

        Returns:
            False, 8

        """
        _bs = BinarySearch()

        A = [15, 14, 12, 12, 12, 8, 8, 7, 6, 3, 3]
        x = 8
        _res = _bs.find_next_match_desc(x, A)

        _i = _res[1]
        print(_i, A[_i-1], x, A[_i])
        _test_1 = A[_i] == x

        return _test_1

    def test_case_62(self):
        """
        Match next sorted descending :
        Special case: value is missing and lower than rightmost value

        Returns:
            False, len(A)

        """
        _bs = BinarySearch()

        A = [15, 14, 12, 12, 12, 8, 8, 7, 6, 3, 3]
        x = 1
        _res = _bs.find_next_match_desc(x, A)

        _i = _res[1]

        _test_1 = _i == len(A)
        # print(_res)

        return _test_1

    def test_case_63(self):
        """
        Match next sorted descending :
        Special case: value is missing and higher than leftmost value

        Returns:
            False, 0

        """
        _bs = BinarySearch()

        A = [15, 14, 12, 12, 12, 8, 8, 7, 6, 3, 3]
        x = 20
        _res = _bs.find_next_match_desc(x, A)

        _i = _res[1]

        _test_1 = _i == 0
        # print(_res)

        return _test_1

    #endregion

if __name__ == "__main__":
    _test = Tests()
    #_test.run([10,11,12,13,14, 15, 20,21,22,23,24, 30, 31, 32, 33, 40, 41, 42, 43, 44])
    _test.run([63])
