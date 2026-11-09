---
symbol: "TGFB1"
type: "gene"
col: 2584
ensembl_id: "ENSG00000105329"
name: "transforming growth factor beta 1"
location: "19q13.2"
module: 161
arm: "+"
pooled_cpm: 106.76
n_lines_expressing: 42
n_dd_up: 5
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 15
direction_downstream: 3
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# TGFB1

*transforming growth factor beta 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.53× (z +7.0, q 1e-09, up in 25 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 5.87×, NCI-H460 2.98×, A549 2.00×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H460 5.00×, A549 3.33×, A498 3.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 6.98×, SW480 2.64×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.12×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.51×).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.486× (z -11.8, q 2e-29, down in 31 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASMTL]] (+0.71, fdr 1e-05), [[RASA4B]] (+0.65, fdr 1e-05), [[HCN2]] (+0.63, fdr 8e-06); moves opposite to [[RAB11FIP2]] (-0.61, fdr 1e-05), [[QRSL1]] (-0.57, fdr 1e-05), [[PAIP1]] (-0.56, fdr 2e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[NRARP]] → it (grade B ⚠); 3 go from it, the strongest it → [[MEIS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 5.87×, NCI-H460 2.98×, A549 2.00×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H460 5.00×, A549 3.33×, A498 3.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 6.98×, SW480 2.64×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.12×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +7.0 | 1e-09 | 25/40 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.004 | 19/40 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.2 | 0.005 | 20/40 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.5 | 0.066 | 17/41 (LoVo, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.4 | 0.066 | 18/39 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -11.8 | 2e-29 | 31/39 (HOP62, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.739×** | -7.0 | 7e-10 | 29/40 (A-172, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -6.2 | 8e-08 | 28/40 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.689×** | -6.1 | 2e-07 | 26/40 (AsPC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.680×** | -5.8 | 6e-07 | 25/40 (AsPC-1, HCT15, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.701×** | -5.8 | 6e-07 | 29/40 (HCT15, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.716×** | -5.5 | 4e-06 | 21/40 (AsPC-1, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.731×** | -4.9 | 6e-05 | 20/39 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.807×** | -4.9 | 7e-05 | 20/40 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.793×** | -4.8 | 8e-05 | 23/40 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.732×** | -4.8 | 8e-05 | 24/40 (HOP62, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.735×** | -4.7 | 1e-04 | 25/42 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.788×** | -4.7 | 1e-04 | 19/40 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.825×** | -4.5 | 3e-04 | 22/41 (HOP62, SW 900, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.781×** | -4.4 | 5e-04 | 20/41 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.771×** | -4.1 | 0.001 | 21/39 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -4.1 | 0.001 | 21/40 (A-172, NCI-H661, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.778×** | -4.0 | 0.002 | 21/40 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.004 | 18/41 (SW480, HCT15, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.850× | -3.7 | 0.005 | 14/41 (SW480, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 473 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 40.8 | 11 (9 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.98× (z +18.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.12× (z +10.3) | — |
| [[A-172 (line)]] | wt | 304 | 0 | 9 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.468× (z -12.9) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.411× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 254 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 147 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -15.4) |
| [[SW480 (line)]] | alt | 102 | 3 (3 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.64× (z +9.8) ⚠ toxic; transcription drop | [[Binimetinib (drug)]] 0.5 µM 0.480× (z -9.2) |
| [[A-427 (line)]] | wt | 78.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.330× (z -10.2) |
| [[HS-578T (line)]] | alt | 267 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.479× (z -11.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.445× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 45.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -10.9) |
| [[H4 (line)]] | wt | 260 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.351× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 280 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -10.9) |
| [[A498 (line)]] | wt | 110 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +23.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 131 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.33× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 150 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -13.5) |
| [[HCT15 (line)]] | alt | 159 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.373× (z -8.5) |
| [[RKO (line)]] | wt | 77.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -17.9) |
| [[RPMI-7951 (line)]] | alt | 282 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -9.8) |
| [[SNU-423 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -10.6) |
| [[SW 900 (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -12.9) |
| [[SW48 (line)]] | wt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -9.5) |
| [[LoVo (line)]] | wt | 59.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.31× (z +8.5) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 49.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 85.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.166× (z -8.5) |
| [[PANC-1 (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.65× (z +9.4) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL]] | +0.71 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[RASA4B]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[HCN2]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[CLIP2]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NAB2]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[NCKAP5L]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RALY]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D10A]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RTN2]] | +0.59 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SMOX]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ECE1]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11FIP2]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[QRSL1]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[VRK2]] | -0.54 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[DERA]] | -0.54 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[TRUB1]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[DIS3L]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[FAIM]] | -0.52 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[RNASEH2B]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MTHFSD]] | -0.51 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[VPS36]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TADA2A]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRARP]] | B | NRARP activity lowers TGFB1's level | lines that do not express NRARP (14) vs lines expressing it (36) | 2.36× higher at baseline in the lines without NRARP | 0.011 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[BICDL1]] | B | BICDL1 activity lowers TGFB1's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.98× higher at baseline in the lines without BICDL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[ZCCHC24]] | B | ZCCHC24 activity raises TGFB1's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without ZCCHC24 | 0.022 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[COL6A2]] | B | COL6A2 activity raises TGFB1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.77× lower at baseline in the lines without COL6A2 | 0.030 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[MRC2]] | B | MRC2 activity raises TGFB1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 2.38× lower at baseline in the lines without MRC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[COL7A1]] | B | COL7A1 activity raises TGFB1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without COL7A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[TSHZ3]] | B | TSHZ3 activity raises TGFB1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without TSHZ3 | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[COL5A3]] | B | COL5A3 activity raises TGFB1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without COL5A3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[TSPAN4]] | B | TSPAN4 activity raises TGFB1's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 2.79× lower at baseline in the lines without TSPAN4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[NRARP]] | B | NRARP activity weakens TGFB1's drug response | lines that do not express NRARP (12) vs lines expressing it (28) | the lines without NRARP respond 1.29× as strongly (z diff -0.79); strongest at Topotecan (hydrochloride) 5 µM: 0.51x vs 0.87x (z diff -5.2) | 0.073 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A; target measured in part of the lines; both ways; artifact flags |
| [[TNS1]] | B | TNS1 activity raises TGFB1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without TNS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[GFPT2]] | B | GFPT2 activity raises TGFB1's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without GFPT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS3]] | B | TGFB1 activity raises MEIS3's level | lines that do not express TGFB1 (8) vs lines expressing it (42) | 3.70× lower at baseline in the lines without TGFB1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZDHHC2, NUAK1, SLC22A4; maybe low, not absent |
| [[AGAP9]] | B | TGFB1 activity raises AGAP9's level | lines that do not express TGFB1 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without TGFB1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZDHHC2, NUAK1, SLC22A4; maybe low, not absent |
| [[KLF12]] | B | TGFB1 activity raises KLF12's level | lines that do not express TGFB1 (8) vs lines expressing it (42) | 2.94× lower at baseline in the lines without TGFB1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ZDHHC2, NUAK1, SLC22A4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, -4.0); signed map (2.0, 28.0). **Vector** length 127, 38.1% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.3 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.3 | -5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.8 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.0 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,301,587-41,353,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CED, TGFbeta; previously TGFB, DPD1 |
| Gene groups (HGNC) | Transforming growth factor beta family |
| Hallmark sets | TGF_BETA_SIGNALING, IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION, P53_PATHWAY, G2M_CHECKPOINT |
| Reactome | 41 pathways, smallest: Influenza Virus Induced Apoptosis; Loss of Function of TGFBR2 in Cancer; TGFBR2 Kinase Domain Mutants in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P01137](https://www.uniprot.org/uniprotkb/P01137) (Transforming growth factor beta-1 proprotein):

> Transforming growth factor beta-1 proprotein: Precursor of the Latency-associated peptide (LAP) and Transforming growth factor beta-1 (TGF-beta-1) chains, which constitute the regulatory and active subunit of TGF-beta-1, respectively.; [Latency-associated peptide]: Required to maintain the Transforming growth factor beta-1 (TGF-beta-1) chain in a latent state during storage in extracellular matrix. Associates non-covalently with TGF-beta-1 and regulates its activation via interaction with …

**Summary**, from NCBI Gene [7040](https://www.ncbi.nlm.nih.gov/gene/7040):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate a latency-associated peptide (LAP) and a mature peptide, and is found in either a latent form composed of a mature peptide homodimer, a LAP homodimer, and a …

**Accessions** — [HGNC:11766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11766) · Entrez [7040](https://www.ncbi.nlm.nih.gov/gene/7040) · UniProt [P01137](https://www.uniprot.org/uniprotkb/P01137) · Ensembl [ENSG00000105329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105329)

## Data

Gene col 2584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2584); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2584]; `tensor/DDL_lfc|DDL_z.npy` [2584]; `embed/gene_vectors.npy` [2584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2584 or target_col == 2584). Every well: [[TGFB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
