package Grid::HTML5;

use strict;
use warnings;
use Grid::Base;

#** @function public begin_html($title, $about, $author, $style, $script)
# @brief Print the HTML5 <head>.
#
# Under construction. Used to dynamically generate the HTML5 head.
# @params $title  String. Sets <title> tag.
# @params $about String. Sets <title> tag.
# @params $author String. Sets <title> tag.
# @params $style String. Path to a  .css file tag.
# @params $script String. Path to a .js file.
#*.
sub begin_html {
    my $title  = $_[0];
    my $about  = $_[1] // "Grid " . Grid::Base::get_version;
    my $author = $_[2] // "Stephen Lorenz, Anthony Dowling";
    my $style  = $_[3] // "css/styles.css";
    my $script = $_[4] // "js/scripts.js";

    print <<EOT;
content-type: text/html

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>$title</title>
<meta name="description" content="$about">
<meta name="author" content="$author">

<link rel="stylesheet" href="$style">
<script src="$script"></script>

<!--[if lt IE 9]>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
<![endif]-->
</head>
<body>
EOT
}

#** @function public end_html()
# @brief Close tags opened by begin_html;
#
# Under construction. Used to ensure that all tags have been properly closed.
#*.
sub end_html {
  print <<EOT;
</body>
</html>
EOT
}

#** @function public generate_header()
# @brief Print a generic <header>.
#
# Under construction.Used to dynamically generate HTML5 headers.
#*.
sub generate_header {
  my $title = $_[0] // "Grid " . Grid::Base::get_version;
  my $about = $_[1] // "";

  print <<EOT;
  <header>
    <h1>$title</h1>
    <p>$about</p>
  </header>
  <nav>
	<ul>	
	<li><a href="index.cgi"> Home</a></li>
	<li><a href="post.cgi"> Post</a></li>
      <li><a href="signup.cgi"> Sign up</a></li>
      <li><a href="feed.cgi"> Feed</a></li>
  </nav>
  <div id='wrapper'>
EOT
}

sub generate_footer {
  my $year = Grid::Base::localtime()->year;
  print <<EOT;

<footer>
	</div>
  <nav>
    <ul>
      <li><a href="about.cgi">About</a></li>
      <li><a href="https://github.com/dowlinah/grid">GitHub</a></li>
      <li><a href="contact.cgi">Contact</a></li>
    </ul>
  </nav>
  <center><p>In development. $year</p></center>

</footer>
EOT
}

1;
