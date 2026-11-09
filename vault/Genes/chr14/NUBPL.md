---
symbol: "NUBPL"
type: "gene"
col: 7516
ensembl_id: "ENSG00000151413"
name: "NUBP iron-sulfur cluster assembly factor, mitochondrial"
location: "14q12"
module: 1
arm: "+"
pooled_cpm: 71.68
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NUBPL

*NUBP iron-sulfur cluster assembly factor, mitochondrial* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.44× (z +8.4, q 3e-14, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.30× (z +4.2, q 0.004, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 1.89×, C-33 A 2.07×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 2 lines (C32 2.25×, Hs 766T 2.13×; ⚠ cell-cycle shift, explains ~52% of this change).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.379× (z -15.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUFIP1]] (+0.78, fdr 7e-06), [[RRP15]] (+0.70, fdr 7e-06), [[TASP1]] (+0.69, fdr 7e-06); moves opposite to [[PDE6D]] (-0.61, fdr 2e-05), [[RAB4B]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7516.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 1.89×, C-33 A 2.07×; ⚠ cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 2 lines (C32 2.25×, Hs 766T 2.13×; ⚠ cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.44×** | +8.4 | 3e-14 | 36/48 (C32, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.30×** | +4.3 | 0.004 | 30/48 (Panc 03.27, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.004 | 26/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.079 | 21/48 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.23× | +3.2 | 0.15 | 19/48 (C32, SW 900, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.23× | +3.1 | 0.18 | 16/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -15.6 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -13.7 | 4e-40 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -12.1 | 1e-31 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -11.9 | 2e-30 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -9.9 | 4e-21 | 39/48 (C-33 A, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.574×** | -8.9 | 4e-17 | 43/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.592×** | -8.1 | 4e-14 | 35/47 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -7.7 | 7e-13 | 37/47 (MIA PaCa-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -7.4 | 1e-11 | 35/49 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.638×** | -7.0 | 2e-10 | 33/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -6.5 | 3e-09 | 31/48 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -6.3 | 2e-08 | 31/50 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -5.8 | 3e-07 | 30/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.512×** | -5.6 | 7e-07 | 29/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.795×** | -5.2 | 7e-06 | 22/48 (A498, SNU-423, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.599×** | -4.3 | 5e-04 | 30/48 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.757×** | -4.2 | 6e-04 | 26/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.003 | 23/47 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.851× | -3.7 | 0.005 | 13/49 (Panc 03.27, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.852× | -3.6 | 0.006 | 18/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.662×** | -3.5 | 0.010 | 26/48 (NCI-H23, RKO, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 116 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -16.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.220× (z -15.0) |
| [[PANC-1 (line)]] | alt | 57.8 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -20.0) |
| [[SW480 (line)]] | alt | 89.5 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -18.5) |
| [[SHP-77 (line)]] | alt | 136 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -13.1) |
| [[J82 (line)]] | alt | 71.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -12.4) |
| [[HOP62 (line)]] | alt | 69.5 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -11.6) |
| [[SNU-423 (line)]] | alt | 68.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.255× (z -12.0) |
| [[BT-474 (line)]] | alt | 78.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 56.4 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -12.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -10.5) |
| [[A498 (line)]] | wt | 51.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.8) |
| [[LoVo (line)]] | wt | 76.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.289× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -17.8) |
| [[A-427 (line)]] | wt | 91.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.342× (z -12.8) |
| [[LS 180 (line)]] | wt | 68.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 66.7 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -10.1) |
| [[A549 (line)]] | wt | 62.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 79.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.25× (z +10.5) ⚠ cell-cycle shift, explains ~52% of this change | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 84.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.351× (z -8.6) |
| [[HCT15 (line)]] | alt | 75.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -10.8) |
| [[RKO (line)]] | wt | 81.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -11.2) |
| [[C-33 A (line)]] | alt | 84.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.223× (z -13.3) |
| [[COLO 205 (line)]] | alt | 68.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.226× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 62.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.396× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -9.1) |
| [[SNU-1 (line)]] | wt | 84.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -10.6) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.436× (z -9.4) |
| [[CHP-212 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HEC-1-A (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -9.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 54.1 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.13× (z +9.1) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 52.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 53.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.303× (z -9.3) |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 1 | — | [[Vandetanib (drug)]] 5 µM 0.0637× (z -8.9) |
| [[SW 1271 (line)]] | alt | 90.7 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0833× (z -10.1) |
| [[SW48 (line)]] | wt | 103 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.4) |
| [[A-172 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUFIP1]] | +0.78 | +0.72 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[RRP15]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TASP1]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SMARCAD1]] | +0.68 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[NARS2]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NOL10]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.66 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.65 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[DDX10]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SLX4IP]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LDAH]] | +0.65 | +0.73 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE6D]] | -0.61 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[RAB4B]] | -0.54 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.8, -39.9); signed map (-3.7, -41.7). **Vector** length 100, 32.6% of its response variance represented; |z| ≥ 3 in 1,286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +7.6 | +8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +5.3 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.6 | -4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | NUBP iron-sulfur cluster assembly factor, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:31,489,956-31,861,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12660, IND1, huInd1; previously C14orf127 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Mitochondrial iron-sulfur assembly components |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB37](https://www.uniprot.org/uniprotkb/Q8TB37) (Iron-sulfur cluster transfer protein NUBPL):

> Iron-sulfur cluster transfer protein involved in the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I). May deliver one or more Fe-S clusters to complex I subunits.

**Summary**, from NCBI Gene [80224](https://www.ncbi.nlm.nih.gov/gene/80224):

> This gene encodes a member of the Mrp/NBP35 ATP-binding proteins family. The encoded protein is required for the assembly of the respiratory chain NADH dehydrogenase (complex I), an oligomeric enzymatic complex located in the inner mitochondrial membrane. Mutations in this gene cause mitochondrial complex I deficiency. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:20278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20278) · Entrez [80224](https://www.ncbi.nlm.nih.gov/gene/80224) · UniProt [Q8TB37](https://www.uniprot.org/uniprotkb/Q8TB37) · Ensembl [ENSG00000151413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151413)

## Data

Gene col 7516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7516); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7516]; `tensor/DDL_lfc|DDL_z.npy` [7516]; `embed/gene_vectors.npy` [7516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7516 or target_col == 7516). Every well: [[NUBPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUBPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
