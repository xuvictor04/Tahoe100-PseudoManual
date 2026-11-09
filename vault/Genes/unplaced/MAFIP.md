---
symbol: "MAFIP"
type: "gene"
col: 15831
ensembl_id: "ENSG00000274847"
name: "MAFF interacting protein"
location: "14 unplaced"
module: 89
arm: "+"
pooled_cpm: 49.52
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# MAFIP

*MAFF interacting protein* — 14 unplaced

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.21× (z +4.7, q 0.002, up in 17 of 41 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.24× (z +3.8, q 0.036, up in 16 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (A-427 2.61×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.345× (z -17.8, q 0e+00, down in 33 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.718× (z -8.1, q 4e-14, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEKT4P2-1]] (+0.72, fdr 7e-06), [[ZNF169]] (+0.69, fdr 7e-06), [[ZNF133]] (+0.67, fdr 7e-06); moves opposite to [[STK17B]] (-0.57, fdr 1e-05), [[EGR2]] (-0.56, fdr 1e-05), [[VCL]] (-0.55, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF234]] → it (grade C ⚠); 5 go from it, the strongest it → [[RNPC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (A-427 2.61×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.7 | 0.002 | 17/41 (C32, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.036 | 16/40 (A-427, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.046 | 14/41 (HepG2/C3A, C32, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.5 | 0.052 | 17/41 (A549, COLO 205, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.052 | 11/41 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.15× | +3.4 | 0.057 | 5/41 (SHP-77, NCI-H1573, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.21×** | +3.3 | 0.086 | 12/41 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.345×** | -17.8 | 0e+00 | 33/35 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.377×** | -17.0 | 0e+00 | 32/38 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.499×** | -11.2 | 1e-26 | 29/36 (C-33 A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.655×** | -10.4 | 5e-23 | 31/40 (C32, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.561×** | -9.7 | 5e-20 | 36/41 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -8.1 | 4e-14 | 31/41 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -7.5 | 4e-12 | 5/42 (HCT15, COLO 205, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.690×** | -6.4 | 9e-09 | 26/40 (NCI-H460, SNU-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.683×** | -6.4 | 1e-08 | 25/40 (SHP-77, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -6.0 | 9e-08 | 23/41 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **0.737×** | -5.3 | 6e-06 | 24/39 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.763×** | -4.7 | 1e-04 | 23/40 (C32, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.769×** | -4.6 | 2e-04 | 21/41 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.802×** | -3.8 | 0.005 | 19/41 (HCT15, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.813×** | -3.6 | 0.013 | 15/41 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.016 | 14/41 (COLO 205, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.771×** | -3.2 | 0.039 | 18/38 (AsPC-1, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.824×** | -3.1 | 0.054 | 14/40 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.0 | 0 | 11 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 80.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -14.8) |
| [[A549 (line)]] | wt | 34.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.6) ⚠ cell-cycle shift, explains ~75% of this change |
| [[C32 (line)]] | wt | 84.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -23.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.8) |
| [[A-172 (line)]] | wt | 44.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -15.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.3) |
| [[A-427 (line)]] | wt | 63.2 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0842× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 72.0 | 0 | 3 (2 ⚠) | — | [[OTS514 (drug)]] 5 µM 0.0804× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 69.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H2347 (line)]] | alt | 35.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -17.0) |
| [[PANC-1 (line)]] | alt | 61.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 66.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0699× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -17.1) |
| [[SW480 (line)]] | alt | 165 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 56.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0669× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0503× (z -29.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 64.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 81.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.220× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.139× (z -9.4) |
| [[CHP-212 (line)]] | wt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H661 (line)]] | alt | 91.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0589× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 18.6 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0684× (z -12.0) |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEKT4P2-1]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZNF169]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SLC25A17]] | +0.65 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[UQCC1]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[APTX]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[METTL22]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PSMF1]] | +0.63 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[TEFM]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[MED9]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[CTU1]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ELMOD3]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK17B]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[EGR2]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[VCL]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[BMAL1]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF234]] | C | ZNF234 activity raises MAFIP's level | lines that do not express ZNF234 (4) vs lines expressing it (46) | 3.83× lower at baseline in the lines without ZNF234 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF222, ZNF551, ZNF264 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNPC3]] | B | MAFIP activity raises RNPC3's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without MAFIP | 0.010 | ⚠ within organs, on part of the lines |
| [[TEFM]] | B | MAFIP activity raises TEFM's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without MAFIP | 0.025 | ⚠ within organs, on part of the lines |
| [[ZBTB26]] | B | MAFIP activity raises ZBTB26's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without MAFIP | 0.071 | ⚠ within organs, on part of the lines |
| [[LYSMD1]] | B | MAFIP activity raises LYSMD1's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without MAFIP | 0.088 | ⚠ within organs, on part of the lines |
| [[GTPBP10]] | B | MAFIP activity raises GTPBP10's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.21× lower at baseline in the lines without MAFIP | 0.094 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.6, -6.5); signed map (-15.3, -18.9). **Vector** length 75.2, 15.5% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | -1.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.6 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.1 | -10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -8.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | -2.2 | -6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAFF interacting protein |
| Locus type | unknown (other) |
| Location | 14 unplaced — chrGL000194.1:53,594-115,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35473, FLJ00219, FLJ39633, MIP, pp5644, TEKT4P4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ33](https://www.uniprot.org/uniprotkb/Q8WZ33) (MaFF-interacting protein):

> Acts as a coactivator of MAFF transcriptional activity. Inhibits cell growth and colony-forming efficiency.

**Summary**, from NCBI Gene [727764](https://www.ncbi.nlm.nih.gov/gene/727764):

> This gene was originally thought to be a protein coding gene. However, the encoded protein sequence is highly similar to the C-terminal sequence of the tektin-4 protein, and the transcript sequences of this gene are highly similar to the TEKT4 pseudogenes, which are found on chromosomes 4, 21 and Y, respectively. Therefore, this gene is thought to be another pseudogene of the TEKT4 gene (GeneID:150483). Multiple alternatively spliced transcript variants have been found for this gene. [provided …

**Accessions** — [HGNC:31102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31102) · Entrez [727764](https://www.ncbi.nlm.nih.gov/gene/727764) · UniProt [Q8WZ33](https://www.uniprot.org/uniprotkb/Q8WZ33) · Ensembl [ENSG00000274847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274847)

## Data

Gene col 15831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15831); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15831]; `tensor/DDL_lfc|DDL_z.npy` [15831]; `embed/gene_vectors.npy` [15831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15831 or target_col == 15831). Every well: [[MAFIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAFIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
