class Translation(object):
    
    START_TXT = """ <b><i> Hi {} ,
 Wait a second, why would I say Hi to you?</b>
<b>It's not like you will need some help to use me !</i></b>\n 
"""
    PROGRESS_BAR = """\n
β­βββ[**πProgress Barπ**]ββββ
β
β<b>π : {1} | {2}</b>
β
β<b>π : {0}%</b>
β
β<b>β‘ : {3}/s</b>
β
β<b>β±οΈ : {4}</b>
β°ββββββββββββββββββ"""
    HELP_TXT = """
<b><i><u>β¨ AVAILABLE COMMANDS:</u> 
β’ /rename - To rename a file or video or audio
β’ /settings - To configure your configs 
β’ /addcaption - To add a custom caption
β’ /showcaption - To show your custom caption
β’ /deletethumb - To remove your custom thumbnail 
β’ /showthumb - To show your custom thumbnail
<u>π₯ FEATURES:</u>
β» support custom caption
β» support custom thumbnail 
β» Available three upload mode  
β» support broadcast</i></b>
<b><i><u>β¨ For Url Upload:</u>
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots</i></b>


""" 
    OWNER_COMMANDS_TXT = """
<b><i><u>π¨ OWNER COMMANDS:</u>

β’ Following commands only can use bot owner.

β’ /ban - To ban a user 
β’ /unban - To unban a user 
β’ /stats - To get bot users stats
β’ /broadcast - To broadcast messages to users</i></b>
"""
    ABOUT_TXT = """
ββββββ° RENAME BOT β±βββ±βΫͺΫͺ
ββ­ββββββββββββββββ£
ββ£βͺΌπΚα΄α΄ : [{}](https://t.me/{})
ββ£βͺΌπ¦Deployer : [huhh!!! Don't get full of yourself](https://t.me/Xzamael)
ββ£βͺΌπ‘Κα΄sα΄α΄α΄ α΄Ι΄ : Koyeb
ββ£βͺΌπ£οΈΚα΄Ι΄Ι’α΄α΄Ι’α΄ : α΄Κα΄Κα΄Ι΄3
ββ£βͺΌπΚΙͺΚΚα΄ΚΚ : α΄ΚΚα΄Ι’Κα΄α΄ α΄sΚΙ΄α΄Ιͺα΄ {} 
ββ£βͺΌποΈα΄ α΄ΚsΙͺα΄Ι΄ : {}
ββ°ββββββββββββββββ£
βββββββββββββββββββββ±βΫͺΫͺ
"""
    
    THUMBNAIL_TXT = """
<b>πΌοΈ CUSTOM THUMBNAIL</b>

you can add custom thumbnail simply by sending a photo to me 
"""
    CUSTOM_CAPTION_TXT = """
<b>π CUSTOM CAPTION</b>

β’ /addcaption <your caption> - To add your custom caption 

<b>AVAILABLE FILLINGS:</b>
β’ `{filename}` - new file name
β’ `{size}` - size of the media
β’ `{duration}` - duration of the media
"""
    SETTINGS_TXT = "<b><u>βοΈ SETTINGS</u>\nConfigure your settings using this buttons</b>"
    BANNED_TXT = "<b>Sorry dude, You would be banned from using me</b>"
    DOWNLOAD_START_TXT = "<b>Downloading To My server !!</b>"
    UPLOAD_START_TXT = "<b>Uploading into telegram</b>"
    UPLOAD_SUCCESS_TXT = "<b>Thank you for Using Me β€οΈ</b>"
    NEW_CUSTOM_THUMB_TXT = "βοΈ Thumbnail Successfully Added"
    REMOVE_CUSTOM_THUMB_TXT = "ποΈ Thumbnail Successfully Removed"
    DOWNLOAD_SUCCESS_TXT = "<b>Media Downloded successfully π</b>"
    THUMB_NOT_FOUND_TXT = "Didn't found any thumbnail yet"
    REPLY_MEDIA_TXT = "<b>Please Reply To An File or video or audio With filename & extension</b>"



    # change to urlup
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "Now Downloading.."
    UPLOAD_START = "Now Uploading.."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @xurluploaderbot)"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@xurluploaderbot"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "β Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /genthumbnail to a media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
