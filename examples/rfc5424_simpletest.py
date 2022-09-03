# SPDX-FileCopyrightText: 2022 Michael E. Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# rfc5424_simpletest.py
# Review the RFC to understand what the fields mean:
# https://datatracker.ietf.org/doc/html/rfc5424 : "The Syslog Protocol"

import time
import rfc5424

# Create an rfc5424-formatted syslog message...
syslog_msg = rfc5424.FormatRFC5424(
    facility = Facility.LOCAL1,
    severity = Severity.INFO,
    timestamp = rfc5424.FormatTimestamp(time.localtime()),
    hostname = "your_hostname_here",
    app_name = "your_appname_here",
    procid = "procID",
    msgid = "msgID",
    msg = "this is the message"
    )

print(repr(syslog_msg))

# vim: set sw=4 ts=8 et ic ai:
