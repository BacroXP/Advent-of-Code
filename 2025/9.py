import shapely
import libs.input

sol1, sol2 = 0, 0
points = [[int(x) for x in line.split(',')] for line in libs.input.file()]
polygon = shapely.Polygon(points)
shapely.prepare(polygon)

for p1 in points:
    for p2 in points:
        rect = shapely.Polygon([p1, (p1[0], p2[1]), p2, (p2[0], p1[1])])
        area = abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)

        if area > sol1:
            sol1 = area

        if polygon.contains(rect) and area > sol2:
            sol2 = area

print(sol1)
print(sol2)