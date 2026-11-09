---
symbol: "PIGA"
type: "gene"
col: 9085
ensembl_id: "ENSG00000165195"
name: "phosphatidylinositol glycan anchor biosynthesis class A"
location: "Xp22.2"
module: 180
arm: "+"
pooled_cpm: 23.9
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# PIGA

*phosphatidylinositol glycan anchor biosynthesis class A* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.10× (z +11.0, q 2e-25, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.756× (z -5.2, q 1e-04, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.334×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA8]] (+0.62, fdr 7e-06), [[FEM1C]] (+0.61, fdr 1e-05), [[EOLA1]] (+0.55, fdr 3e-05); moves opposite to [[TFAM]] (-0.53, fdr 4e-05), [[TGFBRAP1]] (-0.50, fdr 4e-05), [[TCF12]] (-0.48, fdr 1e-04).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.10×** | +11.0 | 2e-25 | 43/48 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +5.9 | 1e-06 | 24/47 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.4 | 1e-05 | 25/47 (BT-474, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.1 | 5e-05 | 26/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.10×** | +5.0 | 6e-05 | 28/45 (CFPAC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.9 | 1e-04 | 26/48 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.7 | 2e-04 | 2/48 (A498, RPMI-7951) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 24/47 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +4.5 | 5e-04 | 19/47 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.40×** | +4.3 | 9e-04 | 18/47 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.001 | 21/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 17/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.007 | 19/46 (LS 180, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.007 | 20/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.014 | 16/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.014 | 16/46 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.015 | 16/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.017 | 14/48 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9085.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.334×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.756×** | -5.2 | 1e-04 | 26/48 (A549, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -4.4 | 0.003 | 21/32 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.732×** | -4.1 | 0.008 | 21/48 (NCI-H1792, RKO, …) | two highest doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.786× | -3.2 | 0.22 | 18/48 (A-172, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.6 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.24× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 67.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +8.6) ⚠ cell-cycle shift, explains ~19% of this change | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 45.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.39× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.9) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[J82 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 13.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.2× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 53.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.0× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.0) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA8]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FEM1C]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[EOLA1]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ARID5A]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MAPK7]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PTPRH]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PPP2R5B]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ERO1A]] | +0.54 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[NGLY1]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ARG2]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[RELA]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[CLK3]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAM]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TGFBRAP1]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[TCF12]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[XPO4]] | -0.48 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[ZZZ3]] | -0.48 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[SLC25A13]] | -0.48 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[PAXBP1]] | -0.47 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[UBE2E3]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[CTDSPL]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[UTP20]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[GTF2I]] | -0.46 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[USP24]] | -0.45 | -0.24 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity raises PIGA's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without NDRG1 | 0.080 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.7, -15.4); signed map (-35.8, 25.7). **Vector** length 84.0, 17.7% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +1.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.0 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.0 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.0 | +0.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:15,319,452-15,335,554 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPI3, PIG-A |
| Gene groups (HGNC) | Glycosyl transferases group 1 domain containing; Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol-N-acetylglucosaminyltransferase complex |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P37287](https://www.uniprot.org/uniprotkb/P37287) (Phosphatidylinositol N-acetylglucosaminyltransferase subunit A):

> Catalytic subunit of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis.

**Summary**, from NCBI Gene [5277](https://www.ncbi.nlm.nih.gov/gene/5277):

> This gene encodes a protein required for synthesis of N-acetylglucosaminyl phosphatidylinositol (GlcNAc-PI), the first intermediate in the biosynthetic pathway of GPI anchor. The GPI anchor is a glycolipid found on many blood cells and which serves to anchor proteins to the cell surface. Paroxysmal nocturnal hemoglobinuria, an acquired hematologic disorder, has been shown to result from mutations in this gene. Alternate splice variants have been characterized. A related pseudogene is located on …

**Accessions** — [HGNC:8957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8957) · Entrez [5277](https://www.ncbi.nlm.nih.gov/gene/5277) · UniProt [P37287](https://www.uniprot.org/uniprotkb/P37287) · Ensembl [ENSG00000165195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165195)

## Data

Gene col 9085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9085); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9085]; `tensor/DDL_lfc|DDL_z.npy` [9085]; `embed/gene_vectors.npy` [9085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9085 or target_col == 9085). Every well: [[PIGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
