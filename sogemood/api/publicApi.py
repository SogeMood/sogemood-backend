import endpoints

WEB_CLIENT_ID = '685692840755-r5hds0qsptostdpampbekve1strudr8g.apps.googleusercontent.com'

public_api = endpoints.api(name='public',
                           version='v1',
                           package_path='public',
                           description="Public SogeMood API")
