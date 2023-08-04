#!/usr/bin/env ruby

regex = /\bSchool\b/
string = ARGV[0]

matches = string.scan(regex)

if matches.any?
  puts matches.join
else
  puts ""
end
