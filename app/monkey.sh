#!/bin/bash
devices=`adb devices|grep '[0-9]'|awk '{print $1}'`
for device in $devices;do
{
	nohup adb -s $device shell monkey --pct-touch 30 --pct-motion 20 --pct-nav 30 --pct-syskeys 20 -v --throttle 500 400 &
}
done