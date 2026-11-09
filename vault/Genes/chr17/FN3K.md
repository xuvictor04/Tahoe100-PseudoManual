---
symbol: "FN3K"
type: "gene"
col: 9456
ensembl_id: "ENSG00000167363"
name: "fructosamine 3 kinase"
location: "17q25.3"
module: 57
arm: "+"
pooled_cpm: 8.62
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# FN3K

*fructosamine 3 kinase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.65× (z +7.1, q 6e-10, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.598× (z -10.4, q 1e-22, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSTM2]] (+0.58, fdr 2e-05), [[DMTN]] (+0.53, fdr 1e-05), [[CCDC183]] (+0.53, fdr 5e-05); moves opposite to [[EHBP1]] (-0.52, fdr 4e-05), [[SATB2]] (-0.48, fdr 1e-04), [[HOMER1]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HAS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +7.1 | 6e-10 | 23/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.1 | 8e-05 | 5/14 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.26×** | +4.7 | 5e-04 | 13/46 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.008 | 10/43 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.31×** | +3.9 | 0.011 | 6/46 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.11 | 6/43 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.27× | +3.2 | 0.11 | 5/25 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.25× | +3.1 | 0.12 | 10/32 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -10.4 | 1e-22 | 28/42 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.496×** | -9.7 | 1e-19 | 30/44 (Panc 03.27, HT-29, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.668×** | -8.2 | 6e-14 | 22/43 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.584×** | -7.7 | 2e-12 | 23/42 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.577×** | -7.6 | 4e-12 | 21/37 (LoVo, A-172, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -7.3 | 2e-11 | 23/43 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.636×** | -6.5 | 7e-09 | 25/46 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -6.4 | 1e-08 | 22/46 (LoVo, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.646×** | -6.3 | 2e-08 | 23/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.670×** | -5.7 | 5e-07 | 24/45 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.662×** | -5.7 | 7e-07 | 19/43 (A-427, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.685×** | -5.4 | 3e-06 | 15/46 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -5.1 | 2e-05 | 17/40 (MIA PaCa-2, CHP-212, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.525×** | -4.8 | 5e-05 | 15/46 (NCI-H460, SNU-423, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.538×** | -4.6 | 1e-04 | 14/41 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.724×** | -4.6 | 1e-04 | 19/43 (LoVo, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -4.3 | 6e-04 | 18/46 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.672×** | -4.1 | 0.001 | 16/43 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.792×** | -3.3 | 0.022 | 9/46 (COLO 205, A-172, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.861× | -3.0 | 0.059 | 5/46 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -11.9) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.104× (z -10.5) |
| [[SW480 (line)]] | alt | 6.22 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.4) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.116× (z -9.3) |
| [[HT-29 (line)]] | alt | 6.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0701× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -12.7) |
| [[KATO III (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0550× (z -8.7) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0707× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 7.21 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.6) |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0638× (z -10.3) |
| [[A498 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTM2]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[DMTN]] | +0.53 | +0.51 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[CCDC183]] | +0.53 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[ZNF852]] | +0.52 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[LPIN3]] | +0.49 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[TESMIN]] | +0.49 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SNX30]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[FN3KRP]] | +0.48 | +0.41 / +0.51 | both halves | 4e-05 | pathway: Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation; ⚠ same locus (5.3 kb, same strand: neighbours can correlate without regulation) |
| [[CIZ1]] | +0.48 | +0.32 / +0.50 | both halves | 2e-04 | STRING 434 |
| [[ABCA2]] | +0.48 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[BACE1-AS]] | +0.47 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[SNX15]] | +0.46 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[SPIN3]] | +0.46 | +0.24 / +0.52 | both halves | 5e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SATB2]] | -0.48 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[HOMER1]] | -0.46 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[PTPRG]] | -0.46 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[TUBA4A]] | -0.46 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[SCHIP1]] | -0.45 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[LETM2]] | -0.44 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[RIC8B]] | -0.44 | -0.21 / -0.44 | both halves | 6e-04 |  |
| [[C14orf119]] | -0.43 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[ITPR2]] | -0.43 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[USP43]] | -0.43 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[S100A11]] | -0.43 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAS2]] | B | HAS2 activity lowers FN3K's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.71× higher at baseline in the lines without HAS2 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[TOP2A]] | B | TOP2A activity raises FN3K's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH5A1]] | B | ALDH5A1 activity raises FN3K's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 2.12× lower at baseline in the lines without ALDH5A1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ |
| [[EPS8L2]] | B | EPS8L2 activity raises FN3K's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.59× lower at baseline in the lines without EPS8L2 | 0.087 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[GSTM2]] | C | GSTM2 activity raises FN3K's level | lines that do not express GSTM2 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without GSTM2 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLEC2D, IMPG2, ENSG00000286952; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.3, 30.5); signed map (-28.5, -3.1). **Vector** length 58.8, 8.04% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.7 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.5 | -5.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | fructosamine 3 kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,735,615-82,751,196 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fructosamine 3 kinase family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H479](https://www.uniprot.org/uniprotkb/Q9H479) (Fructosamine-3-kinase):

> Fructosamine-3-kinase involved in protein deglycation by mediating phosphorylation of fructoselysine residues on glycated proteins, to generate fructoselysine-3 phosphate. Fructoselysine-3 phosphate adducts are unstable and decompose under physiological conditions. Involved in intracellular deglycation in erythrocytes. Involved in the response to oxidative stress by mediating deglycation of NFE2L2/NRF2, glycation impairing NFE2L2/NRF2 function (By similarity). Also able to phosphorylate …

**Summary**, from NCBI Gene [64122](https://www.ncbi.nlm.nih.gov/gene/64122):

> A high concentration of glucose can result in non-enzymatic oxidation of proteins by reaction of glucose and lysine residues (glycation). Proteins modified in this way, fructosamines, are less active or functional. This gene encodes an enzyme which catalyzes the phosphorylation of fructosamines which may result in deglycation. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:24822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24822) · Entrez [64122](https://www.ncbi.nlm.nih.gov/gene/64122) · UniProt [Q9H479](https://www.uniprot.org/uniprotkb/Q9H479) · Ensembl [ENSG00000167363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167363)

## Data

Gene col 9456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9456); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9456]; `tensor/DDL_lfc|DDL_z.npy` [9456]; `embed/gene_vectors.npy` [9456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9456 or target_col == 9456). Every well: [[FN3K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FN3K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
