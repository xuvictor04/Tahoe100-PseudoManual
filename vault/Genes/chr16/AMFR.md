---
symbol: "AMFR"
type: "gene"
col: 8258
ensembl_id: "ENSG00000159461"
name: "autocrine motility factor receptor"
location: "16q13"
module: 214
arm: "+"
pooled_cpm: 47.91
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# AMFR

*autocrine motility factor receptor* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.75× (z +11.8, q 3e-29, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.731× (z -6.6, q 3e-08, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 0.791× (z -4.6, q 1e-03, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.305×, A-172 0.461×, J82 0.494×, NCI-H1792 0.484×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.143×, NCI-H1573 0.398×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.399×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.176×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHPT1]] (+0.62, fdr 1e-05), [[REEP5]] (+0.61, fdr 1e-05), [[CARM1]] (+0.58, fdr 1e-05); moves opposite to [[SPTY2D1]] (-0.51, fdr 3e-05), [[SLFN11]] (-0.50, fdr 3e-05), [[MFAP1]] (-0.49, fdr 1e-05).
> It is in [[Module 214]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +11.8 | 3e-29 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +9.7 | 1e-19 | 40/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +9.5 | 5e-19 | 43/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +8.7 | 7e-16 | 36/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +8.6 | 8e-16 | 37/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +8.1 | 3e-14 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +8.1 | 3e-14 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +8.1 | 5e-14 | 30/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +8.0 | 9e-14 | 35/48 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 5e-07 | 27/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.9 | 6e-05 | 19/35 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.2 | 0.001 | 15/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 24/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.011 | 15/45 (PANC-1, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.017 | 20/45 (PANC-1, AsPC-1, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.025 | 9/48 (NCI-H460, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.029 | 11/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.044 | 18/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8258.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.305×, A-172 0.461×, J82 0.494×, NCI-H1792 0.484×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.143×, NCI-H1573 0.398×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.399×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.176×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.731×** | -6.6 | 3e-08 | 28/48 (A549, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.758×** | -5.8 | 2e-06 | 30/48 (A549, KATO III, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.6 | 1e-03 | 24/47 (A-172, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -4.1 | 0.006 | 14/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.701×** | -3.9 | 0.011 | 19/47 (MIA PaCa-2, A549, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.7 | 0.019 | 16/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.839× | -3.7 | 0.019 | 13/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Proglumide (drug)]] 0.05 µM |  | 0.845× | -3.5 | 0.028 | 17/48 (A549, A498, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.865× | -3.0 | 0.15 | 9/48 (SW480, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.2 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +12.5) | — |
| [[SW480 (line)]] | alt | 51.1 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 52.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.61× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 71.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 34.2 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +11.2) | — |
| [[A549 (line)]] | wt | 63.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.62× (z +9.4) | — |
| [[A-427 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -18.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 73.2 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.176× (z -8.5) |
| [[J82 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 37.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +10.8) | — |
| [[LoVo (line)]] | wt | 38.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 59.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[SW48 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[REEP5]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CARM1]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[STIM1]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TEAD2]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ADD1]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MFSD14B]] | +0.56 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[CDS2]] | +0.56 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NBL1]] | +0.56 | +0.67 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[LAMB2]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SAP30L]] | +0.55 | +0.62 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTY2D1]] | -0.51 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SLFN11]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[MFAP1]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SCFD1]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[HOMER1]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[MYSM1]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[BLZF1]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[BTG1]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GALE]] | -0.46 | -0.52 / -0.39 | both halves | 5e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[BRD2]] | -0.45 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[FAM43A]] | -0.45 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[TENT5C]] | -0.45 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.4, -15.4); signed map (-41.0, -26.2). **Vector** length 90.9, 20.4% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.1 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.6 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.1 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.7 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | autocrine motility factor receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,361,452-56,425,545 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF45, gp78 |
| Gene groups (HGNC) | Ring finger proteins; CUE domain containing; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKV5](https://www.uniprot.org/uniprotkb/Q9UKV5) (E3 ubiquitin-protein ligase AMFR):

> E3 ubiquitin-protein ligase that mediates the polyubiquitination of lysine and cysteine residues on target proteins, such as CD3D, CYP3A4, CFTR, INSIG1, SOAT2/ACAT2 and APOB for proteasomal degradation. Component of a VCP/p97-AMFR/gp78 complex that participates in the final step of endoplasmic reticulum-associated degradation (ERAD). The VCP/p97-AMFR/gp78 complex is involved in the sterol-accelerated ERAD degradation of HMGCR through binding to the HMGCR-INSIG1 complex at the ER membrane. In …

**Summary**, from NCBI Gene [267](https://www.ncbi.nlm.nih.gov/gene/267):

> This locus encodes a glycosylated transmembrane receptor. Its ligand, autocrine motility factor, is a tumor motility-stimulating protein secreted by tumor cells. The encoded receptor is also a member of the E3 ubiquitin ligase family of proteins. It catalyzes ubiquitination and endoplasmic reticulum-associated degradation of specific proteins. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:463) · Entrez [267](https://www.ncbi.nlm.nih.gov/gene/267) · UniProt [Q9UKV5](https://www.uniprot.org/uniprotkb/Q9UKV5) · Ensembl [ENSG00000159461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159461)

## Data

Gene col 8258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8258); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8258]; `tensor/DDL_lfc|DDL_z.npy` [8258]; `embed/gene_vectors.npy` [8258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8258 or target_col == 8258). Every well: [[AMFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
