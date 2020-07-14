"""
.. module:: exchange.off
    :platform: Unix, Windows
    :synopsis: Provides exchange capabilities for OFF file format

.. moduleauthor:: Onur R. Bingol <contact@onurbingol.net>

"""

from ..tessellate import triangular
from ..base import export, GeomdlError
from . import exc_helpers


@export
def export_off_str(surface, **kwargs):
    """ Exports surface(s) in OFF format as a string.

    :param surface: input surface(s)
    :type surface: BSpline.Surface
    :return: contents of the .off file generated
    :rtype: str
    """
    # Input validity checking
    if surface.pdimension != 2:
        raise GeomdlError("Can only export surfaces")

    # Count the vertices to update the face numbers correctly
    vertex_offset = 0

    # Initialize lists for vertices, vertex normals and faces
    str_v = []
    str_f = []

    for srf in surface:
        # Tessellate surface
        vertices, faces = triangular.make_triangle_mesh(srf.evalpts, srf.sample_size[0], srf.sample_size[1])

        # Collect vertices
        for vert in vertices:
            line = str(vert.x) + " " + str(vert.y) + " " + str(vert.z) + "\n"
            str_v.append(line)

        # Collect faces (zero-indexed)
        for t in faces:
            vl = t.data
            line = "3 " + \
                   str(vl[0] + vertex_offset) + " " + \
                   str(vl[1] + vertex_offset) + " " + \
                   str(vl[2] + vertex_offset) + "\n"
            str_f.append(line)

        # Update vertex offset
        vertex_offset = len(str_v)

    # Write file header
    line = "OFF\n"
    line += str(len(str_v)) + " " + str(len(str_f)) + " 0\n"

    # Write all collected data to the file
    for lv in str_v:
        line += lv
    for lf in str_f:
        line += lf

    return line


@export
def export_off(surface, file_name, **kwargs):
    """ Exports surface(s) as a .off file.

    :param surface: input surface(s)
    :type surface: BSpline.Surface
    :param file_name: name of the output file
    :type file_name: str
    :raises GeomdlException: an error occurred writing the file
    """
    content = export_off_str(surface, **kwargs)
    return exc_helpers.write_file(file_name, content)
