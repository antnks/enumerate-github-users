# enumerate-github-users
A script to create fake commits

enum.py

Reads input file lines and creates git commits based on emails read from input
When pushed to Github the commit history should show which user is connected to the supplied email

Usage: python enum.py emails.txt
Input file is one email per line. Example:
<pre>
a@b.com
c@d.com
</pre>

If you wish to push the results to Github, ensure to fork this repo. Otherwise you will get access denied during the push
