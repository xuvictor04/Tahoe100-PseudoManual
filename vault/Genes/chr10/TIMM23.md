---
symbol: "TIMM23"
type: "gene"
col: 15455
ensembl_id: "ENSG00000265354"
name: "translocase of inner mitochondrial membrane 23"
location: "10q11.22"
module: 33
arm: "+"
pooled_cpm: 42.17
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TIMM23

*translocase of inner mitochondrial membrane 23* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.65× (z +20.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.884× (z -7.9, q 1e-12, down in 6 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.820× (z -5.1, q 6e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM23B]] (+0.83, fdr 7e-06), [[NOL10]] (+0.68, fdr 7e-06), [[TSFM]] (+0.68, fdr 1e-05); moves opposite to [[SDCBP]] (-0.59, fdr 1e-05), [[NOTCH2NLB]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SATB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.65×** | +20.5 | 0e+00 | 48/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.02×** | +17.1 | 0e+00 | 43/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +10.6 | 8e-24 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +9.6 | 1e-19 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +8.6 | 6e-16 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.65×** | +8.4 | 4e-15 | 31/45 (NCI-H460, A-172, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.8 | 4e-13 | 35/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +7.2 | 5e-11 | 27/34 (SK-MEL-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.44×** | +6.7 | 1e-09 | 30/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.41×** | +6.2 | 3e-08 | 27/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.41×** | +6.2 | 3e-08 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.5 | 2e-06 | 25/48 (SW480, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +5.3 | 5e-06 | 26/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 1e-05 | 26/48 (CFPAC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +5.1 | 1e-05 | 24/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 7e-05 | 25/48 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 1e-04 | 20/48 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 20/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.003 | 12/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.025 | 11/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.042 | 11/48 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.044 | 14/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.070 | 8/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.073 | 8/48 (PANC-1, NCI-H460, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -7.9 | 1e-12 | 6/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -6.6 | 2e-08 | 23/40 (SW 900, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -5.1 | 6e-05 | 27/48 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -4.5 | 1e-03 | 24/47 (HepG2/C3A, SW480, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.816×** | -3.7 | 0.024 | 17/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.826×** | -3.5 | 0.046 | 16/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.046 | 13/48 (AsPC-1, RKO, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -3.0 | 0.16 | 10/48 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.16 | 12/47 (A-427, NCI-H23, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.9 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.12× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 61.3 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 42.5 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +12.2) | — |
| [[A-172 (line)]] | wt | 37.7 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.62× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 38.8 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.34× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 38.2 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 13.4× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 35.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 50.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 61.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.10× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 29.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +11.3) | — |
| [[KATO III (line)]] | alt | 30.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 15.3× (z +11.3) | — |
| [[LoVo (line)]] | wt | 38.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 17.0× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +11.6) | — |
| [[RKO (line)]] | wt | 97.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 55.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.58× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0630× (z -21.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 49.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.31× (z +9.6) | — |
| [[A-427 (line)]] | wt | 43.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.26× (z +9.6) | — |
| [[A549 (line)]] | wt | 41.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 46.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.63× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0675× (z -19.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 31.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +10.2) | — |
| [[H4 (line)]] | wt | 37.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.4× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 40.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 33.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 32.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.2× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 32.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.50× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 45.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.53× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 39.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.04× (z +8.8) | — |
| [[SW48 (line)]] | wt | 46.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.71× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B]] | +0.83 | +0.78 / +0.86 | both halves | 7e-06 | same gene group; STRING 545 |
| [[NOL10]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TSFM]] | +0.68 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[CTU1]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[UBOX5]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZNF16]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SRM]] | +0.66 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[MRPL3]] | +0.65 | +0.71 / +0.63 | both halves | 7e-06 | same gene group |
| [[GTF3C2]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EIF3B]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[USPL1]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[WDR3]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NOTCH2NLB]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1]] | B | SATB1 activity lowers TIMM23's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.14× higher at baseline in the lines without SATB1 | 0.079 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.2, -16.5); signed map (-42.0, -17.6). **Vector** length 73.4, 15.9% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +20.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.2 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +2.9 | +3.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.9 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.5 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | +10.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:45,972,489-46,003,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIM23 |
| Gene groups (HGNC) | TIM23 complex; Small nucleolar RNA protein coding host genes; Tim17 family |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O14925](https://www.uniprot.org/uniprotkb/O14925) (Mitochondrial import inner membrane translocase subunit Tim23):

> Essential component of the TIM23 complex, a complex that mediates the translocation of transit peptide-containing proteins across the mitochondrial inner membrane. Has a role in the activation of stress-induced mitophagy by protecting PINK1 from OMA1-mediated degradation and facilitating its accumulation at the outer mitochondrial membrane in response to depolarization.

**Summary**, from NCBI Gene [100287932](https://www.ncbi.nlm.nih.gov/gene/100287932):

> The protein encoded by this gene is part of a complex located in the inner mitochondrial membrane that mediates the transport of transit peptide-containing proteins across the membrane. Multiple transcript variants, one protein-coding and others not protein-coding, have been found for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:17312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17312) · Entrez [100287932](https://www.ncbi.nlm.nih.gov/gene/100287932) · UniProt [O14925](https://www.uniprot.org/uniprotkb/O14925) · Ensembl [ENSG00000265354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265354)

## Data

Gene col 15455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15455); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15455]; `tensor/DDL_lfc|DDL_z.npy` [15455]; `embed/gene_vectors.npy` [15455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15455 or target_col == 15455). Every well: [[TIMM23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
