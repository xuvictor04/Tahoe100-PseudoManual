---
symbol: "ATXN7L3-AS1"
type: "gene"
col: 15551
ensembl_id: "ENSG00000267394"
name: "ATXN7L3 antisense RNA 1"
location: "17q21.31"
module: 35
arm: "+"
pooled_cpm: 3.01
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ATXN7L3-AS1

*ATXN7L3 antisense RNA 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.91× (z +21.2, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.512× (z -7.4, q 9e-11, down in 21 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf54]] (+0.77, fdr 1e-05), [[MYLK4]] (+0.75, fdr 1e-05), [[MED28-DT]] (+0.72, fdr 7e-05); moves opposite to [[PPP1CC]] (-0.59, fdr 1e-04), [[HLTF]] (-0.59, fdr 3e-04), [[MRPS31P4]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HOOK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.91×** | +21.2 | 0e+00 | 30/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +8.2 | 8e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.8 | 2e-09 | 5/18 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +6.7 | 2e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.8 | 7e-07 | 11/28 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.6 | 2e-06 | 11/33 (COLO 205, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 6e-06 | 5/27 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.9 | 6e-05 | 11/44 (HEC-1-A, SW1417, …) | rises with dose | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 0.001 | 4/35 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 8/39 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.9 | 0.005 | 3/33 (A-427, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.8 | 0.006 | 3/22 (NCI-H2030, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.011 | 4/40 (A-427, A549, …) | inconsistent across doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.038 | 3/27 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.046 | 6/27 (SNU-423, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -7.4 | 9e-11 | 21/43 (Panc 03.27, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.576×** | -6.1 | 3e-07 | 18/44 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.576×** | -5.9 | 9e-07 | 15/40 (KATO III, SW 900, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.601×** | -5.6 | 3e-06 | 18/45 (NCI-H1573, COLO 205, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -5.3 | 1e-05 | 16/44 (Panc 03.27, LS 180, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -4.8 | 1e-04 | 18/44 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.449×** | -4.6 | 3e-04 | 10/38 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.659×** | -4.6 | 3e-04 | 12/38 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.696×** | -4.0 | 0.004 | 11/32 (LS 180, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.702×** | -3.9 | 0.005 | 14/41 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.712×** | -3.7 | 0.009 | 13/46 (CFPAC-1, A-427, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.734×** | -3.4 | 0.029 | 11/39 (LOX-IMVI, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 4.53 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0510× (z -10.5) |
| [[SW480 (line)]] | alt | 1.96 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +8.8) | [[Belinostat (drug)]] 0.5 µM 0.0948× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 6.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 3.35 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0696× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 9.33 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0233× (z -15.3) |
| [[A-172 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf54]] | +0.77 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.75 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MED28-DT]] | +0.72 | +0.38 / +0.72 | both halves | 7e-05 |  |
| [[SMG1-DT]] | +0.71 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.70 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[CCNO-DT]] | +0.70 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ZFHX2-AS1]] | +0.69 | +0.37 / +0.51 | both halves | 7e-05 | same gene group |
| [[SIAH2-AS1]] | +0.69 | +0.44 / +0.50 | both halves | 3e-05 | same gene group |
| [[NRL]] | +0.68 | +0.39 / +0.71 | both halves | 6e-05 |  |
| [[UBE2R2-AS1]] | +0.67 | +0.46 / +0.56 | both halves | 2e-05 | same gene group |
| [[ATXN1L]] | +0.67 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[PTPN23-DT]] | +0.67 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CC]] | -0.59 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[HLTF]] | -0.59 | -0.26 / -0.52 | both halves | 3e-04 |  |
| [[MRPS31P4]] | -0.57 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOOK1]] | B | HOOK1 activity raises ATXN7L3-AS1's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without HOOK1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[PCAT1]] | B | PCAT1 activity raises ATXN7L3-AS1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without PCAT1 | 0.024 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ATXN7L3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises ATXN7L3-AS1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 1.36× lower at baseline in the lines without SLC44A3-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[ACTR3C]] | B | ACTR3C activity raises ATXN7L3-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.38× lower at baseline in the lines without ACTR3C | 0.035 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[GXYLT2]] | B | GXYLT2 activity lowers ATXN7L3-AS1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 1.52× higher at baseline in the lines without GXYLT2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.8, 20.6); signed map (26.6, -3.0). **Vector** length 56.9, 7.88% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +21.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +0.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -5.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATXN7L3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:44,198,537-44,216,565 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55298) · Entrez [101926967](https://www.ncbi.nlm.nih.gov/gene/101926967) · Ensembl [ENSG00000267394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267394)

## Data

Gene col 15551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15551); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15551]; `tensor/DDL_lfc|DDL_z.npy` [15551]; `embed/gene_vectors.npy` [15551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15551 or target_col == 15551). Every well: [[ATXN7L3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN7L3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
