from pywebio.input import TEXT, input
from pywebio.output import put_text
from pywebio.platform.tornado import start_server

def main():
    activity = input('Activity to do', type=TEXT)
    put_text("Today, we'll be doing ", activity)

start_server(main, port=8080, debug=True)