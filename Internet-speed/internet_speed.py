#pip install speedtest-cli

import speedtest


def Speed_test():
  test = speedtest.Speedtest()

  down_speed = test.download()
  down_speed = round(down_speed / 10**6, 2)
  print("Download speed in Mbps: ", down_speed)

  up_speed = test.upload()
  up_speed = round(up_speed / 10**6, 2)
  print("Upload speed in Mbps: ", up_speed)

  ping = test.results.ping
  print("Ping: ", ping, "ms")

Speed_test()
