import math, re

from django.template import Library, Node, TemplateSyntaxError, VariableDoesNotExist, resolve_variable
from django.conf import settings

register = Library()

# folder inside media that contains the images
IMG_FOLDER = "common/img/star-rate/"
FULL_FOLDER = settings.STATIC_URL + IMG_FOLDER
DIV_TEMPLATE	= "<div class=\"star-rate\" id=\"star_strip_%s\">"
END_DIV_TEMPLATE= "</div>"
IMG_TEMPLATE	= "<img border=\"0\" src=\"%s\" alt=\"%s\"/>"
EX_IMG_TEMPLATE	= "<img onmouseover=\"javascript: hoverStar(%s, %s);\" onmouseout=\"javascript: restoreStar(%s);\" onclick=\"javascript: clickStar('%s', %s, %s);\" border=\"0\" src=\"%s\" alt=\"%s\"/>"
STARS = {
	0.0:	("No Star", "star-rate.0.0.png"),
	0.25:	("Quarter Star", "star-rate.0.25.png"),
	0.5:	("Half Star", "star-rate.0.5.png"),
	0.75:	("Three Quarter Star", "star-rate.0.75.png"),
	1.0:	("Full Star", "star-rate.1.0.png")
}
ROUNDERS = {
	"full": 1,
	"half": 2,
	"quarter": 4
}
CMD_PATTERN	= re.compile("^show_stars (.*) of (\d*) round to (%s)$" % "|".join(ROUNDERS))
EX_CMD_PATTERN	= re.compile("^show_stars (.*) of (\d*) round to (%s) on change call (\w*) with (.*)$" % "|".join(ROUNDERS))
JS_TEMPLATE = """
<script type="text/javascript">
<!--
var starSaves = new Hash();

function hoverStar(id, pos) {
	var starStrip = $('star_strip_' + id);

	if (starSaves.keys().indexOf(id) == -1) {
		var starSave = new Array();
		var imgs = starStrip.select("img")

		for (var i = 0; i < imgs.length; i++) {
			starSave[starSave.length] = imgs[i].src;
			if (i < pos)
				imgs[i].src = "%(star10)s";
			else
				imgs[i].src = "%(star00)s";
		}
		starSaves.set(id, starSave);
	}
}

function clickStar(chainTo, id, pos) {
	try {
		if (eval('typeof(' + chainTo + ')') == 'function')
			eval(chainTo + '(' + id  + ', ' + pos + ');');
	}
	catch (err)
	{
		//do nothing...
		alert(err);
	}
	var starStrip = $('star_strip_' + id);
	var imgs = starStrip.select("img")

	for (var i = 0; i < imgs.length; i++) {
		if (i < pos)
			imgs[i].src = "%(star10)s";
		else
			imgs[i].src = "%(star00)s";
	}
	starSaves.unset(id);
}

function restoreStar(id) {
	srcs = starSaves.get(id);
	if (srcs == undefined)
		return;

	var starStrip = $('star_strip_' + id);
	var imgs = starStrip.select("img");

	for (var i = 0; i < srcs.length; i++) {
		imgs[i].src = srcs[i];
	}
	starSaves.unset(id);
}

//-->
</script>
""" % {
	#'star025' : '/media/img/'+STARS[0.25],
	#'star05' : '/media/img/'+STARS[0.5],
	#'star075' : '/media/img/'+STARS[0.75],
	'star00' : FULL_FOLDER+STARS[0.0][1],
	'star10' : FULL_FOLDER+STARS[1.0][1],
}

class ShowStarsNode(Node):
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


def do_show_stars(parser, token):
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

register.tag("show_stars", do_show_stars)
register.tag("show_stars_script", do_show_stars_script)
