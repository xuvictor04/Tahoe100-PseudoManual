---
symbol: "TRPC6"
type: "gene"
col: 6045
ensembl_id: "ENSG00000137672"
name: "transient receptor potential cation channel subfamily C member 6"
location: "11q22.1"
module: 140
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 36
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# TRPC6

*transient receptor potential cation channel subfamily C member 6* — 11q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.19× (z +26.0, q 0e+00, up in 14 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.161×, A549 0.125×); [[Belinostat (drug)]] 0.5 µM in 1 line (A549 0.0647×; ⚠ cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (A549 0.0660×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0817×).
> Its strongest partners by |cos| (72 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABRG3]] (+0.52, fdr 2e-04), [[AADACL2-AS1]] (+0.51, fdr 8e-05), [[LINC00922]] (+0.50, fdr 4e-04); moves opposite to [[ZNF639]] (-0.44, fdr 1e-04), [[PIP4P1]] (-0.41, fdr 5e-04), [[KAT7]] (-0.40, fdr 4e-04).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZBTB7B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.19×** | +26.0 | 0e+00 | 14/18 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.99×** | +12.9 | 2e-35 | 16/24 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +12.4 | 5e-33 | 2/9 (AsPC-1, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +11.8 | 4e-30 | 9/20 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +10.0 | 1e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.6 | 3e-12 | 11/25 (RPMI-7951, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +6.4 | 1e-08 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +6.3 | 2e-08 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +6.2 | 3e-08 | 3/14 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +6.0 | 1e-07 | 4/20 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.3 | 7e-06 | 3/28 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 1/26 (AsPC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.5 | 4e-04 | 0/6 | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.84×** | +4.0 | 0.002 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.007 | 2/20 (KATO III, SW1417) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.010 | 5/21 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.053 | 1/13 (NCI-H2347) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +2.9 | 0.098 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6045.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.161×, A549 0.125×); [[Belinostat (drug)]] 0.5 µM in 1 line (A549 0.0647×; ⚠ cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (A549 0.0660×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0817×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Relugolix (drug)]] 0.5 µM |  | 0.705× | -3.3 | 0.59 | 2/26 (COLO 205, C32) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.720× | -3.1 | 0.59 | 3/26 (COLO 205, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 9.91 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +11.3) | — |
| [[KATO III (line)]] | alt | 1.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.8× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 8.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0817× (z -8.5) |
| [[A-172 (line)]] | wt | 0.870 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.864 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.892 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.912 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.794 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 24 of them with an alert (⚠; 24 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABRG3]] | +0.52 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[AADACL2-AS1]] | +0.51 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[LINC00922]] | +0.50 | +0.26 / +0.50 | both halves | 4e-04 |  |
| [[PROSER2-AS1]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[FILIP1]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[FAM107B]] | +0.49 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[SORCS3]] | +0.48 | +0.17 / +0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLC35F4]] | +0.48 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[RBFOX1]] | +0.47 | +0.28 / +0.46 | both halves | 3e-04 | same gene group |
| [[GRHL3]] | +0.47 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[C12orf40]] | +0.46 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[AQP4-AS1]] | +0.45 | +0.24 / +0.52 | both halves | 4e-04 |  |
| [[IGF2BP2-AS1]] | +0.45 | +0.27 / +0.39 | both halves | 3e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF639]] | -0.44 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PIP4P1]] | -0.41 | -0.24 / -0.33 | both halves | 5e-04 |  |
| [[KAT7]] | -0.40 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[EP400]] | -0.40 | -0.30 / -0.27 | both halves | 3e-04 |  |
| [[PROSER1]] | -0.40 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[PPA2]] | -0.40 | -0.24 / -0.35 | both halves | 4e-04 |  |
| [[TMEM135]] | -0.39 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[BLTP3A]] | -0.39 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[RAD23A]] | -0.38 | -0.08 / -0.34 | ⚠ not reproduced | 0.003 |  |
| [[DNAJC16]] | -0.38 | -0.14 / -0.32 | ⚠ not reproduced | 0.002 |  |
| [[ZNF782]] | -0.38 | -0.08 / -0.29 | ⚠ not reproduced | 0.003 |  |
| [[ZBTB7B]] | -0.38 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[XPOT]] | -0.37 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[BOD1]] | -0.37 | -0.32 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRPC6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MGLL]] | B | MGLL activity raises TRPC6's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without MGLL | 0.079 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBTB7B]] | B | TRPC6 activity raises ZBTB7B's level | lines that do not express TRPC6 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without TRPC6 | 0.057 | ⚠ within organs, on part of the lines; also absent: UNC80, ARHGAP30, ENSG00000236283; maybe low, not absent |
| [[KDM4A-AS1]] | B | TRPC6 activity lowers KDM4A-AS1's level | lines that do not express TRPC6 (14) vs lines expressing it (36) | 1.31× higher at baseline in the lines without TRPC6 | 0.060 | ⚠ within organs, on part of the lines; also absent: UNC80, ARHGAP30, ENSG00000236283; maybe low, not absent |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.4, 27.6); signed map (32.8, 9.6). **Vector** length 25.7, 2.94% of its response variance represented; |z| ≥ 3 in 580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +26.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.5 | +0.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily C member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.1 — chr11:101,451,564-101,872,562 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRP6; previously FSGS2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; MicroRNA protein coding host genes; Transient receptor potential cation channel subfamily C |
| Reactome | 17 pathways, smallest: Role of second messengers in netrin-1 signaling; Elevation of cytosolic Ca2+ levels; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y210](https://www.uniprot.org/uniprotkb/Q9Y210) (Short transient receptor potential channel 6):

> Non-selective, calcium-permeable cation channel. Mediates calcium entry following G(q)-coupled receptor or receptor tyrosine kinase activation, which triggers phospholipase C (PLC)-mediated hydrolysis of phosphatidylinositides and production of diacylglycerol (DAG) that directly activates TRPC6. Does not appear to be activated by depletion of intracellular calcium stores. Mediates depolarization of intrinsically photosensitive retinal ganglion cells (ipRGCs) in response to light-induced …

**Summary**, from NCBI Gene [7225](https://www.ncbi.nlm.nih.gov/gene/7225):

> The protein encoded by this gene forms a receptor-activated calcium channel in the cell membrane. The channel is activated by diacylglycerol and is thought to be under the control of a phosphatidylinositol second messenger system. Activation of this channel occurs independently of protein kinase C and is not triggered by low levels of intracellular calcium. Defects in this gene are a cause of focal segmental glomerulosclerosis 2 (FSGS2). [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:12338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12338) · Entrez [7225](https://www.ncbi.nlm.nih.gov/gene/7225) · UniProt [Q9Y210](https://www.uniprot.org/uniprotkb/Q9Y210) · Ensembl [ENSG00000137672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137672)

## Data

Gene col 6045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6045); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6045]; `tensor/DDL_lfc|DDL_z.npy` [6045]; `embed/gene_vectors.npy` [6045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6045 or target_col == 6045). Every well: [[TRPC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
