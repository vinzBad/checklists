from flask_wtf import FlaskForm
from wtforms import HiddenField,IntegerField, StringField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired
from .models import ChecklistItemTypes


   
class ChecklistTemplateItemForm(FlaskForm):
    id = HiddenField()
    name = StringField('Name:', [DataRequired()])
    description = StringField("Description: ")
    itemtype = SelectField("Typ:", choices=ChecklistItemTypes.choices(), coerce=ChecklistItemTypes)


class ChecklistTemplateForm(FlaskForm):
    id = HiddenField()
    name = StringField('Name:', [DataRequired()])
    description = StringField("Description:")
    items = FieldList(FormField(ChecklistTemplateItemForm))
