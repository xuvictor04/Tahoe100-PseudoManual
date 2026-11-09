---
symbol: "ATXN7"
type: "gene"
col: 8740
ensembl_id: "ENSG00000163635"
name: "ataxin 7"
location: "3p14.1"
module: 95
arm: "+"
pooled_cpm: 131.2
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# ATXN7

*ataxin 7* — 3p14.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 1.88×, LoVo 1.68×, Hs 766T 1.71×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 1.87×, NCI-H23 1.82×, LS 180 1.67×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.508× (z -13.1, q 3e-36, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFX]] (+0.72, fdr 9e-06), [[ZNF827]] (+0.68, fdr 1e-05), [[MIER3]] (+0.68, fdr 1e-05); moves opposite to [[NBPF3]] (-0.69, fdr 1e-05), [[ARPC1A]] (-0.65, fdr 1e-05), [[MAST3]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FCHO1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8740.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 1.88×, LoVo 1.68×, Hs 766T 1.71×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 1.87×, NCI-H23 1.82×, LS 180 1.67×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.8 | 0.094 | 21/49 (LS 180, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.24 | 11/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.24 | 4/49 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.19× | +3.1 | 0.24 | 17/50 (NCI-H1573, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.36× | +3.1 | 0.24 | 26/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.24 | 21/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -13.1 | 3e-36 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.514×** | -12.8 | 3e-35 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.563×** | -11.1 | 3e-26 | 44/49 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.564×** | -11.0 | 3e-26 | 46/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.553×** | -11.0 | 5e-26 | 41/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -8.2 | 2e-14 | 41/45 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -6.2 | 3e-08 | 37/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -5.4 | 4e-06 | 36/48 (HT-29, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.776×** | -4.9 | 7e-05 | 33/48 (HOP62, C32, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.811×** | -4.0 | 0.003 | 25/48 (HT-29, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.816×** | -3.9 | 0.005 | 29/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.820×** | -3.7 | 0.010 | 24/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -3.4 | 0.028 | 13/48 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.093 | 20/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.803×** | -3.0 | 0.093 | 21/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 145 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -10.7) |
| [[SW480 (line)]] | alt | 135 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -16.0) |
| [[A-172 (line)]] | wt | 126 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 273 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 156 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0926× (z -28.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.357× (z -12.6) |
| [[HOP62 (line)]] | alt | 133 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.475× (z -10.9) |
| [[HS-578T (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.486× (z -8.8) |
| [[HT-29 (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -10.6) |
| [[LoVo (line)]] | wt | 131 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -9.7) |
| [[LS 180 (line)]] | wt | 108 | 2 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 156 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.418× (z -10.2) |
| [[SW48 (line)]] | wt | 126 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -10.6) |
| [[C32 (line)]] | wt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 103 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.471× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.521× (z -8.6) |
| [[PANC-1 (line)]] | alt | 98.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.486× (z -11.5) |
| [[SNU-1 (line)]] | wt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 104 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.515× (z -8.5) |
| [[A-427 (line)]] | wt | 119 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -8.6) |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -10.2) |
| [[C-33 A (line)]] | alt | 203 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.439× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.474× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 73.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 161 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.401× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 170 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.466× (z -8.8) |
| [[A549 (line)]] | wt | 117 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -8.5) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.198× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.491× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 93.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.431× (z -9.2) |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[SW 1271 (line)]] | alt | 153 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.190× (z -9.1) |
| [[A498 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFX]] | +0.72 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[ZNF827]] | +0.68 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MIER3]] | +0.68 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PATL2]] | +0.67 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[ZBED5]] | +0.65 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ZNF689]] | +0.65 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CPSF2]] | +0.65 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ZNF747]] | +0.65 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ANXA2R-AS1]] | +0.64 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ARID1A]] | +0.64 | +0.34 / +0.64 | both halves | 1e-04 | pathway: Chromatin modifying enzymes |
| [[SCAMP1-AS1]] | +0.63 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CREBBP]] | +0.63 | +0.37 / +0.52 | both halves | 8e-05 | pathway: Chromatin modifying enzymes |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.69 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ARPC1A]] | -0.65 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MAST3]] | -0.65 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TOMM20]] | -0.64 | -0.42 / -0.49 | both halves | 4e-05 | pathway: Deubiquitination |
| [[STAM]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 | pathway: Deubiquitination |
| [[HDAC11]] | -0.62 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PLD3]] | -0.62 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.61 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SHQ1]] | -0.59 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PGPEP1]] | -0.59 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[STX7]] | -0.59 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[WDR59]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCHO1]] | B | FCHO1 activity raises ATXN7's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without FCHO1 | 0.022 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[GLI3]] | B | GLI3 activity raises ATXN7's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 1.16× lower at baseline in the lines without GLI3 | 0.075 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-0.2, 7.5); signed map (23.7, -17.8). **Vector** length 99.3, 29.0% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -11.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:63,863,155-64,003,462 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OPCA3, ADCAII, SGF73; previously SCA7 |
| Gene groups (HGNC) | SAGA complex; Ataxin 7 family |
| Reactome | 5 pathways, smallest: HATs acetylate histones; Ub-specific processing proteases; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15265](https://www.uniprot.org/uniprotkb/O15265) (Ataxin-7):

> Acts as a component of the SAGA (aka STAGA) transcription coactivator-HAT complex. Mediates the interaction of SAGA complex with the CRX and is involved in CRX-dependent gene activation. Probably involved in tethering the deubiquitination module within the SAGA complex. Necessary for microtubule cytoskeleton stabilization. Involved in neurodegeneration.

**Summary**, from NCBI Gene [6314](https://www.ncbi.nlm.nih.gov/gene/6314):

> The autosomal dominant cerebellar ataxias (ADCA) are a heterogeneous group of neurodegenerative disorders characterized by progressive degeneration of the cerebellum, brain stem and spinal cord. Clinically, ADCA has been divided into three groups: ADCA types I-III. ADCAI is genetically heterogeneous, with five genetic loci, designated spinocerebellar ataxia (SCA) 1, 2, 3, 4 and 6, being assigned to five different chromosomes. ADCAII, which always presents with retinal degeneration (SCA7), and …

**Accessions** — [HGNC:10560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10560) · Entrez [6314](https://www.ncbi.nlm.nih.gov/gene/6314) · UniProt [O15265](https://www.uniprot.org/uniprotkb/O15265) · Ensembl [ENSG00000163635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163635)

## Data

Gene col 8740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8740); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8740]; `tensor/DDL_lfc|DDL_z.npy` [8740]; `embed/gene_vectors.npy` [8740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8740 or target_col == 8740). Every well: [[ATXN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
