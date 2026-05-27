"""
AXIOS OS Terminal Banner

Displays startup identity banner
when AXIOS OS initializes.
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# --------------------------------------------------
# Console
# --------------------------------------------------

console = Console()

# --------------------------------------------------
# Banner Renderer
# --------------------------------------------------

def display_banner():
    """
    Render AXIOS OS startup banner.
    """

    banner_text = Text()

    banner_text.append(
        "\n"
        " █████╗ ██╗  ██╗██╗ ██████╗ ███████╗     ██████╗ ███████╗\n"
        "██╔══██╗╚██╗██╔╝██║██╔═══██╗██╔════╝    ██╔═══██╗██╔════╝\n"
        "███████║ ╚███╔╝ ██║██║   ██║███████╗    ██║   ██║███████╗\n"
        "██╔══██║ ██╔██╗ ██║██║   ██║╚════██║    ██║   ██║╚════██║\n"
        "██║  ██║██╔╝ ██╗██║╚██████╔╝███████║    ╚██████╔╝███████║\n"
        "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝\n",
        style="bold cyan"
    )

    banner_text.append(
        "\n"
        "Adaptive Existential Intelligence\n"
        "& Operational Mediation System\n",
        style="bold white"
    )

    banner_text.append(
        "\n"
        "Coherence Through Recursive Understanding\n",
        style="italic bright_blue"
    )

    banner = Panel(
        banner_text,
        title="[bold cyan]AXIOS OS[/bold cyan]",
        subtitle="[green]Recursive Intelligence Framework[/green]",
        border_style="bright_blue",
        padding=(1, 4)
    )

    console.print(banner)

    console.print(
        "[bold green]SYSTEM STATUS:[/bold green] OPERATIONAL"
    )

    console.print(
        "[bold cyan]INITIALIZING RECURSIVE COGNITIVE STACK...[/bold cyan]\n"
    )
