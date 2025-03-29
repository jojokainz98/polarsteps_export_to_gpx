# Create GPX files for a polarsteps Trip
Due to the fact that polarsteps do not provide the functionality to export trip data as GPX files directly,
I created simple python code to convert the exportable data to gpx files.

Currently, there are two version available:
1. **complete** - to get the trip as a single gpx file
2. **daily** - to get a single gpx file for each day

## Steps to get GPX Files from your Trip
1. Download a copy of your data from polarsteps as described 
on their [website](https://support.polarsteps.com/hc/en-nl/articles/24266264821138-How-can-I-export-a-copy-of-my-data#:~:text=Log%20in%20at%20www.polarsteps,a%20copy%20of%20your%20data%22).
2. unzip the `user_data.zip` file
3. navigate to the trip you are interested in ( `..\trip\my_example_trip_1234567`)
4. run the changed python file with your `locations.json` file