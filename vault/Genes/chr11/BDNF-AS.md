---
symbol: "BDNF-AS"
type: "gene"
col: 14435
ensembl_id: "ENSG00000245573"
name: "BDNF antisense RNA"
location: "11p14.1"
module: 10
arm: "+"
pooled_cpm: 12.23
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 18
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# BDNF-AS

*BDNF antisense RNA* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +8.8, q 6e-16, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.337× (z -9.5, q 1e-18, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEXIM2-AS1]] (+0.85, fdr 7e-06), [[MAD2L1-DT]] (+0.84, fdr 7e-06), [[ANKRD17-DT]] (+0.84, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.69, fdr 7e-05), [[SH3PXD2B]] (-0.69, fdr 1e-04), [[ANKRD27]] (-0.67, fdr 8e-04, ⚠ one half only (not replicated)), [[FCHO1]] (-0.66, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TMEM9B-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +8.8 | 6e-16 | 34/44 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.8 | 4e-09 | 35/48 (A498, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.1 | 3e-07 | 35/45 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +4.5 | 8e-04 | 28/47 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.005 | 23/47 (SW480, C32, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.0 | 0.006 | 20/46 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.007 | 18/45 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.007 | 22/48 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +3.8 | 0.007 | 18/47 (RKO, A498, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.009 | 16/48 (C-33 A, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.7 | 0.009 | 20/41 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.018 | 18/48 (SW480, A498, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +3.5 | 0.018 | 19/47 (A498, A-427, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.019 | 20/44 (SW480, NCI-H23, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.020 | 20/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.04×** | +3.2 | 0.037 | 10/46 (SW480, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.2 | 0.046 | 14/47 (A498, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.337×** | -9.5 | 1e-18 | 36/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.401×** | -8.0 | 4e-13 | 35/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.438×** | -7.2 | 1e-10 | 34/45 (SW1417, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.444×** | -6.9 | 6e-10 | 32/47 (HT-29, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.484×** | -6.3 | 3e-08 | 33/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.504×** | -5.8 | 5e-07 | 30/46 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -5.4 | 6e-06 | 30/44 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.588×** | -4.5 | 4e-04 | 26/46 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.594×** | -4.4 | 7e-04 | 23/40 (A-427, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.611×** | -4.3 | 9e-04 | 25/48 (SW48, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.414×** | -4.0 | 0.003 | 18/47 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.735×** | -3.8 | 0.007 | 22/48 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -3.7 | 0.008 | 20/44 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.563×** | -3.6 | 0.014 | 19/48 (RKO, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.458×** | -3.6 | 0.014 | 16/45 (NCI-H460, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.705×** | -3.1 | 0.080 | 19/48 (Hs 766T, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.698×** | -3.0 | 0.082 | 13/47 (NCI-H460, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 24.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -8.6) |
| [[SW480 (line)]] | alt | 14.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.227× (z -9.1) |
| [[A498 (line)]] | wt | 10.6 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 36.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -11.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 16.4 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.124× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0681× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.9) |
| [[HCT15 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +8.8) | — |
| [[LoVo (line)]] | wt | 8.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 6.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0559× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 9.15 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0628× (z -10.5) |
| [[SW1417 (line)]] | alt | 8.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0685× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXIM2-AS1]] | +0.85 | +0.84 / +0.61 | both halves | 7e-06 | same gene group |
| [[MAD2L1-DT]] | +0.84 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD17-DT]] | +0.84 | +0.86 / +0.62 | both halves | 7e-06 |  |
| [[UFL1-AS1]] | +0.82 | +0.84 / +0.54 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.81 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.80 | +0.83 / +0.43 | both halves | 3e-05 |  |
| [[LINC02340]] | +0.79 | +0.88 / +0.55 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.78 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.78 | +0.80 / +0.50 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.77 | +0.81 / +0.44 | both halves | 3e-05 |  |
| [[USP38-DT]] | +0.77 | +0.83 / +0.48 | both halves | 2e-05 |  |
| [[DNAI4]] | +0.77 | +0.78 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.69 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[SH3PXD2B]] | -0.69 | -0.68 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.67 | -0.69 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[FCHO1]] | -0.66 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[CCDC134]] | -0.66 | -0.58 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises BDNF-AS's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without TMEM9B-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BDNF-AS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FCHO1]] | B | FCHO1 activity lowers BDNF-AS's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.38× higher at baseline in the lines without FCHO1 | 0.045 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[MTUS1-DT]] | B | MTUS1-DT activity lowers BDNF-AS's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.19× higher at baseline in the lines without MTUS1-DT | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers BDNF-AS's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[DPH6-DT]] | C | DPH6-DT activity raises BDNF-AS's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.4, 17.0); signed map (27.9, -9.6). **Vector** length 86.0, 20.5% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | BDNF antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p14.1 — chr11:27,506,830-27,698,231 (+) |
| Ensembl biotype | lncRNA |
| Also known as | BT2A, BT2B, BT2C, BT2D, NCRNA00049, BDNF-AS1, BDNFAS; previously BDNFOS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20608) · Entrez [497258](https://www.ncbi.nlm.nih.gov/gene/497258) · Ensembl [ENSG00000245573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245573)

## Data

Gene col 14435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14435); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14435]; `tensor/DDL_lfc|DDL_z.npy` [14435]; `embed/gene_vectors.npy` [14435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14435 or target_col == 14435). Every well: [[BDNF-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BDNF-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
