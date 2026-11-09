---
symbol: "TUBA1C"
type: "gene"
col: 9488
ensembl_id: "ENSG00000167553"
name: "tubulin alpha 1c"
location: "12q13.12"
module: 171
arm: "-"
pooled_cpm: 107.97
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# TUBA1C

*tubulin alpha 1c* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.05× (z +8.9, q 4e-16, up in 42 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.63× (z +6.1, q 2e-07, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.696× (z -4.4, q 0.005, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBB4B]] (+0.70, fdr 7e-06), [[GPATCH2L]] (+0.55, fdr 1e-05), [[RIC8B]] (+0.55, fdr 2e-05); moves opposite to [[KCTD3]] (-0.56, fdr 1e-05), [[TMEM183A]] (-0.56, fdr 1e-05), [[AUH]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.05×** | +8.9 | 4e-16 | 42/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.93×** | +8.1 | 1e-13 | 46/48 (RPMI-7951, CFPAC-1, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.66×** | +6.3 | 7e-08 | 38/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +6.1 | 2e-07 | 38/48 (C32, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.9 | 4e-07 | 34/49 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.65×** | +5.8 | 8e-07 | 33/49 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.59×** | +5.5 | 3e-06 | 28/43 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 33/48 (C32, RPMI-7951, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.0 | 4e-05 | 37/48 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.49×** | +4.9 | 5e-05 | 31/48 (CFPAC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.47×** | +4.8 | 1e-04 | 33/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 2e-04 | 39/48 (HT-29, A498, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 5e-04 | 37/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.005 | 33/48 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.7 | 0.008 | 30/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.019 | 25/47 (HT-29, COLO 205, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.040 | 27/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.064 | 25/49 (PANC-1, CFPAC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.696×** | -4.4 | 0.005 | 31/48 (LoVo, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.516×** | -4.3 | 0.006 | 37/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.714×** | -4.1 | 0.006 | 30/50 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.785×** | -4.1 | 0.006 | 31/48 (BT-474, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.777×** | -3.8 | 0.013 | 28/48 (SW480, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -3.8 | 0.013 | 32/48 (A498, SW480, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.019 | 28/47 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.725×** | -3.6 | 0.019 | 31/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.730×** | -3.6 | 0.022 | 31/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.750×** | -3.3 | 0.059 | 25/48 (SW48, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -3.2 | 0.072 | 23/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -3.1 | 0.073 | 25/49 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.773×** | -3.1 | 0.073 | 28/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.074 | 26/48 (H4, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.094 | 22/48 (H4, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 103 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +18.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 65.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.62× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 85.3 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.25× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +9.0) | — |
| [[A498 (line)]] | wt | 172 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[CFPAC-1 (line)]] | alt | 70.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 68.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 106 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Belinostat (drug)]] 5 µM 0.407× (z -8.6) |
| [[A549 (line)]] | wt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[BT-474 (line)]] | alt | 89.8 | 0 | 1 | — | [[Neratinib (drug)]] 0.5 µM 0.308× (z -8.7) |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0516× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +11.2) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 92.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[RPMI-7951 (line)]] | alt | 79.5 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.09× (z +9.0) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 113 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 104 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 131 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB4B]] | +0.70 | +0.77 / +0.65 | both halves | 7e-06 | pathway: Activation of AMPK downstream of NMDARs; STRING 990 |
| [[GPATCH2L]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RIC8B]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SNRPB]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MYH15]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ZNF562]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TUBB6]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 | pathway: Activation of AMPK downstream of NMDARs; STRING 981 |
| [[NACC1]] | +0.53 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CRK]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[DBF4B]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CCDC18]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BLZF2P]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.56 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[TMEM183A]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[AUH]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PPP1CB]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 | pathway: G2/M Transition |
| [[TM7SF3]] | -0.54 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[RCOR3]] | -0.53 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ATG2B]] | -0.52 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[SNX2]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MRS2]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[YPEL2]] | -0.51 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[DNAJC12]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[RBM33]] | -0.51 | -0.60 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TUBA1C's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DNAJC12]] | B | DNAJC12 activity lowers TUBA1C's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.24× higher at baseline in the lines without DNAJC12 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[TUBB6]] | B | TUBB6 activity raises TUBA1C's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 1.12× lower at baseline in the lines without TUBB6 | 0.092 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TUBA1C's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | TUBA1C's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.383 over the table, 0.042 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (33.2, -23.2); signed map (9.9, 14.8). **Vector** length 108, 36.4% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.1 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.6 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -5.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -4.9 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -0.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tubulin alpha 1c |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,188,736-49,274,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14580, MGC10851, bcm948; previously TUBA6 |
| Gene groups (HGNC) | Tubulin alpha family |
| Reactome | 83 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQE3](https://www.uniprot.org/uniprotkb/Q9BQE3) (Tubulin alpha-1C chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [84790](https://www.ncbi.nlm.nih.gov/gene/84790):

> Predicted to enable GTP binding activity. Predicted to be a structural constituent of cytoskeleton. Predicted to be involved in microtubule cytoskeleton organization; mitotic cell cycle; and neuron differentiation. Located in cilium; microtubule cytoskeleton; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20768) · Entrez [84790](https://www.ncbi.nlm.nih.gov/gene/84790) · UniProt [Q9BQE3](https://www.uniprot.org/uniprotkb/Q9BQE3) · Ensembl [ENSG00000167553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167553)

## Data

Gene col 9488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9488); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9488]; `tensor/DDL_lfc|DDL_z.npy` [9488]; `embed/gene_vectors.npy` [9488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9488 or target_col == 9488). Every well: [[TUBA1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBA1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
