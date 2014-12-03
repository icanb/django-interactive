##Sprint 2 - 17 November (Product owner: Ilter Canberk)

* **Creating a URL and action for html_... method (Ilter)

html_.. is supposed to return the up-to-date html string. Since our goal is to prevent user from manually doing this, we will need to dynamically create a url, and action methods that are mapped to these urls.

Expected time: 1 hour

* **Creating a URL and action for json_... method (Naman)

json_render_list is supposed to return JSON representation of the context values. This will be hard because we have no idea about the type of the variables. They might be plain dictionaries or query sets. We need to write a robust checker that recursively goes through the variables and decide how to serialize them.

Expected time: 2 hours

* **Creating a JS Stub generator (Ilter)

This is so that the framework auto generates the stubs for the necessary javascript functions as and when required. The stub generator will be in Python and it will generate JavaScript code. We need to come up with a good architecture for generating methods in general and then move on to implementing individual methods.

Expected time: 2 hours

* **Implementing the stub generator for html_... method (Naman)

html_.. method will send an AJAX request to the Django application and get back the HTML string. It is not supposed to do anything other than passing the string as a callback.

Expected time: 2 hours