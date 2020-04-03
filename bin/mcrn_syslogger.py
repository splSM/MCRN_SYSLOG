
from datetime import datetime as dt, timedelta as td
from random import randint as rand, choice as choose
from time import sleep as snooze

def mcrn_syslogger():
   #############################################################################
   ### DRIVE DIAGNOSTIC CYCLE REPORT:
   when = dt.utcnow()
   choices = ['nom'] * 80 + ['chk'] * 15 + ['err!'] * 5
   reactor = choose(choices)
   thrust = rand(6013579, 6370000)
   Isp = rand(1768971, 1927000)
   Ve1 = rand(4, 6); Ve2 = rand(1, 8)
   mfr1 = rand(1, 2); mfr2 = rand(1, 9)
   thP1 = rand(57, 60); thP2 = rand(1, 9)
   tpo1 = rand(93,96); tpo2 = rand(1, 79)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive diagnostic cycle" report="' + when.strftime('%H:%M:%S') + ': r:' + reactor + ' | t:' + str(thrust) + 'N | Isp:' + str(Isp) + 's | Ve:' + str(Ve1) + '.' + str(Ve2) + '%ls | mfr:' + str(mfr1) + '.' + str(mfr2) + 'kg/s | thP:' + str(thP1) + '.' + str(thP2) + 'tw | tpo:' + str(tpo1) + '.' + str(tpo2) + 'tw"' )
   #############################################################################
   ### PRIMARY LOCK SYSTEMS:
   when = dt.utcnow()
   if when.strftime('%M')[1] in [ '0', '2', '4', '6', '8' ] and when.strftime('%S')[0] in [ '3' ]:
      values_status = [ 'LOCKED' ] * 60 + ['UNLOCKED'] * 40
      values_method = [ 'PIN', 'MANUAL' ]
      values_byWhom = [ 'CHRISSIE', 'BURTONA', 'GUNNY', 'HOLDENJ', 'KAMALA', 'NAGATAN', 'PEACHES', 'PRAXTHEMENG' ]
      ########### LOCK CPS-01:
      status = choose( values_status )
      if status == 'UNLOCKED':
         method = choose( values_method )
         if method == 'PIN':
            byWhom = choose( values_byWhom )
         else:
            byWhom = 'N/A'
      else:
         method = 'N/A'; byWhom = 'N/A'
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="lock status" lock="CPS-01" status="' + status + '" unlock_method="' + method + '" unlocked_by="' + byWhom + '"' )
      ########### LOCK CPS-02:
      status = choose( values_status )
      if status == 'UNLOCKED':
         method = choose( values_method )
         if method == 'PIN':
            byWhom = choose( values_byWhom )
         else:
            byWhom = 'N/A'
      else:
         method = 'N/A'; byWhom = 'N/A'
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="lock status" lock="CPS-02" status="' + status + '" unlock_method="' + method + '" unlocked_by="' + byWhom + '"' )
      ########### LOCK CPS-03:
      status = choose( values_status )
      if status == 'UNLOCKED':
         method = choose( values_method )
         if method == 'PIN':
            byWhom = choose( values_byWhom )
         else:
            byWhom = 'N/A'
      else:
         method = 'N/A'; byWhom = 'N/A'
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="lock status" lock="CPS-03" status="' + status + '" unlock_method="' + method + '" unlocked_by="' + byWhom + '"' )
      ########### LOCK CPS-04:
      status = choose( values_status )
      if status == 'UNLOCKED':
         method = choose( values_method )
         if method == 'PIN':
            byWhom = choose( values_byWhom )
         else:
            byWhom = 'N/A'
      else:
         method = 'N/A'; byWhom = 'N/A'
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="lock status" lock="CPS-04" status="' + status + '" unlock_method="' + method + '" unlocked_by="' + byWhom + '"' )
      ########### LOCK CPS-05:
      status = choose( values_status )
      if status == 'UNLOCKED':
         method = choose( values_method )
         if method == 'PIN':
            byWhom = choose( values_byWhom )
         else:
            byWhom = 'N/A'
      else:
         method = 'N/A'; byWhom = 'N/A'
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="lock status" lock="CPS-05" status="' + status + '" unlock_method="' + method + '" unlocked_by="' + byWhom + '"' )
   #############################################################################
   ### SUB-SYSTEM STATUS:
   when = dt.utcnow()
   if when.strftime('%M')[1] in [ '1', '3', '5', '7', '9' ]:
      choices = ['N'] * 60 + ['C'] * 30 + ['E!'] * 10
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="ASTRO_GEO" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="AUTOPILOT" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="DOCK_CLAMP" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="FILTER_A" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="FILTER_W" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="GALL_COFFEE" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="GALL_COOK" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="GALL_FRIDGE" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="HOLD_CRANE" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="CLIMATE" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="COMMS_INT" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="CPIT_CTRL" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="LIGHTING" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="1" system="LOCKS_INT" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="MED_AUTODOC" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="MED_MONITOR" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="RAIL_TARG" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="REACT_INIT" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="REACT_CONTAIN" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="REACT_CHILLOUT" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="PDC_ACQ" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="PDC_TARG" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="PDC_TRACK" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="THRUST_CTRL" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="TORP_ACQ" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="TORP_TARG" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="TORP_TRACK" status="' + status[0] + '"' )
      status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="sub-system status" column="2" system="WASTE_MGMT" status="' + status[0] + '"' )
   #############################################################################
   ### SELECTED INVENTORY ITEM:
   when = dt.utcnow()
   if when.strftime('%M')[1] in [ '0', '2', '6', '8' ]:
      power = rand(11, 89); efficiency = rand(39, 99); error_rate = rand(3, 59); cleanup = rand(69, 99)
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="1_LFEIPB4UJ" item="40mm Secondary Display System" class="III" state="OK" status="Online" power="' + str(power) + '" efficiency="' + str(efficiency) + '" error_rate="' + str(error_rate) + '" cleanup="' + str(cleanup) + '" log="{[\'date\':\'2020-03-23\',\'work\':\'created rollback point and patched firmware to newest version\',\'modification\':\'mod1\',\'by\':\'BURTONA\'],[\'date\':\'2020-03-25\',\'work\':\'rolled firmware to restore point due to screen tearing issue\',\'modification\':\'mod2\',\'by\':\'PEACHES\']}"' )
   #############################################################################
   ### DOOR SYSTEM INTEGRITY:
   when = dt.utcnow()
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="A01" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="A02" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA1" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA2" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA3" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA4" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="C11" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="D23" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="E01" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="E02" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="H01" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="M1A" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="M16" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="N77" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="P29" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="P76" integrity="' + str(integrity) + '"' )
   integrity = rand(71, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="P77" integrity="' + str(integrity) + '"' )
   #############################################################################
   ### PRESSURE VALVE 2:
   when = dt.utcnow()
   seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V02" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
   #############################################################################
   ### TORPEDO FUEL DORSAL
   when = dt.utcnow()
   value = rand(89,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo fuel" tube="dorsal" fuel="' + str(value) + '"' )
   #############################################################################
   ### DRIVE PLUME WASTE 1:
   when = dt.utcnow()
   waste = rand(11, 39)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="01" waste="' + str(waste) + '"' )
   #############################################################################
   ### FORE THRUSTER PERFORMANCE:
   when = dt.utcnow()
   performance = rand(79, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="thruster performance" thruster="fore" performance="' + str(performance) + '"' )
   #############################################################################
   ### REACTOR CONTAINMENT FIELD PERFORMANCE:
   when = dt.utcnow()
   performance = rand(89, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="containment field integrity" performance="' + str(performance) + '"' )
   #############################################################################
   ### POWER MAIN ALFA:
   when = dt.utcnow()
   power =  rand(11, 97)
   kw = rand(19, 25)
   dtr=kw*27
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="01" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
   #############################################################################
   ### PRESSURE VALVE 5:
   time = dt.utcnow()
   seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V05" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
   #############################################################################
   ###  TORPEDO PROJECTIONS VENTRAL:
   when = dt.utcnow()
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected specific impulse" metric_abbrev="pIsp" value="' + str(value) + '"' )
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected impulse" metric_abbrev="pI" value="' + str(value) + '"' )
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected thrust" metric_abbrev="pTh" value="' + str(value) + '"' )
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected mass ratio" metric_abbrev="pMR" value="' + str(value) + '"' )
   #############################################################################
   ### REACTOR INJECTOR ANTIMATTER:
   when = dt.utcnow()
   performance = rand(79, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="injector integrity - antimatter" performance="' + str(performance) + '"' )
   #############################################################################
   ### DRIVE PLUME WASTE 3:
   when = dt.utcnow()
   waste = rand(29, 79)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="03" waste="' + str(waste) + '"' )
   #############################################################################
   ### INTERNAL PRESSURE:
   when = dt.utcnow()
   metric = rand(3, 25); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure bars Internal Pressure" metric="' + str(metric) + '"' )
   #############################################################################
   ### POWER MAIN DELTA:
   when = dt.utcnow()
   power =  rand(11, 97)
   kw = rand(19, 25)
   dtr=kw*27
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="04" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
   #############################################################################
   ### PRESSURE SENSOR STATUS:
   when = dt.utcnow()
   choices = ['Nominal'] * 60 + ['Check'] * 30 + ['Error!'] * 10
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="CREW01" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="CREW02" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="MED01" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="MED02" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="OPS01" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="OPS02" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="OPS03" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD01" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD02" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD03" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD04" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="ENG01" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="ENG02" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="ENG03" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="GALL01" sensor_status="' + status + '"' )
   status = choose(choices); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="SHOP01" sensor_status="' + status + '"' )
   #############################################################################
   ### PRESSURE VALVE 3:
   time = dt.utcnow()
   seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V03" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
   #############################################################################
   ### REACTOR OVERALL EFFICIENCY:
   when = dt.utcnow()
   performance = rand(79, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="overall efficiency" performance="' + str(performance) + '"' )
   #############################################################################
   ### OXYGEN / C02:
   time = dt.utcnow()
   metric = rand(89, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure bars Oxygen/C02" metric="' + str(metric) + '"' )
   #############################################################################
   ### TORPEDO FUEL VENTRAL:
   time = dt.utcnow()
   value = rand(89,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo fuel" tube="ventral" fuel="' + str(value) + '"' )
   #############################################################################
   ### DRIVE PLUME WASTE 5:
   when = dt.utcnow()
   waste = rand(49, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="05" waste="' + str(waste) + '"' )
   #############################################################################
   ### COMMS STATUS BARS:
   when = dt.utcnow()
   value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="throughput" value="' + str(value) + '"' )
   value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="resolution" value="' + str(value) + '"' )
   value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="cleanup" value="' + str(value) + '"' )
   value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="receiver" value="' + str(value) + '"' )
   value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="transmitter" value="' + str(value) + '"' )
   #############################################################################
   ### POWER MAIN BRAVO:
   when = dt.utcnow()
   power =  rand(11, 97)
   kw = rand(19, 25)
   dtr=kw*27
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="02" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
   #############################################################################
   ### TORPEDO PROJECTIONS DORSAL:
   when = dt.utcnow()
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected specific impulse" metric_abbrev="pIsp" value="' + str(value) + '"' )
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected impulse" metric_abbrev="pI" value="' + str(value) + '"' )
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected thrust" metric_abbrev="pTh" value="' + str(value) + '"' )
   value = rand(79,99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected mass ratio" metric_abbrev="pMR" value="' + str(value) + '"' )
   #############################################################################
   ### PRESSURE VALVE 4:
   time = dt.utcnow()
   seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V04" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
   #############################################################################
   ### EXTERNAL PRESSURE:
   when = dt.utcnow()
   metric = rand(3, 25); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure bars External Pressure" metric="' + str(metric) + '"' )
   #############################################################################
   ### DRIVE PLUME WASTE 2:
   when = dt.utcnow()
   waste = rand(19, 59)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="02" waste="' + str(waste) + '"' )
   #############################################################################
   ### REACTOR INJECTOR DEUTERIUM:
   when = dt.utcnow()
   performance = rand(79, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="injector integrity - deuterium" performance="' + str(performance) + '"' )
   #############################################################################
   ### AFT THRUSTER PERFORMANCE:
   when = dt.utcnow()
   performance = rand(79, 99)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="thruster performance" thruster="aft" performance="' + str(performance) + '"' )
   #############################################################################
   ### PRESSURE VALVE 1:
   time = dt.utcnow()
   seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V01" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
   #############################################################################
   ### POWER MAIN CAIN IS FOR CHARLIE AND DELTA IS FOR CAIN:
   when = dt.utcnow()
   power =  rand(11, 97)
   kw = rand(19, 25)
   dtr=kw*27
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="03" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
   #############################################################################
   ### DRIVE PLUME WASTE 4:
   when = dt.utcnow()
   waste = rand(39, 89)
   print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="04" waste="' + str(waste) + '"' )

allThisHasHappenedBefore = 0
while allThisHasHappenedBefore < 999999999:
      mcrn_syslogger()
      snooze(11)
      allThisHasHappenedBefore = allThisHasHappenedBefore + 1

#############################################################################
### THERE WAS A BUTTON. I PUSHED IT.
