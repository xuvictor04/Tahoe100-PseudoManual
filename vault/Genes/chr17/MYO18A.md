---
symbol: "MYO18A"
type: "gene"
col: 12231
ensembl_id: "ENSG00000196535"
name: "myosin XVIIIA"
location: "17q11.2"
module: 31
arm: "+"
pooled_cpm: 74.22
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MYO18A

*myosin XVIIIA* — 17q11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H1792 8.93×, C32 3.83×, A-427 3.06×, SK-MEL-2 3.97×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 3.33×, SK-MEL-2 4.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 2.43×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.643× (z -7.2, q 4e-10, down in 33 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.755× (z -4.7, q 1e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNM3]] (+0.56, fdr 1e-05), [[EPB41L1]] (+0.55, fdr 1e-05), [[EPS8L2]] (+0.54, fdr 2e-05); moves opposite to [[MECR]] (-0.44, fdr 5e-05), [[MRPS21]] (-0.43, fdr 2e-04), [[ORC5]] (-0.43, fdr 8e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SULF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12231.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H1792 8.93×, C32 3.83×, A-427 3.06×, SK-MEL-2 3.97×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 3.33×, SK-MEL-2 4.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 2.43×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.21× | +3.2 | 0.44 | 17/47 (Hs 766T, A-172, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -7.2 | 4e-10 | 33/46 (RKO, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.700×** | -6.0 | 5e-07 | 33/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.725×** | -5.4 | 1e-05 | 28/48 (LS 180, HT-29, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.733×** | -5.2 | 2e-05 | 29/48 (NCI-H460, SW 1088, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.733×** | -5.2 | 2e-05 | 25/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.749×** | -4.9 | 1e-04 | 25/48 (SW1417, LS 180, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -4.8 | 1e-04 | 29/48 (PANC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.744×** | -4.8 | 1e-04 | 27/48 (BT-474, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.755×** | -4.7 | 1e-04 | 27/48 (MIA PaCa-2, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.759×** | -4.6 | 2e-04 | 21/47 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.623×** | -4.2 | 0.002 | 24/49 (NCI-H1792, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.783×** | -4.1 | 0.002 | 24/48 (NCI-H460, A549, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.777×** | -4.1 | 0.002 | 22/47 (Panc 03.27, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.786×** | -4.0 | 0.002 | 21/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -4.0 | 0.002 | 22/49 (Panc 03.27, SW 900, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.649×** | -3.8 | 0.005 | 19/48 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.012 | 19/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.026 | 15/47 (Panc 03.27, PANC-1, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.701×** | -3.1 | 0.046 | 16/48 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.2 | 0 | 8 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.353× (z -11.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HT-29 (line)]] | alt | 255 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 141 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -12.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 182 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -13.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 39.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.216× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 36.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 77.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1088 (line)]] | alt | 75.5 | 0 | 3 (1 ⚠) | — | [[Rosiglitazone (drug)]] 0.5 µM 0.0663× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.357× (z -10.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 98.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 43.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 94.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -10.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -11.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 94.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.441× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.518× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 78.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -9.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 67.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.449× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -11.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 31.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +26.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[PANC-1 (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.579× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -14.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -9.6) |
| [[SW480 (line)]] | alt | 93.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -11.1) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNM3]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[EPB41L1]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[EPS8L2]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[EVPL]] | +0.53 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[SEMA3B]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PLCD3]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[LAMA5]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ADAP1]] | +0.48 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ANXA11]] | +0.48 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[MICALL2]] | +0.48 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[CHD3]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[MAP1A]] | +0.47 | +0.49 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MECR]] | -0.44 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MRPS21]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ORC5]] | -0.43 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[SNU13]] | -0.42 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SF3B5]] ⚠ | -0.42 | -0.36 / -0.37 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GSTO1]] | -0.41 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[NCBP2AS2]] | -0.40 | -0.21 / -0.44 | both halves | 7e-04 |  |
| [[MFF]] | -0.40 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[PET117]] | -0.40 | -0.20 / -0.49 | both halves | 7e-04 |  |
| [[MRPL15]] | -0.39 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[SMIM3]] | -0.39 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[CNOT10]] | -0.39 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SULF2]] | B | SULF2 activity raises MYO18A's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without SULF2 | 0.007 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[EPS8L2]] | B | EPS8L2 activity raises MYO18A's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without EPS8L2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[ANO1]] | B | ANO1 activity raises MYO18A's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without ANO1 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[SEMA3B]] | B | SEMA3B activity raises MYO18A's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without SEMA3B | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[MISP]] | B | MISP activity raises MYO18A's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without MISP | 0.017 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[MALL]] | B | MALL activity raises MYO18A's level | lines that do not express MALL (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without MALL | 0.019 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[MUC17]] | B | MUC17 activity raises MYO18A's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.03× lower at baseline in the lines without MUC17 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[TNNT2]] | B | TNNT2 activity raises MYO18A's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without TNNT2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[CLU]] | B | CLU activity strengthens MYO18A's drug response | lines that do not express CLU (11) vs lines expressing it (37) | the lines without CLU respond 0.73× as strongly (z diff +0.86); strongest at Digitoxin 5 µM: 0.84x vs 0.59x (z diff +2.8) | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CDC42BPG]] | B | CDC42BPG activity raises MYO18A's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without CDC42BPG | 0.055 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[LAMA5]] | B | LAMA5 activity raises MYO18A's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without LAMA5 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[SULF2]] | B | SULF2 activity strengthens MYO18A's drug response | lines that do not express SULF2 (24) vs lines expressing it (24) | the lines without SULF2 respond 0.60× as strongly (z diff +1.49); strongest at Topotecan (hydrochloride) 5 µM: 0.75x vs 0.49x (z diff +3.7) | 0.072 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.6, 56.3); signed map (57.7, -7.0). **Vector** length 107, 27.8% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.7 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -2.2 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.7 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -4.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.2 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.0 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | myosin XVIIIA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,071,122-29,180,398 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0216, MysPDZ; previously TIAF1 |
| Gene groups (HGNC) | Myosin heavy chains, class XVIII; PDZ domain containing |
| Reactome | 7 pathways, smallest: Signaling by FLT3 fusion proteins; Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95411](https://www.uniprot.org/uniprotkb/O95411) (Putative TGFB1-induced anti-apoptotic factor 1):

> [Isoform TIAF1]: Inhibits the cytotoxic effects of TNF and overexpressed TNF receptor adapters TRADD, FADD, and RIPK1. Involved in TGF-beta1 inhibition of IkappaB-alpha expression and suppression of TNF-mediated IkappaB-alpha degradation.

**Summary**, from NCBI Gene [399687](https://www.ncbi.nlm.nih.gov/gene/399687):

> The protein encoded by this gene can bind GOLPH3, linking the Golgi to the cytoskeleton and influencing Golgi membrane trafficking. The encoded protein is also part of a complex that assembles lamellar actomyosin bundles and may be required for cell migration. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:31104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31104) · Entrez [399687](https://www.ncbi.nlm.nih.gov/gene/399687) · UniProt [O95411](https://www.uniprot.org/uniprotkb/O95411) · Ensembl [ENSG00000196535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196535)

## Data

Gene col 12231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12231); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12231]; `tensor/DDL_lfc|DDL_z.npy` [12231]; `embed/gene_vectors.npy` [12231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12231 or target_col == 12231). Every well: [[MYO18A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO18A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
