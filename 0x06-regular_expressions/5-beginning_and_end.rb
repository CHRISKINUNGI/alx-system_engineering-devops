#!/usr/bin/env ruby

# Define the regular expression pattern
regex = /h[a-z]n/

# Extract the first command-line argument
input_text = ARGV[0]

# Use the regular expression to find matches in the input text
matches = input_text.scan(regex)

# Join the matches into a single string, if any
matched_text = matches.join

# Print the matched text
puts matched_text
