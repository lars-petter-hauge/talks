#!/usr/bin/env
import sys
import pandas as pd
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import yaml


def load_config(fname):
    with open(fname) as handle:
        return yaml.safe_load(handle)

def arrange_connections(config):
    rig_names = [r['name'] for r in config['rigs']]
    slot_names = [s['name'] for s in config['slots']]
    well_names = []
    for r in config['rigs']:
        well_names.extend(r['wells'])
    for s in config['slots']:
        well_names.extend(s['wells'])
    well_names = list(set(well_names))
    well_names.reverse()
    connections = []
    for rig in config['rigs']:
        r_idx = rig_names.index(rig['name'])
        r_idx = r_idx+int(len(slot_names)/len(rig_names))
        for well in rig['wells']:
            connection = [None, None, well_names.index(well), r_idx, 'name']
            connections.append(connection)

        for slot in rig['slots']:
            connection = [r_idx, slot_names.index(slot), None, None, 'name']
            connections.append(connection)

    for slot in config['slots']:
        for well in slot['wells']:
            connection = [None, slot_names.index(slot['name']), well_names.index(well), None, 'name']
            connections.append(connection)

    return connections

def main(fname):
    config = load_config(fname)
    connections = arrange_connections(config)
    df = pd.DataFrame(connections)
    df.columns = ['rig', 'slot','well','rig','name']

    ax = pd.plotting.parallel_coordinates(df, 'name')
    ax.grid(False)
    ax.set_yticks([])
    ax.get_legend().remove()

    plt.savefig("testfig")


if __name__ == '__main__':
    main(sys.argv[1])
