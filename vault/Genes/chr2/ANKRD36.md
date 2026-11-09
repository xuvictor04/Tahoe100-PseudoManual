---
symbol: "ANKRD36"
type: "gene"
col: 5795
ensembl_id: "ENSG00000135976"
name: "ankyrin repeat domain 36"
location: "2q11.2"
module: 175
arm: "+"
pooled_cpm: 143.17
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ANKRD36

*ankyrin repeat domain 36* — 2q11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.283× (z -18.2, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.398× (z -13.2, q 3e-37, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD36B]] (+0.83, fdr 7e-06), [[XYLB]] (+0.64, fdr 1e-05), [[ANKRD36C]] (+0.62, fdr 7e-06); moves opposite to [[GPRC5C]] (-0.52, fdr 3e-04), [[GPANK1]] (-0.51, fdr 3e-05), [[MED13]] (-0.50, fdr 1e-04).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SMIM31]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.283×** | -18.2 | 0e+00 | 46/48 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.398×** | -13.2 | 3e-37 | 46/49 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.271×** | -13.1 | 6e-37 | 46/48 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.388×** | -9.9 | 7e-21 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -9.0 | 2e-17 | 42/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.442×** | -8.5 | 1e-15 | 45/48 (HOP62, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.452×** | -8.3 | 9e-15 | 42/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.238×** | -7.8 | 3e-13 | 47/49 (SK-MEL-2, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.507×** | -7.1 | 9e-11 | 44/48 (A-172, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.569×** | -5.9 | 2e-07 | 36/48 (A-172, SNU-423, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.573×** | -5.8 | 3e-07 | 44/48 (NCI-H2030, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.576×** | -5.8 | 4e-07 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.577×** | -5.5 | 1e-06 | 39/47 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.587×** | -5.3 | 4e-06 | 35/47 (LoVo, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.588×** | -5.3 | 4e-06 | 33/50 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.606×** | -5.2 | 6e-06 | 39/48 (C32, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.596×** | -4.9 | 3e-05 | 37/48 (H4, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -4.8 | 4e-05 | 35/48 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.8 | 5e-05 | 38/48 (A-172, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.727×** | -3.3 | 0.018 | 29/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.647×** | -3.2 | 0.023 | 38/48 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.740×** | -3.1 | 0.032 | 27/48 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.742×** | -3.1 | 0.035 | 28/48 (LoVo, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.745×** | -3.1 | 0.040 | 30/48 (H4, HT-29, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 261 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -22.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.149× (z -15.4) |
| [[C32 (line)]] | wt | 178 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 165 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -20.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.161× (z -17.3) |
| [[SNU-423 (line)]] | alt | 155 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -14.0) |
| [[Hs 766T (line)]] | wt | 120 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -21.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -15.8) |
| [[HS-578T (line)]] | alt | 140 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -12.5) |
| [[PANC-1 (line)]] | alt | 129 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -21.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -16.5) |
| [[SW480 (line)]] | alt | 158 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -13.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.4) |
| [[HCT15 (line)]] | alt | 198 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -13.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -9.5) |
| [[HOP62 (line)]] | alt | 152 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 234 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -15.3) |
| [[A549 (line)]] | wt | 171 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -22.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.154× (z -16.3) |
| [[H4 (line)]] | wt | 172 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -19.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 404 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 244 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -23.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 292 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0441× (z -14.4) |
| [[SNU-1 (line)]] | wt | 257 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -12.1) |
| [[J82 (line)]] | alt | 182 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -16.5) |
| [[LoVo (line)]] | wt | 85.9 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -15.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 48.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 92.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 96.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.9) |
| [[SW48 (line)]] | wt | 176 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.330× (z -8.6) |
| [[A-427 (line)]] | wt | 170 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.323× (z -9.9) |
| [[BT-474 (line)]] | alt | 84.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.8) |
| [[LS 180 (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -8.6) |
| [[SW1417 (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 51.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.249× (z -9.6) |
| [[HT-29 (line)]] | alt | 64.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -11.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 69.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -11.3) |
| [[SW 1088 (line)]] | alt | 182 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0664× (z -11.4) |
| [[COLO 205 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 240 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 218 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD36B]] | +0.83 | +0.86 / +0.80 | both halves | 7e-06 | STRING 983 |
| [[XYLB]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ANKRD36C]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 | STRING 999 |
| [[TBCD]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[STX2]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[KATNAL1]] | +0.60 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[APPL1]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[STARD9]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TCF3]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[POLE2]] | +0.56 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[GARNL3]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[POLD2]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5C]] | -0.52 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[GPANK1]] | -0.51 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MED13]] | -0.50 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[NBR1]] | -0.50 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[C11orf71]] | -0.50 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[RNASEL]] | -0.50 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[ARID4B]] | -0.49 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[FAM200A]] | -0.49 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[BOLA1]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[AP5S1]] | -0.49 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[C14orf119]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MPLKIP]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM31]] | B | SMIM31 activity weakens ANKRD36's drug response | lines that do not express SMIM31 (34) vs lines expressing it (15) | the lines without SMIM31 respond 1.38× as strongly (z diff -1.88); strongest at Panobinostat 0.5 µM: 0.55x vs 0.83x (z diff -3.3) | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; target measured in part of the lines; artifact flags |
| [[SMIM31]] | B | SMIM31 activity lowers ANKRD36's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 1.80× higher at baseline in the lines without SMIM31 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[STARD9]] | B | STARD9 activity raises ANKRD36's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without STARD9 | 0.043 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ANKRD36's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KATNAL1]] | B | KATNAL1 activity raises ANKRD36's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without KATNAL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[HACE1]] | C | HACE1 activity raises ANKRD36's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.1, -53.4); signed map (-49.5, -14.1). **Vector** length 83.2, 32.7% of its response variance represented; |z| ≥ 3 in 1,346 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +3.1 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.9 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | -1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,113,153-97,264,521 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ2430 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [A6QL64](https://www.uniprot.org/uniprotkb/A6QL64) carries no function annotation.

**Summary**, from NCBI Gene [375248](https://www.ncbi.nlm.nih.gov/gene/375248):

> Predicted to enable ion channel inhibitor activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24079) · Entrez [375248](https://www.ncbi.nlm.nih.gov/gene/375248) · UniProt [A6QL64](https://www.uniprot.org/uniprotkb/A6QL64) · Ensembl [ENSG00000135976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135976)

## Data

Gene col 5795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5795); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5795]; `tensor/DDL_lfc|DDL_z.npy` [5795]; `embed/gene_vectors.npy` [5795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5795 or target_col == 5795). Every well: [[ANKRD36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
