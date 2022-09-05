class LanguageHandler:
    def __init__(self, languages, sections):
        self.languages = languages
        self.sections = sections

    def format_languages(self):
        formatted = ""

        for lang in self.languages:
            if lang != self.languages[-1]:
                formatted += f"{lang}/"
            else:
                formatted += lang

        return f"[{formatted}]"

    def get_lang_and_text(self):
        lang_options = self.format_languages()
        self.language = ""

        while self.language not in self.languages:
            self.language = input(f"{lang_options} ? ")

        return self.sections[self.language]
