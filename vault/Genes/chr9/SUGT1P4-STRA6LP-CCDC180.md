---
symbol: "SUGT1P4-STRA6LP-CCDC180"
type: "gene"
col: 14912
ensembl_id: "ENSG00000255036"
name: "SUGT1P4-STRA6LP-CCDC180 readthrough"
location: "9q22.33"
module: 17
arm: "+"
pooled_cpm: 3.25
n_lines_expressing: 41
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SUGT1P4-STRA6LP-CCDC180

*SUGT1P4-STRA6LP-CCDC180 readthrough* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Glycyrrhizic acid (drug)]] 0.5 µM: 1.49× (z +3.8, q 0.039, up in 9 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.233× (z -13.9, q 3e-41, down in 31 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRA6LP]] (+0.85, fdr 7e-06, ⚠ same locus), [[SUGT1P4-STRA6LP]] (+0.84, fdr 7e-06, ⚠ same locus), [[CCDC180]] (+0.79, fdr 7e-06, ⚠ same locus), [[LINC00888]] (+0.60, fdr 1e-05), [[ZNF177]] (+0.59, fdr 2e-05), [[MRPS31P4]] (+0.57, fdr 4e-05); moves opposite to [[DNASE1]] (-0.54, fdr 9e-05), [[BANP]] (-0.54, fdr 4e-05), [[CDK6-AS1]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[CNEP1R1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.039 | 9/34 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.039 | 7/36 (HEC-1-A, SHP-77, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.25× | +3.1 | 0.26 | 4/36 (A549, COLO 205, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 1.38× | +3.1 | 0.26 | 7/37 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.36× | +3.0 | 0.29 | 7/36 (SNU-423, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.233×** | -13.9 | 3e-41 | 31/38 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.308×** | -11.2 | 8e-27 | 30/36 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.468×** | -10.2 | 4e-22 | 22/32 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.373×** | -9.4 | 8e-19 | 16/25 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.389×** | -8.7 | 5e-16 | 18/29 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.403×** | -8.6 | 5e-16 | 25/36 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.563×** | -7.7 | 9e-13 | 17/30 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.466×** | -7.0 | 2e-10 | 15/29 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.504×** | -6.5 | 5e-09 | 21/36 (SNU-423, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -5.5 | 2e-06 | 16/35 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.561×** | -5.3 | 7e-06 | 16/36 (A498, A549, …) | rises with dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.678×** | -5.2 | 1e-05 | 15/37 (A-172, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -4.5 | 2e-04 | 13/36 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.653×** | -4.0 | 0.002 | 14/36 (A498, RPMI-7951, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.661×** | -3.9 | 0.003 | 12/36 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -3.8 | 0.006 | 8/36 (SNU-1, A549, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.588×** | -3.6 | 0.009 | 8/15 (NCI-H23, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.675×** | -3.4 | 0.016 | 10/36 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.021 | 11/37 (BT-474, H4, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.738×** | -2.9 | 0.094 | 5/36 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.52 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0637× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 8.40 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0509× (z -11.6) |
| [[HS-578T (line)]] | alt | 5.52 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0509× (z -10.6) |
| [[PANC-1 (line)]] | alt | 6.11 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0255× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0856× (z -13.5) |
| [[SNU-423 (line)]] | alt | 6.15 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0964× (z -12.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0709× (z -10.2) |
| [[A498 (line)]] | wt | 3.69 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0803× (z -13.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.2) |
| [[A-172 (line)]] | wt | 6.28 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0685× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0605× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRA6LP]] | +0.85 | +0.78 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SUGT1P4-STRA6LP]] | +0.84 | +0.77 / +0.83 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CCDC180]] | +0.79 | +0.71 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00888]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ZNF177]] | +0.59 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[MRPS31P4]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MOCS1]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[POT1]] | +0.55 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[ELP1]] | +0.53 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[ZNF527]] | +0.53 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[HLTF]] | +0.51 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[SKIC3]] | +0.50 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[TTLL1]] | +0.49 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[SAAL1]] | +0.49 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[TTC26]] | +0.49 | +0.30 / +0.53 | both halves | 2e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNASE1]] | -0.54 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[BANP]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CDK6-AS1]] | -0.53 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[CIBAR1-DT]] | -0.51 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[RFX3]] | -0.51 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[FOXC1]] | -0.50 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[UBE2R2-AS1]] | -0.50 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SOX11]] | -0.49 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[LINC00534]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[PAX8-AS1]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[SPHK1]] | -0.48 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[EMSY-DT]] | -0.48 | -0.28 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SUGT1P4-STRA6LP-CCDC180's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZSCAN23]] | B | ZSCAN23 activity raises SUGT1P4-STRA6LP-CCDC180's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without ZSCAN23 | 0.067 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[CCDC180]] | C | CCDC180 activity raises SUGT1P4-STRA6LP-CCDC180's level | lines that do not express CCDC180 (8) vs lines expressing it (42) | 3.44× lower at baseline in the lines without CCDC180 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: STRA6LP; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNEP1R1]] | B | [[STRA6LP]], [[SUGT1P4-STRA6LP]], SUGT1P4-STRA6LP-CCDC180 activity lowers CNEP1R1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.19× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[LYPLA2]] | B | [[STRA6LP]], [[SUGT1P4-STRA6LP]], SUGT1P4-STRA6LP-CCDC180 activity lowers LYPLA2's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.15× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[CCDC180]] | C | [[STRA6LP]], [[SUGT1P4-STRA6LP]], SUGT1P4-STRA6LP-CCDC180 activity raises CCDC180's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 5.07× lower at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.5, -4.3); signed map (-25.8, -14.5). **Vector** length 47.8, 6.17% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.1 | +3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +0.8 | +2.0 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | +0.7 | +3.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.7 | +3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +0.6 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +0.6 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -6.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SUGT1P4-STRA6LP-CCDC180 readthrough |
| Locus type | readthrough (other) |
| Location | 9q22.33 — chr9:97,238,497-97,377,287 (+) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [57653](https://www.ncbi.nlm.nih.gov/gene/57653):

> This locus represents a set of read-through transcripts spanning an upstream pseudogene (GeneID:100499484) extending into a downstream protein-coding locus (GeneID:100499483). All of the read-through transcripts are candidates for nonsense-mediated decay (NMD), so they are not thought to express a protein. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:53835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53835) · Entrez [57653](https://www.ncbi.nlm.nih.gov/gene/57653) · Ensembl [ENSG00000255036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255036)

## Data

Gene col 14912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14912); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14912]; `tensor/DDL_lfc|DDL_z.npy` [14912]; `embed/gene_vectors.npy` [14912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14912 or target_col == 14912). Every well: [[SUGT1P4-STRA6LP-CCDC180 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGT1P4-STRA6LP-CCDC180.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
