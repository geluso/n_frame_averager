WIDTH = 20
MAXX = 1560

IN_DIR = "original_frames"
OUT_DIR = "ave2_frames/"

for i in range(1, MAXX):
  frame_range = range(max(1, i - WIDTH), min(MAXX, i + WIDTH))
  files = ""
  for frame in frame_range:
    files += "%s/%04d.png " % (IN_DIR, frame)
  command = "convert %s -evaluate-sequence mean %s/%04d.png" % (files, OUT_DIR, i)
  print "echo '(%d/%d)'" % (i, MAXX)
  print command
