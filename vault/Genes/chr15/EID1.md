---
symbol: "EID1"
type: "gene"
col: 14932
ensembl_id: "ENSG00000255302"
name: "EP300 interacting inhibitor of differentiation 1"
location: "15q21.1"
module: 16
arm: "+"
pooled_cpm: 52.76
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# EID1

*EP300 interacting inhibitor of differentiation 1* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +11.0, q 1e-25, up in 35 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.28× (z +4.0, q 0.006, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.643× (z -7.1, q 5e-10, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC30A]] (+0.70, fdr 7e-06), [[BBS10]] (+0.66, fdr 7e-06), [[PDHB]] (+0.62, fdr 7e-06); moves opposite to [[SLC35D2]] (-0.64, fdr 1e-05), [[PAM16]] (-0.56, fdr 2e-05), [[SMG1P5]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TTC30A]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF260]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.73×** | +11.0 | 1e-25 | 35/39 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.62×** | +11.0 | 1e-25 | 38/42 (A549, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.83×** | +6.4 | 2e-08 | 35/41 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.48×** | +4.5 | 9e-04 | 29/44 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.005 | 28/44 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.006 | 27/45 (A498, A-427, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +3.8 | 0.011 | 31/45 (MIA PaCa-2, AN3 CA, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.015 | 27/45 (A-172, C32, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.34×** | +3.3 | 0.051 | 28/45 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.076 | 26/45 (CFPAC-1, SNU-423, …) | top dose only | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.090 | 25/44 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.31×** | +3.1 | 0.090 | 22/45 (NCI-H1573, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.30× | +3.0 | 0.11 | 18/45 (A-172, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -7.1 | 5e-10 | 32/45 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.563×** | -6.6 | 1e-08 | 38/45 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.574×** | -6.0 | 3e-07 | 41/45 (PANC-1, J82, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.475×** | -4.5 | 0.001 | 30/42 (hTERT-HPNE, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -4.2 | 0.004 | 30/45 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.006 | 26/45 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.728×** | -3.6 | 0.023 | 24/45 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.733×** | -3.6 | 0.026 | 28/44 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.4 | 0.038 | 24/45 (J82, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.060 | 21/45 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.765× | -3.1 | 0.11 | 20/44 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.246× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 58.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 77.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 80.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.7) |
| [[PANC-1 (line)]] | alt | 47.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Bortezomib (drug)]] 0.05 µM 0.342× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 40.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 60.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.6) |
| [[A498 (line)]] | wt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 39.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 50.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 45.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 72.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 85.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.1) |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 75.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.5) |
| [[SW 1088 (line)]] | alt | 74.8 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 5 µM 0.0745× (z -8.6) |
| [[AN3 CA (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 53.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC30A]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[BBS10]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PDHB]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RANBP6]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ATP7A]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RRAGA]] | +0.58 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[AHR]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ATXN7L3B]] | +0.57 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NORAD]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35D2]] | -0.64 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[PAM16]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SMG1P5]] | -0.56 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[MROH1]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SNHG12]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[FAM229A]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[GNRH1]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[GAS5]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[DRD4]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[IL17RA]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZFYVE21]] | -0.53 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC30A]] | B | TTC30A activity raises EID1's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without TTC30A | 0.070 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[SMIM10]] | B | SMIM10 activity raises EID1's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without SMIM10 | 0.079 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[PSMB5]] | B | PSMB5 activity raises EID1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CEP41]] | C | CEP41 activity raises EID1's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 3.03× lower at baseline in the lines without CEP41 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF260]] | C | EID1 activity raises ZNF260's level | lines that do not express EID1 (3) vs lines expressing it (47) | 4.24× lower at baseline in the lines without EID1 | 0.008 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| [[CEP41]] | C | EID1 activity raises CEP41's level | lines that do not express EID1 (3) vs lines expressing it (47) | 3.57× lower at baseline in the lines without EID1 | 0.017 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | C | EID1, [[TMEM17]] activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 1.29× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |
| [[KRTCAP3]] | C | EID1 activity lowers KRTCAP3's level | lines that do not express EID1 (3) vs lines expressing it (47) | 3.56× higher at baseline in the lines without EID1 | 0.043 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| [[TTC30A]] | C | EID1 activity raises TTC30A's level | lines that do not express EID1 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without EID1 | 0.080 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| [[IL17RA]] | C | EID1 activity raises IL17RA's level | lines that do not express EID1 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without EID1 | 0.081 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| cells under [[Bendamustine (drug)]] 5 µM | C | EID1, [[TMEM17]] activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 0.77× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |
| cells under [[Epirubicin (hydrochloride) (drug)]] 0.5 µM | C | EID1, [[TMEM17]] activity lowers the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 1.26× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |
| cells under [[Nimesulide (drug)]] 5 µM | C | EID1, [[TMEM17]] activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 0.74× the cells of the other lines | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; cell counts less trustworthy; co-absent genes |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.9, 18.3); signed map (-0.4, -30.3). **Vector** length 91.5, 28.1% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.4 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.6 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.4 | -6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | EP300 interacting inhibitor of differentiation 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:48,878,134-48,880,173 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EID-1; previously C15orf3, CRI1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6B2](https://www.uniprot.org/uniprotkb/Q9Y6B2) (EP300-interacting inhibitor of differentiation 1):

> Interacts with RB1 and EP300 and acts as a repressor of MYOD1 transactivation. Inhibits EP300 and CBP histone acetyltransferase activity. May be involved in coupling cell cycle exit to the transcriptional activation of genes required for cellular differentiation. May act as a candidate coinhibitory factor for NR0B2 that can be directly linked to transcription inhibitory mechanisms.

**Summary**, from NCBI Gene [23741](https://www.ncbi.nlm.nih.gov/gene/23741):

> Enables histone acetyltransferase binding activity. Involved in cell differentiation and negative regulation of DNA-templated transcription. Acts upstream of or within negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1191) · Entrez [23741](https://www.ncbi.nlm.nih.gov/gene/23741) · UniProt [Q9Y6B2](https://www.uniprot.org/uniprotkb/Q9Y6B2) · Ensembl [ENSG00000255302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255302)

## Data

Gene col 14932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14932); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14932]; `tensor/DDL_lfc|DDL_z.npy` [14932]; `embed/gene_vectors.npy` [14932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14932 or target_col == 14932). Every well: [[EID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
