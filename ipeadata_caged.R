library(ipeadatar)
library(tidyverse)

series_ipeadata <- ipeadatar::available_series() 

territories_ipeadata <- ipeadatar::available_territories() %>%
  filter(uname == "Municipality") %>%
  select(tcode, tname)

dados_ipeadata <- ipeadatar::ipeadata("ADMISNC") %>%
  filter(uname == "Municipality")
