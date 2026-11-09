---
symbol: "UCK2"
type: "gene"
col: 6692
ensembl_id: "ENSG00000143179"
name: "uridine-cytidine kinase 2"
location: "1q24.1"
module: 18
arm: "+"
pooled_cpm: 63.38
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# UCK2

*uridine-cytidine kinase 2* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 4.05× (z +13.4, q 3e-38, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.463× (z -14.2, q 8e-43, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPARGC1B]] (+0.76, fdr 7e-06), [[ADCY3]] (+0.75, fdr 7e-06), [[TMTC4]] (+0.75, fdr 7e-06); moves opposite to [[TOX4]] (-0.67, fdr 7e-06), [[GOLGB1]] (-0.63, fdr 7e-06), [[SENP2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **4.05×** | +13.4 | 3e-38 | 42/47 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +12.2 | 1e-31 | 41/47 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +8.9 | 9e-17 | 37/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +8.6 | 1e-15 | 31/47 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +8.2 | 2e-14 | 35/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.1 | 6e-14 | 30/47 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +7.6 | 2e-12 | 27/36 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.1 | 7e-08 | 26/47 (SK-MEL-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.0 | 9e-08 | 23/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +6.0 | 1e-07 | 24/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.4 | 4e-06 | 25/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 4e-06 | 26/47 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 1e-05 | 25/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +5.0 | 2e-05 | 25/48 (SHP-77, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 4e-05 | 25/47 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 19/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.001 | 24/47 (HS-578T, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.001 | 19/47 (NCI-H460, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.002 | 21/47 (NCI-H460, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.463×** | -14.2 | 8e-43 | 34/47 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.596×** | -13.5 | 6e-39 | 34/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -9.2 | 9e-18 | 25/47 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -8.0 | 2e-13 | 30/47 (RKO, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.682×** | -7.0 | 2e-10 | 26/47 (C-33 A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.722×** | -6.0 | 2e-07 | 24/47 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.739×** | -5.6 | 2e-06 | 25/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.755×** | -5.0 | 4e-05 | 23/47 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.789×** | -4.4 | 8e-04 | 19/47 (RKO, SW48, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.799×** | -4.0 | 0.004 | 17/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.825×** | -3.8 | 0.007 | 19/49 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.809×** | -3.8 | 0.008 | 20/43 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.5 | 0.019 | 3/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -3.3 | 0.032 | 18/47 (SNU-1, A498, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.835× | -3.3 | 0.032 | 14/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.878× | -3.3 | 0.035 | 9/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.035 | 11/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.045 | 12/47 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.045 | 10/49 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 121 | 1 | 11 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 7.28× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0527× (z -28.6) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.153× (z -26.8) |
| [[MIA PaCa-2 (line)]] | alt | 131 | 1 | 8 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 6.37× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.0) |
| [[PANC-1 (line)]] | alt | 96.6 | 1 | 7 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.53× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -24.7) |
| [[SW48 (line)]] | wt | 115 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 8.07× (z +14.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -16.1) |
| [[SW480 (line)]] | alt | 90.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 127 | 1 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 9.48× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 99.5 | 3 (2 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 3.20× (z +10.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -16.6) |
| [[J82 (line)]] | alt | 97.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -11.4) |
| [[SHP-77 (line)]] | alt | 116 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -14.4) |
| [[A-427 (line)]] | wt | 95.1 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.540× (z -9.1) |
| [[A498 (line)]] | wt | 59.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.6) |
| [[C-33 A (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0344× (z -30.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.495× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 76.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.3) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0749× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.230× (z -16.7) |
| [[A549 (line)]] | wt | 62.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -11.3) |
| [[BT-474 (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.3) |
| [[C32 (line)]] | wt | 26.4 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 23.1× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 53.9 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 3.26× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 64.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 33.4 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 12.2× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 78.6 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 6.61× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.9) |
| [[SW1417 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -8.6) |
| [[A-172 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.87× (z +8.9) ⚠ toxic | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 32.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 93.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.3) |
| [[HOP62 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.43× (z +9.1) ⚠ toxic | — |
| [[KATO III (line)]] | alt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.0) |
| [[LoVo (line)]] | wt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.24× (z +9.9) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.27× (z +9.9) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.71× (z +9.4) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPARGC1B]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | same gene group |
| [[ADCY3]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.75 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[DHX33]] | +0.74 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[URB2]] | +0.74 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PALS2]] | +0.73 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.73 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[DKC1]] | +0.72 | +0.78 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT |
| [[GART]] | +0.72 | +0.78 / +0.67 | both halves | 7e-06 | pathway: Metabolism of nucleotides; STRING 473 |
| [[POLR1B]] | +0.71 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.70 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[ABCC4]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | -0.67 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[GOLGB1]] | -0.63 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[SENP2]] | -0.61 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[LYSMD3]] | -0.58 | -0.64 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises UCK2's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without WNK2 | 0.047 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[BTNL9]] | B | BTNL9 activity raises UCK2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without BTNL9 | 0.059 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[PDE3B]] | B | PDE3B activity raises UCK2's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.45× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[ABCA3]] | B | ABCA3 activity raises UCK2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.65× lower at baseline in the lines without ABCA3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.836). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.6, -37.5); signed map (-4.8, -53.8). **Vector** length 146, 50.0% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.1 | +12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | +6.5 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +13.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.9 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.0 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -6.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -5.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | uridine-cytidine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:165,827,614-165,911,618 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously UMPK |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Uridine-cytidine kinase family |
| Hallmark sets | IL2_STAT5_SIGNALING, G2M_CHECKPOINT |
| Reactome | 3 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZX2](https://www.uniprot.org/uniprotkb/Q9BZX2) (Uridine-cytidine kinase 2):

> Phosphorylates uridine and cytidine to uridine monophosphate and cytidine monophosphate. Does not phosphorylate deoxyribonucleosides or purine ribonucleosides. Can use ATP or GTP as a phosphate donor. Can also phosphorylate cytidine and uridine nucleoside analogs such as 6-azauridine, 5-fluorouridine, 4-thiouridine, 5-bromouridine, N(4)-acetylcytidine, N(4)-benzoylcytidine, 5-fluorocytidine, 2-thiocytidine, 5-methylcytidine, and N(4)-anisoylcytidine.

**Summary**, from NCBI Gene [7371](https://www.ncbi.nlm.nih.gov/gene/7371):

> This gene encodes a pyrimidine ribonucleoside kinase. The encoded protein (EC 2.7.1.48) catalyzes phosphorylation of uridine and cytidine to uridine monophosphate (UMP) and cytidine monophosphate (CMP), respectively.[provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:12562](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12562) · Entrez [7371](https://www.ncbi.nlm.nih.gov/gene/7371) · UniProt [Q9BZX2](https://www.uniprot.org/uniprotkb/Q9BZX2) · Ensembl [ENSG00000143179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143179)

## Data

Gene col 6692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6692); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6692]; `tensor/DDL_lfc|DDL_z.npy` [6692]; `embed/gene_vectors.npy` [6692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6692 or target_col == 6692). Every well: [[UCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
