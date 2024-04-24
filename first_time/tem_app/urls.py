from django.urls import path
from tem_app.views import tem_var, pass_dict, pass_obj, pass_list, show_score, show_list, show_include, show_child, \
    show_filter

urlpatterns = [
    path('var/<name>/', tem_var),
    path('dict/', pass_dict),
    path('obj/', pass_obj),
    path('list/', pass_list),
    path('show_score/<int:score>/', show_score),
    path('show_list/', show_list),
    path('show_include/', show_include),
    path('block/', show_child),
    path('filter/', show_filter),
]
