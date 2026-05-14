import math

import glm


def assert_close(actual, expected):
    assert math.isclose(actual, expected, rel_tol=1e-7, abs_tol=1e-7), (
        actual,
        expected,
    )


vector = glm.vec3(1.0, 2.0, 2.0)
assert_close(glm.length(vector), 3.0)

translation = glm.translate(glm.mat4(1.0), glm.vec3(4.0, 5.0, 6.0))
point = translation * glm.vec4(vector, 1.0)
assert tuple(point) == (5.0, 7.0, 8.0, 1.0)

rotation = glm.angleAxis(glm.radians(90.0), glm.vec3(0.0, 0.0, 1.0))
rotated = rotation * glm.vec3(1.0, 0.0, 0.0)
assert_close(rotated.x, 0.0)
assert_close(rotated.y, 1.0)
assert_close(rotated.z, 0.0)
