import math, re

from django.template import Library, Node, TemplateSyntaxError, VariableDoesNotExist, resolve_variable
from django.conf import settings

register = Library()


class ShowPluginsNode(Node):
	""" Default rounding is to the whole unit """
	def __init__(self, stars, total_stars, round_to, handler=None, identifier=None):
		self.stars = stars
		self.total_stars = int(total_stars)
		self.rounder = ROUNDERS[round_to.lower()]
		self.handler = handler
		self.identifier = identifier

	def merge_star(self, pos, fraction, identifier):
		alt, src = STARS[fraction]
		if self.handler:
			pos += 1
			return EX_IMG_TEMPLATE % (identifier, pos, identifier, self.handler, identifier, pos, FULL_FOLDER + src, alt)
		else:
			return IMG_TEMPLATE % (FULL_FOLDER + src, alt)

	def render(self, context):
		try:
			stars = resolve_variable(self.stars, context)
		except VariableDoesNotExist:
			try:
				stars = float(self.stars)
			except:
				return ""
		try:
			identifier = resolve_variable(self.identifier, context)
		except VariableDoesNotExist:
			identifier = self.identifier

		stars = round(stars * self.rounder) / self.rounder

		fraction, integer = math.modf(stars)
		output = []

		if self.handler:
			output.append(DIV_TEMPLATE % identifier)
		for i in range(self.total_stars):
			if i < integer:
				output.append(self.merge_star(i, 1.0, identifier))
			elif i == integer and fraction:
				output.append(self.merge_star(i, fraction, identifier))
			else:
				output.append(self.merge_star(i, 0.0, identifier))
		if self.handler:
			output.append(END_DIV_TEMPLATE)

		return "".join(output)

class ShowStarsScriptNode(Node):
	def render(self, context):
		return JS_TEMPLATE


def last_plugins(parser, token):
	def syntax_error():
		raise TemplateSyntaxError("example: show_stars <value> of <total> round to %s [on change call <handler> with <identifier>]" % "|".join(ROUNDERS))
	args = token.contents.split()
	if len(args) == 7:
		match = CMD_PATTERN.match(token.contents)
	elif len(args) == 13:
		match = EX_CMD_PATTERN.match(token.contents)
	else:
		syntax_error()
	if not match:
		syntax_error()

	return ShowStarsNode(*match.groups())   


def do_show_stars_script(parser, token):
	return ShowStarsScriptNode()

register.tag("last_plugins", last_plugins)
register.tag("plugins", plugins)
