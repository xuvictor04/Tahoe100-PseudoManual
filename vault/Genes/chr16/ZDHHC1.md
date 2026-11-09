---
symbol: "ZDHHC1"
type: "gene"
col: 8272
ensembl_id: "ENSG00000159714"
name: "zDHHC palmitoyltransferase 1"
location: "16q22.1"
module: 23
arm: "+"
pooled_cpm: 6.77
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ZDHHC1

*zDHHC palmitoyltransferase 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +6.6, q 2e-08, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.380× (z -5.5, q 2e-05, down in 19 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0696×, SW480 0.0844×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.239×, LOX-IMVI 0.150×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Naproxen (drug)]] 5 µM in 1 line (C32 0.0884×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (COLO 205 0.0656×); [[PH-797804 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0450×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATE1OSP]] (+0.65, fdr 1e-05), [[SLC9A8]] (+0.65, fdr 4e-05), [[ZC3HC1]] (+0.65, fdr 1e-05); moves opposite to [[TNIK]] (-0.59, fdr 3e-05), [[PPAT]] (-0.59, fdr 1e-04), [[SKP2]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00944]] → it (grade B ⚠); 7 go from it, the strongest it → [[UNK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +6.6 | 2e-08 | 25/41 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.017 | 11/41 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.017 | 15/42 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.8 | 0.019 | 5/13 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +3.6 | 0.039 | 7/44 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.040 | 10/43 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.040 | 8/43 (PANC-1, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0696×, SW480 0.0844×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.239×, LOX-IMVI 0.150×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Naproxen (drug)]] 5 µM in 1 line (C32 0.0884×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (COLO 205 0.0656×); [[PH-797804 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0450×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.380×** | -5.5 | 2e-05 | 19/38 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.389×** | -5.3 | 2e-05 | 22/43 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.612×** | -5.3 | 2e-05 | 19/43 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.645×** | -4.7 | 3e-04 | 18/37 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.692×** | -4.0 | 0.007 | 15/42 (NCI-H1792, BT-474, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.694×** | -3.8 | 0.014 | 15/32 (HOP62, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.735×** | -3.3 | 0.068 | 16/43 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.737×** | -3.3 | 0.068 | 17/43 (NCI-H23, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +19.3) | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 6.52 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0884× (z -9.3) |
| [[COLO 205 (line)]] | alt | 7.33 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0656× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 8.66 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0450× (z -9.0) |
| [[PANC-1 (line)]] | alt | 6.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 2.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0844× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SLC9A8]] | +0.65 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[ZC3HC1]] | +0.65 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.63 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[WBP4]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[HPS1]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CCDC122]] | +0.62 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[HOMER3]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[NFKBIB]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ITSN2]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SLC66A1]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CDK3]] | +0.60 | +0.57 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNIK]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[PPAT]] | -0.59 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SKP2]] | -0.58 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ERI1]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.57 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[TMED7]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[HLTF]] | -0.56 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[PAPSS1]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TUBB]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SAR1A]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[NT5DC3]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ELP1]] | -0.53 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00944]] | B | LINC00944 activity lowers ZDHHC1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.41× higher at baseline in the lines without LINC00944 | 0.050 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[HDAC6]] | B | HDAC6 activity raises ZDHHC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNK]] | C | ZDHHC1 activity raises UNK's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without ZDHHC1 | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM | C | ZDHHC1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express ZDHHC1 (4) vs lines expressing it (44) | the lines without ZDHHC1: 0.78× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[GGA3]] | C | ZDHHC1 activity raises GGA3's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without ZDHHC1 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[CDK3]] | C | ZDHHC1 activity raises CDK3's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.47× lower at baseline in the lines without ZDHHC1 | 0.073 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[C7orf31]] | C | ZDHHC1 activity raises C7orf31's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without ZDHHC1 | 0.087 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[SLC9A8]] | C | ZDHHC1 activity lowers SLC9A8's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without ZDHHC1 | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[ACYP2]] | C | ZDHHC1 activity raises ACYP2's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without ZDHHC1 | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-8.5, 15.9); signed map (4.1, -11.0). **Vector** length 56.6, 8.17% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.3 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.1 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,394,152-67,416,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSU90653, ZNF377; previously C16orf1 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTX9](https://www.uniprot.org/uniprotkb/Q8WTX9) (Palmitoyltransferase ZDHHC1):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates, such as NCDN and NLRP3. Has a palmitoyltransferase activity toward NCDN and regulates NCDN association with endosome membranes through this palmitoylation (By similarity). Acts as an activator of the NLRP3 inflammasome by mediating palmitoylation of 'Cys-130' and 'Cys-958' of NLRP3, thereby promoting NLRP3 phosphorylation and activation by NEK7.; Also has a palmitoyltransferase activity-independent …

**Summary**, from NCBI Gene [29800](https://www.ncbi.nlm.nih.gov/gene/29800):

> Enables protein-cysteine S-palmitoyltransferase activity. Involved in antiviral innate immune response; positive regulation of NLRP3 inflammasome complex assembly; and positive regulation of defense response to virus by host. Located in Golgi apparatus and endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17916) · Entrez [29800](https://www.ncbi.nlm.nih.gov/gene/29800) · UniProt [Q8WTX9](https://www.uniprot.org/uniprotkb/Q8WTX9) · Ensembl [ENSG00000159714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159714)

## Data

Gene col 8272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8272); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8272]; `tensor/DDL_lfc|DDL_z.npy` [8272]; `embed/gene_vectors.npy` [8272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8272 or target_col == 8272). Every well: [[ZDHHC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
