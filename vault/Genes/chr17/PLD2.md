---
symbol: "PLD2"
type: "gene"
col: 4956
ensembl_id: "ENSG00000129219"
name: "phospholipase D2"
location: "17p13.2"
module: 30
arm: "+"
pooled_cpm: 13.95
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PLD2

*phospholipase D2* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.62× (z +8.0, q 6e-13, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.454× (z -13.1, q 1e-36, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK3]] (+0.69, fdr 7e-06), [[FCHSD1]] (+0.69, fdr 1e-05), [[USP35]] (+0.69, fdr 1e-05); moves opposite to [[MZF1-AS1]] (-0.62, fdr 4e-05), [[LEKR1]] (-0.60, fdr 4e-05), [[ERCC6L2]] (-0.59, fdr 8e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SNTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +8.0 | 6e-13 | 28/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 3e-08 | 24/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.30×** | +6.2 | 1e-07 | 22/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +4.8 | 2e-04 | 16/41 (AsPC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.012 | 12/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +3.8 | 0.012 | 12/46 (NCI-H2030, NCI-H23, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.040 | 12/47 (NCI-H460, NCI-H1573, …) | rises with dose | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +3.4 | 0.040 | 9/47 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.073 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.12 | 8/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.21× | +3.0 | 0.13 | 9/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.454×** | -13.1 | 1e-36 | 36/47 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -12.1 | 5e-31 | 35/46 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.614×** | -11.5 | 4e-28 | 32/47 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.528×** | -10.6 | 3e-24 | 32/47 (A-172, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.587×** | -8.9 | 8e-17 | 33/45 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.590×** | -8.8 | 1e-16 | 33/48 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -8.1 | 6e-14 | 32/47 (A549, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.628×** | -7.7 | 7e-13 | 29/47 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.622×** | -7.6 | 2e-12 | 25/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -7.0 | 2e-10 | 24/44 (SNU-423, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.666×** | -6.8 | 7e-10 | 26/47 (SW480, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -6.1 | 4e-08 | 9/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.740×** | -5.0 | 2e-05 | 19/46 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -4.9 | 3e-05 | 20/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.761×** | -4.5 | 2e-04 | 13/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -3.4 | 0.025 | 11/48 (J82, A-172, …) | top dose only |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.877× | -3.1 | 0.062 | 6/48 (NCI-H1792, A-427, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | 0.836× | -3.0 | 0.078 | 7/48 (A498, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0537× (z -18.3) |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -9.0) |
| [[A549 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -8.7) |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 9.68 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0818× (z -10.0) |
| [[SW 900 (line)]] | alt | 5.94 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0801× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0825× (z -8.8) |
| [[SW480 (line)]] | alt | 12.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.301× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 26.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.197× (z -12.2) |
| [[C32 (line)]] | wt | 8.94 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.101× (z -9.0) |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0889× (z -10.6) |
| [[KATO III (line)]] | alt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.2) |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.113× (z -8.7) |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK3]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[FCHSD1]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[USP35]] | +0.69 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TCIRG1]] | +0.67 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.66 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.66 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[DOK4]] | +0.65 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[STX7]] | +0.63 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[NTAN1]] | +0.63 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[NBPF1]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1-AS1]] | -0.62 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[LEKR1]] | -0.60 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[ZFP91]] | -0.57 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[MCTS1]] | -0.56 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[P2RY11]] | -0.56 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[PCBP1-AS1]] | -0.56 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[WARS2-AS1]] | -0.56 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | -0.56 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[ZNF876P]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NSUN6]] | -0.56 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ST7L]] | -0.56 | -0.59 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | SNTA1 activity raises PLD2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without SNTA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PLD2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers PLD2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NAALADL2]] | B | NAALADL2 activity lowers PLD2's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.32× higher at baseline in the lines without NAALADL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[OSBPL7]] | B | OSBPL7 activity lowers PLD2's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.38× higher at baseline in the lines without OSBPL7 | 0.092 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.4, -7.6); signed map (-31.4, -4.9). **Vector** length 80.5, 14.9% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.2 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.1 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,807,152-4,823,434 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases |
| Reactome | 13 pathways, smallest: Synthesis of PG; Role of phospholipids in phagocytosis; Synthesis of PA |
| Matched by | ensembl_id |

**Function**, from UniProt [O14939](https://www.uniprot.org/uniprotkb/O14939) (Phospholipase D2):

> Function as phospholipase selective for phosphatidylcholine. May have a role in signal-induced cytoskeletal regulation and/or endocytosis (By similarity).

**Summary**, from NCBI Gene [5338](https://www.ncbi.nlm.nih.gov/gene/5338):

> The protein encoded by this gene catalyzes the hydrolysis of phosphatidylcholine to phosphatidic acid and choline. The activity of the encoded enzyme is enhanced by phosphatidylinositol 4,5-bisphosphate and ADP-ribosylation factor-1. This protein localizes to the peripheral membrane and may be involved in cytoskeletal organization, cell cycle control, transcriptional regulation, and/or regulated secretion. Two transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:9068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9068) · Entrez [5338](https://www.ncbi.nlm.nih.gov/gene/5338) · UniProt [O14939](https://www.uniprot.org/uniprotkb/O14939) · Ensembl [ENSG00000129219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129219)

## Data

Gene col 4956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4956); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4956]; `tensor/DDL_lfc|DDL_z.npy` [4956]; `embed/gene_vectors.npy` [4956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4956 or target_col == 4956). Every well: [[PLD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
