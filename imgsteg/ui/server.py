from bottle import request, response, route, run, static_file, template, TEMPLATE_PATH
import os
import io

from ..imgsteg import Imgsteg

base = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH.insert(0, os.path.join(base, "views/"))
file = None


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.join(base, 'static/'))


@route("/")
def index():
    return template('index')


@route("/api/<command>", method="POST")
def inversion(command):
    im = Imgsteg(file)

    # print(command)
    new_im = None

    if command == "original":
        new_im = im.im
    elif command == "inversion":
        new_im = im.invert()
    elif command == "graybits":
        new_im = im.gray_bits()
    elif command.startswith("alpha") or command.startswith("red") \
         or command.startswith("green") or command.startswith("blue"):
        name, type = command.split("-")
        channel_map = {
            "red": 0,
            "green": 1,
            "blue": 2,
            "alpha": 3,
        }
        if type == "full":
            new_im = im.extract_channel_plane(channel_map[name])
        else:
            new_im = im.extract_bit_plane(channel_map[name], int(type))
    elif command.startswith("random"):
        new_im = im.randomize_colormap()

    if not new_im:
        raise Exception()

    blob = io.BytesIO()
    new_im.save(blob, format="png", quality=100)
    # response.set_header("Content-Type", "image/png")
    blob.seek(0)

    return blob.read()


def serve(f):
    global file
    file = f
    run(host='localhost', port=8080)  # , debug=True)
