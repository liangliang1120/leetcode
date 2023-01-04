# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def dfs(currUrl):
            visited.add(currUrl)
            for nextUrl in htmlParser.getUrls(currUrl):
                next_domian = nextUrl.split('http://')[1].split('/')[0]
                if next_domian == domain and nextUrl not in visited:
                    dfs(nextUrl)
        
        domain = startUrl.split('http://')[1].split('/')[0]
        visited = set()
        visited.add(startUrl)
        dfs(startUrl)
        return list(visited)





