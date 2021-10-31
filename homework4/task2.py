"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
# count_dots_on_i("https://example.com/")
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""


import urllib.request, urllib.error


def count_dots_on_i(url: str) -> int:
    try:
        f = urllib.request.urlopen(url)
        n = 0
        s = f.read().decode('utf-8')
        for symbol in s:
            if symbol == "i":
                n += 1
        print(n)
        return n
    except urllib.error.URLError:
        raise ValueError(f"Unreachable {url}")


if __name__ == "__main__":

    count_dots_on_i('https://example.com/')
    count_dots_on_i('https://fghjhgjkhjl.com')