# MaxDOS


MaxDOS is HTTP Denial of Service attack that affects threaded servers. 
It works like this:

1. The tool starts making lots of HTTP requests.
2. Then the tool sends headers periodically (every 15 seconds) to keep the connections open.
3. The connection is never closed unless the server does so. If the server closes a connection, the tool creates a new one keeps doing the same thing.

This exhausts the servers thread pool and the server can't reply to other people.



## [~] Installation & Usage

$ git clone https://github.com/HackWeiser360/MaxDOS.git

$ cd MaxDOS

$ python3 MaxDOS.py example.com


## Configuration options
It is possible to modify the behaviour of MaxDOS with command-line
arguments. In order to get an up-to-date help document, just run
`MaxDOS -h`.

* -p, --port
* * Port of webserver, usually 80
* -s, --sockets
* * Number of sockets to use in the test
* -v, --verbose
* * Increases logging (output on terminal)
* -ua, --randuseragents
* * Randomizes user-agents with each request
* -x, --useproxy
* * Use a SOCKS5 proxy for connecting
* --https
* * Use HTTPS for the requests
* --sleeptime
* * Time to sleep between each header sent

## This tool is still under development. Adding other features soon.
=================
### Author: MådMâx
Follow author on Instagram: [madmax4708](https://www.instagram.com/madmax4708/).

Follow author on Twitter:[503_madmax](https://twitter.com/503_madmax).