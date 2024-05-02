import webview
url=input("enter URL")
w=webview.create_window("site to GUI",url)
webview.start()