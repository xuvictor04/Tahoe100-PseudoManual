---
symbol: "MGAT4A"
type: "gene"
col: 975
ensembl_id: "ENSG00000071073"
name: "alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A"
location: "2q11.2"
module: 11
arm: "-"
pooled_cpm: 22.93
n_lines_expressing: 39
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MGAT4A

*alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.19× (z +14.6, q 1e-45, up in 29 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.513× (z -17.5, q 0e+00, down in 29 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.403× (z -16.9, q 0e+00, down in 29 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDS1]] (+0.67, fdr 7e-06), [[TPD52]] (+0.62, fdr 1e-05), [[RALGPS1]] (+0.62, fdr 1e-05); moves opposite to [[ZNF830]] (-0.67, fdr 9e-06), [[ZNF407-AS1]] (-0.67, fdr 2e-05), [[DDX28]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 9 go from it, the strongest it → [[CDS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +14.6 | 1e-45 | 29/36 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +14.6 | 1e-45 | 29/36 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +13.6 | 7e-40 | 32/36 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +11.8 | 4e-30 | 30/36 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +11.2 | 7e-27 | 23/36 (A498, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +8.1 | 4e-14 | 26/37 (A498, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +6.5 | 8e-09 | 20/35 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.6 | 3e-04 | 9/26 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.085 | 7/36 (RKO, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.11 | 11/34 (SW480, NCI-H23, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.11 | 1/36 (LS 180) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.12 | 8/36 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.513×** | -17.5 | 0e+00 | 29/36 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.403×** | -16.9 | 0e+00 | 29/34 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.462×** | -14.3 | 3e-44 | 29/36 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.449×** | -14.3 | 3e-44 | 27/36 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -8.8 | 1e-16 | 24/38 (HEC-1-A, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.629×** | -8.6 | 7e-16 | 25/35 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.664×** | -7.6 | 3e-12 | 23/35 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -7.5 | 4e-12 | 25/34 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -7.5 | 6e-12 | 20/33 (KATO III, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.691×** | -6.8 | 4e-10 | 21/36 (Hs 766T, SW1417, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -5.4 | 4e-06 | 17/36 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.592×** | -5.0 | 3e-05 | 17/34 (SW 900, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -4.8 | 8e-05 | 16/35 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -4.5 | 2e-04 | 15/36 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -4.2 | 9e-04 | 16/34 (A498, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.799×** | -3.9 | 0.003 | 12/36 (SHP-77, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.004 | 9/35 (BT-474, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.747×** | -3.9 | 0.004 | 6/34 (BT-474, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.673×** | -3.7 | 0.005 | 12/34 (A-172, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.014 | 7/35 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 34.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0947× (z -17.2) |
| [[A498 (line)]] | wt | 11.4 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 10.2× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.66× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 21.9 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 51.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -11.1) |
| [[SHP-77 (line)]] | alt | 102 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.287× (z -10.8) |
| [[A-427 (line)]] | wt | 25.5 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0627× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.307× (z -12.3) |
| [[A549 (line)]] | wt | 16.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 143 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -9.0) |
| [[HOP62 (line)]] | alt | 6.89 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 5.48× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 10.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.27× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 37.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 7.37 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.26× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -8.5) |
| [[A-172 (line)]] | wt | 21.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.53× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.387× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 91.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0712× (z -18.5) |
| [[SW48 (line)]] | wt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.44× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.0) |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.177× (z -10.2) |
| [[SW480 (line)]] | alt | 9.20 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*28 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDS1]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TPD52]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[RALGPS1]] | +0.62 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SNX30]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ADAM10]] | +0.61 | +0.63 / +0.44 | both halves | 3e-05 | pathway: Post-translational protein phosphorylation |
| [[ATP8A1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[STRN]] | +0.60 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[NXPH4]] | +0.60 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[FAM102B]] | +0.60 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MPP7]] | +0.59 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[GTF2IP4]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SORT1]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*72 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF830]] | -0.67 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ZNF407-AS1]] | -0.67 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[DDX28]] | -0.66 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[RPAP1]] | -0.65 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ZNF181]] | -0.64 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.64 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.63 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NAIF1]] | -0.63 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ZNF629]] | -0.62 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[THBS4]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZNF689]] | -0.62 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SCGB2B2]] | -0.62 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity raises MGAT4A's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.56× lower at baseline in the lines without RAPGEF5 | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity raises MGAT4A's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without NR3C2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[SYT13]] | B | SYT13 activity raises MGAT4A's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without SYT13 | 0.037 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[CDS1]] | B | CDS1 activity raises MGAT4A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without CDS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[CYFIP2]] | B | CYFIP2 activity raises MGAT4A's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 3.60× lower at baseline in the lines without CYFIP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[ATP8A1]] | B | ATP8A1 activity raises MGAT4A's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 3.27× lower at baseline in the lines without ATP8A1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MGAT4A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MGAT4A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ENPP5]] | B | ENPP5 activity raises MGAT4A's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without ENPP5 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[FAM3C2P]] | B | FAM3C2P activity lowers MGAT4A's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 2.21× higher at baseline in the lines without FAM3C2P | 0.091 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[MPP7]] | C | MPP7 activity raises MGAT4A's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 3.57× lower at baseline in the lines without MPP7 | 0.008 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | MGAT4A activity raises CDS1's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 3.07× lower at baseline in the lines without MGAT4A | 0.025 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[CNGA1]] | B | MGAT4A activity raises CNGA1's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without MGAT4A | 0.042 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[ZNF181]] | B | MGAT4A activity weakens ZNF181's drug response | lines that do not express MGAT4A (11) vs lines expressing it (34) | the lines without MGAT4A respond 1.30× as strongly (z diff -0.57); strongest at Ouabain (Octahydrate) 0.5 µM: 0.34x vs 0.62x (z diff -2.5) | 0.055 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2; target measured in part of the lines; both ways; artifact flags |
| [[ZDHHC20]] | B | MGAT4A activity raises ZDHHC20's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without MGAT4A | 0.060 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[ZNF41]] | B | MGAT4A activity lowers ZNF41's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 1.42× higher at baseline in the lines without MGAT4A | 0.067 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[VOPP1]] | B | MGAT4A activity strengthens VOPP1's drug response | lines that do not express MGAT4A (10) vs lines expressing it (37) | the lines without MGAT4A respond 0.89× as strongly (z diff +1.05); strongest at Harringtonine 5 µM: 0.76x vs 0.47x (z diff +5.0) | 0.071 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2; target measured in part of the lines; both ways; artifact flags |
| [[RAPGEF5]] | B | MGAT4A activity raises RAPGEF5's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without MGAT4A | 0.072 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| cells under [[9-ING-41 (drug)]] 5 µM | B | MGAT4A activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express MGAT4A (11) vs lines expressing it (37) | the lines without MGAT4A: 1.23× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[MPP7]] | C | MGAT4A activity raises MPP7's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without MGAT4A | 0.027 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.6, 4.9); signed map (-28.8, -5.3). **Vector** length 89.6, 20.0% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +6.1 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +11.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.8 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.1 | -1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -14.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -14.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:98,619,106-98,731,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GnT-Iva, GnT-4a |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases |
| Reactome | 12 pathways, smallest: N-Glycan antennae elongation; N-glycan antennae elongation in the medial/trans-Golgi; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM21](https://www.uniprot.org/uniprotkb/Q9UM21) (Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A):

> Glycosyltransferase that catalyze the transfer of GlcNAc from UDP-GlcNAc to the GlcNAcbeta1-2Manalpha1-3 arm of the core structure of N-linked glycans through a beta1-4 linkage and participates in the production of tri- and tetra-antennary N-linked sugar chains. Involved in glucose transport by mediating SLC2A2/GLUT2 glycosylation, thereby controlling cell-surface expression of SLC2A2 in pancreatic beta cells (By similarity).

**Summary**, from NCBI Gene [11320](https://www.ncbi.nlm.nih.gov/gene/11320):

> This gene encodes a key glycosyltransferase that regulates the formation of tri- and multiantennary branching structures in the Golgi apparatus. The encoded protein, in addition to the related isoenzyme B, catalyzes the transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc in a beta-1,4 linkage to the Man-alpha-1,3-Man-beta-1,4-GlcNAc arm of R-Man-alpha-1,6(GlcNAc-beta-1,2-Man-alpha-1,3)Man-beta-1,4-GlcNAc-beta-1,4-GlcNAc-beta-1-Asn. The encoded protein may play a role in regulating the …

**Accessions** — [HGNC:7047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7047) · Entrez [11320](https://www.ncbi.nlm.nih.gov/gene/11320) · UniProt [Q9UM21](https://www.uniprot.org/uniprotkb/Q9UM21) · Ensembl [ENSG00000071073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071073)

## Data

Gene col 975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 975); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 975]; `tensor/DDL_lfc|DDL_z.npy` [975]; `embed/gene_vectors.npy` [975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 975 or target_col == 975). Every well: [[MGAT4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
