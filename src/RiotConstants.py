URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',

    'base_global': 'https://global.api.pvp.net/api/lol/{url}',

    # Reserverd for Summoners
    'summoner_by_name' : 'v{version}/summoner/by-name/{names}',

    # Reserverd for Match History
    'match_history' : 'v{version}/matchhistory/{summonerId}',

    'runes' : 'v{version}/summoner/{summonerIds}/runes',

    'static_data_runes' : 'static-data/{region}/v1.2/rune'
}

API_VERSIONS = {
    'summoner': 1.4 ,
    'match_history': 2.2,
    'champion': 1.2,
    'runes': 1.4,
    'static_data': 1.2
}

REGIONS = {
    'north_america': 'na',
    'eurpose_west': 'euw',
    'global' : 'global',
    'none' : ''
}