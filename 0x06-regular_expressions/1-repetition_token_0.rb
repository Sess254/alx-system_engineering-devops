#!/usr/bin/env ruby
# ruby script that
# matches repetition
# accepts one argument

puts ARGV[0].scan(/hbt{2,5}n/).join
