from jinja2 import Environment, FileSystemLoader
from .utils import get_view_ids
import json


# Main view
greeting_view = "greeting_view"
# Blocks
ondemand_env_main_view = "ondemand_env_main_view"
stress_test_main_view = "stress_test_main_view"
# Actions
generic_action = "action"

environment = Environment(loader=FileSystemLoader("views/greeting_forms"))

def render_greeting_view() -> str:
    args = {
        "ondemand_env_block": get_view_ids(greeting_view, ondemand_env_main_view, "block"),
        "ondemand_env_action": get_view_ids(greeting_view, ondemand_env_main_view, generic_action),
        "stress_test_block": get_view_ids(greeting_view, stress_test_main_view, "block"),
        "stress_test_action": get_view_ids(greeting_view, stress_test_main_view, generic_action),
    }
    template = environment.get_template("greeting_form.json")
    return json.loads(template.render(args))

