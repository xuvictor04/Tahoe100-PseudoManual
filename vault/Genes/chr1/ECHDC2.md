---
symbol: "ECHDC2"
type: "gene"
col: 4266
ensembl_id: "ENSG00000121310"
name: "enoyl-CoA hydratase domain containing 2"
location: "1p32.3"
module: 46
arm: "+"
pooled_cpm: 33.86
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 36
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ECHDC2

*enoyl-CoA hydratase domain containing 2* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +7.2, q 3e-10, up in 21 of 36 measured lines) ⚠ cell-cycle shift, explains ~72% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.32× (z +4.9, q 3e-04, up in 22 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.361× (z -25.2, q 0e+00, down in 34 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.263× (z -23.4, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGAP3]] (+0.55, fdr 5e-05), [[ACCS]] (+0.55, fdr 4e-05), [[PIGB]] (+0.55, fdr 1e-05); moves opposite to [[RAP2A]] (-0.50, fdr 1e-04), [[SCART1]] (-0.48, fdr 2e-04), [[IL1RAP]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SGK2]] → it (grade B ⚠); 5 go from it, the strongest it → [[BMS1P1-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.34×** | +7.2 | 3e-10 | 21/36 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.9 | 3e-04 | 22/36 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.007 | 15/35 (LS 180, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.013 | 14/36 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.036 | 13/37 (HT-29, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.24×** | +3.6 | 0.036 | 8/36 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.044 | 9/36 (LS 180, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.063 | 15/36 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.063 | 14/35 (A498, HOP62, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.074 | 6/36 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.23×** | +3.2 | 0.075 | 16/36 (LS 180, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.11 | 7/34 (A498, LoVo, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.11 | 5/36 (NCI-H1792, H4, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.361×** | -25.2 | 0e+00 | 34/36 (NCI-H1573, NCI-H23, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.263×** | -23.4 | 0e+00 | 36/36 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.269×** | -23.0 | 0e+00 | 35/36 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.287×** | -21.9 | 0e+00 | 35/36 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.303×** | -20.9 | 0e+00 | 34/36 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.337×** | -19.0 | 0e+00 | 33/34 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.386×** | -16.7 | 0e+00 | 31/36 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.399×** | -16.1 | 0e+00 | 33/36 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.409×** | -15.6 | 0e+00 | 34/36 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.419×** | -15.2 | 0e+00 | 33/35 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.463×** | -13.5 | 9e-40 | 34/36 (SNU-423, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.473×** | -12.6 | 1e-34 | 30/36 (NCI-H1792, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.486×** | -12.2 | 2e-32 | 31/33 (PANC-1, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.323×** | -10.4 | 1e-23 | 32/37 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.344×** | -9.8 | 5e-21 | 33/35 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -8.6 | 4e-16 | 29/36 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.412×** | -8.1 | 1e-14 | 30/36 (HEC-1-A, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.487×** | -6.6 | 1e-09 | 25/35 (NCI-H23, J82, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.5 | 2e-04 | 17/36 (PANC-1, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.7 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -24.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -19.0) |
| [[COLO 205 (line)]] | alt | 84.7 | 0 | 12 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.109× (z -21.8) |
| [[J82 (line)]] | alt | 54.3 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -21.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.138× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 46.3 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -19.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.145× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 59.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -26.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -25.2) |
| [[NCI-H23 (line)]] | alt | 82.5 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -25.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.165× (z -19.7) |
| [[SNU-423 (line)]] | alt | 38.7 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -24.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -16.3) |
| [[HS-578T (line)]] | alt | 43.1 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -20.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.233× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 57.4 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -19.0) |
| [[LS 180 (line)]] | wt | 86.4 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -18.9) |
| [[SW 900 (line)]] | alt | 39.6 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.128× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 33.5 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 55.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.160× (z -14.4) |
| [[A549 (line)]] | wt | 22.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 53.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.264× (z -14.2) |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -13.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -11.5) |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -16.5) |
| [[SW48 (line)]] | wt | 65.4 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -15.9) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -14.2) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -12.9) |
| [[A498 (line)]] | wt | 26.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.330× (z -9.6) |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.208× (z -11.0) |
| [[A-427 (line)]] | wt | 44.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 48.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.289× (z -11.6) |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -12.1) |
| [[H4 (line)]] | wt | 21.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -10.1) |
| [[RKO (line)]] | wt | 37.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 42.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0936× (z -15.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0927× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.2) |
| [[A-172 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAP3]] | +0.55 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[ACCS]] | +0.55 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[PIGB]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MTX3]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[MED24]] | +0.53 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[HSBP1L1]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ABCC6]] | +0.52 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[BMS1P1-1]] | +0.51 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[EFCAB7]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[IDNK]] | +0.50 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[SUPT7L]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[RMDN2]] | +0.50 | +0.31 / +0.39 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP2A]] | -0.50 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[SCART1]] | -0.48 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[IL1RAP]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[ENO1]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[ARHGEF10]] | -0.45 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[SLC2A13]] | -0.45 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[PKM]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[HS3ST3A1]] | -0.44 | -0.46 / -0.23 | both halves | 5e-04 |  |
| [[DOT1L]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[SLC6A6]] | -0.43 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[SNX25]] | -0.43 | -0.36 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGK2]] | B | SGK2 activity raises ECHDC2's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 3.58× lower at baseline in the lines without SGK2 | 0.082 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMS1P1-1]] | B | ECHDC2 activity raises BMS1P1-1's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without ECHDC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[RBM39]] | B | ECHDC2 activity raises RBM39's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without ECHDC2 | 0.015 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[AGAP13P]] | B | ECHDC2 activity raises AGAP13P's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without ECHDC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[RAP2A]] | B | ECHDC2 activity lowers RAP2A's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.29× higher at baseline in the lines without ECHDC2 | 0.047 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| cells under [[Tranilast (drug)]] 0.5 µM | B | ECHDC2 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express ECHDC2 (12) vs lines expressing it (36) | the lines without ECHDC2: 0.85× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-14.1, 8.3); signed map (35.8, -14.2). **Vector** length 78.0, 19.7% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +5.8 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | -2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -15.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -13.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -23.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -16.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -15.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -9.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA hydratase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,895,910-52,927,212 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10948 |
| Matched by | ensembl_id |

UniProt [Q86YB7](https://www.uniprot.org/uniprotkb/Q86YB7) carries no function annotation.

**Summary**, from NCBI Gene [55268](https://www.ncbi.nlm.nih.gov/gene/55268):

> Predicted to enable enoyl-CoA hydratase activity. Predicted to be involved in fatty acid beta-oxidation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23408) · Entrez [55268](https://www.ncbi.nlm.nih.gov/gene/55268) · UniProt [Q86YB7](https://www.uniprot.org/uniprotkb/Q86YB7) · Ensembl [ENSG00000121310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121310)

## Data

Gene col 4266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4266); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4266]; `tensor/DDL_lfc|DDL_z.npy` [4266]; `embed/gene_vectors.npy` [4266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4266 or target_col == 4266). Every well: [[ECHDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECHDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
