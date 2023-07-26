from scrapy.selector import Selector


class HtmlParser(object):
    root: Selector = None
    result: dict = None

    def parse(self, text: str, models: dict) -> dict:
        """
        :param text: str
        :param models: dict
        :return: dict {}
        """
        if not SelectorValidator.validate(models):
            raise SyntaxError("invalid html selector map")

        self.root = Selector(text=text)
        self.result = {}

        self.extract(models)

        return self.result

    def extract(self, models: dict):
        for k, v in models.items():
            if 'list' == v.get('select_type'):
                self.extract_object_list(k, v)
                continue

            self.extract_object(k, v)

    def extract_object(self, key: str, model: dict, parent=None):
        if parent is None:
            parent = self.root

        data = model['model']
        for k, v in data.items():
            data[k] = parent.xpath(v).get()

        self.result[key] = data

    def extract_object_list(self, key: str, model: dict):
        for item in self.root.xpath(model.get('selector')):
            self.extract_object(key, model, item)


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

        return True


book = {
    'name': '//div[@id="wrapper"]/h1/span/text()',
    'origin_name': '//div[@id="info"]/text()[1]',
    'main_pic': '//div[@id="mainpic"]/a/@href',
    'pages': '//*[@id="info"]/text()[3]',
    'ISBN': '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/text()[6]',
    'created_at': '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/text()[2]',
    'introduction': '//*[@id="link-report"]/span[2]/div/div/p/text()',
    'category': '//*[@id="dir_1048007_full"]/text()',
}

conf = {
    "book": {
        "model": book,
    }
}

if __name__ == '__main__':
    file_path = '/Users/wingle/code/github/wolfspider/data'
    filename = f'{file_path}/douban_7_habits.html'
    file = open(filename, "r")
    html = file.read()
    file.close()

    result = HtmlParser().parse(html, conf)
    print(result)
