#!/usr/bin/env ruby

# open the log file
File.open("log", "r") do |f|
  # read each line of the file
  f.each_line do |line|
    # match the line with a regular expression
    match = line.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
    if match
      # extract the sender, receiver, and flags from the match
      sender = match[1]
      receiver = match[2]
      flags = match[3]

      # print the result
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end
