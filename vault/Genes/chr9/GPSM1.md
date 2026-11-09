---
symbol: "GPSM1"
type: "gene"
col: 8345
ensembl_id: "ENSG00000160360"
name: "G protein signaling modulator 1"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 12.58
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GPSM1

*G protein signaling modulator 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.44× (z +4.2, q 0.014, up in 19 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.319× (z -18.6, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP3]] (+0.73, fdr 7e-06), [[MIER2]] (+0.69, fdr 1e-05), [[ZNF598]] (+0.69, fdr 1e-05); moves opposite to [[ITM2B]] (-0.61, fdr 3e-05), [[HFE]] (-0.60, fdr 2e-05), [[ATRAID]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GRHL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.014 | 19/44 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.055 | 11/44 (SK-MEL-2, SW 900, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +3.6 | 0.055 | 15/45 (HT-29, NCI-H460, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.38×** | +3.5 | 0.055 | 11/43 (RKO, A-172, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.092 | 13/43 (SNU-1, A498, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.48× | +3.2 | 0.11 | 10/42 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.319×** | -18.6 | 0e+00 | 41/43 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.332×** | -12.2 | 8e-32 | 32/43 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.490×** | -11.6 | 5e-29 | 36/45 (MIA PaCa-2, SNU-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.410×** | -9.9 | 8e-21 | 33/44 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.588×** | -8.6 | 6e-16 | 34/46 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -6.8 | 8e-10 | 33/46 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.571×** | -6.5 | 9e-09 | 28/46 (SNU-423, A-427, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.587×** | -6.1 | 6e-08 | 30/45 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.589×** | -6.1 | 7e-08 | 27/45 (SNU-423, A-427, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.696×** | -5.9 | 2e-07 | 24/46 (SNU-1, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.608×** | -5.7 | 6e-07 | 23/46 (LoVo, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.613×** | -5.6 | 9e-07 | 22/35 (hTERT-HPNE, A-172, …) | two highest doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.642×** | -4.9 | 4e-05 | 24/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.655×** | -4.9 | 4e-05 | 20/46 (NCI-H23, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -4.4 | 4e-04 | 19/43 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.005 | 15/44 (NCI-H1792, AN3 CA, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.559×** | -3.5 | 0.012 | 15/42 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.581×** | -3.3 | 0.026 | 9/41 (RKO, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Nevirapine (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.042 | 11/43 (SW 900, H4, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.759×** | -3.0 | 0.048 | 12/43 (AN3 CA, SW1417, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.050 | 12/46 (HCT15, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -17.8) |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0527× (z -13.3) |
| [[J82 (line)]] | alt | 18.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -14.9) |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0361× (z -14.9) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -13.3) |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -13.7) |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -11.2) |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0909× (z -16.8) |
| [[HS-578T (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 8.40 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -10.0) |
| [[RKO (line)]] | wt | 33.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0873× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -9.9) |
| [[SW480 (line)]] | alt | 9.29 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -12.9) |
| [[A498 (line)]] | wt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -10.0) |
| [[C32 (line)]] | wt | 13.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0576× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 6.83 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.6) |
| [[KATO III (line)]] | alt | 7.79 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 9.31 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.136× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 6.77 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -8.6) |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -13.2) |
| [[SW48 (line)]] | wt | 23.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0992× (z -14.4) |
| [[A-172 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 | STRING 409 |
| [[MIER2]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.69 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DVL1]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[DPH7]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[FPGS]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ZDHHC18]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[AP1M1]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SIN3B]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2B]] | -0.61 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[HFE]] | -0.60 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ATRAID]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[DECR1]] | -0.56 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[MBNL1]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MBNL3]] | -0.55 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[TMEM123]] | -0.55 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[NQO1]] | -0.54 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ARL6IP5]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PARP8]] | -0.52 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]] | B | GRHL2 activity lowers GPSM1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.04× higher at baseline in the lines without GRHL2 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[KIF26A]] | B | KIF26A activity raises GPSM1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without KIF26A | 0.022 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[TGFB1I1]] | B | TGFB1I1 activity raises GPSM1's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without TGFB1I1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[TOP2A]] | B | TOP2A activity raises GPSM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYT7]] | B | SYT7 activity lowers GPSM1's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.72× higher at baseline in the lines without SYT7 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-3.2, -26.2); signed map (-29.4, 2.6). **Vector** length 91.9, 20.2% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.8 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -18.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -8.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -6.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | G protein signaling modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,327,476-136,359,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AGS3, DKFZP727I051 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 3 pathways, smallest: G alpha (i) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YR5](https://www.uniprot.org/uniprotkb/Q86YR5) (G protein-signaling modulator 1):

> Guanine nucleotide dissociation inhibitor (GDI) which functions as a receptor-independent activator of heterotrimeric G protein signaling. Keeps G(i/o) alpha subunit in its GDP-bound form thus uncoupling heterotrimeric G proteins signaling from G protein-coupled receptors. Controls spindle orientation and asymmetric cell fate of cerebral cortical progenitors. May also be involved in macroautophagy in intestinal cells. May play a role in drug addiction.

**Summary**, from NCBI Gene [26086](https://www.ncbi.nlm.nih.gov/gene/26086):

> G-protein signaling modulators (GPSMs) play diverse functional roles through their interaction with G-protein subunits. This gene encodes a receptor-independent activator of G protein signaling, which is one of several factors that influence the basal activity of G-protein signaling systems. The protein contains seven tetratricopeptide repeats in its N-terminal half and four G-protein regulatory (GPR) motifs in its C-terminal half. Multiple alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:17858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17858) · Entrez [26086](https://www.ncbi.nlm.nih.gov/gene/26086) · UniProt [Q86YR5](https://www.uniprot.org/uniprotkb/Q86YR5) · Ensembl [ENSG00000160360](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160360)

## Data

Gene col 8345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8345); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8345]; `tensor/DDL_lfc|DDL_z.npy` [8345]; `embed/gene_vectors.npy` [8345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8345 or target_col == 8345). Every well: [[GPSM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPSM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
