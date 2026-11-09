---
symbol: "MAP4K2"
type: "gene"
col: 9592
ensembl_id: "ENSG00000168067"
name: "mitogen-activated protein kinase kinase kinase kinase 2"
location: "11q13.1"
module: 30
arm: "+"
pooled_cpm: 8.5
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MAP4K2

*mitogen-activated protein kinase kinase kinase kinase 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.88× (z +16.4, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.591× (z -8.2, q 2e-13, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.69, fdr 1e-05), [[MFSD13A]] (+0.66, fdr 3e-05), [[AHDC1]] (+0.66, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.62, fdr 4e-05), [[WARS2-AS1]] (-0.62, fdr 5e-05), [[MMADHC-DT]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.88×** | +16.4 | 0e+00 | 38/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +15.8 | 0e+00 | 38/45 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +13.2 | 3e-37 | 34/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +9.2 | 3e-18 | 27/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +8.5 | 1e-15 | 27/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +7.6 | 3e-12 | 25/43 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.6 | 3e-09 | 7/15 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 7e-07 | 19/44 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.6 | 1e-06 | 15/45 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.0 | 3e-05 | 15/35 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +4.7 | 1e-04 | 10/45 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.4 | 6e-04 | 13/41 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 7/44 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 5/40 (RPMI-7951, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.002 | 7/45 (NCI-H460, SHP-77, …) | all doses, stronger at high dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.012 | 5/45 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.040 | 7/45 (MIA PaCa-2, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9592.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -8.2 | 2e-13 | 22/45 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.595×** | -8.0 | 2e-13 | 26/45 (SNU-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -6.2 | 9e-08 | 22/42 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.763×** | -5.9 | 4e-07 | 18/46 (SW1417, A-427, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -5.9 | 4e-07 | 19/41 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -5.4 | 5e-06 | 19/45 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.5 | 0.041 | 15/43 (SW1417, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.817× | -3.1 | 0.12 | 11/44 (HOP62, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 9.18 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -10.0) |
| [[A-427 (line)]] | wt | 24.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -10.5) |
| [[A549 (line)]] | wt | 4.25 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0788× (z -8.8) |
| [[BT-474 (line)]] | alt | 9.01 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0974× (z -8.5) |
| [[HS-578T (line)]] | alt | 9.11 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.147× (z -9.1) |
| [[J82 (line)]] | alt | 9.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -8.7) |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 6.32 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0693× (z -8.9) |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.208× (z -12.7) |
| [[SW48 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0736× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.69 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MFSD13A]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[AHDC1]] | +0.66 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.66 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.64 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[OSBPL7]] | +0.64 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ANO8]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.64 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[RNF187]] | +0.63 | +0.59 / +0.43 | both halves | 4e-05 |  |
| [[SNPH]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.62 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[FCHO1]] | +0.62 | +0.36 / +0.58 | both halves | 9e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.62 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[WARS2-AS1]] | -0.62 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[MMADHC-DT]] | -0.60 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.59 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[SON]] | -0.59 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CDK12]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[LINC00571]] | -0.58 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MED1]] | -0.58 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.58 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[ANKRD17-DT]] | -0.57 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[CREBBP]] | -0.57 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.56 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises MAP4K2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.62× lower at baseline in the lines without SEMA6B | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[PTK7]] | B | PTK7 activity raises MAP4K2's level | lines that do not express PTK7 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without PTK7 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000289985, ZNF433, ENSG00000269755 |
| [[TOP2B]] | B | TOP2B activity raises MAP4K2's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TSPAN33]] | B | TSPAN33 activity raises MAP4K2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.51× lower at baseline in the lines without TSPAN33 | 0.099 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[FAM102A]] | C | FAM102A activity lowers MAP4K2's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 2.22× higher at baseline in the lines without FAM102A | 0.071 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.4, -6.6); signed map (-33.4, -6.2). **Vector** length 71.9, 11.8% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,784,918-64,803,241 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCK, BL44; previously RAB8IP |
| Gene groups (HGNC) | MAP4K family (GCK-I subfamily) |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12851](https://www.uniprot.org/uniprotkb/Q12851) (Mitogen-activated protein kinase kinase kinase kinase 2):

> Serine/threonine-protein kinase which acts as an essential component of the MAP kinase signal transduction pathway. Acts as a MAPK kinase kinase kinase (MAP4K) and is an upstream activator of the stress-activated protein kinase/c-Jun N-terminal kinase (SAP/JNK) signaling pathway and to a lesser extent of the p38 MAPKs signaling pathway. Required for the efficient activation of JNKs by TRAF6-dependent stimuli, including pathogen-associated molecular patterns (PAMPs) such as …

**Summary**, from NCBI Gene [5871](https://www.ncbi.nlm.nih.gov/gene/5871):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. Although this kinase is found in many tissues, its expression in lymphoid follicles is restricted to the cells of germinal centre, where it may participate in B-cell differentiation. This kinase can be activated by TNF-alpha, and has been shown to specifically activate MAP kinases. This kinase is also found to interact with TNF receptor-associated factor 2 (TRAF2), which is involved in the activation of …

**Accessions** — [HGNC:6864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6864) · Entrez [5871](https://www.ncbi.nlm.nih.gov/gene/5871) · UniProt [Q12851](https://www.uniprot.org/uniprotkb/Q12851) · Ensembl [ENSG00000168067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168067)

## Data

Gene col 9592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9592); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9592]; `tensor/DDL_lfc|DDL_z.npy` [9592]; `embed/gene_vectors.npy` [9592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9592 or target_col == 9592). Every well: [[MAP4K2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP4K2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
