c = get_config()
c.ContentsManager.root_dir = "/root/"
c.NotebookApp.allow_root = True
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
# Comment out this line or first hash your own password
#c.NotebookApp.password = u'sha1:1234567abcdefghi'
c.ContentsManager.allow_hidden = True
