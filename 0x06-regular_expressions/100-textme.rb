#!/usr/bin/env ruby
# ruby script that
# outputs senders phone number
# receivers phone number
# flags used

from = ARGV[0].scan(/from:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts [from, to, flag].join(',')
