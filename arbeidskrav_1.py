yearly_distance_km = 10000
insurance_el_kr = 5000
insurance_gas_kr = 7500
road_tax_kr_day = 8.38
road_tax_kr_year = (8.38 * 365)
el_kwh_km = 0.2 
el_kr_kWh = 2.00
gas_kr_km = 1.00
el_passage_tax_kr_km = 0.1
gas_passge_tax_kr_km = 0.3




def gasolin_car():
    yearly_cost = (yearly_distance_km * gas_kr_km) + (yearly_distance_km * gas_passge_tax_kr_km) + road_tax_kr_year + insurance_gas_kr
    yearly_cost_str = str(yearly_cost)
    print("Bensinbil koster " + yearly_cost_str + "ckr årlig")
    return yearly_cost

def el_car():
    yearly_cost_el = (yearly_distance_km * el_kr_kWh * el_kwh_km) + (yearly_distance_km * el_passage_tax_kr_km) + road_tax_kr_year + insurance_el_kr
    yearly_cost_str = str(yearly_cost_el)
    print("El-bil koster " + yearly_cost_str + "ckr årlig")
    return yearly_cost_el

def gas_el_car_dif(x, y):
    dif_yearly_cost = x - y
    dif_yearly_cost_str = str(dif_yearly_cost)
    print("Prisforskjellen på årlige utgifter mellom bensinbil og elektrisk bil er " + dif_yearly_cost_str + "ckr, i favør el.")

#gasolin_car()
#el_car()
gas_el_car_dif(gasolin_car(), el_car())