---
symbol: "MRTO4"
type: "gene"
col: 593
ensembl_id: "ENSG00000053372"
name: "MRT4 homolog, ribosome maturation factor"
location: "1p36.13"
module: 5
arm: "+"
pooled_cpm: 23.23
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 6
n_dd_up_clean: 31
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MRTO4

*MRT4 homolog, ribosome maturation factor* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.21× (z +8.5, q 1e-14, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.782× (z -3.8, q 0.050, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP16]] (+0.83, fdr 7e-06), [[DDX31]] (+0.82, fdr 7e-06), [[DHX37]] (+0.81, fdr 7e-06); moves opposite to [[MPC2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +8.5 | 1e-14 | 41/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.50×** | +8.4 | 1e-14 | 43/48 (NCI-H2030, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +7.9 | 6e-13 | 39/45 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.14×** | +7.9 | 6e-13 | 41/48 (PANC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +7.7 | 2e-12 | 33/47 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.73×** | +7.3 | 2e-11 | 33/46 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.98×** | +7.3 | 3e-11 | 41/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.96×** | +6.9 | 4e-10 | 32/43 (RPMI-7951, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.7 | 1e-09 | 32/47 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.85×** | +6.6 | 3e-09 | 36/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.83×** | +6.2 | 3e-08 | 32/48 (NCI-H1792, SNU-423, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.81×** | +6.1 | 6e-08 | 24/37 (Hs 766T, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +5.4 | 2e-06 | 33/47 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.58×** | +4.5 | 3e-04 | 26/43 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.22×** | +4.4 | 4e-04 | 30/45 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +4.3 | 5e-04 | 28/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.17×** | +4.3 | 6e-04 | 30/46 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.14×** | +4.2 | 8e-04 | 27/47 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.09×** | +4.1 | 0.001 | 28/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.005 | 20/47 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.008 | 20/47 (HOP62, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.050 | 17/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.704×** | -3.7 | 0.050 | 24/46 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.712×** | -3.6 | 0.050 | 19/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.788×** | -3.6 | 0.051 | 20/48 (A-427, SW480, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.716×** | -3.5 | 0.057 | 20/46 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.722×** | -3.4 | 0.060 | 20/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.755× | -3.0 | 0.17 | 20/47 (HOP62, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.738× | -3.0 | 0.17 | 15/47 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.82× (z +8.9) | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -9.3) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 9.42 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.152× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.06× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.73× (z +9.0) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.25× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 38.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.83× (z +8.6) | — |
| [[SW480 (line)]] | alt | 34.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.53× (z +9.4) | — |
| [[A-427 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP16]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 800 |
| [[DDX31]] | +0.82 | +0.80 / +0.79 | both halves | 7e-06 | STRING 549 |
| [[DHX37]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[NOP2]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 988 |
| [[TWNK]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[BYSL]] | +0.80 | +0.83 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 954 |
| [[SDAD1]] | +0.79 | +0.77 / +0.75 | both halves | 7e-06 | STRING 978 |
| [[RRS1]] | +0.79 | +0.82 / +0.76 | both halves | 7e-06 | same gene group; STRING 992 |
| [[UTP14A]] | +0.78 | +0.79 / +0.77 | both halves | 7e-06 | STRING 679 |
| [[GTPBP4]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 | STRING 999 |
| [[QTRT2]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[WDR4]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | STRING 800 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.62 | -0.63 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity strengthens MRTO4's drug response | lines that do not express ADD3 (5) vs lines expressing it (43) | the lines without ADD3 respond 0.81× as strongly (z diff +0.90); strongest at Homoharringtonine 0.5 µM: 1.05x vs 2.23x (z diff +3.9) | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MRTO4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WDTC1]] | C | WDTC1's natural level strengthens MRTO4's drug response | WDTC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.21; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.841). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.2, -36.6); signed map (-1.0, -46.3). **Vector** length 94.5, 27.4% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.66 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.66 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.68 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | MRT4 homolog, ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,251,805-19,260,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ657E11.4, MRT4; previously C1orf33 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKD2](https://www.uniprot.org/uniprotkb/Q9UKD2) (mRNA turnover protein 4 homolog):

> Component of the ribosome assembly machinery. Nuclear paralog of the ribosomal protein P0, it binds pre-60S subunits at an early stage of assembly in the nucleolus, and is replaced by P0 in cytoplasmic pre-60S subunits and mature 80S ribosomes.

**Summary**, from NCBI Gene [51154](https://www.ncbi.nlm.nih.gov/gene/51154):

> This gene encodes a protein sharing a low level of sequence similarity with ribosomal protein P0. While the precise function of the encoded protein is currently unknown, it appears to be involved in mRNA turnover and ribosome assembly. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18477) · Entrez [51154](https://www.ncbi.nlm.nih.gov/gene/51154) · UniProt [Q9UKD2](https://www.uniprot.org/uniprotkb/Q9UKD2) · Ensembl [ENSG00000053372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053372)

## Data

Gene col 593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 593); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 593]; `tensor/DDL_lfc|DDL_z.npy` [593]; `embed/gene_vectors.npy` [593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 593 or target_col == 593). Every well: [[MRTO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRTO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
