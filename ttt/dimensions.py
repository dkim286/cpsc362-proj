'''
Provides any coordinate tuples or rectangle definitions to be used by the game.

All definitions are compatible with PyGame's coordinate and rectangle tuples:
- coordinates: (x, y)
- rectangles: (x_offset, y_offset, width, height)

The coordinates naming is tricky. We can either use all letters:

+----+----+----+
| aa | ab | ac |
| -- | -- | -- |
| ba | bb | bc |
| -- | -- | -- |
| ca | cb | cc |
+----+----+----+

or we can prepend a letter to the variable name:


+-----+-----+-----+
| t11 | t12 | t13 |
| --- | --- | --- |
| t21 | t22 | t23 |
| --- | --- | --- |
| t31 | t32 | t33 |
+-----+-----+-----+
'''

# we need to pick one of the two:
# AA = (0, 0)
# T11 = (0, 0)
