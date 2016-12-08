#!/usr/bin/perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;

my $imgpath = "./data/img/";
my $txtpath = "./data/text/";

my $numfiles = 0;
opendir(my $dh, $imgpath);
while (my $de = readdir($dh)) {
      next if $de =~ /^\./ or $de =~ /config_file/;
      $numfiles++;
}
closedir($dh);

## needs to grep all imgs and txts

##reverse sorted to highest number is last.


Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();

## outputs to screen.
print <<EOT;

	<h2>Feed</h2>

<br>
<b> There are $numfiles posts so far </b> <br><br>
<br>
EOT

my $count = $numfiles;

while($count != 0) {

	my $thisfile = $txtpath . $count . ".txt";

	my $img = $imgpath . $count . ".jpg";

	my($file);
	undef $/;
	open (FH, $thisfile);
	$file= <FH>;
	close(FH);

	$file = $file . "<br><br><a href='viewcomments.cgi?post=$count'>Show Comments</a>";

	print "<div id='post'>";

	print "<b><a href='comment.cgi?post=$count'>Comment</b></a>";

	print "<div class='text'>" . $file . "<br><br> </div>";

	print "<br> <div class='image'> <a href=\"" . $img . "\">";

	print "<img src=\"" . $img . "\" width='100';></a></div>\n";
#	print "<div class='clear'></div>";
	print "</div><br>";


	$count--;
}

print "</div><br>";

Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
