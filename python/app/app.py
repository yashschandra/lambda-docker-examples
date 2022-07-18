from htmlwebshot import WebShot
import boto3

def handler(event, context):
    print(event['html_str'])
    shot = WebShot()
    print('writing to local file')
    with open('/tmp/content.html', 'w+') as htmlfile:
        htmlfile.write(event['html_str'])
    print('wrote local file, taking shot')
    shot.create_pic(html='/tmp/content.html', output="/tmp/picture.jpg")
    print('took shot, uploading to s3')
    s3 = boto3.resource('s3')
    data = open('/tmp/picture.jpg', 'rb')
    s3.Bucket('bounty-public').put_object(Key='posters/test/picture.jpg', Body=data)
    print('uploaded')
    return "Hello World!"