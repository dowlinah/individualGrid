#!/usr/bin/perl

use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;

my $query = new CGI;
my $post = $query->url_param('post');
my $comment = $query->param('comment');
my $user = $query->param('user');
my $pass = $query->param('pass');

############## Checks User and Pass ###############
chomp($user);
chomp($pass);

$pass = crypt($pass,69);
my $usrpath = "./data/usr/" . $user . ".usr";
if(-f $usrpath) {
	open(FH, "<$usrpath");
	$testpass = <FH>;
	close FH;
	chomp($testpass);
	if($testpass ne $pass) {
		Grid::HTML5::begin_html();
		Grid::HTML5::generate_header();
		print <<EOT;
		<br><b>
		Incorrect Password.
		</b><br>
EOT
		Grid::HTML5::Generate_footer();
		Grid::HTML5::end_html();
		exit;
	}
} else {
	Grid::HTML5::begin_html();
	Grid::HTML5::generate_header();
	print <<EOT;
	<br><b>
	Username incorrect.
	</b><br>
EOT
	Grid::HTML5::generate_footer();
	Grid::HTML5::end_html();
	exit;
}

######### Adds Comment #################

$cmntpath = "./data/comments/";

$thispostpath = $cmntpath . $post . "*.cmnt";

@allcomments = glob($thispostpath);
$numfiles = @allcomments;
$numfiles++;


$currentpath = $cmntpath . $post . $numfiles . ".cmnt";

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$mon++;
$year = $year + 1900;
$today = "$hour:$min - $mon/$mday/$year -- ";

$newtext = $today . $user . "<br>" . $comment;

open(FH, ">>$currentpath");
print FH $newtext;
closeFH;

print "Location: viewcomments.cgi?post=$post\n\n";
