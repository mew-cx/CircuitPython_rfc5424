# SPDX-FileCopyrightText: 2022 Michael E. Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# simple_test.py
# Review the RFC to understand what the fields mean:
# https://datatracker.ietf.org/doc/html/rfc5424 : "The Syslog Protocol"

import time
import wifi
import socketpool
import ipaddress
import rfc5424

# you need your own secrets...
from secrets import secrets


# Create an rfc5424-formatted syslog message...
syslog_msg = rfc5424.FormatRFC5424(
    facility = Facility.LOCAL1,
    severity = Severity.INFO,
    timestamp = rfc5424.FormatTimestamp(time.localtime()),
    hostname = wifi.radio.ipv4_address,
    app_name = "your_appname_here",
    procid = "procID",
    msgid = "msgID",
    msg = "this is the message"
    )


# Connect to a wifi access point...
print("connecting to AP", secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("my ipaddr", wifi.radio.ipv4_address)

HOST = secrets["syslog_server"]
PORT = 514
TIMEOUT = 5

pool = socketpool.SocketPool(wifi.radio)
server_ipv4 = ipaddress.ip_address(pool.getaddrinfo(HOST, PORT)[0][4][0])
print("server ipaddr", server_ipv4)
print("ping time", wifi.radio.ping(server_ipv4), "ms")


# Now send the message to the syslog server via TCP...
with pool.socket(pool.AF_INET, pool.SOCK_STREAM) as sock:
    sock.settimeout(TIMEOUT)
    print("connecting socket")
    sock.connect((HOST, PORT))
    sent = sock.send(syslog_msg)
    print("sent length : %d" % sent)

# vim: set sw=4 ts=8 et ic ai:
