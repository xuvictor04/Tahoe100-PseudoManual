---
symbol: "TSPAN15"
type: "gene"
col: 1789
ensembl_id: "ENSG00000099282"
name: "tetraspanin 15"
location: "10q22.1"
module: 14
arm: "+"
pooled_cpm: 30.42
n_lines_expressing: 35
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 16
direction_downstream: 28
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TSPAN15

*tetraspanin 15* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.32× (z +22.0, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.470× (z -9.8, q 6e-20, down in 27 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 4 lines (Panc 03.27 0.197×, HT-29 0.210×, NCI-H2347 0.349×, SW1417 0.357×); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.144×, HepG2/C3A 0.125×, Panc 03.27 0.320×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW1417 0.218×, NCI-H2347 0.314×, COLO 205 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGN]] (+0.65, fdr 7e-06), [[CXADR]] (+0.65, fdr 7e-06), [[TNFAIP2]] (+0.61, fdr 7e-06); moves opposite to [[LRRC41]] (-0.58, fdr 1e-04), [[PIGG]] (-0.55, fdr 2e-05), [[ACAD9]] (-0.55, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CXADR]] → it (grade B ⚠); 28 go from it, the strongest it → [[TUFT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.32×** | +22.0 | 0e+00 | 30/33 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.30×** | +15.5 | 0e+00 | 30/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.97×** | +14.1 | 5e-43 | 28/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.98×** | +13.6 | 3e-40 | 29/32 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.76×** | +13.2 | 1e-37 | 31/32 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +12.8 | 2e-35 | 31/33 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +9.1 | 5e-18 | 28/32 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +9.0 | 1e-17 | 25/30 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +8.2 | 2e-14 | 21/29 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.0 | 1e-10 | 20/31 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +6.6 | 2e-09 | 24/32 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.62×** | +6.5 | 3e-09 | 24/33 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.2 | 2e-08 | 17/31 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 2e-07 | 20/31 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 8e-04 | 10/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.006 | 15/32 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 14/33 (PANC-1, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 4 lines (Panc 03.27 0.197×, HT-29 0.210×, NCI-H2347 0.349×, SW1417 0.357×); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.144×, HepG2/C3A 0.125×, Panc 03.27 0.320×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW1417 0.218×, NCI-H2347 0.314×, COLO 205 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.470×** | -9.8 | 6e-20 | 27/31 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.624× | -3.2 | 0.15 | 11/29 (Hs 766T, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.782× | -3.2 | 0.15 | 7/32 (A-172, A549, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.784× | -3.2 | 0.15 | 14/32 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.842× | -3.2 | 0.15 | 16/33 (Hs 766T, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Proglumide (drug)]] 0.05 µM |  | 0.784× | -3.1 | 0.15 | 8/31 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.792× | -3.0 | 0.19 | 8/32 (A-172, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 12 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.64× (z +11.9) | — |
| [[LoVo (line)]] | wt | 23.6 | 6 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.19× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 73.4 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.0) | [[Auranofin (drug)]] 5 µM 0.197× (z -13.8) |
| [[PANC-1 (line)]] | alt | 66.2 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.72× (z +12.2) | — |
| [[SW480 (line)]] | alt | 21.7 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.30× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 50.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 23.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 58.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.180× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.210× (z -11.4) |
| [[BT-474 (line)]] | alt | 78.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 98.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +23.0) | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 27.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.03× (z +11.4) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 3.87× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.79× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.349× (z -9.8) |
| [[SW 900 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +14.4) | — |
| [[A-172 (line)]] | wt | 14.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.91× (z +9.2) | — |
| [[A498 (line)]] | wt | 47.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +10.1) | — |
| [[A549 (line)]] | wt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 20.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 7.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +10.1) | — |
| [[A-427 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGN]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CXADR]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.61 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[BCL3]] | +0.59 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ELF3]] | +0.59 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[SSBP3]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[GRHL1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[USP2]] | +0.56 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[ABCG2]] | +0.56 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[BCAM]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ZNF592]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RHOV]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC41]] | -0.58 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[PIGG]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ACAD9]] | -0.55 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[THBD]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TRMT1]] | -0.52 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[MOSMO]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TIRAP]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[RECQL5]] | -0.51 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[SLC30A6]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[HCG18]] | -0.49 | -0.32 / -0.51 | both halves | 1e-04 |  |
| [[APTX]] | -0.49 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 12, C 4. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity raises TSPAN15's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without CXADR | 0.006 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[CX3CL1]] | B | CX3CL1 activity raises TSPAN15's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without CX3CL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[THBD]] | B | THBD activity raises TSPAN15's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without THBD | 0.012 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[ATP8B1]] | B | ATP8B1 activity raises TSPAN15's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without ATP8B1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises TSPAN15's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without TNFAIP2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[EFNA1]] | B | EFNA1 activity raises TSPAN15's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without EFNA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises TSPAN15's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.87× lower at baseline in the lines without TJP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[TRIM31]] | B | TRIM31 activity raises TSPAN15's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.91× lower at baseline in the lines without TRIM31 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[NFATC2]] | B | NFATC2 activity raises TSPAN15's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without NFATC2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[HHLA2]] | B | HHLA2 activity raises TSPAN15's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without HHLA2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[ARHGAP26]] | B | ARHGAP26 activity raises TSPAN15's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 3.20× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[MPP7]] | B | MPP7 activity raises TSPAN15's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without MPP7 | 0.051 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 24, C 4. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUFT1]] | B | TSPAN15 activity raises TUFT1's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without TSPAN15 | 0.004 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[ZNF592]] | B | TSPAN15 activity raises ZNF592's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.21× lower at baseline in the lines without TSPAN15 | 0.013 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[ZMIZ2]] | B | TSPAN15 activity raises ZMIZ2's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without TSPAN15 | 0.020 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[LYN]] | B | TSPAN15 activity raises LYN's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without TSPAN15 | 0.026 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[IRF1]] | B | TSPAN15 activity raises IRF1's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without TSPAN15 | 0.032 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[LRRC41]] | B | TSPAN15 activity lowers LRRC41's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without TSPAN15 | 0.041 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[TNFAIP2]] | B | TSPAN15 activity raises TNFAIP2's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.45× lower at baseline in the lines without TSPAN15 | 0.044 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[HCG18]] | B | TSPAN15 activity lowers HCG18's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.36× higher at baseline in the lines without TSPAN15 | 0.052 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[EFNA1]] | B | TSPAN15 activity raises EFNA1's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.70× lower at baseline in the lines without TSPAN15 | 0.056 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[AFDN]] | B | TSPAN15 activity raises AFDN's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without TSPAN15 | 0.063 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[ARHGAP26]] | B | TSPAN15 activity raises ARHGAP26's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without TSPAN15 | 0.064 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[ZNF26]] | B | TSPAN15 activity lowers ZNF26's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.47× higher at baseline in the lines without TSPAN15 | 0.065 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.3, 1.7); signed map (47.7, 4.9). **Vector** length 106, 31.6% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +13.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +9.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,451,465-69,507,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NET-7; previously TM4SF15 |
| Gene groups (HGNC) | Tetraspanin family |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95858](https://www.uniprot.org/uniprotkb/O95858) (Tetraspanin-15):

> Part of TspanC8 subgroup, composed of 6 members that interact with the transmembrane metalloprotease ADAM10. This interaction is required for ADAM10 exit from the endoplasmic reticulum and for enzymatic maturation and trafficking to the cell surface as well as substrate specificity. Different TspanC8/ADAM10 complexes have distinct substrates. Promotes ADAM10-mediated cleavage of CDH2. Negatively regulates ligand-induced Notch activity probably by regulating ADAM10 activity.

**Summary**, from NCBI Gene [23555](https://www.ncbi.nlm.nih.gov/gene/23555):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. The use of alternate polyadenylation sites has been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23298) · Entrez [23555](https://www.ncbi.nlm.nih.gov/gene/23555) · UniProt [O95858](https://www.uniprot.org/uniprotkb/O95858) · Ensembl [ENSG00000099282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099282)

## Data

Gene col 1789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1789); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1789]; `tensor/DDL_lfc|DDL_z.npy` [1789]; `embed/gene_vectors.npy` [1789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1789 or target_col == 1789). Every well: [[TSPAN15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
