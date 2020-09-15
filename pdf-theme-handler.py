from bs4 import BeautifulSoup


def get_stylesheet() -> str:
    return """
    h1, h2, h3 {
        string-set: chapter content();
    }
    
    .md-container {
        display: block;
        padding-top: 0;
    }
    
    .md-main {
        display: block;
        height: inherit;
    }
    
    .md-main__inner {
        height: inherit;
        padding-top: 0;
    }
    
    .md-typeset .codehilitetable .linenos {
        display: none;
    }
    
    .md-typeset .footnote-ref {
        display: inline-block;
    }
    
    .md-typeset a.footnote-backref {
        transform: translateX(0);
        opacity: 1;
    }
    .md-typeset .admonition {
        display: block;
        border-top: .1rem solid rgba(0,0,0,.07);
        border-right: .1rem solid rgba(0,0,0,.07);
        border-bottom: .1rem solid rgba(0,0,0,.07);
        page-break-inside: avoid;
    }
    
    .md-typeset a::after {
        color: inherit;
        content: none;
    }
    
    .md-typeset table:not([class]) th {
        min-width: 0;
    }
    
    .md-typeset table {
        border: .1rem solid rgba(0,0,0,.07);
    }
    
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
    
    img {
        max-width:100%;
        image-resolution: 300dpi;
    }
    ul li img, ol li img {
        width:80% !important;
    }
    .md-content aside {
      float:none !important;
      margin-left:none !important;
    }
    body {
        font-size: 10px;
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
