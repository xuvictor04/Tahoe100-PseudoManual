---
symbol: "NELFCD"
type: "gene"
col: 2081
ensembl_id: "ENSG00000101158"
name: "negative elongation factor complex member C/D"
location: "20q13.32"
module: 25
arm: "+"
pooled_cpm: 45.85
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# NELFCD

*negative elongation factor complex member C/D* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +11.0, q 1e-25, up in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.03× (z +7.4, q 3e-11, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.651× (z -12.1, q 4e-31, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCCPDH]] (+0.69, fdr 7e-06), [[GUF1]] (+0.69, fdr 2e-05), [[EXOSC10]] (+0.67, fdr 1e-05); moves opposite to [[SEC61G]] (-0.66, fdr 4e-05), [[RPL36AL]] (-0.65, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RABGEF1]] (-0.64, fdr 2e-05), [[WNT2B]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +11.0 | 1e-25 | 37/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.4 | 7e-23 | 29/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +7.4 | 3e-11 | 32/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +6.9 | 1e-09 | 29/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.27×** | +6.7 | 3e-09 | 28/48 (A498, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.3 | 2e-08 | 26/48 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.9 | 2e-07 | 29/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +5.9 | 3e-07 | 27/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.8 | 4e-07 | 25/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +5.8 | 4e-07 | 26/45 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +5.5 | 2e-06 | 28/48 (SW480, H4, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 28/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +4.7 | 1e-04 | 22/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +4.2 | 9e-04 | 23/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 21/48 (NCI-H1573, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.014 | 15/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.073 | 10/48 (BT-474, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -12.1 | 4e-31 | 35/48 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.550×** | -11.1 | 5e-26 | 45/48 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -10.7 | 2e-24 | 38/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.590×** | -9.8 | 2e-20 | 45/48 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.653×** | -8.1 | 5e-14 | 41/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.761×** | -5.5 | 4e-06 | 29/48 (C-33 A, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.612×** | -5.1 | 2e-05 | 21/48 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -5.0 | 4e-05 | 22/48 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -4.5 | 5e-04 | 21/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -4.2 | 0.001 | 16/48 (AN3 CA, hTERT-HPNE, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.013 | 19/48 (SW480, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.024 | 16/48 (RKO, HT-29, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.892× | -3.2 | 0.051 | 6/48 (HCT15, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.6 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 142 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 42.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.9) |
| [[RKO (line)]] | wt | 67.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.2) ⚠ cell-cycle shift, explains ~51% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -14.0) |
| [[SW480 (line)]] | alt | 68.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.5) | — |
| [[A498 (line)]] | wt | 28.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.4) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +9.4) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.5) |
| [[Hs 766T (line)]] | wt | 52.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.0) |
| [[KATO III (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 39.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 32.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 82.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -15.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 87.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.5) |
| [[A-172 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCCPDH]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[GUF1]] | +0.69 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[EXOSC10]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[MCCC2]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 | STRING 921 |
| [[TRUB1]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[C2CD5]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[IMPACT]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MRPL42]] | +0.65 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[MANEA]] | +0.65 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.65 | +0.39 / +0.72 | both halves | 6e-05 |  |
| [[MBTPS2]] | +0.65 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[ATIC]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61G]] | -0.66 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[RPL36AL]] ⚠ | -0.65 | -0.56 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RABGEF1]] | -0.64 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[WNT2B]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[KCNK6]] | -0.61 | -0.34 / -0.71 | both halves | 1e-04 |  |
| [[ZBTB7A]] | -0.60 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[PLIN3]] | -0.60 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[ATP5MK]] | -0.60 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[C19orf81]] | -0.59 | -0.37 / -0.65 | both halves | 7e-05 |  |
| [[SELENOK]] | -0.59 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[RABAC1]] | -0.58 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[COMMD6]] | -0.58 | -0.39 / -0.65 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NELFCD's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.8, -16.3); signed map (-1.4, -37.3). **Vector** length 91.5, 22.6% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.6 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -12.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.4 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | +0.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | negative elongation factor complex member C/D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,981,208-58,995,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC130, TH1, NELF-C, NELF-D; previously TH1L |
| Gene groups (HGNC) | Armadillo like helical domain containing; Negative elongation factor complex members |
| Hallmark sets | DNA_REPAIR |
| Reactome | 25 pathways, smallest: Abortive elongation of HIV-1 transcript in the absence of Tat; Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXH7](https://www.uniprot.org/uniprotkb/Q8IXH7) (Negative elongation factor C/D):

> Essential component of the NELF complex, a complex that negatively regulates the elongation of transcription by RNA polymerase II. The NELF complex, which acts via an association with the DSIF complex and causes transcriptional pausing, is counteracted by the P-TEFb kinase complex.; (Microbial infection) The NELF complex is involved in HIV-1 latency possibly involving recruitment of PCF11 to paused RNA polymerase II.

**Summary**, from NCBI Gene [51497](https://www.ncbi.nlm.nih.gov/gene/51497):

> The NELF complex of proteins interacts with the DSIF protein complex to repress transcriptional elongation by RNA polymerase II. The protein encoded by this gene is an essential part of the NELF complex. Alternative translation initiation site usage results in the formation of two isoforms with different N-termini. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15934) · Entrez [51497](https://www.ncbi.nlm.nih.gov/gene/51497) · UniProt [Q8IXH7](https://www.uniprot.org/uniprotkb/Q8IXH7) · Ensembl [ENSG00000101158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101158)

## Data

Gene col 2081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2081); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2081]; `tensor/DDL_lfc|DDL_z.npy` [2081]; `embed/gene_vectors.npy` [2081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2081 or target_col == 2081). Every well: [[NELFCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NELFCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
