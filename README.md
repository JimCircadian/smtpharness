# smtpharness
An SMTP Test Harness

It needs features, but it goes like this: 

1. You run the test harness
2. It listens and posts mail through your relay(s) layers, the end of which points back to the relay
3. You can space messages out and trace the failover scenario across multiple resilient layers of SMTP relay

This is useful if you're building a resilient, multi-site SMTP infrastructure for someone ;-)

I used it for sanity checking, but there's a long way you could take it. I haven't finished it as I'm busy with other things...

----

Things to do (this or in subprojects): 

- Make logging better / native
- Add command line arguments
- Eliminate any race conditions
- Integrity checking of results?
- FIX the throttling system
- ADD a reset
