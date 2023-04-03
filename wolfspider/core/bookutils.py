import re


def parse_book_name(text: str) -> str:
    if not text:
        return text

    pattern = re.compile(u'[(（\\[【{](.*?)[)）\\]】}]')
    result = re.sub(pattern, ' ', text)
    if not result:
        return result

    return result.strip()


if __name__ == '__main__':
    print(parse_book_name(u'高效能人士的七个习惯（精华版）'))
    print(parse_book_name(u'高效能人士的七个习惯(精华版)'))
    print(parse_book_name(u'高效能人士的七个习惯[精华版]'))
    print(parse_book_name(u'高效能人士的七个习惯【精华版】'))
    print(parse_book_name(u'高效能人士的七个习惯{精华版}'))
