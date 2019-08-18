import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        return cherrypy.request.json["name"]

cherrypy.quickstart(HelloWorld())