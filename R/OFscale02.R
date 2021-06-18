OFscale02 <- function(length, up)
{
  if (missing(up))
  {
    high <- 444
  }
  else
  {
    high <- 444 - up
  }
  width <- 400 * (high / 444)
  actual <- length / width * 10
  return(actual)
}
