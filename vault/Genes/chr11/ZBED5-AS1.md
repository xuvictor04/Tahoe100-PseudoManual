---
symbol: "ZBED5-AS1"
type: "gene"
col: 14490
ensembl_id: "ENSG00000247271"
name: "ZBED5 antisense RNA 1"
location: "11p15.4"
module: 10
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZBED5-AS1

*ZBED5 antisense RNA 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.88× (z +18.3, q 0e+00, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.551× (z -5.7, q 7e-06, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHI1-DT]] (+0.78, fdr 7e-06), [[TMEM202-AS1]] (+0.75, fdr 7e-06), [[USP38-DT]] (+0.74, fdr 1e-05); moves opposite to [[PBX4]] (-0.64, fdr 6e-05), [[ACAP2]] (-0.61, fdr 7e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.88×** | +18.3 | 0e+00 | 31/33 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.66×** | +12.4 | 1e-32 | 14/17 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.52×** | +11.1 | 2e-26 | 5/5 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +11.0 | 5e-26 | 3/3 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.17×** | +10.4 | 2e-23 | 25/44 (SW480, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +6.7 | 2e-09 | 12/33 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.94×** | +6.3 | 2e-08 | 24/45 (A-172, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.6 | 1e-06 | 11/45 (A-172, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +5.5 | 2e-06 | 13/29 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +5.2 | 1e-05 | 12/41 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.1 | 2e-05 | 7/18 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.0 | 2e-05 | 6/17 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.0 | 3e-05 | 9/34 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.8 | 7e-05 | 14/35 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.1 | 0.002 | 8/42 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.007 | 3/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.007 | 9/43 (HCT15, A-172, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.008 | 3/14 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.011 | 3/39 (LS 180, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.019 | 8/39 (NCI-H23, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.551×** | -5.7 | 7e-06 | 20/44 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -5.2 | 6e-05 | 17/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -4.4 | 0.002 | 11/26 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -4.1 | 0.006 | 15/38 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.746×** | -4.0 | 0.009 | 9/45 (LOX-IMVI, A-172, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -3.7 | 0.021 | 13/44 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -3.6 | 0.029 | 16/41 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.710×** | -3.3 | 0.078 | 12/44 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.722× | -3.1 | 0.12 | 8/42 (HCT15, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.27 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +9.8) | [[Bortezomib (drug)]] 0.05 µM 0.121× (z -10.0) |
| [[A-427 (line)]] | wt | 3.55 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0584× (z -9.9) |
| [[A498 (line)]] | wt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +8.5) | — |
| [[A549 (line)]] | wt | 4.24 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0857× (z -8.7) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 6.06 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.05 µM 0.0761× (z -8.8) |
| [[SW480 (line)]] | alt | 4.39 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.142× (z -9.1) |
| [[A-172 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1-DT]] | +0.78 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.75 | +0.71 / +0.64 | both halves | 7e-06 | same gene group |
| [[USP38-DT]] | +0.74 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[TAF9B]] | +0.73 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.73 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.72 | +0.75 / +0.41 | both halves | 4e-05 | same gene group |
| [[PCNX4-DT]] | +0.72 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.71 | +0.72 / +0.44 | both halves | 3e-05 | same gene group |
| [[RAP2C-AS1]] | +0.71 | +0.75 / +0.50 | both halves | 1e-05 | same gene group |
| [[KRBA2]] | +0.71 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[LINC00240]] | +0.71 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.70 | +0.66 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX4]] | -0.64 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[ACAP2]] | -0.61 | -0.44 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZBED5-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ZBED5-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.6, 17.3); signed map (28.7, -10.8). **Vector** length 53.6, 7.26% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +6.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +4.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ZBED5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.4 — chr11:10,858,179-10,908,972 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48646) · Entrez [729013](https://www.ncbi.nlm.nih.gov/gene/729013) · Ensembl [ENSG00000247271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247271)

## Data

Gene col 14490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14490); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14490]; `tensor/DDL_lfc|DDL_z.npy` [14490]; `embed/gene_vectors.npy` [14490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14490 or target_col == 14490). Every well: [[ZBED5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
