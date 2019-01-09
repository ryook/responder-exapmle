import responder


hello = responder.API()


@hello.route("/{who}")
def hello_world_user(req, resp, *, who):
    resp.text = f"hello, {who}!"


@hello.route("/{who}/json")
def hello_world_user_json(req, resp, *, who):
    resp.media = {"action": "hello", "name": who}


@hello.route("/{who}/html")
def hello_world_user_json(req, resp, *, who):
    resp.content = hello.template("index.html", who=who)


