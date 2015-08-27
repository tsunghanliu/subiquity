# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Palette Loader """


def apply_default_colors(cls):
    color_map = {'dark_magenta': 'dark magenta',
                 'light_magenta': 'light magenta',
                 'light_green': 'light green',
                 'dark_green': 'dark green',
                 'white': 'white',
                 'black': 'black',
                 'light_gray': 'light gray',
                 'dark_gray': 'dark gray',
                 'dark_red': 'dark red',
                 'light_red': 'light red'}
    for k, v in color_map.items():
        setattr(cls, k, v)
    return cls


@apply_default_colors
class Palette:
    pass

STYLES = [
    ('frame_header', '', '', '',
     Palette.white, ''),
    ('frame_footer', '', '', '',
     Palette.white, ''),
    ('body', '', '', '',
     Palette.white, ''),
    ('menu_button', '', '',
     '', Palette.white, ''),
    ('menu_button focus', '', '', '',
     Palette.black, Palette.light_gray),
    ('button', '', '',
     '', Palette.white, ''),
    ('button focus', '', '', '',
     Palette.black, Palette.dark_green),
    ('info_minor', '', '', '',
     Palette.dark_gray, ''),
    ('string_input', '', '', '',
     Palette.black, Palette.light_gray),
    ('string_input focus', '', '', '',
     Palette.white, Palette.dark_gray)
]


STYLES_MONO = [('frame_header', Palette.white, Palette.black,
                '', '', ''),
               ('frame_footer', Palette.white, Palette.black,
                '', '', ''),
               ('body', Palette.white, Palette.black,
                '', '', ''),
               ('info_minor', Palette.white, Palette.black,
                '', '', ''),
               ('menu_button', '', '',
                '', Palette.white, ''),
               ('menu_button focus', '', '', '',
                Palette.white, ''),
               ('button', Palette.white, Palette.black,
                '', '', ''),
               ('button focus', Palette.white, Palette.black,
                '', '', '')]
