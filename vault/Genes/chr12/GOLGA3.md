---
symbol: "GOLGA3"
type: "gene"
col: 1632
ensembl_id: "ENSG00000090615"
name: "golgin A3"
location: "12q24.33"
module: 52
arm: "+"
pooled_cpm: 143.58
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# GOLGA3

*golgin A3* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.27× (z +3.9, q 0.064, up in 24 of 44 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.34×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.415× (z -14.3, q 8e-44, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHFR]] (+0.75, fdr 7e-06, ⚠ same locus), [[LRRC59]] (+0.74, fdr 7e-06), [[COL20A1]] (+0.72, fdr 7e-06), [[DPP9]] (+0.72, fdr 7e-06); moves opposite to [[SPPL3]] (-0.64, fdr 1e-05), [[ABCB7]] (-0.60, fdr 1e-05), [[CHIC1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1632.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.34×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.9 | 0.064 | 24/44 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.23× | +3.5 | 0.13 | 25/49 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.22× | +3.4 | 0.13 | 19/48 (C32, A-427, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.415×** | -14.3 | 8e-44 | 44/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -13.7 | 4e-40 | 44/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.512×** | -11.4 | 1e-27 | 37/48 (HOP62, H4, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.683×** | -9.1 | 9e-18 | 32/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.583×** | -8.8 | 2e-16 | 42/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.727×** | -7.6 | 2e-12 | 43/48 (RKO, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.6 | 3e-12 | 42/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.672×** | -6.7 | 1e-09 | 33/48 (H4, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -6.7 | 1e-09 | 39/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.696×** | -6.1 | 5e-08 | 32/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.702×** | -6.0 | 1e-07 | 32/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.704×** | -5.9 | 1e-07 | 34/48 (A498, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.715×** | -5.7 | 6e-07 | 35/49 (CHP-212, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.732×** | -5.3 | 5e-06 | 27/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -4.5 | 3e-04 | 28/48 (A498, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -3.9 | 0.003 | 25/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.856× | -3.7 | 0.006 | 14/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.010 | 25/48 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.048 | 22/48 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.886× | -2.9 | 0.088 | 12/48 (J82, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 218 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -15.1) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.310× (z -12.6) |
| [[HOP62 (line)]] | alt | 161 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.281× (z -13.5) |
| [[A-172 (line)]] | wt | 136 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -17.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -13.4) |
| [[BT-474 (line)]] | alt | 163 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[H4 (line)]] | wt | 218 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.217× (z -12.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 183 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.305× (z -10.7) |
| [[SW 900 (line)]] | alt | 179 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.334× (z -10.4) |
| [[SW480 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.385× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -18.6) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.239× (z -12.5) |
| [[Hs 766T (line)]] | wt | 143 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 185 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.419× (z -10.4) |
| [[A549 (line)]] | wt | 154 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.275× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.327× (z -12.4) |
| [[PANC-1 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.412× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.402× (z -9.6) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.425× (z -8.8) |
| [[A-427 (line)]] | wt | 89.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +9.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.423× (z -9.8) |
| [[KATO III (line)]] | alt | 151 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.376× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.511× (z -8.5) |
| [[LoVo (line)]] | wt | 236 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 144 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.341× (z -10.8) |
| [[RKO (line)]] | wt | 112 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.374× (z -9.7) |
| [[SW1417 (line)]] | alt | 89.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.428× (z -8.9) |
| [[A498 (line)]] | wt | 228 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.469× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.426× (z -9.5) |
| [[COLO 205 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.238× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.417× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -11.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.468× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 121 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.367× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.397× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 83.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.204× (z -8.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.412× (z -10.1) |
| [[SW 1088 (line)]] | alt | 157 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0681× (z -12.2) |
| [[AN3 CA (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 74.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHFR]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LRRC59]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[COL20A1]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[DPP9]] | +0.72 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[TAF13]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[YKT6]] | +0.72 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[UVSSA]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RER1]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[PMM2]] | +0.71 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[GDI2]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.70 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[COPG1]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[ABCB7]] | -0.60 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[CHIC1]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.56 | -0.41 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.817). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.8, -28.3); signed map (-50.8, 3.6). **Vector** length 140, 51.0% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.8 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.6 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.8 | -7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.2 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -14.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | golgin A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,768,902-132,829,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | golgin-160, GCP170, MEA-2 |
| Gene groups (HGNC) | Golgins |
| Reactome | 4 pathways, smallest: RND2 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08378](https://www.uniprot.org/uniprotkb/Q08378) (Golgin subfamily A member 3):

> Golgi auto-antigen; probably involved in maintaining Golgi structure.

**Summary**, from NCBI Gene [2802](https://www.ncbi.nlm.nih.gov/gene/2802):

> The Golgi apparatus, which participates in glycosylation and transport of proteins and lipids in the secretory pathway, consists of a series of stacked cisternae (flattened membrane sacs). Interactions between the Golgi and microtubules are thought to be important for the reorganization of the Golgi after it fragments during mitosis. This gene encodes a member of the golgin family of proteins which are localized to the Golgi. Its encoded protein has been postulated to play a role in nuclear …

**Accessions** — [HGNC:4426](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4426) · Entrez [2802](https://www.ncbi.nlm.nih.gov/gene/2802) · UniProt [Q08378](https://www.uniprot.org/uniprotkb/Q08378) · Ensembl [ENSG00000090615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090615)

## Data

Gene col 1632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1632); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1632]; `tensor/DDL_lfc|DDL_z.npy` [1632]; `embed/gene_vectors.npy` [1632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1632 or target_col == 1632). Every well: [[GOLGA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
