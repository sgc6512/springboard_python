def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # copy = []
    # for elem in lst:
    #     if elem:
    #         copy.append(elem)
    # return copy
    return [elem for elem in lst if elem]
