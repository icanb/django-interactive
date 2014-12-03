#django-interactive

Django library for creating view hierarchies and auto-generating corresponding client-side methods in your project.

## Overview

In its current state, it is immensly difficult to create and maintain the connection between the server-side and the client-side functionality in a Django app. Once the django action calls 'render' with some context, it is clueless about the rest of the process.

Django-interactive aims to solve this problem by letting the application developer define `subview`s and auto-generating client-side JavaScript stubs that are capable of dynamically rendering these partial views.

## Design Goals

This library should make simple things easy, and complex things still possible. As with any abstraction, it will involve some biased decisions but the application developer should be able to choose not to use some of these decisions and customize parts.

* The application programmer should not be forced to switch all the django.
* The JS stubs can play well with application's usual JavaScript.


## Use

Please refer to [web page](http://icanberk.github.io/django-interactive) for now.

## Examples

We have provided a sample Todo application implemented using this library in the `example/` directory. 

Please especially look at `todo.js` for implementations.

We were able to implement lots of AJAX capability with couple lines.


## Installing


```
	pip install django-interactive
```


In `settings.py`, add `django-interactive` to your installed apps.

```
INSTALLED_APPS = (
    ...
    'interactive',
    ...
)
```

## Contributors

* Ilter Canberk
* Naman Seth

## License

The project is released under the [MIT License](http://opensource.org/licenses/mit-license.php).

