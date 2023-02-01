from jinja2 import Environment, FileSystemLoader
from .utils import get_view_ids
import json
from .greeting import ondemand_env_main_view, generic_action


# Main view
get_env_status_view = "get_env_status_view"
get_all_envs_view   = "get_all_envs_view"
create_env_view    = "create_env_view"
# Blocks
env_name_input     = "env_name_input"
env_hostname_input = "env_hostname_input"
env_db_name_input   = "env_db_name_input"
env_image_tag_input = "env_image_tag_input"

environment = Environment(loader=FileSystemLoader("views/ondemand_env_forms"))

def render_ondemand_env_main_view() -> dict:

    args = {
		"create_env_block":     get_view_ids(ondemand_env_main_view, create_env_view, "block"),
		"create_env_action":     get_view_ids(ondemand_env_main_view, create_env_view, generic_action),
		"get_env_status_block":     get_view_ids(ondemand_env_main_view, get_env_status_view, "block"),
		"get_env_status_action":     get_view_ids(ondemand_env_main_view, get_env_status_view, generic_action),
		"get_all_envs_block":     get_view_ids(ondemand_env_main_view, get_all_envs_view, "block"),
		"get_all_envs_action":    get_view_ids(ondemand_env_main_view, get_all_envs_view, generic_action),

    }
    template = environment.get_template("main/main_form.json")
    return json.loads(template.render(args))




def render_ondemand_env_get_env_status_view() -> dict:

    args = {
		"name_input_block":     get_view_ids(ondemand_env_main_view, env_name_input, "block"),
		"name_input_action":     get_view_ids(ondemand_env_main_view, env_name_input, generic_action),
    }
    template = environment.get_template("getEnvStatus/getEnvStatusRequestForm.json")
    return json.loads(template.render(args))




def render_ondemand_env_get_env_status_submit(env_name, env_status) -> dict:

    # get env status from k8s
    args = {
		"env_name":     env_name,
		"env_status":     env_status,
    }
    template = environment.get_template("getEnvStatus/getEnvStatusResponseForm.json")
    return json.loads(template.render(args))

