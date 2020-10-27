# Convert-Firefly

This git provides the most simple way to convert Gadget's simulation in HDF5 format to .json one in order to feed it into Firefly.

It requires the user to already have Firefly downloaded: https://github.com/ageller/Firefly

Once it is done, you can put the python code in the firefly_api folder : Firefly/data/firefly_api (it needs FIREreader to work)

As written in the code, one needs to create a subdirectory in Firefly/data in order to put the .json files in it.

When it is done:

```python
$ python3 -m http.server
```

Then open your browser and enter the url : http://localhost:8000/

Go to the Firefly directory: it will launch the app. Click on the screen and select the directory from your startup file (it will show you the inner example of Firefly and the one you have create).

If not, you have to modify startup.json in Firefly/data.
If the code line is: 
```python
{"0":"data\/isolatedGalaxy_s50"}
```
Then change it to: 
```python
{"0":"data\/isolatedGalaxy_s50","1":"data\/..."} 
```
and replace "..." with the name of the subdirectory in which there is your .json files. But normally the python code of Firefly do it for you.
If not, check reader.py in Firefly/data/firefly_api if the line 23 is as follows:

```python
write_startup = 'append',# True -> write | False -> leave alone | "append" -> adds to existing file
```

This command line append the new subdirectory if it is not in startup.json when you execute the python code (it checks if the subdirectory in which you put the json file already exist or not).
