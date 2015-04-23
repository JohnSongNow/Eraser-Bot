import requests
import RiotConstants as Consts


class RiotAPI():

    def __init__(self, api_key, region=Consts.REGIONS["north_america"]):
        '''
        (RiotAPI, Str, [Str]) -> NoneType
        Initializes a new RiotAPI.
        '''
        self.api_key = api_key
        self.region = region


    def _request(self, api_url, params=dict()):
        '''
        (RiotAPI, Str, Dict()) -> Str (JSON Format)
        Returns a JSON result based on the api_url inpited
        and the aprams. Note that the if the _requests is invalid
        a value of None will be returned instead.
        '''
        args = {'api_key': self.api_key}
        # Looping through the keys
        for key, value in params.items():
            if key not in args:
                args[key] = value

        # Our request lnie
        line = Consts.URL['base'].format(
                proxy = self.region,
                region = self.region,
                url = api_url
                )
        print(line)
        # Getting the response from the server
        # based on our URL, REGION and BASE
        response = requests.get(line, params=args)
        # Catching any bad foramts os errors with the response
        print(response)
        try:
            return response.json()
        except Exception:
            return None

    def _request_global(self, api_url, params=dict()):
            '''
            (RiotAPI, Str, Dict()) -> Str (JSON Format)
            Returns a JSON result based on the api_url inpited
            and the aprams. Note that the if the _requests is invalid
            a value of None will be returned instead.
            '''
            args = {'api_key': self.api_key}
            # Looping through the keys
            for key, value in params.items():
                if key not in args:
                    args[key] = value

            # Our request lnie
            line = Consts.URL['base_global'].format(
                    region = self.region,
                    url = api_url
                    )
            # Getting the response from the server
            # based on our URL, REGION and BASE
            response = requests.get(line, params=args)
            # Catching any bad foramts os errors with the response
            print(response)
            try:
                return response.json()
            except Exception:
                return None

    def get_summoner_by_name(self, name):
        '''
        (Self, Str) -> Str (JSON
        Returns a JSON respresentation of the summoner
        based on their name, note that a value of None
        wil be returned if the requests is invalid.
        '''
        # Generating the url based on the name
        api_url = Consts.URL['summoner_by_name'].format(
            version = Consts.API_VERSIONS['summoner'],
            names = name
            )
        return self._request(api_url)


    def get_summoner_match_history(self, summonerID, params={}):
        '''
        (Self, Str) -> Str (JSON
        Returns a JSON respresentation of this summoner's
        match history
        '''
        # Generating the url based on the name
        api_url = Consts.URL['match_history'].format(
            version = Consts.API_VERSIONS['match_history'],
            summonerId = summonerID
            )
        return self._request(api_url, params)


    def get_runepages(self, summonerID, params={}):
        '''
        (Self, Str) -> Str (JSON
        Returns a JSON respresentation of this summoner's
        match history
        '''
        # Generating the url based on the name
        api_url = Consts.URL['runes'].format(
            version = Consts.API_VERSIONS['runes'],
            summonerIds = summonerID
            )
        return self._request(api_url, params)

    def get_current_runes(self, ID):
        '''
        '''
        runepages = self.get_runepages(ID)
        for runepage in runepages[str(ID)]['pages']:
            if(runepage['current'] == True):
                print(runepage)


    def get_static_data_runes(self, region="north_america", params={}):
        '''
        (Self, Str) -> Str (JSON
        Returns a JSON respresentation of this summoner's
        match history
        '''
        # Generating the url based on the name
        api_url = Consts.URL['static_data_runes'].format(
            version = Consts.API_VERSIONS['static_data'],
            region = Consts.REGIONS[region]
            )
        print(api_url)
        return self._request_global(api_url, params)


class RiotFormatter():


    def __init__(self, my_api):
        self.runes_info = my_api.get_static_data_runes()


    def format_runepage(self, runepage):
        '''
        (RiotFormatter, str)
        Represents a clean str representation of the current runepage
        '''

    def get_api(self):
        '''
        (RiotFormatter) -> RiotAPI
        '''

if __name__ == '__main__':
    my_api = RiotAPI('b4a70e9e-748e-44f7-85ea-bef1b5ea62ca')
    my_formatter = RiotFormatter(my_api)
    #print(my_api.get_summoner_by_name('TheCheeseyGamer'))
    current_runepage = my_formatter.format_runepage(my_api.get_current_runes(21222532))
