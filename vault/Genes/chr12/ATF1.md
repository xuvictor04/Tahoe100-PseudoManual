---
symbol: "ATF1"
type: "gene"
col: 4421
ensembl_id: "ENSG00000123268"
name: "activating transcription factor 1"
location: "12q13.12"
module: 51
arm: "+"
pooled_cpm: 91.64
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ATF1

*activating transcription factor 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.22× (z +9.7, q 2e-19, up in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (LoVo 3.61×, PANC-1 3.01×, COLO 205 6.56×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 1.64×, SK-MEL-2 1.85×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 2.10×, SHP-77 2.26×; ⚠ cell-cycle shift, explains ~15% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (PANC-1 2.87×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.402× (z -21.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWC22]] (+0.65, fdr 7e-06), [[EPC2]] (+0.63, fdr 7e-06), [[PRPF38B]] (+0.61, fdr 1e-05); moves opposite to [[SEC61A2]] (-0.61, fdr 1e-05), [[NAPB]] (-0.58, fdr 1e-05), [[ZDHHC16]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4421.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (LoVo 3.61×, PANC-1 3.01×, COLO 205 6.56×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 1.64×, SK-MEL-2 1.85×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 2.10×, SHP-77 2.26×; ⚠ cell-cycle shift, explains ~15% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (PANC-1 2.87×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +9.7 | 2e-19 | 41/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +8.1 | 1e-13 | 40/48 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +5.8 | 1e-06 | 28/48 (LS 180, SHP-77, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.15× | +3.4 | 0.11 | 20/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | 1.14× | +3.1 | 0.16 | 17/48 (LS 180, SHP-77, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.29× | +3.1 | 0.16 | 12/48 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.15× | +3.1 | 0.16 | 19/48 (SK-MEL-2, NCI-H2347, …) | top dose only | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.16 | 9/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.402×** | -21.2 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.466×** | -17.7 | 0e+00 | 48/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.491×** | -16.5 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -12.6 | 2e-34 | 39/49 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -9.3 | 1e-18 | 47/48 (SW 1088, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.681×** | -8.9 | 6e-17 | 39/48 (HepG2/C3A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -7.7 | 1e-12 | 36/48 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.565×** | -6.9 | 3e-10 | 41/49 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -6.3 | 2e-08 | 29/50 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.802×** | -4.9 | 5e-05 | 23/44 (SHP-77, LS 180, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.765×** | -4.7 | 2e-04 | 23/45 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.823×** | -4.5 | 3e-04 | 20/49 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.829×** | -4.2 | 0.001 | 23/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.848× | -3.8 | 0.005 | 20/48 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.843× | -3.8 | 0.005 | 15/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -3.7 | 0.009 | 17/48 (SW 900, NCI-H460, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.812×** | -3.6 | 0.010 | 22/48 (LoVo, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.878× | -3.6 | 0.010 | 15/48 (HEC-1-A, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 118 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.285× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 140 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -17.3) |
| [[LoVo (line)]] | wt | 148 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.61× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.374× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 92.8 | 0 | 5 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 117 | 1 (1 ⚠) | 4 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.79× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.299× (z -18.3) |
| [[PANC-1 (line)]] | alt | 104 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 3.01× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.339× (z -18.5) |
| [[RKO (line)]] | wt | 103 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -26.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.433× (z -10.3) |
| [[SHP-77 (line)]] | alt | 69.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +8.5) ⚠ cell-cycle shift, explains ~15% of this change | [[Panobinostat (drug)]] 5 µM 0.309× (z -12.2) |
| [[SNU-423 (line)]] | alt | 82.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.4) |
| [[SW480 (line)]] | alt | 162 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -19.2) |
| [[A-427 (line)]] | wt | 134 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 79.6 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 85.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.404× (z -12.5) |
| [[HOP62 (line)]] | alt | 61.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 78.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 78.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -12.0) |
| [[A549 (line)]] | wt | 96.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.3) |
| [[LS 180 (line)]] | wt | 88.9 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +8.9) ⚠ cell-cycle shift, explains ~15% of this change | [[Panobinostat (drug)]] 5 µM 0.468× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 65.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -11.3) |
| [[A-172 (line)]] | wt | 53.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.2) |
| [[C32 (line)]] | wt | 75.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 72.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.7) |
| [[COLO 205 (line)]] | alt | 87.6 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.56× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.292× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 60.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 94.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.7) |
| [[A498 (line)]] | wt | 53.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.8) |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -11.1) |
| [[H4 (line)]] | wt | 79.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.360× (z -8.5) |
| [[HCT15 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 49.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 55.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.6) |
| [[KATO III (line)]] | alt | 83.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -10.7) |
| [[SNU-1 (line)]] | wt | 93.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.350× (z -8.9) |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.0517× (z -9.9) |
| [[SW 1271 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 86.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -11.0) |
| [[SW1417 (line)]] | alt | 75.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -9.8) |
| [[AN3 CA (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC22]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[EPC2]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PRPF38B]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[HELQ]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RBM23]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CEBPZ]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[EPC1]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ADNP]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[GPATCH8]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CCDC97]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD17]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[NAPB]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ZDHHC16]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[DCUN1D4]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[OTULIN]] | -0.55 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[FAM199X]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[C1orf198]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CRAT]] | -0.52 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[AKTIP]] | -0.52 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[MICE]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RAB18]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TRAF6]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 | pathway: Interleukin-17 signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ATF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.2, 11.2); signed map (6.3, -17.9). **Vector** length 112, 32.5% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +8.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.5 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -17.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,763,710-50,821,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TREB36 |
| Gene groups (HGNC) | CREB1 transcription factor family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 28 pathways, smallest: CREB phosphorylation; MAPK targets/ Nuclear events mediated by MAP kinases; NGF-stimulated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P18846](https://www.uniprot.org/uniprotkb/P18846) (Cyclic AMP-dependent transcription factor ATF-1):

> This protein binds the cAMP response element (CRE) (consensus: 5'-GTGACGT[AC][AG]-3'), a sequence present in many viral and cellular promoters. Binds to the Tax-responsive element (TRE) of HTLV-I. Mediates PKA-induced stimulation of CRE-reporter genes. Represses the expression of FTH1 and other antioxidant detoxification genes. Triggers cell proliferation and transformation.

**Summary**, from NCBI Gene [466](https://www.ncbi.nlm.nih.gov/gene/466):

> This gene encodes an activating transcription factor, which belongs to the ATF subfamily and bZIP (basic-region leucine zipper) family. It influences cellular physiologic processes by regulating the expression of downstream target genes, which are related to growth, survival, and other cellular activities. This protein is phosphorylated at serine 63 in its kinase-inducible domain by serine/threonine kinases, cAMP-dependent protein kinase A, calmodulin-dependent protein kinase I/II, mitogen- and …

**Accessions** — [HGNC:783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:783) · Entrez [466](https://www.ncbi.nlm.nih.gov/gene/466) · UniProt [P18846](https://www.uniprot.org/uniprotkb/P18846) · Ensembl [ENSG00000123268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123268)

## Data

Gene col 4421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4421); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4421]; `tensor/DDL_lfc|DDL_z.npy` [4421]; `embed/gene_vectors.npy` [4421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4421 or target_col == 4421). Every well: [[ATF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
