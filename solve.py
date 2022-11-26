import pandas
from itertools import permutations

DICTFILE = 'words_dictionary.json'

def solve(df, choices, problem):
    choices = list(choices.strip().lower())
    problem = list(problem.strip().lower())

    for letter in problem:
        if letter == '_':
            continue

        choices.remove(letter)

    possibilities = list(permutations(choices, len(choices)))

    possible_sols = []
    for possibility in possibilities:
        new_word = []
        j = 0
        for i in range(len(problem)):
            if problem[i] == '_':
                new_word.append(possibility[j])
                j += 1
            else:
                new_word.append(problem[i])

        new_word = ''.join(new_word)
        if df['words'].get(new_word) is None:
            continue

        possible_sols.append(new_word)

    return list(set(possible_sols))

if __name__ == '__main__':
    print('Loading in words dictionary; this may take a while...')
    df = pandas.read_json(DICTFILE)
    print('Done loading words dictionary.')

    while True:
        choices = input('what are the letters you have in your wheel? just enter lower case without any spaces or commas (i.e. abcd): ')
        problem = input('what are letters so far for the word you are solving? for blanks, give _ (i.e. a_p_e could be apple): ')

        print('Great. Attempting to solve now...')

        possible_sols = solve(df, choices, problem)

        for sol in possible_sols:
            print('Possible solution: ', sol)
        print()

