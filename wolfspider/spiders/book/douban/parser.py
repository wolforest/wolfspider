import re

from scrapy.selector import Selector


class DetailParser(object):
    html: Selector = None

    def parse(self, text: str):
        self.html = Selector(text=text)

        # title = self.html.xpath('//title/text()').get()
        # print('title: ', title)
        #
        # content = self.html.xpath('//div[@id="wrapper"]/h1/span/text()').get()
        # print('book name: ', content)
        #
        # content = self.html.xpath('//div[@id="mainpic"]/a/@href').get()
        # print('main pic: ', content)
        #
        # content = self.html.css('#info span:contains(ISBN)').get()
        # print('ISBN: ', content)
        content = self.html.xpath('//div[@id="info"]/span[contains(., "原作名")]/following-sibling::text()').extract()
        print('原作名:' , content)

        # content = self.html.xpath('//div[@id="info"]/span[contains(., "出版年")]/following-sibling::text()').get()
        # print('出版年:' + content.strip())
        #
        # content = self.html.xpath('//div[@id="info"]/span[contains(., "页数")]/following-sibling::text()').get()
        # print('页数:' + content.strip())
        #
        # content = self.html.xpath('//div[@id="info"]/span[contains(., "定价")]/following-sibling::text()').get()
        # print('定价:' + content.strip())
        #
        # content = self.html.xpath('//div[@id="info"]/span[contains(., "装帧")]/following-sibling::text()').get()
        # print('装帧:' + content.strip())

        # content = self.html.xpath('//div[@id="info"]/span[contains(., "ISBN")]/following-sibling::text()').get()
        # print('ISBN:' + content.strip())

        # content = self.html.xpath('//*[@id="info"]').re(r'<span\s*class="pl">(.*)<\/span>((?:.|\n)*?)<br[\/]?>')
        # print('category: ', content)
        #
        # print(len(content))
        # map = dict(zip(*[iter(content)] * 2))
        #
        # for k, v in map.items():
        #     print(self.format(k) + ":" + self.format(v))

    def format(self, text: str):
        pattern = re.compile(r'\\t|\\n|:')
        result = re.sub(pattern, '', text)

        pattern = re.compile(r'\s+')
        result = re.sub(pattern, ' ', result)

        if not result:
            return result

        return result.strip()

        # print("related books: ")
        # for dl in self.html.xpath('//div[@id="db-rec-section"]/div/dl'):
        #     item = dl.xpath('.//dd/a/text()').get()
        #     if item:
        #         print(item.strip())

        return None


if __name__ == '__main__':
    file_path = '/Users/wingle/code/github/wolfspider/data'
    filename = f'{file_path}/douban_7_habits.html'
    file = open(filename, "r")
    html = file.read()
    file.close()

    html = html.replace("\n", "")
    pattern = re.compile(r'\s+')
    html = re.sub(pattern, " ", html)


    parser = DetailParser()
    parser.parse(html)
