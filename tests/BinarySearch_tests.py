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
        _res = _bs.binary_search_exact_asc_iter(x, A)
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
        _res = _bs.binary_search_exact_asc_iter(x, A)
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
        _res = _bs.binary_search_exact_asc_iter(x, A)
        if _res == -1: return True

    def test_case_13(self):
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
            _res = _bs.binary_search_exact_asc_iter(x, A)

            if _res == -1:
                try:
                    A.index(x)
                    _check = False
                except Exception as e:
                    _check = True
            else:
                _check = A.index(x) == _res
            if not _check:
                print("Error ", _res, A.index(x), A)
                return False

if __name__ == "__main__":
    _test = Tests()
    _test.run([13])
