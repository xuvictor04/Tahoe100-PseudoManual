---
symbol: "KAT5"
type: "gene"
col: 10324
ensembl_id: "ENSG00000172977"
name: "lysine acetyltransferase 5"
location: "11q13.1"
module: 16
arm: "+"
pooled_cpm: 18.44
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# KAT5

*lysine acetyltransferase 5* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +12.0, q 3e-30, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.31× (z +11.9, q 3e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.396× (z -24.9, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YJU2]] (+0.75, fdr 7e-06), [[ZNF414]] (+0.74, fdr 7e-06), [[EPC1]] (+0.72, fdr 7e-06); moves opposite to [[MTFR1]] (-0.61, fdr 1e-05), [[PLEKHA8]] (-0.60, fdr 1e-05), [[METTL21A]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.56×** | +12.0 | 3e-30 | 37/47 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.31×** | +11.9 | 3e-30 | 42/48 (SW480, RKO, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +9.6 | 1e-19 | 37/44 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.66×** | +9.2 | 4e-18 | 37/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.44×** | +7.0 | 4e-10 | 28/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 2e-07 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.6 | 1e-06 | 3/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.006 | 12/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.050 | 12/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.080 | 10/44 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | 1.18× | +3.2 | 0.080 | 12/44 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.11 | 15/46 (NCI-H460, RKO, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.396×** | -24.9 | 0e+00 | 44/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.434×** | -15.9 | 0e+00 | 44/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.438×** | -15.1 | 0e+00 | 40/46 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.456×** | -14.9 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -13.8 | 2e-41 | 36/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.505×** | -13.0 | 2e-36 | 42/48 (NCI-H2347, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.511×** | -12.8 | 2e-35 | 41/48 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -11.7 | 9e-30 | 24/32 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.581×** | -10.3 | 4e-23 | 39/47 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.619×** | -9.1 | 5e-18 | 25/41 (SHP-77, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.745×** | -7.9 | 1e-13 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.475×** | -7.4 | 7e-12 | 32/48 (hTERT-HPNE, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.5 | 4e-09 | 25/48 (A-427, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.759×** | -5.2 | 7e-06 | 21/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.759×** | -4.8 | 5e-05 | 16/36 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.05 µM |  | **0.833×** | -3.5 | 0.019 | 7/47 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.025 | 12/47 (NCI-H661, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.071 | 7/46 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.6 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -12.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.319× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 13.2 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +13.4) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -13.9) |
| [[SW480 (line)]] | alt | 21.9 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 6.07× (z +9.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -17.2) |
| [[A549 (line)]] | wt | 16.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.3) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 19.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 3 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.113× (z -10.1) |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.3) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -17.2) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.190× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -13.0) |
| [[LoVo (line)]] | wt | 13.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.8) |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0715× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -11.8) |
| [[RKO (line)]] | wt | 15.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.4) ⚠ cell-cycle shift, explains ~41% of this change | [[Belinostat (drug)]] 0.5 µM 0.198× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -15.8) |
| [[SHP-77 (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -13.6) |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.7) |
| [[A-427 (line)]] | wt | 20.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.398× (z -8.5) |
| [[A498 (line)]] | wt | 10.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.273× (z -8.6) |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -10.4) |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -10.5) |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.3) |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0870× (z -11.2) |
| [[KATO III (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -9.0) |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -14.9) |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -12.0) |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YJU2]] | +0.75 | +0.77 / +0.80 | both halves | 7e-06 |  |
| [[ZNF414]] | +0.74 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[EPC1]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 997 |
| [[ZNF180]] | +0.69 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIL1]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[RNF40]] | +0.68 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZSWIM1]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MCRS1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 942 |
| [[PEX12]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTFR1]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[METTL21A]] | -0.59 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[MFN1]] | -0.59 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[PIGF]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[SRD5A1]] | -0.57 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[HPRT1]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KAT5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF793]] | B | ZNF793 activity raises KAT5's level | lines that do not express ZNF793 (22) vs lines expressing it (28) | 1.07× lower at baseline in the lines without ZNF793 | 0.088 | ⚠ within organs, on part of the lines; also absent: PEG10, MAP6, ZNF570 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.2, 9.1); signed map (-0.6, -24.5). **Vector** length 87.2, 18.9% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +9.2 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.7 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.1 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.6 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -15.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -24.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,711,996-65,719,604 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIP60, PLIP, cPLA2, HTATIP1, ESA1; previously HTATIP |
| Gene groups (HGNC) | MYST type domain containing lysine acetyltransferases; Tip60/Nua4 histone acetyltransferase complex subunits; Zinc fingers MYST C2HC-type |
| Reactome | 46 pathways, smallest: Sensing of DNA Double Strand Breaks; Cardiogenesis; Impaired BRCA2 binding to PALB2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92993](https://www.uniprot.org/uniprotkb/Q92993) (Histone acetyltransferase KAT5):

> Catalytic subunit of the NuA4 histone acetyltransferase complex, a multiprotein complex involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H2A and H4. Histone acetylation alters nucleosome-DNA interactions and promotes interaction of the modified histones with other proteins which positively regulate transcription. The NuA4 histone acetyltransferase complex is required for the activation of transcriptional programs associated with …

**Summary**, from NCBI Gene [10524](https://www.ncbi.nlm.nih.gov/gene/10524):

> The protein encoded by this gene belongs to the MYST family of histone acetyl transferases (HATs) and was originally isolated as an HIV-1 TAT-interactive protein. HATs play important roles in regulating chromatin remodeling, transcription and other nuclear processes by acetylating histone and nonhistone proteins. This protein is a histone acetylase that has a role in DNA repair and apoptosis and is thought to play an important role in signal transduction. Alternative splicing of this gene …

**Accessions** — [HGNC:5275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5275) · Entrez [10524](https://www.ncbi.nlm.nih.gov/gene/10524) · UniProt [Q92993](https://www.uniprot.org/uniprotkb/Q92993) · Ensembl [ENSG00000172977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172977)

## Data

Gene col 10324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10324); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10324]; `tensor/DDL_lfc|DDL_z.npy` [10324]; `embed/gene_vectors.npy` [10324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10324 or target_col == 10324). Every well: [[KAT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
