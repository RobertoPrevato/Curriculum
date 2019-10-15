from conf import configuration
from rocore.folders import ensure_folder
from jinja2 import Environment, Template, PackageLoader, select_autoescape


class JinjaGenerator:

    def __init__(self, module_name='source'):
        self.environment = Environment(
            loader=PackageLoader(module_name, 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        ensure_folder('out')

    def generate(self):
        template = self.environment.get_template('index.html')

        with open('./out/index.html', mode='wt', encoding='utf8') as index_file:
            index_file.write(self.render_template(template, configuration))

    @staticmethod
    def render_template(template: Template, model=None):
        if model:
            return template.render(**model)
        return template.render()


if __name__ == '__main__':

    gen = JinjaGenerator()
    gen.generate()

