---
symbol: "LPIN3"
type: "gene"
col: 5373
ensembl_id: "ENSG00000132793"
name: "lipin 3"
location: "20q12"
module: 96
arm: "+"
pooled_cpm: 15.59
n_lines_expressing: 44
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# LPIN3

*lipin 3* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.45× (z +6.3, q 1e-07, up in 25 of 42 measured lines) ⚠ cell-cycle shift, explains ~70% of this change.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.268× (z -22.4, q 0e+00, down in 39 of 41 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.433× (z -14.2, q 2e-43, down in 35 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1G2]] (+0.66, fdr 7e-06), [[DMTN]] (+0.61, fdr 2e-05), [[MINDY1]] (+0.60, fdr 1e-05); moves opposite to [[EHBP1]] (-0.50, fdr 4e-05), [[SCHIP1]] (-0.50, fdr 4e-05), [[AKT3]] (-0.49, fdr 9e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPHX2]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.45×** | +6.3 | 1e-07 | 25/42 (A-427, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.31× | +3.2 | 0.33 | 14/40 (A498, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.268×** | -22.4 | 0e+00 | 39/41 (NCI-H460, HEC-1-A, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.433×** | -14.2 | 2e-43 | 35/41 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.322×** | -13.6 | 5e-40 | 32/39 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.314×** | -11.5 | 1e-28 | 36/40 (MIA PaCa-2, HEC-1-A, …) | rises with dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.446×** | -9.7 | 4e-20 | 35/41 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.450×** | -9.6 | 9e-20 | 35/41 (HCT15, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.457×** | -9.4 | 4e-19 | 35/41 (HCT15, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.428×** | -8.5 | 2e-15 | 30/38 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.506×** | -8.2 | 2e-14 | 32/40 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.524×** | -7.8 | 5e-13 | 32/41 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.549×** | -7.2 | 3e-11 | 30/41 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.383×** | -6.0 | 8e-08 | 27/40 (CFPAC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.552×** | -5.9 | 2e-07 | 21/39 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -5.8 | 3e-07 | 14/42 (SW1417, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.622×** | -5.7 | 5e-07 | 23/40 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.645×** | -5.3 | 5e-06 | 23/39 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -4.5 | 2e-04 | 20/40 (HT-29, CFPAC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.2 | 7e-04 | 19/41 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -3.7 | 0.005 | 17/38 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -3.3 | 0.022 | 16/40 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.599×** | -3.2 | 0.030 | 11/41 (NCI-H460, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.031 | 13/39 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.846× | -2.8 | 0.096 | 6/41 (RPMI-7951, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -21.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -10.6) |
| [[SW480 (line)]] | alt | 17.0 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -12.0) |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0795× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -17.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.6) |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.165× (z -10.1) |
| [[KATO III (line)]] | alt | 31.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.0) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -18.3) |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.2) |
| [[PANC-1 (line)]] | alt | 9.77 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -11.7) |
| [[A549 (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 7.40 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -9.1) |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.0) |
| [[J82 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -8.7) |
| [[LS 180 (line)]] | wt | 24.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SHP-77 (line)]] | alt | 8.76 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.110× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.140× (z -10.0) |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 8.42 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1G2]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[DMTN]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MINDY1]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SGSH]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[PICK1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[FBXO44]] | +0.54 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CCDC120]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[MED24]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[WASH9P]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NEIL1]] | +0.50 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[METTL22]] | +0.50 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[DMAP1]] | +0.50 | +0.37 / +0.56 | both halves | 9e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[SCHIP1]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[AKT3]] | -0.49 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[IQCJ-SCHIP1]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TSHZ3]] | -0.47 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[DPH1-AS1]] | -0.46 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[KLF12]] | -0.46 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[CHSY3]] | -0.45 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SRGAP2C]] | -0.45 | -0.19 / -0.56 | ⚠ one half (not replicated) | 9e-04 |  |
| [[MSC-AS1]] | -0.45 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[LINC02798]] | -0.44 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[SATB2]] | -0.44 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NAV1]] | -0.43 | -0.31 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHX2]] | B | EPHX2 activity raises LPIN3's level | lines that do not express EPHX2 (10) vs lines expressing it (40) | 3.17× lower at baseline in the lines without EPHX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: MELTF, OPLAH, SEPTIN9-DT |
| [[MUC1]] | B | MUC1 activity raises LPIN3's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without MUC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | C | LPIN3 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LPIN3 (6) vs lines expressing it (42) | the lines without LPIN3: 0.63× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: TNFRSF10D, TACC2, PTER |
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | LPIN3 activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express LPIN3 (6) vs lines expressing it (42) | the lines without LPIN3: 0.73× the cells of the other lines | 0.045 | ⚠ tissue-confounded; across organs; also absent: TNFRSF10D, TACC2, PTER |
| cells under [[Infigratinib (drug)]] 5 µM | C | LPIN3 activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express LPIN3 (6) vs lines expressing it (42) | the lines without LPIN3: 0.68× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; also absent: TNFRSF10D, TACC2, PTER |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.379). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.3, 26.9); signed map (-8.8, -30.5). **Vector** length 67.4, 13.3% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +5.7 | +6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | -1.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | -0.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.5 | -11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.5 | -22.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -13.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -2.2 | -8.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | lipin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12 — chr20:41,340,821-41,360,582 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMP2; previously LIPN3L |
| Gene groups (HGNC) | Lipins |
| Reactome | 13 pathways, smallest: Triglyceride biosynthesis; Synthesis of PE; Depolymerization of the Nuclear Lamina |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQK8](https://www.uniprot.org/uniprotkb/Q9BQK8) (Phosphatidate phosphatase LPIN3):

> Magnesium-dependent phosphatidate phosphatase enzyme which catalyzes the conversion of phosphatidic acid to diacylglycerol during triglyceride, phosphatidylcholine and phosphatidylethanolamine biosynthesis therefore regulates fatty acid metabolism.

**Summary**, from NCBI Gene [64900](https://www.ncbi.nlm.nih.gov/gene/64900):

> The protein encoded by this gene is a member of the lipin family of proteins, and all family members share strong homology in their C-terminal region. This protein is thought to form hetero-oligomers with other lipin family members, while one family member, lipin 1, can also form homo-oligomers. This protein contains conserved motifs for phosphatidate phosphatase 1 (PAP1) activity as well as a domain that interacts with a transcriptional co-activator. Lipin complexes act in the cytoplasm to …

**Accessions** — [HGNC:14451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14451) · Entrez [64900](https://www.ncbi.nlm.nih.gov/gene/64900) · UniProt [Q9BQK8](https://www.uniprot.org/uniprotkb/Q9BQK8) · Ensembl [ENSG00000132793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132793)

## Data

Gene col 5373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5373); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5373]; `tensor/DDL_lfc|DDL_z.npy` [5373]; `embed/gene_vectors.npy` [5373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5373 or target_col == 5373). Every well: [[LPIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
