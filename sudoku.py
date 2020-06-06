from hashset import HashSet


def read_matrix(file_name):
    """
    Read a sudoku grid from a text file and returns a solvable matrix.

    :param str file_name: file storing the sudoku grid
    :return list[list[HashSet]]: 2D matrix of sudoku cells
    """
    matrix = []
    with open(file_name) as f:
        for row in f:
            line = []
            for cell in row.strip():
                if cell.lower() == "x":
                    line.append(HashSet(list(range(1, 10))))
                else:
                    line.append(HashSet([int(cell)]))
            matrix.append(line)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for i, cell in enumerate(row):
            print(repr(cell).strip("{}").replace(" ", ""), end="")
            if i == 8:
                print("")


def reduce(matrix):
    """
    At the moment, this can only solve very easy sudokus.

    :param list[list[HashSet]] matrix: 2D matrix representing sudoku cells
    """
    changed = True
    groups = get_groups(matrix)
    while changed:
        changed = reduce_groups(groups)


def get_groups(matrix):
    """
    Generate groups of cells for solving sudoku.

    :param list[list[HashSet]] matrix: 2D matrix representing sudoku cells
    :return list[list[HashSet]]: groups of cells for solving sudoku
    """
    groups = []

    # rows are groups 0 to 8
    for row in matrix:
        groups.append(row)

    # columns are groups 9 to 17
    for i in range(9):
        column = []
        for row in matrix:
            column.append(row[i])
        groups.append(column)

    # squares are groups 18 to 26
    for a in (0, 3, 6):
        for b in (0, 3, 6):
            square = []
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    square.append(matrix[i][j])
            groups.append(square)

    return groups


def reduce_groups(groups):
    """
    Reduce groups of sets according to rules 1 and 2 of sudoku solving.

    :param list[HashSet] groups: groups to reduce
    :return bool: True if groupes were reduced at least partially, else False
    """
    changed = False
    for group in groups:
        changed |= rule_1(group)
        changed |= rule_2(group)
    return changed


def rule_1(group):
    """
    Reduce a group using rule #1: if a set of the group has a cardinality
    of 1, the value of this set can be removed from other sets in the group.

    :param list[HashSets] group: group of sets
    :return bool: True if the group was changed, else False
    """
    changed = False
    for _set in group:
        for single in sets_with_one_element(group):
            if len(_set) > 1 and len(_set.intersection(single)) > 0:
                _set.difference_update(single)
                changed = True
    return changed


def rule_2(group):
    """
    Reduce a group using rule #2: if an element from a set is absent from all
    other sets of the group, this element can be made the only element of this
    set.

    :param list[HashSets] group: group of sets
    :return bool: True if the group was changed, else False
    """
    changed = False
    for i in range(len(group)):
        if len(group[i]) > 1:
            copy = HashSet(group[i])
            for j in range(len(group)):
                if i != j:
                    copy.difference_update(group[j])
            if len(copy) == 1:
                group[i] = copy
                changed = True
    return changed


def sets_with_one_element(group):
    """
    Return sets within the group with cardinality = 1.

    :param list[HashSet] group: list of sets
    :return list[HashSet]: sets with a single element
    """
    return [i for i in group if len(i) == 1]
