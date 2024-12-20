class DataStream:

    def __init__(self):
        self.data_storage ={}

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        
        if data_string not in self.data_storage:
            # update the timestamp
            self.data_storage[data_string]=timestamp
            return True
        
        # timestamp check
        last_timestamp_of_data = self.data_storage[data_string]
        if last_timestamp_of_data + 5 <= timestamp:
            # update the timestamp
            self.data_storage[data_string]=timestamp
            return True
        
        else:
            return False


data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=1, data_string="world"))
print(data_stream.should_output_data_str(timestamp=6, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=7, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=8, data_string="world"))
