---
symbol: "USP14"
type: "gene"
col: 2152
ensembl_id: "ENSG00000101557"
name: "ubiquitin specific peptidase 14"
location: "18p11.32"
module: 4
arm: "+"
pooled_cpm: 126.36
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# USP14

*ubiquitin specific peptidase 14* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.40× (z +21.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.684× (z -13.2, q 4e-37, down in 42 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (LoVo 0.493×, HOP62 0.510×, RKO 0.498×, SW480 0.617×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.686×; ⚠ cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TALDO1]] (+0.77, fdr 7e-06), [[OPA1]] (+0.76, fdr 7e-06), [[API5]] (+0.75, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.68, fdr 7e-06), [[POLR1H]] (-0.67, fdr 1e-05), [[HMGCL]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[S100A13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.40×** | +21.3 | 0e+00 | 48/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.34×** | +19.5 | 0e+00 | 47/48 (HT-29, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.20×** | +19.2 | 0e+00 | 47/48 (HOP62, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.71×** | +13.0 | 2e-36 | 36/49 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +12.7 | 1e-34 | 48/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +10.6 | 3e-24 | 42/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.53×** | +10.3 | 4e-23 | 44/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +10.3 | 6e-23 | 43/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.52×** | +9.7 | 1e-20 | 34/44 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +8.6 | 4e-16 | 43/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +8.3 | 5e-15 | 31/48 (C32, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.45×** | +8.3 | 7e-15 | 35/45 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +8.2 | 1e-14 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.39×** | +8.0 | 4e-14 | 41/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +7.5 | 2e-12 | 41/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 3e-11 | 31/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +7.1 | 4e-11 | 31/48 (HT-29, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.007 | 18/48 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.008 | 16/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.16× | +3.3 | 0.016 | 15/48 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.031 | 13/48 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.059 | 9/49 (SNU-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 1.13× | +2.8 | 0.095 | 4/48 (SW 1088, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (LoVo 0.493×, HOP62 0.510×, RKO 0.498×, SW480 0.617×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.686×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -13.2 | 4e-37 | 42/49 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.792×** | -5.7 | 3e-06 | 28/49 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.783×** | -4.3 | 0.003 | 24/48 (A-172, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.841× | -4.1 | 0.005 | 20/49 (NCI-H1792, A549, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.9 | 0.012 | 11/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.884× | -3.1 | 0.18 | 11/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.886× | -3.0 | 0.18 | 5/48 (SW 1088, Hs 766T, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.886× | -3.0 | 0.18 | 7/48 (NCI-H460, LS 180, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 125 | 11 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 99.9 | 8 (3 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.662× (z -9.1) |
| [[SW480 (line)]] | alt | 129 | 8 (3 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.77× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 106 | 7 (4 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.65× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -12.0) |
| [[HOP62 (line)]] | alt | 153 | 6 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.64× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -14.6) |
| [[LoVo (line)]] | wt | 130 | 6 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.66× (z +14.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -15.4) |
| [[C32 (line)]] | wt | 98.3 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 65.5 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 90.0 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.62× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 89.5 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.20× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 164 | 4 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 211 | 5 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.12× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 126 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +12.7) | — |
| [[A549 (line)]] | wt | 81.6 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.38× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -9.0) |
| [[HCT15 (line)]] | alt | 122 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.05× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 139 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -10.4) |
| [[HT-29 (line)]] | alt | 142 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +16.2) | — |
| [[hTERT-HPNE (line)]] | wt | 76.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.35× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 132 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 100 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.80× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.33× (z +10.3) | — |
| [[A-172 (line)]] | wt | 177 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +13.9) | — |
| [[A-427 (line)]] | wt | 314 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 37.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.03× (z +13.0) | — |
| [[J82 (line)]] | alt | 200 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.08× (z +11.1) | — |
| [[KATO III (line)]] | alt | 93.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +13.2) | — |
| [[SNU-1 (line)]] | wt | 159 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.46× (z +8.9) | — |
| [[SW48 (line)]] | wt | 178 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.86× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 72.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.6) |
| [[BT-474 (line)]] | alt | 194 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 1.96× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -9.1) |
| [[H4 (line)]] | wt | 128 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +9.4) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 127 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 80.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 115 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +9.2) | — |
| [[A498 (line)]] | wt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.5) |
| [[RKO (line)]] | wt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.7) |
| [[SW 900 (line)]] | alt | 105 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.49× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALDO1]] | +0.77 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[OPA1]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[API5]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.71 | +0.74 / +0.82 | both halves | 7e-06 | STRING 689 |
| [[HERC2]] | +0.70 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.70 | +0.65 / +0.77 | both halves | 7e-06 | pathway: Deubiquitination; STRING 999 |
| [[DLAT]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[AGPS]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CCT2]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | STRING 516 |
| [[TCP1]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[PHKB]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.68 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[POLR1H]] | -0.67 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.67 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[HLA-A]] | -0.65 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.63 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.61 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[NDUFC1]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[BET1]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[MIA]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.59 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[GAD1]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A13]] | C | S100A13 activity lowers USP14's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 1.89× higher at baseline in the lines without S100A13 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.7, -14.5); signed map (-16.1, -43.4). **Vector** length 118, 40.2% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +21.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.7 | +19.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.0 | +19.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +7.1 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +6.4 | +9.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +7.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.9 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +10.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.7 | -13.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | -6.8 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -6.2 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:158,383-214,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TGT, Ubp6 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 25 pathways, smallest: Regulation of NF-kappa B signaling; TAK1-dependent IKK and NF-kappa-B activation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P54578](https://www.uniprot.org/uniprotkb/P54578) (Ubiquitin carboxyl-terminal hydrolase 14):

> Proteasome-associated deubiquitinase which releases ubiquitin from the proteasome targeted ubiquitinated proteins. Ensures the regeneration of ubiquitin at the proteasome. Is a reversibly associated subunit of the proteasome and a large fraction of proteasome-free protein exists within the cell. Required for the degradation of the chemokine receptor CXCR4 which is critical for CXCL12-induced cell chemotaxis. Also serves as a physiological inhibitor of endoplasmic reticulum-associated …

**Summary**, from NCBI Gene [9097](https://www.ncbi.nlm.nih.gov/gene/9097):

> This gene encodes a member of the ubiquitin-specific processing (UBP) family of proteases that is a deubiquitinating enzyme (DUB) with His and Cys domains. This protein is located in the cytoplasm and cleaves the ubiquitin moiety from ubiquitin-fused precursors and ubiquitinylated proteins. Mice with a mutation that results in reduced expression of the ortholog of this protein are retarded for growth, develop severe tremors by 2 to 3 weeks of age followed by hindlimb paralysis and death by 6 to …

**Accessions** — [HGNC:12612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12612) · Entrez [9097](https://www.ncbi.nlm.nih.gov/gene/9097) · UniProt [P54578](https://www.uniprot.org/uniprotkb/P54578) · Ensembl [ENSG00000101557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101557)

## Data

Gene col 2152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2152); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2152]; `tensor/DDL_lfc|DDL_z.npy` [2152]; `embed/gene_vectors.npy` [2152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2152 or target_col == 2152). Every well: [[USP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
