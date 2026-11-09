---
symbol: "TAGLN2"
type: "gene"
col: 8182
ensembl_id: "ENSG00000158710"
name: "transgelin 2"
location: "1q23.2"
module: 111
arm: "+"
pooled_cpm: 152.7
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# TAGLN2

*transgelin 2* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.54× (z +14.6, q 1e-45, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H23 5.75×, NCI-H1573 9.76×, PANC-1 5.59×, A498 4.07×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.97×, A498 3.62×, NCI-H1573 6.65×, KATO III 4.39×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.570× (z -6.1, q 6e-07, down in 36 of 44 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.760× (z -4.5, q 0.001, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD151]] (+0.67, fdr 7e-06), [[BSG]] (+0.61, fdr 1e-05), [[GPAA1]] (+0.59, fdr 1e-05); moves opposite to [[DNAJC2]] (-0.62, fdr 8e-06), [[ZNF500]] (-0.58, fdr 1e-05), [[ZFYVE9]] (-0.58, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PRSS23]] → it (grade B ⚠); 1 goes from it, the strongest it → [[S100A6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H23 5.75×, NCI-H1573 9.76×, PANC-1 5.59×, A498 4.07×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.97×, A498 3.62×, NCI-H1573 6.65×, KATO III 4.39×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.54×** | +14.6 | 1e-45 | 44/45 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.69×** | +11.0 | 1e-25 | 39/40 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +8.8 | 3e-16 | 39/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **1.50×** | +4.6 | 5e-04 | 34/44 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.40×** | +3.8 | 0.013 | 32/44 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.31× | +3.1 | 0.20 | 25/44 (PANC-1, NCI-H23, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.570×** | -6.1 | 6e-07 | 36/44 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.663×** | -4.7 | 6e-04 | 36/44 (HOP62, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.760×** | -4.5 | 0.001 | 22/44 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.687×** | -4.3 | 0.002 | 27/44 (HepG2/C3A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.493×** | -4.3 | 0.002 | 26/41 (A498, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.796×** | -3.7 | 0.018 | 24/44 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.023 | 24/44 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.737×** | -3.5 | 0.032 | 31/44 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.761× | -3.1 | 0.10 | 29/44 (CFPAC-1, Hs 766T, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.607× | -3.0 | 0.15 | 28/45 (AsPC-1, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 243 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Bortezomib (drug)]] 0.05 µM 0.313× (z -10.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 82.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 172 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.79× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Bortezomib (drug)]] 0.05 µM 0.370× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 275 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 141 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 52.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 39.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 200 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 190 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.4) ⚠ cell-cycle shift, explains ~5% of this change | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 92.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 194 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Bortezomib (drug)]] 0.05 µM 0.359× (z -9.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[COLO 205 (line)]] | alt | 90.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.9) |
| [[H4 (line)]] | wt | 188 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.0) |
| [[Hs 766T (line)]] | wt | 288 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.3) |
| [[HS-578T (line)]] | alt | 247 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 66.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 251 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 49.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 74.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 77.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.8) |
| [[A-172 (line)]] | wt | 494 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.368× (z -9.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 536 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 276 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.1) |
| [[J82 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.0) |
| [[SW 1088 (line)]] | alt | 241 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.127× (z -9.2) |
| [[SW 900 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 68.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW48 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 186 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD151]] | +0.67 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[BSG]] | +0.61 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[GPAA1]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[S100A4]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 | STRING 426 |
| [[CFL1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 716 |
| [[TMSB4X]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 475 |
| [[CAV2]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ECE1]] | +0.57 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PLP2]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[H2AZ2]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[YWHAZ]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 577 |
| [[PKM]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.62 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[ZNF500]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ZFYVE9]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NSA2]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[EIF2S2]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[NDUFB9]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZNF581]] | -0.52 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ZFAND2A]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[GAS5]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[C19orf12]] | -0.51 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | PRSS23 activity raises TAGLN2's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.91× lower at baseline in the lines without PRSS23 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises TAGLN2's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.98× lower at baseline in the lines without SMAD3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[ARHGDIB]] | B | ARHGDIB activity raises TAGLN2's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without ARHGDIB | 0.045 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[NRP2]] | B | NRP2 activity raises TAGLN2's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without NRP2 | 0.063 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[HDAC6]] | B | HDAC6 activity raises TAGLN2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TAGLN2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CAV2]] | B | CAV2 activity raises TAGLN2's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without CAV2 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent |
| [[TMSB4X]] | B | TMSB4X activity raises TAGLN2's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 2.12× lower at baseline in the lines without TMSB4X | 0.092 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |
| [[S100A6]] | C | S100A6 activity raises TAGLN2's level | lines that do not express S100A6 (5) vs lines expressing it (45) | 4.12× lower at baseline in the lines without S100A6 | 0.060 | ⚠ within organs, on part of the lines; also absent: GPRC5D-AS1, HLA-H, PRRG1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A6]] | C | TAGLN2 activity raises S100A6's level | lines that do not express TAGLN2 (4) vs lines expressing it (46) | 3.85× lower at baseline in the lines without TAGLN2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PPP4R1L, FSTL3, BIRC3; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.7, -4.1); signed map (12.6, 23.5). **Vector** length 110, 39.8% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +4.2 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +1.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -7.1 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.7 | -4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -4.3 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | transgelin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:159,918,107-159,925,507 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0120, HA1756 |
| Gene groups (HGNC) | Transgelin family |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

UniProt [P37802](https://www.uniprot.org/uniprotkb/P37802) carries no function annotation.

**Summary**, from NCBI Gene [8407](https://www.ncbi.nlm.nih.gov/gene/8407):

> The protein encoded by this gene is similar to the protein transgelin, which is one of the earliest markers of differentiated smooth muscle. The specific function of this protein has not yet been determined, although it is thought to be a tumor suppressor. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:11554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11554) · Entrez [8407](https://www.ncbi.nlm.nih.gov/gene/8407) · UniProt [P37802](https://www.uniprot.org/uniprotkb/P37802) · Ensembl [ENSG00000158710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158710)

## Data

Gene col 8182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8182); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8182]; `tensor/DDL_lfc|DDL_z.npy` [8182]; `embed/gene_vectors.npy` [8182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8182 or target_col == 8182). Every well: [[TAGLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAGLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
