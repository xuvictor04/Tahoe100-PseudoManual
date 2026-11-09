---
symbol: "QSER1"
type: "gene"
col: 694
ensembl_id: "ENSG00000060749"
name: "glutamine and serine rich 1"
location: "11p13"
module: 1
arm: "+"
pooled_cpm: 141.81
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# QSER1

*glutamine and serine rich 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.23× (z +5.9, q 2e-06, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 1.73×, NCI-H2347 1.76×, A549 1.84×, A498 1.44×, …; ⚠ cell-cycle shift, explains ~11% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 2.21×, A549 2.11×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.314× (z -34.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXIP1]] (+0.67, fdr 1e-05), [[TMPO]] (+0.55, fdr 1e-05), [[MCCC2]] (+0.55, fdr 2e-04); moves opposite to [[SERINC2]] (-0.57, fdr 3e-05), [[MEF2D]] (-0.57, fdr 1e-04), [[RIOK3]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 1.73×, NCI-H2347 1.76×, A549 1.84×, A498 1.44×, …; ⚠ cell-cycle shift, explains ~11% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 2.21×, A549 2.11×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +5.9 | 2e-06 | 24/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +5.7 | 3e-06 | 24/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.14× | +3.8 | 0.025 | 15/47 (BT-474, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.2 | 0.17 | 12/47 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.11× | +3.1 | 0.24 | 14/48 (BT-474, SHP-77, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.314×** | -34.5 | 0e+00 | 47/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -31.1 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -25.2 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -12.8 | 3e-35 | 43/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -11.3 | 9e-28 | 29/49 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.707×** | -10.3 | 9e-23 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -6.9 | 4e-10 | 20/48 (SW480, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.800×** | -6.6 | 3e-09 | 24/48 (HT-29, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.814×** | -6.1 | 6e-08 | 25/49 (HT-29, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.825×** | -5.5 | 3e-06 | 26/47 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.882× | -5.2 | 1e-05 | 22/48 (COLO 205, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.839× | -5.0 | 3e-05 | 24/50 (HEC-1-A, HOP62, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.695×** | -4.0 | 0.003 | 20/48 (HOP62, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.866× | -3.9 | 0.004 | 20/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | 0.880× | -3.8 | 0.006 | 17/48 (SW480, HT-29, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.821×** | -3.7 | 0.008 | 19/48 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.723×** | -3.6 | 0.011 | 14/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.036 | 19/49 (HEC-1-A, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.854× | -2.9 | 0.085 | 14/47 (SNU-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 163 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -22.2) |
| [[SW480 (line)]] | alt | 170 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -28.3) |
| [[A549 (line)]] | wt | 161 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.2) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.11× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -19.3) |
| [[HEC-1-A (line)]] | alt | 171 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -24.5) |
| [[HT-29 (line)]] | alt | 141 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -20.0) |
| [[SNU-1 (line)]] | wt | 159 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -15.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.329× (z -13.1) |
| [[A-427 (line)]] | wt | 205 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -19.8) |
| [[C-33 A (line)]] | alt | 239 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -21.0) |
| [[COLO 205 (line)]] | alt | 123 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -19.0) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.293× (z -14.9) |
| [[H4 (line)]] | wt | 251 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -16.5) |
| [[HCT15 (line)]] | alt | 190 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -15.2) |
| [[J82 (line)]] | alt | 191 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -19.7) |
| [[LoVo (line)]] | wt | 128 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.481× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 180 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -21.3) |
| [[PANC-1 (line)]] | alt | 184 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +15.5) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.21× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -20.0) |
| [[A-172 (line)]] | wt | 170 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -20.2) |
| [[A498 (line)]] | wt | 180 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -27.4) |
| [[AN3 CA (line)]] | alt | 219 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -10.0) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.8) |
| [[HS-578T (line)]] | alt | 97.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.1) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 211 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -25.0) |
| [[NCI-H2030 (line)]] | alt | 95.6 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.5) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 112 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.8) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -19.3) |
| [[SW1417 (line)]] | alt | 138 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -17.6) |
| [[SW48 (line)]] | wt | 169 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 97.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -13.7) |
| [[BT-474 (line)]] | alt | 105 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -14.1) |
| [[Hs 766T (line)]] | wt | 142 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -15.0) |
| [[KATO III (line)]] | alt | 69.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -13.3) |
| [[LS 180 (line)]] | wt | 113 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -15.7) |
| [[NCI-H1792 (line)]] | alt | 111 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 136 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -17.3) |
| [[RKO (line)]] | wt | 189 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.5) |
| [[SHP-77 (line)]] | alt | 97.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -15.0) |
| [[SNU-423 (line)]] | alt | 162 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -18.5) |
| [[HepG2_C3A (line)]] | wt | 95.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -11.7) |
| [[SW 900 (line)]] | alt | 56.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.2) |
| [[CHP-212 (line)]] | wt | 86.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 79.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.486× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -8.7) |
| [[SW 1088 (line)]] | alt | 112 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.106× (z -8.9) |
| [[C32 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXIP1]] | +0.67 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TMPO]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.55 | +0.29 / +0.51 | both halves | 2e-04 |  |
| [[TASOR]] | +0.55 | +0.24 / +0.58 | both halves | 4e-04 |  |
| [[RNASEH2B]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[DCLRE1A]] | +0.55 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[TTF2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RIF1]] | +0.54 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[USP13]] | +0.54 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[SNX5]] | +0.54 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[GEN1]] | +0.54 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ZNF507]] | +0.54 | +0.21 / +0.58 | both halves | 7e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC2]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MEF2D]] | -0.57 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[RIOK3]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[FBXO33]] | -0.55 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[CASP9]] | -0.54 | -0.21 / -0.43 | both halves | 6e-04 |  |
| [[TMSB10]] | -0.54 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ABCA7]] | -0.54 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[GUK1]] | -0.53 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[PEDS1]] | -0.53 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[CYP46A1]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PNPLA8]] | -0.53 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[TBC1D22A-DT]] | -0.52 | -0.39 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (7.6, -42.7); signed map (20.5, -36.5). **Vector** length 100, 27.2% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +1.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -34.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.8 | -31.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -25.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -12.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -6.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | glutamine and serine rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:32,892,811-32,993,316 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21924 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2KHR3](https://www.uniprot.org/uniprotkb/Q2KHR3) (Glutamine and serine-rich protein 1):

> Plays an essential role in the protection and maintenance of transcriptional and developmental programs. Protects many bivalent promoters and poised enhancers from hypermethylation, showing a marked preference for these regulatory elements over other types of promoters or enhancers. Mechanistically, cooperates with TET1 and binds to DNA in a common complex to inhibit the binding of DNMT3A/3B and therefore de novo methylation.

**Summary**, from NCBI Gene [79832](https://www.ncbi.nlm.nih.gov/gene/79832):

> Predicted to be located in chromosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26154) · Entrez [79832](https://www.ncbi.nlm.nih.gov/gene/79832) · UniProt [Q2KHR3](https://www.uniprot.org/uniprotkb/Q2KHR3) · Ensembl [ENSG00000060749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060749)

## Data

Gene col 694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 694); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 694]; `tensor/DDL_lfc|DDL_z.npy` [694]; `embed/gene_vectors.npy` [694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 694 or target_col == 694). Every well: [[QSER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QSER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
