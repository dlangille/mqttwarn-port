--- services/pushsafer.py.orig	2018-03-26 17:02:51.149292000 +0000
+++ services/pushsafer.py	2018-03-26 17:03:33.436002000 +0000
@@ -65,22 +65,22 @@
         params['d'] = addrs[1]
 		
 	if len(addrs) > 2:
-        params['i'] = addrs[2]
+          params['i'] = addrs[2]
 		
 	if len(addrs) > 3:
-        params['s'] = addrs[3]
+          params['s'] = addrs[3]
 		
 	if len(addrs) > 3:
-        params['v'] = addrs[4]
+          params['v'] = addrs[4]
 		
 	if len(addrs) > 4:
-        params['u'] = addrs[5]
+          params['u'] = addrs[5]
 		
 	if len(addrs) > 5:
-        params['ut'] = addrs[6]
+          params['ut'] = addrs[6]
 		
 	if len(addrs) > 6:
-        params['l'] = addrs[7]
+          params['l'] = addrs[7]
 
     if title is not None:
         params['t'] = title
