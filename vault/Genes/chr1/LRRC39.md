---
symbol: "LRRC39"
type: "gene"
col: 4339
ensembl_id: "ENSG00000122477"
name: "leucine rich repeat containing 39"
location: "1p21.2"
module: 39
arm: "+"
pooled_cpm: 4.89
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# LRRC39

*leucine rich repeat containing 39* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.98× (z +9.7, q 1e-19, up in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.21× (z +8.0, q 3e-13, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.500× (z -7.0, q 2e-09, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.556× (z -5.9, q 6e-07, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKDD1B]] (+0.74, fdr 7e-06), [[SLC6A13]] (+0.73, fdr 7e-06), [[GCNA]] (+0.70, fdr 7e-06); moves opposite to [[POLD2]] (-0.62, fdr 1e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.98×** | +9.7 | 1e-19 | 33/46 (HS-578T, A498, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +8.0 | 3e-13 | 32/47 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.9 | 5e-07 | 16/38 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.8 | 8e-07 | 21/42 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.7 | 1e-06 | 3/8 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +5.6 | 2e-06 | 20/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.2 | 2e-05 | 16/36 (HT-29, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.9 | 6e-05 | 13/48 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.13×** | +4.0 | 0.004 | 8/45 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.42×** | +3.6 | 0.022 | 10/44 (LS 180, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.029 | 11/47 (CFPAC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.029 | 10/47 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.041 | 7/46 (HT-29, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.057 | 4/47 (A498, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.074 | 11/39 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.089 | 5/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.099 | 2/42 (LoVo, COLO 205) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.500×** | -7.0 | 2e-09 | 27/47 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -6.9 | 2e-09 | 25/41 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -5.9 | 6e-07 | 25/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.564×** | -5.8 | 1e-06 | 23/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.406×** | -4.8 | 2e-04 | 19/44 (RPMI-7951, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.633×** | -4.6 | 4e-04 | 18/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -3.9 | 0.009 | 16/41 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.689×** | -3.6 | 0.021 | 12/46 (HOP62, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.705×** | -3.5 | 0.027 | 12/45 (H4, HepG2/C3A, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.559× | -3.1 | 0.12 | 10/36 (SW 900, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 9.36 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0950× (z -12.0) |
| [[LoVo (line)]] | wt | 5.41 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0698× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 5.71 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0627× (z -11.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 8.73 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.242× (z -8.8) |
| [[H4 (line)]] | wt | 5.54 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0475× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 3.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0708× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 4.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKDD1B]] | +0.74 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.73 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[GCNA]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[CDKL4]] | +0.70 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.70 | +0.77 / +0.57 | both halves | 9e-06 |  |
| [[CMYA5]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | STRING 485 |
| [[HSD17B3]] | +0.69 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[PDC-AS1]] | +0.69 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[GRK7]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.68 | +0.71 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD2]] | -0.62 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises LRRC39's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without FSIP2-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRRC39's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises LRRC39's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without ST8SIA5 | 0.028 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[LINC01917]] | B | LINC01917 activity raises LRRC39's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without LINC01917 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[ACOT12]] | B | ACOT12 activity raises LRRC39's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without ACOT12 | 0.083 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[TNNI3K]] | C | TNNI3K activity raises LRRC39's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without TNNI3K | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.0, -12.9); signed map (17.1, 6.7). **Vector** length 53.3, 6.70% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.3 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,148,448-100,178,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14816, myomasp |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DD0](https://www.uniprot.org/uniprotkb/Q96DD0) (Leucine-rich repeat-containing protein 39):

> Component of the sarcomeric M-band which plays a role in myocyte response to biomechanical stress. May regulate expression of other M-band proteins via an SRF-dependent pathway. Important for normal contractile function in heart.

**Summary**, from NCBI Gene [127495](https://www.ncbi.nlm.nih.gov/gene/127495):

> Predicted to be involved in intracellular signal transduction. Predicted to be located in M band. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28228) · Entrez [127495](https://www.ncbi.nlm.nih.gov/gene/127495) · UniProt [Q96DD0](https://www.uniprot.org/uniprotkb/Q96DD0) · Ensembl [ENSG00000122477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122477)

## Data

Gene col 4339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4339); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4339]; `tensor/DDL_lfc|DDL_z.npy` [4339]; `embed/gene_vectors.npy` [4339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4339 or target_col == 4339). Every well: [[LRRC39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
