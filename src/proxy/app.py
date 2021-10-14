import falcon
from proxy.resources import CommnunityResource, WebAppResource, RecordResource, FileResource, WebAppResourceRDFXML

#api = falcon.API()
app = falcon.App()
app.add_route('/fdp/', WebAppResource())
app.add_route('/catalogs/', CommnunityResource())
app.add_route('/catalogs/{_id}', CommnunityResource())
app.add_route('/datasets/', RecordResource())
app.add_route('/datasets/{_id}', RecordResource())
app.add_route('/distributions/{_id}', FileResource())
app.add_route('/rdfxml/fdp/', WebAppResourceRDFXML())
