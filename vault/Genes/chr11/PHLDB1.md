---
symbol: "PHLDB1"
type: "gene"
col: 310
ensembl_id: "ENSG00000019144"
name: "pleckstrin homology like domain family B member 1"
location: "11q23.3"
module: 13
arm: "+"
pooled_cpm: 25.95
n_lines_expressing: 46
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PHLDB1

*pleckstrin homology like domain family B member 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +8.7, q 1e-15, up in 24 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (PANC-1 4.24×, NCI-H460 4.62×, NCI-H2347 6.02×, NCI-H23 5.10×, …); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 5.10×, NCI-H460 5.48×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.16×; ⚠ cell-cycle shift, explains ~10% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.479× (z -9.7, q 1e-19, down in 33 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.543× (z -8.1, q 2e-13, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL7A1]] (+0.65, fdr 7e-06), [[PRR7]] (+0.62, fdr 1e-05), [[EGR3]] (+0.60, fdr 1e-05); moves opposite to [[GNAI1]] (-0.52, fdr 3e-05), [[ASAH1]] (-0.48, fdr 4e-05), [[MBNL2]] (-0.48, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FRMD4A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FIBP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 310.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (PANC-1 4.24×, NCI-H460 4.62×, NCI-H2347 6.02×, NCI-H23 5.10×, …); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 5.10×, NCI-H460 5.48×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.16×; ⚠ cell-cycle shift, explains ~10% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +8.7 | 1e-15 | 24/43 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.045 | 18/44 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.34 | 10/44 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -9.7 | 1e-19 | 33/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.543×** | -8.1 | 2e-13 | 32/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -7.0 | 4e-10 | 26/43 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -6.9 | 6e-10 | 29/44 (SW480, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -6.7 | 2e-09 | 28/44 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.638×** | -5.9 | 3e-07 | 25/44 (SW480, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -5.4 | 5e-06 | 23/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.671×** | -5.3 | 9e-06 | 23/44 (A-172, HOP62, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -5.1 | 2e-05 | 24/42 (RPMI-7951, C-33 A, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.712×** | -4.2 | 0.002 | 20/35 (MIA PaCa-2, H4, …) | all doses, flat | composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **0.743×** | -3.9 | 0.004 | 15/44 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.581×** | -3.8 | 0.008 | 16/43 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.761×** | -3.6 | 0.014 | 20/39 (HepG2/C3A, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.701×** | -3.5 | 0.015 | 17/30 (Panc 03.27, HEC-1-A, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.015 | 14/44 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.022 | 20/44 (C32, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -3.3 | 0.028 | 17/43 (RPMI-7951, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.039 | 13/43 (H4, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.069 | 19/44 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.748×** | -2.9 | 0.096 | 13/44 (HOP62, SW 1271, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.360× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -9.7) |
| [[HOP62 (line)]] | alt | 45.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 14.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +15.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0568× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 38.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +18.0) | — |
| [[H4 (line)]] | wt | 40.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -8.6) |
| [[KATO III (line)]] | alt | 11.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +14.4) | [[Digitoxin (drug)]] 0.5 µM 0.154× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 8.58 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +15.2) | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0753× (z -12.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.122× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +13.6) | — |
| [[C32 (line)]] | wt | 77.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[Hs 766T (line)]] | wt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H1573 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0998× (z -9.0) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +9.4) | — |
| [[A-172 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL7A1]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 | same gene group |
| [[PRR7]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[EGR3]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[STK10]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.59 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[APCDD1L]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CSPG4]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FMNL3]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SH2B3]] | +0.57 | +0.54 / +0.62 | both halves | 1e-05 | same gene group |
| [[SALL1]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ARNT2]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[NANOS3]] | +0.56 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI1]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ASAH1]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MBNL2]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[FNTB]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZNF148]] | -0.47 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R12B]] | -0.46 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4A]] | B | FRMD4A activity raises PHLDB1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without FRMD4A | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[CSPG4]] | B | CSPG4 activity raises PHLDB1's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.22× lower at baseline in the lines without CSPG4 | 0.054 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[HTR7]] | B | HTR7 activity raises PHLDB1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without HTR7 | 0.057 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[COL7A1]] | B | COL7A1 activity raises PHLDB1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 1.89× lower at baseline in the lines without COL7A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[ROBO4]] | B | ROBO4 activity raises PHLDB1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without ROBO4 | 0.075 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[CSPG4]] | B | CSPG4 activity strengthens PHLDB1's drug response | lines that do not express CSPG4 (27) vs lines expressing it (17) | the lines without CSPG4 respond 0.76× as strongly (z diff +1.05); strongest at Idarubicin (hydrochloride) 5 µM: 0.83x vs 0.53x (z diff +3.7) | 0.091 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; target measured in part of the lines; artifact flags |
| [[LTBP3]] | C | LTBP3 activity raises PHLDB1's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without LTBP3 | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FIBP]] | C | PHLDB1 activity raises FIBP's level | lines that do not express PHLDB1 (4) vs lines expressing it (46) | 1.10× lower at baseline in the lines without PHLDB1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NUAK1, MYBL1, C12orf75; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, -2.4); signed map (2.9, 29.8). **Vector** length 100, 24.1% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +2.6 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.3 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.8 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology like domain family B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,606,440-118,658,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00141, LL5a, KIAA0638 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

UniProt [Q86UU1](https://www.uniprot.org/uniprotkb/Q86UU1) carries no function annotation.

**Summary**, from NCBI Gene [23187](https://www.ncbi.nlm.nih.gov/gene/23187):

> Involved in basement membrane organization. Located in basal cortex. Implicated in osteogenesis imperfecta. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23697) · Entrez [23187](https://www.ncbi.nlm.nih.gov/gene/23187) · UniProt [Q86UU1](https://www.uniprot.org/uniprotkb/Q86UU1) · Ensembl [ENSG00000019144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019144)

## Data

Gene col 310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 310); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 310]; `tensor/DDL_lfc|DDL_z.npy` [310]; `embed/gene_vectors.npy` [310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 310 or target_col == 310). Every well: [[PHLDB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLDB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
