import random
import json
import os.path
import math

# Represents an instance of a list of elements that need to be ranked and an ordered list of ranked elements
class Ranker:

  # Initialize the to_rank and ranked lists
  def __init__(self, to_rank, ranked):
    self.to_rank = to_rank
    self.ranked = ranked

  # Returns a JSON representation of the current object
  def JSON_form(self):
    return json.dumps(self.__dict__)

  # This will rank one element and add it to the ranked list
  def rank(self):
    current = self.to_rank[0]
    start = 0
    end = len(self.ranked) - 1
    mid = 0
    response = 0
    previous_bounds = []

    # Perform binary search to find the correct insertion location
    while start <= end:
      mid = (start + end) // 2

      response = 0
      while response < 1 or response > 10:
        try:
          text = "Which should be ranked higher: " + str(current) + " or " + str(self.ranked[mid]) + "? (1 or 2, 9 for more options): "
          response = int(input(text))
        except ValueError:
          pass

      # Option 1 was better
      if response == 1:
        previous_bounds.append(start)
        previous_bounds.append(end)
        end = mid-1

      # Option 2 was better
      elif response == 2:
        previous_bounds.append(start)
        previous_bounds.append(end)
        start = mid+1

      # Print to_rank and ranked lists
      elif response == 3:
        print("\n\n- List of things to rank in to_rank (size " + str(len(to_rank)) + "):\t" + str(to_rank))
        print("\n- List of ranked things in ranked (size " + str(len(ranked)) + "):\t" + str(ranked) + "\n")

      # Print how many questions will be asked with the remaining number of elements to rank
      elif response == 4:
        sum_min = 0
        sum_max = 0

        # Calculates the minimum and maximum number of questions 
        for i in range(len(ranked) + 1, len(ranked) + len(to_rank) + 1):
          min_value = math.floor(math.log(i, 2))
          max_value = math.ceil(math.log(i, 2))
          sum_min += min_value
          sum_max += max_value

        print("\n\n- You still have to rank " + str(len(to_rank)) + " thing(s) and " + str(len(ranked)) + " thing(s) have been ranked")
        print("- You have been asked " + str(len(previous_bounds) // 2) + " question(s) trying to rank " + current)
        print("- The numbers listed below assume no questions have been asked trying to rank " + current)

        print("\n- Minimum number of questions remaining is " + str(sum_min))
        print("- Average number of questions remaining is " + str(math.ceil((sum_min + sum_max) / 2)))
        print("- Maximum number of questions remaining is " + str(sum_max) + "\n")

      # Undo previous action
      elif response == 5:
        if len(previous_bounds) > 0:
          end = previous_bounds.pop()
          start = previous_bounds.pop()
        else:
          print("\nNo previous actions for this option")

      # Undo this entry
      elif response == 6:
        return "undo_entry"
      
      # Rerank a previous entry
      elif response == 7:
        entry = False
        print()

        # Run until an entry entered was found to be in the ranked list or the user left it blank
        while not entry:
          text = "Which entry would you like to rerank? (Leave blank to cancel): "
          response = input(text)
          print()

          # Check if what the user entered is a valid entry in the ranked list
          if len(response) > 0:
            entry = response in ranked
            if not entry:
              print("What you entered was not found in the ranked list, please try again.")
            else:
              print("\nFound element \"" + response + "\" in the ranked list, now reranking it")
              return ["rerank_entry", response]

          # User left the input blank, so cancel this request
          else:
            entry = True
      
      # Add or remove an entry
      elif response == 8:
        back1 = True
        print()

        # Run until the user enters "add", "delete", or leaves it blank
        while back1:
          text1 = "Would you like to add or delete an entry? (Type \"add\" or \"delete\", or leave blank to cancel): "
          response1 = input(text1).lower()

          # If the user typed in something
          if len(response1) > 0:
            if response1 == "add":
              back1 = False
              back2 = True
              print()

              # Run until the new entry entered is valid, meaning it is not already in either to_rank or ranked lists, or the user left it blank
              while back2:
                text2 = "What entry would you like to add? (Leave blank to cancel): "
                new_entry = input(text2)

                # If the user typed in something
                if len(new_entry) > 0:
                  if new_entry in to_rank:
                    print("\n" + new_entry + " is already in the list of things to rank")
                  elif new_entry in ranked:
                    print("\n" + new_entry + " is already in the list of ranked things")
                  else:
                    back2 = False
                    back3 = True
                    print()

                    # Run until the user enters "now", "end", "random", or leaves it blank
                    while back3:
                      text3 = "Would you like to rank this now, at the end, or put this somewhere in the middle of things left to rank? (Type \"now\", \"end\", or \"random\", or leave blank to cancel): "
                      insert_request = input(text3).lower()

                      # If the user typed in something
                      if len(insert_request) > 0:
                        if insert_request in ["now", "end", "random"]:
                          return ["add_entry", insert_request, new_entry]
                        else:
                          print("\nInvalid option")
                      
                      # User typed in nothing, so this will go back to the second loop
                      else:
                        back2 = True
                        back3 = False
                        print()

                # User typed in nothing, so this will go back to the first loop
                else:
                  back1 = True
                  back2 = False
                  print()

            
            elif response1 == "delete":
              print("Feature to be added")
              text = "What entry would you like to delete? (Leave blank to cancel): "
              response2 = input(text)

            # User did not type in "add", "delete", or nothing
            else:
              print("\nInvalid option")
          
          # User typed in nothing, so cancel this request
          else:
            back1 = False
        
        print("\n")

      # Help menu
      elif response == 9:
        print("\nValid options:")
        print(" 1: Option 1 is better")
        print(" 2: Option 2 is better")
        print(" 3: Print the current list of remaining things to rank and the list of ranked things")
        print(" 4: Print the remaining number of questions that will be asked")
        print(" 5: Undo most recent action (will compare option 1 back to the previous option 2)")
        print(" 6: Undo this entry and rerank the previous entry")
        print(" 7: Remove an entry from the ranked list and rerank it")
        print(" 8: Add or delete an entry")
        print(" 9: Display this help menu")
        print("10: Exit program\n")

      # Quit the program on all other valid options
      else:
        quit()

    # Insertion changes based on whether option 1 or 2 was selected last
    if response == 1:
      self.ranked.insert(mid, current)
    else:
      self.ranked.insert(mid+1, current)

    del self.to_rank[0]
    return json.dumps(self.__dict__)


# Start of program with default values
filename = ""
to_rank = []
ranked = []

# Checking if the user would like to create a new list or read from an existing one
response = 0
while response == None or response < 1 or response > 3:
  try:
    response = int(input("Would you like to create a new file or read from an existing file? (1 or 2): "))
  except ValueError:
    pass

# Create new file and ranking list
if response == 1:
  filename = input("What should the filename be? (Include the path): ")
  if os.path.exists(filename):
    print("File already exists, exiting program.")
    quit()

  # Runs until the user is done adding things to rank
  response = None
  while response != "":
    response = input("Enter something to rank (leave this blank to stop adding elements): ")

    # Checks if the user wants to stop adding elements to the to_rank list
    if len(response) > 0:
      if response in to_rank:
        print("\nWhat you entered is already in the list, please try again.")
      else:
       to_rank.append(response)
       print("\nEntered \"" + response + "\" into the list of things to rank.")

  # Runs until the user is done adding ranked things
  print("\n")
  response = None
  while response != "":
    response = input("Enter an entry that is already ranked (insert in ascending order, leave this blank to stop adding elements): ")

    # Checks if the user wants to stop adding elements to the ranked list
    if len(response) > 0:
      if response in to_rank:
        print("\nWhat you entered is already in the list of things to rank, please try again.")
      elif response in ranked:
        print("\nWhat you entered is already in the list of ranked things, please try again.")
      else:
       ranked.append(response)
       print("\nAppended \"" + response + "\" into the list of ranked things.")
  
  # Shuffles the to_rank list if the user requests it
  response = 0
  while response < 1 or response > 2:
    try:
      response = int(input("\nShuffle the list of things to rank? (1 for yes, 2 for no): "))
      if response == 1:
        random.shuffle(to_rank)
    except ValueError:
      pass

  # Initial write before anything is added to ranked
  with open(filename, "w") as writer:
    json.dump(Ranker(to_rank, ranked).JSON_form(), writer)
    writer.write("\n")


# Find existing file
elif response == 2:
  filename = input("What is the filename? (Include the path): ")
  if not os.path.exists(filename):
    print("File was not found, exiting program.")
    quit()
  
  # Read the existing JSON lines from the file
  with open(filename, "r") as reader:
    lines = reader.readlines()

  # Read the last JSON line and put its values into the to_rank and ranked lists
  obj = json.loads(json.loads(lines[-1]))
  to_rank = obj["to_rank"]
  ranked = obj["ranked"]


# Debug (use a list manually put into the code)
else:
  filename = "test.txt"
  to_rank = ["A", "B", "C", "D", "E"]
  ranked = []

  # Initial write before anything is added to ranked
  with open(filename, "w") as writer:
    json.dump(Ranker(to_rank, ranked).JSON_form(), writer)
    writer.write("\n")



# Will run until there is nothing left to rank
while len(to_rank) > 0:

  if len(to_rank) == 1:
    print("\n" + str(len(to_rank)) + " thing left to rank.")
  elif len(ranked) != 0:
    print("\n" + str(len(to_rank)) + " things left to rank.")

  tuple = Ranker(to_rank, ranked).rank()

  # Will run when undo is called
  if tuple == "undo_entry":
    
    # Reads all of the JSON lines currently in the file
    with open(filename, "r") as reader:
      lines = reader.readlines()
    
    # One line in the list means that it is the initial write, so there is nothing to undo
    if len(lines) == 1:
      print("\n\nNo previous entries to undo, reverting back to first comparison made with this option")

    # Able to undo
    else:
      # Writes all of the lines back except for the last one (w+ since the second to last JSON object needs to be read)
      with open(filename, "w+") as writer:
        i = 0
        for line in lines:

          # The second to last JSON object will be used since they were the previous set of lists used to rank
          if i == len(lines) - 2:
            obj = json.loads(json.loads(line))
            to_rank = obj["to_rank"]
            ranked = obj["ranked"]
          
          # Writes back every JSON object except for the last one (not an elif statement since this should run even
          # when the previous if statement runs)
          if i != len(lines) - 1:
            writer.write(line)
            i += 1
      
      print("\n\nUndo successful")

  # Will run when the user wants to rerank an entry already in the ranked list
  elif type(tuple) == list and tuple[0] == "rerank_entry":
    to_rank.insert(0, tuple[1])
    ranked.remove(tuple[1])

    # Appends the new to_rank and ranked lists that have been adjusted to the file containing the JSONs
    with open(filename, "a") as writer:
      json.dump(Ranker(to_rank, ranked).JSON_form(), writer)
      writer.write("\n")

  # Will run when the user wants to add a new entry
  elif type(tuple) == list and tuple[0] == "add_entry":

    # Adds the new entry to the beginning of to_rank, so this option will immediately replace what is currently being ranked
    if tuple[1] == "now":
      to_rank.insert(0, tuple[2])
      print("\n\nAdded \"" + tuple[2] + "\" to the beginning of the list of things to be ranked")
    
    # Adds the new entry to the end of to_rank
    elif tuple[1] == "end":
      to_rank.append(tuple[2])
      print("\n\nAdded \"" + tuple[2] + "\" to the end of the list of things to be ranked")

    # Adds the new entry somewhere random in to_rank
    else:
      position = random.randint(0, len(to_rank))
      to_rank.insert(position, tuple[2])
      print("\n\nAdded \"" + tuple[2] + "\" somewhere in the list of things to be ranked")
    
    # Appends the new to_rank list that has been adjusted to the file containing the JSONs
    with open(filename, "a") as writer:
      json.dump(Ranker(to_rank, ranked).JSON_form(), writer)
      writer.write("\n")


  # Will run when something new was inserted into the ranked list (and when nothing else was called)
  else:
    to_rank = json.loads(tuple)["to_rank"]
    ranked = json.loads(tuple)["ranked"]

    # Appends the new to_rank and ranked lists from the Ranker class to the file containing the JSONs
    with open(filename, "a") as writer:
      json.dump(tuple, writer)
      writer.write("\n")

# Printing the final results to standard output
print("\n" + json.dumps(ranked) + "\n")

count = 1
for item in ranked:
  print(str(count) + ". " + item)
  count += 1

print()

# Will output a clean looking array of the ranked list into the file
with open(filename, "a") as writer:
  json.dump(json.loads(Ranker(to_rank, ranked).JSON_form())["ranked"], writer)
  writer.write("\n")
