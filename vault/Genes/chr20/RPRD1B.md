---
symbol: "RPRD1B"
type: "gene"
col: 2133
ensembl_id: "ENSG00000101413"
name: "regulation of nuclear pre-mRNA domain containing 1B"
location: "20q11.23"
module: 46
arm: "+"
pooled_cpm: 118.91
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# RPRD1B

*regulation of nuclear pre-mRNA domain containing 1B* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.80× (z +16.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.554× (z -10.6, q 1e-23, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAF1]] (+0.66, fdr 1e-05), [[LUC7L2]] (+0.66, fdr 1e-05), [[VPS52]] (+0.62, fdr 1e-04); moves opposite to [[NGLY1]] (-0.60, fdr 1e-04), [[CBL]] (-0.60, fdr 1e-04), [[CCDC112]] (-0.59, fdr 7e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.80×** | +16.5 | 0e+00 | 48/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.10×** | +13.2 | 2e-37 | 47/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +10.9 | 2e-25 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +10.0 | 1e-21 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.5 | 1e-15 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +8.2 | 2e-14 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +7.4 | 1e-11 | 30/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 5e-07 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 2e-04 | 28/47 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 4e-04 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.012 | 24/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.018 | 20/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.022 | 26/49 (C-33 A, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.023 | 21/37 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.19× | +3.1 | 0.079 | 20/48 (CFPAC-1, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -10.6 | 1e-23 | 48/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -10.3 | 2e-22 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.515×** | -10.1 | 8e-22 | 41/49 (SW1417, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -9.7 | 6e-20 | 37/44 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -8.8 | 1e-16 | 48/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.730×** | -8.0 | 1e-13 | 42/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -7.4 | 8e-12 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.697×** | -6.5 | 6e-09 | 41/49 (CHP-212, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.788×** | -4.3 | 0.001 | 30/48 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.808×** | -3.8 | 0.007 | 26/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.025 | 26/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.694×** | -3.4 | 0.028 | 26/49 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.2 | 0.058 | 20/48 (KATO III, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.820× | -3.0 | 0.10 | 22/48 (KATO III, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 143 | 6 (1 ⚠) | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.39× (z +15.0) | [[Belinostat (drug)]] 5 µM 0.508× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 144 | 10 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 106 | 5 | 4 | [[TAK-901 (drug)]] 5 µM 4.54× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.474× (z -10.9) |
| [[LoVo (line)]] | wt | 85.6 | 7 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -9.2) |
| [[PANC-1 (line)]] | alt | 86.2 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -15.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 230 | 4 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.01× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 179 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 122 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 86.7 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 197 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.492× (z -9.4) |
| [[KATO III (line)]] | alt | 184 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.409× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 168 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.92× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 70.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +22.3) | — |
| [[A498 (line)]] | wt | 92.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 78.8 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.57× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 154 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.28× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 80.8 | 3 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.54× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 117 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 113 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.66× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -9.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 92.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 102 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 160 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.57× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 162 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.75× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 72.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 197 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.17× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 110 | 1 | 1 | [[Oxaprozin (drug)]] 5 µM 2.31× (z +10.4) | [[Everolimus (drug)]] 5 µM 0.219× (z -10.2) |
| [[RKO (line)]] | wt | 136 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.1× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 150 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 90.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.15× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 151 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.69× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.31× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 85.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.29× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 84.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0416× (z -18.1) |
| [[COLO 205 (line)]] | alt | 123 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.24× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 69.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAF1]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[LUC7L2]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[VPS52]] | +0.62 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[PRCC]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[QTRT1]] | +0.59 | +0.25 / +0.51 | both halves | 4e-04 |  |
| [[WBP11]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | +0.59 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[ZFX]] | +0.58 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[RPRD2]] | +0.57 | +0.38 / +0.48 | both halves | 7e-05 | same gene group; pathway: RNA polymerase II transcribes snRNA genes; STRING 939 |
| [[ZNF362]] | +0.57 | +0.29 / +0.42 | both halves | 2e-04 |  |
| [[FIZ1]] | +0.57 | +0.20 / +0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NNT]] | +0.57 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.56 | +0.28 / +0.38 | both halves | 3e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGLY1]] | -0.60 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CBL]] | -0.60 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.59 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[UBA6]] | -0.59 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[SPAG9]] | -0.56 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[DLGAP4]] | -0.56 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CSGALNACT2]] | -0.55 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[SH3BGRL3]] | -0.55 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[CCNYL1]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CIB1]] | -0.54 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[NDRG1]] | -0.54 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[GDPD5]] | -0.53 | -0.36 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RPRD1B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RPRD1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.7, 4.8); signed map (29.3, -25.7). **Vector** length 87.0, 26.9% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +16.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.1 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.5 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.0 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.4 | -6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.7 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -8.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | regulation of nuclear pre-mRNA domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:38,033,725-38,127,780 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1057B20.2, DKFZp434P0735, CREPT, FLJ44520, NET60, Kub5-Hera, K-H; previously C20orf77 |
| Gene groups (HGNC) | CTD interacting domain containing; Regulation of nuclear pre-mRNA domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQG5](https://www.uniprot.org/uniprotkb/Q9NQG5) (Regulation of nuclear pre-mRNA domain-containing protein 1B):

> Interacts with phosphorylated C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit POLR2A, and participates in dephosphorylation of the CTD by RPAP2. Transcriptional regulator which enhances expression of CCND1. Promotes binding of RNA polymerase II to the CCDN1 promoter and to the termination region before the poly-A site but decreases its binding after the poly-A site. Prevents RNA polymerase II from reading through the 3' end termination site and may allow it …

**Summary**, from NCBI Gene [58490](https://www.ncbi.nlm.nih.gov/gene/58490):

> Enables RNA polymerase II complex binding activity and identical protein binding activity. Involved in several processes, including RNA polymerase II promoter clearance; positive regulation of cell population proliferation; and positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of transcription preinitiation complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16209) · Entrez [58490](https://www.ncbi.nlm.nih.gov/gene/58490) · UniProt [Q9NQG5](https://www.uniprot.org/uniprotkb/Q9NQG5) · Ensembl [ENSG00000101413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101413)

## Data

Gene col 2133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2133); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2133]; `tensor/DDL_lfc|DDL_z.npy` [2133]; `embed/gene_vectors.npy` [2133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2133 or target_col == 2133). Every well: [[RPRD1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPRD1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
