---
symbol: "ANKRD28"
type: "gene"
col: 13050
ensembl_id: "ENSG00000206560"
name: "ankyrin repeat domain 28"
location: "3p25.1"
module: 33
arm: "+"
pooled_cpm: 298.62
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ANKRD28

*ankyrin repeat domain 28* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.39× (z +6.7, q 1e-08, up in 32 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 2.78×, MIA PaCa-2 1.60×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 3.08×, C32 2.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 2.55×, A-172 2.36×); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 3.25×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.542× (z -17.0, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCL1]] (+0.61, fdr 7e-06), [[ZHX3]] (+0.54, fdr 5e-05), [[SPIDR]] (+0.52, fdr 4e-05); moves opposite to [[KRBOX5]] (-0.49, fdr 1e-04), [[LRP2BP]] (-0.47, fdr 2e-04), [[STXBP2]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MBNL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 2.78×, MIA PaCa-2 1.60×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 3.08×, C32 2.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 2.55×, A-172 2.36×); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.7 | 1e-08 | 32/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.43× | +3.6 | 0.10 | 19/50 (HOP62, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.39× | +3.3 | 0.18 | 23/49 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.36× | +3.1 | 0.31 | 20/48 (J82, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -17.0 | 0e+00 | 40/49 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -14.4 | 1e-44 | 43/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -13.5 | 4e-39 | 39/44 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -13.3 | 3e-38 | 42/48 (SW480, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.600×** | -10.7 | 7e-25 | 40/49 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -8.6 | 1e-15 | 34/50 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.677×** | -8.2 | 2e-14 | 40/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -7.5 | 4e-12 | 34/48 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.790×** | -6.5 | 6e-09 | 29/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -6.1 | 6e-08 | 29/48 (RKO, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.757×** | -5.6 | 9e-07 | 29/48 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.753×** | -5.5 | 1e-06 | 29/45 (RKO, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.772×** | -5.5 | 2e-06 | 30/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.646×** | -4.4 | 4e-04 | 27/48 (NCI-H1792, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.817×** | -4.3 | 7e-04 | 27/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.689×** | -3.7 | 0.006 | 26/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.852× | -3.4 | 0.023 | 21/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.894× | -3.1 | 0.058 | 10/48 (NCI-H2030, SW480, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.818×** | -3.0 | 0.073 | 15/48 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 296 | 1 (1 ⚠) | 9 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.10× (z +11.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -21.3) |
| [[hTERT-HPNE (line)]] | wt | 618 | 1 | 8 (5 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.37× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 364 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -18.7) |
| [[RKO (line)]] | wt | 201 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.238× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 391 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 615 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -17.9) |
| [[SW480 (line)]] | alt | 408 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.320× (z -19.3) |
| [[A-427 (line)]] | wt | 495 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.292× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 356 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.2) |
| [[SNU-423 (line)]] | alt | 303 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 129 | 4 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 309 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 303 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.397× (z -11.5) |
| [[HOP62 (line)]] | alt | 665 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -12.2) |
| [[J82 (line)]] | alt | 315 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 277 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.8) |
| [[SW 900 (line)]] | alt | 457 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.294× (z -11.5) |
| [[SW1417 (line)]] | alt | 362 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -14.0) |
| [[A549 (line)]] | wt | 265 | 2 | 2 | [[Triamcinolone (drug)]] 0.5 µM 2.01× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 438 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.5) |
| [[SW48 (line)]] | wt | 254 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -11.9) |
| [[A-172 (line)]] | wt | 172 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -10.1) |
| [[C32 (line)]] | wt | 318 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 3.25× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -11.7) |
| [[H4 (line)]] | wt | 371 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -11.7) |
| [[HS-578T (line)]] | alt | 315 | 1 | 2 | [[Clobetasol propionate (drug)]] 5 µM 2.26× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -15.5) |
| [[LoVo (line)]] | wt | 184 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.397× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 565 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.2) |
| [[SHP-77 (line)]] | alt | 262 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.343× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 267 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -16.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.356× (z -15.0) |
| [[KATO III (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -14.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 227 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.348× (z -14.0) |
| [[A498 (line)]] | wt | 167 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.5) |
| [[BT-474 (line)]] | alt | 225 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.7) |
| [[Hs 766T (line)]] | wt | 296 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -8.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 249 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -14.6) |
| [[SNU-1 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.422× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 609 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.4) |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 246 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 298 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCL1]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 | same gene group |
| [[ZHX3]] | +0.54 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[SPIDR]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[AKAP13]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 | same gene group |
| [[TMEM131L]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[TGFBR2]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[LDLRAD3]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 | same gene group |
| [[XPR1]] | +0.51 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[EXOSC5]] | +0.50 | +0.40 / +0.42 | both halves | 4e-05 |  |
| [[TMEM245]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 | same gene group |
| [[TTLL5]] | +0.49 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[NARS2]] | +0.49 | +0.34 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX5]] | -0.49 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[LRP2BP]] | -0.47 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[STXBP2]] | -0.47 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.47 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[CSRNP2]] | -0.46 | -0.47 / -0.33 | both halves | 1e-04 | same gene group |
| [[ZNF547]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ATXN1L]] | -0.46 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[LRIF1]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[LINC03016]] | -0.46 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SRP19]] | -0.46 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ZDBF2]] | -0.45 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[ZNF774]] | -0.45 | -0.40 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises ANKRD28's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without HEG1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[HEG1]] | B | HEG1 activity strengthens ANKRD28's drug response | lines that do not express HEG1 (11) vs lines expressing it (39) | the lines without HEG1 respond 0.66× as strongly (z diff +2.19); strongest at Idarubicin (hydrochloride) 5 µM: 0.73x vs 0.51x (z diff +3.7) | 0.078 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK; artifact flags |
| [[FZD4]] | B | FZD4 activity raises ANKRD28's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without FZD4 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CDCA7L]] | B | CDCA7L activity raises ANKRD28's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without CDCA7L | 0.093 | ⚠ within organs, on part of the lines |
| [[TOP2A]] | B | TOP2A activity raises ANKRD28's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBNL1]] | C | ANKRD28's natural level strengthens MBNL1's drug response | ANKRD28's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.35; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.368). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (31.6, 9.8); signed map (-11.6, 51.7). **Vector** length 123, 38.8% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.5 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.8 | +2.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.7 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.0 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,667,236-15,859,771 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0379, PITK, PP6-ARS-A, PPP1R65, FAP79, CFAP79 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; Protein phosphatase 6 regulatory subunits; Cilia and flagella associated; MicroRNA protein coding host genes |
| Reactome | 11 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O15084](https://www.uniprot.org/uniprotkb/O15084) (Serine/threonine-protein phosphatase 6 regulatory ankyrin repeat subunit A):

> Regulatory subunit of protein phosphatase 6 (PP6) that may be involved in the recognition of phosphoprotein substrates. Involved in the PP6-mediated dephosphorylation of NFKBIE opposing its degradation in response to TNF. Selectively inhibits the phosphatase activity of PPP1C. Targets PPP1C to modulate HNRPK phosphorylation. Involved in the PP6-mediated dephosphorylation of MOB1 and induced focal adhesion assembly during cell migration.

**Summary**, from NCBI Gene [23243](https://www.ncbi.nlm.nih.gov/gene/23243):

> Enables protein phosphatase regulator activity. Involved in positive regulation of focal adhesion assembly. Located in cytosol and lamellipodium. Part of protein serine/threonine phosphatase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29024) · Entrez [23243](https://www.ncbi.nlm.nih.gov/gene/23243) · UniProt [O15084](https://www.uniprot.org/uniprotkb/O15084) · Ensembl [ENSG00000206560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206560)

## Data

Gene col 13050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13050); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13050]; `tensor/DDL_lfc|DDL_z.npy` [13050]; `embed/gene_vectors.npy` [13050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13050 or target_col == 13050). Every well: [[ANKRD28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
