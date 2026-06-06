#!/bin/bash
# Sends a GET request with custom header X-HolbertonSchool-User-Id set to 98
curl -s -H "X-School-User-Id: 98" "${1}"
