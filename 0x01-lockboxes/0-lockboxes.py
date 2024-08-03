#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each list contains
        keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set([0])  # Start with the first box open
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in opened and key < n:
                opened.add(key)
                keys.append(key)

    return len(opened) == n
