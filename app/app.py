import time

import responder

from hello import hello
from method import method_test


api = responder.API()

api.mount("/hello", hello)
api.mount("/method", method_test)


@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


@api.route("/400")
def teapot(req, resp):
    resp.status_code = api.status_codes.HTTP_400


@api.route("/incoming")
async def receive_incoming(req, resp):

    @api.background.task
    def process_data(data):
        time.sleep(3)
        print("done")
        print(data)

    data = await req.media()

    process_data(data)

    resp.media = {"success": True}

@api.route("/ramune")
class ramuneResource:

    async def on_get(self, req, resp):
        resp.media = {"ramune": 1}

    def on_post(self, req, resp):
        resp.status_code = api.status_codes.HTTP_403

    async def on_put(self, req, resp):
        data = await req.media()
        resp.media = data




if __name__ == "__main__":
    api.run(debug=True)
