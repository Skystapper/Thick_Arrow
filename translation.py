class Translation(object):
    
    START_TXT = """ <b><i> Hi {} ,
 Wait a second, why would I say Hi to you?</b>
<b>It's not like you will need some help to use me !</i></b>\n 
"""
    PROGRESS_BAR = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│
├<b>📁 : {1} | {2}</b>
│
├<b>🚀 : {0}%</b>
│
├<b>⚡ : {3}/s</b>
│
├<b>⏱️ : {4}</b>
╰─────────────────⍟"""
    HELP_TXT = """
<b><i><u>✨ AVAILABLE COMMANDS:</u> 
➢ /rename - To rename a file or video or audio
➢ /settings - To configure your configs 
➢ /addcaption - To add a custom caption
➢ /showcaption - To show your custom caption
➢ /deletethumb - To remove your custom thumbnail 
➢ /showthumb - To show your custom thumbnail
<u>🔥 FEATURES:</u>
➻ support custom caption
➻ support custom thumbnail 
➻ Available three upload mode  
➻ support broadcast</i></b>
<b><i><u>✨ For Url Upload:</u>
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots</i></b>


""" 
    OWNER_COMMANDS_TXT = """
<b><i><u>👨 OWNER COMMANDS:</u>

• Following commands only can use bot owner.

➢ /ban - To ban a user 
➢ /unban - To unban a user 
➢ /stats - To get bot users stats
➢ /broadcast - To broadcast messages to users</i></b>
"""
    ABOUT_TXT = """
╔════❰ RENAME BOT ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : [{}](https://t.me/{})
║┣⪼👦Deployer : [huhh!!! Don't get full of yourself](https://t.me/Xzamael)
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : Koyeb
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ {} 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : {}
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
    
    THUMBNAIL_TXT = """
<b>🖼️ CUSTOM THUMBNAIL</b>

you can add custom thumbnail simply by sending a photo to me 
"""
    CUSTOM_CAPTION_TXT = """
<b>📝 CUSTOM CAPTION</b>

➢ /addcaption <your caption> - To add your custom caption 

<b>AVAILABLE FILLINGS:</b>
• `{filename}` - new file name
• `{size}` - size of the media
• `{duration}` - duration of the media
"""
    SETTINGS_TXT = "<b><u>⚙️ SETTINGS</u>\nConfigure your settings using this buttons</b>"
    BANNED_TXT = "<b>Sorry dude, You would be banned from using me</b>"
    DOWNLOAD_START_TXT = "<b>Downloading To My server !!</b>"
    UPLOAD_START_TXT = "<b>Uploading into telegram</b>"
    UPLOAD_SUCCESS_TXT = "<b>Thank you for Using Me ❤️</b>"
    NEW_CUSTOM_THUMB_TXT = "✔️ Thumbnail Successfully Added"
    REMOVE_CUSTOM_THUMB_TXT = "🗑️ Thumbnail Successfully Removed"
    DOWNLOAD_SUCCESS_TXT = "<b>Media Downloded successfully 🎉</b>"
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
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /genthumbnail to a media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
