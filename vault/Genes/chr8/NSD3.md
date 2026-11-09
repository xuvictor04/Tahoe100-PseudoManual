---
symbol: "NSD3"
type: "gene"
col: 7198
ensembl_id: "ENSG00000147548"
name: "nuclear receptor binding SET domain protein 3"
location: "8p11.23"
module: 130
arm: "+"
pooled_cpm: 182.14
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# NSD3

*nuclear receptor binding SET domain protein 3* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +10.7, q 5e-24, up in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (MIA PaCa-2 1.69×, AsPC-1 1.69×, NCI-H1573 1.77×, PANC-1 1.49×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (RPMI-7951 2.32×, NCI-H460 1.50×, A549 1.64×, NCI-H1792 1.71×, …; ⚠ cell-cycle shift, explains ~11% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 2.24×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.583× (z -17.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP57]] (+0.67, fdr 7e-06), [[SOS1]] (+0.58, fdr 1e-05), [[TCEANC2]] (+0.57, fdr 5e-05); moves opposite to [[FAAP100]] (-0.54, fdr 2e-05), [[ARFRP1]] (-0.54, fdr 1e-05), [[ARHGDIA]] (-0.54, fdr 3e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AP1S3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (MIA PaCa-2 1.69×, AsPC-1 1.69×, NCI-H1573 1.77×, PANC-1 1.49×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (RPMI-7951 2.32×, NCI-H460 1.50×, A549 1.64×, NCI-H1792 1.71×, …; ⚠ cell-cycle shift, explains ~11% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 2.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +10.7 | 5e-24 | 28/49 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +4.1 | 0.011 | 10/48 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.08× | +3.4 | 0.11 | 4/48 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.20 | 2/49 (HT-29, SNU-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -17.7 | 0e+00 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -17.2 | 0e+00 | 47/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -11.9 | 2e-30 | 42/48 (AsPC-1, H4, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -11.2 | 4e-27 | 41/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.755×** | -8.9 | 9e-17 | 33/48 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.783×** | -8.0 | 8e-14 | 31/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.759×** | -8.0 | 1e-13 | 29/48 (AsPC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.775×** | -7.7 | 9e-13 | 29/45 (H4, AN3 CA, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -6.7 | 1e-09 | 18/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.821×** | -6.5 | 6e-09 | 26/49 (SHP-77, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.816×** | -6.4 | 8e-09 | 23/44 (SK-MEL-2, SNU-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.839× | -5.8 | 4e-07 | 20/48 (A-427, A498, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -5.5 | 2e-06 | 21/48 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.846× | -5.5 | 2e-06 | 15/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.896× | -5.1 | 1e-05 | 19/48 (A-427, AsPC-1, …) | all doses, flat | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.822×** | -4.6 | 2e-04 | 24/48 (NCI-H1792, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.833×** | -4.3 | 6e-04 | 19/48 (SW 1271, Panc 03.27, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.785×** | -4.1 | 0.001 | 19/47 (RPMI-7951, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.006 | 20/49 (J82, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.857× | -3.6 | 0.008 | 12/48 (SK-MEL-2, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.009 | 19/46 (Panc 03.27, NCI-H460, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 205 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.385× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 106 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +11.5) | [[Harringtonine (drug)]] 0.5 µM 0.408× (z -12.8) |
| [[HS-578T (line)]] | alt | 243 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.9) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 5 µM 0.478× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 231 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.536× (z -10.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 151 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +12.7) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 5 µM 0.531× (z -13.7) |
| [[SHP-77 (line)]] | alt | 294 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.573× (z -10.2) |
| [[A-427 (line)]] | wt | 188 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -14.4) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.563× (z -10.0) |
| [[A549 (line)]] | wt | 163 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.6) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 0.5 µM 0.546× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.455× (z -12.1) |
| [[SW480 (line)]] | alt | 207 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -14.4) |
| [[Hs 766T (line)]] | wt | 197 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -12.1) |
| [[HT-29 (line)]] | alt | 99.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.510× (z -9.2) |
| [[KATO III (line)]] | alt | 229 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.572× (z -10.4) |
| [[LoVo (line)]] | wt | 188 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.564× (z -9.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.593× (z -9.3) |
| [[LS 180 (line)]] | wt | 217 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.482× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 195 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.5) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 5 µM 0.408× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 201 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.518× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 196 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.3) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +11.0) | — |
| [[A498 (line)]] | wt | 163 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.541× (z -13.2) |
| [[H4 (line)]] | wt | 216 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.480× (z -10.5) |
| [[J82 (line)]] | alt | 272 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.547× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 195 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.566× (z -8.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 170 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.498× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 283 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.553× (z -11.0) |
| [[SW 900 (line)]] | alt | 163 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -11.4) |
| [[AN3 CA (line)]] | alt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[BT-474 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.617× (z -8.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[C-33 A (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.476× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[C32 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.449× (z -10.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 160 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.594× (z -8.5) |
| [[COLO 205 (line)]] | alt | 188 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 199 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.534× (z -12.9) |
| [[HOP62 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.397× (z -8.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.485× (z -8.8) |
| [[PANC-1 (line)]] | alt | 78.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.593× (z -8.9) |
| [[SNU-1 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 253 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 165 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 268 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP57]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SOS1]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TCEANC2]] | +0.57 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[CNOT6L]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[HSPA14]] | +0.57 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[EMSY]] | +0.55 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[METTL4]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ZNF248]] | +0.53 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[YY1]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TTC9C]] | +0.52 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZCCHC8]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[LIN54]] | +0.51 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAP100]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ARFRP1]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ARHGDIA]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ODC1]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TMEM177]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZMIZ2]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[PSEN2]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[POLM]] | -0.52 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[GGACT]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[SRRD]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP1S3]] | C | AP1S3 activity strengthens NSD3's drug response | lines that do not express AP1S3 (4) vs lines expressing it (45) | the lines without AP1S3 respond 0.95× as strongly (z diff +0.68); strongest at Belinostat 5 µM: 0.85x vs 0.68x (z diff +3.5) | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.4, -28.9); signed map (4.6, 3.1). **Vector** length 126, 38.2% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.4 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.9 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -17.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor binding SET domain protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,269,704-38,382,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20353, WHISTLE, KMT3F; previously WHSC1L1 |
| Gene groups (HGNC) | PHD finger proteins; Histone lysine methyltransferases; PWWP domain containing; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZ95](https://www.uniprot.org/uniprotkb/Q9BZ95) (Histone-lysine N-methyltransferase NSD3):

> Histone methyltransferase. Preferentially dimethylates 'Lys-4' and 'Lys-27' of histone H3 forming H3K4me2 and H3K27me2. H3 'Lys-4' methylation represents a specific tag for epigenetic transcriptional activation, while 'Lys-27' is a mark for transcriptional repression.

**Summary**, from NCBI Gene [54904](https://www.ncbi.nlm.nih.gov/gene/54904):

> This gene is related to the Wolf-Hirschhorn syndrome candidate-1 gene and encodes a protein with PWWP (proline-tryptophan-tryptophan-proline) domains. This protein methylates histone H3 at lysine residues 4 and 27, which represses gene transcription. Two alternatively spliced variants have been described. [provided by RefSeq, May 2015]

**Accessions** — [HGNC:12767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12767) · Entrez [54904](https://www.ncbi.nlm.nih.gov/gene/54904) · UniProt [Q9BZ95](https://www.uniprot.org/uniprotkb/Q9BZ95) · Ensembl [ENSG00000147548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147548)

## Data

Gene col 7198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7198); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7198]; `tensor/DDL_lfc|DDL_z.npy` [7198]; `embed/gene_vectors.npy` [7198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7198 or target_col == 7198). Every well: [[NSD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
