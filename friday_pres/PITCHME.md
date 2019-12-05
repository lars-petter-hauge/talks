# DRILL SCHEDULING

Lars Petter Øren Hauge,
Software Innovation Bergen

Note:

 - subpart of a bigger project
 - Interesting task in may - different ways to solve
 - Advent of code'ish
 - Will provide some context, show the problem at hand
   and provide our implementation

---
### Everest

@ul
![Logo](friday_pres/img/everest.png)
@ulend

Note:

 - optimize model usage given custom objective
 - reservoir drainage strategy
 - everest/dakota provides numbers, eclipse wants dates
 - This stask is a "translation" from optimizer to simulator

---
### What do we have to work with

@ul[spaced snap west]
- Rigs
- Slots
- Wells
@ulend

@snap[east span-70]
@ul[spaced]
@img[fragment](edc_2019/img/platform.png)
@img[fragment](edc_2019/img/template.jpg)
@img[fragment](edc_2019/img/drillstring.jpg)
@ulend
@snapend

Note:
Equinor
Claxton engineering
Piping engineering

---
### Day 1

Create a valid drilling schedule for a set of wells

---
### Day 1 - continue

@ul
 - A well must be drilled from a rig through a slot
 - A rig can drill a set of wells
 - A slot can be used for a set of wells, not reusable
@ulend

---
### Day 1 - continue

 - A well must be drilled from a rig through a slot
 - A rig can drill a set of wells
 - A slot can be used for a set of wells, not reusable


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
### Day 1 - continue


![Logo](friday_pres/img/simple_config_parcoord.png)

Note:

 - lines show connections
 - connect a line from side to side, must end at same rig

---
### Day 1 - continue


![Logo](friday_pres/img/config_parcoord.png)

---
### Day 1 - continue


![Logo](friday_pres/img/large_config_parcoord.png)

---
### Day 1 - continue

Each well is given a drilltime and a priority

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

---
### Day 1 - continue

Job shop problem

![Logo](friday_pres/img/or_tools_jobshop.png)

---
### Approach

@ul
 - Greedy approach
 - SAT solver
@ulend

---
### CP SAT solver - OR-tools
SAT solver - boolean SATisfiable problem

@ul
 - Create model with a set of formulas
 - Solve
@ulend

---
### CP SAT solver - OR-tools

```python
for rig, slot, well in product(rigs, slots, wells):

    interval = IntervalTask(
        begin,
        well.drilltime,
        end,
        presence)
```

@snap[south span-100]
@[1](Go through all rigs/slots/wells combination)
@[1-7](Create an Interval Task)
@snapend

---
### Create constraints

 - A rig can only drill one well at a time

```python
for rig in rigs:
    intervals = [task.interval for task in rig_tasks(rig)]
    AddNoOverlap(intervals)
```
@snap[south span-100]
@[1](For each rig)
@[2-3](Add constraint that non of the task intervals overlap)
@snapend
---
### Create constraints

 - A well can only be drilled at some rigs and slots

```python
for (well, rig, slot), task in tasks.items():
    if not (rig.can_drill(slot, well)
            or slot.can_drill(well)):
        Add(task.presence == 0)
```

@snap[south span-100]
@[1](Go through all created tasks)
@[2-4](Specify false on drilling well if it can not be drilled)
@snapend
---
### Create constraints

 - A well is only drilled once

```python
for well in wells:
    present = [task.presence for task in well_tasks(well)]
    self.Add(sum(present) == 1)
```

@snap[south span-100]
@[1](Go through all well tasks)
@[2-3](Specify that the sum must be one)
@snapend
---
### Create constraints

 - A slot can not be reused

```python
for slot in slots:
    present = [task.presence for task in slot_tasks(slot)]
    self.Add(sum(present) <= 1)
```

@snap[south span-100]
@[1](Go through all slot tasks)
@[2-3](Specify that the sum can not be more than one)
@snapend

---
### Objective function

 - Wells should be completed as soon as possible, higher priority wells first

```python
Minimize(
    sum(task.end * well.priority for well, task in tasks.items())
)
```

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

![Logo](edc_2019/img/gantt_chart.png)

---
### Create Constraints

 - A rig can not drill when unavailable

```python
for rig in rigs:
    unavailable_intervals = [
        IntervalVar(begin, duration, end)
        for (begin, duration, end) in rig.unavailable_ranges
    ]

    for task in rig_tasks(rig):
        for interval in unavailable_intervals:
            AddNoOverlap([task.interval, interval])
```
@snap[south span-100]
@[1-5](Create an IntervalVar for every unavailable range)
@[7-9](Set No Overlap for each rig task and all IntervalVars created)
@snapend

---
### Create Constraints

 - A slot can not drill while unavailable

```python
for slot in slots:
    unavailable_intervals = [
        IntervalVar(begin, duration, end)
        for (begin, duration, end) in slot.unavailable_ranges
    ]

    for task in slot_tasks(slot):
        for interval in unavailable_intervals:
            AddNoOverlap([task.interval, interval])
```

---
### Ending Remarks
