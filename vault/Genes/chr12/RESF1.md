---
symbol: "RESF1"
type: "gene"
col: 10517
ensembl_id: "ENSG00000174718"
name: "retroelement silencing factor 1"
location: "12p11.21"
module: 56
arm: "+"
pooled_cpm: 80.3
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RESF1

*retroelement silencing factor 1* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.26× (z +15.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.562× (z -10.1, q 2e-21, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.418× (z -8.7, q 1e-15, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A11]] (+0.56, fdr 3e-05), [[TAF7]] (+0.56, fdr 2e-05), [[MBP]] (+0.54, fdr 3e-05); moves opposite to [[ELP1]] (-0.60, fdr 2e-05), [[TFG]] (-0.58, fdr 1e-05), [[FAM168A]] (-0.57, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +15.5 | 0e+00 | 44/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +8.8 | 4e-16 | 32/48 (AsPC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +8.6 | 1e-15 | 33/48 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.6 | 4e-12 | 29/48 (AsPC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +7.4 | 2e-11 | 26/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 3e-07 | 29/48 (LoVo, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 6e-07 | 30/47 (LS 180, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.5 | 3e-06 | 26/48 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.3 | 7e-06 | 24/49 (LoVo, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +5.2 | 1e-05 | 25/47 (A-172, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 24/48 (NCI-H1573, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +4.1 | 0.002 | 26/47 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 23/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +3.9 | 0.005 | 18/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.005 | 18/48 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.005 | 22/48 (AsPC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.8 | 0.005 | 14/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -10.1 | 2e-21 | 34/45 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -8.7 | 1e-15 | 28/49 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.638×** | -8.5 | 3e-15 | 35/49 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.674×** | -6.6 | 7e-09 | 30/42 (SHP-77, PANC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.741×** | -5.7 | 1e-06 | 26/48 (KATO III, AsPC-1, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.612×** | -4.9 | 1e-04 | 29/48 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -4.7 | 2e-04 | 26/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.796×** | -4.3 | 0.001 | 25/48 (KATO III, HT-29, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.688×** | -3.7 | 0.013 | 20/48 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.846× | -3.2 | 0.086 | 19/48 (SK-MEL-2, SHP-77, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 280 | 8 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +38.1) | [[Panobinostat (drug)]] 5 µM 0.357× (z -11.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.526× (z -9.3) |
| [[KATO III (line)]] | alt | 135 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.70× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.314× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 88.7 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +29.5) | [[Betamethasone dipropionate (drug)]] 5 µM 0.343× (z -8.6) |
| [[PANC-1 (line)]] | alt | 110 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -18.1) |
| [[SNU-423 (line)]] | alt | 90.6 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.85× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 66.8 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +12.6) | — |
| [[LoVo (line)]] | wt | 115 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 74.3 | 3 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 97.4 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 148 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.53× (z +14.6) | [[Osimertinib (mesylate) (drug)]] 5 µM 0.248× (z -10.1) |
| [[COLO 205 (line)]] | alt | 86.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +24.4) | [[Panobinostat (drug)]] 5 µM 0.259× (z -9.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 59.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 82.5 | 4 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.20× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 51.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0441× (z -27.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 66.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.20× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.407× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 97.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 65.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -14.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.2) | — |
| [[CHP-212 (line)]] | wt | 46.0 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0889× (z -10.5) |
| [[HOP62 (line)]] | alt | 83.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 176 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 38.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -18.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +11.8) | — |
| [[H4 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -11.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +9.0) | — |
| [[RKO (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +13.6) | — |
| [[SW48 (line)]] | wt | 81.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A11]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TAF7]] | +0.56 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[MBP]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[SH3D19]] | +0.54 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[NUP50-DT]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZNF562]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CLCF1]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[TSC22D1]] | +0.53 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[TLNRD1]] | +0.53 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ARAP2]] | +0.52 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[CDKN2B]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[AGO2]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[TFG]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[FAM168A]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[NUS1]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CLINT1]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ALDH18A1]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SEC23A]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PRRC1]] | -0.55 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[SEC63]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[DDB1]] | -0.53 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[MARCHF6]] | -0.53 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[NIPSNAP1]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RESF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction -0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.7, -31.3); signed map (13.3, -5.3). **Vector** length 129, 37.4% of its response variance represented; |z| ≥ 3 in 1,408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.8 | +8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.3 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.5 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.4 | +3.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.9 | -8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.3 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -10.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -1.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | retroelement silencing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:31,959,370-31,993,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20696, FLJ10652, UTA2-1, GET; previously C12orf35, KIAA1551 |
| Gene groups (HGNC) | Minor histocompatibility antigens |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCM1](https://www.uniprot.org/uniprotkb/Q9HCM1) (Retroelement silencing factor 1):

> Plays a role in the regulation of imprinted gene expression, regulates repressive epigenetic modifications associated with SETDB1. Required for the recruitment or accumulation of SETDB1 to the endogenous retroviruses (ERVs) and maintenance of repressive chromatin configuration, contributing to a subset of the SETDB1-dependent ERV silencing in embryonic stem cells.

**Summary**, from NCBI Gene [55196](https://www.ncbi.nlm.nih.gov/gene/55196):

> Predicted to enable histone binding activity and histone methyltransferase binding activity. Predicted to be involved in transposable element silencing by heterochromatin formation. Predicted to act upstream of or within response to bacterium. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25559) · Entrez [55196](https://www.ncbi.nlm.nih.gov/gene/55196) · UniProt [Q9HCM1](https://www.uniprot.org/uniprotkb/Q9HCM1) · Ensembl [ENSG00000174718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174718)

## Data

Gene col 10517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10517); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10517]; `tensor/DDL_lfc|DDL_z.npy` [10517]; `embed/gene_vectors.npy` [10517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10517 or target_col == 10517). Every well: [[RESF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RESF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
