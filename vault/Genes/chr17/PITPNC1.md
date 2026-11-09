---
symbol: "PITPNC1"
type: "gene"
col: 7784
ensembl_id: "ENSG00000154217"
name: "phosphatidylinositol transfer protein cytoplasmic 1"
location: "17q24.2"
module: 174
arm: "+"
pooled_cpm: 434.61
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 73
n_dd_up_clean: 1
n_dd_down_clean: 53
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# PITPNC1

*phosphatidylinositol transfer protein cytoplasmic 1* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.39× (z +4.7, q 0.001, up in 28 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 2.86×, SW480 2.33×, SW48 2.23×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (LOX-IMVI 2.52×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 2.88×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (Hs 766T 2.85×).
> Pooled over the cell lines (median), lowered significantly by 73 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.160× (z -36.1, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPAS2]] (+0.78, fdr 7e-06), [[SPRY4-AS1]] (+0.72, fdr 7e-06), [[HMGA2]] (+0.71, fdr 7e-06); moves opposite to [[MATCAP2]] (-0.51, fdr 1e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7784.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 2.86×, SW480 2.33×, SW48 2.23×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (LOX-IMVI 2.52×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 2.88×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (Hs 766T 2.85×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 0.001 | 28/43 (LOX-IMVI, SW48, …) | two highest doses | low cells (technical?) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.27× | +3.4 | 0.21 | 23/44 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.22 | 26/44 (NCI-H1792, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 74 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 73 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.160×** | -36.1 | 0e+00 | 43/44 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.199×** | -21.7 | 0e+00 | 44/44 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.222×** | -21.0 | 0e+00 | 44/44 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.222×** | -21.0 | 0e+00 | 44/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.252×** | -19.2 | 0e+00 | 42/44 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.271×** | -18.2 | 0e+00 | 42/44 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.293×** | -17.1 | 0e+00 | 44/44 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.297×** | -16.9 | 0e+00 | 44/44 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.396×** | -12.4 | 2e-33 | 36/43 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.456×** | -10.9 | 5e-26 | 41/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -9.8 | 6e-21 | 35/44 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.547×** | -9.7 | 1e-20 | 40/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.497×** | -9.7 | 1e-20 | 39/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.486×** | -9.7 | 2e-20 | 35/43 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.619×** | -9.4 | 2e-19 | 34/44 (C32, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.581×** | -9.2 | 8e-19 | 39/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.494×** | -9.1 | 3e-18 | 41/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.523×** | -9.0 | 6e-18 | 39/45 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.526×** | -8.9 | 1e-17 | 31/44 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.554×** | -8.2 | 6e-15 | 36/44 (HepG2/C3A, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,265 | 0 | 36 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0304× (z -47.6) |
| [[SHP-77 (line)]] | alt | 521 | 0 | 30 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -27.1) |
| [[C32 (line)]] | wt | 1,509 | 0 | 28 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0405× (z -44.8) |
| [[NCI-H1573 (line)]] | alt | 926 | 0 | 28 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0400× (z -44.3) |
| [[hTERT-HPNE (line)]] | wt | 1,290 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -31.3) |
| [[HepG2_C3A (line)]] | wt | 390 | 0 | 21 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -23.5) |
| [[HOP62 (line)]] | alt | 489 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -23.8) |
| [[NCI-H1792 (line)]] | alt | 1,008 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -36.4) |
| [[PANC-1 (line)]] | alt | 599 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -40.8) |
| [[A549 (line)]] | wt | 834 | 0 | 19 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0308× (z -34.7) |
| [[NCI-H2030 (line)]] | alt | 1,338 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0555× (z -35.2) |
| [[NCI-H23 (line)]] | alt | 413 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -28.5) |
| [[SK-MEL-2 (line)]] | alt | 365 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -31.5) |
| [[AsPC-1 (line)]] | alt | 490 | 0 | 16 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0767× (z -23.2) |
| [[LOX-IMVI (line)]] | wt | 289 | 1 | 13 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.52× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -27.9) |
| [[A-427 (line)]] | wt | 443 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -20.2) |
| [[C-33 A (line)]] | alt | 280 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -21.4) |
| [[SNU-1 (line)]] | wt | 134 | 1 (1 ⚠) | 11 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 5 µM 0.141× (z -16.5) |
| [[LoVo (line)]] | wt | 301 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -22.0) |
| [[BT-474 (line)]] | alt | 300 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -25.8) |
| [[HT-29 (line)]] | alt | 578 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -23.9) |
| [[RKO (line)]] | wt | 312 | 0 | 10 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0878× (z -21.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.0) |
| [[RPMI-7951 (line)]] | alt | 381 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -27.5) |
| [[SNU-423 (line)]] | alt | 322 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0885× (z -26.7) |
| [[SW48 (line)]] | wt | 213 | 1 (1 ⚠) | 9 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -23.0) |
| [[Hs 766T (line)]] | wt | 116 | 4 | 4 | [[Clobetasol propionate (drug)]] 0.05 µM 2.88× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.9) |
| [[LS 180 (line)]] | wt | 445 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 8 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -18.0) |
| [[SW 900 (line)]] | alt | 252 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -20.0) |
| [[SW1417 (line)]] | alt | 165 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.8) |
| [[A-172 (line)]] | wt | 224 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -26.5) |
| [[CFPAC-1 (line)]] | alt | 492 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -25.9) |
| [[HS-578T (line)]] | alt | 109 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 185 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.0) |
| [[SW 1271 (line)]] | alt | 543 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -18.4) |
| [[SW480 (line)]] | alt | 112 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.7) |
| [[AN3 CA (line)]] | alt | 233 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.7) |
| [[COLO 205 (line)]] | alt | 166 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.6) |
| [[CHP-212 (line)]] | wt | 254 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.6) |
| [[H4 (line)]] | wt | 144 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.6) |
| [[HCT15 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -16.8) |
| [[A498 (line)]] | wt | 52.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 84.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 68.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 35.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 702 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 527 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPAS2]] | +0.78 | +0.79 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4-AS1]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.71 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.70 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[EFNA5]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.67 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[DOCK5]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 | same gene group |
| [[PTPN12]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[MAML3]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.66 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATCAP2]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PITPNC1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 12.3% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.7, 5.9); signed map (7.8, 47.9). **Vector** length 131, 53.9% of its response variance represented; |z| ≥ 3 in 2,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.2 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.2 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.6 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.4 | +1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -11.7 | -9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -10.5 | -9.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -10.2 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -10.0 | -8.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -10.0 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -9.9 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol transfer protein cytoplasmic 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:67,377,281-67,697,256 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RDGBB1, RDGBB, RDGB-BETA |
| Gene groups (HGNC) | Phosphatidylinositol transfer proteins; MicroRNA protein coding host genes |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKF7](https://www.uniprot.org/uniprotkb/Q9UKF7) (Cytoplasmic phosphatidylinositol transfer protein 1):

> [Isoform 1]: Catalyzes the transfer of phosphatidylinositol (PI) and phosphatidic acid (PA) between membranes. Binds PA derived from the phospholipase D signaling pathway and among the cellular PA species, preferably binds to the C16:0/16:1 and C16:1/18:1 PA species.; [Isoform 2]: Catalyzes the transfer of phosphatidylinositol between membranes.

**Summary**, from NCBI Gene [26207](https://www.ncbi.nlm.nih.gov/gene/26207):

> This gene encodes a member of the phosphatidylinositol transfer protein family. The encoded cytoplasmic protein plays a role in multiple processes including cell signaling and lipid metabolism by facilitating the transfer of phosphatidylinositol between membrane compartments. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 1. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:21045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21045) · Entrez [26207](https://www.ncbi.nlm.nih.gov/gene/26207) · UniProt [Q9UKF7](https://www.uniprot.org/uniprotkb/Q9UKF7) · Ensembl [ENSG00000154217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154217)

## Data

Gene col 7784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7784); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7784]; `tensor/DDL_lfc|DDL_z.npy` [7784]; `embed/gene_vectors.npy` [7784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7784 or target_col == 7784). Every well: [[PITPNC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
