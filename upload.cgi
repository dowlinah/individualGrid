#!/usr/bin/perl 
#upload24cgi   # Uploads images; shows image.  Creates a select box using &make_select from mylib.pl 
require ("mylib.pl");

use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
$CGI::POST_MAX = 1024 * 4000;    # 4MB

my $upload_dir = "./data/img";
my $query = new CGI;
my $filename = $query->param("upload_file");  # In tag: name="upload_file";

my $success="",$ext;
my $select="";

my $numfiles = 0;
opendir(my $dh, $upload_dir);
while (my $de = readdir($dh)) {
      next if $de =~ /^\./ or $de =~ /config_file/;
      $numfiles++;
}
closedir($dh);

if (!$filename){

Grid::HTML5::begin_html();
Grid::HTML5::generate_header();
print <<EOT;
<br><b>
No File Selected.
</b><br>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
exit;
}

my $user = $query->param("user");
my $pass = $query->param("pass");
chomp($user);
chomp($pass);
my $pass = crypt($pass,69);

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
		Grid::HTML5::generate_footer();
		Grid::HTML5::end_html();
		exit;		
	} 
} else {
Grid::HTML5::begin_html();
Grid::HTML5::generate_header();
print <<EOT;
<br> <b>
Username incorrect.
</b><br>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
exit;
}

################ creates post ################

$filename =~ /(.*)\.(\w*$)/;
$filename =$1;
$ext = $2;
$filename =~ s/\W//g;        #security!
$ext = lc($ext);

$filename = $numfiles +1;

$ext = ".jpg";          #SECURITY!
$filename = $filename . $ext;

my $upload_filehandle = $query->upload("upload_file"); #Named "upload_file" in the input tag

$path = "$upload_dir/$filename";

open ( UPLOADFILE, ">$path") or &webdie ("Can't upload $path: $!");
binmode UPLOADFILE; 

while ( <$upload_filehandle> )
{
print UPLOADFILE;
}
close UPLOADFILE;

############### save post text.

my $textpath = $numfiles +1;
$textpath = $textpath . ".txt";

$textpath = "./data/text/" . $textpath;
my $posttext = $query->param("upload_text");

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$mon++;
$year = $year + 1900;
$today = "$hour:$min - $mon/$mday/$year -- ";

my $posttitle = $query->param("upload_title");
$posttitle = "<b>" . $posttitle . "</b><br> - ";
$posttext = $posttitle . $posttext;

$posttext = $today . $user . "<br>" . $posttext;

open (FH , ">>$textpath");

print FH $posttext;

close FH;

################# HTML ##################

Grid::HTML5::begin_html("Post Successful");
Grid::HTML5::generate_header();
print <<EOT;

<br>
<b> Post Sucessful! </b>

EOT

Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
}
