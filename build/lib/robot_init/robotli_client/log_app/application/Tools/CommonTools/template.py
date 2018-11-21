# -*- cofing:utf8 -*-

from ...env import re

# class ConfigTemplate:
#     def __init__(self, config_dict, source, **kwargs):
#         self.render_dict = config_dict
#         if not isinstance(source, basestring):
#             source = str(source)
#         self.template = jinja2.Template(source, variable_start_string="{", variable_end_string="}", **kwargs)
#
#     def render(self, use):
#         return self.template.render(use)
#
#     @property
#     def render_value(self):
#         return self.render(self.render_dict)

class RowRender(object):
    def __init__(self, render_dict, regx="{...}"):
        assert isinstance(render_dict, dict), "Please Insert Dict Type"
        self._render_dict = render_dict
        self._regx_left, self._regx_right = tuple(regx.split("..."))
        self._regx = regx.replace("...", "[^%s]+"%(self._regx_left+self._regx_right,))
    def render(self, source):
        while True:
            source_list = re.findall(self._regx, source)
            if len(source_list) == 0:
                break
            for s_ in source_list:
                source = source.replace( s_, self._render_dict.get( s_.replace(self._regx_right, "").replace(self._regx_left, "").strip(), ""))
        return source

