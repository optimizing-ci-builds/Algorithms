import inotify.adapters
from datetime import datetime
import os

# target_dir = "/home/jhilke/researh/ut-se/test-inotify/commons-lang/target"
# log_file = "/home/jhilke/researh/ut-se/test-inotify/commons-lang/inotify_logger2.csv"

target_dir = os.argv[1]
log_file = os.argv[2]

with open(log_file, "w") as f:
    pass

def _main():
    i = inotify.adapters.InotifyTree(target_dir)
    
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        with open(log_file, "a") as f:
            f.write(f"{timestamp};{path};{filename};{','.join(type_names)}\n")
            f.flush()
        
if __name__ == '__main__':
    _main()