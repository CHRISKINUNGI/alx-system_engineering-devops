#!/usr/bin/env ruby

# Define the regular expression pattern to extract required information
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Read lines from standard input
ARGF.each_line do |line|
  # Match the regular expression to extract sender, receiver, and flags
  match = line.match(regex)

  # Output sender, receiver, and flags if there's a match
  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]

    puts "#{sender},#{receiver},#{flags}"
  end
end

