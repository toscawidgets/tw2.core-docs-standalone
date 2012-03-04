import tw2.core
import tw2.forms
import tw2.dynforms
import tw2.sqla
import tw2.jqplugins.jqgrid
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
        id = tw2.forms.HiddenField()
        title = tw2.forms.TextField(validator=tw2.core.Required)
        director = tw2.forms.TextField()
        genre = tw2.sqla.DbCheckBoxList(entity=model.Genre)
        class cast(tw2.dynforms.GrowingGridLayout):
            character = tw2.forms.TextField()
            actor = tw2.forms.TextField()

class GridWidget(tw2.jqplugins.jqgrid.SQLAjqGridWidget):
    entity = model.Movie
    excluded_columns = ['id']
    prmFilter = {'stringResult': True, 'searchOnEnter': False}
    pager_options = { "search" : True, "refresh" : True, "add" : False, }
    options = {
        'url': '/db_jqgrid/',
        'rowNum':15,
        'rowList':[15,30,50],
        'viewrecords':True,
        'imgpath': 'scripts/jqGrid/themes/green/images',
        'width': 900,
        'height': 'auto',
    }

tw2.core.register_controller(GridWidget, 'db_jqgrid')

class Grid(tw2.core.Page):
    title = 'jQuery jqGrid'
    child = GridWidget

tw2.core.dev_server(repoze_tm=True)

