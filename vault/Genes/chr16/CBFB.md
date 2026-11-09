---
symbol: "CBFB"
type: "gene"
col: 874
ensembl_id: "ENSG00000067955"
name: "core-binding factor subunit beta"
location: "16q22.1"
module: 18
arm: "+"
pooled_cpm: 147.26
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CBFB

*core-binding factor subunit beta* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.66× (z +13.7, q 6e-40, up in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +12.3, q 4e-32, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.762× (z -7.3, q 2e-10, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMTM4]] (+0.61, fdr 1e-05), [[PBX3]] (+0.60, fdr 1e-05), [[SRPK1]] (+0.59, fdr 1e-05); moves opposite to [[UFSP2]] (-0.50, fdr 3e-05), [[ASB8]] (-0.49, fdr 1e-04), [[KBTBD7]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +13.7 | 6e-40 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +12.3 | 4e-32 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +9.3 | 2e-18 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +9.2 | 7e-18 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +8.0 | 2e-13 | 30/47 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +5.2 | 2e-05 | 26/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +5.0 | 5e-05 | 23/48 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.20× | +4.8 | 1e-04 | 21/48 (LS 180, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 3e-04 | 21/49 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +4.3 | 9e-04 | 17/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.15× | +3.9 | 0.006 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.6 | 0.013 | 14/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.13× | +3.3 | 0.042 | 15/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.042 | 8/48 (SW 900, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.0 | 0.088 | 13/48 (C-33 A, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.762×** | -7.3 | 2e-10 | 29/48 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.802×** | -6.3 | 6e-08 | 31/49 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.792×** | -6.3 | 6e-08 | 26/48 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -6.2 | 6e-08 | 20/48 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.804×** | -5.8 | 6e-07 | 28/49 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.828×** | -5.8 | 7e-07 | 24/48 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.826×** | -5.7 | 7e-07 | 23/50 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.823×** | -5.6 | 1e-06 | 24/48 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.819×** | -5.4 | 4e-06 | 24/47 (SW480, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.812×** | -5.4 | 4e-06 | 29/47 (HOP62, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.820×** | -5.3 | 5e-06 | 26/48 (J82, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.692×** | -5.0 | 3e-05 | 25/49 (NCI-H23, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -4.9 | 5e-05 | 18/48 (A-427, J82, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.829×** | -4.8 | 5e-05 | 23/48 (SW480, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.837× | -4.8 | 6e-05 | 22/48 (AN3 CA, A-172, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.708×** | -4.7 | 1e-04 | 27/47 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **0.727×** | -4.3 | 6e-04 | 21/48 (PANC-1, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 329 | 6 (3 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +16.5) | [[Binimetinib (drug)]] 0.5 µM 0.568× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 171 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.79× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 177 | 4 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.35× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.521× (z -9.0) |
| [[LoVo (line)]] | wt | 102 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 118 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.50× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.463× (z -10.1) |
| [[BT-474 (line)]] | alt | 118 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.75× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.6) | — |
| [[KATO III (line)]] | alt | 124 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +13.7) | — |
| [[A-427 (line)]] | wt | 154 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -10.7) |
| [[A498 (line)]] | wt | 121 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.621× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 162 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 105 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.472× (z -8.6) |
| [[H4 (line)]] | wt | 113 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.36× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.523× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[PANC-1 (line)]] | alt | 114 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.4) | — |
| [[A-172 (line)]] | wt | 175 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.564× (z -8.5) |
| [[AN3 CA (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 155 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[J82 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.509× (z -9.9) |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.271× (z -10.2) |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.37× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 192 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 195 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM4]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PBX3]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SRPK1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[NFATC2IP]] | +0.58 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[PTPN9]] | +0.56 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MOB1B]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ZNF718]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[VAV2]] | +0.54 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[BCL7C]] | +0.52 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NSD2]] | +0.52 | +0.67 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ASB8]] | -0.49 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[KBTBD7]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BNIP1]] | -0.49 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[CLCN3]] | -0.48 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[BTN3A1]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RAB30]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[THAP8]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ECH1]] | -0.48 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[COPS2]] | -0.47 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[SPTLC3]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MBNL2]] | -0.45 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CBFB's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (28.8, -38.2); signed map (-20.3, 47.7). **Vector** length 115, 34.2% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +6.4 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -9.0 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.2 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.8 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | core-binding factor subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,028,984-67,101,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEBP2B |
| Reactome | 29 pathways, smallest: RUNX1 and FOXP3 control the development of regulatory T lymphocytes (Tregs); RUNX3 regulates RUNX1-mediated transcription; RUNX1 regulates expression of components of tight junctions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13951](https://www.uniprot.org/uniprotkb/Q13951) (Core-binding factor subunit beta):

> Forms the heterodimeric complex core-binding factor (CBF) with RUNX family proteins (RUNX1, RUNX2, and RUNX3). RUNX members modulate the transcription of their target genes through recognizing the core consensus binding sequence 5'-TGTGGT-3', or very rarely, 5'-TGCGGT-3', within their regulatory regions via their runt domain, while CBFB is a non-DNA-binding regulatory subunit that allosterically enhances the sequence-specific DNA-binding capacity of RUNX. The heterodimers bind to the core site …

**Summary**, from NCBI Gene [865](https://www.ncbi.nlm.nih.gov/gene/865):

> The protein encoded by this gene is the beta subunit of a heterodimeric core-binding transcription factor belonging to the PEBP2/CBF transcription factor family which master-regulates a host of genes specific to hematopoiesis (e.g., RUNX1) and osteogenesis (e.g., RUNX2). The beta subunit is a non-DNA binding regulatory subunit; it allosterically enhances DNA binding by alpha subunit as the complex binds to the core site of various enhancers and promoters, including murine leukemia virus, …

**Accessions** — [HGNC:1539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1539) · Entrez [865](https://www.ncbi.nlm.nih.gov/gene/865) · UniProt [Q13951](https://www.uniprot.org/uniprotkb/Q13951) · Ensembl [ENSG00000067955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067955)

## Data

Gene col 874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 874); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 874]; `tensor/DDL_lfc|DDL_z.npy` [874]; `embed/gene_vectors.npy` [874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 874 or target_col == 874). Every well: [[CBFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
