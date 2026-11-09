---
type: "index"
tags: ["index", "home"]
generated_by: "tahoemap"
---

# Home

The reading room of a **tahoemap** run on [[Tahoe-100M]]: for every gene, which drugs raise or lower it and in which cell lines, which genes move with it or opposite to it, and where it sits in the vector space and the nodal map.

Run folder: `C:\tahoe\out`. Every path quoted in a note is relative to it.

| | |
|---|---|
| Genes with a note | 16,643 (98 with a written section) |
| Genes in the vector space | 15,076 (64 dimensions, 46,527 (drug-dose, line) contexts; 79 of them only through drug-doses that carry an alert ⚠) |
| Modules | 235 |
| Drugs / drug-doses | 379 / 1,132 |
| Cell lines | 50 |
| Plates / wells | 14 / 1,329 |
| Probable direction (arrows SOURCE → TARGET; [[Probable direction]]) | 98,577 arrows: grade A 25, B 53,178, C 45,374; 98,577 with an alert ⚠ |

## Start here

| If you want | Read |
|---|---|
| what every section of a note means, and the baseline of every fold change | [[How to read this vault]] |
| a gene | the quick switcher (Ctrl/Cmd-O), or [[Genes by letter]] |
| the modules of the nodal map | [[Genes by module]] |
| which gene probably acts on which (from the cell lines; not proof of direct regulation) | [[Probable direction]], and a gene note's Direction (probable) |
| a drug | [[Drugs by mechanism]] |
| a cell line | [[Lines by organ]] |
| why a gene has no note | [[Genes below the detection limit]] |
| a plate's layout and its failed wells | [[Plate 01]], [[Plate 02]], [[Plate 03]], [[Plate 04]], [[Plate 05]], [[Plate 06]], [[Plate 07]], [[Plate 08]], [[Plate 09]], [[Plate 10]], [[Plate 11]], [[Plate 12]], [[Plate 13]], [[Plate 14]] |

## Concepts

Written notes (from `tahoemap/vault_seed/notes/`), each explained once:

- [[Corrections and retractions]], [[Cross-fitting and circularity]], [[FDR calibration and the inflated null]], [[Plate batch effects]], [[Readthrough spillover]], [[Reliability and disattenuation]], [[Tahoe-100M]], [[The p21-DREAM axis]], [[The p53 pathway]], [[p53 nullification in cancer cell lines]]

Generated from this run: [[Probable direction]] (the direction stage's arrows, their grades, alerts and controls).

## Validation

From `validation/report.md` (curated control programmes not derived from Tahoe):

- Control sets: 19 scored; median AUROC (signed cos) 0.945; 19 with AUROC ≥ 0.6.
- Modules labelled by enrichment: 96 of 235.
- Novel candidate relations: 2,815 edges; candidate new set members: 2,145 genes.

- Opposite-arm test P53_TARGETS_UP / DREAM_G2M_DOWN: mean cross-set cos -0.15 (expect < 0); share of cross pairs in one module 0 (random pairs 0.00830).
- Opposite-arm test ISR_ATF4 / RIBOSOME_BIOGENESIS: mean cross-set cos -0.00 (expect < 0); share of cross pairs in one module 0 (random pairs 0.00830).

## Largest modules

| Module | Label | Genes | + arm (top) | − arm (top) |
|---|---|---|---|---|
| [[Module 001]] | rRNA processing | 298 | MAK16, UTP15, LTV1, BYSL | PHF1, MXD1, GNAS, FBXO33 |
| [[Module 002]] | — | 248 | SBF1, ZDHHC8, KLHL17, SH3GLB2 | MEIS2, PARP8, FNDC3A, RBM7 |
| [[Module 003]] | mRNA 3'-end processing | 246 | MPG, COMMD6, LIN7B, LCMT1 | HNRNPK, YWHAE, EWSR1, EIF4G2 |
| [[Module 004]] | MYC targets v1 | 245 | MRPS27, POLR1A, NAA15, TMEM33 | RSRP1, AAMDC, TESK2, ZFYVE1 |
| [[Module 005]] | MYC targets v2 | 244 | WDR4, PUS1, TWNK, ALG8 | PJA2, MPC2, PPDPF, SKAP2 |
| [[Module 006]] | E2F targets | 236 | EXO1, WDR76, CDC45, MYBL2 | ATP6V1G1, CPEB4, TMEM150A, RNF10 |
| [[Module 007]] | Dengue Virus-Host Interactions | 235 | CBLL1, SMG8, ZNF629, MOCS3 | PTMA, SEPTIN2, AP3S1, ATP1B3 |
| [[Module 008]] | Dectin-2 family | 228 | SLC44A4, BCL2L15, POF1B, ST14 |  |
| [[Module 009]] | Neuronal System | 222 | CDH12, RALYL, CDH10, KCNH7 |  |
| [[Module 010]] | — | 217 | PCNX4-DT, TMEM202-AS1, LINC00240, DPH6-DT | L2HGDH, FAM118A, CCDC134, KLHL8 |
| [[Module 011]] | Mitochondrial translation elongation | 217 | RPP38, MRFAP1L1, C1orf131, RPP25L | TMED4, TECR, NUTF2, LAPTM4A |
| [[Module 012]] | mRNA Splicing - Major Pathway | 215 | CCDC174, RBMX2, RP9, PHAX | SMG1P3, BCAP31, PTDSS1, EIF4EBP2 |

## The run

Stage stamps (`stages/*.json`):

- build: v3, 2026-11-07 19:57:35
- effects: v3, 2026-11-07 20:01:33
- tensor: v2, 2026-11-07 20:04:35
- tables: v4, 2026-11-09 10:49:27
- embed: v4, 2026-11-09 10:50:12
- reference: v1, 2026-11-09 11:02:09
- relations: v4, 2026-11-09 11:02:27
- graph: v5, 2026-11-09 11:04:13
- direction: v2, 2026-11-09 11:07:29
- validate: v4, 2026-11-09 11:07:47

Registry downloads (`reference/sources.json`):

- ensembl: downloaded, 2026-11-09, 63,140 rows
- hallmark: cached, 2026-11-08, 50 rows
- hgnc: cached, 2026-11-08, 45,326 rows
- ncbi: downloaded, 2026-11-09, 151,703 rows
- reactome: cached, 2026-11-08, 2,874 rows
- string_info: cached, 2026-11-08, 19,699 rows
- string_links: cached, 2026-11-08, 1,858,944 rows
- uniprot: cached, 2026-11-08, 20,429 rows

## Honesty ledger

Corrections to the written layer are recorded, not hidden: [[Corrections and retractions]].
