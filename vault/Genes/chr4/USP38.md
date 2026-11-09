---
symbol: "USP38"
type: "gene"
col: 9912
ensembl_id: "ENSG00000170185"
name: "ubiquitin specific peptidase 38"
location: "4q31.21"
module: 215
arm: "+"
pooled_cpm: 25.25
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# USP38

*ubiquitin specific peptidase 38* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.90× (z +24.0, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.662× (z -5.2, q 1e-04, down in 29 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.661× (z -3.7, q 0.058, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW 900 0.105×, Panc 03.27 0.145×, NCI-H2030 0.283×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.150×, HepG2/C3A 0.112×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.153×, RKO 0.218×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.150×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.197×); [[Orlistat (drug)]] 0.05 µM in 1 line (H4 0.0790×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C17orf80]] (+0.60, fdr 3e-05), [[EIF4G2]] (+0.58, fdr 1e-05), [[ZXDB]] (+0.56, fdr 1e-05); moves opposite to [[FAM118A]] (-0.55, fdr 7e-05), [[NKTR]] (-0.54, fdr 4e-04), [[ARNT]] (-0.53, fdr 7e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.90×** | +24.0 | 0e+00 | 47/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **9.85×** | +13.1 | 7e-37 | 46/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +12.2 | 4e-32 | 42/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.51×** | +11.0 | 4e-26 | 42/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.34×** | +10.6 | 5e-24 | 44/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.96×** | +10.2 | 1e-22 | 44/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.25×** | +10.1 | 6e-22 | 44/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.22×** | +9.9 | 2e-21 | 42/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.09×** | +9.1 | 4e-18 | 41/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.08×** | +9.1 | 6e-18 | 43/48 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +7.9 | 2e-13 | 44/48 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.84×** | +7.6 | 2e-12 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.5 | 2e-12 | 32/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.79×** | +7.3 | 2e-11 | 37/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +6.1 | 3e-08 | 25/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.8 | 3e-07 | 32/47 (C32, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.6 | 8e-07 | 33/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +5.1 | 8e-06 | 30/47 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9912.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW 900 0.105×, Panc 03.27 0.145×, NCI-H2030 0.283×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.150×, HepG2/C3A 0.112×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.153×, RKO 0.218×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.150×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.197×); [[Orlistat (drug)]] 0.05 µM in 1 line (H4 0.0790×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.662×** | -5.2 | 1e-04 | 29/44 (SNU-423, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.661×** | -3.7 | 0.058 | 22/46 (A-427, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -3.5 | 0.095 | 17/35 (LS 180, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.688× | -3.4 | 0.11 | 16/48 (NCI-H2030, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.5 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +21.0) | — |
| [[PANC-1 (line)]] | alt | 14.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +15.3) | — |
| [[LS 180 (line)]] | wt | 30.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +12.6) | — |
| [[SW480 (line)]] | alt | 24.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.6) | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +20.3) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.150× (z -13.4) |
| [[A498 (line)]] | wt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +24.6) | — |
| [[HOP62 (line)]] | alt | 19.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +16.1) | — |
| [[KATO III (line)]] | alt | 23.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +17.1) | — |
| [[AsPC-1 (line)]] | alt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +14.1) | — |
| [[C32 (line)]] | wt | 28.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.7) | — |
| [[COLO 205 (line)]] | alt | 23.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +17.5) | — |
| [[H4 (line)]] | wt | 17.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +9.2) | [[Orlistat (drug)]] 0.05 µM 0.0790× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 31.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 16.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.197× (z -10.1) |
| [[LoVo (line)]] | wt | 38.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +14.9) | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 30.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 53.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 18.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 25.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.101× (z -8.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +15.3) | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.174× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 49.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +13.6) | — |
| [[J82 (line)]] | alt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.9) | — |
| [[SW48 (line)]] | wt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +9.3) | — |
| [[A-172 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf80]] | +0.60 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[EIF4G2]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TWF1]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[HSPB8]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PPP2CA]] | +0.54 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[POLR2M]] | +0.53 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[MGAT2]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[MPDU1]] | +0.52 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[C9orf64]] | +0.52 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[SMCR8]] | +0.52 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[MRPS7]] | +0.52 | +0.54 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.55 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[NKTR]] | -0.54 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[ARNT]] | -0.53 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[E4F1]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[DENND6A]] | -0.53 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[MHENCR]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PTMA]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SEC22A]] | -0.51 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[VPS37C]] | -0.51 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.50 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PKN1]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[LAMTOR4]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP38's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.2, -22.3); signed map (16.9, -33.8). **Vector** length 64.2, 13.8% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +13.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.4 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.8 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -2.7 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:143,184,917-143,223,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1891, HP43.8KD |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB14](https://www.uniprot.org/uniprotkb/Q8NB14) (Ubiquitin carboxyl-terminal hydrolase 38):

> Deubiquitinating enzyme that plays a role in various cellular processes, including DNA repair, cell cycle regulation, and immune response. Plays a role in the inhibition of type I interferon signaling by mediating the 'Lys-33' to 'Lys-48' ubiquitination transition of TBK1 leading to its degradation. Cleaves the ubiquitin chain from the histone demethylase LSD1/KDM1A and prevents it from degradation by the 26S proteasome, thus maintaining LSD1 protein level in cells. Plays a role in the DNA …

**Summary**, from NCBI Gene [84640](https://www.ncbi.nlm.nih.gov/gene/84640):

> Enables cysteine-type deubiquitinase activity. Involved in negative regulation of innate immune response; negative regulation of proteasomal ubiquitin-dependent protein catabolic process; and protein K33-linked deubiquitination. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20067) · Entrez [84640](https://www.ncbi.nlm.nih.gov/gene/84640) · UniProt [Q8NB14](https://www.uniprot.org/uniprotkb/Q8NB14) · Ensembl [ENSG00000170185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170185)

## Data

Gene col 9912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9912); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9912]; `tensor/DDL_lfc|DDL_z.npy` [9912]; `embed/gene_vectors.npy` [9912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9912 or target_col == 9912). Every well: [[USP38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
