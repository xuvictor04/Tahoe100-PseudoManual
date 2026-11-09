---
symbol: "SMARCD1"
type: "gene"
col: 818
ensembl_id: "ENSG00000066117"
name: "SWI/SNF related BAF chromatin remodeling complex subunit D1"
location: "12q13.12"
module: 153
arm: "+"
pooled_cpm: 29.54
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# SMARCD1

*SWI/SNF related BAF chromatin remodeling complex subunit D1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.82× (z +16.1, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.85× (z +5.0, q 7e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.714× (z -7.4, q 9e-11, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX19]] (+0.64, fdr 1e-05), [[ARAF]] (+0.63, fdr 2e-05), [[RAB11B]] (+0.62, fdr 1e-05); moves opposite to [[SNHG9]] (-0.60, fdr 2e-05), [[FKBP2]] (-0.59, fdr 1e-05, ⚠ FKBP2 in the vector space only through flagged drug-doses), [[RPS29]] (-0.58, fdr 1e-05), [[CDK7]] (-0.57, fdr 7e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KCNK6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +16.1 | 0e+00 | 43/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +12.3 | 4e-32 | 31/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +10.9 | 1e-25 | 38/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +5.0 | 7e-05 | 25/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.34×** | +4.5 | 7e-04 | 24/46 (J82, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.32×** | +4.1 | 0.004 | 21/47 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.29×** | +3.9 | 0.007 | 20/48 (CFPAC-1, LS 180, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.8 | 0.010 | 22/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +3.8 | 0.010 | 14/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +3.7 | 0.013 | 17/48 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.5 | 0.021 | 16/40 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.075 | 21/47 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.075 | 9/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.084 | 15/47 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.1 | 0.084 | 12/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -7.4 | 9e-11 | 36/48 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.764×** | -4.2 | 0.008 | 22/48 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.775×** | -4.0 | 0.014 | 22/47 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.015 | 20/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.786×** | -3.7 | 0.019 | 22/47 (HEC-1-A, RKO, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -3.7 | 0.019 | 24/47 (SW 1271, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.846× | -3.7 | 0.019 | 18/48 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.793×** | -3.6 | 0.023 | 20/48 (SW 1088, LS 180, …) | all doses, stronger at high dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.854× | -3.5 | 0.032 | 13/48 (SHP-77, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.808×** | -3.3 | 0.051 | 18/47 (SW 1271, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +14.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.33× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 47.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0982× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0889× (z -11.2) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 34.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -10.3) |
| [[A549 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX19]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ARAF]] | +0.63 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[RAB11B]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[AP3M1]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TARDBP]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[PSMD1]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[BAP1]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[API5]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[OCRL]] | +0.59 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ANKRD40]] | +0.59 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MAPRE1]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 | STRING 409 |
| [[TAF6]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |

## Genes that move opposite

*30 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.60 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[FKBP2]] ⚠ | -0.59 | -0.50 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[CDK7]] | -0.57 | -0.38 / -0.65 | both halves | 7e-05 | pathway: Epigenetic regulation of gene expression |
| [[WSB1]] | -0.56 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[NDUFA1]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[POLR2H]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins |
| [[KCNK6]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[POLR1H]] | -0.55 | -0.34 / -0.61 | both halves | 1e-04 | pathway: Epigenetic regulation of gene expression |
| [[CEP164P1]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[MINDY2]] | -0.54 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[BET1]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK6]] | B | KCNK6 activity lowers SMARCD1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.36× higher at baseline in the lines without KCNK6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SMARCD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SMARCD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.5, -24.0); signed map (-14.5, -35.0). **Vector** length 88.8, 18.5% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,085,200-50,100,707 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAF60A, Rsc6p, CRACD1 |
| Gene groups (HGNC) | BAF complex subunits; PBAF complex subunits; GBAF complex subunits |
| Reactome | 22 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GM5](https://www.uniprot.org/uniprotkb/Q96GM5) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily D member 1):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and the neuron-specific chromatin remodeling complex (nBAF complex). …

**Summary**, from NCBI Gene [6602](https://www.ncbi.nlm.nih.gov/gene/6602):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and has sequence similarity to the yeast Swp73 protein. Two transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:11106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11106) · Entrez [6602](https://www.ncbi.nlm.nih.gov/gene/6602) · UniProt [Q96GM5](https://www.uniprot.org/uniprotkb/Q96GM5) · Ensembl [ENSG00000066117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066117)

## Data

Gene col 818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 818); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 818]; `tensor/DDL_lfc|DDL_z.npy` [818]; `embed/gene_vectors.npy` [818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 818 or target_col == 818). Every well: [[SMARCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
