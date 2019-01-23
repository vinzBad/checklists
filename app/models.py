import click

from app import db
from enum import Enum
from flask.cli import with_appcontext

class ChecklistItemTypes(Enum):
    Checkbox = "Checkbox"
    Textbox = "Textbox"

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)

class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)

class ChecklistTemplate(db.Model, BaseMixin):
    name = db.Column(db.String())
    description = db.Column(db.String())
    items = db.relationship('ChecklistTemplateItem', lazy='select', backref='template')

class ChecklistTemplateItem(db.Model, BaseMixin):
    itemtype = db.Column(db.Enum(ChecklistItemTypes))
    name = db.Column(db.String())
    description = db.Column(db.String())
    required_for_create = db.Column(db.Boolean())
    template_id = db.Column(db.Integer, db.ForeignKey('checklist_template.id'),
        nullable=False)


# class Checklist(db.Model, BaseMixin):

# class ChecklistItem(db.Model, BaseMixin):



@click.command('db-createall')
@with_appcontext
def createall_command():
    """Create new database."""
    db.create_all()  
    click.echo('Initialized the database.')

@click.command('db-dropall')
@with_appcontext
def dropall_command():
    """Clear existing data."""
    db.drop_all()  
    click.echo('Dropped the database.')


@click.command('db-testmodel')
@with_appcontext
def testmodel_command():
    """Test model definition"""
    template = ChecklistTemplate()
    template.name = "Testtemplate"
    template.description = "This is a test template"
    for i in range(1,4):
        item = ChecklistTemplateItem()
        item.name = "test item %s" % i
        item.description = "this is a test item"
        item.itemtype = ChecklistItemTypes.Checkbox  if i % 2 == 1 else ChecklistItemTypes.Textbox
        template.items.append(item)
    db.session.add(template)
    db.session.commit()
    # TODO: do some querying
    
    click.echo('Tested the model')

def init_app(app):
    app.cli.add_command(createall_command)
    app.cli.add_command(dropall_command)
    app.cli.add_command(testmodel_command)
