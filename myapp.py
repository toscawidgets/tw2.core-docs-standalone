import tw2.core
import tw2.forms
import tw2.sqla
import model

class Index(tw2.core.Page):
    template = 'genshi:./index.html'

    def fetch_data(self, req):
        self.req = str(req)

class Movie(tw2.sqla.DbFormPage):
    entity = model.Movie
    resources = [tw2.core.CSSLink(filename='myapp.css')]
    title = 'Movie'
    class child(tw2.forms.TableForm):
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genre = tw2.sqla.DbCheckBoxList(entity=model.Genre)
        class cast(tw2.forms.GridLayout):
            extra_reps = 5
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()


tw2.core.dev_server(repoze_tm=True)

