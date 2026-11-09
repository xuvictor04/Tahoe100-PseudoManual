---
symbol: "MTCL1"
type: "gene"
col: 9663
ensembl_id: "ENSG00000168502"
name: "microtubule crosslinking factor 1"
location: "18p11.22"
module: 195
arm: "+"
pooled_cpm: 92.84
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# MTCL1

*microtubule crosslinking factor 1* — 18p11.22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 2.56×, HT-29 2.24×, LS 180 2.83×; ⚠ cell-cycle shift, explains ~68% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.63×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 2.54×; ⚠ cell-cycle shift, explains ~47% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.665× (z -8.2, q 1e-13, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICAL3]] (+0.61, fdr 7e-06), [[SLC4A7]] (+0.58, fdr 1e-05), [[SMS]] (+0.57, fdr 1e-05); moves opposite to [[COPS5]] (-0.51, fdr 3e-05), [[AZI2]] (-0.51, fdr 3e-05), [[SECISBP2L]] (-0.51, fdr 4e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MGAT5B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GARNL3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 2.56×, HT-29 2.24×, LS 180 2.83×; ⚠ cell-cycle shift, explains ~68% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.63×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 2.54×; ⚠ cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Brivudine (drug)]] 5 µM |  | 1.63× | +3.6 | 0.15 | 20/48 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.26× | +3.3 | 0.23 | 21/47 (HT-29, A498, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.2 | 0.23 | 17/47 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 1.17× | +3.1 | 0.27 | 17/47 (NCI-H2347, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.665×** | -8.2 | 1e-13 | 33/47 (RKO, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -7.6 | 7e-12 | 32/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -7.0 | 4e-10 | 31/47 (SNU-1, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -6.2 | 1e-07 | 28/45 (MIA PaCa-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -5.0 | 7e-05 | 25/47 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -4.9 | 8e-05 | 29/49 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.712×** | -4.8 | 1e-04 | 25/47 (MIA PaCa-2, A-172, …) | two highest doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.793×** | -4.7 | 2e-04 | 26/47 (A-172, LOX-IMVI, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -4.6 | 2e-04 | 24/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.706×** | -4.6 | 2e-04 | 26/44 (C-33 A, SHP-77, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -4.6 | 3e-04 | 26/47 (A-172, LOX-IMVI, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.643×** | -4.5 | 3e-04 | 28/47 (CHP-212, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.733×** | -4.4 | 4e-04 | 27/47 (SW48, LOX-IMVI, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -4.4 | 5e-04 | 24/47 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.731×** | -4.3 | 7e-04 | 24/46 (A-172, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.007 | 22/47 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.612×** | -3.7 | 0.008 | 20/48 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.009 | 23/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.045 | 17/47 (A498, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.045 | 19/47 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.674×** | -2.9 | 0.080 | 20/47 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 233 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -19.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.211× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 206 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -16.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -12.1) |
| [[PANC-1 (line)]] | alt | 157 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -12.3) |
| [[SW48 (line)]] | wt | 94.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.9) |
| [[A549 (line)]] | wt | 188 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -14.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -8.8) |
| [[RKO (line)]] | wt | 88.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.134× (z -15.0) |
| [[HOP62 (line)]] | alt | 179 | 1 (1 ⚠) | 4 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +12.6) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.200× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.232× (z -10.5) |
| [[A-427 (line)]] | wt | 165 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.6) |
| [[HS-578T (line)]] | alt | 67.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 69.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -10.1) |
| [[C32 (line)]] | wt | 59.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 75.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.396× (z -9.4) |
| [[HT-29 (line)]] | alt | 42.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[J82 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.2) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.476× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 74.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -9.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.343× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.332× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.270× (z -10.0) |
| [[SNU-1 (line)]] | wt | 59.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -13.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0895× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 57.6 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0757× (z -8.6) |
| [[LoVo (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +13.2) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LS 180 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[Panc 03.27 (line)]] | alt | 89.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.413× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.392× (z -8.7) |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A498 (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICAL3]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SLC4A7]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SMS]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MGAT5B]] | +0.53 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TRIO]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CTPS1]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[VAV2]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PPM1G]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[NLN]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TBC1D4]] | +0.51 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[WWC2]] | +0.51 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[KIRREL3]] | +0.51 | +0.54 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS5]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[AZI2]] | -0.51 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[SECISBP2L]] | -0.51 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[GOLPH3L]] | -0.49 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CWC15]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CCNG2]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[BPNT1]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PREPL]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ATOSA]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CIR1]] | -0.46 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TMEM59]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[BCAS2]] | -0.46 | -0.38 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT5B]] | B | MGAT5B activity raises MTCL1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without MGAT5B | 0.040 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL |
| [[SH3TC1]] | B | SH3TC1 activity lowers MTCL1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 1.90× higher at baseline in the lines without SH3TC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[LOXL2]] | B | LOXL2 activity raises MTCL1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without LOXL2 | 0.098 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GARNL3]] | C | MTCL1's natural level strengthens GARNL3's drug response | MTCL1's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.18; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.3, 10.3); signed map (-0.3, 54.8). **Vector** length 115, 33.4% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.2 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.5 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.4 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.7 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.5 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.8 | -1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | microtubule crosslinking factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:8,705,556-8,832,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0802, CCDC165, SOGA2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4B5](https://www.uniprot.org/uniprotkb/Q9Y4B5) (Microtubule cross-linking factor 1):

> Microtubule-associated factor involved in the late phase of epithelial polarization and microtubule dynamics regulation. Plays a role in the development and maintenance of non-centrosomal microtubule bundles at the lateral membrane in polarized epithelial cells. Required for faithful chromosome segregation during mitosis.

**Summary**, from NCBI Gene [23255](https://www.ncbi.nlm.nih.gov/gene/23255):

> Enables microtubule binding activity. Involved in chromosome segregation. Located in kinetochore; midbody; and spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29121) · Entrez [23255](https://www.ncbi.nlm.nih.gov/gene/23255) · UniProt [Q9Y4B5](https://www.uniprot.org/uniprotkb/Q9Y4B5) · Ensembl [ENSG00000168502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168502)

## Data

Gene col 9663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9663); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9663]; `tensor/DDL_lfc|DDL_z.npy` [9663]; `embed/gene_vectors.npy` [9663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9663 or target_col == 9663). Every well: [[MTCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
