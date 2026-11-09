---
symbol: "ENDOD1"
type: "gene"
col: 7351
ensembl_id: "ENSG00000149218"
name: "endonuclease domain containing 1"
location: "11q21"
module: 23
arm: "-"
pooled_cpm: 21.51
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ENDOD1

*endonuclease domain containing 1* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.96× (z +9.4, q 2e-18, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.394× (z -18.4, q 0e+00, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UXS1]] (+0.61, fdr 1e-05), [[EHD4]] (+0.58, fdr 3e-05), [[HYAL2]] (+0.57, fdr 3e-05); moves opposite to [[ATE1OSP]] (-0.61, fdr 8e-05), [[OXA1L-DT]] (-0.60, fdr 5e-05), [[CDKL3]] (-0.59, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CNTNAP3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.96×** | +9.4 | 2e-18 | 42/46 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.8 | 5e-16 | 36/46 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.72×** | +7.7 | 3e-12 | 32/46 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +7.4 | 3e-11 | 34/45 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.57×** | +6.4 | 2e-08 | 26/46 (J82, AsPC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.7 | 1e-06 | 25/45 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.38×** | +4.4 | 8e-04 | 16/31 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.4 | 9e-04 | 18/45 (AsPC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 17/44 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.026 | 13/45 (HEC-1-A, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.394×** | -18.4 | 0e+00 | 33/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -12.5 | 3e-33 | 36/43 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -8.3 | 2e-14 | 27/43 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -7.2 | 8e-11 | 29/46 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.6 | 6e-09 | 24/44 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -5.6 | 2e-06 | 26/45 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -5.4 | 5e-06 | 23/45 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -5.3 | 1e-05 | 25/44 (PANC-1, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.682×** | -5.1 | 2e-05 | 25/44 (SW48, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -5.0 | 3e-05 | 18/45 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -4.4 | 5e-04 | 20/45 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -4.2 | 0.001 | 23/45 (CFPAC-1, SW 1271, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.741×** | -4.1 | 0.002 | 21/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -4.1 | 0.002 | 17/45 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -4.0 | 0.003 | 8/46 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.583×** | -3.9 | 0.003 | 17/44 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -3.9 | 0.003 | 18/46 (RPMI-7951, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 57.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.4) |
| [[PANC-1 (line)]] | alt | 27.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -26.5) |
| [[A-427 (line)]] | wt | 27.9 | 0 | 3 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.348× (z -12.1) |
| [[A498 (line)]] | wt | 21.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -19.9) |
| [[LoVo (line)]] | wt | 39.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 10.0 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.154× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.7) |
| [[SW48 (line)]] | wt | 32.5 | 0 | 3 | — | [[Orlistat (drug)]] 0.05 µM 0.147× (z -9.7) |
| [[C32 (line)]] | wt | 29.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.4) |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.3) |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.0) |
| [[HS-578T (line)]] | alt | 40.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.3) |
| [[KATO III (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.7) |
| [[LS 180 (line)]] | wt | 33.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.4) |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -9.9) |
| [[SW480 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -11.0) |
| [[A549 (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -12.7) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0819× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.7) |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.0) |
| [[HT-29 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.285× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 8.67 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.8) |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.2) |
| [[A-172 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UXS1]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[EHD4]] | +0.58 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[HYAL2]] | +0.57 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SPATA13]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[GDE1]] | +0.55 | +0.45 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[PIP4K2A]] | +0.54 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[TRAK1]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[TIAM1]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[EDA]] | +0.52 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[CARMIL1]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[PRRG1]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[VWA1]] | +0.52 | +0.49 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | -0.61 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[OXA1L-DT]] | -0.60 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[CDKL3]] | -0.59 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.57 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZNF547]] | -0.57 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[ZCWPW1]] | -0.57 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[MFF-DT]] | -0.55 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[ZNF785]] | -0.55 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[ZNF490]] | -0.54 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[GABPB2]] | -0.54 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[C11orf71]] | -0.54 | -0.41 / -0.24 | both halves | 5e-04 |  |
| [[SLC35E2B]] | -0.54 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3C]] | B | CNTNAP3C activity raises ENDOD1's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without CNTNAP3C | 0.004 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA |
| [[ACOXL]] | B | ACOXL activity raises ENDOD1's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without ACOXL | 0.019 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[GFOD1]] | B | GFOD1 activity strengthens ENDOD1's drug response | lines that do not express GFOD1 (5) vs lines expressing it (41) | the lines without GFOD1 respond 0.60× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 1.08x vs 0.37x (z diff +7.4) | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MAOB]] | B | MAOB activity raises ENDOD1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without MAOB | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[ROR1]] | B | ROR1 activity raises ENDOD1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without ROR1 | 0.022 | ⚠ within organs, on part of the lines |
| [[FAM3C2P]] | B | FAM3C2P activity strengthens ENDOD1's drug response | lines that do not express FAM3C2P (6) vs lines expressing it (40) | the lines without FAM3C2P respond 0.50× as strongly (z diff +1.50); strongest at Harringtonine 5 µM: 1.28x vs 0.34x (z diff +5.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TGM2]] | B | TGM2 activity raises ENDOD1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.64× lower at baseline in the lines without TGM2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[VWA1]] | B | VWA1 activity raises ENDOD1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without VWA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[ROR1]] | B | ROR1 activity strengthens ENDOD1's drug response | lines that do not express ROR1 (12) vs lines expressing it (34) | the lines without ROR1 respond 0.76× as strongly (z diff +0.86); strongest at Homoharringtonine 0.5 µM: 0.93x vs 0.44x (z diff +4.4) | 0.069 | ⚠ within organs, on part of the lines; target measured in part of the lines; both ways; artifact flags |
| [[ARHGAP20]] | B | ARHGAP20 activity raises ENDOD1's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 1.20× lower at baseline in the lines without ARHGAP20 | 0.082 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ENDOD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ENDOD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.5, 16.4); signed map (-18.4, 36.2). **Vector** length 81.8, 16.8% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.2 | +7.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -18.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | endonuclease domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,089,846-95,132,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0830 |
| Hallmark sets | HEME_METABOLISM, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [O94919](https://www.uniprot.org/uniprotkb/O94919) (Endonuclease domain-containing 1 protein):

> May act as a DNase and a RNase. Plays a role in the modulation of innate immune signaling through the cGAS-STING pathway by interacting with RNF26.

**Summary**, from NCBI Gene [23052](https://www.ncbi.nlm.nih.gov/gene/23052):

> Predicted to enable several functions, including endonuclease activity; metal ion binding activity; and nucleic acid binding activity. Predicted to be involved in innate immune response. Located in extracellular exosome and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29129) · Entrez [23052](https://www.ncbi.nlm.nih.gov/gene/23052) · UniProt [O94919](https://www.uniprot.org/uniprotkb/O94919) · Ensembl [ENSG00000149218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149218)

## Data

Gene col 7351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7351); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7351]; `tensor/DDL_lfc|DDL_z.npy` [7351]; `embed/gene_vectors.npy` [7351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7351 or target_col == 7351). Every well: [[ENDOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENDOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
