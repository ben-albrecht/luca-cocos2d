#!/bin/sh
# Requires ImageMagick cl tool 'convert'
# TODO: Make this more robust (more of a reference than a script now)

convert -delay 20 -loop 0 *png animated.gif
