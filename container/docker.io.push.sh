#!/bin/sh
VERSION="1.0.0-SNAPSHOT"
MAINTAINERS="Zak Hassan"
COMPONENT="openshift-"


cat << 'EOF'
  _________                          _________       __
 /   _____/__ ________   ___________/   _____/ _____/  |_
 \_____  \|  |  \____ \_/ __ \_  __ \_____  \_/ __ \   __\
 /        \  |  /  |_> >  ___/|  | \/        \  ___/|  |
/_______  /____/|   __/ \___  >__| /_______  /\___  >__|
        \/      |__|        \/             \/     \/

EOF

echo " "
echo "Maintainers: $MAINTAINERS"
echo " "
echo "Version: $VERSION"
echo " "
echo "Component: $COMPONENT"
echo " "
echo "Building Containers and pushing docker images to docker registry"
echo " "

docker tag  zmhassan/openshift-superset  quay.io/zmhassan/openshift-superset
docker push  quay.io/zmhassan/openshift-superset
