import tw2.core
import tw2.forms
import tw2.dynforms
import tw2.sqla
import model

class Index(tw2.sqla.DbListPage):
    entity = model.Movie
    title = 'Movies'
    newlink = tw2.forms.LinkField(link='movie', text='New', value=1)
    class child(tw2.forms.GridLayout):
        title = tw2.forms.LabelField()
        id = tw2.forms.LinkField(link='movie?id=$', text='Edit', label=None)


class Movie(tw2.sqla.DbFormPage):
    entity = model.Movie
    redirect = '/'
    resources = [tw2.core.CSSLink(filename='myapp.css')]
    title = 'Movie'
    class child(tw2.dynforms.CustomisedTableForm):
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genre = tw2.sqla.DbCheckBoxList(entity=model.Genre)
        class cast(tw2.dynforms.GrowingGridLayout):
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()


tw2.core.dev_server(repoze_tm=True)

