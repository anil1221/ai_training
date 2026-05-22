import psutil
import shutil
import socket


class SystemManagementTool:

    def get_system_stats(self):
        memory = psutil.virtual_memory()
        disk = shutil.disk_usage("/")

        return {
            "ram_total_gb": round(memory.total / (1024**3), 2),
            "ram_available_gb": round(memory.available / (1024**3), 2),
            "storage_total_gb": round(disk.total / (1024**3), 2),
            "storage_free_gb": round(disk.free / (1024**3), 2) }

    def get_open_ports(self):
        connections = psutil.net_connections()
        open_ports = []

        for conn in connections:
            if conn.status == "LISTEN":
                try:
                    process = psutil.Process(conn.pid).name()
                except:
                    process = "Unknown"
                open_ports.append({ "port": conn.laddr.port, "process": process })

        return open_ports

    def get_running_services(self):
        services = []

        for process in psutil.process_iter(['pid', 'name']):
            services.append({ "pid": process.info['pid'], "name": process.info['name']})

        return services[:20]