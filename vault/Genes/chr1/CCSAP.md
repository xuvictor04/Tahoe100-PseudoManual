---
symbol: "CCSAP"
type: "gene"
col: 7805
ensembl_id: "ENSG00000154429"
name: "centriole, cilia and spindle associated protein"
location: "1q42.13"
module: 79
arm: "+"
pooled_cpm: 48.45
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# CCSAP

*centriole, cilia and spindle associated protein* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.36× (z +4.4, q 0.006, up in 25 of 46 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 1.69× (z +3.9, q 0.025, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SW1417 2.51×, Panc 03.27 2.69×, LoVo 1.98×, COLO 205 4.17×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 2.60×; ⚠ cell-cycle shift, explains ~43% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.449× (z -11.4, q 4e-27, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.611× (z -6.7, q 3e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXP]] (+0.65, fdr 7e-06), [[PDK3]] (+0.64, fdr 1e-05), [[VLDLR]] (+0.64, fdr 7e-06); moves opposite to [[ITPA]] (-0.55, fdr 1e-05), [[UTP20]] (-0.54, fdr 2e-05), [[FIZ1]] (-0.52, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7805.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SW1417 2.51×, Panc 03.27 2.69×, LoVo 1.98×, COLO 205 4.17×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 2.60×; ⚠ cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.36×** | +4.4 | 0.006 | 25/46 (SW 900, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.69×** | +3.9 | 0.025 | 22/47 (SHP-77, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.27× | +3.4 | 0.14 | 20/48 (LoVo, LS 180, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.25× | +3.2 | 0.18 | 17/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.18 | 9/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.24× | +3.1 | 0.18 | 20/48 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.449×** | -11.4 | 4e-27 | 39/46 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -9.7 | 6e-20 | 37/41 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.611×** | -6.7 | 3e-09 | 33/48 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.715×** | -6.7 | 3e-09 | 36/48 (A-172, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -5.3 | 1e-05 | 30/49 (A498, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.7 | 2e-04 | 28/48 (SK-MEL-2, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.720×** | -4.5 | 6e-04 | 24/48 (NCI-H2347, C-33 A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -4.2 | 0.002 | 4/49 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.731×** | -4.2 | 0.002 | 25/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.820×** | -4.0 | 0.004 | 19/48 (A-172, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.9 | 0.004 | 23/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.683×** | -3.9 | 0.005 | 25/47 (HepG2/C3A, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.746×** | -3.8 | 0.005 | 22/44 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.622×** | -3.5 | 0.018 | 18/46 (LS 180, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.798×** | -3.2 | 0.053 | 19/48 (HOP62, HepG2/C3A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.793×** | -3.1 | 0.070 | 16/47 (A-172, LS 180, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.810×** | -3.0 | 0.095 | 14/48 (SW 1088, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 98.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -11.9) |
| [[A-172 (line)]] | wt | 104 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -10.8) |
| [[C32 (line)]] | wt | 81.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -14.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 90.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.250× (z -10.3) |
| [[LoVo (line)]] | wt | 40.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -23.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 77.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -12.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 58.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 73.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.418× (z -8.5) |
| [[SW480 (line)]] | alt | 26.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 82.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -9.4) |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.218× (z -8.6) |
| [[CHP-212 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 73.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0778× (z -15.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXP]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PDK3]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[VLDLR]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SAP30]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TENT4A]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[EFNA3]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.60 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD37]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPA]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[UTP20]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[FIZ1]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PRORP]] | -0.52 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TAF2]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MRRF]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[COMT]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GDAP1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DHX37]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[AGAP6]] | -0.51 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[RRP15]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[AMMECR1]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.9, -15.6); signed map (-35.9, 22.1). **Vector** length 124, 35.8% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.51 to 5); *glycolysis* (hallmark, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | +4.5 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.9 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | centriole, cilia and spindle associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:229,321,011-229,343,294 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41471, CSAP; previously C1orf96 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ19](https://www.uniprot.org/uniprotkb/Q6IQ19) (Centriole, cilia and spindle-associated protein):

> Plays a role in microtubule (MT) stabilization and this stabilization involves the maintenance of NUMA1 at the spindle poles. Colocalizes with polyglutamylated MTs to promote MT stabilization and regulate bipolar spindle formation in mitosis. Binding of CCSAP to centrosomes and the spindle around centrosomes during mitosis inhibits MT depolymerization, thereby stabilizing the mitotic spindle. May play a role in embryonic development. May be required for proper cilia beating (By similarity).

**Summary**, from NCBI Gene [126731](https://www.ncbi.nlm.nih.gov/gene/126731):

> Enables microtubule binding activity. Involved in mitotic spindle microtubule depolymerization and regulation of mitotic spindle assembly. Located in axon; ciliary transition zone; and cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29578) · Entrez [126731](https://www.ncbi.nlm.nih.gov/gene/126731) · UniProt [Q6IQ19](https://www.uniprot.org/uniprotkb/Q6IQ19) · Ensembl [ENSG00000154429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154429)

## Data

Gene col 7805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7805); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7805]; `tensor/DDL_lfc|DDL_z.npy` [7805]; `embed/gene_vectors.npy` [7805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7805 or target_col == 7805). Every well: [[CCSAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCSAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
