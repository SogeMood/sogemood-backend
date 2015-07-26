import endpoints

WEB_CLIENT_ID = '685692840755-r5hds0qsptostdpampbekve1strudr8g.apps.googleusercontent.com'

secured_api = endpoints.api(name='secured',
                            version='v1',
                            allowed_client_ids=[
                                WEB_CLIENT_ID,
                                endpoints.API_EXPLORER_CLIENT_ID],
                            scopes=[endpoints.EMAIL_SCOPE],
                            package_path='secured',
                            description="Secured SogeMood API")
