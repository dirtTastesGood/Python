import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == '__main__':
    patterns = '*'
    ignore_patterns = ''
    ignore_directories = ''
    
    my_event_handler = PatternMatchingEventHandler(
        patterns = patterns,  # watched patterns
        ignore_patterns = ignore_patterns,  # ignored patterns
        ignore_directories = ignore_directories,  # ignored directories
        case_sensitive = True
    )

    def on_created(event):
        print(f"File created: {event.src_path}")

    def on_deleted(event):
        print(f"File deleted: {event.src_path}")
    def on_modified(event):
        print(f"File modified: {event.src_path}")
    def on_moved(event):
        print(f"File moved: {event.src_path}")

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    path = '.'
    observer = Observer()
    observer.schedule(
        my_event_handler,
        path,
        recursive=True
    )

    observer.start()
    try:
        print("Watching...")
        print("Press Ctrl + C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()