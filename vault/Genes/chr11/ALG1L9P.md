---
symbol: "ALG1L9P"
type: "gene"
col: 14560
ensembl_id: "ENSG00000248671"
name: "ALG1 like 9, pseudogene"
location: "11q13.4"
module: 26
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ALG1L9P

*ALG1 like 9, pseudogene* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.27× (z +27.0, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.447× (z -8.3, q 4e-14, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.83, fdr 7e-06), [[MYLK4]] (+0.78, fdr 7e-06), [[XNDC1N-ZNF705EP-ALG1L9P]] (+0.77, fdr 7e-06, ⚠ same locus), [[ERICH2-DT]] (+0.75, fdr 1e-05); moves opposite to [[COMMD2]] (-0.66, fdr 3e-05), [[SLC25A11]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.27×** | +27.0 | 0e+00 | 35/35 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +10.9 | 4e-25 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.65×** | +10.1 | 6e-22 | 28/43 (LoVo, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +10.1 | 1e-21 | 27/33 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +9.1 | 1e-17 | 3/8 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +8.6 | 6e-16 | 24/37 (HT-29, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.6 | 6e-16 | 19/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.2 | 2e-14 | 11/19 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.007 | 10/39 (NCI-H23, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.007 | 8/45 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.40×** | +3.5 | 0.021 | 9/43 (A-172, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.035 | 5/43 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.036 | 6/47 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.061 | 3/47 (A-172, KATO III, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.061 | 5/46 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.447×** | -8.3 | 4e-14 | 24/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.454×** | -8.2 | 9e-14 | 27/47 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.510×** | -7.0 | 7e-10 | 17/33 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.646×** | -4.3 | 0.002 | 12/42 (SW480, COLO 205, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.659×** | -4.3 | 0.002 | 13/46 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.631×** | -4.0 | 0.005 | 13/43 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.701×** | -3.7 | 0.019 | 16/45 (SW480, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.702×** | -3.6 | 0.019 | 15/44 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -3.6 | 0.021 | 13/45 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.040 | 9/47 (SNU-423, C32, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.537×** | -3.4 | 0.040 | 10/41 (SW480, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -3.1 | 0.087 | 9/33 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.1 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0754× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.9) |
| [[COLO 205 (line)]] | alt | 15.9 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -15.2) |
| [[A-172 (line)]] | wt | 3.73 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +9.0) | [[Auranofin (drug)]] 0.5 µM 0.0682× (z -9.2) |
| [[A498 (line)]] | wt | 4.20 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +8.6) | [[Silodosin (drug)]] 5 µM 0.0600× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 7.67 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 9.95 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.103× (z -10.7) |
| [[SW1417 (line)]] | alt | 4.07 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +9.8) | [[Pentoxifylline (drug)]] 0.5 µM 0.0800× (z -8.6) |
| [[A549 (line)]] | wt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.64× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 5.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 3.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +8.7) | — |
| [[KATO III (line)]] | alt | 4.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0883× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 4.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 1.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.91× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 5.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +9.9) | — |
| [[A-427 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.83 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[MYLK4]] | +0.78 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.77 | +0.75 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[ERICH2-DT]] | +0.75 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[MAMDC2-AS1]] | +0.75 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.74 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[LIX1-AS1]] | +0.74 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.74 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[CDNF]] | +0.73 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[SAXO1]] | +0.73 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.73 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ALOX12-AS1]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[DRAIC]] | +0.72 | +0.66 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.66 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SLC25A11]] | -0.62 | -0.51 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALG1L9P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSCAML1]] | B | DSCAML1 activity raises ALG1L9P's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.50× lower at baseline in the lines without DSCAML1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[MAP2K1]] | B | MAP2K1 activity lowers ALG1L9P's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TSBP1-AS1]] | B | TSBP1-AS1 activity raises ALG1L9P's level | lines that do not express TSBP1-AS1 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without TSBP1-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000288993; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.813). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.4, 18.9); signed map (25.7, -3.0). **Vector** length 69.0, 11.2% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +27.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +8.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ALG1 like 9, pseudogene |
| Locus type | pseudogene |
| Location | 11q13.4 — chr11:71,800,541-71,804,640 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44378) · Entrez [285407](https://www.ncbi.nlm.nih.gov/gene/285407) · Ensembl [ENSG00000248671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248671)

## Data

Gene col 14560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14560); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14560]; `tensor/DDL_lfc|DDL_z.npy` [14560]; `embed/gene_vectors.npy` [14560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14560 or target_col == 14560). Every well: [[ALG1L9P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG1L9P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
