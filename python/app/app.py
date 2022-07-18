from htmlwebshot import WebShot
import boto3

def handler(event, context):
    shot = WebShot()
    with open('/tmp/content.html', 'w+') as htmlfile:
        htmlfile.write(event['html_str'])
    shot.create_pic(html='/tmp/content.html', output="/tmp/picture.jpg")
    s3 = boto3.resource('s3')
    data = open('/tmp/picture.jpg', 'rb')
    s3.Bucket('bounty-public').put_object(Key='posters/test/picture.jpg', Body=data)
    return "Hello World!"