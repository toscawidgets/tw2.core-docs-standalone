import tw2.core
import tw2.forms

class Index(tw2.core.Page):
    template = 'genshi:./index.html'

    def fetch_data(self, req):
        self.req = str(req)

tw2.core.dev_server()

