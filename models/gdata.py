# coding: utf8
import gdata.photos.service
import gdata.media
import gdata.photos
import gdata.geo
import gdata.youtube
import gdata.youtube.service

photo_service = gdata.photos.service.PhotosService()
photo_service.email = 'zerooo123@gmail.com'
photo_service.password = 'ctrlsoft0811TD'
photo_service.source = 'moaradepiatra'
photo_service.ProgrammaticLogin()

yt_service = gdata.youtube.service.YouTubeService()
yt_service.email = 'zerooo123@gmail.com'
yt_service.password = 'ctrlsoft0811TD'
yt_service.source = 'moaradepiatra'
yt_service.developer_key = 'AI39si6mLBFZSZtY12iSVA7t7RL2vfnnq508tUqYD_W02dUYEpMpuYzlTmFDaF5lPhq32Xw9rm4WXaldyLn3Sn6YT6mM0qm6aA'
yt_service.client_id = 'moaradepiatra'
yt_service.ProgrammaticLogin()
# coding: utf8
