from docutils import nodes
from sphinx import addnodes
from urllib.parse import urljoin


class Visitor:

    def __init__(self, document):
        self.document = document
        self.text_list = []
        self.n_sections = 0

    def dispatch_visit(self, node):
        # toctreeは飛ばす
        if isinstance(node, addnodes.compact_paragraph) and node.get('toctree'):
            raise nodes.SkipChildren

        # 3つ目のセクションまではテキスト収集する
        if self.n_sections < 3:

            # テキストを収集
            if isinstance(node, nodes.paragraph):
                self.text_list.append(node.astext())

            # セクションに来たら深さを追加
            if isinstance(node, nodes.section):
                self.n_sections += 1

    def dispatch_departure(self, node):
        pass

    def get_og_description(self):
        text = ' '.join(self.text_list)
        if len(text) > 180:
            text = text[:177] + '...'
        return text


def get_og_tags(context, doctree):
    # collection
    visitor = Visitor(doctree)
    doctree.walkabout(visitor)

    # og:description
    og_desc = visitor.get_og_description()

    ## OGP
    tags = '''
    <meta name="theme-color" content="#08C"/>
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@archlinux_jp" />
    <meta name="twitter:title" content="{ctx}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://www.archlinux.jp/images/amplogo.png">
    '''.format(ctx='Arch Linux マニュアルページ' if context['title'] == 'Arch Linux マニュアルページ' else context['title'] + " - Arch Linux マニュアルページ", desc=og_desc)
    return tags


def html_page_context(app, pagename, templatename, context, doctree):
    if not doctree:
        return

    context['metatags'] += get_og_tags(context, doctree)


def setup(app):
    app.connect('html-page-context', html_page_context)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
