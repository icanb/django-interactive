Sprint 1 - 10 November (Product Owner: Naman Seth)
Making an empty module that is installable by Django (Ilter) - completed.

This feature will enable easy installation of the feature into the django framework so users can use our library from inside the Django applications. Once the user installs library, they can easily import the modules and start using the features of our in the application they are working. Because the installation is easy it decreases the effort required from the users end in setup and precious time and energy can be used to actually developing applications.

After creating this, we should also find an easy way to use this module in "Development mode" so that we don't need to re-install the package everytime we change something. It would drop the productivity a lot.

Expected time: 2 hours

Creating the @page_view decorator (Naman) - completed.

This decorator identifies the method that is subsequently written as the one that renders an entire page. With this decorator in place, our framework can insert the necessary JavaScript stubs and necessary libraries. This also makes sure that similar stubs or same libraries are only injected in the page once.

Expected time: 2 hours

Creating the @sub_view decorator (Ilter) - completed.

This decorator should take the name of the template and the context, and return the representation for sub_view so that the page views can render it, or helper methods(eg.json generator) can use it.For each subview, there are three JS methods generated.

Expected time: 3 hours

Creating the ability to render subviews inside other templates (Naman) - completed.

This will allow developers to render subviews in different templates. It will give developers the flexibility to render swift views in different templates. We will be using "template_tags" to enable this feature. We really would like to refrain from forcing user to write {% load ... %} on top of every template, but it might not be technically possible.

