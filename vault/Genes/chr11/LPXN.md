---
symbol: "LPXN"
type: "gene"
col: 3102
ensembl_id: "ENSG00000110031"
name: "leupaxin"
location: "11q12.1"
module: 80
arm: "+"
pooled_cpm: 19.6
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# LPXN

*leupaxin* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.96× (z +34.5, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.533× (z -9.6, q 5e-19, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.80, fdr 1e-05), [[UBE2D3-AS1]] (+0.75, fdr 3e-05), [[PATL2]] (+0.74, fdr 2e-05); moves opposite to [[ANKRD27]] (-0.73, fdr 1e-05), [[SLC9A6]] (-0.70, fdr 4e-05), [[ATRN]] (-0.69, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.96×** | +34.5 | 0e+00 | 43/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.11×** | +30.4 | 0e+00 | 43/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.01×** | +21.1 | 0e+00 | 41/46 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.53×** | +18.5 | 0e+00 | 43/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.6 | 4e-29 | 33/48 (A-427, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +10.3 | 9e-23 | 25/33 (LoVo, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +10.0 | 2e-21 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +9.1 | 9e-18 | 29/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.5 | 1e-15 | 29/45 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.2 | 1e-14 | 28/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +7.4 | 5e-12 | 26/47 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +6.2 | 3e-08 | 23/47 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.2 | 3e-08 | 19/36 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 8e-06 | 19/47 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.5 | 2e-04 | 12/26 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 3e-04 | 17/46 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 16/46 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 15/48 (SW480, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.533×** | -9.6 | 5e-19 | 30/48 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -8.8 | 4e-16 | 28/47 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.645×** | -6.7 | 5e-09 | 25/48 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -5.8 | 1e-06 | 25/45 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.753×** | -4.3 | 0.002 | 16/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.764×** | -3.9 | 0.007 | 19/43 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.775×** | -3.9 | 0.008 | 17/44 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -3.3 | 0.064 | 13/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 35.2 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.9) | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -10.2) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -9.8) |
| [[A-427 (line)]] | wt | 25.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 8.84× (z +15.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.276× (z -8.9) ⚠ toxic |
| [[C32 (line)]] | wt | 91.3 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.125× (z -16.1) |
| [[LoVo (line)]] | wt | 22.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +25.4) | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 105 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 13.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +17.4) | [[Digitoxin (drug)]] 0.05 µM 0.109× (z -12.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 9.87 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 24.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +18.5) | — |
| [[NCI-H1792 (line)]] | alt | 90.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.0996× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 6.70 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +12.9) | [[Carbamazepine (drug)]] 0.5 µM 0.196× (z -8.5) |
| [[PANC-1 (line)]] | alt | 12.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.176× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -12.2) |
| [[A498 (line)]] | wt | 10.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 36.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +15.2) | — |
| [[J82 (line)]] | alt | 10.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 12.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 21.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +15.2) | — |
| [[LS 180 (line)]] | wt | 10.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 6.53 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +15.7) | — |
| [[RKO (line)]] | wt | 16.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 14.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +16.8) | — |
| [[SW480 (line)]] | alt | 12.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 5.24 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.23× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 9.53 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +18.3) | — |
| [[HCT15 (line)]] | alt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 11.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 8.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 48.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.237× (z -8.5) |
| [[SW48 (line)]] | wt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[SW1417 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +14.0) | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.80 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.75 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[PATL2]] | +0.74 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[LINC00863]] | +0.73 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[PDCL3P4]] | +0.73 | +0.79 / +0.48 | both halves | 2e-05 |  |
| [[USP11]] | +0.73 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.75 / +0.25 | both halves | 4e-04 |  |
| [[NEK8]] | +0.72 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[PPP3CB-AS1]] | +0.72 | +0.67 / +0.36 | both halves | 1e-04 |  |
| [[LINC00705]] | +0.72 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.72 | +0.76 / +0.30 | both halves | 2e-04 |  |
| [[LINC01829]] | +0.72 | +0.64 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | -0.73 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.70 | -0.74 / -0.42 | both halves | 4e-05 |  |
| [[ATRN]] | -0.69 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[MYPOP]] | -0.67 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MAST3]] | -0.66 | -0.62 / -0.25 | both halves | 4e-04 |  |
| [[LPCAT4]] | -0.65 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[TSEN54]] | -0.65 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.65 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.64 | -0.72 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R12B]] | -0.64 | -0.64 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LPXN's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.9% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises LPXN's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ABCA10]] | B | ABCA10 activity raises LPXN's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without ABCA10 | 0.079 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[UBE2D3-AS1]] | C | UBE2D3-AS1's natural level strengthens LPXN's drug response | UBE2D3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.21; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.870). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, 10.6); signed map (21.8, -5.4). **Vector** length 122, 32.5% of its response variance represented; |z| ≥ 3 in 1,286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +34.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +30.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.9 | +21.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +18.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.9 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.6 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.0 | -6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.8 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.4 | -9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | leupaxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:58,526,871-58,578,220 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LDPL |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O60711](https://www.uniprot.org/uniprotkb/O60711) (Leupaxin):

> Transcriptional coactivator for androgen receptor (AR) and serum response factor (SRF). Contributes to the regulation of cell adhesion, spreading and cell migration and acts as a negative regulator in integrin-mediated cell adhesion events. Suppresses the integrin-induced tyrosine phosphorylation of paxillin (PXN). May play a critical role as an adapter protein in the formation of the adhesion zone in osteoclasts. Negatively regulates B-cell antigen receptor (BCR) signaling.

**Summary**, from NCBI Gene [9404](https://www.ncbi.nlm.nih.gov/gene/9404):

> The product encoded by this gene is preferentially expressed in hematopoietic cells and belongs to the paxillin protein family. Similar to other members of this focal-adhesion-associated adaptor-protein family, it has four leucine-rich LD-motifs in the N-terminus and four LIM domains in the C-terminus. It may function in cell type-specific signaling by associating with PYK2, a member of focal adhesion kinase family. As a substrate for a tyrosine kinase in lymphoid cells, this protein may also …

**Accessions** — [HGNC:14061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14061) · Entrez [9404](https://www.ncbi.nlm.nih.gov/gene/9404) · UniProt [O60711](https://www.uniprot.org/uniprotkb/O60711) · Ensembl [ENSG00000110031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110031)

## Data

Gene col 3102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3102); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3102]; `tensor/DDL_lfc|DDL_z.npy` [3102]; `embed/gene_vectors.npy` [3102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3102 or target_col == 3102). Every well: [[LPXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
