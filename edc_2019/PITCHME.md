# DRILL SCHEDULING
Prepare for an advent of code challenge

Lars Petter Øren Hauge,
Software Innovation Bergen

---
### What do we have to work with

@ul[spaced]
 - rigs
 - slots
 - wells
@ulend

---
### Day 1

 - Create a valid drilling schedule for a set of wells
 - Each well is given a drilltime and a priority


```yaml
wells:
    -
        name: 'W1',
        drilltime: 20,
        priority: 2
    -
        name: 'W2',
        drilltime: 15,
        priority: 1
```
@css[text-white snap south]https://adventofcode.com/

Note:
 - header: #00cc00
 - background: #0f0f23
 - body: #666666
---
### Day 1 - continue

 - A well must be drilled from a rig through a slot
 - A rig can drill a set of wells
 - A slot can drill a set of wells

```yaml
rigs:
    -
        name: 'R1',
        wells: ['W1', 'W2']
slots:
    -
        name: 'S1',
        wells: ['W1']
    -
        name: 'S2',
        wells: ['W2']
```

---
### Structure

![Logo](edc_2019/img/simple_config_structure2.png)

---
### Structure

![Logo](edc_2019/img/simple_config_parcoord.png)

---
### Let's solve!

```python
wells = ['W1', 'W2']

while wells:
    for rig in occupied_rigs:
        rig[days] -= 1
        if rig[days] == 0:
            available_rigs.add(rig)
            occupied_rigs.pop(rig)

    if available_rigs:
        well_to_drill = sorted(wells, key=priority)

        rig, slot = valid_rig_slot(well_to_drill, rigs, slots)
        if rig and slot:
            available_rigs.pop(rig)
            slots.pop(slot)
            wells.pop(well)

            occupied_rigs[rig][days] = wells[well_to_drill][drill_time]
            completed_wells.append(well)

def valid_rig_slot(well, rigs, slots):
    rigs = filter(rigs, well in rig[well])
    slots = filter(slots, well in slot[well])

    return rig, slot
```

@snap[south span-100]
@[1](The wells we want to schedule)
@[3,10-11](Find highest priority well)
@[22-26](Retrieve available rig and slot)
@[10,12-17](Add to queue)
@[19-20](Occupy rig for the duration of drilling)
@[4-8](Release rigs that have completed drilling)
@snapend

---
### Day 2 Unavailability

 - Unavailable rig
 - Unavailable slot

Note:

 - the platform is up north and can't be used during winter season
 - template simply hasn't been installed yet

---
### Day 2 -- continue

```yaml
rigs:
  -
    name: 'A'
    wells: ['w1', 'w2', 'w3', 'w4']
    slots: ['S1', 'S2', 'S3']
    unavailability:
      -
        start: 2000-01-01
        stop: 2000-02-02
      -
        start: 2000-03-14
        stop: 2000-03-19
```
---
### Day 2 -- continue

GANT PLOT SHOWING UNAVAILABILITY

---
### Let's solve!

```python
wells = ['W1', 'W2']
day = 0

while wells:
    for rig in occupied_rigs:
        rig[days] -= 1
        if rig[days] == 0:
            available_rigs.add(rig)
            occupied_rigs.pop(rig)

    if available_rigs:
        well_to_drill = sorted(wells, key=priority)

        rig, slot = valid_rig_slot(well_to_drill, rigs, slots, day)
        if rig and slot:
            available_rigs.pop(rig)
            slots.pop(slot)
            wells.pop(well)

            occupied_rigs[rig][days] = wells[well_to_drill][drill_time]
            completed_wells.append(well)
    day += 1

def valid_rig_slot(well, rigs, slots, day):
    rigs = filter(rigs, well in rig[well])
    rigs = filter(rigs, day not in rig[unavailability])

    slots = filter(slots, well in slot[well])
    slots = filter(slots, day not in rig[unavailability])

    return rig, slot
```

@snap[south span-100]
@[24, 26, 29](Make sure rig and slot are available)
@snapend

---
### Day 2 input

