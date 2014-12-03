from pyquery import PyQuery as pq
from lxml import etree
import urllib

def page_view(original_function):
    def new_function(request, *args, **kwargs):
        print("page_view is invoked.")
        r = original_function(request, *args, **kwargs)
        x = r._container
        htmlCode = pq(x)
        #x.append("<script src=\"//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.js\" type=\"text/javascript\"></script>")
        
        r._container = x

        print str(htmlCode)
        #d = pq(etree.fromstring("<html></html>"))
        #d = pq(url='http://google.com/')
        #d = pq(filename=path_to_html_file)
        #print d

        return r

    return new_function