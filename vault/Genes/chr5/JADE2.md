---
symbol: "JADE2"
type: "gene"
col: 494
ensembl_id: "ENSG00000043143"
name: "jade family PHD finger 2"
location: "5q31.1"
module: 46
arm: "+"
pooled_cpm: 26.46
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 37
n_dd_up_clean: 9
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# JADE2

*jade family PHD finger 2* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +6.2, q 4e-07, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.209× (z -22.6, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.72, fdr 1e-05), [[ANXA2R-AS1]] (+0.64, fdr 3e-05), [[IQCH-AS1]] (+0.63, fdr 4e-05); moves opposite to [[UBA6]] (-0.63, fdr 1e-04), [[FLNB-AS1]] (-0.62, fdr 1e-05), [[UCHL3]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.2 | 4e-07 | 21/46 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.2 | 6e-05 | 26/46 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.9 | 2e-04 | 25/44 (SNU-423, Hs 766T, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.013 | 14/45 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.013 | 15/47 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.20× | +3.8 | 0.016 | 14/47 (HT-29, NCI-H2347, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.050 | 13/47 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.055 | 8/45 (A549, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.072 | 15/46 (LoVo, AsPC-1, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.072 | 14/45 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.072 | 12/46 (KATO III, AsPC-1, …) | top dose only |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.072 | 10/47 (KATO III, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.209×** | -22.6 | 0e+00 | 45/47 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.214×** | -22.2 | 0e+00 | 45/47 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.233×** | -21.0 | 0e+00 | 45/46 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.430×** | -12.2 | 7e-32 | 40/46 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.488×** | -10.3 | 5e-23 | 34/47 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -9.0 | 3e-17 | 31/47 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -7.7 | 2e-12 | 30/46 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.573×** | -7.6 | 3e-12 | 31/46 (MIA PaCa-2, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.697×** | -7.3 | 1e-11 | 31/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.391×** | -7.1 | 8e-11 | 36/47 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.617×** | -7.0 | 2e-10 | 33/45 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[EX229 (drug)]] 5 µM |  | **0.404×** | -6.8 | 4e-10 | 29/45 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.422×** | -6.5 | 3e-09 | 31/46 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -6.5 | 4e-09 | 31/46 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.544×** | -6.3 | 1e-08 | 33/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.484×** | -5.5 | 2e-06 | 24/46 (A-427, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.485×** | -5.4 | 2e-06 | 24/46 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -27.7) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0567× (z -23.5) |
| [[COLO 205 (line)]] | alt | 59.1 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0688× (z -18.6) |
| [[A498 (line)]] | wt | 54.5 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -21.3) |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.0) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.7) |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -10.7) |
| [[SW480 (line)]] | alt | 20.4 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -18.4) |
| [[A-427 (line)]] | wt | 32.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 56.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -21.6) |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0965× (z -16.0) |
| [[LoVo (line)]] | wt | 30.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 65.1 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0627× (z -26.6) |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -18.6) |
| [[C32 (line)]] | wt | 22.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -11.2) |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -16.4) |
| [[SW48 (line)]] | wt | 24.1 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0712× (z -12.3) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -10.5) |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0530× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 15.9 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.0) ⚠ cell-cycle shift, explains ~10% of this change | [[Panobinostat (drug)]] 5 µM 0.163× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -19.7) |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -11.4) |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -12.4) |
| [[KATO III (line)]] | alt | 13.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0955× (z -12.7) |
| [[A549 (line)]] | wt | 19.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.202× (z -8.9) |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -9.1) |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -9.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.141× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.9) ⚠ cell-cycle shift, explains ~10% of this change |
| [[RKO (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0897× (z -10.5) |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -9.0) |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -9.1) |
| [[AN3 CA (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.72 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.64 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | +0.63 | +0.58 / +0.40 | both halves | 4e-05 |  |
| [[CABLES1]] | +0.63 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[ZBTB2]] | +0.63 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[HDGF]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PATZ1]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[HOTAIR]] | +0.61 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[RCC2]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ARID1B]] | +0.59 | +0.45 / +0.51 | both halves | 3e-05 | pathway: Chromatin modifying enzymes |
| [[TAPBPL]] | +0.59 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | -0.63 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[FLNB-AS1]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[UCHL3]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CLTCL1]] | -0.61 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GP6-AS1]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LRRFIP1]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[ARID3B]] | -0.59 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PIGH]] | -0.58 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[NGLY1]] | -0.57 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[RTN4]] | -0.57 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ENTPD7]] | -0.57 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[EPN2]] | -0.57 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (14.5, 5.6); signed map (31.9, -24.3). **Vector** length 116, 33.2% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.3 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -12.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -21.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -22.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -7.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.0 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | jade family PHD finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,524,312-134,583,230 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0239, JADE-2; previously PHF15 |
| Gene groups (HGNC) | PHD finger proteins; Jade family PHD fingers |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQC1](https://www.uniprot.org/uniprotkb/Q9NQC1) (E3 ubiquitin-protein ligase Jade-2):

> Scaffold subunit of some HBO1 complexes, which have a histone H4 acetyltransferase activity. Acts as an E3 ubiquitin-protein ligase mediating the ubiquitination and subsequent proteasomal degradation of target protein histone demethylase KDM1A. Also acts as a ubiquitin ligase E3 toward itself. Positive regulator of neurogenesis (By similarity).

**Summary**, from NCBI Gene [23338](https://www.ncbi.nlm.nih.gov/gene/23338):

> Enables histone H4K12 acetyltransferase activity; histone H4K5 acetyltransferase activity; and histone H4K8 acetyltransferase activity. Contributes to histone H3K14 acetyltransferase activity. Involved in regulation of DNA biosynthetic process; regulation of DNA replication; and regulation of cell cycle. Located in nucleoplasm. Part of histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22984) · Entrez [23338](https://www.ncbi.nlm.nih.gov/gene/23338) · UniProt [Q9NQC1](https://www.uniprot.org/uniprotkb/Q9NQC1) · Ensembl [ENSG00000043143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000043143)

## Data

Gene col 494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 494); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 494]; `tensor/DDL_lfc|DDL_z.npy` [494]; `embed/gene_vectors.npy` [494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 494 or target_col == 494). Every well: [[JADE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JADE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
