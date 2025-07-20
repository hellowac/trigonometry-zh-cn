# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "三角学(trigonometry)"
copyright = "2009, Michael Corral"
author = "Michael Corral"
release = "1.0"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinxcontrib.youtube",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx_togglebutton",
]

source_encoding = 'utf-8'
language = "zh_CN"

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'furo'
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/hellowac/trigonometry-zh-cn",
    "use_repository_button": True,
}
html_static_path = ["_static"]
html_css_files = []
html_title = "三角学(trigonometry)"

highlight_language = "python"  # 默认语言（可选）
pygments_style = "sphinx"  # Sphinx 默认样式

togglebutton_hint = "原文"
togglebutton_hint_hide = "收起"

mathjax3_config = {
    "tex": {
        "inlineMath": [['$', '$'], ['\\(', '\\)']],
        "displayMath": [['$$', '$$'], ['\\[', '\\]']],
    }
}


# mathjax3_config = {
#     "loader": {"load": ["[tex]/cancel"]},
#     "tex": {"packages": {"[+]": ["cancel"]}},
# }

# .. math::

#    \cancel{ABC}        % 单线删除线（从右上到左下）
#    \bcancel{ABC}       % 反方向（从左上到右下）
#    \xcancel{ABC}       % 交叉删除线
#    \cancelto{0}{ABC}   % 画一条箭头线指向某值
