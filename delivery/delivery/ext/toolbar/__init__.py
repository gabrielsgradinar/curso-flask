from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    DebugToolbarExtension(app)

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER_ENABLED"] = True
