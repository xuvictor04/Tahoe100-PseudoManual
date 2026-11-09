---
symbol: "PCID2"
type: "gene"
col: 4723
ensembl_id: "ENSG00000126226"
name: "PCI domain containing 2"
location: "13q34"
module: 28
arm: "+"
pooled_cpm: 62.15
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PCID2

*PCI domain containing 2* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +21.6, q 0e+00, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (LoVo 0.234×, SNU-1 0.159×, A-427 0.299×, CHP-212 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.341×, SW48 0.278×, RKO 0.360×, NCI-H1573 0.400×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (RPMI-7951 0.181×, NCI-H460 0.339×, C32 0.304×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.397×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.355×); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.139×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT5]] (+0.54, fdr 1e-05), [[ZNF638]] (+0.53, fdr 1e-05), [[ZNG1B]] (+0.53, fdr 3e-05); moves opposite to [[PLAA]] (-0.54, fdr 4e-05), [[MCU]] (-0.52, fdr 3e-05), [[TRAPPC10]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGAP44]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +21.6 | 0e+00 | 41/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +12.2 | 8e-32 | 37/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +11.3 | 4e-27 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +9.3 | 1e-18 | 32/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +9.0 | 3e-17 | 36/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +8.0 | 1e-13 | 35/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.9 | 2e-13 | 35/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +7.4 | 8e-12 | 35/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.8 | 8e-10 | 28/47 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.8 | 4e-07 | 25/48 (Panc 03.27, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 9e-07 | 26/48 (AsPC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.5 | 2e-06 | 24/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.2 | 7e-06 | 20/49 (A-172, RKO, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.8 | 7e-05 | 24/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +4.7 | 1e-04 | 22/48 (AsPC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 7e-04 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.058 | 8/47 (SW480, Panc 03.27, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.15× | +2.9 | 0.090 | 8/48 (NCI-H460, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4723.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (LoVo 0.234×, SNU-1 0.159×, A-427 0.299×, CHP-212 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.341×, SW48 0.278×, RKO 0.360×, NCI-H1573 0.400×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (RPMI-7951 0.181×, NCI-H460 0.339×, C32 0.304×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.397×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.355×); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 5 µM |  | 0.890× | -3.6 | 0.096 | 4/48 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | 0.841× | -3.5 | 0.096 | 20/45 (LoVo, SNU-1, …) | inconsistent across doses | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.096 | 14/48 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.841× | -3.3 | 0.12 | 10/48 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.870× | -3.0 | 0.23 | 12/48 (C32, NCI-H460, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.855× | -3.0 | 0.23 | 11/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 119 | 11 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.29× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 37.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +27.5) | — |
| [[A-427 (line)]] | wt | 100 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 95.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[RKO (line)]] | wt | 98.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +23.5) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A549 (line)]] | wt | 43.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +31.6) | — |
| [[C32 (line)]] | wt | 88.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -9.3) |
| [[PANC-1 (line)]] | alt | 51.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +33.1) | — |
| [[SW48 (line)]] | wt | 86.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A498 (line)]] | wt | 45.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +21.7) | — |
| [[J82 (line)]] | alt | 89.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +17.3) | — |
| [[LOX-IMVI (line)]] | wt | 87.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +23.0) | — |
| [[NCI-H2030 (line)]] | alt | 46.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +21.9) | — |
| [[NCI-H23 (line)]] | alt | 71.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW480 (line)]] | alt | 120 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.4) | — |
| [[A-172 (line)]] | wt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.50× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.436× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +19.7) | — |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 68.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[CFPAC-1 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +17.0) | — |
| [[CHP-212 (line)]] | wt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[COLO 205 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 43.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 84.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 51.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.6) | — |
| [[LoVo (line)]] | wt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[NCI-H596 (line)]] | alt | 71.6 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.139× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 57.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SNU-423 (line)]] | alt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.8) | — |
| [[SW 900 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT5]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ZNF638]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ZNG1B]] | +0.53 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[FNIP1]] | +0.52 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[SNAPC1]] | +0.51 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[TRMT13]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[HHLA3]] | +0.49 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[MPV17]] | +0.49 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[MTCH2]] | +0.48 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[ZC3H6]] | +0.48 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[GIGYF2]] | +0.47 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[SLC35E2B]] | +0.47 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAA]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[MCU]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TRAPPC10]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[KLHL25]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[NAPG]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[NFATC3]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CHUK]] | -0.48 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[OTULIN]] | -0.47 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SLC46A3]] | -0.46 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[SAP130]] | -0.45 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[AP4B1]] | -0.45 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[GDAP2]] | -0.45 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP44]] | B | ARHGAP44 activity raises PCID2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.24× lower at baseline in the lines without ARHGAP44 | 0.066 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[ASAP3]] | B | ASAP3 activity raises PCID2's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without ASAP3 | 0.090 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.0, 17.5); signed map (8.2, -15.2). **Vector** length 81.3, 16.9% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | +7.4 | -2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +7.3 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +21.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | +4.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +12.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -0.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -5.7 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -0.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -3.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | PCI domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,177,536-113,208,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11305 |
| Gene groups (HGNC) | Transcription and export complex 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JVF3](https://www.uniprot.org/uniprotkb/Q5JVF3) (PCI domain-containing protein 2):

> Required for B-cell survival through the regulation of the expression of cell-cycle checkpoint MAD2L1 protein during B cell differentiation (By similarity). As a component of the TREX-2 complex, involved in the export of mRNAs to the cytoplasm through the nuclear pores. Binds and stabilizes BRCA2 and is thus involved in the control of R-loop-associated DNA damage and transcription-associated genomic instability. Blocks the activity of the SRCAP chromatin remodeling complex by interacting with …

**Summary**, from NCBI Gene [55795](https://www.ncbi.nlm.nih.gov/gene/55795):

> This gene encodes a component of the TREX-2 complex (transcription and export complex 2), which regulates mRNA export from the nucleus. This protein regulates expression of Mad2 mitotic arrest deficient-like 1, a cell division checkpoint protein. This protein also interacts with and stabilizes Brca2 (breast cancer 2) protein. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:25653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25653) · Entrez [55795](https://www.ncbi.nlm.nih.gov/gene/55795) · UniProt [Q5JVF3](https://www.uniprot.org/uniprotkb/Q5JVF3) · Ensembl [ENSG00000126226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126226)

## Data

Gene col 4723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4723); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4723]; `tensor/DDL_lfc|DDL_z.npy` [4723]; `embed/gene_vectors.npy` [4723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4723 or target_col == 4723). Every well: [[PCID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
