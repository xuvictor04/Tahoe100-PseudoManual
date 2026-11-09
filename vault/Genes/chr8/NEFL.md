---
symbol: "NEFL"
type: "gene"
col: 15894
ensembl_id: "ENSG00000277586"
name: "neurofilament light chain"
location: "8p21.2"
module: 19
arm: "+"
pooled_cpm: 17.76
n_lines_expressing: 16
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NEFL

*neurofilament light chain* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.05× (z +10.4, q 9e-23, up in 5 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.12× (z +7.9, q 4e-13, up in 13 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.445× (z -5.8, q 5e-06, down in 8 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFMBT2]] (+0.65, fdr 1e-05), [[ASXL3]] (+0.59, fdr 3e-05), [[BARX1]] (+0.57, fdr 3e-05); moves opposite to [[ITGA9-AS1]] (-0.46, fdr 1e-04), [[TIMM23B-AGAP6]] (-0.44, fdr 1e-04), [[AGAP6]] (-0.42, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02994]] → it (grade C ⚠); 1 goes from it, the strongest it → [[SLC25A30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.05×** | +10.4 | 9e-23 | 5/11 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +8.1 | 1e-13 | 4/8 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +7.9 | 4e-13 | 13/14 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +6.2 | 7e-08 | 5/10 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +5.0 | 8e-05 | 10/12 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.7 | 3e-04 | 2/11 (A498, NCI-H2030) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +3.4 | 0.059 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.35× | +3.2 | 0.11 | 2/12 (A498, A-172) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | 1.34× | +3.0 | 0.13 | 5/14 (A-172, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | 1.51× | +3.0 | 0.13 | 4/11 (A-172, SHP-77, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.445×** | -5.8 | 5e-06 | 8/12 (A549, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -4.4 | 0.003 | 8/13 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.574×** | -3.9 | 0.018 | 1/13 (NCI-H1792) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.576×** | -3.8 | 0.018 | 1/13 (A549) | inconsistent across doses |  |
| [[Riluzole hydrochloride (drug)]] 0.05 µM |  | 0.645× | -3.3 | 0.11 | 2/14 (CHP-212, SW 1088) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.653× | -3.1 | 0.20 | 3/13 (NCI-H2030, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.2) |
| [[A498 (line)]] | wt | 33.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.50× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 9.08 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.38× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0835× (z -17.1) |
| [[A-172 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.8 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.189× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 5.40 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.25× (z +10.2) | — |
| [[A549 (line)]] | wt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.0) |
| [[SHP-77 (line)]] | alt | 83.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.3) |
| [[AN3 CA (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFMBT2]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.59 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[BARX1]] | +0.57 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[NDNF]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NEFM]] | +0.57 | +0.42 / +0.67 | both halves | 4e-05 | same gene group; STRING 999; ⚠ same locus (31.9 kb: neighbours can correlate without regulation) |
| [[RAB3C]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[SLITRK5]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 | pathway: Neuronal System |
| [[SYT11]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[KCNJ6]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 | pathway: Neuronal System |
| [[ARHGAP28]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[KCTD16]] | +0.51 | +0.50 / +0.43 | both halves | 4e-05 |  |
| [[DDIT4L]] | +0.51 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[EBF2]] | +0.51 | +0.55 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA9-AS1]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[TIMM23B-AGAP6]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[AGAP6]] | -0.42 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[LIN52]] | -0.42 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[ATR]] | -0.42 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[C1orf159]] | -0.41 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[LRRK1]] | -0.41 | -0.32 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02994]] | C | LINC02994 activity raises NEFL's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 2.41× lower at baseline in the lines without LINC02994 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598; co-absent with the target |
| [[PALMD]] | C | PALMD activity raises NEFL's level | lines that do not express PALMD (27) vs lines expressing it (23) | 3.18× lower at baseline in the lines without PALMD | 0.037 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |
| [[NEFM]] | C | NEFM activity raises NEFL's level | lines that do not express NEFM (35) vs lines expressing it (15) | 4.56× lower at baseline in the lines without NEFM | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, GTF2I-AS1, LINC03000; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A30]] | B | NEFL activity lowers SLC25A30's level | lines that do not express NEFL (34) vs lines expressing it (16) | 1.17× higher at baseline in the lines without NEFL | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADD2, UCHL1, LINC03046 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, 36.0); signed map (40.4, 40.1). **Vector** length 52.2, 18.8% of its response variance represented; |z| ≥ 3 in 353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | neurofilament light chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:24,950,955-24,956,721 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NFL, CMT1F, CMT2E, NF68, PPP1R110 |
| Gene groups (HGNC) | Intermediate filaments Type IV; Protein phosphatase 1 regulatory subunits; MicroRNA protein coding host genes |
| Reactome | 14 pathways, smallest: Ras activation upon Ca2+ influx through NMDA receptor; Unblocking of NMDA receptors, glutamate binding and activation; Negative regulation of NMDA receptor-mediated neuronal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [P07196](https://www.uniprot.org/uniprotkb/P07196) (Neurofilament light polypeptide):

> Neurofilaments usually contain three intermediate filament proteins: NEFL, NEFM, and NEFH which are involved in the maintenance of neuronal caliber. May additionally cooperate with the neuronal intermediate filament proteins PRPH and INA to form neuronal filamentous networks (By similarity).

**Summary**, from NCBI Gene [4747](https://www.ncbi.nlm.nih.gov/gene/4747):

> Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and they functionally maintain the neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene encodes the light chain neurofilament protein. Mutations in this gene cause Charcot-Marie-Tooth disease types 1F (CMT1F) and 2E (CMT2E), disorders of the peripheral nervous system that are characterized by …

**Accessions** — [HGNC:7739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7739) · Entrez [4747](https://www.ncbi.nlm.nih.gov/gene/4747) · UniProt [P07196](https://www.uniprot.org/uniprotkb/P07196) · Ensembl [ENSG00000277586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277586)

## Data

Gene col 15894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15894); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15894]; `tensor/DDL_lfc|DDL_z.npy` [15894]; `embed/gene_vectors.npy` [15894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15894 or target_col == 15894). Every well: [[NEFL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEFL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
