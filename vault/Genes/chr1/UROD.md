---
symbol: "UROD"
type: "gene"
col: 4714
ensembl_id: "ENSG00000126088"
name: "uroporphyrinogen decarboxylase"
location: "1p34.1"
module: 7
arm: "+"
pooled_cpm: 11.11
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# UROD

*uroporphyrinogen decarboxylase* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.48× (z +16.5, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.574× (z -7.4, q 8e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK2B]] (+0.66, fdr 7e-06), [[OTUB1]] (+0.65, fdr 3e-05), [[CSNK1G1]] (+0.63, fdr 2e-04); moves opposite to [[ABCD3]] (-0.50, fdr 1e-03, ⚠ not reproduced), [[ZNF544]] (-0.50, fdr 1e-04), [[GIPC1]] (-0.49, fdr 8e-05), [[KCTD20]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +16.5 | 0e+00 | 44/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +11.6 | 2e-28 | 32/34 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.46×** | +11.2 | 1e-26 | 18/20 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +8.7 | 5e-16 | 38/47 (A-172, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +7.0 | 2e-10 | 29/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.8 | 1e-09 | 33/48 (A-172, HS-578T, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +6.8 | 1e-09 | 33/44 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +6.3 | 3e-08 | 21/26 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.2 | 3e-08 | 31/44 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +4.7 | 2e-04 | 25/43 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.012 | 16/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.574×** | -7.4 | 8e-11 | 40/48 (HS-578T, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -5.1 | 8e-05 | 30/48 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.584×** | -5.1 | 8e-05 | 25/45 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.608×** | -4.7 | 4e-04 | 24/46 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -4.6 | 4e-04 | 27/46 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -4.6 | 4e-04 | 23/44 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -4.5 | 6e-04 | 21/41 (SW480, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -4.2 | 0.002 | 27/46 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -3.4 | 0.037 | 12/43 (HS-578T, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.716×** | -3.2 | 0.090 | 16/46 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.6) | — |
| [[A549 (line)]] | wt | 5.09 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +12.0) | [[Valdecoxib (drug)]] 0.05 µM 0.0806× (z -9.9) |
| [[HS-578T (line)]] | alt | 19.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +12.0) | [[Tucidinostat (drug)]] 5 µM 0.340× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 8.18 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 9.03 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 2 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0680× (z -13.1) |
| [[SW480 (line)]] | alt | 14.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +14.2) | — |
| [[A-172 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +10.8) | — |
| [[C32 (line)]] | wt | 8.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 7.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.5) | — |
| [[J82 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.9) | — |
| [[KATO III (line)]] | alt | 7.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 9.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.158× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 8.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 8.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +10.2) | — |
| [[A-427 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK2B]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[OTUB1]] | +0.65 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[CSNK1G1]] | +0.63 | +0.29 / +0.64 | both halves | 2e-04 |  |
| [[CDIPT]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GET3]] | +0.61 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[ZUP1]] | +0.59 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[APH1A]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[EAF1]] | +0.57 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[WDFY3]] | +0.56 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[NCOA2]] | +0.55 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[TRAPPC2L]] | +0.55 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[PGAP4]] | +0.55 | +0.35 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCD3]] | -0.50 | -0.18 / -0.49 | ⚠ not reproduced | 1e-03 |  |
| [[ZNF544]] | -0.50 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[GIPC1]] | -0.49 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[KCTD20]] | -0.49 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[THOC2]] | -0.49 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[DHRS2]] | -0.48 | -0.05 / -0.44 | ⚠ not reproduced | 0.005 |  |
| [[SYP]] | -0.48 | -0.32 / -0.38 | both halves | 1e-04 |  |
| [[PCNX2]] | -0.47 | -0.07 / -0.57 | ⚠ one half (not replicated) | 0.004 |  |
| [[TMEM170B]] | -0.46 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ADRA1B]] | -0.46 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[SPTSSA]] | -0.46 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[SLC23A2]] | -0.46 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.45 | -0.27 / -0.32 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UROD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.296). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-17.1, -17.1); signed map (-9.7, -22.2). **Vector** length 69.7, 14.1% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +16.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.0 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | uroporphyrinogen decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,010,950-45,015,575 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_UP, HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P06132](https://www.uniprot.org/uniprotkb/P06132) (Uroporphyrinogen decarboxylase):

> Catalyzes the sequential decarboxylation of the four acetate side chains of uroporphyrinogen to form coproporphyrinogen and participates in the fifth step in the heme biosynthetic pathway. Isomer I or isomer III of uroporphyrinogen may serve as substrate, but only coproporphyrinogen III can ultimately be converted to heme. In vitro also decarboxylates pentacarboxylate porphyrinogen I.

**Summary**, from NCBI Gene [7389](https://www.ncbi.nlm.nih.gov/gene/7389):

> This gene encodes an enzyme in the heme biosynthetic pathway. This enzyme is responsible for catalyzing the conversion of uroporphyrinogen to coproporphyrinogen through the removal of four carboxymethyl side chains. Mutations and deficiency in this enzyme are known to cause familial porphyria cutanea tarda and hepatoerythropoetic porphyria.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:12591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12591) · Entrez [7389](https://www.ncbi.nlm.nih.gov/gene/7389) · UniProt [P06132](https://www.uniprot.org/uniprotkb/P06132) · Ensembl [ENSG00000126088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126088)

## Data

Gene col 4714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4714); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4714]; `tensor/DDL_lfc|DDL_z.npy` [4714]; `embed/gene_vectors.npy` [4714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4714 or target_col == 4714). Every well: [[UROD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UROD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
