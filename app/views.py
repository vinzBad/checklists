from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app import db

from .models import ChecklistItemTypes, ChecklistTemplate, ChecklistTemplateItem
from .forms import ChecklistTemplateForm, ChecklistTemplateItemForm

bp = Blueprint('views', __name__)

@bp.route("/")
def index():
    templates = ChecklistTemplate.query.all()
    return render_template("index.html", templates=templates)

@bp.route("/template/<int:template_id>/edit", methods=["POST", "GET"])
def edit_template(template_id):
    template = ChecklistTemplate.query.get_or_404(template_id)
    form = ChecklistTemplateForm(request.form, obj=template)

    if form.validate_on_submit():
        form.populate_obj(template)
        db.session.add(template)
        db.session.commit()
    return render_template("edit_template.html", template=template, form=form)