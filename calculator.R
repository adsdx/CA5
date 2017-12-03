#######################################################
# This is a programme to create a programme that will
# serve similarly to a scientific calculator with
# various functionalities.
#
# Some example functions are called at the bottom of
# the script
#
# Scripted by Andrew Doran-Sherlock 10361540
# 01 Decemeber 2017
#######################################################

add <- function(x,y) {
    return(x+y)
}

subtract <- function(x,y) {
    return(x-y)
}

multiply <- function(x,y) {
    return(x*y)
}

divide <- function(x,y) {
    return(x/y)
}

exponential <- function(x,y) {
    return(x**y)
}

square_root <- function(x) {
    return(sqrt(x))
}

sine <- function(x) {
    return(sin(x))
}

cosine <- function(x) {
    return(cos(x))
}

square <- function(x) {
    return(x**2)
}

cube <- function(x) {
  return(x**3)
}

add(2,4)
subtract(2,4)
multiply(2,-4)
divide(-4,2)
exponential(4,2)
square_root(81)
sine(0)
cosine(0)
square(2)
cube(2)
