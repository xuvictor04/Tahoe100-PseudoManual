---
symbol: "SYT1"
type: "gene"
col: 868
ensembl_id: "ENSG00000067715"
name: "synaptotagmin 1"
location: "12q21.2"
module: 9
arm: "+"
pooled_cpm: 158.84
n_lines_expressing: 30
n_dd_up: 22
n_dd_down: 21
n_dd_up_clean: 19
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SYT1

*synaptotagmin 1* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.01× (z +15.4, q 0e+00, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.577× (z -8.6, q 5e-15, down in 18 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAM2]] (+0.67, fdr 7e-06), [[ERBB4]] (+0.66, fdr 7e-06), [[PCDH9]] (+0.63, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ADGRL3]] → it (grade B ⚠); 2 go from it, the strongest it → [[PLCB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +15.4 | 0e+00 | 24/28 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +11.3 | 4e-27 | 24/29 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +7.4 | 3e-11 | 21/28 (NCI-H23, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +7.2 | 1e-10 | 14/28 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.6 | 2e-06 | 8/29 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.4 | 6e-06 | 17/28 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 7e-06 | 17/28 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.9 | 5e-05 | 18/28 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.8 | 1e-04 | 18/27 (A-427, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +4.4 | 6e-04 | 17/29 (NCI-H23, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 1e-03 | 13/28 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.2 | 0.001 | 13/28 (MIA PaCa-2, KATO III, …) | top dose only | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 12/28 (A-427, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.003 | 15/28 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 10/28 (A-172, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.019 | 10/28 (KATO III, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.019 | 16/27 (A-427, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -8.6 | 5e-15 | 18/28 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -7.1 | 3e-10 | 23/28 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.648×** | -6.3 | 4e-08 | 15/27 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -6.3 | 4e-08 | 23/29 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.506×** | -5.6 | 3e-06 | 21/28 (A-427, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -5.2 | 2e-05 | 21/28 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -4.8 | 1e-04 | 20/28 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.721×** | -4.8 | 1e-04 | 19/28 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -4.6 | 3e-04 | 19/28 (A-427, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -4.6 | 3e-04 | 13/28 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -4.5 | 3e-04 | 20/28 (PANC-1, A-172, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.578×** | -4.5 | 4e-04 | 16/28 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.756×** | -4.2 | 0.001 | 10/28 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.002 | 14/28 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.773×** | -4.0 | 0.002 | 15/28 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -4.0 | 0.002 | 17/27 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 136 | 6 | 12 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.38× (z +12.7) | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 178 | 6 | 10 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.06× (z +16.9) | [[Digitoxin (drug)]] 0.5 µM 0.154× (z -20.0) |
| [[COLO 205 (line)]] | alt | 293 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.0) |
| [[A-427 (line)]] | wt | 453 | 4 (1 ⚠) | 7 (4 ⚠) | [[Trametinib (drug)]] 5 µM 2.29× (z +10.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.97× (z +10.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.9) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 119 | 8 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.78× (z +15.9) | [[Digitoxin (drug)]] 5 µM 0.279× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.311× (z -9.8) |
| [[HOP62 (line)]] | alt | 45.9 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.51× (z +13.7) | — |
| [[A-172 (line)]] | wt | 223 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.3) | [[Ixazomib citrate (drug)]] 5 µM 0.384× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 87.2 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +12.5) | — |
| [[SW480 (line)]] | alt | 890 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -20.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[C32 (line)]] | wt | 59.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.55× (z +11.5) | — |
| [[CHP-212 (line)]] | wt | 1,386 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -16.3) ⚠ cell-cycle shift, explains ~9% of this change |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 63.1 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.24× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 178 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 122 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.0) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 71.3 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 3.31× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -8.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 74.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 410 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -12.8) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -10.0) |
| [[H4 (line)]] | wt | 202 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 62.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 744 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SW 900 (line)]] | alt | 597 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.5) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A498 (line)]] | wt | 31.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 33.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 37.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 484 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 33.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM2]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ERBB4]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 | same gene group; pathway: Neuronal System |
| [[PCDH9]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CDH18]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CTNNA2]] | +0.61 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[ADGRV1]] | +0.60 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[MARCHF1]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[B3GALT1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[LINC02484]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ASXL3]] | +0.57 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[LINC01885]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PLCB1]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 | pathway: Neuronal System |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRL3]] | B | ADGRL3 activity raises SYT1's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without ADGRL3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[LINC01885]] | B | LINC01885 activity raises SYT1's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without LINC01885 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383 |
| [[PLCB1]] | B | PLCB1 activity raises SYT1's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without PLCB1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[CDH18]] | B | CDH18 activity raises SYT1's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 2.85× lower at baseline in the lines without CDH18 | 0.074 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent |
| [[BCHE]] | B | BCHE activity raises SYT1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without BCHE | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[EPHA5]] | B | EPHA5 activity raises SYT1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without EPHA5 | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4 |
| [[CSRNP3]] | B | CSRNP3 activity raises SYT1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without CSRNP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[GAP43]] | C | GAP43 activity raises SYT1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.76× lower at baseline in the lines without GAP43 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises SYT1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 3.67× lower at baseline in the lines without PCDH18 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCB1]] | B | SYT1 activity raises PLCB1's level | lines that do not express SYT1 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without SYT1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EDIL3, LAYN, PRRX1 |
| [[GLRB]] | B | SYT1 activity raises GLRB's level | lines that do not express SYT1 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without SYT1 | 0.090 | ⚠ within organs, on part of the lines; also absent: EDIL3, LAYN, PRRX1 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 33.9); signed map (40.6, 35.5). **Vector** length 102, 28.7% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.7 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.2 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.0 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.0 | -6.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.4 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:78,863,993-79,452,008 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P65; previously SYT, SVP65 |
| Gene groups (HGNC) | Synaptotagmins; MicroRNA protein coding host genes |
| Reactome | 19 pathways, smallest: Toxicity of botulinum toxin type G (botG); Neurotoxicity of clostridium toxins; Acetylcholine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P21579](https://www.uniprot.org/uniprotkb/P21579) (Synaptotagmin-1):

> Calcium sensor that participates in triggering neurotransmitter release at the synapse (By similarity). May have a regulatory role in the membrane interactions during trafficking of synaptic vesicles at the active zone of the synapse (By similarity). It binds acidic phospholipids with a specificity that requires the presence of both an acidic head group and a diacyl backbone. A Ca(2+)-dependent interaction between synaptotagmin and putative receptors for activated protein kinase C has also been …

**Summary**, from NCBI Gene [6857](https://www.ncbi.nlm.nih.gov/gene/6857):

> This gene encodes a member of the synaptotagmin protein family. The synaptotagmins are integral membrane proteins of synaptic vesicles that serve as calcium sensors in the process of vesicular trafficking and exocytosis. The encoded protein participates in triggering neurotransmitter release at the synapse in response to calcium binding. Mutations in this gene are associated with Baker-Gordon syndrome. [provided by RefSeq, Jan 2023]

**Accessions** — [HGNC:11509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11509) · Entrez [6857](https://www.ncbi.nlm.nih.gov/gene/6857) · UniProt [P21579](https://www.uniprot.org/uniprotkb/P21579) · Ensembl [ENSG00000067715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067715)

## Data

Gene col 868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 868); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 868]; `tensor/DDL_lfc|DDL_z.npy` [868]; `embed/gene_vectors.npy` [868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 868 or target_col == 868). Every well: [[SYT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
