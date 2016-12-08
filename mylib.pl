# mylib.pl  This is my perl library.  It must be called with require(mylib.pl)
# Contents:  &get_lines(); &get_lines_text(); &get_count(), &begin_html(), sort num_alpha(@array)
# &make_select(); read_form_results();


# Get the lines of a file, but only a file in the current directory (security)
sub get_lines{
  my(@array);
  $file = $_[0];
  open (FH, $file);
  @array= <FH>;
  unshift (@array,"$file\n\n");
  close (FH);
  return(@array);
}                       #End &make_lines_array



# Slurp the lines of a file, but only a file in the current directory (security)
sub slurp_lines{
  my $all;
  undef $/;					#Slurp mode
  $file = $_[0];
  open (FH, $file);
  $all= <FH>;
  close (FH);
  return $all;
}                       #End &slurp_lines




# Get the lines of a file, but only from the directory "text/"
sub get_lines_text{                                   
  my(@array);
  $file = $_[0];
  $file =~ s#/##g;                  # SECURITY!
  $file = "text/" . $file;          # SECURITY: get from the text/ directory
  open (FH, $file);
  @array= (<FH>);
  unshift (@array,"$file\n\n");
  close (FH);
  return(@array);
}                       #End &make_lines_array



sub numerically {$a <=> $b};      #for a numeric sort

sub numeric_reverse {$b <=> $a}   #for a reverse numeric sort


# make_select():input: array of urls; output: string creates a complete select box
# <select id="selBox"> options list .... </select>: click to go to url (a picture or html etc.) 
sub make_select(){  
  my $str, $name;
  my @items = @_;
  @items= sort(@items);
  my $len = @items;
  if($len <= 5){$len==6;}
  else {$len=15;}
  my $str= "<select id=\"selBox\" size=$len>\n";
  foreach (@items){
      $_ =~ /.*\/(.*$)/;
      $name= $1;
      $str .= "<option value= \"$_\"> $name </option>\n";
  }
  $str .= "</select>";
  return $str;
}


sub webdie{
&begin_html("System Difficulties");
print("$_[0]<p> $@ <p>\n");
print("</body></html>");
exit;
}
$index = int(rand(2));

#Chooses a random passage
#Passages are separated by ^

sub get_fortune{
my($count, @phrase, $index);
$/ = "\n^";
open(FILEIN,"@_[0]");
while(<FILEIN>){
  tr/^/ /;
  push(@phrase,$_);
}
close (FILEIN);
$count= $#phrase;
$/= "\n";			#restore record separator
shift(@phrase);    #omit blank first element
srand;
$index = rand($count);
return($phrase[$index]);
}

# &getcount():  Get the count, increment, write back to file.
# arguments: 1. data file 
# returns:  A number (scalar)
sub get_count{
my($file,$count,$return_count);
$file = @_[0]; 
if (!-e "$file") {			#if $file doesn't exist, create it
   open (OUT, ">$file");
   print (OUT "0");
   close (OUT);
   chmod(0660, "$file");
   }

open (READ, "$file");			#Read stored count
while (<READ>){
   $count = $_;
   last;				#quit after first line.
}
close (READ);

$return_count = $count;
$count++;				#Increment count.

open (OUT, ">$file");			#Print out new count
print (OUT "$count");
close (OUT);
return($return_count);
}					#End &get_count



# begin_html(): Print the HTML header  
# arguments 1. title
# No return.  Prints to the screen.
sub begin_html{
my($title);
$title = $_[0];      
print <<EOT;
Content-type: text/html\n\n

<!doctype html>
<html lang-en>
<head>
<title>dowlina: $title </title>
 <link rel="stylesheet" type="text/css" href="comm442.css" />

EOT
}									#End &begin_html



# begin_html_blank(): Print the HTML header  
# One argument: title
# No return.  Prints to the screen.
sub begin_html_blank{
my $title= "Horn";
$title= $_[0] if $_[0];
print <<EOT;
Content-type: text/html\n\n

<!doctype html>
<html lang-en>
<head><title>$title </title>
  <link rel="stylesheet" type="text/css" href="comm442.css" />
  <style type="text/css">
  </style>
  <script type="application/x-javascript">
  </script> 
</head>
EOT
}					#End print_html_header



# Accepts STDIN data stream from forms HTML; splits name/value pairs,
# and assigns value to the associative array %entry with name as key
#

sub read_form_results { 
    my ($buffer, $name, $value);
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    foreach (split(/&/, $buffer))
    {
        ($name, $value) = split(/=/);                                          
        # Un-Webify plus signs and %-encoding                            
        $value =~ tr/+/ /;                                               
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;     
        $entry{$name} = $value;                                          
    }                                                                      
    1;                                                                   
}                                                                        


## larger number first then alphabetical
sub num_alpha{                          #Llama 190
   $b <=> $a or $a cmp $b;
}
      

sub today{
 my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)= localtime(time);
 my @weekday=(Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday);
 my @month= (January,February,March,April,May,June,July,August,September,October,November,December);
 my $year = 1900 + $year;
 my $mytime = "@weekday[$wday], $mday @month[$mon], $year";
 return $mytime;
}


####################3 GETS A VERSE FROM THE Tao Te Ching
sub get_tao{
my $file, @verses,$count, $poem, $index;
$/="\n";
open(IN,"/home/horn/public_html/classes/comm442/perl/tao_te_ching.fdb");
while (<IN>){
  if (/^#/) {next;}
  $file .= $_
}
close (IN);
@verses = split(/\d\d?/,$file);
shift (@verses);
$count = @verses;     #scalar context gives length
srand;
$index = int(rand($count));


$poem= $verses[$index];
$poem =~ s/\n/<br \/>\n/g;
$index++;
$poem=  "<h5>$index</h5>$poem";
return $poem;
}



1;	#Or return(1); Library must return yes.

