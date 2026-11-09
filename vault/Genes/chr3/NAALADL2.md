---
symbol: "NAALADL2"
type: "gene"
col: 10854
ensembl_id: "ENSG00000177694"
name: "N-acetylated alpha-linked acidic dipeptidase like 2"
location: "3q26.31"
module: 10
arm: "+"
pooled_cpm: 101.33
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 37
n_dd_up_clean: 18
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# NAALADL2

*N-acetylated alpha-linked acidic dipeptidase like 2* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.12× (z +6.9, q 3e-09, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.374× (z -13.2, q 3e-37, down in 31 of 37 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.297× (z -11.6, q 7e-29, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP418-AS1]] (+0.61, fdr 2e-05), [[STPG2]] (+0.61, fdr 5e-05), [[ZRANB2-DT]] (+0.59, fdr 3e-05); moves opposite to [[HDAC11]] (-0.62, fdr 1e-05), [[SLC8B1]] (-0.57, fdr 1e-04), [[DOCK6]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GRHL2]] → it (grade B ⚠); 9 go from it, the strongest it → [[MIR583HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.12×** | +6.9 | 3e-09 | 32/36 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.74×** | +5.1 | 8e-05 | 28/37 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +5.1 | 8e-05 | 29/37 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 8e-05 | 26/37 (KATO III, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.64×** | +4.8 | 2e-04 | 27/39 (KATO III, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.59×** | +4.5 | 7e-04 | 25/38 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.84×** | +4.4 | 1e-03 | 28/36 (LoVo, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 0.001 | 27/37 (KATO III, HEC-1-A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 0.001 | 25/37 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.58×** | +4.0 | 0.003 | 23/37 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.003 | 22/37 (HEC-1-A, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.003 | 26/38 (CFPAC-1, SW48, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.004 | 20/37 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.015 | 22/37 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **2.04×** | +3.6 | 0.015 | 22/37 (KATO III, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.52×** | +3.3 | 0.040 | 19/37 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.374×** | -13.2 | 3e-37 | 31/37 (COLO 205, HEC-1-A, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.273×** | -12.4 | 1e-32 | 35/37 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.285×** | -11.9 | 1e-30 | 35/37 (COLO 205, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.290×** | -11.8 | 6e-30 | 36/37 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.292×** | -11.7 | 1e-29 | 35/37 (COLO 205, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.297×** | -11.6 | 7e-29 | 35/37 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.333×** | -10.5 | 1e-23 | 35/37 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.321×** | -10.4 | 2e-23 | 29/37 (COLO 205, A-427, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.338×** | -10.3 | 3e-23 | 33/37 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.392×** | -8.4 | 2e-15 | 35/37 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.413×** | -8.4 | 2e-15 | 34/37 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.425×** | -8.1 | 2e-14 | 34/37 (COLO 205, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.436×** | -7.9 | 1e-13 | 32/37 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -7.2 | 3e-11 | 27/37 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.254×** | -6.8 | 3e-10 | 32/38 (HT-29, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.278×** | -6.4 | 6e-09 | 31/37 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -6.2 | 2e-08 | 27/37 (COLO 205, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.649×** | -5.8 | 2e-07 | 28/37 (HEC-1-A, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.598×** | -4.9 | 2e-05 | 27/37 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.548×** | -4.7 | 6e-05 | 26/37 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.676×** | -3.6 | 0.007 | 26/37 (Panc 03.27, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 447 | 0 | 20 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0702× (z -18.2) |
| [[COLO 205 (line)]] | alt | 419 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -24.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0413× (z -23.0) |
| [[LS 180 (line)]] | wt | 270 | 0 | 17 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0832× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 12 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.124× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -13.4) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 12 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 208 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -14.7) |
| [[SW48 (line)]] | wt | 519 | 0 | 11 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0558× (z -14.9) |
| [[A-427 (line)]] | wt | 127 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.188× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 82.4 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0820× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.189× (z -10.3) |
| [[HOP62 (line)]] | alt | 115 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.220× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 70.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.259× (z -9.7) |
| [[H4 (line)]] | wt | 160 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0762× (z -15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.177× (z -10.2) |
| [[J82 (line)]] | alt | 65.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -9.0) |
| [[KATO III (line)]] | alt | 100 | 3 | 2 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 5.51× (z +11.7) | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 69.3 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.204× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 4 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.296× (z -9.6) |
| [[SW1417 (line)]] | alt | 78.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.220× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 167 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.202× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 168 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 87.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.178× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.178× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -8.8) |
| [[SW 1271 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0610× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 231 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.366× (z -10.2) |
| [[HS-578T (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 27.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP418-AS1]] | +0.61 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[STPG2]] | +0.61 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ZRANB2-DT]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[FBXL17]] | +0.58 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[TMEM232]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 | same gene group |
| [[EIF1B-AS1]] | +0.57 | +0.58 / +0.27 | both halves | 3e-04 |  |
| [[LINC02615]] | +0.57 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[BCLAF1]] | +0.56 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[ATXN7]] | +0.55 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[PKN2-AS1]] | +0.55 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[SLC38A4-AS1]] | +0.55 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[UFL1-AS1]] | +0.55 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC11]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SLC8B1]] | -0.57 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[DOCK6]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[BAIAP3]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ETHE1]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[PPP2R2C]] | -0.53 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[PBX4]] | -0.52 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[FCHSD1]] | -0.52 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[KYAT1]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PLEKHM1P1]] | -0.52 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[EML2]] | -0.52 | -0.48 / -0.37 | both halves | 9e-05 | same gene group |
| [[ABTB1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]] | B | GRHL2 activity raises NAALADL2's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without GRHL2 | 0.021 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[ANK3]] | B | ANK3 activity raises NAALADL2's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.78× lower at baseline in the lines without ANK3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers NAALADL2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[LINC00886]] | B | LINC00886 activity raises NAALADL2's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without LINC00886 | 0.056 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[LINC02147]] | B | LINC02147 activity raises NAALADL2's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without LINC02147 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |
| [[SLCO1B1]] | B | SLCO1B1 activity strengthens NAALADL2's drug response | lines that do not express SLCO1B1 (20) vs lines expressing it (17) | the lines without SLCO1B1 respond 0.78× as strongly (z diff +1.64); strongest at Panobinostat 5 µM: 0.37x vs 0.18x (z diff +2.9) | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; target measured in part of the lines; artifact flags |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises NAALADL2's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 3.42× lower at baseline in the lines without FSIP2-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR583HG]] | B | NAALADL2 activity raises MIR583HG's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without NAALADL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[ZFX]] | B | NAALADL2 activity lowers ZFX's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without NAALADL2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[GRHL2]] | B | NAALADL2 activity raises GRHL2's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 3.37× lower at baseline in the lines without NAALADL2 | 0.047 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[LINC01208]] | B | NAALADL2 activity raises LINC01208's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without NAALADL2 | 0.055 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[ZNF827]] | B | NAALADL2 activity raises ZNF827's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without NAALADL2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[BEAN1]] | B | NAALADL2 activity lowers BEAN1's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 2.07× higher at baseline in the lines without NAALADL2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | NAALADL2 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express NAALADL2 (11) vs lines expressing it (37) | the lines without NAALADL2: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[PLD2]] | B | NAALADL2 activity lowers PLD2's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without NAALADL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[ADAMTSL4]] | B | NAALADL2 activity lowers ADAMTSL4's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without NAALADL2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.5, 16.4); signed map (29.4, -10.2). **Vector** length 103, 36.5% of its response variance represented; |z| ≥ 3 in 1,430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.4 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -7.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.1 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.4 | -11.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.3 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylated alpha-linked acidic dipeptidase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:174,438,573-175,810,548 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M28 metallopeptidases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58DX5](https://www.uniprot.org/uniprotkb/Q58DX5) (Inactive N-acetylated-alpha-linked acidic dipeptidase-like protein 2):

> May be catalytically inactive.

**Summary**, from NCBI Gene [254827](https://www.ncbi.nlm.nih.gov/gene/254827):

> Predicted to act upstream of or within response to bacterium. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23219) · Entrez [254827](https://www.ncbi.nlm.nih.gov/gene/254827) · UniProt [Q58DX5](https://www.uniprot.org/uniprotkb/Q58DX5) · Ensembl [ENSG00000177694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177694)

## Data

Gene col 10854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10854); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10854]; `tensor/DDL_lfc|DDL_z.npy` [10854]; `embed/gene_vectors.npy` [10854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10854 or target_col == 10854). Every well: [[NAALADL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAALADL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
