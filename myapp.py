import tw2.core

class Index(tw2.core.Page):
    template = 'genshi:./index.html'

tw2.core.dev_server()

