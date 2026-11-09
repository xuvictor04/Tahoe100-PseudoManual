---
symbol: "DCAF13"
type: "gene"
col: 9036
ensembl_id: "ENSG00000164934"
name: "DDB1 and CUL4 associated factor 13"
location: "8q22.3"
module: 33
arm: "+"
pooled_cpm: 64.76
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 20
n_dd_up_clean: 15
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# DCAF13

*DDB1 and CUL4 associated factor 13* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.69× (z +8.9, q 3e-16, up in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.55× (z +7.8, q 1e-12, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.682× (z -6.5, q 4e-08, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URB1]] (+0.71, fdr 7e-06), [[WDR3]] (+0.71, fdr 7e-06), [[NSUN2]] (+0.71, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.66, fdr 1e-05), [[WBP4]] (-0.61, fdr 1e-05), [[C11orf58]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.9 | 3e-16 | 35/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +8.2 | 8e-14 | 43/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.8 | 1e-12 | 37/48 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.5 | 1e-11 | 38/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 2e-06 | 27/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.5 | 4e-06 | 30/45 (SW 900, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.5 | 4e-06 | 27/48 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.36×** | +5.4 | 4e-06 | 29/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +5.3 | 7e-06 | 27/48 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.34×** | +5.2 | 1e-05 | 28/48 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.2 | 1e-05 | 31/48 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 2e-05 | 30/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.32×** | +4.9 | 3e-05 | 25/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +4.7 | 1e-04 | 24/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.29×** | +4.2 | 0.001 | 21/45 (NCI-H460, SNU-423, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 23/49 (SHP-77, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 21/48 (C-33 A, NCI-H1573, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.006 | 24/48 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.009 | 16/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.023 | 11/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.027 | 16/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.027 | 15/48 (MIA PaCa-2, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.047 | 14/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.682×** | -6.5 | 4e-08 | 30/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.699×** | -6.1 | 3e-07 | 30/47 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -5.5 | 6e-06 | 30/48 (RKO, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.815×** | -5.1 | 4e-05 | 22/48 (AsPC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.747×** | -5.1 | 4e-05 | 30/50 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.762×** | -4.8 | 1e-04 | 26/47 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.822×** | -4.8 | 1e-04 | 24/48 (SW480, RKO, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.811×** | -4.3 | 1e-03 | 24/48 (A-427, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.779×** | -4.3 | 0.001 | 22/48 (C32, SW 1088, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -4.2 | 0.001 | 21/48 (A-427, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.832×** | -4.1 | 0.002 | 17/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.796×** | -4.0 | 0.002 | 18/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.797×** | -4.0 | 0.002 | 21/48 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.662×** | -3.8 | 0.005 | 19/50 (AsPC-1, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.006 | 19/48 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.669×** | -3.7 | 0.007 | 18/48 (AsPC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 129 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +12.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 142 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.404× (z -9.4) |
| [[RKO (line)]] | wt | 147 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.1) |
| [[A-427 (line)]] | wt | 46.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0889× (z -22.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 42.0 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.83× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[AN3 CA (line)]] | alt | 62.8 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.173× (z -9.3) |
| [[COLO 205 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.257× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 45.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.08× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[Panc 03.27 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 88.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.0) |
| [[SW480 (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -9.7) |
| [[A-172 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[WDR3]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[NSUN2]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[STRAP]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 | same gene group |
| [[NAPG]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TFB2M]] | +0.67 | +0.79 / +0.54 | both halves | 1e-05 | STRING 757 |
| [[UTP18]] | +0.67 | +0.72 / +0.58 | both halves | 8e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[PMPCA]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ZNF587B]] | +0.66 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[WDR36]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.66 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[WBP4]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.60 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB4]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CREBBP]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.58 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[H2AJ]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[CHD2]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[UNK]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TAPBPL]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[TEF]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RNF115]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises DCAF13's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.3, -28.4); signed map (-14.0, -57.9). **Vector** length 117, 35.6% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.8 | +5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.2 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.9 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.9 | +4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.9 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:103,414,714-103,443,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O0463, Gm83, HSPC064, Sof1; previously WDSOF1 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors; SSU processome |
| Reactome | 6 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV06](https://www.uniprot.org/uniprotkb/Q9NV06) (DDB1- and CUL4-associated factor 13):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Participates in the 18S rRNA processing in growing oocytes, being …

**Summary**, from NCBI Gene [25879](https://www.ncbi.nlm.nih.gov/gene/25879):

> Enables nuclear estrogen receptor binding activity and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including decidualization; epigenetic programming in the zygotic pronuclei; and spindle assembly involved in female meiosis. Part of Cul4-RING E3 ubiquitin ligase complex. Is active in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24535) · Entrez [25879](https://www.ncbi.nlm.nih.gov/gene/25879) · UniProt [Q9NV06](https://www.uniprot.org/uniprotkb/Q9NV06) · Ensembl [ENSG00000164934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164934)

## Data

Gene col 9036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9036); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9036]; `tensor/DDL_lfc|DDL_z.npy` [9036]; `embed/gene_vectors.npy` [9036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9036 or target_col == 9036). Every well: [[DCAF13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
