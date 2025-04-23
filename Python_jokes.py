import pyjokes
from jinja2.nodes import Literal

joke = pyjokes.get_joke('en',  'neutral')

print(joke)