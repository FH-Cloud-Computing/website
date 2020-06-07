import pprint

from bs4 import BeautifulSoup


def get_stylesheet() -> str:
    return """
    body > .container {
        margin-top: -100px;
    }
    @page {
        @bottom-left {
            content: counter(__pgnum__);
        }
        size: a4;
    }

    @media print {
        .noprint {
            display: none;
        }
    }
    """


def modify_html(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    downloads = soup.findAll("div", {"class": "download"})
    if len(downloads) > 0:

        a = soup.new_tag('a', href=href, download=None)
        button = soup.new_tag('button')
        button.string = 'Download PDF 🖨️'
        a.append(button)

        downloads[0].insert(0, a)
    return str(soup)
