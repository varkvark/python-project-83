from urllib.parse import urlparse, urlunparse


def parsed_url(input_url):
    url_parts = urlparse(input_url)
    parsed_url = urlunparse((url_parts.scheme, url_parts.netloc, '', '', '', ''))
    return parsed_url


def format_date(value, format='%Y-%m-%d'):
    if value is None:
        return ""
    return value.strftime(format)
