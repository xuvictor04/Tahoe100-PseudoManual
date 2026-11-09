---
symbol: "TMEM62"
type: "gene"
col: 6083
ensembl_id: "ENSG00000137842"
name: "transmembrane protein 62"
location: "15q15.2"
module: 32
arm: "+"
pooled_cpm: 40.93
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 36
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 20
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TMEM62

*transmembrane protein 62* — 15q15.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -17.7, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.437× (z -14.1, q 7e-43, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM26]] (+0.58, fdr 1e-05), [[CMPK2]] (+0.56, fdr 4e-05), [[DCLRE1C]] (+0.54, fdr 1e-05); moves opposite to [[TMEM14B]] (-0.48, fdr 3e-05), [[PCID2]] (-0.44, fdr 1e-04), [[C4orf47]] (-0.43, fdr 5e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[SIDT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.35× | +3.6 | 0.18 | 20/47 (SNU-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.354×** | -17.7 | 0e+00 | 43/47 (COLO 205, A498, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.437×** | -14.1 | 7e-43 | 43/47 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.320×** | -13.8 | 8e-41 | 46/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.327×** | -13.5 | 3e-39 | 42/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.331×** | -13.3 | 2e-38 | 44/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.373×** | -11.9 | 1e-30 | 45/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.409×** | -10.8 | 3e-25 | 36/47 (HT-29, COLO 205, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -10.8 | 4e-25 | 41/47 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -10.1 | 5e-22 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.446×** | -9.4 | 5e-19 | 37/48 (COLO 205, RPMI-7951, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.486×** | -8.7 | 2e-16 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.506×** | -7.9 | 1e-13 | 37/45 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -7.9 | 2e-13 | 36/47 (COLO 205, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -6.9 | 2e-10 | 32/49 (HT-29, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.563×** | -6.4 | 6e-09 | 25/37 (A-172, SW48, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -5.7 | 4e-07 | 31/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -5.7 | 4e-07 | 32/47 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.692×** | -4.3 | 6e-04 | 29/48 (COLO 205, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.785×** | -4.1 | 0.001 | 22/48 (PANC-1, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.795×** | -3.9 | 0.002 | 24/48 (HT-29, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.009 | 23/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.747×** | -3.4 | 0.015 | 19/46 (SNU-1, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 259 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0641× (z -28.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0953× (z -17.1) |
| [[A-172 (line)]] | wt | 46.8 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -19.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.183× (z -12.0) |
| [[HT-29 (line)]] | alt | 121 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -17.5) |
| [[SW480 (line)]] | alt | 39.5 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -17.8) |
| [[LoVo (line)]] | wt | 68.1 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 45.4 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.121× (z -13.5) |
| [[SW1417 (line)]] | alt | 60.7 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.303× (z -9.8) |
| [[SW48 (line)]] | wt | 70.0 | 0 | 8 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0822× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.311× (z -10.0) |
| [[PANC-1 (line)]] | alt | 26.9 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.342× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 51.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -18.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -12.1) |
| [[A498 (line)]] | wt | 34.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 47.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -15.2) |
| [[A549 (line)]] | wt | 43.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.4) |
| [[J82 (line)]] | alt | 30.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.289× (z -9.5) |
| [[KATO III (line)]] | alt | 43.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.305× (z -9.9) |
| [[LS 180 (line)]] | wt | 53.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -16.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 88.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.211× (z -11.4) |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -8.7) |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.2) |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 58.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -10.1) |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0947× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.222× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 50.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.8) |
| [[RKO (line)]] | wt | 39.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -11.8) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.2) |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.287× (z -8.7) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.153× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM26]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CMPK2]] | +0.56 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[DCLRE1C]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TDRD7]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[HERC6]] | +0.54 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[IFI44]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PSMA3]] | +0.53 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[LAP3]] | +0.53 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[SLC25A28]] | +0.53 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[MX1]] | +0.52 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[TMEM140]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[PNPT1]] | +0.52 | +0.36 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14B]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PCID2]] | -0.44 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[C4orf47]] | -0.43 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[LEPR]] | -0.43 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[LVRN]] | -0.42 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[P4HA1]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[CCDC18-AS1]] | -0.42 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB25]] | -0.41 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIDT1]] | B | SIDT1 activity raises TMEM62's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[RSAD2]] | B | RSAD2 activity raises TMEM62's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without RSAD2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[TTC22]] | B | TTC22 activity raises TMEM62's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.03× lower at baseline in the lines without TTC22 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[TNFSF10]] | B | TNFSF10 activity raises TMEM62's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without TNFSF10 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[NRIR]] | B | NRIR activity raises TMEM62's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without NRIR | 0.022 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[OAS1]] | B | OAS1 activity raises TMEM62's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without OAS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises TMEM62's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without PARP9 | 0.029 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises TMEM62's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without PLSCR1 | 0.030 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[RASGRP3]] | B | RASGRP3 activity raises TMEM62's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.39× lower at baseline in the lines without RASGRP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[HSH2D]] | B | HSH2D activity raises TMEM62's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without HSH2D | 0.038 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity strengthens TMEM62's drug response | lines that do not express OAS1 (13) vs lines expressing it (35) | the lines without OAS1 respond 0.67× as strongly (z diff +1.85); strongest at Idarubicin (hydrochloride) 5 µM: 0.64x vs 0.39x (z diff +3.0) | 0.049 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS3]] | B | OAS3 activity raises TMEM62's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without OAS3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.7, 55.9); signed map (66.0, 34.0). **Vector** length 88.1, 25.7% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +7.2 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +0.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.8 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:43,123,279-43,185,144 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23375 |
| Matched by | ensembl_id |

UniProt [Q0P6H9](https://www.uniprot.org/uniprotkb/Q0P6H9) carries no function annotation.

**Summary**, from NCBI Gene [80021](https://www.ncbi.nlm.nih.gov/gene/80021):

> Predicted to enable hydrolase activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26269) · Entrez [80021](https://www.ncbi.nlm.nih.gov/gene/80021) · UniProt [Q0P6H9](https://www.uniprot.org/uniprotkb/Q0P6H9) · Ensembl [ENSG00000137842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137842)

## Data

Gene col 6083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6083); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6083]; `tensor/DDL_lfc|DDL_z.npy` [6083]; `embed/gene_vectors.npy` [6083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6083 or target_col == 6083). Every well: [[TMEM62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
