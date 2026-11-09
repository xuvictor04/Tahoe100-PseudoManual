---
symbol: "RUBCN"
type: "gene"
col: 6951
ensembl_id: "ENSG00000145016"
name: "rubicon autophagy regulator"
location: "3q29"
module: 2
arm: "+"
pooled_cpm: 48.93
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RUBCN

*rubicon autophagy regulator* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +26.8, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.736× (z -10.4, q 1e-22, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.0833×, AsPC-1 0.315×, HS-578T 0.336×, PANC-1 0.426×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.1000×, Panc 03.27 0.241×, MIA PaCa-2 0.238×, AsPC-1 0.306×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change); [[Selinexor (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.467×, A549 0.432×, NCI-H460 0.561×); [[Delamanid (drug)]] 0.5 µM in 1 line (AN3 CA 0.145×); [[NVP-BHG712 (drug)]] 0.5 µM in 1 line (NCI-H661 0.0573×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORMDL2]] (+0.67, fdr 7e-06), [[KLC1]] (+0.64, fdr 7e-06), [[WDR44]] (+0.60, fdr 1e-05); moves opposite to [[CHIC1]] (-0.60, fdr 8e-05), [[DHRS4L2]] (-0.59, fdr 2e-05), [[NDUFA5]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PDE4D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +26.8 | 0e+00 | 44/49 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +17.2 | 0e+00 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +16.2 | 0e+00 | 43/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +15.4 | 0e+00 | 44/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +13.3 | 2e-38 | 41/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.4 | 4e-19 | 33/49 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +7.6 | 3e-12 | 36/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +6.6 | 3e-09 | 28/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.30×** | +6.2 | 3e-08 | 25/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +6.2 | 4e-08 | 29/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.9 | 2e-07 | 23/48 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.27×** | +5.4 | 3e-06 | 20/48 (H4, KATO III, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +4.6 | 1e-04 | 16/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.20×** | +4.3 | 6e-04 | 13/48 (H4, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.2 | 0.001 | 11/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.1 | 0.001 | 12/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.004 | 12/48 (HT-29, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.0833×, AsPC-1 0.315×, HS-578T 0.336×, PANC-1 0.426×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.1000×, Panc 03.27 0.241×, MIA PaCa-2 0.238×, AsPC-1 0.306×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change); [[Selinexor (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.467×, A549 0.432×, NCI-H460 0.561×); [[Delamanid (drug)]] 0.5 µM in 1 line (AN3 CA 0.145×); [[NVP-BHG712 (drug)]] 0.5 µM in 1 line (NCI-H661 0.0573×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.736×** | -10.4 | 1e-22 | 33/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -10.3 | 2e-22 | 32/48 (A-427, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -7.6 | 8e-12 | 24/42 (SK-MEL-2, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.788×** | -5.7 | 1e-06 | 24/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | 0.841× | -4.0 | 0.006 | 15/48 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.844× | -4.0 | 0.007 | 19/40 (A549, Panc 03.27, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | 0.853× | -3.8 | 0.010 | 17/47 (A-172, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Pentoxifylline (drug)]] 0.05 µM | ⚠ transcription drop | 0.875× | -3.2 | 0.083 | 8/48 (SW 1088, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 33.2 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[NCI-H460 (line)]] | wt | 27.9 | 4 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.561× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 74.5 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.467× (z -10.5) |
| [[SW480 (line)]] | alt | 62.1 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 58.4 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.56× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 37.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +18.2) | — |
| [[LS 180 (line)]] | wt | 35.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +14.1) | — |
| [[A-427 (line)]] | wt | 65.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0833× (z -26.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 51.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 77.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[PANC-1 (line)]] | alt | 65.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 43.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.432× (z -10.3) |
| [[C32 (line)]] | wt | 24.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +14.7) | — |
| [[H4 (line)]] | wt | 28.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 53.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 74.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +12.2) | — |
| [[A498 (line)]] | wt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +15.5) | — |
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.145× (z -9.3) |
| [[COLO 205 (line)]] | alt | 44.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +13.9) | — |
| [[J82 (line)]] | alt | 53.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.7) | — |
| [[KATO III (line)]] | alt | 59.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 65.1 | 0 | 1 | — | [[NVP-BHG712 (drug)]] 0.5 µM 0.0573× (z -8.9) |
| [[RKO (line)]] | wt | 49.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 47.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 40.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 66.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +14.6) | — |
| [[SW48 (line)]] | wt | 55.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORMDL2]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[KLC1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[WDR44]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 | same gene group |
| [[FBH1]] | +0.57 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[SERINC2]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SLC27A4]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[MROH1]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[KATNBL1]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[UBE2D2]] | +0.54 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[TSPAN17]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ELOVL1]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHIC1]] | -0.60 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[DHRS4L2]] | -0.59 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NDUFA5]] | -0.52 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[BDH2]] | -0.52 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[GNG2]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[ACBD6]] | -0.51 | -0.37 / -0.49 | both halves | 8e-05 | same gene group |
| [[SRSF10]] | -0.50 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[CDC73]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 | same gene group |
| [[PRPF4B]] | -0.49 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ARRB1]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 | same gene group |
| [[CC2D2A]] | -0.49 | -0.25 / -0.52 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4D]] | B | PDE4D activity lowers RUBCN's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.33× higher at baseline in the lines without PDE4D | 0.010 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[GNG2]] | B | GNG2 activity strengthens RUBCN's drug response | lines that do not express GNG2 (22) vs lines expressing it (27) | the lines without GNG2 respond 0.80× as strongly (z diff +0.77); strongest at Panobinostat 0.5 µM: 1.61x vs 2.17x (z diff +1.9) | 0.033 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers RUBCN's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GNG2]] | B | GNG2 activity lowers RUBCN's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 1.27× higher at baseline in the lines without GNG2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.376). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-12.7, -0.3); signed map (-14.5, 17.5). **Vector** length 94.4, 22.6% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +26.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.0 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +3.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.9 | -10.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.4 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | rubicon autophagy regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,668,867-197,749,727 (-) |
| Ensembl biotype | protein_coding |
| Also known as | rubicon, rundataxin; previously KIAA0226 |
| Gene groups (HGNC) | PIK3C3 complex subunits; MicroRNA protein coding host genes; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92622](https://www.uniprot.org/uniprotkb/Q92622) (Run domain Beclin-1-interacting and cysteine-rich domain-containing protein):

> Inhibits PIK3C3 activity; under basal conditions negatively regulates PI3K complex II (PI3KC3-C2) function in autophagy. Negatively regulates endosome maturation and degradative endocytic trafficking and impairs autophagosome maturation process. Can sequester UVRAG from association with a class C Vps complex (possibly the HOPS complex) and negatively regulates Rab7 activation.; Involved in regulation of pathogen-specific host defense of activated macrophages. Following bacterial infection …

**Summary**, from NCBI Gene [9711](https://www.ncbi.nlm.nih.gov/gene/9711):

> The protein encoded by this gene is a negative regulator of autophagy and endocytic trafficking and controls endosome maturation. This protein contains two conserved domains, an N-terminal RUN domain and a C-terminal DUF4206 domain. The RUN domain is involved in Ras-like GTPase signaling, and the DUF4206 domain contains a diacylglycerol (DAG) binding-like motif. Mutation in this gene results in deletion of the DAG binding-like motif and causes a recessive ataxia. Alternatively spliced …

**Accessions** — [HGNC:28991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28991) · Entrez [9711](https://www.ncbi.nlm.nih.gov/gene/9711) · UniProt [Q92622](https://www.uniprot.org/uniprotkb/Q92622) · Ensembl [ENSG00000145016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145016)

## Data

Gene col 6951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6951); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6951]; `tensor/DDL_lfc|DDL_z.npy` [6951]; `embed/gene_vectors.npy` [6951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6951 or target_col == 6951). Every well: [[RUBCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUBCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
