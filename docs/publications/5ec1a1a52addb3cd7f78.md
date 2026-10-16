---
title: 'Proyecto Centinela avanzado v2.1 – reingeniería profunda y fortalecimiento
  de la plataforma para la colaboración: reingeniería del módulo de analítica académica
  para la plataforma Centinela'
authors:
- C.A.(Cristopher Alexander) Bonilla Molina
date: '2026-10-13'
type: dissertation
category: &id001
- Inteligência Artificial
doi: null
abstract: 'Centinela es la plataforma de gestión de producción científica de la Escuela
  Politécnica Nacional. Su módulo de analítica, sin embargo, arrastra varios problemas
  que afectan cómo funciona. El más grave es que cada actualización de datos obliga
  a regenerar toda la base desde cero, algo que gasta demasiados recursos del servidor
  y, peor todavía, borra cualquier historial anterior. A esto se suma que las visualizaciones
  actuales son estáticas y ya no alcanzan para cubrir lo que necesitan los perfiles
  administrativos. Este trabajo aborda la reingeniería de ese módulo a través de tres
  frentes. El primero es el diagnóstico y la optimización del modelo de datos en MongoDB:
  se evalúa si hace falta una migración tecnológica y se diseña una estrategia de
  sincronización incremental basada en marcas de tiempo. El segundo frente cubre el
  diseño e implementación de dashboards dinámicos para dos perfiles de usuario, investigadores
  y administradores, siguiendo los principios de Visual Analytics. El tercero consiste
  en validar el sistema mediante pruebas de carga y sesiones de retroalimentación
  con usuarios reales. Para lograrlo, la metodología combina tres marcos de trabajo:
  CRISP-DM para estructurar el ciclo de vida de los datos, Scrum para organizar el
  desarrollo en cinco sprints iterativos y el proceso de Visual Analytics para guiar
  el diseño de las interfaces. La arquitectura resultante conserva un esquema de persistencia
  políglota, en el que Neo4j sigue siendo la fuente de verdad para las relaciones
  de coautoría y MongoDB concentra los documentos analíticos precomputados que alimentan
  los dashboards. El proceso de actualización pasó de ser una regeneración destructiva
  y síncrona a una carga incremental basada en operaciones de tipo upsert, que se
  ejecuta en segundo plano sin bloquear la interfaz del administrador. Sobre esta
  base se construyó un panel de salud del sistema y una capa de analítica visual que
  aplica los tres niveles del mantra de Visual Analytics: visión general primero,
  zoom y filtro, y detalles bajo demanda, incluyendo una matriz de concentración de
  tópicos por institución con navegación interactiva. Con esto se espera reducir de
  forma notable los tiempos de respuesta ante consultas masivas, eliminar la regeneración
  total de la base de datos y contar con tableros de control que apoyen la toma de
  decisiones institucionales sobre la producción científica. La validación formal
  de rendimiento y usabilidad con el volumen íntegro de datos de la plataforma queda
  para la siguiente fase del proyecto.'
source:
- OpenAlex
source_ids:
- https://openalex.org/W7221836892
url: https://openalex.org/W7221836892
discovered_at: '2026-10-16'
tags: *id001
---

# Proyecto Centinela avanzado v2\.1 – reingeniería profunda y fortalecimiento de la plataforma para la colaboración: reingeniería del módulo de analítica académica para la plataforma Centinela

**Autores:** C\.A\.\(Cristopher Alexander\) Bonilla Molina

**Data:** 2026-10-13 · **Tipo:** dissertation

## Resumo

Centinela es la plataforma de gestión de producción científica de la Escuela Politécnica Nacional\. Su módulo de analítica, sin embargo, arrastra varios problemas que afectan cómo funciona\. El más grave es que cada actualización de datos obliga a regenerar toda la base desde cero, algo que gasta demasiados recursos del servidor y, peor todavía, borra cualquier historial anterior\. A esto se suma que las visualizaciones actuales son estáticas y ya no alcanzan para cubrir lo que necesitan los perfiles administrativos\. Este trabajo aborda la reingeniería de ese módulo a través de tres frentes\. El primero es el diagnóstico y la optimización del modelo de datos en MongoDB: se evalúa si hace falta una migración tecnológica y se diseña una estrategia de sincronización incremental basada en marcas de tiempo\. El segundo frente cubre el diseño e implementación de dashboards dinámicos para dos perfiles de usuario, investigadores y administradores, siguiendo los principios de Visual Analytics\. El tercero consiste en validar el sistema mediante pruebas de carga y sesiones de retroalimentación con usuarios reales\. Para lograrlo, la metodología combina tres marcos de trabajo: CRISP\-DM para estructurar el ciclo de vida de los datos, Scrum para organizar el desarrollo en cinco sprints iterativos y el proceso de Visual Analytics para guiar el diseño de las interfaces\. La arquitectura resultante conserva un esquema de persistencia políglota, en el que Neo4j sigue siendo la fuente de verdad para las relaciones de coautoría y MongoDB concentra los documentos analíticos precomputados que alimentan los dashboards\. El proceso de actualización pasó de ser una regeneración destructiva y síncrona a una carga incremental basada en operaciones de tipo upsert, que se ejecuta en segundo plano sin bloquear la interfaz del administrador\. Sobre esta base se construyó un panel de salud del sistema y una capa de analítica visual que aplica los tres niveles del mantra de Visual Analytics: visión general primero, zoom y filtro, y detalles bajo demanda, incluyendo una matriz de concentración de tópicos por institución con navegación interactiva\. Con esto se espera reducir de forma notable los tiempos de respuesta ante consultas masivas, eliminar la regeneración total de la base de datos y contar con tableros de control que apoyen la toma de decisiones institucionales sobre la producción científica\. La validación formal de rendimiento y usabilidad con el volumen íntegro de datos de la plataforma queda para la siguiente fase del proyecto\.

[Consultar publicação](<https://openalex.org/W7221836892>)
