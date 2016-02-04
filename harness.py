#!/usr/bin/env python

import sys
import pprint
from traceback import print_tb
from smtpnodes import sender, receiver
from termwindow import window

class CommandProcessor():
    MENUS = [
        [ None, "Choose:", None, ],
        [ "c", "", "c)", "change sending limit", lambda s: s.limit(cp.prompt("Enter new limit: ")) ],
        [ "d", "", "d)", "change duration", lambda s: s.duration(cp.prompt("Enter new duration: ")) ],
        [ "s", "", "s)", "start client sending", lambda s: s.start() ],
        [ "q", "", "q)", "quit", lambda r: r.stop() ],
    ]
        
    STATUSES = [
        [ "Threads Status:", ],
        [ "", ],
        [ "Server thread:", lambda r: r.status(), ],
        [ "Client thread:", lambda s: s.status(), ], 
        [ "", ],
        [ "Messages sent:", lambda s: "{0} / {1}    ".format(s.get_sent(), s.get_limit()), ],
        [ "Sender duration:", lambda s: "{0} seconds".format(s.get_duration()), ],
        [ "Messages received:", lambda r: r.get_received(), ],
    ]

    def __init__(self):
        self.tw = window.TermMenu()
        
        self.tw.assign_menus(self.MENUS)
        self.tw.assign_statuses(self.STATUSES)

    def prompt(self, msg):
        return self.tw.prompt(msg)
                
    def start(self, recv, send):
        try:
            self.tw.start_window({
                'r':  recv,
                's':  send,
            })
        except:
            self.tw.cleanup()
            recv.stop()
            send.stop()
            print "Well, something went wrong and I've attempted to shut down gracefully..."
            print "Unexpected error: ", pprint.pprint(sys.exc_info())
            print_tb(sys.exc_info()[2])

cp = CommandProcessor()

def main():
    r = receiver.Receiver("0.0.0.0", 2255)
    s = sender.Sender("127.0.0.1", 2255)
    r.start()
    # s.start()
    cp.start(r, s)
    
if __name__ == "__main__":
    main()
