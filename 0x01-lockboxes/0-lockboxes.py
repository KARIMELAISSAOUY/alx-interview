#!/usr/bin/python3
"""
Solution to lockboxes (Problem).
"""


def canUnlockAll(boxes):
    """
    Determines the Feasibility of Opening a Series,
    of Locked Boxes Using Attainable Keys:
    A Solution to the Lockbox Problem.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
