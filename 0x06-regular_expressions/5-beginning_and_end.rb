#!/usr/bin/env ruby
# ruby script
# regular expression that starts wit h and ends with n
# accepts one argument

puts ARGV[0].scan(/^h.n$/).join
