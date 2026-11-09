---
symbol: "LRPPRC"
type: "gene"
col: 6125
ensembl_id: "ENSG00000138095"
name: "leucine rich pentatricopeptide repeat containing"
location: "2p21"
module: 4
arm: "+"
pooled_cpm: 250.81
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 6
n_dd_up_clean: 26
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LRPPRC

*leucine rich pentatricopeptide repeat containing* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +17.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Celecoxib (drug)]] 0.5 µM: 0.725× (z -3.9, q 0.052, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO5]] (+0.74, fdr 7e-06), [[PRKDC]] (+0.74, fdr 7e-06), [[HEATR1]] (+0.73, fdr 7e-06); moves opposite to [[HOTAIRM1]] (-0.68, fdr 7e-06), [[ING2]] (-0.67, fdr 7e-06), [[ACAP1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +17.9 | 0e+00 | 42/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +14.4 | 2e-44 | 48/48 (NCI-H23, HT-29, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.46×** | +13.7 | 2e-40 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.17×** | +13.6 | 4e-40 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +11.8 | 4e-30 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.92×** | +9.9 | 4e-21 | 47/48 (HS-578T, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +9.4 | 4e-19 | 45/47 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +8.6 | 6e-16 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +8.4 | 3e-15 | 44/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.41×** | +8.2 | 2e-14 | 44/48 (HOP62, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +7.9 | 2e-13 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.8 | 2e-13 | 35/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.56×** | +7.5 | 4e-12 | 41/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +7.3 | 1e-11 | 40/48 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +7.2 | 2e-11 | 38/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.69×** | +7.2 | 2e-11 | 43/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +7.0 | 7e-11 | 41/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.5 | 1e-06 | 33/48 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 2e-04 | 40/48 (NCI-H460, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 4e-04 | 27/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 5e-04 | 34/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.16×** | +4.2 | 5e-04 | 38/48 (AsPC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Celecoxib (drug)]] 0.5 µM |  | **0.725×** | -3.9 | 0.052 | 38/49 (RKO, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.741×** | -3.7 | 0.068 | 27/48 (PANC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.068 | 29/48 (KATO III, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.758×** | -3.4 | 0.082 | 29/48 (CHP-212, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.760×** | -3.4 | 0.082 | 30/47 (hTERT-HPNE, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.082 | 29/48 (CHP-212, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.814× | -3.2 | 0.12 | 25/48 (NCI-H2030, HCT15, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.834× | -3.1 | 0.12 | 22/47 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.840× | -3.0 | 0.17 | 22/47 (SNU-423, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 154 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 210 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +18.1) | — |
| [[NCI-H460 (line)]] | wt | 326 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +20.2) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.8) | — |
| [[COLO 205 (line)]] | alt | 120 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 136 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 190 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.5) | — |
| [[LoVo (line)]] | wt | 272 | 8 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.79× (z +12.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 122 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.0) | — |
| [[KATO III (line)]] | alt | 266 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 318 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 186 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.4) | — |
| [[A-172 (line)]] | wt | 123 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +19.0) | — |
| [[LOX-IMVI (line)]] | wt | 221 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.3) | — |
| [[Panc 03.27 (line)]] | alt | 225 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.1) | — |
| [[SW480 (line)]] | alt | 327 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 166 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +15.4) | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +17.9) | — |
| [[H4 (line)]] | wt | 192 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 177 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 194 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.79× (z +10.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 4 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.81× (z +12.7) ⚠ unreliable plate only | — |
| [[SW 900 (line)]] | alt | 195 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.2) | — |
| [[A498 (line)]] | wt | 233 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.45× (z +12.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.0) | — |
| [[A549 (line)]] | wt | 301 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 162 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 247 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 2.44× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 262 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 171 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 204 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 386 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.71× (z +12.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 631 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.90× (z +14.4) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.05× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 246 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 332 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +11.3) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.04× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 235 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.15× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.20× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 312 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.9) | — |
| [[RKO (line)]] | wt | 352 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.1) | — |
| [[C32 (line)]] | wt | 163 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 294 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.10× (z +8.6) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 460 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 343 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 367 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 305 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 278 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 350 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[PAICS]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.71 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[IPO7]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[RPSA]] | +0.68 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[MDN1]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[PUM3]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[CCT2]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[FAM120A]] | +0.65 | +0.45 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOTAIRM1]] | -0.68 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[ING2]] | -0.67 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.67 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.65 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.65 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[COX17]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[TIMM29]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[FRG1]] | -0.61 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.61 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[ZNF707]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[ZFAND2B]] | -0.60 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[PURA]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises LRPPRC's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without DUXAP8 | 0.080 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.5, -31.5); signed map (-19.9, -45.0). **Vector** length 110, 48.8% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.60 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | +8.7 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | +8.4 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.4 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +6.3 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.8 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.4 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | +17.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | +0.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich pentatricopeptide repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:43,886,224-43,996,226 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GP130, LRP130; previously LSFC |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Pentatricopeptide repeat containing; Mitochondrial nucleoid associated proteins; LRPPRC:SLIRP complex subunits |
| Hallmark sets | MITOTIC_SPINDLE, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Mitochondrial mRNA modification; Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P42704](https://www.uniprot.org/uniprotkb/P42704) (Leucine-rich PPR motif-containing protein, mitochondrial):

> May play a role in RNA metabolism in both nuclei and mitochondria. In the nucleus binds to HNRPA1-associated poly(A) mRNAs and is part of nmRNP complexes at late stages of mRNA maturation which are possibly associated with nuclear mRNA export. Positively modulates nuclear export of mRNAs containing the EIF4E sensitivity element (4ESE) by binding simultaneously to both EIF4E and the 4ESE and acting as a platform for assembly for the RNA export complex. Also binds to exportin XPO1/CRM1 to engage …

**Summary**, from NCBI Gene [10128](https://www.ncbi.nlm.nih.gov/gene/10128):

> This gene encodes a leucine-rich protein that has multiple pentatricopeptide repeats (PPR). The precise role of this protein is unknown but studies suggest it may play a role in cytoskeletal organization, vesicular transport, or in transcriptional regulation of both nuclear and mitochondrial genes. The protein localizes primarily to mitochondria and is predicted to have an N-terminal mitochondrial targeting sequence. Mutations in this gene are associated with the French-Canadian type of Leigh …

**Accessions** — [HGNC:15714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15714) · Entrez [10128](https://www.ncbi.nlm.nih.gov/gene/10128) · UniProt [P42704](https://www.uniprot.org/uniprotkb/P42704) · Ensembl [ENSG00000138095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138095)

## Data

Gene col 6125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6125); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6125]; `tensor/DDL_lfc|DDL_z.npy` [6125]; `embed/gene_vectors.npy` [6125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6125 or target_col == 6125). Every well: [[LRPPRC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRPPRC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
