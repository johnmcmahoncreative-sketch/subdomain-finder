from src.os_detector import Detect
from rich.console import Console
from rich.panel import Panel

console = Console()
OS_info = Panel.fit(f"[blue]OS:{Detect()}")
console.print(OS_info)
