TFscale02 <- function(length, up)
{
  if (missing(up))
  {
    high <- 337
  }
  else
  {
    high <- 337 - up
  }
  width <- 170 * (high / 337)
  actual <- length / width * 10
  return(actual)
}
