from dataclasses import dataclass


@dataclass
class TableDto:
    data_list: list
    total: int

