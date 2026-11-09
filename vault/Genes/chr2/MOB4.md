---
symbol: "MOB4"
type: "gene"
col: 3692
ensembl_id: "ENSG00000115540"
name: "MOB family member 4, phocein"
location: "2q33.1"
module: 7
arm: "+"
pooled_cpm: 60.17
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MOB4

*MOB family member 4, phocein* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.61× (z +22.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.693× (z -8.4, q 2e-14, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.491×, HOP62 0.471×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.316×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZKSCAN4]] (+0.68, fdr 7e-06), [[HIKESHI]] (+0.67, fdr 1e-05), [[PSMC2]] (+0.66, fdr 1e-05); moves opposite to [[AHCY]] (-0.56, fdr 2e-05), [[RELL1]] (-0.56, fdr 3e-05), [[NPHP4]] (-0.56, fdr 6e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.61×** | +22.0 | 0e+00 | 45/48 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.46×** | +12.3 | 4e-32 | 34/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +12.0 | 9e-31 | 38/47 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +11.4 | 7e-28 | 39/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +11.1 | 9e-27 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.51×** | +11.1 | 2e-26 | 47/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +10.1 | 4e-22 | 33/48 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +9.0 | 2e-17 | 38/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +8.8 | 1e-16 | 40/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +8.1 | 3e-14 | 31/48 (LS 180, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +8.0 | 6e-14 | 35/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +7.6 | 2e-12 | 32/48 (LS 180, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +7.1 | 7e-11 | 29/48 (NCI-H1573, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +7.0 | 1e-10 | 38/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.9 | 3e-10 | 32/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +6.0 | 6e-08 | 30/49 (A498, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.3 | 4e-06 | 28/47 (A549, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.014 | 19/48 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.014 | 13/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3692.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.491×, HOP62 0.471×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.316×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.693×** | -8.4 | 2e-14 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.718×** | -7.6 | 7e-12 | 35/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.0 | 0.011 | 18/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.0 | 0.011 | 21/48 (SW480, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.869× | -3.1 | 0.21 | 17/41 (NCI-H1573, NCI-H2030, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 55.8 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.06× (z +15.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 52.5 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.05× (z +13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.46× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 48.8 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.39× (z +16.6) | — |
| [[SHP-77 (line)]] | alt | 69.5 | 6 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 19.5× (z +23.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.62× (z +10.7) | — |
| [[LoVo (line)]] | wt | 48.1 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 49.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +12.9) | — |
| [[SW480 (line)]] | alt | 59.5 | 4 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 3.13× (z +17.2) | [[Panobinostat (drug)]] 0.5 µM 0.491× (z -10.6) |
| [[A498 (line)]] | wt | 87.0 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 62.2 | 2 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.65× (z +10.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.316× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 96.9 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.88× (z +12.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 2.74× (z +12.1) | — |
| [[A-172 (line)]] | wt | 71.2 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.75× (z +19.9) | — |
| [[A549 (line)]] | wt | 58.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 42.6 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 23.7× (z +23.9) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 52.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.81× (z +11.4) | — |
| [[C32 (line)]] | wt | 50.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.29× (z +14.8) | — |
| [[HepG2_C3A (line)]] | wt | 70.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 53.7 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.70× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.6) |
| [[KATO III (line)]] | alt | 54.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 55.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 59.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.69× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 55.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.16× (z +12.1) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0961× (z -10.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.74× (z +14.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.81× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 56.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +14.5) | — |
| [[CFPAC-1 (line)]] | alt | 63.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[H4 (line)]] | wt | 59.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 51.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.33× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 57.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +11.1) | — |
| [[RKO (line)]] | wt | 48.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 59.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 38.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.50× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 80.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.18× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 50.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.67× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN4]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HIKESHI]] | +0.67 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[C3orf38]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LEPROTL1]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[YAE1]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[EHHADH]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CCNT2]] | +0.60 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[THBS4]] | +0.59 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[COPS5]] | +0.59 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ZNF227]] | +0.59 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[NFU1]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCY]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[RELL1]] | -0.56 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[NPHP4]] | -0.56 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[ODF2]] | -0.55 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GRK6]] | -0.54 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[SMG1P3]] | -0.52 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[USP2-AS1]] | -0.52 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[PACS2]] | -0.50 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-16.0, 8.8); signed map (14.1, -24.4). **Vector** length 85.4, 20.2% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +22.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.4 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +11.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +6.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | -1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.0 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.7 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -8.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | MOB family member 4, phocein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,515,571-197,553,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOB3, DKFZP564M112, CGI-95, 2C4D, PHOCN; previously PREI3, MOBKL3 |
| Gene groups (HGNC) | MOB kinase activators; STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3A3](https://www.uniprot.org/uniprotkb/Q9Y3A3) (MOB-like protein phocein):

> Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, differentiation, apoptosis, metabolism and immune regulation.

**Summary**, from NCBI Gene [25843](https://www.ncbi.nlm.nih.gov/gene/25843):

> This gene was identified based on its similarity with the mouse counterpart. Studies of the mouse counterpart suggest that the expression of this gene may be regulated during oocyte maturation and preimplantation following zygotic gene activation. Alternatively spliced transcript variants encoding distinct isoforms have been observed. Naturally occurring read-through transcription occurs between this locus and the neighboring locus HSPE1.[provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:17261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17261) · Entrez [25843](https://www.ncbi.nlm.nih.gov/gene/25843) · UniProt [Q9Y3A3](https://www.uniprot.org/uniprotkb/Q9Y3A3) · Ensembl [ENSG00000115540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115540)

## Data

Gene col 3692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3692); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3692]; `tensor/DDL_lfc|DDL_z.npy` [3692]; `embed/gene_vectors.npy` [3692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3692 or target_col == 3692). Every well: [[MOB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
