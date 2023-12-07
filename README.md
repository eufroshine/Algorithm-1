# Algorithm-1

## Empty Set Creation and Type Printing

    s = set()
    print("Type of s is ", type(s))

An empty set s is created.

The type of s is printed.

## List to Set Conversion

    lis1 = [3, 4, 1, 4, 5]
    print("The list before conversion is: " + str(lis1))
    set_from_list = set(lis1)
    print("The list after conversion is: " + str(set_from_list))

A list lis1 is declared.

The original list is printed.

The list is converted to a set, and the result is printed.

## Tuple to Set Conversion

    tup1 = (3, 4, 1, 4, 5)
    print("The tuple before conversion is: " + str(tup1))
    set_from_tuple = set(tup1)
    print("The tuple after conversion is: " + str(set_from_tuple))

A tuple tup1 is declared.

The original tuple is printed.

The tuple is converted to a set, and the result is printed.

## Range to Set Conversion:

    r = range(5)
    set_from_range = set(r)
    print("The Range after conversion is: " + str(set_from_range))
A range object r is declared.

The range is converted to a set, and the result is printed.

## Dictionary Keys to Set Conversion

    dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}
    print("Dictionary before conversion is: " + str(dic1))
    set_from_dict = set(dic1.keys())
    print("Dictionary keys after conversion is: " + str(set_from_dict))

A dictionary dic1 is declared.

The original dictionary is printed.

The keys of the dictionary are converted to a set, and the result is printed.

## Removing Elements from a Set using pop()

    def Remove(initial_set):
        while initial_set:
            initial_set.pop()
        print("Set after popping elements:", initial_set)

    initial_set = set([12, 10, 13, 15, 8, 9])
    Remove(initial_set)

A set initial_set is declared with some initial elements.

The Remove function is called, which repeatedly pops elements from the set until it's empty, and then prints the set.

===========================================

    s1 = {1, 2, 3, 4}
    print("Before popping: ", s1)
    s1.pop()
    s1.pop()
    s1.pop()
    print("After 3 elements popped, s1:", s1)

    s1 = {9, 1, 0}
    popped_element = s1.pop()
    print("Popped element:", popped_element)
    print("Set after popping one element:", s1)

    A = {4, 1, 3, 5}
    B = {6, 0, 4, 1, 5, 0, 3, 5}
    print("A is subset of B:", A.issubset(B))
    print("B is subset of A:", B.issubset(A))

    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5}
    print("s2 is subset of s1:", s2.issubset(s1))

Various set operations are demonstrated, including popping elements, adding elements, and checking whether one set is a subset of another.