#!/usr/bin/env python3

import urllib.request
import json

dc_url = 'http://datacenters-api.va.3sca.net/datacenters/'
s_url = 'http://servers-api.va.3sca.net/servers/'
user = '3scale'
pwd = '3scale'
realm = 'Password required'

def server(id_server):
    '''
    Get information for the server specified
    :param: id_server
    :return: s_data
    '''
    s_auth_handler = urllib.request.HTTPBasicAuthHandler()
    sid_url = s_url + id_server\
    #+ '.json'

    s_auth_handler.add_password(realm = realm, uri = sid_url, user = user,passwd = pwd)
    s_opener = urllib.request.build_opener(s_auth_handler)
    urllib.request.install_opener(s_opener)
    notFound = False
    try:
        s_response = urllib.request.urlopen(sid_url)
    except urllib.error.HTTPError as e:
        notFound = True

    if not notFound:
        encoding = s_response.info().get_param('charset', 'utf8')
        s_data = json.loads(s_response.read().decode(encoding))
    else:
        s_data = {'name':'not found', 'description':'unknown'}

    return s_data

def datacenters():
    '''
    Get all datacenters information
    :return: dc_data
    '''
    # Get datacenters json
    dc_auth_handler = urllib.request.HTTPBasicAuthHandler()
    dc_auth_handler.add_password(realm = realm, uri = dc_url, user = user,passwd = pwd)
    dc_opener = urllib.request.build_opener(dc_auth_handler)
    urllib.request.install_opener(dc_opener)
    dc_response = urllib.request.urlopen(dc_url)
    encoding = dc_response.info().get_param('charset', 'utf8')
    dc_data = json.loads(dc_response.read().decode(encoding))

    return dc_data

def main():
    ## Get all datacenters data
    dc_data = datacenters()

    ## Get data for each datacenter
    for datacenter in dc_data:
        print ("- Datacenter: " + datacenter['name'])
        servers_list = datacenter['servers'].split(',')
        print ("\t- Servers:")
        for id_server in servers_list:
            ## Get data for id_server
            s_data = server(id_server)
            print ("\t\t- " + s_data['name'] + ": " + s_data['description'])

if __name__ == '__main__':
    main()
