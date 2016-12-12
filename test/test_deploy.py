from helpers import *


def test_deploy(app):
    run(["config"])
    run(["deploy"])
    assert rails("Deployment.all.first.app.name") == app
    assert rails("Build.all.first.app.name") == app