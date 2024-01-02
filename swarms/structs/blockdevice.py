from tracemalloc import start
from typing import Any, Callable, Dict, List, Union

from dataclasses import dataclass, field

@dataclass
class BlockDevice:
    device: str
    cluster: str
    description: str
    
    def __init__(self, device: str, cluster: str, description: str):
        self.device = device
        self.cluster = cluster
        self.description = description
        
    def __str__(self):
        return f"BlockDevice(device={self.device}, cluster={self.cluster}, description={self.description})"
    
