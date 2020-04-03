FROM:
MARTIAN CONGRESSIONAL REPUBLIC NAVY (MCRN)
SYSTEM & TECHNOLOGY DEVELOPMENT COMMAND (SYSTECHDEVCOM)
DISPLAY & CONTROL DIVISION (DISCONDIV)

TO:
Commander, SYSTECHDEVCOM, MCRN

MEMORANDUM OF SYSTEM VERSION RELEASE

SUBJ: MCRN SYSLOG DISPLAY CONSOLE; CORVETTE IMPLEMENTATION v1.1.1

Sir/Madam,

Attached please find details of the most recent version of the MCRN SYSLOG DISPLAY CONSOLE for CORVETTE-class vessels.

As per SYSTECHDEVCOM guidance, DISCONDIV has leveraged the "new and improved" dashboarding functionality in Splunk v8 to create this version of the MCRN SYSLOG DISPLAY CONSOLE.

The DISPLAY CONSOLE in this version runs seventy-five (75) real-time searches and visualizes live data from multiple shipboard systems. An Event Generator is included so that operations personnel may view historical data and current system events as they are generated.

This system is ready for immediate release and implementation into the systems of vessels which correspond to the class for which this system was developed. DISCONDIV stands ready to assist with deployment and user training, as per SYSTECHDEVCOM policy.

Development Engineer
MCRN SYSLOG DISPLAY CONSOLE Project

cc:
Commander, DISCONDIV, SYSTECHDEVCOM, MCRN

# You MUST have the Splunk Enterprise Dashboards Beta app installed!

# NOTES
- This app consists primarily of a single huge dashboard running 75 real-time searches and two event generators in Python which produce data for the dashboard to visualize.
- The app is designed to emulate interactive display screens as seen on Martian Congressional Republic Navy vessels, as an exercise in "what is possible" with the new dashboarding functionality in Splunk v8.

# INSTALL
- Get the Splunk Enterprise Dashboards Beta app before you try to install MCRN SYSLOG.
- Install of MCRN SYSLOG is fairly self-explanatory.
    - After the initial installation, you will be prompted to restart Splunk so the app's images and such can be loaded for the dashboard.
    - Next, you'll want to enable the Backlog for loading, on the app's Setup page. It is initially turned off so that it will not run prior to the required restart.

# UTILIZE THE MCRN SYSLOG DISPLAY CONSOLE
- The default homepage of the app will take you to the dashboard.
    - THIS DASHBOARD RUNS 75 REAL-TIME SEARCHES. Make sure your server can handle it.
    - The searches may need a minute to catch up. Best to grab a coffee or a märzen after you click Restart, so it has a couple minutes to load. If for some reason you get a bunch of No Results Found which won't go away, go to Activity > Jobs and stop *all* the running Jobs, then load the dashboard again.
