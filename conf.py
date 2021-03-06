# -*- coding: utf-8 -*-
#
# RoboFont documentation build configuration file, created by
# sphinx-quickstart on Wed Sep  3 17:42:26 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
from datetime import date

today = date.today()
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'RoboFont'
copyright = u'%s, Frederik Berlaen' % today.year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.6'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'roboFontTheme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
sys.path.append(os.path.abspath('theme'))
html_theme_path = ['theme']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'RoboFontdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'RoboFont.tex', u'RoboFont',
   u'Frederik Berlaen', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'robofont', u'RoboFont',
     [u'Frederik Berlaen'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'RoboFont', u'RoboFont',
   u'Frederik Berlaen', 'RoboFont', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

## sphinx hacking
import posixpath

import os

from sphinx import addnodes
from docutils.parsers.rst import directives
from sphinx.directives.code import LiteralInclude
from sphinx.directives.other import TocTree
from sphinx.writers.html import HTMLTranslator

from docutils import io, utils, statemachine

def visit_download_reference(self, node):
    if node.hasattr('filename'):
        data = dict(
            urlPath=posixpath.join(self.builder.dlpath, node['filename']),
            fileName=node['filename']
            )
        self.body.append('<div class="downloadlink"><a class="scriptReference roboFontLink" href="%(urlPath)s?open=1">Open in RoboFont: %(fileName)s</a>' % data)
        self.body.append('<a class="scriptReference" href="%(urlPath)s">Download: %(fileName)s</a></div>' % data)

        node.clear()

def depart_download_reference(self, node):
    pass

HTMLTranslator.visit_download_reference = visit_download_reference
HTMLTranslator.depart_download_reference = depart_download_reference

class ShowCode(LiteralInclude):

    has_content = False
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        nodes = super(ShowCode, self).run()
        node = addnodes.download_reference()
        node['reftarget'] = self.arguments[0]
        nodes.append(node)
        return nodes

class DocTocTree(TocTree):

    def run(self):
        rst = super(DocTocTree, self).run()
        rst[0][0]['entries'].reverse()
        return rst



class BlogPreview(directives.misc.Include):

    option_spec = {'literal': directives.flag,
                   'encoding': directives.encoding,
                   'tab-width': int,
                   'start-line': int,
                   'end-line': int,
                   'start-after': directives.unchanged_required,
                   'end-before': directives.unchanged_required,
                   'max-posts': int,
                   'title': directives.unchanged_required}

    def run(self):
        source = self.state_machine.input_lines.source(
            self.lineno - self.state_machine.input_offset - 1)
        source_dir = os.path.dirname(os.path.abspath(source))
        path = directives.path(self.arguments[0])
        path = os.path.normpath(os.path.join(source_dir, path))

        relativePath = os.path.normpath(os.path.join(source_dir, path))
        relativePath = utils.relative_path(None, path)

        encoding = self.options.get(
            'encoding', self.state.document.settings.input_encoding)
        tab_width = self.options.get(
            'tab-width', self.state.document.settings.tab_width)
        # must be a comment
        before_text = self.options.get('end-before', '.. Continue Reading')
        title = self.options.get('title', None)
        max_posts = self.options.get('max-posts', 3)
        paths = os.listdir(path)

        rawtext = ""
        rawtext += '.. raw:: html\n\n    <aside class="blogentries">\n\n'

        if title:
            rawtext += title + "\n"
            rawtext += len(title)*'-' + "\n\n"

        c = 0
        paths.sort()
        for blogPath in reversed(paths):
            if c > max_posts:
                break
            pageName, ext = os.path.splitext(blogPath)
            if ext != ".rst":
                continue
            blogPath = os.path.join(path, blogPath)
            self.state.document.settings.record_dependencies.add(blogPath)
            try:
                include_file = io.FileInput(
                    source_path=blogPath, encoding=encoding,
                    error_handler=(self.state.document.settings.\
                                   input_encoding_error_handler),
                    handle_io_errors=None)
            except IOError, error:
                raise self.severe(u'Problems with "%s" directive path:\n%s.' %
                            (self.name, error))
            content = include_file.read()
            include_file.close()

            if before_text:
                # skip content in rawtext after *and incl.* a matching text
                before_index = content.find(before_text)
                if before_index >= 0:
                    tag = before_text[3:]
                    content = content[:before_index] + "\n.. cssclass:: continue_reading\n\n" + tag
                    content = content.replace(tag, '`%s <%s>`__' % (tag,  os.path.join(relativePath, pageName) + '.html'))

            lines = content.split("\n")
            if len(lines) > 2 and len(lines[0]) == len(lines[1]) and len(lines[1])*"=" == lines[1]:
                # we have title
                lines[0] = '`%s <%s>`__' % (lines[0], os.path.join(relativePath, pageName) + '.html')
                lines[1] = len(lines[0]) * "-"
            content = "\n".join(lines)

            rawtext += content
            rawtext += "\n\n"
            c += 1

        rawtext += '.. raw:: html\n\n    </div></aside><div>\n\n'

        include_lines = statemachine.string2lines(
                rawtext, tab_width, convert_whitespace=1)
        self.state_machine.insert_input(include_lines, path)
        return []

def setup(app):
    app.add_directive('showcode', ShowCode)
    app.add_directive('doctoctree', DocTocTree)
    app.add_directive('blogpreview', BlogPreview)
