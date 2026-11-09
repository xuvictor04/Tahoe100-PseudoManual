---
symbol: "C5orf15"
type: "gene"
col: 3477
ensembl_id: "ENSG00000113583"
name: "chromosome 5 open reading frame 15"
location: "5q31.1"
module: 46
arm: "+"
pooled_cpm: 49.66
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# C5orf15

*chromosome 5 open reading frame 15* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.24× (z +11.4, q 3e-27, up in 33 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +7.0, q 8e-10, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.488× (z -11.1, q 6e-26, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERAP1]] (+0.72, fdr 7e-06), [[MOV10]] (+0.70, fdr 1e-05), [[TAPBP]] (+0.69, fdr 1e-05); moves opposite to [[CCDC112]] (-0.65, fdr 1e-05), [[ASL]] (-0.64, fdr 2e-05), [[TECPR1]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MBNL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +11.4 | 3e-27 | 33/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.0 | 8e-10 | 29/48 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.9 | 8e-10 | 35/48 (HEC-1-A, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +4.9 | 1e-04 | 28/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.8 | 2e-04 | 28/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.018 | 23/48 (HS-578T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.030 | 19/47 (AsPC-1, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.032 | 18/48 (HOP62, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.064 | 19/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.2 | 0.076 | 14/48 (Hs 766T, A-427, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.15× | +3.1 | 0.12 | 6/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -11.1 | 6e-26 | 46/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.516×** | -10.2 | 4e-22 | 46/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.538×** | -9.6 | 1e-19 | 47/48 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.592×** | -8.1 | 7e-14 | 42/48 (SW480, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.662×** | -6.4 | 2e-08 | 35/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -6.0 | 1e-07 | 36/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.734×** | -4.8 | 1e-04 | 30/48 (A-172, CHP-212, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.751×** | -4.4 | 6e-04 | 27/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.033 | 21/48 (H4, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.084 | 15/47 (BT-474, A-427, …) | rises with dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.820× | -3.1 | 0.10 | 14/48 (SW 1271, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 82.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -12.5) |
| [[A498 (line)]] | wt | 78.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -10.9) |
| [[H4 (line)]] | wt | 77.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 73.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -11.8) |
| [[A-172 (line)]] | wt | 91.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -10.6) |
| [[A-427 (line)]] | wt | 49.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 37.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -10.1) |
| [[A549 (line)]] | wt | 49.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 60.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.444× (z -8.9) |
| [[HOP62 (line)]] | alt | 44.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 62.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -9.1) |
| [[HS-578T (line)]] | alt | 51.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 65.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +12.7) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.117× (z -9.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 43.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERAP1]] | +0.72 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MOV10]] | +0.70 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TAPBP]] | +0.69 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HLA-H]] | +0.68 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[SUMO3]] | +0.66 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[HFE]] | +0.65 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[FOXJ2]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | +0.64 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[USF1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DECR1]] | +0.64 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[LINC00938]] | +0.64 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[CTSO]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC112]] | -0.65 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ASL]] | -0.64 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TECPR1]] | -0.63 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TOX2]] | -0.62 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TOMM20]] | -0.62 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SPATA2L]] | -0.61 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PWWP3A]] | -0.61 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[GIPR]] | -0.61 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ACAP2]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LRRFIP1]] | -0.60 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[TMEM41B]] | -0.60 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SPIRE1]] | -0.59 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBNL3]] | B | MBNL3 activity lowers C5orf15's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.22× higher at baseline in the lines without MBNL3 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[LPAR3]] | B | LPAR3 activity raises C5orf15's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.10× lower at baseline in the lines without LPAR3 | 0.058 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[MDK]] | B | MDK activity lowers C5orf15's level | lines that do not express MDK (14) vs lines expressing it (36) | 1.36× higher at baseline in the lines without MDK | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers C5orf15's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises C5orf15's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises C5orf15's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (18.5, 3.9); signed map (24.7, -20.5). **Vector** length 119, 32.0% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.3 | +6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -8.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.0 | -11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -10.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 5 open reading frame 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:133,955,510-133,968,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCT2, HTGN29 |
| Matched by | ensembl_id |

UniProt [Q8NC54](https://www.uniprot.org/uniprotkb/Q8NC54) carries no function annotation.

**Summary**, from NCBI Gene [56951](https://www.ncbi.nlm.nih.gov/gene/56951):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20656) · Entrez [56951](https://www.ncbi.nlm.nih.gov/gene/56951) · UniProt [Q8NC54](https://www.uniprot.org/uniprotkb/Q8NC54) · Ensembl [ENSG00000113583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113583)

## Data

Gene col 3477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3477); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3477]; `tensor/DDL_lfc|DDL_z.npy` [3477]; `embed/gene_vectors.npy` [3477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3477 or target_col == 3477). Every well: [[C5orf15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5orf15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
