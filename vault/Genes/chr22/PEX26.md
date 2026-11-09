---
symbol: "PEX26"
type: "gene"
col: 13251
ensembl_id: "ENSG00000215193"
name: "peroxisomal biogenesis factor 26"
location: "22q11.21"
module: 5
arm: "+"
pooled_cpm: 31.87
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PEX26

*peroxisomal biogenesis factor 26* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +15.3, q 0e+00, up in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.94× (z +9.1, q 1e-17, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.704× (z -13.1, q 3e-36, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP42]] (+0.73, fdr 7e-06), [[TMEM138]] (+0.69, fdr 7e-06), [[MAPKAPK5]] (+0.68, fdr 1e-05); moves opposite to [[JPT1]] (-0.59, fdr 3e-05), [[RYBP]] (-0.58, fdr 4e-05), [[ING1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +15.3 | 0e+00 | 35/45 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +14.5 | 3e-45 | 30/39 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +12.9 | 1e-35 | 32/41 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +11.0 | 9e-26 | 40/46 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +9.1 | 1e-17 | 34/48 (Panc 03.27, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.2 | 2e-14 | 31/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +6.1 | 9e-08 | 23/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +6.1 | 1e-07 | 23/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +5.7 | 7e-07 | 19/46 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 5e-05 | 16/46 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.5 | 4e-04 | 10/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.2 | 0.001 | 15/47 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +4.1 | 0.002 | 12/47 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +4.0 | 0.002 | 8/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 16/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.029 | 1/48 (LS 180) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.040 | 10/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.095 | 2/48 (NCI-H23, HT-29) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -13.1 | 3e-36 | 34/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -12.4 | 6e-33 | 38/48 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.753×** | -7.5 | 1e-11 | 32/48 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.771×** | -6.9 | 1e-09 | 24/48 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.779×** | -6.6 | 5e-09 | 23/48 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.826×** | -4.9 | 1e-04 | 18/48 (PANC-1, MIA PaCa-2, …) | top dose only | composition shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.015 | 10/47 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 5 µM | ⚠ toxic | **0.786×** | -3.3 | 0.064 | 10/45 (A549, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 0.840× | -3.3 | 0.064 | 12/45 (H4, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.885× | -3.2 | 0.068 | 6/48 (SW 1271, NCI-H460, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.801× | -3.1 | 0.11 | 7/45 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 0.892× | -3.0 | 0.12 | 10/47 (Hs 766T, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 52.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 27.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.5) |
| [[PANC-1 (line)]] | alt | 20.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -17.8) |
| [[C32 (line)]] | wt | 36.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.7) |
| [[LS 180 (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 48.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -19.7) |
| [[A-427 (line)]] | wt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.4) |
| [[A498 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.133× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.203× (z -9.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.9) |
| [[J82 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.9) |
| [[KATO III (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.37× (z +9.5) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP42]] | +0.73 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TMEM138]] | +0.69 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.68 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[LARP4]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[COMT]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[NADK]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SENP3]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[HSF1]] | +0.64 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[UBE2L3]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPT1]] | -0.59 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RYBP]] | -0.58 | -0.40 / -0.59 | both halves | 4e-05 |  |
| [[ING1]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TMEM205]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CDKL5]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[LGALS1]] | -0.57 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[NBPF19]] | -0.56 | -0.49 / -0.61 | both halves | 2e-05 |  |
| [[FSCN1]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[BTG1]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[DNAJC1]] | -0.55 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[SHOC2]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[BIK]] | -0.54 | -0.39 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PEX26's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity lowers PEX26's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.1, -30.7); signed map (-8.4, -42.3). **Vector** length 96.1, 20.2% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +14.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +15.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -6.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -0.2 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:18,077,923-18,105,396 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20695 |
| Gene groups (HGNC) | Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Class I peroxisomal membrane protein import; Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z412](https://www.uniprot.org/uniprotkb/Q7Z412) (Peroxisome assembly protein 26):

> Peroxisomal docking factor that anchors PEX1 and PEX6 to peroxisome membranes. PEX26 is therefore required for the formation of the PEX1-PEX6 AAA ATPase complex, a complex that mediates the extraction of the PEX5 receptor from peroxisomal membrane.

**Summary**, from NCBI Gene [55670](https://www.ncbi.nlm.nih.gov/gene/55670):

> This gene belongs to the peroxin-26 gene family. It is probably required for protein import into peroxisomes. It anchors PEX1 and PEX6 to peroxisome membranes, possibly to form heteromeric AAA ATPase complexes required for the import of proteins into peroxisomes. Defects in this gene are the cause of peroxisome biogenesis disorder complementation group 8 (PBD-CG8). PBD refers to a group of peroxisomal disorders arising from a failure of protein import into the peroxisomal membrane or matrix. …

**Accessions** — [HGNC:22965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22965) · Entrez [55670](https://www.ncbi.nlm.nih.gov/gene/55670) · UniProt [Q7Z412](https://www.uniprot.org/uniprotkb/Q7Z412) · Ensembl [ENSG00000215193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215193)

## Data

Gene col 13251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13251); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13251]; `tensor/DDL_lfc|DDL_z.npy` [13251]; `embed/gene_vectors.npy` [13251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13251 or target_col == 13251). Every well: [[PEX26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
