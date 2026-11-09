---
symbol: "ABRAXAS2"
type: "gene"
col: 9159
ensembl_id: "ENSG00000165660"
name: "abraxas 2, BRISC complex subunit"
location: "10q26.13"
module: 11
arm: "+"
pooled_cpm: 26.11
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ABRAXAS2

*abraxas 2, BRISC complex subunit* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +21.8, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.541× (z -16.4, q 0e+00, down in 32 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.124×, NCI-H460 0.189×, PANC-1 0.352×, HT-29 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.155×, PANC-1 0.261×, NCI-H460 0.246×, KATO III 0.142×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (PANC-1 0.215×, hTERT-HPNE 0.127×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (BT-474 0.0926×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL14EP]] (+0.82, fdr 7e-06), [[RPP38]] (+0.79, fdr 7e-06), [[NME6]] (+0.76, fdr 7e-06); moves opposite to [[NPTN]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZFP30]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +21.8 | 0e+00 | 42/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +16.4 | 0e+00 | 42/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +16.0 | 0e+00 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +14.8 | 0e+00 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +10.7 | 1e-24 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +8.6 | 1e-15 | 28/48 (A498, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +7.8 | 7e-13 | 24/48 (A498, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +6.7 | 1e-09 | 22/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +6.5 | 5e-09 | 26/47 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +5.6 | 1e-06 | 18/47 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.3 | 8e-06 | 13/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +5.0 | 2e-05 | 15/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.9 | 4e-05 | 0/48 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.7 | 9e-05 | 14/48 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +4.5 | 3e-04 | 12/48 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.001 | 14/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.004 | 9/47 (MIA PaCa-2, SW 1271, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.016 | 5/47 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.025 | 7/47 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.036 | 4/48 (AsPC-1, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9159.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.124×, NCI-H460 0.189×, PANC-1 0.352×, HT-29 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.155×, PANC-1 0.261×, NCI-H460 0.246×, KATO III 0.142×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (PANC-1 0.215×, hTERT-HPNE 0.127×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (BT-474 0.0926×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.541×** | -16.4 | 0e+00 | 32/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -12.7 | 1e-34 | 24/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.662×** | -10.2 | 4e-22 | 25/40 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.802×** | -5.7 | 2e-06 | 22/47 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | 0.842× | -4.6 | 5e-04 | 19/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -4.3 | 0.001 | 15/48 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.871× | -3.7 | 0.019 | 6/48 (NCI-H661, PANC-1, …) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 5 µM |  | 0.873× | -3.5 | 0.035 | 4/47 (A498, CHP-212, …) | top dose only | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.883× | -3.2 | 0.094 | 4/48 (PANC-1, SW1417, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.8 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +17.7) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.6 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -20.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.0 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -27.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 26.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -17.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 23.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 22.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -15.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0926× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -11.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14EP]] | +0.82 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[RPP38]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[NME6]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[MRPL38]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[RPAP1]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[ZNF197]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.74 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.73 | +0.77 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP30]] | B | ZFP30 activity raises ABRAXAS2's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.12× lower at baseline in the lines without ZFP30 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.823). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.5, 6.3); signed map (1.4, -20.6). **Vector** length 96.6, 20.7% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +16.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +21.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +10.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -16.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | abraxas 2, BRISC complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,801,819-124,836,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Em:AC068896.4, ABRO1; previously KIAA0157, FAM175B |
| Gene groups (HGNC) | BRISC complex |
| Reactome | 2 pathways, smallest: Metalloprotease DUBs; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15018](https://www.uniprot.org/uniprotkb/Q15018) (BRISC complex subunit Abraxas 2):

> Component of the BRISC complex, a multiprotein complex that specifically cleaves 'Lys-63'-linked polyubiquitin, leaving the last ubiquitin chain attached to its substrates. May act as a central scaffold protein that assembles the various components of the BRISC complex and retains them in the cytoplasm. Plays a role in regulating the onset of apoptosis via its role in modulating 'Lys-63'-linked ubiquitination of target proteins (By similarity). Required for normal mitotic spindle assembly and …

**Summary**, from NCBI Gene [23172](https://www.ncbi.nlm.nih.gov/gene/23172):

> Enables microtubule binding activity and polyubiquitin modification-dependent protein binding activity. Involved in nuclear chromosome segregation; protein K63-linked deubiquitination; and response to ischemia. Located in cytosol; microtubule cytoskeleton; and midbody. Part of BRISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28975) · Entrez [23172](https://www.ncbi.nlm.nih.gov/gene/23172) · UniProt [Q15018](https://www.uniprot.org/uniprotkb/Q15018) · Ensembl [ENSG00000165660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165660)

## Data

Gene col 9159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9159); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9159]; `tensor/DDL_lfc|DDL_z.npy` [9159]; `embed/gene_vectors.npy` [9159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9159 or target_col == 9159). Every well: [[ABRAXAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABRAXAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
