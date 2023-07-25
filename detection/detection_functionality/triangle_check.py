from detection.triangle import Triangle

from scipy import stats
import numpy as np

import math

def get_triangle(df, max_length):
    xmins = df.index[(df["high_low"] == -1) | (df["high_low"] == 3)].to_list()
    ymins = df.iloc[xmins]["low"].to_list()

    xmaxes = df.index[(df["high_low"] == 1) | (df["high_low"] == 3)].to_list()
    ymaxes = df.iloc[xmaxes]["high"].to_list()

    triangle = None

    if check_sufficient_points(xmins, xmaxes):
        triangle = find_triangle(xmins, ymins, xmaxes, ymaxes, max_length)

    return triangle


# checks if there are atleast 5 points and at least 2 for highs and lows
def check_sufficient_points(xmins, xmaxes):
    return (len(xmins) + len(xmaxes) >= 5) and len(xmins) >= 2 and len(xmaxes) >= 2


def find_triangle(xmins, ymins, xmaxes, ymaxes, max_length):
    slopeMin, intersectMin, rvalueMin, pvalueMin, stderrMin = stats.linregress(
        xmins, ymins
    )
    slopeMax, intersectMax, rvalueMax, pvalueMax, stderrMax = stats.linregress(
        xmaxes, ymaxes
    )

    is_valid_triangle_shape = False

    # if there is a strong correlation
    if (
        (abs(rvalueMax) > 0.9 and abs(rvalueMin) > 0.9)
        or (slopeMax == 0 and abs(rvalueMin) > 0.9)
        or (slopeMin == 0 and abs(rvalueMax) > 0.9)
    ):
        if abs(slopeMax) <= 0.005 and slopeMin > 0:  # ascending triangle
            is_valid_triangle_shape = True
        elif abs(slopeMin) <= 0.005 and slopeMax < 0:  # descending triangle
            is_valid_triangle_shape = True
        elif (
            slopeMax < 0
            and slopeMin > 0
            and min(abs(slopeMax), slopeMin) / max(abs(slopeMax), slopeMin) >= 0.5
        ):  # symmetrical triangle
            is_valid_triangle_shape = True

    # if shape is not valid or slopes are parallel
    if not is_valid_triangle_shape or slopeMax == slopeMin:
        return None

    start_x = min(xmins[0], xmaxes[0])
    end_cross_x = math.floor(
        (intersectMin - intersectMax) / (slopeMax - slopeMin)
    )  # point where two lines meet

    # if triangle is longer than max length
    if end_cross_x - start_x + 1 > max_length:
        return None

    xs = np.array([start_x, end_cross_x])
    ysMin = xs * slopeMin + intersectMin
    ysMax = xs * slopeMax + intersectMax

    triangle = Triangle(start_x, end_cross_x, ysMax[0], ysMin[0], ysMax[1], ysMin[1])

    return triangle
