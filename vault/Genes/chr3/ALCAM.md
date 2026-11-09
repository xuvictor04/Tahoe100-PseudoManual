---
symbol: "ALCAM"
type: "gene"
col: 9894
ensembl_id: "ENSG00000170017"
name: "activated leukocyte cell adhesion molecule"
location: "3q13.11"
module: 197
arm: "+"
pooled_cpm: 435.03
n_lines_expressing: 41
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# ALCAM

*activated leukocyte cell adhesion molecule* — 3q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.29× (z +43.4, q 0e+00, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.906× (z -8.6, q 4e-15, down in 0 of 41 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.795× (z -5.9, q 5e-07, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLCB4]] (+0.68, fdr 7e-06), [[SEMA3C]] (+0.65, fdr 7e-06), [[NFIB]] (+0.65, fdr 7e-06); moves opposite to [[SLC30A6]] (-0.59, fdr 1e-05), [[GLE1]] (-0.57, fdr 3e-05), [[ZNF549]] (-0.57, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CRYBG1]] → it (grade B ⚠); 5 go from it, the strongest it → [[PTPRK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.29×** | +43.4 | 0e+00 | 35/39 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.24×** | +29.2 | 0e+00 | 35/39 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +20.8 | 0e+00 | 37/40 (SNU-423, H4, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +18.6 | 0e+00 | 34/36 (SNU-423, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +16.6 | 0e+00 | 31/35 (H4, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +13.7 | 1e-40 | 23/39 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.54×** | +11.2 | 4e-27 | 31/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +10.5 | 4e-24 | 29/38 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +10.5 | 4e-24 | 24/39 (SK-MEL-2, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +10.3 | 4e-23 | 28/40 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +10.0 | 1e-21 | 25/39 (SK-MEL-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +8.3 | 7e-15 | 23/40 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +8.0 | 4e-14 | 22/39 (NCI-H460, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.33×** | +7.3 | 1e-11 | 25/39 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +6.3 | 1e-08 | 22/38 (NCI-H1573, SW48, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +5.8 | 3e-07 | 20/39 (NCI-H1573, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +5.6 | 8e-07 | 22/40 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.4 | 2e-06 | 19/41 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +4.4 | 3e-04 | 18/38 (SW48, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +4.3 | 4e-04 | 17/39 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +4.2 | 7e-04 | 16/40 (A-427, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.001 | 17/39 (hTERT-HPNE, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -8.6 | 4e-15 | 0/41 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.839× | -6.5 | 3e-08 | 18/39 (A-172, H4, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -5.9 | 5e-07 | 22/39 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -5.6 | 4e-06 | 21/39 (COLO 205, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.819×** | -5.2 | 2e-05 | 19/39 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.810×** | -5.2 | 2e-05 | 19/39 (A549, COLO 205, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.833× | -4.7 | 2e-04 | 20/39 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.855× | -4.1 | 0.003 | 17/39 (PANC-1, COLO 205, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.872× | -3.6 | 0.023 | 13/39 (LS 180, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.883× | -3.2 | 0.068 | 15/39 (H4, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.2 | 0.076 | 17/39 (LS 180, HEC-1-A, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 259 | 27 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +30.5) | [[Selinexor (drug)]] 5 µM 0.565× (z -9.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 242 | 15 (7 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +24.3) | [[Selinexor (drug)]] 5 µM 0.440× (z -12.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H460 (line)]] | wt | 161 | 16 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +29.8) | — |
| [[J82 (line)]] | alt | 300 | 13 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +41.8) | [[Selinexor (drug)]] 5 µM 0.603× (z -11.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HEC-1-A (line)]] | alt | 1,465 | 7 (4 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +24.3) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -16.4) |
| [[SNU-423 (line)]] | alt | 378 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +35.2) | — |
| [[PANC-1 (line)]] | alt | 196 | 10 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +38.7) | [[Ixazomib citrate (drug)]] 5 µM 0.505× (z -10.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SK-MEL-2 (line)]] | alt | 421 | 11 (5 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.72× (z +19.1) | — |
| [[HS-578T (line)]] | alt | 912 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +33.1) | — |
| [[SW 900 (line)]] | alt | 345 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +23.6) | — |
| [[A498 (line)]] | wt | 620 | 7 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +33.1) | [[Panobinostat (drug)]] 0.5 µM 0.583× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 626 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +29.8) | — |
| [[A-172 (line)]] | wt | 427 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +26.9) | [[Selinexor (drug)]] 5 µM 0.533× (z -12.9) ⚠ cell-cycle shift, explains ~83% of this change |
| [[H4 (line)]] | wt | 507 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +19.1) | [[Selinexor (drug)]] 5 µM 0.487× (z -12.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H1792 (line)]] | alt | 421 | 7 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.91× (z +18.1) | — |
| [[Panc 03.27 (line)]] | alt | 392 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +38.2) | — |
| [[SW48 (line)]] | wt | 315 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +20.6) | — |
| [[A-427 (line)]] | wt | 163 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +23.2) | — |
| [[LoVo (line)]] | wt | 544 | 2 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.65× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -10.3) |
| [[RKO (line)]] | wt | 514 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.331× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~78% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 334 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +21.7) | — |
| [[A549 (line)]] | wt | 606 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 215 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 1,171 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 370 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.445× (z -10.2) |
| [[SW1417 (line)]] | alt | 167 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +20.2) | — |
| [[AsPC-1 (line)]] | alt | 141 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.8) | — |
| [[Hs 766T (line)]] | wt | 672 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -13.0) |
| [[LS 180 (line)]] | wt | 1000 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -18.9) |
| [[NCI-H2347 (line)]] | alt | 1,205 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 506 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.7) | [[Auranofin (drug)]] 5 µM 0.557× (z -9.6) |
| [[SW 1088 (line)]] | alt | 294 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +14.9) | [[Temsirolimus (drug)]] 0.5 µM 0.139× (z -9.9) |
| [[KATO III (line)]] | alt | 340 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 953 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 530 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +18.9) | — |
| [[CHP-212 (line)]] | wt | 165 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 264 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +10.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 37.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 69.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 36.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 108 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 73.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 41.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 54.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCB4]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[SEMA3C]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 | STRING 471 |
| [[NFIB]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PTPRK]] | +0.64 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[PLCE1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ITGAV]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 539 |
| [[MBNL1]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CDH2]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | same gene group; STRING 448 |
| [[THBS1]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SYNE2]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[GLE1]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[ZNF549]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MPG]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[LSM11]] | -0.57 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[IL17RA]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 | same gene group |
| [[SCNM1]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SS18L1]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[C8orf76]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[FLYWCH1]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZNF333]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[XYLT2]] | -0.53 | -0.42 / -0.66 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG1]] | B | CRYBG1 activity raises ALCAM's level | lines that do not express CRYBG1 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without CRYBG1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[PTPRK]] | B | PTPRK activity raises ALCAM's level | lines that do not express PTPRK (6) vs lines expressing it (44) | 3.62× lower at baseline in the lines without PTPRK | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000246225, EPS8, ASPH |
| [[PSMB5]] | B | PSMB5 activity raises ALCAM's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPTLC3]] | B | SPTLC3 activity raises ALCAM's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without SPTLC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[PLCB4]] | B | PLCB4 activity raises ALCAM's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without PLCB4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[ARHGAP42]] | B | ARHGAP42 activity raises ALCAM's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without ARHGAP42 | 0.090 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[PALLD]] | B | PALLD activity raises ALCAM's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.60× lower at baseline in the lines without PALLD | 0.098 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[DIO2]] | B | DIO2 activity raises ALCAM's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without DIO2 | 0.0995 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRK]] | B | ALCAM activity raises PTPRK's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without ALCAM | 0.058 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |
| [[ARHGAP42]] | B | ALCAM activity raises ARHGAP42's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 2.80× lower at baseline in the lines without ALCAM | 0.064 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |
| [[LPP]] | B | ALCAM activity raises LPP's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without ALCAM | 0.078 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |
| [[ENAH]] | B | ALCAM activity lowers ENAH's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 1.65× higher at baseline in the lines without ALCAM | 0.081 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |
| [[ATF6]] | B | ALCAM activity lowers ATF6's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 1.25× higher at baseline in the lines without ALCAM | 0.083 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 15.2); signed map (47.1, 18.5). **Vector** length 132, 39.3% of its response variance represented; |z| ≥ 3 in 1,534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +29.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +43.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.0 | +11.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.1 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.5 | +5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.5 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | -6.8 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -5.3 | -6.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.1 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | activated leukocyte cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.11 — chr3:105,366,909-105,576,900 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD166, MEMD |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C2-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, IL2_STAT5_SIGNALING |
| Reactome | 3 pathways, smallest: L1CAM interactions; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13740](https://www.uniprot.org/uniprotkb/Q13740) (CD166 antigen):

> Cell adhesion molecule that mediates both heterotypic cell-cell contacts via its interaction with CD6, as well as homotypic cell-cell contacts. Promotes T-cell activation and proliferation via its interactions with CD6. Contributes to the formation and maturation of the immunological synapse via its interactions with CD6. Mediates homotypic interactions with cells that express ALCAM. Acts as a ligand for the LILRB4 receptor, enhancing LILRB4-mediated inhibition of T cell proliferation. Required …

**Summary**, from NCBI Gene [214](https://www.ncbi.nlm.nih.gov/gene/214):

> This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple alternatively spliced transcript variants encoding different isoforms have been found. [provided by …

**Accessions** — [HGNC:400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:400) · Entrez [214](https://www.ncbi.nlm.nih.gov/gene/214) · UniProt [Q13740](https://www.uniprot.org/uniprotkb/Q13740) · Ensembl [ENSG00000170017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170017)

## Data

Gene col 9894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9894); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9894]; `tensor/DDL_lfc|DDL_z.npy` [9894]; `embed/gene_vectors.npy` [9894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9894 or target_col == 9894). Every well: [[ALCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
