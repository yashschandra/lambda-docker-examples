from html2image import Html2Image

def handler(event, context):
    print(event)
    hti = Html2Image()
    print(hti.browser.flags)
    return "it works"