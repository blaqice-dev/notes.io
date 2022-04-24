import sys

from PySide6.QtWidgets import QApplication

from views.dashboard import DashboardFrame


class Notes(QApplication):
    dashboard_frame: DashboardFrame

    def __init__(self):
        super(Notes, self).__init__([])

    def setUI(self):
        self.dashboard_frame = DashboardFrame()
        self.dashboard_frame.setMinimumSize(450, 700)
        self.dashboard_frame.resize(450, 700)

    def start(self):
        self.setUI()
        self.dashboard_frame.show()

        sys.exit(self.exec())
