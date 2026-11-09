---
symbol: "CPSF3"
type: "gene"
col: 4044
ensembl_id: "ENSG00000119203"
name: "cleavage and polyadenylation specific factor 3"
location: "2p25.1"
module: 5
arm: "+"
pooled_cpm: 37.34
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CPSF3

*cleavage and polyadenylation specific factor 3* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +16.4, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.695× (z -8.0, q 6e-13, down in 28 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.734× (z -6.8, q 2e-09, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.358×, PANC-1 0.456×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.456×, BT-474 0.287×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.466×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAT1]] (+0.73, fdr 7e-06), [[EIF2S1]] (+0.66, fdr 7e-06), [[PARG]] (+0.66, fdr 1e-05); moves opposite to [[KCTD7]] (-0.62, fdr 8e-06), [[SAT2]] (-0.62, fdr 1e-05), [[ELL3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +16.4 | 0e+00 | 39/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.02×** | +15.4 | 0e+00 | 44/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.85×** | +13.5 | 2e-39 | 44/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.77×** | +12.5 | 1e-33 | 39/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.64×** | +10.5 | 1e-23 | 34/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.57×** | +9.6 | 1e-19 | 23/40 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +9.4 | 5e-19 | 31/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +9.4 | 6e-19 | 34/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +9.1 | 5e-18 | 34/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.53×** | +9.0 | 1e-17 | 31/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.49×** | +8.7 | 1e-16 | 30/44 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.33×** | +6.2 | 3e-08 | 21/47 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.34×** | +6.2 | 3e-08 | 23/46 (HCT15, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +6.0 | 6e-08 | 23/48 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 4e-07 | 21/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 3e-06 | 22/48 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.9 | 3e-05 | 17/48 (LS 180, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.003 | 19/47 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.027 | 7/48 (A498, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.11× | +3.2 | 0.030 | 3/48 (SNU-1, HCT15, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.038 | 8/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.053 | 6/48 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.053 | 6/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.054 | 8/47 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.15× | +2.9 | 0.075 | 9/48 (PANC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4044.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.358×, PANC-1 0.456×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.456×, BT-474 0.287×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.466×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -8.0 | 6e-13 | 28/47 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.734×** | -6.8 | 2e-09 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -5.6 | 4e-06 | 3/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.8 | 0.025 | 18/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.069 | 12/48 (NCI-H2030, A-172, …) | two highest doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.900× | -3.3 | 0.089 | 4/48 (SW 1271, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.1 | 0.11 | 19/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.906× | -3.1 | 0.11 | 2/48 (MIA PaCa-2, BT-474) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.865× | -3.1 | 0.11 | 7/48 (SW1417, HOP62, …) | rises with dose | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.11 | 6/48 (C-33 A, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 44.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 57.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.456× (z -11.3) |
| [[BT-474 (line)]] | alt | 31.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.287× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 37.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -11.9) |
| [[SW480 (line)]] | alt | 51.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +11.0) | — |
| [[A-427 (line)]] | wt | 74.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.466× (z -8.9) |
| [[A498 (line)]] | wt | 47.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HT-29 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | — |
| [[NCI-H23 (line)]] | alt | 73.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.458× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | — |
| [[RKO (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW 900 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[SW1417 (line)]] | alt | 39.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.5) | — |
| [[A-172 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT1]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PARG]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[GEN1]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ALG8]] | +0.64 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[GTF2E1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ZNF623]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MAPKAP1]] | +0.64 | +0.73 / +0.48 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions |
| [[PPIL1]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[RUVBL1]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.62 | +0.71 / +0.66 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[HASPIN]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD7]] | -0.62 | -0.70 / -0.58 | both halves | 8e-06 |  |
| [[SAT2]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ELL3]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[OAZ1]] | -0.59 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[ARMCX3]] | -0.58 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[SIRT2]] | -0.58 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[CSKMT]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TOM1]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[BEX2]] | -0.55 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[GLMP]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SNHG7]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SNN]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPSF3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEMP2]] | B | NEMP2 activity raises CPSF3's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without NEMP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.9, -33.3); signed map (-6.0, -39.8). **Vector** length 84.3, 18.4% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cleavage and polyadenylation specific factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,423,651-9,473,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPSF-73, CPSF73, YSH1 |
| Gene groups (HGNC) | Cleavage and polyadenylation specific factor subunits; MBL fold containing DNA/RNA interacting subfamily; Endoribonucleases |
| Reactome | 13 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKF6](https://www.uniprot.org/uniprotkb/Q9UKF6) (Cleavage and polyadenylation specificity factor subunit 3):

> Component of the cleavage and polyadenylation specificity factor (CPSF) complex that plays a key role in pre-mRNA 3'-end formation, recognizing the AAUAAA signal sequence and interacting with poly(A) polymerase and other factors to bring about cleavage and poly(A) addition. Has endonuclease activity, and functions as an mRNA 3'-end-processing endonuclease. Also involved in the histone 3'-end pre-mRNA processing. U7 snRNP-dependent protein that induces both the 3'-endoribonucleolytic cleavage of …

**Summary**, from NCBI Gene [51692](https://www.ncbi.nlm.nih.gov/gene/51692):

> This gene encodes a member of the metallo-beta-lactamase family. The encoded protein is a 73kDa subunit of the cleavage and polyadenylation specificity factor and functions as an endonuclease that recognizes the pre-mRNA 3'-cleavage site AAUAAA prior to polyadenylation. It also cleaves after the pre-mRNA sequence ACCCA during histone 3'-end pre-mRNA processing. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:2326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2326) · Entrez [51692](https://www.ncbi.nlm.nih.gov/gene/51692) · UniProt [Q9UKF6](https://www.uniprot.org/uniprotkb/Q9UKF6) · Ensembl [ENSG00000119203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119203)

## Data

Gene col 4044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4044); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4044]; `tensor/DDL_lfc|DDL_z.npy` [4044]; `embed/gene_vectors.npy` [4044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4044 or target_col == 4044). Every well: [[CPSF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPSF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
