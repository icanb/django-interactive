from django.template import Context, Template

class StubGenerator(object):

    def __init__(self, subviews):
        self.subviews = subviews


    def generate_html_method(self, subview_name):
        skeleton = """
            Stub.{{ subview_name }}_html = function() {
                console.log("HTML");
                $.ajax({
                  type: "GET",
                  url: "/interactive/{{ subview_name }}/html/",
                  complete: function(data) {
                    console.log(data)
                  }
                });
            }
        """

        t = Template(skeleton)
        c = Context({"subview_name": subview_name})
        js_string = t.render(c)


        return js_string


    def generate_json_method(self, subview_name):
        skeleton = """
            Stub.{{ subview_name }}_json = function() {
                console.log("HTML");
                $.ajax({
                  type: "GET",
                  url: "/interactive/{{ subview_name }}/json/",
                  complete: function(data) {
                    console.log(data.responseJSON)
                  }
                });
            }
        """

        t = Template(skeleton)
        c = Context({"subview_name": subview_name})
        js_string = t.render(c)

        return js_string


    def generate_reload_method(self, subview_name):
        skeleton = """
            Stub.{{ subview_name }}_reload = function() {
                console.log("HTML");
                $.ajax({
                  type: "GET",
                  url: "/interactive/{{ subview_name }}/reload/",
                  complete: function(data) {
                    console.log(data)
                  }
                });
            }
        """

        t = Template(skeleton)
        c = Context({"subview_name": subview_name})
        js_string = t.render(c)

        return js_string


    def generate_javascript(self):
        all_string = "var Stub = {};"

        for subview in self.subviews.keys():
            all_string += self.generate_html_method(subview)
            all_string += self.generate_json_method(subview)
            all_string += self.generate_reload_method(subview)

        return all_string

