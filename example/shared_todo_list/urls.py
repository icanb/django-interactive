from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'shared_todo_list.views.home'),
    url(r'^add-item', 'shared_todo_list.views.add_item'),
    # Parses number from URL and uses it as the item_id argument to the action
    url(r'^delete-item/(?P<item_id>\d+)$', 'shared_todo_list.views.delete_item'),
)
