'''
 [~]
 ✘  jaisriram  cat http42
key:
   - please
   - please2

 [~]
 jaisriram  curl -X POST -H "Content-Type: application/yaml" http://ptl-7f3f29a4-fc8bb845.libcurl.so/pentesterlab --data-binary @http42
The key for this challenge is: fd8e88bc-da33-4cd0-8c34-2a2315a8d0a3
'''

curl -X POST -H "Content-Type: application/yaml" http://ptl-7f3f29a4-fc8bb845.libcurl.so/pentesterlab --data-binary @http42