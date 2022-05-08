from matplotlib import pyplot as plt
from matplotlib import cm

def plot(x, y, xlabel=None, ylabel=None, title=None, figsize=None):
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=14)
    plt.grid(':')
    plt.show()


def plot_state_evolution(X, t, ylabels=None, xlabel=None, title=None, figsize=None):
    # NOTA questa è una funzione di disegno più complessa!
    # Il codice è basato su quello di: https://matplotlib.org/3.5.0/gallery/spines/multiple_yaxis_with_spines.html
    plt.figure(figsize=figsize)
    
    # Definisco le etichette per gli assi y
    if ylabels is None:
        ylabels = [None for i in range(X.shape[1])]
        
    # Preparo la mappa dei colori
    cmap = cm.get_cmap('Set2')
    
    # Preparo l'offset per gli assi addizionali
    offset = .05
    
    # Disegno la componente principale
    plt.plot(t, X[:, 0], label=ylabels[0], color=cmap(0))
    plt.gca().set_xlabel(xlabel, fontsize=14)
    plt.gca().set_ylabel(ylabels[0], fontsize=14)
    plt.gca().yaxis.label.set_color(cmap(0))
    
    # Disegno le altre componenti
    for i in range(1, X.shape[1]):
        ax = plt.gca().twinx()
        h = ax.plot(t, X[:, i], color=cmap(i))
        ax.spines.right.set_position(("axes", 1 + offset * (i-1)))
        ax.set_ylabel(ylabels[i], fontsize=14)
        ax.yaxis.label.set_color(cmap(i))

    plt.title(title, fontsize=14)
    plt.grid(':')
    plt.show()