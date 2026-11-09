---
symbol: "TTLL1"
type: "gene"
col: 1908
ensembl_id: "ENSG00000100271"
name: "TTL family tubulin polyglutamylase complex subunit L1"
location: "22q13.2"
module: 17
arm: "+"
pooled_cpm: 7.07
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 27
n_dd_up_clean: 19
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TTLL1

*TTL family tubulin polyglutamylase complex subunit L1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.82× (z +12.6, q 1e-33, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.210× (z -18.9, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF41]] (+0.67, fdr 5e-05), [[ARMC2]] (+0.66, fdr 7e-06), [[BRAT1]] (+0.66, fdr 2e-05); moves opposite to [[MMADHC-DT]] (-0.61, fdr 6e-04), [[KIF26B]] (-0.57, fdr 1e-04), [[ARRDC3-AS1]] (-0.57, fdr 0.002, ⚠ not reproduced), [[ARSB]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +12.6 | 1e-33 | 38/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.80×** | +12.5 | 1e-33 | 42/47 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +8.6 | 1e-15 | 27/47 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +8.5 | 2e-15 | 30/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.5 | 4e-06 | 22/46 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +5.5 | 4e-06 | 17/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.1 | 2e-05 | 13/33 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 1e-04 | 14/44 (KATO III, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 4e-04 | 17/45 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +4.2 | 0.001 | 13/46 (A498, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 9/47 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.004 | 7/48 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.007 | 9/47 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.009 | 8/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.014 | 4/47 (KATO III, NCI-H1573, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.035 | 7/47 (KATO III, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.210×** | -18.9 | 0e+00 | 43/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.310×** | -14.2 | 3e-43 | 42/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.323×** | -13.7 | 2e-40 | 36/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.343×** | -12.9 | 4e-36 | 31/41 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.347×** | -12.3 | 7e-33 | 36/45 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.390×** | -11.4 | 3e-28 | 37/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.414×** | -10.7 | 1e-24 | 29/46 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.553×** | -10.1 | 3e-22 | 26/42 (PANC-1, Hs 766T, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.472×** | -9.1 | 6e-18 | 29/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.488×** | -8.7 | 2e-16 | 27/45 (Hs 766T, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -7.4 | 7e-12 | 22/37 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -6.8 | 5e-10 | 23/47 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.606×** | -6.1 | 6e-08 | 22/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -5.8 | 2e-07 | 16/43 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -5.6 | 9e-07 | 20/45 (BT-474, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.425×** | -5.4 | 2e-06 | 21/42 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -5.1 | 1e-05 | 18/46 (A-427, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -4.9 | 3e-05 | 19/41 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -4.7 | 8e-05 | 17/48 (SNU-423, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0418× (z -20.9) |
| [[A-427 (line)]] | wt | 12.7 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0656× (z -13.8) |
| [[A549 (line)]] | wt | 6.54 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0509× (z -11.3) |
| [[BT-474 (line)]] | alt | 8.20 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0441× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 5.88 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0822× (z -11.9) |
| [[SW480 (line)]] | alt | 6.12 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0978× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -10.9) |
| [[Hs 766T (line)]] | wt | 8.35 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -17.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0816× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 8.57 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -15.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -9.6) |
| [[SNU-423 (line)]] | alt | 7.12 | 0 | 3 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.107× (z -9.0) |
| [[LoVo (line)]] | wt | 5.17 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0775× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.102× (z -11.8) |
| [[A-172 (line)]] | wt | 8.02 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -9.5) |
| [[A498 (line)]] | wt | 8.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 5.63 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0170× (z -16.3) |
| [[LS 180 (line)]] | wt | 7.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0754× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0874× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 7.93 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0549× (z -9.3) |
| [[SW 900 (line)]] | alt | 4.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0661× (z -8.5) |
| [[AN3 CA (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF41]] | +0.67 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[ARMC2]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[BRAT1]] | +0.66 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ZNF559-ZNF177]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.64 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[BTBD2]] | +0.64 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PLD3]] | +0.61 | +0.37 / +0.61 | both halves | 7e-05 |  |
| [[MAST3]] | +0.61 | +0.32 / +0.49 | both halves | 1e-04 |  |
| [[HEATR6]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[ZNF559]] | +0.60 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[NCK1]] | +0.60 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[TOMM20]] | +0.60 | +0.37 / +0.50 | both halves | 7e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.61 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[KIF26B]] | -0.57 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ARRDC3-AS1]] | -0.57 | -0.14 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[ARSB]] | -0.57 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[MPDU1]] | -0.56 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[CRPPA]] | -0.56 | -0.18 / -0.50 | ⚠ not reproduced | 0.001 |  |
| [[GRIP1]] | -0.56 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[RNF6]] | -0.56 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[USP11]] | -0.56 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[LINC01829]] | -0.56 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[ATXN1L]] | -0.55 | -0.18 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[CDKN2B-AS1]] | -0.55 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[DGKH]] | -0.55 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[ARMT1]] | -0.54 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[RAP2C]] | -0.54 | -0.26 / -0.52 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises TTLL1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without ZNF594-DT | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[TOP2A]] | B | TOP2A activity raises TTLL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNK15-AS1]] | B | KCNK15-AS1 activity raises TTLL1's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without KCNK15-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.6, 27.0); signed map (-26.9, -13.0). **Vector** length 62.7, 10.7% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +12.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +12.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +8.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -5.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TTL family tubulin polyglutamylase complex subunit L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:43,039,516-43,089,419 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGs3, TPGS3; previously C22orf7 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family; Tubulin polyglutamylase complex subunits |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [O95922](https://www.uniprot.org/uniprotkb/O95922) (Polyglutamylase complex subunit TTLL1):

> Catalytic subunit of a polyglutamylase complex which modifies tubulin, generating side chains of glutamate on the gamma-carboxyl group of specific glutamate residues within the C-terminal tail of tubulin. Probably involved in the side-chain elongation step of the polyglutamylation reaction rather than the initiation step. Modifies both alpha- and beta-tubulins with a preference for the alpha-tail. Unlike most polyglutamylases of the tubulin--tyrosine ligase family, only displays a catalytic …

**Summary**, from NCBI Gene [25809](https://www.ncbi.nlm.nih.gov/gene/25809):

> Enables tubulin-glutamic acid ligase activity. Involved in microtubule cytoskeleton organization. Is active in microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1312) · Entrez [25809](https://www.ncbi.nlm.nih.gov/gene/25809) · UniProt [O95922](https://www.uniprot.org/uniprotkb/O95922) · Ensembl [ENSG00000100271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100271)

## Data

Gene col 1908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1908); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1908]; `tensor/DDL_lfc|DDL_z.npy` [1908]; `embed/gene_vectors.npy` [1908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1908 or target_col == 1908). Every well: [[TTLL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
