---
symbol: "KITLG"
type: "gene"
col: 543
ensembl_id: "ENSG00000049130"
name: "KIT ligand"
location: "12q21.32"
module: 66
arm: "+"
pooled_cpm: 39.05
n_lines_expressing: 40
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 21
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# KITLG

*KIT ligand* — 12q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.15× (z +17.5, q 0e+00, up in 30 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Sunitinib (drug)]] 5 µM: 0.635× (z -4.9, q 4e-04, down in 22 of 37 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.0663×, LS 180 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.226×, A-172 0.169×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.267×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.132×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD12]] (+0.61, fdr 7e-06), [[PLK2]] (+0.60, fdr 1e-05), [[DSEL]] (+0.59, fdr 1e-05); moves opposite to [[PPOX]] (-0.49, fdr 1e-04), [[ZNF500]] (-0.49, fdr 6e-05), [[STARD3]] (-0.49, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SCIN]] → it (grade B ⚠); 21 go from it, the strongest it → [[PIKFYVE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.15×** | +17.5 | 0e+00 | 30/38 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.95×** | +11.2 | 9e-27 | 29/38 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.48×** | +9.8 | 2e-20 | 25/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.40×** | +9.5 | 5e-19 | 27/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +9.2 | 3e-18 | 30/38 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +8.9 | 4e-17 | 31/38 (LoVo, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.09×** | +8.0 | 1e-13 | 24/38 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +7.1 | 1e-10 | 28/38 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.90×** | +6.9 | 3e-10 | 26/38 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.51×** | +6.2 | 2e-08 | 19/38 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.0 | 1e-07 | 25/38 (A549, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +5.8 | 3e-07 | 24/38 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +5.8 | 3e-07 | 21/38 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.64×** | +5.4 | 4e-06 | 25/38 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.61×** | +5.1 | 1e-05 | 24/37 (A549, NCI-H460, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.7 | 1e-04 | 22/38 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +4.6 | 1e-04 | 21/39 (NCI-H1573, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.3 | 5e-04 | 19/37 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.51×** | +4.2 | 8e-04 | 21/38 (SW48, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 9e-04 | 19/37 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.001 | 15/38 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.003 | 17/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +3.5 | 0.010 | 17/38 (BT-474, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.0663×, LS 180 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.226×, A-172 0.169×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.267×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.635×** | -4.9 | 4e-04 | 22/37 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.806× | -3.3 | 0.25 | 18/39 (SHP-77, NCI-H2347, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.756× | -3.0 | 0.43 | 16/35 (Hs 766T, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.2 | 19 (12 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.0× (z +16.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.92× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 19.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0663× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.267× (z -9.9) |
| [[A498 (line)]] | wt | 34.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +15.1) | — |
| [[HEC-1-A (line)]] | alt | 50.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.0) | — |
| [[LoVo (line)]] | wt | 111 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +11.5) | — |
| [[SW480 (line)]] | alt | 10.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +14.7) | — |
| [[A549 (line)]] | wt | 17.6 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 32.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +17.2) | — |
| [[C32 (line)]] | wt | 13.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +16.2) | — |
| [[COLO 205 (line)]] | alt | 45.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 184 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 23.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 31.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.2) | — |
| [[A-172 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 66.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 28.7× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 44.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD12]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PLK2]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DSEL]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TLE4]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FAT1]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[CDC42EP3]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[RASEF]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[FHL2]] | +0.52 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[LTBP1]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[NETO2]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ABCA13]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CDH6]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPOX]] | -0.49 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ZNF500]] | -0.49 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[STARD3]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.48 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[GPR107]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[RAB18]] | -0.48 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PIKFYVE]] | -0.47 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[ZNF836]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[FRG1HP]] | -0.45 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[OXNAD1]] | -0.45 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[SHARPIN]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[IFI27L1]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCIN]] | B | SCIN activity raises KITLG's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without SCIN | 0.013 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[PLCL2]] | B | PLCL2 activity raises KITLG's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without PLCL2 | 0.051 | ⚠ within organs, on part of the lines |
| [[LRATD1]] | B | LRATD1 activity raises KITLG's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without LRATD1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495 |
| [[ABCA12]] | B | ABCA12 activity raises KITLG's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without ABCA12 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |
| [[LTBP1]] | B | LTBP1 activity raises KITLG's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without LTBP1 | 0.097 | ⚠ within organs, on part of the lines |
| [[SH3RF1]] | C | SH3RF1 activity raises KITLG's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 5.31× lower at baseline in the lines without SH3RF1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[AHR]] | C | AHR activity raises KITLG's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.93× lower at baseline in the lines without AHR | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39; co-absent with the target |
| [[DUSP10]] | C | DUSP10 activity raises KITLG's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without DUSP10 | 0.072 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent; co-absent with the target |
| [[TLE4]] | C | TLE4 activity raises KITLG's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.96× lower at baseline in the lines without TLE4 | 0.082 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIKFYVE]] | B | KITLG activity lowers PIKFYVE's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.31× higher at baseline in the lines without KITLG | 0.008 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[STON2]] | B | KITLG activity raises STON2's level | lines that do not express KITLG (10) vs lines expressing it (40) | 3.59× lower at baseline in the lines without KITLG | 0.012 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[PMAIP1]] | B | KITLG activity raises PMAIP1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without KITLG | 0.013 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[SH3RF1]] | B | KITLG activity raises SH3RF1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without KITLG | 0.017 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[VCAN]] | B | KITLG activity raises VCAN's level | lines that do not express KITLG (10) vs lines expressing it (40) | 4.31× lower at baseline in the lines without KITLG | 0.034 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[FAT1]] | B | KITLG activity raises FAT1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without KITLG | 0.040 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[PTPRK]] | B | KITLG activity raises PTPRK's level | lines that do not express KITLG (10) vs lines expressing it (40) | 3.24× lower at baseline in the lines without KITLG | 0.042 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[CEMIP2]] | B | KITLG activity raises CEMIP2's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.41× lower at baseline in the lines without KITLG | 0.049 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | KITLG activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express KITLG (10) vs lines expressing it (38) | the lines without KITLG: 1.23× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[TNFRSF21]] | B | KITLG activity raises TNFRSF21's level | lines that do not express KITLG (10) vs lines expressing it (40) | 3.02× lower at baseline in the lines without KITLG | 0.055 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[ARHGAP42]] | B | KITLG activity raises ARHGAP42's level | lines that do not express KITLG (10) vs lines expressing it (40) | 3.06× lower at baseline in the lines without KITLG | 0.066 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[MBNL1]] | B | KITLG activity raises MBNL1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without KITLG | 0.080 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 18.6); signed map (22.4, 35.9). **Vector** length 115, 31.7% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.7 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.6 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +4.2 |
| fall | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -2.6 | -4.9 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | KIT ligand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.32 — chr12:88,492,793-88,580,851 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCF, SF, Kitl, KL-1, FPH2, SLF, DFNA69; previously MGF |
| Reactome | 15 pathways, smallest: Regulation of KIT signaling; Signaling by SCF-KIT; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P21583](https://www.uniprot.org/uniprotkb/P21583) (Kit ligand):

> Ligand for the receptor-type protein-tyrosine kinase KIT. Plays an essential role in the regulation of cell survival and proliferation, hematopoiesis, stem cell maintenance, gametogenesis, mast cell development, migration and function, and in melanogenesis. KITLG/SCF binding can activate several signaling pathways. Promotes phosphorylation of PIK3R1, the regulatory subunit of phosphatidylinositol 3-kinase, and subsequent activation of the kinase AKT1. KITLG/SCF and KIT also transmit signals via …

**Summary**, from NCBI Gene [4254](https://www.ncbi.nlm.nih.gov/gene/4254):

> This gene encodes the ligand of the tyrosine-kinase receptor encoded by the KIT locus. This ligand is a pleiotropic factor that acts in utero in germ cell and neural cell development, and hematopoiesis, all believed to reflect a role in cell migration. In adults, it functions pleiotropically, while mostly noted for its continued requirement in hematopoiesis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6343) · Entrez [4254](https://www.ncbi.nlm.nih.gov/gene/4254) · UniProt [P21583](https://www.uniprot.org/uniprotkb/P21583) · Ensembl [ENSG00000049130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049130)

## Data

Gene col 543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 543); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 543]; `tensor/DDL_lfc|DDL_z.npy` [543]; `embed/gene_vectors.npy` [543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 543 or target_col == 543). Every well: [[KITLG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KITLG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
