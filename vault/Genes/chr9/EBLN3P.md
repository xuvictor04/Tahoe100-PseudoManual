---
symbol: "EBLN3P"
type: "gene"
col: 15987
ensembl_id: "ENSG00000281649"
name: "endogenous Bornavirus like nucleoprotein 3, pseudogene"
location: "9p13.2"
module: 41
arm: "+"
pooled_cpm: 63.81
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# EBLN3P

*endogenous Bornavirus like nucleoprotein 3, pseudogene* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.17× (z +5.0, q 3e-04, up in 18 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 2.24×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.522× (z -14.2, q 1e-42, down in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.440× (z -9.4, q 2e-18, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3D]] (+0.68, fdr 7e-06), [[SPTY2D1]] (+0.64, fdr 7e-06), [[ZNF805]] (+0.62, fdr 1e-05); moves opposite to [[NDUFAF5]] (-0.50, fdr 3e-05), [[SNRPF]] (-0.47, fdr 4e-05), [[NDUFS6]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 2.24×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.17× | +5.0 | 3e-04 | 18/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +4.3 | 0.004 | 17/49 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.16× | +3.4 | 0.14 | 12/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.15 | 19/48 (NCI-H2030, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -14.2 | 1e-42 | 43/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.715×** | -10.3 | 2e-22 | 39/47 (H4, PANC-1, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -9.4 | 2e-18 | 40/49 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -8.3 | 1e-14 | 33/48 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.701×** | -7.7 | 1e-12 | 33/48 (PANC-1, HOP62, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -7.5 | 5e-12 | 4/49 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.711×** | -7.1 | 9e-11 | 31/48 (PANC-1, AN3 CA, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.724×** | -7.0 | 2e-10 | 34/48 (H4, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.736×** | -6.7 | 2e-09 | 29/48 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -6.5 | 6e-09 | 28/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.574×** | -6.3 | 1e-08 | 25/34 (HepG2/C3A, A549, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.601×** | -5.8 | 3e-07 | 28/48 (Panc 03.27, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -5.3 | 4e-06 | 25/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.672×** | -4.5 | 3e-04 | 24/48 (SNU-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.805×** | -4.5 | 3e-04 | 20/48 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.755×** | -4.3 | 5e-04 | 23/48 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -4.2 | 8e-04 | 20/48 (NCI-H23, NCI-H661, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.776×** | -3.9 | 0.002 | 14/49 (SHP-77, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.890× | -3.5 | 0.011 | 7/48 (hTERT-HPNE, J82, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.012 | 13/48 (RKO, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.849× | -3.3 | 0.022 | 20/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.039 | 14/48 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.758×** | -3.1 | 0.040 | 9/48 (C-33 A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 0.908× | -2.9 | 0.069 | 8/48 (SHP-77, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 128 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.368× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.263× (z -11.4) |
| [[J82 (line)]] | alt | 68.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.461× (z -8.6) |
| [[A498 (line)]] | wt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 107 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 70.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 60.6 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.05 µM 0.171× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 41.4 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0973× (z -8.5) ⚠ toxic · without an alert: [[Naproxen (drug)]] 0.05 µM 0.268× (z -8.5) |
| [[HOP62 (line)]] | alt | 56.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.363× (z -11.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 73.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.483× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 65.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 64.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.436× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0777× (z -9.2) |
| [[SNU-423 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.408× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.401× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3D]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SPTY2D1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZNF805]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[TMED2]] | +0.60 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB41]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA5]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[COPB1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ERLEC1]] | +0.58 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SRPRA]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[LTN1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[UFM1]] | +0.57 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF5]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SNRPF]] | -0.47 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NDUFS6]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PSPC1]] | -0.45 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ARHGEF11]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (12.5, -37.5); signed map (-53.4, 13.7). **Vector** length 98.8, 23.2% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.1 | +5.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.9 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.8 | -10.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -14.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.1 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.3 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | endogenous Bornavirus like nucleoprotein 3, pseudogene |
| Locus type | pseudogene |
| Location | 9p13.2 — chr9:37,079,645-37,090,928 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC100506710; previously EBLN3 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50682) · Entrez [100506710](https://www.ncbi.nlm.nih.gov/gene/100506710) · Ensembl [ENSG00000281649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281649)

## Data

Gene col 15987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15987); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15987]; `tensor/DDL_lfc|DDL_z.npy` [15987]; `embed/gene_vectors.npy` [15987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15987 or target_col == 15987). Every well: [[EBLN3P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBLN3P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
