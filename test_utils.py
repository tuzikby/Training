import requests

url = "https://hn.algolia.com/api/v1/search?query="


# options = """Please choose an option from below
# 1. Find article with highest number of comments
# 2. Find article with the highest number of points
# 3. First 10 articles about python"""

# def getUserSelection():
#     r = input(options)
#     return r

def http_request(query):
    r = requests.get(url + query)
    json_payload = r.json()
    hits = json_payload["hits"]
    return hits


def find_article_by_max_property(propertyName):
    hits = http_request('p')
    max_number = 0
    element = 0
    for x in range(0, len(hits)):
        data = hits[x]
        num = data[propertyName]
        if num > max_number:
            max_number = num
            element = x

    title = hits[element]["title"]
    return_value = {'Title': title, 'Number of ' + propertyName: max_number}
    return return_value


def highest_num_comments():
    return find_article_by_max_property('num_comments')


def highest_rating():
    return find_article_by_max_property('points')


def pretty_print(array):
    for x in array:
        print(x)
        print('\n')


def first_ten_python_articles():
    hits = http_request('python')
    array_articles = []
    for x in range(0, 9):
        data = hits[x]
        title = data['title']
        array_articles.append(title)
    return array_articles


def top_ten_articles():
    return_array = []
    hits = http_request('p')
    hits.sort(key=lambda x: x['num_comments'], reverse=True)
    top_ten = hits[0:9]
    for x in top_ten:
        return_array.append({'Title':x['title'], 'Number Of Comments':x['num_comments']})
    return return_array
