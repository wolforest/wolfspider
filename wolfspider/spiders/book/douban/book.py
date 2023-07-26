
book = {
    'name': '',
    'origin_name': '',
    'main_pic': '',
    'pages': 0,
    'ISBN': '',
    'created_at': '',
    'introduction': '',
    'category': '',
}

rate = {
    'rate': '',
    'rate_count': '',
    '5star_percent': '',
    '4star_percent': '',
    '3star_percent': '',
    '2star_percent': '',
    '1star_percent': '',

}

author = {

}

excerpt = {

}

comment = {

}

review = {

}

selectors = {
    "book": {
        "model": book,
        "selector": "root"
    },
    "rate": {
        "model": rate,
        "selector": "",
        "regex": "",
    },
    "authors": {
        "model": author,
        "selector": ""
    },
    "excerpts": {

    },
    "related_books": {
        "model": book,
        "selector": "",
        "selector_type": "list",
    },
    "comments": {

    },
    "reviews": {

    }

}




