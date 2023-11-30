import pyulog
import os


def read_ulg(log_file, time_interval):
    log = pyulog.ULog(log_file)

    data_list = log.data_list

    vehicle_position_data = log.get_dataset('vehicle_local_position')

    previous_timestamp = None

    content = ""

    for timestamp, x, y, z in zip(vehicle_position_data.data['timestamp'],
                                  vehicle_position_data.data['x'],
                                  vehicle_position_data.data['y'],
                                  vehicle_position_data.data['z']):
        if previous_timestamp is None or timestamp - previous_timestamp >= time_interval * 1e6:
            content += f"Timestamp: {timestamp}, X: {x}, Y: {y}, Z: {z} \n"
            previous_timestamp = timestamp

    return content
