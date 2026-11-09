---
symbol: "TNRC18"
type: "gene"
col: 11238
ensembl_id: "ENSG00000182095"
name: "trinucleotide repeat containing 18"
location: "7p22.1"
module: 17
arm: "-"
pooled_cpm: 153.4
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 47
n_dd_up_clean: 0
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TNRC18

*trinucleotide repeat containing 18* — 7p22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.54×, C32 2.36×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.32×; ⚠ cell-cycle shift, explains ~25% of this change).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.404× (z -21.0, q 0e+00, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.282× (z -20.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCC2]] (+0.60, fdr 1e-05), [[ALDH16A1]] (+0.54, fdr 4e-05), [[LEMD3]] (+0.54, fdr 2e-04); moves opposite to [[RBM11]] (-0.55, fdr 3e-05), [[TTLL7]] (-0.54, fdr 3e-05), [[SH3PXD2B]] (-0.54, fdr 4e-04).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.54×, C32 2.36×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.32×; ⚠ cell-cycle shift, explains ~25% of this change).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.404×** | -21.0 | 0e+00 | 41/48 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.282×** | -20.7 | 0e+00 | 48/48 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.283×** | -20.7 | 0e+00 | 48/48 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.316×** | -18.9 | 0e+00 | 48/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -15.0 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.478×** | -12.1 | 2e-31 | 48/48 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.491×** | -11.6 | 2e-29 | 43/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.458×** | -11.4 | 2e-28 | 44/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.506×** | -11.1 | 6e-27 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.524×** | -10.6 | 3e-24 | 44/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.531×** | -10.4 | 2e-23 | 43/48 (LoVo, HT-29, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.529×** | -9.8 | 3e-21 | 45/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.337×** | -9.3 | 6e-19 | 48/49 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -8.1 | 2e-14 | 44/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.635×** | -7.4 | 5e-12 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -7.2 | 2e-11 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -6.1 | 3e-08 | 33/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -6.1 | 3e-08 | 30/48 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -5.5 | 7e-07 | 32/48 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.529×** | -5.4 | 1e-06 | 42/49 (SW1417, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 178 | 0 | 21 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -18.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -17.3) |
| [[LoVo (line)]] | wt | 373 | 0 | 18 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0658× (z -25.3) |
| [[SW480 (line)]] | alt | 174 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -21.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.223× (z -16.8) |
| [[PANC-1 (line)]] | alt | 223 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -20.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -19.6) |
| [[HT-29 (line)]] | alt | 216 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -18.1) |
| [[LS 180 (line)]] | wt | 177 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 77.0 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -19.2) |
| [[COLO 205 (line)]] | alt | 162 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.162× (z -15.6) |
| [[HS-578T (line)]] | alt | 90.3 | 0 | 10 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0530× (z -14.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.261× (z -12.8) |
| [[KATO III (line)]] | alt | 293 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -24.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.320× (z -14.5) |
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -20.2) |
| [[MIA PaCa-2 (line)]] | alt | 168 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -19.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.241× (z -16.7) |
| [[SW 900 (line)]] | alt | 137 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -19.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.277× (z -11.6) |
| [[A-427 (line)]] | wt | 181 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 158 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.158× (z -13.1) |
| [[BT-474 (line)]] | alt | 168 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -15.9) |
| [[SW1417 (line)]] | alt | 175 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -16.7) |
| [[H4 (line)]] | wt | 300 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.390× (z -10.3) |
| [[HOP62 (line)]] | alt | 89.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -18.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.369× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 118 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +18.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Panobinostat (drug)]] 5 µM 0.249× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 153 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.267× (z -13.9) |
| [[A-172 (line)]] | wt | 123 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -17.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -16.4) |
| [[A498 (line)]] | wt | 196 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -11.7) |
| [[AN3 CA (line)]] | alt | 194 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.318× (z -13.4) |
| [[A549 (line)]] | wt | 111 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -23.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.327× (z -11.5) |
| [[C32 (line)]] | wt | 81.0 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -10.6) |
| [[HCT15 (line)]] | alt | 151 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 68.7 | 0 | 5 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0766× (z -11.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 82.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -15.2) |
| [[SHP-77 (line)]] | alt | 125 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.371× (z -10.9) |
| [[SNU-423 (line)]] | alt | 94.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -12.9) |
| [[C-33 A (line)]] | alt | 213 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -20.4) |
| [[RKO (line)]] | wt | 84.2 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -11.3) |
| [[SNU-1 (line)]] | wt | 121 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.354× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 115 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 84.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -11.2) |
| [[Hs 766T (line)]] | wt | 137 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.363× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.392× (z -8.5) |
| [[SW48 (line)]] | wt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -12.6) |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.191× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -16.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CHP-212 (line)]] | wt | 91.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -8.9) |
| [[J82 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 1088 (line)]] | alt | 153 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0977× (z -9.5) |
| [[SW 1271 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC2]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ALDH16A1]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[LEMD3]] | +0.54 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[NACC2]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SAFB]] | +0.53 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[PHF2]] | +0.53 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[ANKMY1]] | +0.52 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SMAD6]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ZNF362]] | +0.51 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[SEPTIN9-DT]] | +0.51 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[PLXNB1]] | +0.51 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[OARD1]] | +0.51 | +0.19 / +0.50 | ⚠ not reproduced | 8e-04 |  |
| [[SETD1B]] | +0.51 | +0.31 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM11]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TTLL7]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | -0.54 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[CYB5R1]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ESD]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MOCS2]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TBC1D19]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[PIGH]] | -0.51 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[CYB5R4]] | -0.51 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[SOGA3]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[DTNA]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[FAM241B]] | -0.48 | -0.37 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.5, 11.9); signed map (27.1, -25.4). **Vector** length 96.6, 35.5% of its response variance represented; |z| ≥ 3 in 1,602 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | -1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -9.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -10.4 |

## What is on record

|  |  |
|---|---|
| Name | trinucleotide repeat containing 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,306,790-5,425,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAGL79, TNRC18A, KIAA1856 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15417](https://www.uniprot.org/uniprotkb/O15417) (Trinucleotide repeat-containing gene 18 protein):

> Chromatin reader involved in the silencing of endogenous retroviruses (ERV) class-I elements, such as LTR12. Specifically binds histone H3 trimethylated at 'Lys-9' (H3K9me3) deposited by SETB1 at class-I ERV and directly mediates recruitment of corepressor complexes, such as Sin3-type and N-Cor complexes, leading to ERV silencing.

**Summary**, from NCBI Gene [84629](https://www.ncbi.nlm.nih.gov/gene/84629):

> Enables histone H3K9me2/3 reader activity. Involved in protein localization to chromatin and transposable element silencing by heterochromatin formation. Located in cytosol; mitochondrion; and nucleus. Is active in chromatin and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11962) · Entrez [84629](https://www.ncbi.nlm.nih.gov/gene/84629) · UniProt [O15417](https://www.uniprot.org/uniprotkb/O15417) · Ensembl [ENSG00000182095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182095)

## Data

Gene col 11238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11238); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11238]; `tensor/DDL_lfc|DDL_z.npy` [11238]; `embed/gene_vectors.npy` [11238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11238 or target_col == 11238). Every well: [[TNRC18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNRC18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
