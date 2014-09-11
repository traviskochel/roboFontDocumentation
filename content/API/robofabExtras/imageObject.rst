Image Object
============

.. class:: Image

    .. function:: transform(tranformation)

        image.Transform the image with a transform matrix (xy, yy, xx, yx, x, y)

    .. function:: move((x, y))

        Move the image with a given x, y

    .. function:: translate((x, y))

        Translate the image with a given x, y

    .. function:: skew(angle, offset=None)

        Skew the image with a given angle, optionally with an offset (x, y)

    .. function:: rotate(angle, offset=None)

        Rotate the image with a given angle, optionally with an offset (x, y)

    .. function:: scale((x, y), center=(0, 0))

        Scale the image with a given x, y, optionally with a center coordinate

    .. attribute:: path

        path to the image

    .. attribute:: bounds

        image bounding box

    .. attribute:: brightness

        set brightness of the image (float)

    .. attribute:: contrast

        set contrast of the image (float)

    .. attribute:: saturation

        set saturation of the image (float)

    .. attribute:: sharpness

        set sharpness of the image (float)

    .. attribute:: blackAndWhite

        convert image to black and white (bool)

    .. attribute:: selected
