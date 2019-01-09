import responder


method_test = responder.API()


@method_test.route("/ramune")
class ramuneResource:

    def on_get(self, req, resp):
        resp.media = {"ramune": 1}

    def on_put(self, req, resp):
        data = req.media()
        resp.media = data

