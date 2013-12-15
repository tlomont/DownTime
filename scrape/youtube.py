import requests
from db_connect import Item
        
def search_youtube(query):    
    search_url = "https://gdata.youtube.com/feeds/api/videos?alt=json"
    #id_start = len('http://gdata.youtube.com/feeds/api/videos/')
    response = requests.get(search_url, params={"q":query})
    #print response.url
    #print str(response.text)
    response = response.json()
    videos = response["feed"]["entry"]
    """vid_ids_long = [video["id"]["$t"] for video in videos]
    vid_ids = [vid_id[id_start:] for vid_id in vid_ids_long]
    api_url_base = "https://www.googleapis.com/youtube/v3/videos?id="
    api_urls = [api_url_base + vid_id + "&key=AIzaSyCQ5Zw_FlMQgu_tGN559nqpEZ4Dx0PPPXQ&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics" for vid_id in vid_ids]
    l_items = len(api_urls)
    for i in xrange(0,l_api_urls): # build my fucking items
        api_url = vid_urls[i]
        item = Item()
        item.tags = []
        response = requests.get(api_url).json()
        items.add_tag(videos[i]["category"][1]["term"])
        item.name = response["items"]["title"]
        item.duration = response["items"]["contentDetails"]["duration"] # Warning google is returning duration in this bullshit-ass form: PT29S
        item.
    """
    items = []
    for video in videos:
        # Lets get the title
        title = video["title"]["$t"]
        # Now lets get tags
        tag = video["category"][1]["term"]
        # We need to contact another api to get the length
        vid_id_long = video["id"]["$t"]
        id_start = len('http://gdata.youtube.com/feeds/api/videos/')
        api_url_base = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails%2Cstatistics&key=AIzaSyCQ5Zw_FlMQgu_tGN559nqpEZ4Dx0PPPXQ"
        vid_id = vid_id_long[id_start:]
        #api_url = api_url_base + vid_id + "&key=AIzaSyCQ5Zw_FlMQgu_tGN559nqpEZ4Dx0PPPXQ&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics"
        response = requests.get(api_url_base, params={"id": vid_id})
        response = response.json()
        duration = response["items"][0]["contentDetails"]["duration"] # Warning google is returning duration in this bullshit-ass form: PT5M29S
        url = "https://www.youtube.com/watch?"+vid_id
        item = Item()
        item.duration = duration
        item.name = title
        item.add_tag(tag)
        item.url = url
        items.append(item)
    return items

# if __name__=='__main__':
#     items = search_youtube("mongodb is webscale")
#     fp = open('response.txt', 'w')
#     map(lambda item: fp.write(item.name.encode('utf-8'))+'\n', items)


    
    
