from googleapiclient.discovery import build


def scrap(link, garbage):
    if link[0:4] == "www.":
        link = link[4:]
    if link[-4::] == ".com":
        link =  link[0:-4]

    if link in garbage.keys():
        garbage[link] += 1
    else:
        garbage[link] = 1


def searching(query):
    api_key = "AIzaSyBLVDk1uPI7Y0uY13V3D-3zarwDsEXvx7g"
    cse_key = "51dc0711ee7b871cf"

    start_index = 1
    garbage = {}

    resource = build("customsearch", 'v1', developerKey=api_key).cse()
    result = resource.list(q=query, cx=cse_key).execute()

    for j in result['items']:
        scrap(j['displayLink'], garbage)

    totalResults = int(result['queries']['request'][0]['totalResults'])
    print(totalResults)

    while start_index + 10 < totalResults and start_index + 10 <= 100:
        start_index += 10
        result = resource.list(q=query, cx=cse_key, start=start_index).execute()

        for j in result['items']:
            scrap(j['displayLink'], garbage)

    print(garbage)


searching("Оникс")
