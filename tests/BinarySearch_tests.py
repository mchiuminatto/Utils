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

        A = [1, 2, 3, 5, 7, 9, 12, 20]
        x = 9
        _res = _bs.binary_search_exact_asc_rec(x, A, 0, len(A)-1)
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
        _res = _bs.binary_search_exact_asc_iter_any(x, A)
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
        _res = _bs.binary_search_exact_asc_iter_any(x, A)
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
        _res = _bs.binary_search_exact_asc_iter_any(x, A)
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
            _res = _bs.binary_search_exact_asc_iter_any(x, A)
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
            _res = _bs.binary_search_exact_asc_iter_any(x, A)
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
            _res = _bs.binary_search_exact_asc_iter_any(x, A)
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


if __name__ == "__main__":
    _test = Tests()
    _test.run([15])
