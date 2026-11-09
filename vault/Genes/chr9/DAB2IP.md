---
symbol: "DAB2IP"
type: "gene"
col: 5917
ensembl_id: "ENSG00000136848"
name: "DAB2 interacting protein"
location: "9q33.2"
module: 8
arm: "+"
pooled_cpm: 27.49
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 13
direction_downstream: 8
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DAB2IP

*DAB2 interacting protein* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +6.2, q 4e-07, up in 22 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (J82 3.91×, HOP62 2.61×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 4.71×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.618× (z -10.3, q 6e-22, down in 29 of 44 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.543× (z -9.2, q 9e-18, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHROOM2]] (+0.57, fdr 1e-05), [[AFAP1L2]] (+0.56, fdr 1e-05), [[TP53I11]] (+0.56, fdr 1e-05); moves opposite to [[FAM228B]] (-0.51, fdr 3e-05), [[CKMT2-AS1]] (-0.48, fdr 5e-05), [[XPNPEP3]] (-0.47, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CLIC5]] → it (grade B ⚠); 8 go from it, the strongest it → [[LRRC27]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (J82 3.91×, HOP62 2.61×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 4.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.2 | 4e-07 | 22/44 (J82, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 2e-04 | 22/43 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +3.9 | 0.017 | 16/44 (LS 180, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.618×** | -10.3 | 6e-22 | 29/44 (C32, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -9.2 | 9e-18 | 32/42 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -8.9 | 1e-16 | 28/43 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.566×** | -8.6 | 1e-15 | 28/44 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.591×** | -7.9 | 2e-13 | 31/42 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -7.2 | 8e-11 | 29/43 (HT-29, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -6.3 | 3e-08 | 23/45 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.664×** | -5.7 | 8e-07 | 18/34 (HEC-1-A, C32, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.690×** | -5.3 | 8e-06 | 21/44 (C32, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.700×** | -5.2 | 1e-05 | 25/41 (SW480, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.712×** | -5.1 | 1e-05 | 21/43 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.724×** | -4.9 | 5e-05 | 28/43 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -4.8 | 6e-05 | 22/42 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -4.7 | 1e-04 | 22/43 (C32, HepG2/C3A, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.740×** | -4.6 | 2e-04 | 18/43 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.573×** | -4.4 | 4e-04 | 15/41 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.851× | -3.5 | 0.013 | 17/44 (C32, HT-29, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.673×** | -3.1 | 0.040 | 10/42 (A-172, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.871× | -3.0 | 0.063 | 9/44 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.821×** | -2.9 | 0.082 | 9/43 (C32, NCI-H23, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -2.9 | 0.083 | 13/44 (NCI-H2030, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 99.1 | 0 | 24 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -28.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -17.5) |
| [[SW480 (line)]] | alt | 32.3 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -8.7) |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0509× (z -24.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 57.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 52.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[HT-29 (line)]] | alt | 55.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.186× (z -12.5) |
| [[KATO III (line)]] | alt | 59.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -12.0) |
| [[LoVo (line)]] | wt | 33.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[RKO (line)]] | wt | 23.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.6) |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0647× (z -10.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0674× (z -10.0) |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.1) |
| [[BT-474 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 44.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.9) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -11.7) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A498 (line)]] | wt | 18.9 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 86.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.165× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 42.1 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.182× (z -8.9) |
| [[HOP62 (line)]] | alt | 14.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.61× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 9.41 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.130× (z -9.2) |
| [[HS-578T (line)]] | alt | 30.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -9.1) |
| [[J82 (line)]] | alt | 12.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.91× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 53.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.0) |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0777× (z -10.2) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHROOM2]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TP53I11]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RAPGEF5]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[UNC5A]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[B3GNT2]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TGFBR3]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PTPRU]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SEMA4D]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MUC3A]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ATP10B]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[FZD5]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM228B]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CKMT2-AS1]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[XPNPEP3]] | -0.47 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[HERC4]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TMEM91]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ZCWPW2]] | -0.46 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[FLJ46284]] | -0.46 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[TICAM2]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TMCO3]] | -0.44 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DCAF10]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MFSD11]] | -0.44 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[BBOF1]] | -0.44 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLIC5]] | B | CLIC5 activity raises DAB2IP's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.71× lower at baseline in the lines without CLIC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[ATP10B]] | B | ATP10B activity raises DAB2IP's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.20× lower at baseline in the lines without ATP10B | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[CEACAM1]] | B | CEACAM1 activity raises DAB2IP's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without CEACAM1 | 0.017 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[PCDH1]] | B | PCDH1 activity raises DAB2IP's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without PCDH1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[PCDH1]] | B | PCDH1 activity strengthens DAB2IP's drug response | lines that do not express PCDH1 (18) vs lines expressing it (27) | the lines without PCDH1 respond 0.58× as strongly (z diff +1.73); strongest at Auranofin 5 µM: 0.77x vs 0.45x (z diff +3.3) | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29; target measured in part of the lines; artifact flags |
| [[TMPRSS2]] | B | TMPRSS2 activity raises DAB2IP's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without TMPRSS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[B3GNT7]] | B | B3GNT7 activity raises DAB2IP's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.69× lower at baseline in the lines without B3GNT7 | 0.043 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[PROM1]] | B | PROM1 activity raises DAB2IP's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 1.85× lower at baseline in the lines without PROM1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[UGT8]] | B | UGT8 activity raises DAB2IP's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without UGT8 | 0.074 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[NOS1AP]] | B | NOS1AP activity raises DAB2IP's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without NOS1AP | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[ITGB6]] | B | ITGB6 activity raises DAB2IP's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without ITGB6 | 0.089 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[CEACAM1]] | B | CEACAM1 activity strengthens DAB2IP's drug response | lines that do not express CEACAM1 (24) vs lines expressing it (21) | the lines without CEACAM1 respond 0.54× as strongly (z diff +1.81); strongest at Dinaciclib 0.05 µM: 0.89x vs 0.54x (z diff +3.6) | 0.091 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; target measured in part of the lines; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC27]] | C | DAB2IP activity weakens LRRC27's drug response | lines that do not express DAB2IP (4) vs lines expressing it (43) | the lines without DAB2IP respond 2.20× as strongly (z diff -2.91); strongest at Ouabain (Octahydrate) 5 µM: 0.18x vs 0.39x (z diff -4.6) | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MYRF]] | C | DAB2IP activity raises MYRF's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without DAB2IP | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[LRRC27]] | C | DAB2IP activity lowers LRRC27's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without DAB2IP | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[TICAM2]] | C | DAB2IP activity lowers TICAM2's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.70× higher at baseline in the lines without DAB2IP | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[TBC1D2B]] | C | DAB2IP activity raises TBC1D2B's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without DAB2IP | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[OTULINL]] | C | DAB2IP activity raises OTULINL's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without DAB2IP | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[XPNPEP3]] | C | DAB2IP activity lowers XPNPEP3's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.10× higher at baseline in the lines without DAB2IP | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[TMCO3]] | C | DAB2IP activity lowers TMCO3's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.69× higher at baseline in the lines without DAB2IP | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, 44.1); signed map (55.0, 14.1). **Vector** length 95.5, 22.1% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | +5.1 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | -2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | DAB2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:121,567,057-121,785,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF9Q34, DIP1/2, KIAA1743, AIP1 |
| Gene groups (HGNC) | C2 and RasGAP domain containing |
| Reactome | 4 pathways, smallest: Regulation of RAS by GAPs; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWQ8](https://www.uniprot.org/uniprotkb/Q5VWQ8) (Disabled homolog 2-interacting protein):

> Functions as a scaffold protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Involved in several processes such as innate immune response, inflammation and cell growth inhibition, apoptosis, cell survival, angiogenesis, cell migration and maturation. Also plays a role in cell cycle checkpoint control; reduces G1 phase cyclin levels resulting in G0/G1 cell cycle arrest. Mediates signal transduction by receptor-mediated inflammatory signals, …

**Summary**, from NCBI Gene [153090](https://www.ncbi.nlm.nih.gov/gene/153090):

> DAB2IP is a Ras (MIM 190020) GTPase-activating protein (GAP) that acts as a tumor suppressor. The DAB2IP gene is inactivated by methylation in prostate and breast cancers (Yano et al., 2005 [PubMed 15386433]).[supplied by OMIM, May 2010]

**Accessions** — [HGNC:17294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17294) · Entrez [153090](https://www.ncbi.nlm.nih.gov/gene/153090) · UniProt [Q5VWQ8](https://www.uniprot.org/uniprotkb/Q5VWQ8) · Ensembl [ENSG00000136848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136848)

## Data

Gene col 5917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5917); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5917]; `tensor/DDL_lfc|DDL_z.npy` [5917]; `embed/gene_vectors.npy` [5917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5917 or target_col == 5917). Every well: [[DAB2IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAB2IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
