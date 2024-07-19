#!/bin/bash
sleep 10
DISPLAY=:0 ~/../../usr/bin/chromium-browser --kiosk --disable-restore-session-state  http://127.0.0.1:5000/
