# CircuitPython_rfc5424

This library implements the syslog message formatting specified by RFC5424.
- https://datatracker.ietf.org/doc/html/rfc5424 : "The Syslog Protocol"

This library only does formatting, it does not transmit its results by any transport.
It is left to the caller to send the results by whatever means.

The formatting specifications are primarily under [Section 6](https://datatracker.ietf.org/doc/html/rfc5424#section-6) of the RFC.
