from scrapy.selector import Selector


class DetailParser(object):
    html: Selector = None

    def parse(self, text: str):
        self.html = Selector(text=text)

        title = self.html.xpath('//title/text()').get()
        print('title: ', title)

        content = self.html.xpath('//div[@id="wrapper"]/h1/span/text()').get()
        print('book name: ', content)

        content = self.html.xpath('//div[@id="mainpic"]/a/@href').get()
        print('main pic: ', content)

        content = self.html.xpath('//div[@id="mainpic"]/a/img/@src').get()
        print('main pic: ', content)

        print("related books: ")
        for dl in self.html.xpath('//div[@id="db-rec-section"]/div/dl'):
            item = dl.xpath('.//dd/a/text()').get()
            if item:
                print(item.strip())


        return None


if __name__ == '__main__':
    file_path = '/Users/wingle/code/github/wolfspider/data'
    filename = f'{file_path}/douban_7_habits.html'
    file = open(filename, "r")
    html = file.read()
    file.close()

    parser = DetailParser()
    parser.parse(html)


