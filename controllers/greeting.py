import views.greeting

class Greeting:


    # The constructor for the class. It takes the channel name as the a 
    # parameter and then sets it as an instance variable
    def __init__(self, app):
        @app.event("app_mention")
        def app_mention(client, event):
            view = views.greeting.render_greeting_view()
            #say(blocks=view['blocks'])
            client.chat_postEphemeral(
                channel=event["channel"],
                user=event['user'],
                blocks=view['blocks'],
                text="Sup?"
            )

        @app.event("app_home_opened")
        def handle_app_home_opened_events(client, event):
            view = views.greeting.render_greeting_view()
            view['type']="home"
            client.views_publish(
                user_id=event['user'],
                view=view)


