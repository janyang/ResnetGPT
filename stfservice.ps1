adb shell am start-foreground-service --user 0 -a jp.co.cyberagent.stf.ACTION_START -n jp.co.cyberagent.stf/.Service

$APK=$(adb shell pm path jp.co.cyberagent.stf | tr -d '\r' | awk -F: '{print $2}')

adb shell "export CLASSPATH=`"$APK`"; exec app_process /system/bin jp.co.cyberagent.stf.Agent"