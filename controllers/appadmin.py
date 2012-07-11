# -*- coding: utf-8 -*-
items_per_page = 20
def index():
    return dict()

def photo():
    return dict()
                    
def loadAlbums():
    items = []  
    albums = photo_service.GetUserFeed(user='default')
    for entry in albums.entry:         
      items.append(LI(
                   DIV(
                   IMG(_src=entry.media.thumbnail[0].url), 
                   DIV(H5(entry.media.title.text),
                       P(entry.numphotos.text + ' foto'),
                       P(
                           A(I(_class='icon-trash'),"Delete", _href='#', _class='btn btn-small',_id='btn_delete_album',_name=entry.gphoto_id.text),
                           A(I(_class='icon-folder-open'),"Open", _href='#', _class='btn btn-small',_id='btn_open_album',_name=entry.gphoto_id.text)),
                   _class='caption'), 
                    _class='span2'), 
                   _class='thumbnail albumthumb',_id=entry.gphoto_id.text))       
                              
    return UL(*items, _class='thumbnails')
    
def newAlbum():
    try:
        albumTitle = str(request.vars.newAlbumTitle)
        photo_service.InsertAlbum(title=albumTitle, summary='This is an album')
        return loadAlbums()
    except: return Exception, str(error)    
        
def deleteAlbum():
    albums = photo_service.GetUserFeed(user='default')
    id_to_delete = request.vars.album_id
    for entry in albums.entry:
        if entry.gphoto_id.text == id_to_delete:
            photo_service.Delete(entry);
            return "deleted"
    return "album nout found"

def loadAlbumPhotos():
    album_id = request.vars.album_id;
    photos = photo_service.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album_id))
    items = []
    for photo in photos.entry:
     url = photo.media.thumbnail[0].url   
     crop_str = '/s125-c/'
     img_title = url.rsplit('/', 1)[1]
     rest_url = url.rsplit('/', 2)[0]
     img_url = rest_url+crop_str+img_title     
     items.append(LI(A(IMG( _src=img_url, _alt=''),_album_id=album_id, _photo_id=photo.gphoto_id.text, _href='#', _url=photo.content.src, _class='thumbnail photo_thumb'), _class='span2', _id=photo.gphoto_id.text))
    
    return DIV(UL(*items, _class='thumbnails'),_id='images_grid')
        
    
def uploadPhoto():    
    items = []  
    albums = photo_service.GetUserFeed(user='default')
                        
    form=FORM( 
         DIV(LABEL('Select image',_for='image'),DIV(INPUT(_name='image', _type='file', _id='inputfile', _accept='.jpg,png,jpeg,bmp') ,_class='input'),_class='clearfix'),    
         DIV(LABEL('Select Album',_for='stackedSelect'),
         DIV(
             SELECT([(OPTION(entry.media.title.text, _value=entry.gphoto_id.text,))for entry in albums.entry], _name='stackedSelect',_id='stackedSelect'),
                     _class='input'),
             _class='clearfix'),
         DIV(INPUT(_type='submit',_value='Upload',_class='btn',_id="submit_btn")),_class='well')
    
    if form.accepts(request.vars):
            album_id = request.vars.stackedSelect
            album_url = '/data/feed/api/user/default/albumid/%s' % album_id
            file_obj = request.vars.image.file
            filename = str(request.vars.image.filename)
            photo = photo_service.InsertPhotoSimple(album_url, filename,filename, file_obj, content_type='image/jpeg')
            redirect(URL('photo'))          
    return dict(form=form)   
         
def deletePhoto():
    photo_id = request.vars.photo_id
    album_id = request.vars.album_id
    photos = photo_service.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album_id))
    for entry in photos.entry:
        if entry.gphoto_id.text == photo_id:
            photo_service.Delete(entry);
            return "deleted"
    return "album nout found"

