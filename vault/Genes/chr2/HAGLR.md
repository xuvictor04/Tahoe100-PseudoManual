---
symbol: "HAGLR"
type: "gene"
col: 13386
ensembl_id: "ENSG00000224189"
name: "HOXD antisense growth-associated long non-coding RNA"
location: "2q31.1"
module: 102
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 36
n_dd_up: 33
n_dd_down: 12
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# HAGLR

*HOXD antisense growth-associated long non-coding RNA* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.50× (z +13.6, q 1e-39, up in 20 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.455× (z -11.7, q 4e-29, down in 19 of 22 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.301× (z -11.1, q 4e-26, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF483]] (+0.63, fdr 1e-05), [[RAB6B]] (+0.62, fdr 1e-05), [[MAP6]] (+0.60, fdr 3e-05); moves opposite to [[PDCD7]] (-0.62, fdr 1e-05), [[SPG11]] (-0.56, fdr 3e-05), [[NFX1]] (-0.55, fdr 3e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SEPTIN3]] → it (grade B ⚠); 2 go from it, the strongest it → [[EBF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +13.6 | 1e-39 | 20/30 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +12.1 | 3e-31 | 3/5 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +10.6 | 6e-24 | 7/8 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +9.8 | 1e-20 | 3/5 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.1 | 7e-18 | 10/19 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +9.1 | 9e-18 | 14/23 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +6.8 | 7e-10 | 9/23 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.57×** | +6.8 | 1e-09 | 12/28 (A498, LoVo, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.95×** | +6.7 | 2e-09 | 6/24 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.5 | 2e-06 | 8/27 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +4.9 | 4e-05 | 10/29 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +4.9 | 4e-05 | 1/7 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 9e-05 | 7/26 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 2e-04 | 1/18 (C32) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.54×** | +4.5 | 2e-04 | 6/29 (COLO 205, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.49×** | +4.2 | 8e-04 | 6/27 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.001 | 1/19 (SK-MEL-2) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.005 | 6/26 (NCI-H1573, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +3.7 | 0.005 | 2/23 (SW480, PANC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.006 | 1/17 (SW480) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.006 | 3/25 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.022 | 2/19 (NCI-H1573, LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.455×** | -11.7 | 4e-29 | 19/22 (HepG2/C3A, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.301×** | -11.1 | 4e-26 | 24/26 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -7.4 | 2e-11 | 12/20 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.495×** | -7.4 | 2e-11 | 19/29 (J82, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -5.2 | 2e-05 | 11/26 (LoVo, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -5.0 | 6e-05 | 13/30 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -4.3 | 0.002 | 10/22 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.5 µM |  | **0.715×** | -3.5 | 0.027 | 6/28 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.686×** | -3.5 | 0.031 | 2/30 (RKO, SHP-77) | top dose only | plate-row cell shift |
| [[Ciclopirox (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.075 | 7/24 (C32, NCI-H2347, …) | rises with dose |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.723×** | -3.2 | 0.079 | 3/23 (C32, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.747×** | -3.1 | 0.098 | 7/23 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.1 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.108× (z -9.7) |
| [[LoVo (line)]] | wt | 3.58 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0489× (z -11.3) |
| [[A498 (line)]] | wt | 3.99 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0993× (z -9.4) ⚠ transcription drop |
| [[C32 (line)]] | wt | 6.10 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0645× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 8.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0277× (z -16.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 3.69 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0845× (z -9.3) |
| [[J82 (line)]] | alt | 6.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -10.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 1 | — | [[Proglumide (drug)]] 0.5 µM 0.0573× (z -8.7) |
| [[PANC-1 (line)]] | alt | 3.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0691× (z -16.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 1.83 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0537× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.730 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.634 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.855 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.556 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF483]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.62 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[MAP6]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[TUB]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TMEM150C]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[JAM3]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[AHSA1]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MFAP3L]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.57 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SDK2]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.56 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[BVES-AS1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | -0.62 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SPG11]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[NFX1]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[LINS1]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[LRRC37A2]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[BPTF]] | -0.53 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[C1orf131]] | -0.52 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[HELQ]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD26]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DNAL4]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MRPS18B]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN3]] | B | SEPTIN3 activity raises HAGLR's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without SEPTIN3 | 0.045 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises HAGLR's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without EBF4 | 0.056 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[CACNB4]] | B | CACNB4 activity raises HAGLR's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without CACNB4 | 0.074 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[RET]] | B | RET activity raises HAGLR's level | lines that do not express RET (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without RET | 0.086 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[TMEM98]] | B | TMEM98 activity raises HAGLR's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without TMEM98 | 0.098 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[SCN8A]] | C | SCN8A activity raises HAGLR's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without SCN8A | 0.096 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | HAGLR activity raises EBF4's level | lines that do not express HAGLR (14) vs lines expressing it (36) | 3.19× lower at baseline in the lines without HAGLR | 0.059 | ⚠ within organs, on part of the lines; also absent: ARNT2, BEND6, ITPR1 |
| [[HELQ]] | B | HAGLR activity raises HELQ's level | lines that do not express HAGLR (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without HAGLR | 0.090 | ⚠ within organs, on part of the lines; also absent: ARNT2, BEND6, ITPR1 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.9, 40.9); signed map (25.2, 28.6). **Vector** length 39.3, 6.00% of its response variance represented; |z| ≥ 3 in 651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.1 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HOXD antisense growth-associated long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.1 — chr2:176,164,051-176,188,958 (-) |
| Ensembl biotype | lncRNA |
| Also known as | Mdgt, MIR7704HG, STEEL; previously HOXD-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43755) · Entrez [401022](https://www.ncbi.nlm.nih.gov/gene/401022) · Ensembl [ENSG00000224189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224189)

## Data

Gene col 13386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13386); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13386]; `tensor/DDL_lfc|DDL_z.npy` [13386]; `embed/gene_vectors.npy` [13386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13386 or target_col == 13386). Every well: [[HAGLR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAGLR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
