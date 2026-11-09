---
symbol: "AHDC1"
type: "gene"
col: 4752
ensembl_id: "ENSG00000126705"
name: "AT-hook DNA binding motif containing 1"
location: "1p36.11-p35.3"
module: 161
arm: "+"
pooled_cpm: 64.48
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# AHDC1

*AT-hook DNA binding motif containing 1* — 1p36.11-p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.63× (z +6.4, q 8e-08, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.548× (z -7.8, q 2e-12, down in 34 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.612× (z -6.4, q 2e-08, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3A]] (+0.74, fdr 7e-06), [[PEDS1]] (+0.74, fdr 7e-06), [[SLC26A6]] (+0.73, fdr 7e-06); moves opposite to [[ENOX2]] (-0.72, fdr 1e-05), [[ZMYND11]] (-0.71, fdr 1e-05), [[DNAJC11]] (-0.71, fdr 7e-06).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +6.4 | 8e-08 | 30/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +6.2 | 2e-07 | 31/48 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +5.2 | 4e-05 | 27/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.005 | 26/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.006 | 24/48 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.022 | 27/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.022 | 25/48 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.025 | 29/49 (PANC-1, LS 180, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.042 | 23/49 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.1 | 0.093 | 22/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.093 | 16/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | 1.55× | +3.0 | 0.11 | 20/48 (CFPAC-1, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.8 | 2e-12 | 34/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.554×** | -7.4 | 3e-11 | 26/40 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -6.4 | 2e-08 | 28/48 (CFPAC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -6.4 | 2e-08 | 34/49 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.592×** | -6.3 | 3e-08 | 29/42 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -5.5 | 3e-06 | 34/48 (NCI-H1573, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -4.6 | 3e-04 | 32/48 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -4.1 | 0.003 | 26/50 (RPMI-7951, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.731×** | -4.1 | 0.003 | 28/48 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -4.0 | 0.003 | 25/48 (LOX-IMVI, SW 900, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.010 | 25/48 (NCI-H1573, A-172, …) | inconsistent across doses | position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **0.766×** | -3.5 | 0.025 | 22/48 (A-172, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.033 | 27/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.775×** | -3.3 | 0.039 | 21/49 (NCI-H2122, SW1417, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.782×** | -3.2 | 0.053 | 20/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.828×** | -3.2 | 0.053 | 18/48 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.786×** | -3.1 | 0.054 | 19/48 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.054 | 18/48 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.054 | 21/49 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 96.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.0) |
| [[Hs 766T (line)]] | wt | 86.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0953× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -14.0) |
| [[A-427 (line)]] | wt | 29.8 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 50.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 84.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 57.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 51.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0923× (z -17.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 52.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[A498 (line)]] | wt | 86.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 74.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 61.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.5) |
| [[HOP62 (line)]] | alt | 69.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 74.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0234× (z -29.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.288× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 84.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -11.9) |
| [[SW 900 (line)]] | alt | 86.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.6) |
| [[A-172 (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 42.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.80× (z +8.6) | — |
| [[C32 (line)]] | wt | 41.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -12.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 85.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.4) |
| [[J82 (line)]] | alt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.9) | — |
| [[KATO III (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -9.5) |
| [[PANC-1 (line)]] | alt | 86.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | +0.74 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PEDS1]] | +0.74 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SLC26A6]] | +0.73 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MPND]] | +0.73 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.73 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[MAST1]] | +0.71 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PNKD]] | +0.71 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.70 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.70 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LRP1]] | +0.70 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[RPS6KA1]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.72 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.71 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.71 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[UTP20]] | -0.70 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[DPH5-DT]] | -0.68 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[ALG8]] | -0.67 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.67 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ATR]] | -0.67 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[AVEN]] | -0.67 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[MED1]] | -0.67 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.65 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.65 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises AHDC1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without PDGFB | 0.012 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[RIPK4]] | B | RIPK4 activity raises AHDC1's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.53× lower at baseline in the lines without RIPK4 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[ATG9B]] | B | ATG9B activity raises AHDC1's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without ATG9B | 0.022 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[EPS8L2]] | B | EPS8L2 activity raises AHDC1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without EPS8L2 | 0.025 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[LMTK3]] | B | LMTK3 activity raises AHDC1's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.29× lower at baseline in the lines without LMTK3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[THEMIS2]] | B | THEMIS2 activity raises AHDC1's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without THEMIS2 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[VSIR]] | B | VSIR activity raises AHDC1's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without VSIR | 0.041 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises AHDC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDC42BPG]] | B | CDC42BPG activity raises AHDC1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without CDC42BPG | 0.050 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity raises AHDC1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.18× lower at baseline in the lines without IRF6 | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[BAIAP3]] | B | BAIAP3 activity raises AHDC1's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[CARD10]] | B | CARD10 activity raises AHDC1's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 1.47× lower at baseline in the lines without CARD10 | 0.060 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.7, -3.6); signed map (-28.7, 20.6). **Vector** length 123, 36.7% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +1.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.5 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | AT-hook DNA binding motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11-p35.3 — chr1:27,534,035-27,604,431 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DJ159A19.3, RP1-159A19.1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TGY3](https://www.uniprot.org/uniprotkb/Q5TGY3) (Transcription factor Gibbin):

> Transcription factor required for the proper patterning of the epidermis, which plays a key role in early epithelial morphogenesis. Directly binds promoter and enhancer regions and acts by maintaining local enhancer-promoter chromatin architecture. Interacts with many sequence-specific zinc-finger transcription factors and methyl-CpG-binding proteins to regulate the expression of mesoderm genes that wire surface ectoderm stratification.

**Summary**, from NCBI Gene [27245](https://www.ncbi.nlm.nih.gov/gene/27245):

> This gene encodes a protein containing two AT-hooks, which likely function in DNA binding. Mutations in this gene were found in individuals with Xia-Gibbs syndrome. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:25230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25230) · Entrez [27245](https://www.ncbi.nlm.nih.gov/gene/27245) · UniProt [Q5TGY3](https://www.uniprot.org/uniprotkb/Q5TGY3) · Ensembl [ENSG00000126705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126705)

## Data

Gene col 4752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4752); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4752]; `tensor/DDL_lfc|DDL_z.npy` [4752]; `embed/gene_vectors.npy` [4752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4752 or target_col == 4752). Every well: [[AHDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
