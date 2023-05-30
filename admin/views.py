from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask import url_for, redirect

class MyAdminIndexView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth'))


class AuthUser(ModelView):
    column_display_pk = True
    
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth'))

