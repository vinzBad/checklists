from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired
from .models import ChecklistItemTypes

   
class ChecklistTemplateItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField("description")
    itemtype = SelectField("itemtype", choices=ChecklistItemTypes.choices(), coerce=ChecklistItemTypes)


class ChecklistTemplateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField("description")
    items = FieldList(FormField(ChecklistTemplateItemForm))
