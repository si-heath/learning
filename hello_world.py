"""This is a docstring summary to shut pylint up

Usage hello_world
More details at: https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
"""
import sys
import requests

print(sys.version)
print(sys.executable)
print("Hello World")

# YT Tutorial https://www.youtube.com/watch?v=-nh9rCzPJ20
r = requests.get('https://thevrhub.co.uk')
print(r.status_code)

print("hello")
