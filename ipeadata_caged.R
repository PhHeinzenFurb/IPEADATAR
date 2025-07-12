library(ipeadatar)
library(tidyverse)
library(data.table)

# verificando as séries dentro de ipeadataR
series_ipeadata <- ipeadatar::available_series() 

# selecionando os municipios dentro dos territorios disponiveis
territories_ipeadata <- ipeadatar::available_territories() %>%
  filter(uname == "Municipality") %>%
  select(tcode, tname)

codigos <- c("Admissões" = "ADMISNC", "Demissões" = "DESLIGNC")

# dados de admissoes da IPEA, filtrados por municipios
dados_caged <- ipeadatar::ipeadata(codigos) %>%
  filter(uname == "Municipality")

dados_caged_trans <- dados_caged %>%
  mutate(categoria = case_when(
    str_detect(code, "ADMISNC") ~ "Admissões",
    str_detect(code, "DESLIGNC") ~ "Demissões"
  ),
  tcode = as.character(tcode)) %>%
  left_join(territories_ipeadata, by = "tcode") %>%
  select(date, value, categoria, tname)
