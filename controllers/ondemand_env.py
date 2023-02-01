from views.greeting import greeting_view, generic_action
from views.utils import get_view_ids
import views.ondemand_env
import drivers.ondemand_env



class OndemandEnv:
    def __init__(self,app):
        ### Main
        @app.action(get_view_ids(greeting_view, views.ondemand_env.ondemand_env_main_view, generic_action))
        def ondemand_env_main_view(ack, body, client):
            ack()
            client.views_open(
                trigger_id=body["trigger_id"],
                view=views.ondemand_env.render_ondemand_env_main_view()
            )
            return


        ### Get env status
        @app.action(get_view_ids(views.ondemand_env.ondemand_env_main_view, views.ondemand_env.get_env_status_view, generic_action))
        def ondemand_env_get_env_status_view(ack, body, client):
            ack()
            client.views_update(
                view_id=body["view"]["id"],
                view=views.ondemand_env.render_ondemand_env_get_env_status_view()
            )
            return  


        @app.view("get_env_status_submit")
        def ondemand_env_get_env_status_submit(ack, body, client):
            ack()
            env_name = body['view']['state']['values'][
                get_view_ids(views.ondemand_env.ondemand_env_main_view, views.ondemand_env.env_name_input, "block")][
                    get_view_ids(views.ondemand_env.ondemand_env_main_view, views.ondemand_env.env_name_input, generic_action)]['value']
            env_status = drivers.ondemand_env.get_ondemand_env_status(env_name)
            client.chat_postMessage(
                channel=body['user']['id'],
                blocks=views.ondemand_env.render_ondemand_env_get_env_status_submit(env_name, env_status)['blocks'],
                text="Sup?"
            )
            return
        

