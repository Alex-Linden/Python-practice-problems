def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    out = []

    for el in lst:
        if el:
            out.append(el)

    return out

    # with list comprehension
    # return [val for val in lst if val]