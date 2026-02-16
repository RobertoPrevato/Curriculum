from essentials.folders import ensure_folder
from jinja2 import Environment, Template, PackageLoader, select_autoescape
from markupsafe import Markup
from conf import load_configuration
import markdown


class JinjaGenerator:

    def __init__(self, module_name="source"):
        self.environment = Environment(
            loader=PackageLoader(module_name, "templates"),
            autoescape=select_autoescape(["html", "xml"]),
        )
        # Add custom filter for markdown conversion
        self.environment.filters['markdown'] = self.markdown_to_html
        ensure_folder("out")

    @staticmethod
    def markdown_to_html(text):
        """Convert markdown text to HTML."""
        if not text:
            return text
        return markdown.markdown(text, extensions=['extra', 'nl2br'])

    def generate(self):
        template = self.environment.get_template("index.html")

        configuration = load_configuration()

        data = configuration.values
        # Process profile entries to convert markdown to HTML
        if 'profile' in data:
            data['profile'] = [
                self.markdown_to_html(entry) for entry in data['profile']
            ]

        if 'projects' in data:
            for item in data["projects"]:
                item["description"] = self.markdown_to_html(item["description"])

        with open("./out/index.html", mode="wt", encoding="utf8") as index_file:
            index_file.write(self.render_template(template, data))

    @staticmethod
    def render_template(template: Template, model=None):
        if model:
            return template.render(**model)
        return template.render()


if __name__ == "__main__":

    gen = JinjaGenerator()
    gen.generate()
    print("[*] CV was generated.")
