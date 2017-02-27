#!/bin/bash
TESTPATH=`dirname $(readlink -f $0)`
PATH=$PATH:.
xvfb-run python selenium-uchiwa/uchiwa_test.py --ip 192.168.33.51 --username operator --password changeme --protocol http --port 80 --wait 10
