# -*- coding: utf-8 -*-
#from ctypes import cdll
import ctypes
import cv2
import numpy as np

import os, sys, io, gc, re
import glob, uuid, base64, json, time

from tornado.escape import json_encode

from tornado import websocket, web, ioloop

import tornado.ioloop
import tornado.web
import tornado.websocket

from cStringIO import StringIO


class ImageWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()
    myfile = file
    def check_origin(self, origin):
        return True

    def open(self):
        ImageWebSocket.clients.add(self)
        print("WebSocket opened from: " + self.request.remote_ip)

    def on_message(self, message):
        
        #try:
                ms =  json.loads(message)
                if ms.keys()[0] == "Start":
                   print "Start"
                   self.myfile = open(ms["Start"]["Name"], "wb")
                   self.write_message("MoreData")
                if ms.keys()[0] == "Upload":
                 
                   da = ms["Upload"]["Data"]#.encode("utf-8")#
                   da = da.split(",")[1]
                   file_bytes = io.BytesIO(base64.b64decode(da)).read()
                   
                   self.myfile.write(file_bytes)
                   self.write_message("MoreData")
                if ms.keys()[0] == "Done":
                   
                   print "Done"
                   self.myfile.close() 
        #except:
           #print message


    def on_close(self):
        ImageWebSocket.clients.remove(self)
        print("WebSocket closed from: " + self.request.remote_ip)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
	self.render("upload.html", title="Нейронная сеть/Тренировка")

app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", ImageWebSocket),
    ])
app.listen(8800)

print("Starting server: http://xxx.xx.xx.xxx:8800/") # IP

tornado.ioloop.IOLoop.current().start()



