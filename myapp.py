import tw2.core
import tw2.forms

class Index(tw2.core.Page):
    template = 'genshi:./index.html'

    def fetch_data(self, req):
        self.req = str(req)

class Movie(tw2.forms.FormPage):
    resources = [tw2.core.CSSLink(filename='myapp.css')]
    title = 'Movie'
    class child(tw2.forms.TableForm):
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genre = tw2.forms.CheckBoxList(
            options=['Action', 'Comedy', 'Romance', 'Sci-fi'])
        class cast(tw2.forms.GridLayout):
            extra_reps = 5
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()


tw2.core.dev_server()

