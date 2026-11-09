---
symbol: "SDHA"
type: "gene"
col: 1052
ensembl_id: "ENSG00000073578"
name: "succinate dehydrogenase complex flavoprotein subunit A"
location: "5p15.33"
module: 168
arm: "+"
pooled_cpm: 80.07
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# SDHA

*succinate dehydrogenase complex flavoprotein subunit A* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.67× (z +9.7, q 2e-19, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.550× (z -15.9, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLEC]] (+0.71, fdr 7e-06), [[SDHAP4]] (+0.71, fdr 1e-05), [[RPA1]] (+0.68, fdr 1e-05); moves opposite to [[THG1L]] (-0.66, fdr 1e-05), [[METTL18]] (-0.64, fdr 3e-05), [[EIF4EBP3]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +9.7 | 2e-19 | 39/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +8.3 | 4e-14 | 35/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +8.0 | 2e-13 | 38/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +7.5 | 1e-11 | 31/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +5.6 | 3e-06 | 26/49 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Tolcapone (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 4e-05 | 28/49 (A498, KATO III, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +4.3 | 0.001 | 26/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +4.3 | 0.001 | 23/48 (NCI-H1573, SW480, …) | all doses, flat | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.004 | 22/48 (LS 180, J82, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.010 | 19/48 (A-172, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.20× | +3.4 | 0.033 | 14/48 (BT-474, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.550×** | -15.9 | 0e+00 | 43/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -10.6 | 9e-24 | 37/48 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -8.0 | 3e-13 | 36/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -5.2 | 3e-05 | 29/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.777×** | -4.7 | 3e-04 | 24/49 (SW48, H4, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.848× | -4.4 | 0.001 | 22/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.802×** | -4.1 | 0.003 | 22/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.848× | -4.1 | 0.003 | 18/49 (HEC-1-A, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -4.0 | 0.003 | 19/41 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trimetrexate (drug)]] 0.05 µM |  | **0.818×** | -3.8 | 0.010 | 24/48 (SW 1271, LS 180, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.6 | 0.017 | 23/48 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.023 | 20/48 (SW 1088, CHP-212, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.775×** | -3.4 | 0.029 | 16/48 (HT-29, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.883× | -3.3 | 0.039 | 5/48 (H4, SNU-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.839× | -3.3 | 0.039 | 19/48 (HOP62, A-427, …) | rises with dose | composition shift |
| [[Rutin (trihydrate) (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.039 | 12/48 (NCI-H2347, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.847× | -3.1 | 0.067 | 21/48 (H4, LS 180, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.799×** | -3.0 | 0.086 | 17/48 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.894× | -2.9 | 0.100 | 8/48 (J82, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 146 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -22.1) |
| [[SW480 (line)]] | alt | 91.7 | 4 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -10.0) |
| [[A-172 (line)]] | wt | 90.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 64.6 | 3 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.8) |
| [[SW 900 (line)]] | alt | 161 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.4) |
| [[A-427 (line)]] | wt | 109 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.3) |
| [[A498 (line)]] | wt | 114 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.458× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -29.1) |
| [[C32 (line)]] | wt | 61.4 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -23.3) |
| [[SHP-77 (line)]] | alt | 93.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 73.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 43.6 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -8.5) |
| [[LS 180 (line)]] | wt | 79.5 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 55.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.19× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 93.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 71.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -15.6) |
| [[A549 (line)]] | wt | 57.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.1) |
| [[COLO 205 (line)]] | alt | 71.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.5) |
| [[HS-578T (line)]] | alt | 86.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.5) |
| [[HT-29 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.9) |
| [[J82 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 59.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -22.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -8.6) |
| [[SNU-1 (line)]] | wt | 60.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.8) |
| [[SNU-423 (line)]] | alt | 62.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -8.9) |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 145 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLEC]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[RPA1]] | +0.68 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.66 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[P3H1]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CRAT]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[SETD3]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.63 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[ZDHHC16]] | +0.62 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[RNF4]] | +0.62 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.62 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THG1L]] | -0.66 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[METTL18]] | -0.64 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.64 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[CFLAR-AS1]] | -0.64 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.62 | -0.71 / -0.40 | both halves | 5e-05 |  |
| [[GABPB2]] | -0.61 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[ZNF518A]] | -0.60 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[KCNMB3]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[LINC00486]] | -0.60 | -0.69 / -0.30 | both halves | 2e-04 |  |
| [[LZIC]] | -0.59 | -0.74 / -0.31 | both halves | 2e-04 |  |
| [[NSRP1]] | -0.59 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[JMJD1C]] | -0.59 | -0.38 / -0.57 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.8, -15.7); signed map (-39.7, -11.2). **Vector** length 123, 33.9% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.7 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +8.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +0.4 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.9 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -12.6 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.9 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.4 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex flavoprotein subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:218,303-257,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FP, SDHF; previously SDH2 |
| Gene groups (HGNC) | Mitochondrial complex II: succinate dehydrogenase subunits; Flavoproteins |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P31040](https://www.uniprot.org/uniprotkb/P31040) (Succinate dehydrogenase):

> Flavoprotein (FP) subunit of succinate dehydrogenase (SDH) that is involved in complex II of the mitochondrial electron transport chain and is responsible for transferring electrons from succinate to ubiquinone (coenzyme Q). SDH also oxidizes malate to the non-canonical enol form of oxaloacetate, enol-oxaloacetate (By similarity). Enol-oxaloacetate, which is a potent inhibitor of the succinate dehydrogenase activity, is further isomerized into keto-oxaloacetate (By similarity). Can act as a …

**Summary**, from NCBI Gene [6389](https://www.ncbi.nlm.nih.gov/gene/6389):

> This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identified on chromosome 3q29. Alternatively spliced transcript variants encoding different isoforms have …

**Accessions** — [HGNC:10680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10680) · Entrez [6389](https://www.ncbi.nlm.nih.gov/gene/6389) · UniProt [P31040](https://www.uniprot.org/uniprotkb/P31040) · Ensembl [ENSG00000073578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073578)

## Data

Gene col 1052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1052); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1052]; `tensor/DDL_lfc|DDL_z.npy` [1052]; `embed/gene_vectors.npy` [1052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1052 or target_col == 1052). Every well: [[SDHA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
