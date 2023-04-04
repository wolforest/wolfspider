from scrapy.selector import Selector


class HtmlParser(object):
    root: Selector = None

    def parse(self, text: str, selector: dict) -> dict:
        """
        :param text: str
        :param selector: dict
        :return: dict {}
        """
        if not SelectorValidator.validate(selector):
            raise SyntaxError("invalid html selector map")

        self.root = Selector(text=text)

        return {}


class SelectorValidator(object):
    @staticmethod
    def validate(selector: dict) -> bool:
        if not dict:
            return False

        for k, v in selector.items():
            if not isinstance(k, str):
                return False

            if not isinstance(v, dict):
                return False

            if 'model' not in v:
                return False

            if 'selector' not in v and 'regex' not in v:
                return False

        return True
