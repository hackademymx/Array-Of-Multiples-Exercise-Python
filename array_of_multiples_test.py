import arrayOfMultiples
import collections

def test_array_of_multi_one():
    print('Multiples of 7, 5 times')
    multiple_list = [7, 14, 21, 28, 35]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(7,5)) == collections.Counter(multiple_list)

def test_array_of_multi_two():
    print('Multiples of 17, 6 times')
    multiple_list = [17, 34, 51, 68, 85, 102]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(17,6)) == collections.Counter(multiple_list)

def test_array_of_multi_three():
    print('Multiples of 17, 7 times')
    multiple_list = [17, 34, 51, 68, 85, 102, 119]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(17,7)) == collections.Counter(multiple_list)

def test_array_of_multi_four():
    print('Multiples of 630, 14 times')
    multiple_list = [630, 1260, 1890, 2520, 3150, 3780, 4410, 5040, 5670, 6300, 6930, 7560, 8190, 8820]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(630,14)) == collections.Counter(multiple_list)

def test_array_of_multi_five():
    print('Multiples of 140, 3 times')
    multiple_list = [140, 280, 420]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(140,3)) == collections.Counter(multiple_list)

def test_array_of_multi_six():
    print('Multiples of 7, 8 times')
    multiple_list = [7, 14, 21, 28, 35, 42, 49, 56]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(7,8)) == collections.Counter(multiple_list)

def test_array_of_multi_seven():
    print('Multiples of 11, 21 times')
    multiple_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231]
    assert collections.Counter(arrayOfMultiples.get_arrayOfMultiples(11,21)) == collections.Counter(multiple_list)
