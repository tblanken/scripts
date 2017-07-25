# Evaluation and Substitution 2

set NYCapital Albany
set Label "The Capitol of New York is: "

puts "\n................. examples of differences between  \" and \{"
puts "$Label $NYCapital"
puts {$Label $NYCapital}

puts "\n....... examples of differences in nesting \{ and \" "
puts "$Label {$NYCapital}"
puts {Who said, "What this country needs is a good $0.05 cigar!"?}

puts "\n................. examples of escape strings"
puts {There are no substitutions done within braces \n \r \x0a \f \v}
puts {But, the escaped newline at the end of a\
string is still evaluated as a space}

