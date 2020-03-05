Python script to take all countlines associated with a project and format them for client facing purposes.

Before executing the python script a csv file containing all countlines for a given project must be downloaded from the metabase custom query section. This is done by searching for countlines, filtered by active countlines only and desired project.

To run the script type the following into the command line in terminal and execute:

python CountsCoords.py 'path to downloaded csvfile'

Copy the entire output and paste it into the countlineIDs table, found within the API guide.
