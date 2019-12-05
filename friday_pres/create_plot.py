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

def arrange_connections(config, well_category, slot_category):
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
        # A bit of hack if there's only one rig..
        if len(config['rigs']) == 1:
            r_idx = 0.5
        for well in rig['wells']:
            category = well_category.get(well, 'undefined')
            connection = [None, None, well_names.index(well), r_idx, category]
            connections.append(connection)

        for slot in rig['slots']:
            category = slot_category.get(slot, 'undefined')
            connection = [r_idx, slot_names.index(slot), None, None, category]
            connections.append(connection)

    for slot in config['slots']:
        for well in slot['wells']:
            category = well_category.get(well, 'undefined')
            if category == 'undefined':
                category = slot_category.get(slot['name'], 'undefined')

            connection = [None, slot_names.index(slot['name']), well_names.index(well), None, category]
            connections.append(connection)

    return connections

def main(fname):
    config = load_config(fname)
    well_category = {
        "W1": 'completed',
        "W2": 'next'
        }

    well_category = {"W1": 'next',}

    slot_category = {
        "S1": 'completed',
        "S2": 'next'
        }
    slot_category = {"S1": 'completed'}
    well_category = {}
    slot_category = {}

    connections = arrange_connections(config, well_category=well_category, slot_category=slot_category)
    df = pd.DataFrame(connections)
    df.columns = ['rig', 'slot','well','rig','name']

    ax = pd.plotting.parallel_coordinates(df, 'name', color = ('#669999'))
    ax.grid(False)
    ax.set_yticks([])
    ax.get_legend().remove()

    plt.savefig("testfig")


if __name__ == '__main__':
    main("friday_pres/edc_config_large.yml")
    #main(sys.argv[1])
