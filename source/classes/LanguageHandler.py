class LanguageHandler:
    def __init__(self, languages: list[str], sections: dict[list]):
        self.languages = languages
        self.sections = sections

    def format_languages(self, sep):
        return f"[{sep.join(self.languages)}]"

    def get_lang_and_text(self):
        lang_options = self.format_languages("/")
        self.language = ""

        while self.language not in self.languages:
            self.language = input(f"{lang_options} ? ")

        return self.sections[self.language]
