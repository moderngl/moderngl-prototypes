from typing import Any


class Attribute:
    """This class represents a program attribute."""

    def __init__(self):
        self._location: int = None
        self._array_length: int = None
        self._dimension: int = None
        self._shape: int = None
        self._name: str = None
        self.extra: Any = None  #: Attribute for storing user defined objects

    def __repr__(self) -> str:
        return '<Attribute: %d>' % self._location

    @property
    def mglo(self):
        return self

    @property
    def location(self) -> int:
        """
        int: The location of the attribute.

        The result of the glGetAttribLocation.
        """
        return self._location

    @property
    def array_length(self) -> int:
        """
        int: If the attribute is an array the array_length.

        is the length of the array otherwise `1`.
        """
        return self._array_length

    @property
    def dimension(self) -> int:
        """
        int: The attribute dimension.

        +-----------+-----------+
        | GLSL type | dimension |
        +===========+===========+
        | int       | 1         |
        +-----------+-----------+
        | ivec2     | 2         |
        +-----------+-----------+
        | ivec3     | 3         |
        +-----------+-----------+
        | ivec4     | 4         |
        +-----------+-----------+
        | uint      | 1         |
        +-----------+-----------+
        | uvec2     | 2         |
        +-----------+-----------+
        | uvec3     | 3         |
        +-----------+-----------+
        | uvec4     | 4         |
        +-----------+-----------+
        | float     | 1         |
        +-----------+-----------+
        | vec2      | 2         |
        +-----------+-----------+
        | vec3      | 3         |
        +-----------+-----------+
        | vec4      | 4         |
        +-----------+-----------+
        | double    | 1         |
        +-----------+-----------+
        | dvec2     | 2         |
        +-----------+-----------+
        | dvec3     | 3         |
        +-----------+-----------+
        | dvec4     | 4         |
        +-----------+-----------+
        | mat2      | 4         |
        +-----------+-----------+
        | mat2x3    | 6         |
        +-----------+-----------+
        | mat2x4    | 8         |
        +-----------+-----------+
        | mat3x2    | 6         |
        +-----------+-----------+
        | mat3      | 9         |
        +-----------+-----------+
        | mat3x4    | 12        |
        +-----------+-----------+
        | mat4x2    | 8         |
        +-----------+-----------+
        | mat4x3    | 12        |
        +-----------+-----------+
        | mat4      | 16        |
        +-----------+-----------+
        | dmat2     | 4         |
        +-----------+-----------+
        | dmat2x3   | 6         |
        +-----------+-----------+
        | dmat2x4   | 8         |
        +-----------+-----------+
        | dmat3x2   | 6         |
        +-----------+-----------+
        | dmat3     | 9         |
        +-----------+-----------+
        | dmat3x4   | 12        |
        +-----------+-----------+
        | dmat4x2   | 8         |
        +-----------+-----------+
        | dmat4x3   | 12        |
        +-----------+-----------+
        | dmat4     | 16        |
        +-----------+-----------+
        """
        return self._dimension

    @property
    def shape(self) -> str:
        """
        str: The shape is a single character, representing the scalar type of the attribute.

        +---------+--------------------------+
        | shape   | GLSL types               |
        +=========+==========================+
        | ``'i'`` | int                      |
        |         +--------------------------+
        |         | ivec2 ivec3 ivec4        |
        +---------+--------------------------+
        | ``'I'`` | uint                     |
        |         +--------------------------+
        |         | uvec2 uvec3 uvec4        |
        +---------+--------------------------+
        | ``'f'`` | float                    |
        |         +--------------------------+
        |         | vec2 vec3 vec4           |
        |         +--------------------------+
        |         | mat2 mat3 mat4           |
        |         +--------------------------+
        |         | mat2x3 mat2x4 mat3x4     |
        |         | mat4x2 mat4x2 mat4x3     |
        +---------+--------------------------+
        | ``'d'`` | double                   |
        |         +--------------------------+
        |         | dvec2 dvec3 dvec4        |
        |         +--------------------------+
        |         | dmat2 dmat3 dmat4        |
        |         +--------------------------+
        |         | dmat2x3 dmat2x4 dmat3x4  |
        |         | dmat4x2 dmat4x2 dmat4x3  |
        +---------+--------------------------+
        """
        return self._shape

    @property
    def name(self) -> str:
        """
        str: The attribute name.

        The name will be filtered to have no array syntax on it's end.
        Attribute name without ``'[0]'`` ending if any.
        """
        return self._name


