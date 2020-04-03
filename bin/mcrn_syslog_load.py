
from datetime import datetime as dt, timedelta as td
from random import randint as rand, choice as choose
from splunk.clilib import cli_common as cli
from time import sleep as snooze
import requests as r, sys, os

splunk_dir = os.environ['SPLUNK_HOME']
local_path = splunk_dir + '/etc/apps/mcrn_syslog/local'
local_conf = local_path + '/mcrn.conf'

if os.path.exists( local_path ):
   if os.path.exists ( local_conf ):
      with open ( local_conf, 'r' ) as CONF:
           stanza = CONF.read()
           if 'reload_backlog = 1' not in stanza:
              exit(0)
   else:
      exit(0)
else:
   exit(0)

#############################################################################
### DOOR SYSTEM INTEGRITY:

time = dt.utcnow()
when = time - td(days = 91)

while when != time:
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="A01" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="A02" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA1" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA2" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA3" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="BA4" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="C11" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="D23" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="E01" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="E02" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="H01" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="M1A" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="M16" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="N77" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="P29" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="P76" integrity="' + str(event_value) + '"' )
      event_value = rand(51, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="system integrity" system="P77" integrity="' + str(event_value) + '"' )
      when = when + td(hours = 1)

#############################################################################
### PRESSURE CONTROL STATUS:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

while when != stop:
      ########### VALVE 01
      seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V01" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
      ########### VALVE 02
      seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V02" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
      ########### VALVE 03
      seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V03" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
      ########### VALVE 04
      seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V04" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
      ########### VALVE 05
      seal = rand(81, 100); inlet = rand(81, 100); housing = rand(81, 100); pressure = rand(81, 100);
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure control valve" pressure_valve="V05" seal_strength="' + str(seal) + '" inlet_strength="' + str(inlet) + '" housing_integrity="' + str(housing) + '" pressure="' + str(pressure) + '"' )
      when = when + td(hours = 1)

#############################################################################
### PRESSURE SENSOR STATUS:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

choices = ['Nominal'] * 60 + ['Check'] * 30 + ['Error!'] * 10

while when != stop:
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="CREW01" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="CREW02" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="MED01" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="MED02" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="OPS01" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="OPS02" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="OPS03" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD01" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD02" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD03" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="HOLD04" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="ENG01" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="ENG02" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="ENG03" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="GALL01" sensor_status="' + status + '"' )
      status = choose(choices); print( 'timestemp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure sensor" sensor_id="SHOP01" sensor_status="' + status + '"' )
      when = when + td(hours = 1)

#############################################################################
### PRESSURE / C02 BAR CHART:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

while when != stop:
      ########### EXTERNAL PRESSURE (LOWER IS BETTER):
      metric = rand(3, 25); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure bars External Pressure" metric="' + str(metric) + '"' )
      ########### INTERNAL PRESSURE (LOWER IS BETTER):
      metric = rand(3, 25); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure bars Internal Pressure" metric="' + str(metric) + '"' )
      ########### OXYGEN TO C02 RATIO (HIGHER IS BETTER):
      metric = rand(89, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="pressure bars Oxygen/C02" metric="' + str(metric) + '"' )
      when = when + td(hours = 1)

#############################################################################
### LOCKING SYSTEM STATUS:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

values_status = [ 'LOCKED' ] * 70 + ['UNLOCKED'] * 30
values_method = [ 'PIN', 'MANUAL' ]
values_byWhom = [ 'CHRISSIE', 'BURTONA', 'GUNNY', 'HOLDENJ', 'KAMALA', 'NAGATAN', 'PEACHES', 'PRAXTHEMENG' ]

while when != stop:
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
      when = when + td(hours = 1)

#############################################################################
### SUB-SYSTEM STATUS TABLE:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

choices = ['N'] * 60 + ['C'] * 30 + ['E!'] * 10

while when != stop:
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
      when = when + td(hours = 1)

#############################################################################
### CONSOLE SELECTED SYSTEM BARS - COMMS:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

while when != stop:
      value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="throughput" value="' + str(value) + '"' )
      value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="resolution" value="' + str(value) + '"' )
      value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="cleanup" value="' + str(value) + '"' )
      value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="receiver" value="' + str(value) + '"' )
      value = rand(69, 100); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="console selected system" metric="transmitter" value="' + str(value) + '"' )
      when = when + td(hours = 1)

#############################################################################
### POWER STATUS:

time = dt.utcnow()
when = time - td(days = 8)
data = ''

while when != time:
      ########### MAIN 01:
      power =  rand(11, 97); kw = rand(19, 25); dtr=kw*27
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="01" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
      ########### MAIN 02:
      power =  rand(11, 97); kw = rand(19, 25); dtr=kw*27
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="02" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
      ########### MAIN 03:
      power =  rand(11, 97); kw = rand(19, 25); dtr=kw*27
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="03" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
      ########### MAIN 04:
      power =  rand(11, 97); kw = rand(19, 25); dtr=kw*27
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="power main" main="04" power="' + str(power) + '" max_throughput="' + str(kw) + '" days_til_repair="' + str(dtr) + '"' )
      when = when + td(hours = 1)

#############################################################################
### DRIVE DIAGNOSTIC CYCLE REPORT:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

choices = ['nom'] * 80 + ['chk'] * 15 + ['err!'] * 5

while when != stop:
      reactor = choose(choices)
      thrust = rand(6013579, 6370000)
      Isp = rand(1768971, 1927000)
      Ve1 = rand(4, 6); Ve2 = rand(1, 8)
      mfr1 = rand(1, 2); mfr2 = rand(1, 9)
      thP1 = rand(57, 60); thP2 = rand(1, 9)
      tpo1 = rand(93,96); tpo2 = rand(1, 79)
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive diagnostic cycle" report="09:45:00 | r:' + reactor + ' | t:' + str(thrust) + 'N | Isp:' + str(Isp) + 's | Ve:' + str(Ve1) + '.' + str(Ve2) + '%ls | mfr:' + str(mfr1) + '.' + str(mfr2) + 'kg/s | thP:' + str(thP1) + '.' + str(thP2) + 'tw | tpo:' + str(tpo1) + '.' + str(tpo1) + 'tw"' )
      when = when + td(hours = 1)

#############################################################################
### THRUSTERS & REACTOR PERFORMANCE:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

while when != stop:
      performance = rand(79, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="thruster performance" thruster="fore" performance="' + str(performance) + '"' )
      performance = rand(79, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="thruster performance" thruster="aft" performance="' + str(performance) + '"' )
      performance = rand(79, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="overall efficiency" performance="' + str(performance) + '"' )
      performance = rand(89, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="containment field integrity" performance="' + str(performance) + '"' )
      performance = rand(79, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="injector integrity - antimatter" performance="' + str(performance) + '"' )
      performance = rand(79, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="reactor performance" metric="injector integrity - deuterium" performance="' + str(performance) + '"' )
      when = when + td(hours = 1)

#############################################################################
### DRIVE PLUME WASTE:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 25)

while when != stop:
      ########### SENSOR 01 (CLOSE TO NOZZLE; LOW WASTE EXPECTED)
      waste = rand(11, 39); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="01" waste="' + str(waste) + '"' )
      ########### SENSOR 02 (CLOSE-ISH TO NOZZLE; LOW-TO-MEDIUM WASTE EXPECTED)
      waste = rand(19, 59); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="02" waste="' + str(waste) + '"' )
      ########### SENSOR 03 (NOT CLOSE TO NOZZLE; MEDIUM WASTE EXPECTED)
      waste = rand(29, 79); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="03" waste="' + str(waste) + '"' )
      ########### SENSOR 04 (FAR FROM NOZZLE; MEDIUM-TO-HIGH WASTE EXPECTED)
      waste = rand(39, 89); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="04" waste="' + str(waste) + '"' )
      ########### SENSOR 05 (A LONG DAMN WAY FROM THE NOZZLE NOZZLE; HIGH WASTE EXPECTED)
      waste = rand(49, 99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="drive plume waste" sensor="05" waste="' + str(waste) + '"' )
      when = when + td(hours = 1)

#############################################################################
### ASSORTED TORPEDO GOODIES:

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(hours = 3)

print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo control scrubber" position="50"' )

while when != stop:
      value = rand(89,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo fuel" tube="dorsal" fuel="' + str(value) + '"' )
      value = rand(89,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo fuel" tube="ventral" fuel="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected specific impulse" metric_abbrev="pIsp" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected impulse" metric_abbrev="pI" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected thrust" metric_abbrev="pTh" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="dorsal" metric="projected mass ratio" metric_abbrev="pMR" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected specific impulse" metric_abbrev="pIsp" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected impulse" metric_abbrev="pI" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected thrust" metric_abbrev="pTh" value="' + str(value) + '"' )
      value = rand(79,99); print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="torpedo metrics" tube="ventral" metric="projected mass ratio" metric_abbrev="pMR" value="' + str(value) + '"' )
      when = when + td(hours = 1)

#############################################################################
### INVENTORY LISTING:

when = dt.utcnow()

values_state = [ 'OK', 'NOT OK' ]
weight_state = [ 0.8, 0.2 ]
values_status = [ 'Online', 'Offline' ]
weight_status = [ 0.8, 0.2 ]

values_state = ['OK'] * 80 + ['NOT OK'] * 20
values_status = ['Online'] * 80 + ['Offline'] * 20

state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="4PDFS1FAGDD" item="42mm Secondary Display System" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="C0DIT27F7BE" item="CNRY-112 EWAR Camera Array" class="V" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="KQ69N9IPZ.R" item="53mm Primary Display System" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="T7.4US3ALNA" item="Handheld NAV/COM Tranceiver" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="G7YIR5_PU4F" item="Communications Buffer A" class="II" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="9_SLL06_MWY" item="Communications Buffer B" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="IJ7RR.UXM76" item="Electromagnetic Shield" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="B94.QJCWCNB" item="Full Spectrum Analyzer" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="18KV9YJEPJF" item="Ordnance Calibration Unit" class="V" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial=".EQTNGV0KOJ" item="Telemetry Analyzer" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="FJAW1T8_XZ7" item="Discrete Input Sequencer" class="II" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="MS1BWSXROA2" item="Antipersonnel Control Unit" class="I" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="K5HEUN03V_G" item="Entry Monitoring Control Panel" class="II" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="WYGZ1HW3.K9" item="Twin Strut Absorption Tube" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="0G.B8D5AHXC" item="Control Unit Driver" class="II" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="UM87W4G0DGM" item="Air Filtration/Treatment System" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="9T6UVMPZ.E9" item="Inertial Reference Unit" class="II" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="8S66.DQOV_H" item="Thermal Cell Secondary" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="QR1T19KX206" item="Annual Confinement Array" class="II" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="HNZVRFCF3J8" item="Deuterium Injector Assembly" class="IV" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="X9N2W66WJ0Z" item="Thermal Cell Primary" class="IV" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="3AQ93M4TCV6" item="Bussard Collectors Ventral" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="VE9B684ZHZ6" item="Bussard Collectors Dorsal" class="III" state="' + state + '" status="' + status + '" log="{}"')
state = choose(values_state); status = choose(values_status)
print('timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="QR1T19KX206" item="Annular Confinement Array" class="II" state="' + state + '" status="' + status + '" log="{}"')

time = dt.utcnow()
stop = time + td(hours = 1)
when = stop - td(days = 8)
log1 = time - td(days = 11)
log2 = time - td(days = 9)

while when != stop:
      power = rand(51, 89); efficiency = rand(49, 99); error_rate = rand(3, 44); cleanup = rand(71, 99)
      print( 'timestamp="' + when.strftime('%Y-%m-%dT%H:%M:%SZ') + '" type="inventory" serial="1_LFEIPB4UJ" item="40mm Secondary Display System" class="III" state="OK" status="Offline" power="' + str(power) + '" efficiency="' + str(efficiency) + '" error_rate="' + str(error_rate) + '" cleanup="' + str(cleanup) + '" log="{[\'date\':\'' + log1.strftime('%Y-%m-%d') + '\',\'work\':\'created rollback point and patched firmware to newest version\',\'modification\':\'mod1\',\'by\':\'BURTONA\'],[\'date\':\'' + log2.strftime('%Y-%m-%d') + '\',\'work\':\'rolled firmware to restore point due to screen tearing issue\',\'modification\':\'mod2\',\'by\':\'PEACHES\']}"' )
      when = when + td(hours = 1)

#############################################################################
### BACKLOG LOADED; DON'T LOAD IT AGAIN UNLESS SPECIFICALLY TOLD TO
### AND RELOAD mcrn.conf SO IT SHOWS PROPERLY IN setup.xml:

confD = cli.readConfFile( splunk_dir + '/etc/apps/mcrn_syslog/default/mcrn.conf' )
confL = cli.readConfFile( splunk_dir + '/etc/apps/mcrn_syslog/local/mcrn.conf' )
for name, content in confL.items():
    if name in confD:
       confD[name].update(content)
    else:
       confD[name] = content
conf = confD['backlog']

with open ( local_conf, 'w' ) as CONF:
     CONF.write('[backlog]\ndisabled = 0\nreload_backlog = 0\nmgmt_port = ' + conf['mgmt_port'] + ' \n')

endpoint = 'https://localhost:' + conf['mgmt_port'] + '/servicesNS/nobody/mcrn_syslog/configs/conf-mcrn/_reload?output_mode=json'
head = {'Authorization':'Splunk ' + sys.stdin.read() }
response = r.get( endpoint, headers=head, verify=False )

#############################################################################
### I CAN'T FIGHT PIRATES WITHOUT COFFEE.

