---
symbol: "STRA6LP"
type: "gene"
col: 14886
ensembl_id: "ENSG00000254633"
name: "STRA6 like, pseudogene"
location: "9q22.33"
module: 17
arm: "+"
pooled_cpm: 3.04
n_lines_expressing: 41
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# STRA6LP

*STRA6 like, pseudogene* — 9q22.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.243× (z -13.1, q 1e-36, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGT1P4-STRA6LP]] (+0.95, fdr 7e-06, ⚠ same locus), [[SUGT1P4-STRA6LP-CCDC180]] (+0.85, fdr 7e-06, ⚠ same locus), [[MRPS31P4]] (+0.78, fdr 7e-06), [[LINC00888]] (+0.71, fdr 7e-06), [[ELP1]] (+0.67, fdr 1e-05); moves opposite to [[MIATNB]] (-0.62, fdr 2e-05), [[RFX3]] (-0.61, fdr 2e-05), [[FBXL19-AS1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RASSF4]] → it (grade B ⚠); 7 go from it, the strongest it → [[PAPSS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.47× | +3.5 | 0.18 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.44× | +3.4 | 0.18 | 3/37 (RKO, NCI-H2347, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 1.39× | +3.1 | 0.35 | 10/37 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.38× | +3.0 | 0.35 | 3/36 (HT-29, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.243×** | -13.1 | 1e-36 | 29/38 (SHP-77, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.407×** | -11.8 | 2e-29 | 28/31 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.340×** | -10.0 | 3e-21 | 23/34 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.351×** | -9.7 | 5e-20 | 26/36 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.358×** | -9.1 | 7e-18 | 21/29 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -9.1 | 9e-18 | 19/27 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.393×** | -8.3 | 8e-15 | 20/29 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.561×** | -7.6 | 3e-12 | 23/37 (HOP62, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.487×** | -6.6 | 2e-09 | 21/36 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.639×** | -4.1 | 0.002 | 12/36 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -4.1 | 0.003 | 14/36 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.650×** | -4.0 | 0.003 | 10/30 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -3.9 | 0.003 | 13/36 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -3.8 | 0.005 | 16/36 (H4, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.718×** | -3.1 | 0.081 | 5/36 (NCI-H1573, HS-578T, …) | rises with dose | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.718×** | -3.0 | 0.081 | 6/36 (SNU-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.40 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0976× (z -13.8) |
| [[A-172 (line)]] | wt | 6.34 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0401× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0743× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 3.75 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -13.2) |
| [[PANC-1 (line)]] | alt | 5.06 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.178× (z -8.6) |
| [[SHP-77 (line)]] | alt | 3.69 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0321× (z -10.7) |
| [[SNU-423 (line)]] | alt | 5.70 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0414× (z -11.6) |
| [[SW480 (line)]] | alt | 2.07 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0473× (z -11.6) |
| [[A498 (line)]] | wt | 3.46 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0754× (z -10.0) |
| [[HS-578T (line)]] | alt | 5.52 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0775× (z -9.1) |
| [[SNU-1 (line)]] | wt | 9.20 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0737× (z -8.8) |
| [[A-427 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.265 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P4-STRA6LP]] | +0.95 | +0.92 / +0.91 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SUGT1P4-STRA6LP-CCDC180]] | +0.85 | +0.78 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MRPS31P4]] | +0.78 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[LINC00888]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ELP1]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CCDC180]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 | ⚠ same locus (11.5 kb, same strand: neighbours can correlate without regulation) |
| [[BBS5]] | +0.65 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.64 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[POT1]] | +0.63 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[IFT172]] | +0.63 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[PRPF39]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNF18]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.61 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIATNB]] | -0.62 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RFX3]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | -0.61 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[BANP]] | -0.59 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[MCF2]] | -0.59 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.58 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[IGF2BP3]] | -0.58 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[UBE2R2-AS1]] | -0.57 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ZNF407]] | -0.57 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ASXL2]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[MED13]] | -0.56 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CIBAR1-DT]] | -0.55 | -0.24 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF4]] | B | RASSF4 activity raises STRA6LP's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without RASSF4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises STRA6LP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZSCAN23]] | B | ZSCAN23 activity raises STRA6LP's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without ZSCAN23 | 0.050 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[NQO1]] | B | NQO1 activity lowers STRA6LP's level | lines that do not express NQO1 (5) vs lines expressing it (45) | 1.67× higher at baseline in the lines without NQO1 | 0.098 | ⚠ within organs, on part of the lines |
| [[CCDC180]] | C | CCDC180 activity raises STRA6LP's level | lines that do not express CCDC180 (8) vs lines expressing it (42) | 3.43× lower at baseline in the lines without CCDC180 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: STRA6LP; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS1]] | B | STRA6LP, [[SUGT1P4-STRA6LP]] activity lowers PAPSS1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP (9) vs lines expressing them (41) | 1.32× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP | 0.027 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[CNEP1R1]] | B | STRA6LP, [[SUGT1P4-STRA6LP]], [[SUGT1P4-STRA6LP-CCDC180]] activity lowers CNEP1R1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.19× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[RASSF4]] | B | STRA6LP activity raises RASSF4's level | lines that do not express STRA6LP (9) vs lines expressing it (41) | 1.94× lower at baseline in the lines without STRA6LP | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CCDC180 |
| [[EIF2B4]] | B | STRA6LP activity lowers EIF2B4's level | lines that do not express STRA6LP (9) vs lines expressing it (41) | 1.15× higher at baseline in the lines without STRA6LP | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CCDC180 |
| [[LYPLA2]] | B | STRA6LP, [[SUGT1P4-STRA6LP]], [[SUGT1P4-STRA6LP-CCDC180]] activity lowers LYPLA2's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.15× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[CCDC180]] | C | STRA6LP, [[SUGT1P4-STRA6LP]], [[SUGT1P4-STRA6LP-CCDC180]] activity raises CCDC180's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 5.07× lower at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent with the target; co-absent genes |
| [[SUGT1P4-STRA6LP]] | C | STRA6LP's natural level strengthens SUGT1P4-STRA6LP's drug response | STRA6LP's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.26; direction not clear | 0.087 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.4, -4.3); signed map (-25.8, -14.5). **Vector** length 56.0, 8.55% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +2.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.8 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | STRA6 like, pseudogene |
| Locus type | pseudogene |
| Location | 9q22.33 — chr9:97,276,569-97,295,765 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [112272565](https://www.ncbi.nlm.nih.gov/gene/112272565):

> Predicted to act upstream of or within retinol transport and vitamin A import into cell. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53830) · Entrez [112272565](https://www.ncbi.nlm.nih.gov/gene/112272565) · Ensembl [ENSG00000254633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254633)

## Data

Gene col 14886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14886); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14886]; `tensor/DDL_lfc|DDL_z.npy` [14886]; `embed/gene_vectors.npy` [14886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14886 or target_col == 14886). Every well: [[STRA6LP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRA6LP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
