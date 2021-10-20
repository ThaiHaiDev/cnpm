from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user
from flask import redirect
from hospital.models import Patient, Medicine, Policy
from hospital import db, admin


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class MedicineModelView(AuthenticatedView):
    can_export = True


class PatientModelView(AuthenticatedView):
    can_export = True


class PolicyModelView(AuthenticatedView):
    can_export = True


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(MedicineModelView(Medicine, db.session, name="Danh sach thuoc"))
admin.add_view(PatientModelView(Patient, db.session, name="Danh sach benh nhan"))
admin.add_view(StatsView(name="BAO CAO THANG"))
admin.add_view(PolicyModelView(Policy, db.session, name="Quy dinh"))
admin.add_view(LogoutView(name="Dang xuat"))