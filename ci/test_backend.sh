#!/bin/bash
export COMPOSE_PROJECT_NAME=famass_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run famass unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
