
#!/bin/sh
VERSION="1.0.0-SNAPSHOT"
AUTHOR="Zak Hassan <zak.hassan@redhat.com>"
COMPONENT=""

cat << 'EOF'


  _________                          _________       __
 /   _____/__ ________   ___________/   _____/ _____/  |_
 \_____  \|  |  \____ \_/ __ \_  __ \_____  \_/ __ \   __\
 /        \  |  /  |_> >  ___/|  | \/        \  ___/|  |
/_______  /____/|   __/ \___  >__| /_______  /\___  >__|
        \/      |__|        \/             \/     \/


EOF
docker   build   -t  zmhassan/openshift-superset .
