<!--- For use with https://github.com/ogom/sublimetext-markdown-slideshow  -->
Introduction to Django
======================

Randall Ma

AHS Software Development Club 2012

---

### What is Django?

* Django is a web framework for Python.
* Django lets you build dynamic websites (with server-side programming logic) easily and quickly.
* Django is easy to learn.
* Django has been used to build many high profile websites (example: onion.com).

---

### How does Django work?

Django is an MVC (model/view/controller) framework, which means it has a standardized structure (though it uses different names than other frameworks, so don't get confused). Using Django's terms:

**Model**: A class used to describe an object you would put into a database. For example: if you were creating a blog, one of your models might be "Post", or "Author".

**View**: A function called whenever HTTP is used to hit a server with information (i.e. a computer sending data to a server). You would likely use one view for "show home page", one for "show blog post", one for "post blog post", and so on for all the functions of your blog you wish to interact with via the web.

**Template**: An HTML template you can project information onto.

---

Most functions of a web site can be setup to take place in an order like this:

1. User goes to page on website. Server does everything in the appropriate view...
2. ...like fetching the contents of a blog post from an instance of a model.
3. It will then pass that information onto the template, which the user sees.