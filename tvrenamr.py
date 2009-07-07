from tvrenamr_core import TvRenamr
from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-a", "--auto", dest="auto_move", help="Automatically move renamed files to the appropriate directory under the directory specified. Mutually exclusive to -r")
parser.add_option("-l", "--log", dest="logging", help="Set the location for logs to be created in")
parser.add_option("-n", "--name", dest="name", help="Set the show name for renaming")
parser.add_option("-r", "--renamed", dest="renamed_dir", help="The directory to move renamed files to. Mutually exclusive to -a")
parser.add_option("--regex", dest="regex", help="the regular expression to set the format of files being renamed. Use %n to specify the show name, %s for the season number and %e for the episode number. All spaces are converted to periods before the regex is run")
parser.add_option("-s", "--season", dest="season")
parser.add_option("-w", "--working", dest="working_dir", help="The working directory to run tvrenamr in. Required!")
(options, args) = parser.parse_args()

working_dir = options.working_dir
renamed_dir = options.renamed_dir
auto_move = options.auto_move
logging = options.logging
regex = options.regex
#working_dir = "/Users/madnashua/Projects/tvrenamr/core/tests/data/files"
#regex = "%n\.\-\.[Ss]?%s\.E%e"

tv = TvRenamr(working_dir)
for fn in os.listdir(working_dir):
    if auto_move != None:
        #rename and auto move
        try:
            details = tv.extract_episode_details_from_file(fn, user_regex=regex)
            name = tv.retrieve_episode_name(details[0],details[1],details[2])
            path = tv.build_path(details,name,auto_move)
            tv.rename(fn,path)
        except Exception, e:
            print e
            continue
    elif renamed_dir != None:
        #rename and move
        try:
            details = tv.extract_episode_details_from_file(fn, user_regex=regex)
            name = tv.retrieve_episode_name(details[0],details[1],details[2])
            path = tv.build_path(details,name,renaed_dir)
            tv.rename(fn,path)
        except Exception, e:
            print e
            continue
    elif auto_move == None and renamed_dir == None:
        #rename
        try:
            details = tv.extract_episode_details_from_file(fn, user_regex=regex)
            name = tv.retrieve_episode_name(details[0],details[1],details[2])
            path = tv.build_path(details,name)
            tv.rename(fn,path)
        except Exception, e:
            print e
            continue
    else:
        print "incorrect options!"