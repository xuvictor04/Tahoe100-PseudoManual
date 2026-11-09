---
symbol: "CLASP2"
type: "gene"
col: 8714
ensembl_id: "ENSG00000163539"
name: "cytoplasmic linker associated protein 2"
location: "3p22.3"
module: 18
arm: "+"
pooled_cpm: 135.4
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CLASP2

*cytoplasmic linker associated protein 2* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.20× (z +4.9, q 5e-04, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-172 2.04×, J82 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 1.69×); [[Ponatinib (drug)]] 5 µM in 1 line (RPMI-7951 2.04×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.579× (z -13.3, q 9e-38, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.763× (z -7.1, q 1e-10, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDIN1]] (+0.66, fdr 7e-06), [[UBE3C]] (+0.63, fdr 1e-05), [[VWA8]] (+0.61, fdr 1e-05); moves opposite to [[RARA]] (-0.53, fdr 2e-05), [[SNIP1]] (-0.51, fdr 3e-05), [[ZNF490]] (-0.50, fdr 8e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC8D]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-172 2.04×, J82 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 1.69×); [[Ponatinib (drug)]] 5 µM in 1 line (RPMI-7951 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +4.9 | 5e-04 | 21/48 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 0.002 | 21/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.9 | 0.018 | 11/48 (SNU-1, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.044 | 19/49 (SNU-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.061 | 15/47 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.067 | 16/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.067 | 13/47 (SW480, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -13.3 | 9e-38 | 35/45 (SK-MEL-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.748×** | -10.8 | 1e-24 | 30/48 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -8.2 | 5e-14 | 32/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.754×** | -7.4 | 1e-11 | 28/49 (NCI-H23, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.747×** | -7.4 | 1e-11 | 27/44 (SNU-1, A-427, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -7.1 | 1e-10 | 29/48 (SW480, AN3 CA, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.601×** | -7.0 | 2e-10 | 37/49 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -6.8 | 9e-10 | 26/49 (A549, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.776×** | -6.7 | 2e-09 | 31/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -4.7 | 2e-04 | 19/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.828×** | -4.6 | 2e-04 | 23/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.850× | -4.3 | 9e-04 | 19/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.857× | -4.0 | 0.002 | 21/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.788×** | -3.3 | 0.042 | 15/38 (Panc 03.27, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 241 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.519× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 125 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.495× (z -11.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.539× (z -10.4) |
| [[SW480 (line)]] | alt | 218 | 1 | 5 (4 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.69× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -14.8) |
| [[A-427 (line)]] | wt | 194 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[MIA PaCa-2 (line)]] | alt | 140 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -13.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -11.7) |
| [[LoVo (line)]] | wt | 197 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.498× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 169 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 142 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 170 | 1 | 3 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 2.04× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -12.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 214 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 76.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -8.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-1 (line)]] | wt | 199 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0795× (z -28.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -11.9) |
| [[SW48 (line)]] | wt | 220 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -9.6) |
| [[A-172 (line)]] | wt | 96.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 65.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -18.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 172 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 211 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.210× (z -12.8) |
| [[CHP-212 (line)]] | wt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -15.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.134× (z -14.1) ⚠ toxic |
| [[RKO (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -12.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[H4 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.134× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -18.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HT-29 (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.496× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 96.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.0858× (z -9.2) |
| [[PANC-1 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.646× (z -11.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW1417 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -11.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 205 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIN1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[UBE3C]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[VWA8]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SPECC1L]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CAMKMT]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MRTFB]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PTPN4]] | +0.59 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[R3HDM1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MIPOL1]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CMSS1]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[DTNB]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARA]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SNIP1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.50 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[GPR84-AS1]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[SNX33]] | -0.49 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[PLXNB3]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF436]] | -0.45 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ZNF17]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[FAM120AOS]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[RSRP1]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8D]] | C | LRRC8D activity raises CLASP2's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.1, -34.3); signed map (-13.9, -51.5). **Vector** length 94.6, 23.8% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.6 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.1 | -7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +4.8 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.5 | -10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -7.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.2 | -8.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | +0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Daidzin (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic linker associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:33,496,245-33,718,356 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0627 |
| Gene groups (HGNC) | TOG domain containing |
| Reactome | 21 pathways, smallest: Role of ABL in ROBO-SLIT signaling; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [O75122](https://www.uniprot.org/uniprotkb/O75122) (CLIP-associating protein 2):

> Microtubule plus-end tracking protein that promotes the stabilization of dynamic microtubules. Involved in the nucleation of noncentrosomal microtubules originating from the trans-Golgi network (TGN). Required for the polarization of the cytoplasmic microtubule arrays in migrating cells towards the leading edge of the cell. May act at the cell cortex to enhance the frequency of rescue of depolymerizing microtubules by attaching their plus-ends to cortical platforms composed of ERC1 and PHLDB2. …

**Summary**, from NCBI Gene [23122](https://www.ncbi.nlm.nih.gov/gene/23122):

> Enables cytoskeletal protein binding activity; dystroglycan binding activity; and protein tyrosine kinase binding activity. Involved in several processes, including cytoskeleton organization; regulation of cell migration; and regulation of supramolecular fiber organization. Located in several cellular components, including basal cortex; focal adhesion; and microtubule cytoskeleton. Is active in glutamatergic synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17078) · Entrez [23122](https://www.ncbi.nlm.nih.gov/gene/23122) · UniProt [O75122](https://www.uniprot.org/uniprotkb/O75122) · Ensembl [ENSG00000163539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163539)

## Data

Gene col 8714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8714); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8714]; `tensor/DDL_lfc|DDL_z.npy` [8714]; `embed/gene_vectors.npy` [8714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8714 or target_col == 8714). Every well: [[CLASP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLASP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
