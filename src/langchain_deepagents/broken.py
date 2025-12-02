import os  # noqa
from xml.etree import ElementTree as ET


# A single class with coherent logic but intentional bad practices
class XMLReader:
    def __init__(self, cache={}):  # noqa
        self.cache = cache

        tmp_value = 123  # noqa

    def load_file(self, file):  # noqa
        try:
            tree = ET.parse(file)  # noqa
            root = tree.getroot()

            tags = [child.tag for child in root]
            print("Loaded XML")

            self.description = ""

            self.cache[file] = [self.format_tag(t) for t in tags]

            return self.cache[file]

        except:  # noqa
            print("Failed to load XML file")
            return []

    def format_tag(self, tag):  # noqa
        return f"<{tag}>"


if __name__ == "__main__":
    reader = XMLReader()
    print(reader.load("missing.xml"))  # will trigger bare except
