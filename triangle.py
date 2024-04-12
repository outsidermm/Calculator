# coding: utf-8

"""
This Python script contains a set of functions to visualize and annotate a triangle based on given angles. The script uses the `matplotlib` library to plot and label the triangle's sides and angles. Below is a description of each function included in the script:

1. `draw_triangle` Function:
This function draws a triangle on a plot based on the provided three angles. It first converts the angles to radians and then calculates the coordinates of the third point. It uses the `matplotlib` library to draw the sides of the triangle and annotate the angles.

2. `draw_line` Function:
This auxiliary function is used to draw a straight line on a plot. It takes the coordinates of two points as parameters and draws a line between these two points on the current plot.

3. `annotate_angles` Function:
This function annotates the angles of a triangle at each vertex on a plot. It uses the `Arc` object from the `matplotlib` library to draw arcs for the angle annotations and adds text labels next to the arcs to display the size of the angles.

4. `annotate_lengths` Function:
This function annotates the relative lengths of the sides of a triangle on a plot. It calculates and labels the lengths of each side of the triangle and displays this information on the plot.

The main program, indicated by the `if __name__ == "__main__":` block, is where the actual drawing of a triangle is invoked by calling the `draw_triangle` function.

The script provides a visual representation of a triangle, including annotations for side lengths and angles, using the `matplotlib` library. The comments and documentation help to understand the functionality and implementation details of the code.
"""

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from typing import Tuple

# Assuming utility module exists and contains the midpoint function
import utilities


def draw_triangle(angle1: float, angle2: float, angle3: float) -> None:
    """
    Draw a triangle on relative scale based on the given three angles.

    Args:
        angle1 (float): Angle 1 of the triangle.
        angle2 (float): Angle 2 of the triangle.
        angle3 (float): Angle 3 of the triangle.

    Returns:
        None: Exports a PNG with the drawn triangle.
    """
    # Rad conversion for MatPlotLib utilisation
    angle1_rad = math.radians(angle1)
    angle2_rad = math.radians(angle2)

    # Calculate third point based on the given angles, assume pt1 (0,0) and
    # pt2 (1,0) for relative scaling
    x3 = math.tan(angle2_rad) / (math.tan(angle2_rad) + math.tan(angle1_rad))
    y3 = math.tan(angle1_rad) * x3

    pt1 = (0.0, 0.0)
    pt2 = (1.0, 0.0)
    pt3 = (x3, y3)

    # Common MatplotLib Setting
    plt.cla()
    plt.axis("equal")
    plt.rc("lines", linestyle="solid", marker="o")
    plt.rcParams["font.size"] = 12

    # Plot three sides of the triangle
    draw_line(pt1, pt2)
    draw_line(pt2, pt3)
    draw_line(pt1, pt3)

    annotate_angles(pt1, pt2, pt3, angle1, angle2, angle3, 0.25)
    annotate_lengths(pt1, pt2, pt3, angle1, angle2)
    # Export plot to PNG
    plt.savefig("triangle.png")
    print(
        f"Relative side length: 1, {round(math.dist(pt2,pt3),2)}, {round(math.dist(pt1,pt3),2)}"
    )


def draw_line(pt1: Tuple[float, float], pt2: Tuple[float, float]) -> None:
    """
    Draw a linear line from point pt1 to point pt2 on a plot.

    Parameters:
    pt1 (Tuple[float, float]): The start point of the line, in the format (x1, y1).
    pt2 (Tuple[float, float]): The end point of the line, in the format (x2, y2).

    Returns:
    None: The line is drawn on the current plot.
    """
    plt.plot(
        [pt1[0], pt2[0]],
        [pt1[1], pt2[1]],
    )


def annotate_angles(
    pt1: Tuple[float, float],
    pt2: Tuple[float, float],
    pt3: Tuple[float, float],
    angle1: float,
    angle2: float,
    angle3: float,
    arc_radius: float,
) -> None:
    """
    Annotate the angles of a triangle on a plot.

    Args:
    pt1, pt2, pt3: Tuple[float, float]: The coordinates of the triangle's vertices.
    angle1, angle2, angle3: float: The angles of the triangle at each vertex.
    arc_radius: float: The radius of the arc used for the angle annotations.

    Returns:
    None: The angles are annotated on the current plot.
    """

    # Add angle arc for the angles
    plt.gca().add_patch(
        Arc(pt1, arc_radius, arc_radius, angle=0, theta1=0, theta2=angle1)
    )
    plt.gca().add_patch(
        Arc(pt2, arc_radius, arc_radius, angle=0, theta1=180 - angle2, theta2=180)
    )
    plt.gca().add_patch(
        Arc(pt3, arc_radius, arc_radius, angle=180 + angle1, theta1=0, theta2=angle3)
    )

    # Annotate angle size on the angles
    angle1_rad = math.radians(angle1)
    angle2_rad = math.radians(angle2)

    label_angle1 = angle1_rad / 2
    label1_x = pt1[0] + arc_radius * math.cos(label_angle1)
    label1_y = pt1[1] + arc_radius * math.sin(label_angle1)
    plt.gca().text(
        label1_x,
        label1_y,
        f"{angle1}°",
        horizontalalignment="center",
        rotation=label_angle1,
        rotation_mode="anchor",
        transform=plt.gca().transData,
    )

    label_angle2 = angle2_rad / 2
    label2_x = pt2[0] - arc_radius * math.cos(label_angle2)
    label2_y = pt2[1] + arc_radius * math.sin(label_angle2)
    plt.gca().text(
        label2_x,
        label2_y,
        f"{angle2}°",
        horizontalalignment="center",
        rotation=label_angle2,
        rotation_mode="anchor",
        transform=plt.gca().transData,
    )

    label_angle3 = ((math.pi + angle1_rad) + (math.tau - angle2_rad)) / 2
    label3_x = pt3[0] + arc_radius * math.cos(label_angle3)
    label3_y = pt3[1] + arc_radius * math.sin(label_angle3)
    plt.gca().text(
        label3_x,
        label3_y,
        f"{angle3}°",
        horizontalalignment="center",
        rotation=label_angle3,
        rotation_mode="anchor",
        transform=plt.gca().transData,
    )


def annotate_lengths(
    pt1: Tuple[float, float],
    pt2: Tuple[float, float],
    pt3: Tuple[float, float],
    angle1: float,
    angle2: float,
) -> None:
    """
    Annotate the relative lengths of the sides of a triangle on a plot.

    Args:
    pt1, pt2, pt3: Tuple[float, float]: The coordinates of the triangle's vertices.
    angle1, angle2: float: Two of the angles of the triangle (third angle is calculated).

    Returns:
    None: The side lengths are annotated on the current plot.
    """
    midpoint12 = utilities.midpoint(pt1, pt2)
    midpoint23 = utilities.midpoint(pt2, pt3)
    midpoint13 = utilities.midpoint(pt1, pt3)

    plt.gca().text(midpoint12[0], midpoint12[1], "1", horizontalalignment="center")

    plt.gca().text(
        midpoint13[0],
        midpoint13[1],
        f"{round(math.dist(pt1, pt3), 2)}",
        horizontalalignment="center",
        rotation=angle1,
    )

    plt.gca().text(
        midpoint23[0],
        midpoint23[1],
        f"{round(math.dist(pt2, pt3), 2)}",
        horizontalalignment="center",
        rotation=360 - angle2,
    )


# The main program would be executed here, for example:
if __name__ == "__main__":
    # Example usage: draw a triangle with angles 30, 60, and 90 degrees
    draw_triangle(30, 60, 90)