class UniformBlock:
    """Uniform Block metadata."""

    def __init__(self):
        self._program_obj = None
        self._index = None
        self._size = None
        self._name = None
        self._ctx = None
        self.extra = None  #: Any - Attribute for storing user defined objects

    def __repr__(self):
        return '<UniformBlock: %d>' % self._index

    @property
    def mglo(self):
        return self

    @property
    def binding(self) -> int:
        """int: The binding of the uniform block."""
        return self._ctx._get_ubo_binding(self._program_obj, self._index)

    @binding.setter
    def binding(self, binding: int) -> None:
        self._ctx._set_ubo_binding(self._program_obj, self._index, binding)

    @property
    def value(self) -> int:
        """int: The value of the uniform block."""
        return self._ctx._get_ubo_binding(self._program_obj, self._index)

    @value.setter
    def value(self, value: int) -> None:
        self._ctx._set_ubo_binding(self._program_obj, self._index, value)

    @property
    def name(self) -> str:
        """str: The name of the uniform block."""
        return self._name

    @property
    def index(self) -> int:
        """int: The index of the uniform block."""
        return self._index

    @property
    def size(self) -> int:
        """int: The size of the uniform block."""
        return self._size


class Error(Exception):
    """Generic moderngl error."""
    pass


ATTRIBUTE_LOOKUP_TABLE = {
    0x1404: (1, 0x1404, 1, 1, False, 'i'),
    0x8b53: (2, 0x1404, 1, 2, False, 'i'),
    0x8b54: (3, 0x1404, 1, 3, False, 'i'),
    0x8b55: (4, 0x1404, 1, 4, False, 'i'),
    0x1405: (1, 0x1405, 1, 1, False, 'i'),
    0x8dc6: (2, 0x1405, 1, 2, False, 'i'),
    0x8dc7: (3, 0x1405, 1, 3, False, 'i'),
    0x8dc8: (4, 0x1405, 1, 4, False, 'i'),
    0x1406: (1, 0x1406, 1, 1, True, 'f'),
    0x8b50: (2, 0x1406, 1, 2, True, 'f'),
    0x8b51: (3, 0x1406, 1, 3, True, 'f'),
    0x8b52: (4, 0x1406, 1, 4, True, 'f'),
    0x140a: (1, 0x140a, 1, 1, False, 'd'),
    0x8ffc: (2, 0x140a, 1, 2, False, 'd'),
    0x8ffd: (3, 0x140a, 1, 3, False, 'd'),
    0x8ffe: (4, 0x140a, 1, 4, False, 'd'),
    0x8b5a: (4, 0x1406, 2, 2, True, 'f'),
    0x8b65: (6, 0x1406, 2, 3, True, 'f'),
    0x8b66: (8, 0x1406, 2, 4, True, 'f'),
    0x8b67: (6, 0x1406, 3, 2, True, 'f'),
    0x8b5b: (9, 0x1406, 3, 3, True, 'f'),
    0x8b68: (12, 0x1406, 3, 4, True, 'f'),
    0x8b69: (8, 0x1406, 4, 2, True, 'f'),
    0x8b6a: (12, 0x1406, 4, 3, True, 'f'),
    0x8b5c: (16, 0x1406, 4, 4, True, 'f'),
    0x8f46: (4, 0x140a, 2, 2, False, 'd'),
    0x8f49: (6, 0x140a, 2, 3, False, 'd'),
    0x8f4a: (8, 0x140a, 2, 4, False, 'd'),
    0x8f4b: (6, 0x140a, 3, 2, False, 'd'),
    0x8f47: (9, 0x140a, 3, 3, False, 'd'),
    0x8f4c: (12, 0x140a, 3, 4, False, 'd'),
    0x8f4d: (8, 0x140a, 4, 2, False, 'd'),
    0x8f4e: (12, 0x140a, 4, 3, False, 'd'),
    0x8f48: (16, 0x140a, 4, 4, False, 'd'),
}


def make_attribute(name, gl_type, program_obj, location, array_length):
    tmp = ATTRIBUTE_LOOKUP_TABLE.get(gl_type, (1, 0, 1, 1, False, '?'))
    dimension, scalar_type, rows_length, row_length, normalizable, shape = tmp
    row_length *= array_length
    res = Attribute()
    res._type = gl_type
    res._program_obj = program_obj
    res._scalar_type = scalar_type
    res._rows_length = rows_length
    res._row_length = row_length
    res._normalizable = normalizable
    res._location = location
    res._array_length = array_length
    res._dimension = dimension
    res._shape = shape
    res._name = name
    return res


def make_uniform_block(name, program_obj, index, size, ctx):
    res = UniformBlock()
    res._name = name
    res._program_obj = program_obj
    res._index = index
    res._size = size
    res._ctx = ctx
    return res
