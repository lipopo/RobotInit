# -*- cofing:utf8 -*-

from ...env import jinja2


class ConfigTemplate:
    def __init__(self, config_dict, source, **kwargs):
        self.render_dict = config_dict
        self.template = jinja2.Template(source, variable_start_string="{", variable_end_string="}", **kwargs)

    def render(self, use):
        return self.template.render(use)

    @property
    def render_value(self):
        return self.render(self.render_dict)