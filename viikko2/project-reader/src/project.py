class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors = ""
        for author in self.authors:
            authors += f"- {author}\n"

        dependencies = ""
        for dependency in self.dependencies:
            dependencies += f"- {dependency}\n"

        dev_dependencies = ""
        for dev_dependency in self.dev_dependencies:
            dev_dependencies += f"- {dev_dependency}\n"  

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{authors}"
            f"\nDependencies:\n{dependencies}"
            f"\nDevelopment dependencies:\n{dev_dependencies}"
        )
