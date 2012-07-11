# coding: utf8
import gdata.photos.service
import gdata.media
import gdata.photos
import gdata.geo
import gdata.youtube
import gdata.youtube.service

photo_service = gdata.photos.service.PhotosService()
photo_service.email = 'zerooo123@gmail.com'
photo_service.password = '**********'
photo_service.source = 'client id'
photo_service.ProgrammaticLogin()

yt_service = gdata.youtube.service.YouTubeService()
yt_service.email = 'zerooo123@gmail.com'
yt_service.password = '**********'
yt_service.source = 'moaradepiatra'
yt_service.developer_key = 'api key'
yt_service.client_id = 'client id'
yt_service.ProgrammaticLogin()
# coding: utf8
