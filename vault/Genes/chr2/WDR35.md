---
symbol: "WDR35"
type: "gene"
col: 4031
ensembl_id: "ENSG00000118965"
name: "WD repeat domain 35"
location: "2p24.1"
module: 1
arm: "+"
pooled_cpm: 46.74
n_lines_expressing: 45
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# WDR35

*WD repeat domain 35* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +17.9, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.718× (z -10.1, q 3e-21, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSEN2]] (+0.70, fdr 7e-06), [[RIOK1]] (+0.67, fdr 1e-05), [[DDX10]] (+0.66, fdr 7e-06); moves opposite to [[GNAS]] (-0.62, fdr 1e-05), [[C2]] (-0.56, fdr 1e-04), [[TAX1BP1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[LCLAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +17.9 | 0e+00 | 40/43 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +16.6 | 0e+00 | 37/43 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +16.4 | 0e+00 | 35/43 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +15.5 | 0e+00 | 38/43 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +12.4 | 3e-33 | 37/43 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +11.3 | 1e-27 | 33/43 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +11.2 | 4e-27 | 28/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.20×** | +11.0 | 3e-26 | 33/43 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +10.6 | 3e-24 | 30/42 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +9.4 | 3e-19 | 28/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +9.2 | 2e-18 | 30/43 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +8.6 | 3e-16 | 27/43 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +8.4 | 2e-15 | 29/43 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +8.1 | 2e-14 | 28/42 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +6.5 | 4e-09 | 24/43 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +6.5 | 4e-09 | 26/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +6.3 | 1e-08 | 26/43 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4031.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -10.1 | 3e-21 | 29/43 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -9.7 | 6e-20 | 30/43 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.7 | 4e-09 | 26/43 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -5.1 | 4e-05 | 22/43 (NCI-H23, RKO, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.793×** | -4.8 | 2e-04 | 21/42 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.802×** | -4.8 | 2e-04 | 17/42 (NCI-H2030, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.803×** | -4.6 | 4e-04 | 15/42 (C-33 A, LOX-IMVI, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.815×** | -4.2 | 0.002 | 18/42 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.824×** | -4.2 | 0.002 | 18/43 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.9 | 0.005 | 16/43 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.867× | -3.9 | 0.005 | 16/43 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.671×** | -3.8 | 0.007 | 14/43 (SNU-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.6 | 0.014 | 21/42 (C-33 A, NCI-H2030, …) | all doses, flat | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | 0.860× | -3.3 | 0.046 | 11/43 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 75.1 | 6 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 82.8 | 3 (2 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +8.9) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 7.00× (z +8.8) | [[Adagrasib (drug)]] 0.05 µM 0.636× (z -15.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 28.2 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.0) |
| [[SW480 (line)]] | alt | 68.0 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 31.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +19.5) | — |
| [[NCI-H460 (line)]] | wt | 60.4 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 134 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -23.3) |
| [[A-427 (line)]] | wt | 87.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.555× (z -9.7) |
| [[A498 (line)]] | wt | 41.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.5) |
| [[C32 (line)]] | wt | 35.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 33.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.09× (z +9.9) | — |
| [[RKO (line)]] | wt | 82.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -17.1) |
| [[A549 (line)]] | wt | 78.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 44.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.0) |
| [[LoVo (line)]] | wt | 14.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 72.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0738× (z -12.2) |
| [[H4 (line)]] | wt | 29.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.8) |
| [[Hs 766T (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 45.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -8.6) |
| [[SW 1271 (line)]] | alt | 64.9 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.104× (z -8.6) |
| [[SW 900 (line)]] | alt | 28.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN2]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[DDX10]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[URB2]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZNHIT6]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[CMSS1]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NUBPL]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[MCAT]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[NLE1]] | +0.62 | +0.48 / +0.70 | both halves | 2e-05 | same gene group |
| [[NARS2]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[RRP15]] | +0.62 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 | pathway: Hedgehog 'off' state |
| [[C2]] | -0.56 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TAX1BP1]] | -0.52 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[ATG9A]] | -0.50 | -0.44 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WDR35's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SHOX2]] | B | SHOX2 activity raises WDR35's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without SHOX2 | 0.062 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[MICB]] | B | MICB activity raises WDR35's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without MICB | 0.098 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LCLAT1]] | B | WDR35 activity strengthens LCLAT1's drug response | lines that do not express WDR35 (5) vs lines expressing it (45) | the lines without WDR35 respond 0.90× as strongly (z diff +0.47); rises at some drug-doses, falls at others (71% from rises): TAK-901 5 µM: 1.63x vs 2.65x (z diff +2.5); PH-797804 5 µM: 1.25x vs 1.88x (z diff +2.4); Dinaciclib 0.05 µM: 0.87x vs 0.66x (z diff +1.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: AGK, DUSP19, ENTPD1-AS1; maybe low, not absent; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[CNPY4]] | B | WDR35 activity raises CNPY4's level | lines that do not express WDR35 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without WDR35 | 0.084 | ⚠ within organs, on part of the lines; also absent: AGK, DUSP19, ENTPD1-AS1; maybe low, not absent |
| [[AGK]] | C | WDR35 activity raises AGK's level | lines that do not express WDR35 (5) vs lines expressing it (45) | 3.40× lower at baseline in the lines without WDR35 | 0.040 | ⚠ within organs, on part of the lines; also absent: AGK, DUSP19, ENTPD1-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.2, -42.5); signed map (-7.0, -49.1). **Vector** length 113, 31.4% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:19,910,263-19,990,105 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33196, KIAA1336, IFT121, IFTA1, FAP118, CFAP118 |
| Gene groups (HGNC) | WD repeat domain containing; IFT-A complex |
| Reactome | 6 pathways, smallest: Intraflagellar transport; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2L0](https://www.uniprot.org/uniprotkb/Q9P2L0) (WD repeat-containing protein 35):

> As a component of the IFT complex A (IFT-A), a complex required for retrograde ciliary transport and entry into cilia of G protein-coupled receptors (GPCRs), it is involved in ciliogenesis and ciliary protein trafficking. May promote CASP3 activation and TNF-stimulated apoptosis.

**Summary**, from NCBI Gene [57539](https://www.ncbi.nlm.nih.gov/gene/57539):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Multiple alternatively spliced transcript variants encoding distinct isoforms …

**Accessions** — [HGNC:29250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29250) · Entrez [57539](https://www.ncbi.nlm.nih.gov/gene/57539) · UniProt [Q9P2L0](https://www.uniprot.org/uniprotkb/Q9P2L0) · Ensembl [ENSG00000118965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118965)

## Data

Gene col 4031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4031); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4031]; `tensor/DDL_lfc|DDL_z.npy` [4031]; `embed/gene_vectors.npy` [4031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4031 or target_col == 4031). Every well: [[WDR35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
