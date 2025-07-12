# chamando bibliotecas
library(ipeadatar)
library(tidyverse)
library(geobr)
library(leaflet)
library(sf)

# extraindo dados geoespaciais dos municipios
municipios <- read_municipality(year = 2022, simplified = T)

# codigos a serem utilizados na extracao
codigos <- c("Admissões" = "ADMISNC", "Demissões" = "DESLIGNC")

# dados de admissoes da IPEA, filtrados por municipios
dados_caged <- ipeadatar::ipeadata(codigos) %>%
  filter(uname == "Municipality") %>%
  mutate(categoria = case_when(
    str_detect(code, "ADMISNC") ~ "Admissões",
    str_detect(code, "DESLIGNC") ~ "Demissões"
  )) %>%
  left_join(municipios, by = c("tcode" = "code_muni")) %>%
  select(-c(code, tcode, code_state, code_region)) %>%
  pivot_wider(
    names_from = categoria,
    values_from = value
  )

dados_caged_sf <- dados_caged %>%
  st_as_sf() %>%
  st_transform(crs = 4326)

m <- dados_caged_sf %>%
  filter(date == "2025-01-01") %>%
  leaflet() %>%
  addTiles() %>%
  addPolygons(stroke = T,
              color = "#2C2D2D",
              weight = 1.0,
              fillOpacity = 0.5, 
              smoothFactor = 1,
              fillColor = ~ colorQuantile(
                palette = "YlOrRd",
                domain = Admissões,
                na.color = "transparent",
                n = 9
              )(Admissões)
  )

  
  
  
  
  
  
  
  
  
  
