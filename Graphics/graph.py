import matplotlib.pyplot as plt
from pathlib import Path


def create_graph(y,
                x=None,
                xlabel='X',
                ylabel='Y',
                title='График',
                filename='graph.png',
                transparent=False,
                grid=True):

    dirr = Path(__file__).parent.parent
    last_dirr = dirr / 'static' / 'images'
    last_dirr.mkdir(parents=True, exist_ok=True)
    path = last_dirr / filename

    if path.exists():
        print(f"Файл {filename} уже существует в {dir}")
        return False

    fig, ax = plt.subplots(figsize=(10, 6))

    if x is None:
        x = range(len(y))

    ax.plot(x, y, linewidth=2, marker='o', markersize=4)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    if grid:
        ax.grid(grid, linestyle='--')

    if transparent:
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
    else:
        fig.patch.set_facecolor('white')
        ax.set_facecolor('#f8f9fa')

    plt.tight_layout()
    plt.savefig(
        path,
        dpi=300,
        bbox_inches='tight',
        transparent=transparent
    )
    plt.close(fig)

    return True