import feedparser
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt5.Qt import QFont




class News(QScrollArea):
    def __init__(self):
        super(News, self).__init__()

        widget = QWidget()
        layout = QVBoxLayout(widget)

        # news feed code
        def parseRSS(rss_url):
            return feedparser.parse(rss_url)

        def getHeadLines(rss_url):
            headlines = []

            feed = parseRSS(rss_url)
            for newitem in feed['items']:
                headlines.append(newitem['title'])

            return headlines

        def getHyperLink(rss_url):
            hyperlinks = []

            feed = parseRSS(rss_url)
            for newitem in feed['items']:
                hyperlinks.append(newitem['link'])

            return hyperlinks

        allheadlines = []
        allhyperlinks = []


        newsurls = {
            # Auto Zone
            'googlenews': 'https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREo2Tm5kc0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen',
            # O'Reilly Auto Parts
            # 'googlenews': 'https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNR2czWDNoZkVnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen',
            # Pep Boys
            # 'googlenews': 'https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRE13Y0Y5d0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen'
        }

        for key, url in newsurls.items():
            allheadlines.extend(getHeadLines(url))

        for key, url in newsurls.items():
            allhyperlinks.extend(getHyperLink(url))

        for h, url in zip(allheadlines, allhyperlinks):
            headline = QLabel()
            headline.setOpenExternalLinks(True)
            headline.setFont(QFont('Arial', 12))
            headline.setText(f'<a href={url}> {h} </a>')
            headline.setMaximumWidth(800)
            layout.addWidget(headline)

        self.setWidget(widget)
        self.setWidgetResizable(True)