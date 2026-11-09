---
symbol: "SMAD2"
type: "gene"
col: 10604
ensembl_id: "ENSG00000175387"
name: "SMAD family member 2"
location: "18q21.1"
module: 41
arm: "-"
pooled_cpm: 196.19
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SMAD2

*SMAD family member 2* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.23× (z +4.9, q 6e-04, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 1.60×, A-172 1.65×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.593× (z -12.5, q 5e-33, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA1]] (+0.56, fdr 3e-05), [[NME4]] (+0.54, fdr 4e-05), [[TBL1XR1]] (+0.54, fdr 1e-05); moves opposite to [[SLC4A1AP]] (-0.57, fdr 1e-05), [[KRBOX4]] (-0.55, fdr 4e-05), [[SDE2]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 1.60×, A-172 1.65×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.9 | 6e-04 | 24/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.8 | 6e-04 | 25/47 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.044 | 22/48 (HOP62, H4, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.17× | +3.6 | 0.046 | 18/47 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.091 | 19/48 (PANC-1, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.593×** | -12.5 | 5e-33 | 43/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -11.7 | 5e-29 | 38/49 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.617×** | -11.6 | 1e-28 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -10.9 | 1e-25 | 32/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.637×** | -10.8 | 5e-25 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.656×** | -10.1 | 5e-22 | 46/48 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -9.3 | 9e-19 | 39/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.678×** | -8.6 | 6e-16 | 35/45 (NCI-H460, C-33 A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.729×** | -7.3 | 2e-11 | 43/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.757×** | -6.4 | 9e-09 | 33/50 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.767×** | -6.3 | 1e-08 | 28/49 (NCI-H460, H4, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.779×** | -6.0 | 1e-07 | 36/48 (A-172, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.801×** | -5.3 | 5e-06 | 28/48 (NCI-H1573, SW48, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.806×** | -5.2 | 1e-05 | 28/48 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.809×** | -5.1 | 1e-05 | 26/48 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.816×** | -4.6 | 1e-04 | 25/48 (SW1417, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -4.6 | 1e-04 | 24/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.737×** | -3.8 | 0.003 | 23/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.904× | -3.4 | 0.013 | 13/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.870× | -3.3 | 0.018 | 14/48 (NCI-H2347, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 548 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 224 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -15.1) |
| [[A549 (line)]] | wt | 251 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -19.4) |
| [[NCI-H1573 (line)]] | alt | 270 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -15.8) |
| [[SW1417 (line)]] | alt | 272 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.4) |
| [[SW48 (line)]] | wt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -11.9) |
| [[C-33 A (line)]] | alt | 334 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 205 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.492× (z -12.1) |
| [[HOP62 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.401× (z -13.2) |
| [[HS-578T (line)]] | alt | 184 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -11.0) |
| [[HT-29 (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.451× (z -10.9) |
| [[LS 180 (line)]] | wt | 287 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 370 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.1) |
| [[PANC-1 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.580× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.614× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 208 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.368× (z -14.3) |
| [[A-172 (line)]] | wt | 128 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.509× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 84.1 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.431× (z -11.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 229 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 181 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.658× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 171 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -20.6) |
| [[NCI-H23 (line)]] | alt | 212 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.557× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 173 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -9.4) |
| [[SHP-77 (line)]] | alt | 188 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.6) |
| [[SNU-423 (line)]] | alt | 209 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.3) |
| [[SW480 (line)]] | alt | 112 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.487× (z -12.8) |
| [[A498 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 78.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -10.5) |
| [[H4 (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -15.9) |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0413× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.447× (z -9.9) |
| [[SW 900 (line)]] | alt | 85.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.434× (z -9.4) |
| [[A-427 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA1]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[NME4]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[TBL1XR1]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CHN1]] | +0.53 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[PON2]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PUM2]] | +0.50 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CD99L2]] | +0.50 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[STT3B]] | +0.49 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[XPR1]] | +0.49 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[ARL2]] | +0.49 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[LRRC28]] | +0.49 | +0.43 / +0.29 | both halves | 2e-04 |  |
| [[THAP12]] | +0.48 | +0.38 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | -0.57 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SDE2]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[BAG3]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZRSR2]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[JMJD6]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[FCF1]] | -0.52 | -0.62 / -0.43 | both halves | 4e-05 |  |
| [[BRF2]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TXNL4B]] | -0.52 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[KIN]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[YIPF5]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TTF1]] | -0.50 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.478). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.7, -17.7); signed map (12.3, -51.3). **Vector** length 92.0, 26.2% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +6.1 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +5.6 | -8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.4 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | -0.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.2 | -4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:47,808,957-47,931,146 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MADR2, JV18-1; previously MADH2 |
| Gene groups (HGNC) | SMAD family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 28 pathways, smallest: Loss of Function of SMAD4 in Cancer; SMAD2/3 MH2 Domain Mutants in Cancer; SMAD4 MH2 Domain Mutants in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15796](https://www.uniprot.org/uniprotkb/Q15796) (SMAD family member 2):

> Receptor-regulated SMAD (R-SMAD) that is an intracellular signal transducer and transcriptional modulator activated by TGF-beta (transforming growth factor) and activin type 1 receptor kinases. Binds the TRE element in the promoter region of many genes that are regulated by TGF-beta and, on formation of the SMAD2/SMAD4 complex, activates transcription. Promotes TGFB1-mediated transcription of odontoblastic differentiation genes in dental papilla cells (By similarity). Positively regulates PDPK1 …

**Summary**, from NCBI Gene [4087](https://www.ncbi.nlm.nih.gov/gene/4087):

> The protein encoded by this gene belongs to the SMAD, a family of proteins similar to the gene products of the Drosophila gene 'mothers against decapentaplegic' (Mad) and the C. elegans gene Sma. SMAD proteins are signal transducers and transcriptional modulators that mediate multiple signaling pathways. This protein mediates the signal of the transforming growth factor (TGF)-beta, and thus regulates multiple cellular processes, such as cell proliferation, apoptosis, and differentiation. This …

**Accessions** — [HGNC:6768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6768) · Entrez [4087](https://www.ncbi.nlm.nih.gov/gene/4087) · UniProt [Q15796](https://www.uniprot.org/uniprotkb/Q15796) · Ensembl [ENSG00000175387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175387)

## Data

Gene col 10604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10604); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10604]; `tensor/DDL_lfc|DDL_z.npy` [10604]; `embed/gene_vectors.npy` [10604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10604 or target_col == 10604). Every well: [[SMAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
