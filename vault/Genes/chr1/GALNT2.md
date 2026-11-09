---
symbol: "GALNT2"
type: "gene"
col: 6785
ensembl_id: "ENSG00000143641"
name: "polypeptide N-acetylgalactosaminyltransferase 2"
location: "1q42.13"
module: 20
arm: "+"
pooled_cpm: 165.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# GALNT2

*polypeptide N-acetylgalactosaminyltransferase 2* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.61× (z +9.2, q 3e-17, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.672× (z -7.3, q 1e-10, down in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.778× (z -6.8, q 3e-09, down in 26 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC1]] (+0.57, fdr 2e-05), [[POLR2E]] (+0.57, fdr 7e-05), [[STOM]] (+0.56, fdr 3e-05); moves opposite to [[FAM98C]] (-0.51, fdr 6e-05), [[MED18]] (-0.50, fdr 4e-05), [[KLHL28]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +9.2 | 3e-17 | 41/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +9.0 | 8e-17 | 40/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +8.6 | 2e-15 | 37/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +7.0 | 4e-10 | 37/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +6.0 | 2e-07 | 30/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 1e-06 | 28/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.3 | 7e-06 | 26/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.8 | 1e-04 | 28/49 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +4.5 | 5e-04 | 25/50 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 9e-04 | 28/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 26/48 (A-172, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +4.0 | 0.003 | 22/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 22/47 (HOP62, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | **1.23×** | +3.9 | 0.004 | 25/48 (SW480, A-172, …) | two highest doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.004 | 21/48 (SW 900, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.042 | 22/48 (SW 900, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.067 | 13/48 (H4, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -7.3 | 1e-10 | 35/47 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.8 | 3e-09 | 26/49 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.771×** | -5.0 | 1e-04 | 24/48 (SNU-423, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.6 | 6e-04 | 20/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.855× | -4.2 | 0.002 | 20/49 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -4.2 | 0.002 | 23/48 (SNU-423, C32, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.004 | 24/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -3.9 | 0.008 | 23/48 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.870× | -3.8 | 0.009 | 18/49 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.046 | 18/49 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.850× | -3.1 | 0.089 | 16/48 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.850× | -3.1 | 0.089 | 19/48 (C32, J82, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.096 | 17/48 (SW 1088, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.844× | -3.0 | 0.100 | 16/47 (C32, AN3 CA, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | 0.855× | -3.0 | 0.100 | 18/48 (SW 900, H4, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 234 | 11 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.58× (z +11.9) ⚠ toxic; cell-cycle shift, explains ~81% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.38× (z +11.3) | — |
| [[A-172 (line)]] | wt | 167 | 10 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.7) | — |
| [[SW480 (line)]] | alt | 80.3 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 303 | 7 | 0 | [[Cobimetinib (drug)]] 5 µM 3.25× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 486 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -19.0) |
| [[C32 (line)]] | wt | 315 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.4) |
| [[A549 (line)]] | wt | 184 | 4 | 0 | [[Trametinib (drug)]] 5 µM 2.66× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 87.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.71× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 156 | 2 | 2 (2 ⚠) | [[Trametinib (drug)]] 5 µM 2.45× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 264 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 254 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.475× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.479× (z -8.8) |
| [[HOP62 (line)]] | alt | 182 | 3 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 3.15× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 89.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 249 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.5) |
| [[HCT15 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 90.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.03× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 158 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.7) | — |
| [[J82 (line)]] | alt | 193 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 87.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 226 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.9) |
| [[A-427 (line)]] | wt | 90.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[COLO 205 (line)]] | alt | 123 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.385× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 248 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -9.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 89.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 69.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.378× (z -9.2) |
| [[RKO (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 111 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 77.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[A498 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 247 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC1]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[POLR2E]] | +0.57 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[STOM]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[LRP11]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SLC16A7]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ADAM15]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[IL13RA1]] | +0.53 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[EXT2]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[FGG]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[G6PD]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TGFBI]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TGM2]] | +0.52 | +0.37 / +0.52 | both halves | 9e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM98C]] | -0.51 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MED18]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[KLHL28]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TMEM216]] | -0.48 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[UFL1]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GATAD1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C10orf88]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CHMP4C]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[CCDC174]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TMEM267]] | -0.46 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[C3orf33]] | -0.46 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ADPRM]] | -0.45 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises GALNT2's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without PLOD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[EFEMP1]] | B | EFEMP1 activity raises GALNT2's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.58× lower at baseline in the lines without EFEMP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.342). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (17.1, -21.5); signed map (-12.6, 33.2). **Vector** length 135, 42.8% of its response variance represented; |z| ≥ 3 in 1,522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.8 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.3 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.9 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.4 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -6.3 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.2 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:230,057,990-230,282,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T2 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 7 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10471](https://www.uniprot.org/uniprotkb/Q10471) (Polypeptide N-acetylgalactosaminyltransferase 2):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has a broad spectrum of substrates for peptides such as EA2, Muc5AC, Muc1a, Muc1b. Probably involved in O-linked glycosylation of the immunoglobulin A1 (IgA1) hinge region. Involved in O-linked glycosylation of APOC-III, ANGPTL3 and PLTP. It participates in the regulation of HDL-C metabolism.

**Summary**, from NCBI Gene [2590](https://www.ncbi.nlm.nih.gov/gene/2590):

> This gene encodes a member of the glycosyltransferase 2 protein family. Members of this family initiate mucin-type O-glycoslation of peptides in the Golgi apparatus. The encoded protein may be involved in O-linked glycosylation of the immunoglobulin A1 hinge region. This gene may influence triglyceride levels, and may be involved Type 2 diabetes, as well as several types of cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:4124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4124) · Entrez [2590](https://www.ncbi.nlm.nih.gov/gene/2590) · UniProt [Q10471](https://www.uniprot.org/uniprotkb/Q10471) · Ensembl [ENSG00000143641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143641)

## Data

Gene col 6785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6785); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6785]; `tensor/DDL_lfc|DDL_z.npy` [6785]; `embed/gene_vectors.npy` [6785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6785 or target_col == 6785). Every well: [[GALNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