```yaml
rigs:
  -
    name: 'A'
    wells: ['w1', 'w2', 'w3', 'w4']
    slots: ['S1', 'S2', 'S3']
  -
    name: 'B'
    wells: ['w2', 'w3', 'w4', 'w5']
    slots: ['S3', 'S4', 'S5']
slots:
  -
    name: 'S1'
    wells: ['w1', 'w2', 'w3']
  -
    name: 'S2'
    wells: ['w2', 'w3']
  -
    name: 'S3'
    wells: ['w2', 'w3']
  -
    name: 'S4'
    wells: ['w3', 'w4']
  -
    name: 'S5'
    wells: ['w3', 'w4', 'w5']
```
+++
###
```python
    """
    Five wells should be drilled, there are three available rigs and a total of five slots

    The rigs can drill tree wells each: Rig A can drill the first 3 wells,
    Rig B wells 1-4 and rig C wells 3-5. (i.e. all rigs can drill well 3).

    Slot 3 is the only slot that can drill well 5. Slot 3 is also the only slot that can
    be drilled at all rigs. The logic must here handle that slot 3 is "reserved" for the
    last well.

    To reduce the overall drill time, the logic must also handle rig reservation to specific
    wells


    In order for all wells to be drilled, the wells can't be taken randomly
    from an instruction set of all possible combinations.
     - Slot 3 must be reserved to well 5
     - W4 can not be drilled at rig A, hence the first well to finish (W1)
       should not be drilled at Rig A
     - W5 can only be drilled at Rig C, Slot 3. Thus the second well to
       finish (W3) should be drilled at Rig C
    The key aspect here is that it is possible to drill the wells continuously
    given that they are assigned to specific slots and rigs

    A valid setup that will allow for this drilling regime is:
    (well='W1', rig='B', slot='S2')
    (well='W3', rig='C', slot='S1')
    (well='W2', rig='A', slot='S4')
    (well='W4', rig='B', slot='S5')
    (well='W5', rig='C', slot='S3')
    """
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2001, 1, 1)
    wells = ["W1", "W2", "W3", "W4", "W5"]
    slots = ["S1", "S2", "S3", "S4", "S5"]
    config = {
        "start_date": start_date,
        "end_date": end_date,
        "wells": [
            {"name": "W1", "drill_time": 10},
            {"name": "W2", "drill_time": 30},
            {"name": "W3", "drill_time": 25},
            {"name": "W4", "drill_time": 20},
            {"name": "W5", "drill_time": 40},
        ],
        "rigs": [
            {"name": "A", "wells": wells[:3], "slots": slots},
            {"name": "B", "wells": wells[:4], "slots": slots},
            {"name": "C", "wells": wells[2:], "slots": slots},
        ],
        "slots": [
            {"name": "S1", "wells": wells[:4]},
            {"name": "S2", "wells": wells[:4]},
            {"name": "S3", "wells": wells},
            {"name": "S4", "wells": wells[:4]},
            {"name": "S5", "wells": wells[:4]},
        ],
        "wells_priority": {"W1": 5, "W2": 4, "W3": 3, "W4": 2, "W5": 1},
    }
```
---
### Day 2 structure

![Logo](edc_2019/img/advanced_config_structure.png)

---
### Day 2 structure

![Logo](edc_2019/img/config_parcoord.png)

---
### What can we do?

```python
wells = ['W1', 'W2']
day = 0

while wells:
    for rig in occupied_rigs:
        rig[days] -= 1
        if rig[days] == 0:
            available_rigs.add(rig)
            occupied_rigs.pop(rig)

    if available_rigs:
        well_to_drill = sorted(wells, key=priority)

        rig, slot = valid_rig_slot(well_to_drill, rigs, slots, day)
        if rig and slot:
            available_rigs.pop(rig)
            slots.pop(slot)
            wells.pop(well)

            occupied_rigs[rig][days] = wells[well_to_drill][drill_time]
            completed_wells.append(well)
    day += 1

def valid_rig_slot(well, rigs, slots, day):
    rigs = filter(rigs, well in rig[well])
    rigs = filter(rigs, day not in rig[unavailability])
    rig = sorted(rigs, key=len(slots[wells]))[0]

    slots = filter(slots, well in slot[well])
    slots = filter(slots, day not in rig[unavailability])
    slot = sorted(slots, key=len(slots[wells]))[0]

    return rig, slot
```

@snap[south span-100]
@[24, 27, 31, 32](sorting rigs and slots - picking those with most possibilities)
@snapend
---
### Realization

Can we guarantee that we find the optimal solution?

---
### Brute force[snap north]

@ul[spaced span-50 snap west]
 - How many wells?
 - How many slots?
 - How many rigs?
@ulend
@ul[spaced span-50 snap east]
- 200
- 200
- 5
@ulend
@css[text-white fragment snap south](Simply - not a viable solution)

---
### Current implementation

CP SAT solver

@ul[spaced]
- Create a task for every combination
- Add constraints for each:
    - Valid combination
    - Unavailability
    - Rig Overlap
    - Well drilled once
    - Slot used once
- Add objective function:
    - Minimize days to drill_start, scaled by prioritization
@ulend

---
### Current implementation

CP SAT solver

https://github.com/equinor/spinningjenny/tree/master/spinningjenny/drill_planner

---
### Day 3

Dynamic rig constraints

Note:

 - Rigs can be moved, and as such the slot constraint may change
