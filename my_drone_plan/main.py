import sys
import folium
import io
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QListWidget, QHBoxLayout, QWidget, QSlider, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MissionPlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mission Planner - Simulasi Drone")
        self.setGeometry(100, 100, 1200, 700)

        # Layout Utama
        main_layout = QHBoxLayout()

        # Peta
        self.map_view = QWebEngineView()
        self.create_map()
        main_layout.addWidget(self.map_view, 70)

        # Panel Kontrol
        control_panel = QVBoxLayout()
        control_panel.setContentsMargins(10, 10, 10, 10)

        self.log_list = QListWidget()
        control_panel.addWidget(QLabel("Log Waypoints"))
        control_panel.addWidget(self.log_list)

        # Input Latitude & Longitude
        self.lat_input = QLineEdit()
        self.lat_input.setPlaceholderText("Latitude")
        self.lon_input = QLineEdit()
        self.lon_input.setPlaceholderText("Longitude")
        self.altitude_slider = QSlider()
        self.altitude_slider.setOrientation(1)
        self.altitude_slider.setMinimum(10)
        self.altitude_slider.setMaximum(100)
        self.altitude_slider.setValue(50)

        control_panel.addWidget(QLabel("Latitude"))
        control_panel.addWidget(self.lat_input)
        control_panel.addWidget(QLabel("Longitude"))
        control_panel.addWidget(self.lon_input)
        control_panel.addWidget(QLabel("Altitude (m)"))
        control_panel.addWidget(self.altitude_slider)

        # Tombol Tambah Waypoint
        self.add_waypoint_btn = QPushButton("Tambah Waypoint")
        self.add_waypoint_btn.clicked.connect(self.add_waypoint)
        control_panel.addWidget(self.add_waypoint_btn)

        # Tombol Start & Stop
        self.start_mission_btn = QPushButton("Mulai Misi")
        self.start_mission_btn.clicked.connect(self.start_mission)
        self.stop_mission_btn = QPushButton("Hentikan Misi")
        self.stop_mission_btn.clicked.connect(self.stop_mission)

        control_panel.addWidget(self.start_mission_btn)
        control_panel.addWidget(self.stop_mission_btn)

        main_layout.addLayout(control_panel, 30)

        # Set layout utama
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Data Waypoints
        self.waypoints = []

    def create_map(self):
        """Buat peta awal di Jakarta"""
        start_coords = [-6.2088, 106.8456]
        m = folium.Map(location=start_coords, zoom_start=13)
        folium.Marker(location=start_coords, popup="Starting Point", icon=folium.Icon(color="blue")).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.map_view.setHtml(data.getvalue().decode())

    def add_waypoint(self):
        """Tambah waypoint ke dalam peta dan log"""
        try:
            lat = float(self.lat_input.text())
            lon = float(self.lon_input.text())
            altitude = self.altitude_slider.value()
            waypoint = {"lat": lat, "lon": lon, "alt": altitude}
            self.waypoints.append(waypoint)

            self.log_list.addItem(f"Waypoint: {lat}, {lon}, Alt: {altitude}m")
            self.update_map()
        except ValueError:
            self.log_list.addItem("Error: Input tidak valid!")

    def update_map(self):
        """Update peta dengan waypoint terbaru"""
        m = folium.Map(location=[-6.2088, 106.8456], zoom_start=13)
        for wp in self.waypoints:
            folium.Marker(location=[wp["lat"], wp["lon"]], popup=f"Alt: {wp['alt']}m",
                          icon=folium.Icon(color="red")).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.map_view.setHtml(data.getvalue().decode())

    def start_mission(self):
        """Mulai simulasi misi"""
        if self.waypoints:
            self.log_list.addItem("Misi dimulai...")
            for i, wp in enumerate(self.waypoints):
                self.log_list.addItem(f"Menuju Waypoint {i+1}: {wp['lat']}, {wp['lon']} (Alt: {wp['alt']}m)")
        else:
            self.log_list.addItem("Tidak ada waypoint! Tambahkan dulu.")

    def stop_mission(self):
        """Hentikan simulasi misi"""
        self.log_list.addItem("Misi dihentikan!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MissionPlanner()
    window.show()
    sys.exit(app.exec_())
