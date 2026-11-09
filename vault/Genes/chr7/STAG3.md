---
symbol: "STAG3"
type: "gene"
col: 842
ensembl_id: "ENSG00000066923"
name: "STAG3 cohesin complex component"
location: "7q22.1"
module: 87
arm: "+"
pooled_cpm: 5.12
n_lines_expressing: 36
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# STAG3

*STAG3 cohesin complex component* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +19.3, q 0e+00, up in 15 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.637× (z -5.7, q 7e-06, down in 8 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.0743×, C32 0.310×); [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.217×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.234×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.272×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFR3B]] (+0.66, fdr 7e-06), [[LOXL3]] (+0.62, fdr 1e-05), [[C10orf90]] (+0.61, fdr 1e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[SNX32]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +19.3 | 0e+00 | 15/24 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.50×** | +15.8 | 0e+00 | 4/9 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +12.9 | 1e-35 | 2/5 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +10.7 | 9e-25 | 10/23 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +8.9 | 4e-17 | 10/33 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +7.9 | 2e-13 | 12/31 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.8 | 7e-13 | 7/31 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +6.4 | 2e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.8 | 3e-07 | 3/11 (RPMI-7951, A498, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +5.5 | 3e-06 | 1/12 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.52×** | +5.3 | 6e-06 | 2/17 (SW480, NCI-H23) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.5 | 4e-04 | 8/26 (NCI-H23, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.4 | 4e-04 | 1/23 (SW480) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 4e-04 | 1/24 (NCI-H2347) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 1/31 (HEC-1-A) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.002 | 3/18 (NCI-H2347, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.024 | 2/27 (NCI-H2030, C-33 A) | inconsistent across doses |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.031 | 3/24 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Flutamide (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.031 | 3/24 (SNU-1, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.037 | 2/25 (SNU-423, SW480) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.063 | 4/24 (NCI-H2347, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 842.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.0743×, C32 0.310×); [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.217×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.234×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.272×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -5.7 | 7e-06 | 8/29 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.765× | -3.4 | 0.20 | 5/33 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.764× | -3.3 | 0.20 | 7/25 (LoVo, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.788× | -3.0 | 0.36 | 7/31 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 74.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0743× (z -20.6) |
| [[A498 (line)]] | wt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +9.5) | — |
| [[C32 (line)]] | wt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 1.80 | 0 | 1 | — | [[Methyl aminolevulinate (hydrochloride) (drug)]] 5 µM 0.0338× (z -9.5) |
| [[A-172 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3B]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 | same gene group |
| [[LOXL3]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PPFIA3]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[LEF1-AS1]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RHOJ]] | +0.60 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[SOX10]] | +0.59 | +0.66 / +0.40 | both halves | 5e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[CPNE5]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TMEM39B]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[COL19A1]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MIR3681HG]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[TDRD9]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STAG3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX32]] | B | STAG3 activity raises SNX32's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without STAG3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[LEF1]] | B | STAG3 activity raises LEF1's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without STAG3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[PPFIA3]] | B | STAG3 activity raises PPFIA3's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.82× lower at baseline in the lines without STAG3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[RYR1]] | B | STAG3 activity raises RYR1's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.53× lower at baseline in the lines without STAG3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[TMEM139-AS1]] | B | STAG3 activity raises TMEM139-AS1's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without STAG3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[LOXL3]] | B | STAG3 activity raises LOXL3's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without STAG3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.9, 28.0); signed map (28.2, 39.6). **Vector** length 34.8, 4.51% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | STAG3 cohesin complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,177,563-100,214,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SA3 |
| Gene groups (HGNC) | Cohesin complex; Armadillo like helical domain containing; STAG family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ98](https://www.uniprot.org/uniprotkb/Q9UJ98) (Cohesin subunit SA-3):

> Meiosis specific component of cohesin complex. The cohesin complex is required for the cohesion of sister chromatids after DNA replication. The cohesin complex apparently forms a large proteinaceous ring within which sister chromatids can be trapped. At anaphase, the complex is cleaved and dissociates from chromatin, allowing sister chromatids to segregate. The meiosis-specific cohesin complex probably replaces mitosis specific cohesin complex when it dissociates from chromatin during prophase …

**Summary**, from NCBI Gene [10734](https://www.ncbi.nlm.nih.gov/gene/10734):

> The protein encoded by this gene is expressed in the nucleus and is a subunit of the cohesin complex which regulates the cohesion of sister chromatids during cell division. A mutation in this gene is associated with premature ovarian failure. Alternate splicing results in multiple transcript variants encoding distinct isoforms. This gene has multiple pseudogenes. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:11356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11356) · Entrez [10734](https://www.ncbi.nlm.nih.gov/gene/10734) · UniProt [Q9UJ98](https://www.uniprot.org/uniprotkb/Q9UJ98) · Ensembl [ENSG00000066923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066923)

## Data

Gene col 842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 842); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 842]; `tensor/DDL_lfc|DDL_z.npy` [842]; `embed/gene_vectors.npy` [842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 842 or target_col == 842). Every well: [[STAG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
