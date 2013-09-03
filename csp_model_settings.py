#
# BASIC SETTINGS
#

# TODO these have to be somehow better managed/generated...
time_res = 6
path_input = 'Input/NA-6hr-2005'
path_output = 'Output'
demand_filename = 'DemandTable_EU.csv'
results_file_json = 'csp_model.json'
D_scale = 0.32
noncsp_avail = 0.0
#i_subset = None
i_subset = [33, 75, 34, 23, 85, 86, 16, 98, 57, 36]

#
# MODEL SETTINGS AND PARAMETERS
#

# General parameters
eff_stor = 1.0  # Storage throughput efficiency [dimensionless]
mu_stor = 0.002  # Storage heat loss rate [per hour]
E_init = 0  # Initial storage contents [kWht]
startup_time = 12  # Initial hours during which backup burner is allowed [h], Default: 12

# Plant sizing
P_max = 100000  # Maximum turbine size [kWe], Default: 20000
sf_max = 7950000  # Maximum solar field size [m2], Default: 318000, overridden if scale_sf is True
E_time = 30  # Maximum storage time [h], Default: 15
E_max = 745321  # Maximum storage size [kWht], Default: 745321, overriden by E_time_ if use_E_time = 1
scale_sf = 32  # Scaling factor for solar field, Default: 15.9, which is the ratio of the Gemasolar plant

# Switches
use_E_time = True  # Use E_time to calculate E_max?
use_scale_sf = False  # Use scale_sf to calculate sf_max based on P_max?

# Costs
csp_rec_per_sf = 0.54  # kWt of receiver needed per m2 of solar field, estimate from Sandia National Labs 2011 baseline price estimate reference plant [dimensionless]
cost_csp_stor = 30  # Cost of storage [USD/kWht]
cost_csp_sf = 200  # Cost of solar field [USD/m2]
cost_csp_rec = 200  # Cost of tower and receiver [EUR/kWt]
cost_csp_pb = 1350  # Cost of power block [USD/kWe]
cost_csp_omfrac = 0  # Yearly O&M costs [fraction of total investment]
cost_csp_omvar = 0.002  # Variable O&M costs [USD/kWe]
cost_noncsp_build = 750  # Cost of construction for non-CSP plants [USD/kWe]
cost_noncsp_fuel = 0.12  # Cost of running non-CSP plants [USD/kWhe]
cost_noncsp_omfrac = 0  # Yearly non-CSP O&M costs [fraction of total investment
interest_csp = 0.10  # Interest rate for CSP plants [dimensionless] (assumption, sensible range is around 0.05-0.15)
interest_noncsp = 0.10  # Interest rate for non-CSP plants [dimensionless] (assumption)
plant_life = 25  # Lifetime of a plant [years] (assumption)

# Objective function weights
lambda_csp = 1
lambda_noncsp = 1
lambda_slack = 1e9
