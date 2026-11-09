---
symbol: "ESAM"
type: "gene"
col: 7389
ensembl_id: "ENSG00000149564"
name: "endothelial cell adhesion molecule"
location: "11q24.2"
module: 34
arm: "+"
pooled_cpm: 3.79
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ESAM

*endothelial cell adhesion molecule* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.26× (z +11.8, q 1e-29, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.77× (z +8.4, q 6e-15, up in 21 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (AsPC-1 0.0550×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (H4 0.0586×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0953×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEAR1]] (+0.66, fdr 1e-05), [[GDPD5]] (+0.63, fdr 9e-06), [[PDLIM7]] (+0.61, fdr 1e-05); moves opposite to [[GTF2I]] (-0.51, fdr 3e-05), [[ACTR3C]] (-0.51, fdr 3e-05), [[ARFGEF2]] (-0.50, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLC3]] → it (grade B ⚠); 2 go from it, the strongest it → [[LRWD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +11.8 | 1e-29 | 1/6 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.6 | 5e-24 | 8/14 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +8.4 | 6e-15 | 21/40 (SW480, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.0 | 2e-13 | 18/34 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +7.8 | 5e-13 | 2/8 (KATO III, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +7.1 | 1e-10 | 18/38 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.6 | 4e-09 | 18/41 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +6.4 | 1e-08 | 17/40 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +6.1 | 6e-08 | 3/15 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.65×** | +5.2 | 1e-05 | 14/42 (SW480, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +4.7 | 1e-04 | 14/41 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 1e-03 | 11/27 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.002 | 8/30 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 7/34 (A498, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +4.0 | 0.003 | 8/34 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.003 | 6/24 (HT-29, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.003 | 8/38 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7389.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (AsPC-1 0.0550×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (H4 0.0586×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0953×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.523× | -3.6 | 0.21 | 8/36 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.720× | -3.3 | 0.25 | 13/31 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.809× | -3.2 | 0.29 | 6/41 (Hs 766T, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.49 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0550× (z -9.7) |
| [[H4 (line)]] | wt | 9.56 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0586× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0953× (z -9.0) |
| [[A-172 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAR1]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 | STRING 451 |
| [[GDPD5]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[PDLIM7]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RAC2]] | +0.58 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[STK10]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[FAM131A]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[KLC3]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[BMP8A]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PDE2A]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.56 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[AP1M1]] | +0.56 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ACTR3C]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ARFGEF2]] | -0.50 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[RPRD2]] | -0.48 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[LETMD1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | -0.48 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[SNX13]] | -0.48 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLC3]] | B | KLC3 activity strengthens ESAM's drug response | lines that do not express KLC3 (8) vs lines expressing it (34) | the lines without KLC3 respond the other way (z diff +2.14); strongest at Topotecan (hydrochloride) 5 µM: 0.08x vs 1.15x (z diff +8.7) | 0.094 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRWD1]] | C | ESAM activity raises LRWD1's level | lines that do not express ESAM (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without ESAM | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |
| [[PJA1]] | C | ESAM activity raises PJA1's level | lines that do not express ESAM (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without ESAM | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.3, -0.6); signed map (-1.4, 45.8). **Vector** length 52.0, 6.87% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | endothelial cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,752,583-124,762,290 (-) |
| Ensembl biotype | protein_coding |
| Also known as | W117m |
| Gene groups (HGNC) | V-set domain containing; IgCAM CXADR-related subfamily |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AP7](https://www.uniprot.org/uniprotkb/Q96AP7) (Endothelial cell-selective adhesion molecule):

> Can mediate aggregation most likely through a homophilic molecular interaction.

**Summary**, from NCBI Gene [90952](https://www.ncbi.nlm.nih.gov/gene/90952):

> Enables cell-cell adhesion mediator activity and identical protein binding activity. Involved in several processes, including bicellular tight junction assembly; cell-cell adhesion; and regulation of actin filament polymerization. Located in cell-cell junction and plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17474) · Entrez [90952](https://www.ncbi.nlm.nih.gov/gene/90952) · UniProt [Q96AP7](https://www.uniprot.org/uniprotkb/Q96AP7) · Ensembl [ENSG00000149564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149564)

## Data

Gene col 7389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7389); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7389]; `tensor/DDL_lfc|DDL_z.npy` [7389]; `embed/gene_vectors.npy` [7389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7389 or target_col == 7389). Every well: [[ESAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
