from htmlwebshot import WebShot
import boto3

def handler(event, context):
    html = event['html_str']
    shot = WebShot()
    shot.create_pic(html=html, output="/tmp/picture.jpg")
    s3 = boto3.resource('s3')
    data = open('/tmp/picture.jpg', 'rb')
    s3.Bucket('bounty-public').put_object(Key='posters/test/picture.jpg', Body=data)
    return "Hello World!"