def video():
   import math
   import urllib   
   from xml.dom.minidom import parse
   
   uri = 'https://gdata.youtube.com/feeds/api/users/TheZerooo123/uploads?start-index=1&max-results=1'
   videolist = yt_service.GetYouTubeVideoFeed(uri) 
   dom = parse(urllib.urlopen(uri))
   dom.toxml()
   nodes = dom.getElementsByTagName('openSearch:totalResults')
  
   total_entries = [(node.firstChild.nodeValue) for node in nodes]
   total_pages=int(math.ceil((int(total_entries[0])+0.0)/items_per_page))
   
   return dict(total_pages=total_pages)

def setVideoTitle():
    form = FORM(
    INPUT(_type='text',_name='videotitle',_id='videotitle'),
    INPUT(_type='submit', _value='Next',_class='btn'),
    _action=URL('uploadVideo'),_class='well form-search')    
    return dict(form=form)
    
def uploadVideo():
    # create media group as usual  
    if request.vars.videotitle:
        video_title = str(request.vars.videotitle);     
        my_media_group = gdata.media.Group(
          title=gdata.media.Title(text=video_title),
          description=gdata.media.Description(description_type='plain',text='My description'),
          category=[gdata.media.Category(
              text='Autos',
              scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
              label='Autos')],
          player=None
        )   
        # create video entry as usual
        video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group)
        
        # upload meta data only
        response = yt_service.GetFormUploadToken(video_entry)
        
        # parse response tuple and use the variables to build a form (see next code snippet)
        post_url = response[0]
        youtube_token = response[1]
        next = 'http://89.28.110.232:8000/picasa/appadmin/video'
        form=FORM(INPUT(_name='file',_type='file'), 
                  INPUT(_name='token',_type='hidden', value=youtube_token), 
                  INPUT(_value='Upload', _type='submit'))          
        form.update(_action=post_url+"?nexturl="+next)    
        return dict(form=form)
    else:
        redirect(URL('setVideoTitle'))
        
def deleteEntry():    
    video_id = str(request.vars.video_id)
    uri = 'https://gdata.youtube.com/feeds/api/users/default/uploads/%s' % (video_id)  
    try:
     entry = yt_service.GetYouTubeUserEntry(uri=uri)
    except Exception, err: return str(err)
    response = yt_service.DeleteVideoEntry(entry)
    if response: return "acest video a fost sters"
    else: return "try again latter"
   


def printEntries():
    try:
        start_index = int(request.vars.page_index)*20-19;
    except:
        start_index = 1;
   
    uri = 'https://gdata.youtube.com/feeds/api/users/default/uploads?start-index='+str(start_index)+'&max-results='+str(items_per_page)
    videolist = yt_service.GetYouTubeVideoFeed(uri)     
    items = [] 
   
    for entry in videolist.entry:         
   #    upload_status = yt_service.CheckUploadStatus(entry)
       status = ''
     
   #    if upload_status is not None:
   #       status = upload_status[0]+'('+upload_status[1]+')'       
       items.append(
        LI(
           DIV(
               IMG(_alt='',_src=entry.media.thumbnail[1].url, _class='pull-left'),
               DIV( 
                   H5(entry.media.title.text),                  
                   P(A(I(_class='icon-trash icon-white'),"Delete",_class='btn btn-small btn-danger delete_btn', _name=entry.id.text.split('/')[-1]),
                     A(I(_class='icon-facetime-video'),'Play',**{'_data-toogle':'modal', '_href':'#myModal','_class':'btn btn-small play','_name':entry.id.text.split('/')[-1]}) 
                    ),
                   P( SPAN(str(int(entry.media.duration.seconds)/60) +':'+str(int(entry.media.duration.seconds) % 60)+' '),
    #                  SPAN(str(status),_class='label label-important')
                    ),
                _class='caption pull-right', _style='width: 250px'), 
            _class='thumbnail-horiz thumbnail'), 
        _id=entry.id.text.split('/')[-1], _class='span6')
                    ) 
                      
    return UL(*items, _class='thumbnails')
    
def download():
    return response.download(request,db)
