You ever get tired of dealing with having two or more programs trying to read from the same osc port on vrchat?
Well now you have this program! :3

This program will simply get incoming dispatches from vrchat and dispatch them to the specified ports.


To simply create another dispatching port..
```
OSCRouter -c 127.0.0.1:9003
```
Or if you wanted multiple ports
```
OSCRouter -c 127.0.0.1:9010 127.0.0.1:9011 127.0.0.1:9012
```

You can also specify the vrchat server ip/port...
```
OSCRouter -s 127.0.0.1:9001
```
