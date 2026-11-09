---
symbol: "CDC16"
type: "gene"
col: 5030
ensembl_id: "ENSG00000130177"
name: "cell division cycle 16"
location: "13q34"
module: 65
arm: "+"
pooled_cpm: 69.69
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# CDC16

*cell division cycle 16* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.29× (z +4.7, q 0.001, up in 25 of 43 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 4.30×, Panc 03.27 1.90×; ⚠ cell-cycle shift, explains ~52% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (J82 2.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (J82 2.83×; ⚠ cell-cycle shift, explains ~58% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.506× (z -18.2, q 0e+00, down in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (C32 0.167×, HOP62 0.352×, Hs 766T 0.345×, NCI-H460 0.428×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-423 0.343×, MIA PaCa-2 0.369×, C32 0.392×, NCI-H1573 0.454×; ⚠ cell-cycle shift, explains ~52% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.259×; ⚠ cell-cycle shift, explains ~29% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRS2]] (+0.67, fdr 7e-06), [[WDR11]] (+0.65, fdr 7e-06), [[DPY19L4]] (+0.61, fdr 3e-05); moves opposite to [[INTS6]] (-0.57, fdr 2e-05), [[MEIS2]] (-0.56, fdr 1e-05), [[SIK3]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZFP82]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 4.30×, Panc 03.27 1.90×; ⚠ cell-cycle shift, explains ~52% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (J82 2.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (J82 2.83×; ⚠ cell-cycle shift, explains ~58% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.7 | 0.001 | 25/43 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.6 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.17 | 8/48 (LoVo, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +3.2 | 0.17 | 19/47 (A549, RPMI-7951, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.19 | 10/48 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (C32 0.167×, HOP62 0.352×, Hs 766T 0.345×, NCI-H460 0.428×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-423 0.343×, MIA PaCa-2 0.369×, C32 0.392×, NCI-H1573 0.454×; ⚠ cell-cycle shift, explains ~52% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.259×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -18.2 | 0e+00 | 45/49 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.715×** | -8.9 | 1e-16 | 29/48 (SNU-423, MIA PaCa-2, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.705×** | -6.4 | 2e-08 | 30/50 (C32, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.749×** | -5.3 | 1e-05 | 25/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.757×** | -5.1 | 3e-05 | 23/48 (SK-MEL-2, A-172, …) | inconsistent across doses | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.802×** | -4.2 | 0.002 | 26/48 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.820×** | -3.8 | 0.011 | 21/48 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.826×** | -3.7 | 0.016 | 21/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.838× | -3.4 | 0.041 | 22/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 0.839× | -3.4 | 0.041 | 22/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.847× | -3.2 | 0.072 | 18/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.890× | -3.2 | 0.072 | 11/48 (A-172, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | 0.843× | -3.1 | 0.072 | 17/47 (NCI-H460, RPMI-7951, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.892× | -3.1 | 0.083 | 9/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.737×** | -3.1 | 0.084 | 21/49 (C32, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 103 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -26.1) |
| [[hTERT-HPNE (line)]] | wt | 73.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.9) |
| [[J82 (line)]] | alt | 95.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +25.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[SNU-423 (line)]] | alt | 63.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.9) |
| [[A498 (line)]] | wt | 65.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.0) |
| [[A549 (line)]] | wt | 75.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 65.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -13.5) |
| [[HCT15 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.2) |
| [[HOP62 (line)]] | alt | 53.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -16.4) |
| [[HS-578T (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 74.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -10.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 74.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 99.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 58.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 91.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.4) ⚠ cell-cycle shift, explains ~52% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.5) |
| [[PANC-1 (line)]] | alt | 54.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -12.7) |
| [[SW480 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.6) |
| [[A-172 (line)]] | wt | 108 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.4) |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -11.2) |
| [[H4 (line)]] | wt | 54.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 63.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.9) |
| [[Hs 766T (line)]] | wt | 89.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -15.4) |
| [[LoVo (line)]] | wt | 58.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.0) |
| [[RKO (line)]] | wt | 70.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SNU-1 (line)]] | wt | 94.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.6) |
| [[SW48 (line)]] | wt | 81.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.3) |
| [[A-427 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRS2]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[WDR11]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[DPY19L4]] | +0.61 | +0.43 / +0.73 | both halves | 3e-05 |  |
| [[MTG1]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[TRAK2]] | +0.60 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ACTR10]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ELMOD2]] | +0.58 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[ANAPC5]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 | same gene group; pathway: APC-Cdc20 mediated degradation of Nek2A; STRING 999 |
| [[CIZ1]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CIAO3]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[EXD2]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[MEIS2]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 | same gene group |
| [[SIK3]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RBBP6]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TLE4]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[GASAL1]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[SEMA4A]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SNRPB]] | -0.51 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[MICOS10]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GSTP1]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[NECTIN2]] | -0.50 | -0.33 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP82]] | B | ZFP82 activity lowers CDC16's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 1.28× higher at baseline in the lines without ZFP82 | 0.064 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |
| [[TOP2A]] | B | TOP2A activity raises CDC16's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.364). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.8, -3.1); signed map (-23.3, -15.1). **Vector** length 99.9, 23.6% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -18.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.9 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.6 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:114,234,887-114,272,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APC6, ANAPC6, CUT9 |
| Gene groups (HGNC) | Anaphase promoting complex; Tetratricopeptide repeat domain containing; MicroRNA protein coding host genes |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13042](https://www.uniprot.org/uniprotkb/Q13042) (Cell division cycle protein 16 homolog):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C complex catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin …

**Summary**, from NCBI Gene [8881](https://www.ncbi.nlm.nih.gov/gene/8881):

> The protein encoded by this gene functions as a protein ubiquitin ligase and is a component of the multiprotein APC complex. The APC complex is a cyclin degradation system that governs exit from mitosis by targeting cell cycle proteins for degredation by the 26S proteasome. Each component protein of the APC complex is highly conserved among eukaryotic organisms. This protein, and other APC complex proteins, contain a tetratricopeptide repeat (TPR) domain; a protein domain that is often involved …

**Accessions** — [HGNC:1720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1720) · Entrez [8881](https://www.ncbi.nlm.nih.gov/gene/8881) · UniProt [Q13042](https://www.uniprot.org/uniprotkb/Q13042) · Ensembl [ENSG00000130177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130177)

## Data

Gene col 5030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5030); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5030]; `tensor/DDL_lfc|DDL_z.npy` [5030]; `embed/gene_vectors.npy` [5030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5030 or target_col == 5030). Every well: [[CDC16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
