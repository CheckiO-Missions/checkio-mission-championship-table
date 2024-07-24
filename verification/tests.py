"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(10, 20, 6, 2, -1)],
            "answer": (10, 20, 6, 2, 2),
        },
        {
            "input": [(-1, 64, 18, 10, 10)],
            "answer": (38, 64, 18, 10, 10),
        },
        {
            "input": [(-1, 47, 14, -1, 9)],
            "answer": (28, 47, 14, 5, 9),
        },
    ],
    "Extra": [
        {
            "input": [(-1, -1, 0, 0, 0)],
            "answer": (0, 0, 0, 0, 0),
        },
        {
            "input": [(-1, 50, -1, 2, 4)],
            "answer": (22, 50, 16, 2, 4),
        },
        {
            "input": [(38, -1, 18, 10, 10)],
            "answer": (38, 64, 18, 10, 10),
        },
        {
            "input": [(38, 64, -1, 10, 10)],
            "answer": (38, 64, 18, 10, 10),
        },
        {
            "input": [(38, 64, 18, -1, 10)],
            "answer": (38, 64, 18, 10, 10),
        },
        {
            "input": [(28, -1, -1, 5, 9)],
            "answer": (28, 47, 14, 5, 9),
        },
        {
            "input": [(28, -1, 14, -1, 9)],
            "answer": (28, 47, 14, 5, 9),
        },
        {
            "input": [(28, -1, 14, 5,-1)],
            "answer": (28, 47, 14, 5, 9),
        },
        {
            "input": [(10, 20, -1, 2, -1)],
            "answer": (10, 20, 6, 2, 2),
        },
        {
            "input": [(10, 20, 6, -1, -1)],
            "answer": (10, 20, 6, 2, 2),
        },
        {
            "input": [(10, 20, -1, -1, 2)],
            "answer": (10, 20, 6, 2, 2),
        },
    ]
}
