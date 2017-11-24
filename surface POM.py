# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:50:43 2017

@author: abel
"""

# First kmos.types
from kmos.types import *

# Initialize the project
pt = Project()

# Set projects metadata
pt.set_meta( author = 'Haoran_Ding',
             email = 'D201677318@hust.edu.cn',
             model_name = 'POM on surface',
             model_dimension = 2)
#==============================================================================
# Define the lattice
layer = Layer(name = 'perovskite')                 # define a layer
site = Site(name = 'hollow', pos = '0.5 0.5 0.5') # define a site
layer.sites.append(site)                       # add site to layer
# Add layer to Project
pt.add_layer(layer)
#==============================================================================
# Define the surface species
#define gasous species
pt.add_species(name = 'empty', color = '#dddddd')         #白色
pt.add_species(name = 'CH4', color = '#cd3700')     #棕色
pt.add_species(name = 'CO', color = '#cd0000')      #红   
pt.add_species(name = 'CO2', color = '#9FB6CD')     #银灰色
pt.add_species(name = 'H2', color = '#66cd00')      #绿色
pt.add_species(name = 'N2', color = '#000000')      #黑色
pt.add_species(name = 'H2O', color = '#436eee')     #深蓝
pt.add_species(name = 'O2', color = '#6495ed')      #蓝色
#/define adsorbed species
pt.add_species(name = 'CH4_ads', color = '#cd5c5c',
               representation = "Atoms('B',[[0.,0.,0.]])",)     #渐浅红棕色
pt.add_species(name = 'CH3_ads', color = '#cd6839',
               representation = "Atoms('C',[[0.,0.,0.]])",)     
pt.add_species(name = 'CH2_ads', color = '#cd8162',
               representation = "Atoms('N',[[0.,0.,0.]])",)     
pt.add_species(name = 'CH_ads', color = '#cd919e',
               representation = "Atoms('O',[[0.,0.,0.]])",)      
pt.add_species(name = 'C_ads', color = '#575757',
               representation = "Atoms('F',[[0.,0.,0.]])",)       #深灰
pt.add_species(name = 'CO_ads', color = '#cd6839',
               representation = "Atoms('Ne',[[0.,0.,0.]])",)      #橙
pt.add_species(name = 'H_ads', color = '#c0ff3e',
               representation = "Atoms('Na',[[0.,0.,0.]])",)       #浅绿
pt.add_species(name = 'O_ads', color = '#5cacee',
               representation = "Atoms('Mg',[[0.,0.,0.]])",)       #浅蓝
pt.add_species(name = 'OH_ads', color = '#cdad00',
               representation = "Atoms('Al',[[0.,0.,0.]])",)      #黄
pt.add_species(name = 'Ox', color = '#4b0082',
               representation = "Atoms('Si',[[0.,0.,0.]])",)       #紫
#==============================================================================
#Model parameters
#temperature K
pt.add_parameter(name = 'T', value = 973.15,
                 adjustable = True,  min = 773.15, max = 1223.15) 
#gas constant
pt.add_parameter(name = 'R', value = '8.3145')

#concentration of methane 
pt.add_parameter(name = 'p_CH4', value = 0.5,
                 adjustable = True, min = 1e-10, max = 0.5) 
#concentration of oxygen
pt.add_parameter(name='p_O2', value = 0.25,
                 adjustable = True, min = 1e-10, max = 0.5)

#preexponential factor and activation energy of reactions
pt.add_parameter(name = 'A1', value = '0.0045')
pt.add_parameter(name = 'E1', value = '0.0')

pt.add_parameter(name = 'A2', value = '1.0e+4')
pt.add_parameter(name = 'E2', value = '33053.6')

pt.add_parameter(name = 'A3', value = '1.3e+8')
pt.add_parameter(name = 'E3', value = '57739.2')

pt.add_parameter(name = 'A4', value = '1.0e+13')
pt.add_parameter(name = 'E4', value = '115478.4')

pt.add_parameter(name = 'A5', value = '1.0e+13')
pt.add_parameter(name = 'E5', value = '97068.8')

pt.add_parameter(name = 'A6', value = '1.0e+13')
pt.add_parameter(name = 'E6', value = '18828.0')

pt.add_parameter(name = 'A7', value = '0.011')
pt.add_parameter(name = 'E7', value = '0.0')

pt.add_parameter(name = 'A8', value = '1.0e+11')
pt.add_parameter(name = 'E8', value = '186606.4')

pt.add_parameter(name = 'A9', value = '1.0e+12')
pt.add_parameter(name = 'E9', value = '146440')

pt.add_parameter(name = 'A10', value = '1.0e+10')
pt.add_parameter(name = 'E10', value = '116524.4')

pt.add_parameter(name = 'A11', value = '3.1e+12')
pt.add_parameter(name = 'E11', value = '97487.2')

pt.add_parameter(name = 'A12', value = '5.0e+6')
pt.add_parameter(name = 'E12', value = '63596.8')

pt.add_parameter(name = 'A13', value = '1.0e+7')
pt.add_parameter(name = 'E13', value = '82006.4')

pt.add_parameter(name = 'A14', value = '3.1e+11')
pt.add_parameter(name = 'E14', value = '32216.8')

pt.add_parameter(name = 'A15', value = '1.0e+5')
pt.add_parameter(name = 'E15', value = '65688.8')

pt.add_parameter(name = 'A16', value = '1.0e+7')
pt.add_parameter(name = 'E16', value = '101420.16')

pt.add_parameter(name = 'A17', value = '1.0e+5')
pt.add_parameter(name = 'E17', value = '71128.0')

pt.add_parameter(name = 'A18', value = '5.2e+3')
pt.add_parameter(name = 'E18', value = '46024.0')

# Auxiliary coordinates
#coord = pt.lattice.generate_coord('hollow.(0,0,0).simple_cubic')
center = pt.lattice.generate_coord('hollow')
up = pt.lattice.generate_coord('hollow.(0,1,0)')
right = pt.lattice.generate_coord('hollow.(1,0,0)')
down = pt.lattice.generate_coord('hollow.(0,-1,0)')
left = pt.lattice.generate_coord('hollow.(-1,0,0)')

#==============================================================================
#define processess
#1 CH4+*=>CH4*
pt.add_process(name='reaction_1',
               conditions=[Condition(coord=center, species='empty')],
               actions=[Action(coord=center, species='CH4_ads')],
               rate_constant='p_CH4*A1*exp(E1/(R*T))')
#2 CH4*=>CH4+*
pt.add_process(name='reaction_2',
               conditions=[Condition(coord=center, species='CH4_ads')],
               actions=[Action(coord=center, species='empty')],
               rate_constant='A2*exp(E2/(R*T))')
#3 CH4*+*=>CH3*+H*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='CH4_ads'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='CH3_ads'),
                 Action(coord=coord, species='H_ads')]
    pt.add_process(name = 'reaction_3__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A3*exp(E3/(R*T))')

#4 CH3*+*=>CH2*+H*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='CH3_ads'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='CH2_ads'),
                 Action(coord=coord, species='H_ads')]
    pt.add_process(name = 'reaction_4__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A4*exp(E4/(R*T))')
#5 CH2*+*=>CH*+H*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='CH2_ads'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='CH_ads'),
                 Action(coord=coord, species='H_ads')]
    pt.add_process(name = 'reaction_5__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A5*exp(E5/(R*T))')
#6 CH*+*=>C*+H*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='CH_ads'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='C_ads'),
                 Action(coord=coord, species='H_ads')]
    pt.add_process(name = 'reaction_6__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A6*exp(E6/(R*T))')
#7 O2+2*=>2O*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='empty'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='O_ads'),
                 Action(coord=coord, species='O_ads')]
    pt.add_process(name = 'reaction_7__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A7*exp(E7/(R*T))')
#8 2O*=>O2+*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='O_ads'),
                 Condition(coord=coord, species='O_ads')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_8__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A8*exp(E8/(R*T))',tof_count = {'O2_production':1})
#9 C*+O*=>CO*+*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='C_ads'),
                 Condition(coord=coord, species='O_ads')]
    ads_acts  = [Action(coord=center, species='CO_ads'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_9__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A9*exp(E8/(R*T))')
#10 CO*=>CO+*
pt.add_process(name='reaction_10',
               conditions=[Condition(coord=coord, species='CO')],
               actions=[Action(coord=coord, species='empty')],
               rate_constant='A10*exp(E10/(R*T))',tof_count = {'CO_production':1})
#11 2H*=>H2+2*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='H_ads'),
                 Condition(coord=coord, species='H_ads')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_11__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A11*exp(E11/(R*T))',tof_count = {'H2_production':1})
#12 CO*+O*=>CO2+2*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='CO_ads'),
                 Condition(coord=coord, species='O_ads')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_12__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A12*exp(E12/(R*T))',tof_count = {'CO2_production':1})
#13 H*+O*=>OH*+*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='H_ads'),
                 Condition(coord=coord, species='O_ads')]
    ads_acts  = [Action(coord=center, species='OH_ads'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_13__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A13*exp(E13/(R*T))')
#14 H*+OH*=>H2O+2*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='H_ads'),
                 Condition(coord=coord, species='OH_ads')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_14__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A14*exp(E14/(R*T))',tof_count = {'H2O_production':1})
#15 O*=>Ox
pt.add_process(name='reaction_15',
               conditions=[Condition(coord=coord, species='O_ads')],
               actions=[Action(coord=coord, species='Ox')],
               rate_constant='A14*exp(E14/(R*T))')
#16 C*+Ox=>CO*+*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='C_ads'),
                 Condition(coord=coord, species='Ox')]
    ads_acts  = [Action(coord=center, species='CO_ads'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_16__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A16*exp(E16/(R*T))')
#17 CO*+Ox=>CO2+2*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='CO_ads'),
                 Condition(coord=coord, species='Ox')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_17__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A17*exp(E17/(R*T))',tof_count = {'CO2_production':1})
#18 H*+Ox=>OH*+*
for i, coord in enumerate([up,right,down,left]):
    ads_conds = [Condition(coord=center, species='H_ads'),
                 Condition(coord=coord, species='Ox')]
    ads_acts  = [Action(coord=center, species='OH_ads'),
                 Action(coord=coord, species='empty')]
    pt.add_process(name = 'reaction_18__{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'A18*exp(E18/(R*T))')
#==============================================================================
pt.print_statistics()
pt.filename='POM_on_surface.xml'
pt.save()