from rocore.folders import ensure_folder
from jinja2 import Environment, Template, PackageLoader, select_autoescape
from conf import load_configuration


class JinjaGenerator:

    def __init__(self, module_name='source'):
        self.environment = Environment(
            loader=PackageLoader(module_name, 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        ensure_folder('out')

    def generate(self):
        template = self.environment.get_template('index.html')

        configuration = load_configuration()

        with open('./out/index.html', mode='wt', encoding='utf8') as index_file:
            index_file.write(self.render_template(template, configuration.values))

    @staticmethod
    def render_template(template: Template, model=None):
        if model:
            return template.render(**model)
        return template.render()


if __name__ == '__main__':

    gen = JinjaGenerator()
    gen.generate()

