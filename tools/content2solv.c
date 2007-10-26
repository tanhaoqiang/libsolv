#include <sys/types.h>
#include <limits.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "pool.h"
#include "repo_content.h"
#include "repo_write.h"

int
main(int argc, char **argv)
{
  Pool *pool = pool_create();
  Repo *repo = pool_addrepo_content(pool, stdin);
  pool_writerepo(pool, repo, stdout);
  pool_free(pool);
  return 0;
}
