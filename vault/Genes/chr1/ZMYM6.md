---
symbol: "ZMYM6"
type: "gene"
col: 8795
ensembl_id: "ENSG00000163867"
name: "zinc finger MYM-type containing 6"
location: "1p34.3"
module: 41
arm: "+"
pooled_cpm: 52.06
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ZMYM6

*zinc finger MYM-type containing 6* — 1p34.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.68×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.397× (z -19.3, q 0e+00, down in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.402× (z -19.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD17]] (+0.74, fdr 7e-06), [[RARS1]] (+0.66, fdr 1e-05), [[INIP]] (+0.66, fdr 4e-05); moves opposite to [[RCC2]] (-0.63, fdr 2e-05), [[ATE1]] (-0.59, fdr 1e-04), [[TOR1A]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.68×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-733 (drug)]] 0.05 µM |  | 1.21× | +3.7 | 0.13 | 15/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.3 | 0.31 | 16/47 (NCI-H460, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -19.3 | 0e+00 | 41/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -19.0 | 0e+00 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -14.7 | 0e+00 | 39/48 (SNU-1, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.511×** | -14.0 | 3e-42 | 42/48 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -13.9 | 4e-42 | 43/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -13.2 | 9e-38 | 38/47 (MIA PaCa-2, H4, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -13.2 | 1e-37 | 45/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.553×** | -12.3 | 4e-33 | 38/48 (hTERT-HPNE, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.594×** | -10.0 | 6e-22 | 33/44 (Panc 03.27, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.616×** | -9.7 | 1e-20 | 30/40 (HOP62, LoVo, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -9.3 | 7e-19 | 35/48 (LoVo, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -8.4 | 2e-15 | 31/48 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -7.9 | 1e-13 | 33/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.677×** | -7.7 | 6e-13 | 36/48 (Hs 766T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.695×** | -7.3 | 1e-11 | 30/48 (H4, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -5.9 | 1e-07 | 25/48 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -5.5 | 9e-07 | 24/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.802×** | -4.4 | 2e-04 | 21/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.817×** | -3.9 | 0.002 | 21/47 (AN3 CA, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.005 | 17/49 (Hs 766T, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.853× | -3.3 | 0.019 | 20/48 (MIA PaCa-2, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 69.7 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -14.4) |
| [[Hs 766T (line)]] | wt | 87.9 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -11.9) |
| [[LoVo (line)]] | wt | 58.6 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 64.0 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 68.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -10.9) |
| [[PANC-1 (line)]] | alt | 61.8 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -15.4) |
| [[SW480 (line)]] | alt | 51.6 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -14.4) |
| [[A498 (line)]] | wt | 60.6 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -12.4) |
| [[A549 (line)]] | wt | 46.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 54.3 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -12.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.2) |
| [[H4 (line)]] | wt | 65.5 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -10.8) |
| [[A-172 (line)]] | wt | 41.5 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -10.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.7) |
| [[COLO 205 (line)]] | alt | 64.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -12.1) |
| [[KATO III (line)]] | alt | 49.6 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 42.4 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.401× (z -10.7) |
| [[HS-578T (line)]] | alt | 83.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -11.9) |
| [[J82 (line)]] | alt | 40.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 63.4 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.263× (z -13.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 41.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.9) |
| [[SNU-423 (line)]] | alt | 53.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -9.0) |
| [[SW 900 (line)]] | alt | 59.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.253× (z -12.4) |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 50.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -9.2) |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -11.6) |
| [[A-427 (line)]] | wt | 41.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -12.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 38.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -8.9) |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0982× (z -9.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HEC-1-A (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0978× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 63.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 49.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -13.0) |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -10.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD17]] | +0.74 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[RARS1]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[INIP]] | +0.66 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[DIS3]] | +0.65 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[NAGK]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[MMUT]] | +0.64 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[FRA10AC1]] | +0.64 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[UTP6]] | +0.63 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[GOLGA2]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[UFL1]] | +0.62 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.62 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC2]] | -0.63 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ATE1]] | -0.59 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[TOR1A]] | -0.58 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[SUMO3]] | -0.58 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[FUCA2]] | -0.57 | -0.61 / -0.22 | both halves | 6e-04 |  |
| [[HCFC1]] | -0.55 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[POU2F1]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ZNF704]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[RAB15]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ARSB]] | -0.53 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[ARHGEF11]] | -0.53 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[PSPC1]] | -0.52 | -0.47 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZMYM6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.2, -34.2); signed map (-52.7, 18.2). **Vector** length 94.0, 25.2% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | -0.6 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.6 | -0.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.5 | -0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -19.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -13.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.4 | -13.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYM-type containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:34,986,165-35,031,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF198L4, MYM, Buster2, ZBED7, KIAA1353; previously ZNF258 |
| Gene groups (HGNC) | Zinc fingers BED-type; Zinc fingers MYM-type |
| Matched by | ensembl_id |

**Function**, from UniProt [O95789](https://www.uniprot.org/uniprotkb/O95789) (Zinc finger MYM-type protein 6):

> Required for regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [9204](https://www.ncbi.nlm.nih.gov/gene/9204):

> Predicted to enable DNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13050) · Entrez [9204](https://www.ncbi.nlm.nih.gov/gene/9204) · UniProt [O95789](https://www.uniprot.org/uniprotkb/O95789) · Ensembl [ENSG00000163867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163867)

## Data

Gene col 8795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8795); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8795]; `tensor/DDL_lfc|DDL_z.npy` [8795]; `embed/gene_vectors.npy` [8795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8795 or target_col == 8795). Every well: [[ZMYM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
