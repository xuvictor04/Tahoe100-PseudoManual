---
symbol: "BCL2L14"
type: "gene"
col: 4269
ensembl_id: "ENSG00000121380"
name: "BCL2 like 14"
location: "12p13.2"
module: 44
arm: "+"
pooled_cpm: 17.24
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# BCL2L14

*BCL2 like 14* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.73× (z +9.9, q 2e-20, up in 35 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +8.7, q 7e-16, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.338×, LS 180 0.388×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.258×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A2MP1]] (+0.66, fdr 7e-06), [[ACSM3]] (+0.65, fdr 2e-05), [[MUC12]] (+0.63, fdr 1e-05); moves opposite to [[MLX]] (-0.56, fdr 1e-05), [[LZTR1]] (-0.56, fdr 3e-05), [[UBL4A]] (-0.53, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[MUC4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +9.9 | 2e-20 | 35/40 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +9.5 | 5e-19 | 23/29 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.7 | 7e-16 | 38/47 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.69×** | +5.4 | 1e-05 | 31/46 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.58×** | +4.7 | 3e-04 | 23/41 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.58×** | +4.4 | 0.001 | 16/31 (J82, A549, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.003 | 23/47 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.006 | 23/46 (CFPAC-1, NCI-H2030, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.338×, LS 180 0.388×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.258×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.717× | -3.2 | 0.85 | 13/48 (NCI-H661, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 45.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -8.7) |
| [[A549 (line)]] | wt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +9.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 9.74 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +15.8) | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A2MP1]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ACSM3]] | +0.65 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[MUC12]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC02331]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[DLEU7]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MGAM2]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ELF3]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MUC13]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TSPAN8]] | +0.59 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[SLC3A1]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[BCL2L15]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 | same gene group; STRING 649 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLX]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[LZTR1]] | -0.56 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[UBL4A]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TOP3B]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[STEAP3]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 | pathway: TP53 Regulates Transcription of Cell Death Genes |
| [[ABLIM3]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MAPKAPK3]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CDPF1]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ZNF473]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MIER2]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC4]] | B | MUC4 activity raises BCL2L14's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 1.44× lower at baseline in the lines without MUC4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[SLC44A4]] | B | SLC44A4 activity raises BCL2L14's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 1.57× lower at baseline in the lines without SLC44A4 | 0.025 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[GPRC5C]] | B | GPRC5C activity raises BCL2L14's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without GPRC5C | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[CLIC5]] | B | CLIC5 activity raises BCL2L14's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.62× lower at baseline in the lines without CLIC5 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[SIDT1]] | B | SIDT1 activity raises BCL2L14's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without SIDT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[LINC02331]] | B | LINC02331 activity raises BCL2L14's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without LINC02331 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[GRHL2]] | B | GRHL2 activity raises BCL2L14's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without GRHL2 | 0.043 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[PLA2G2A]] | B | PLA2G2A activity raises BCL2L14's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 1.52× lower at baseline in the lines without PLA2G2A | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[PLAAT4]] | B | PLAAT4 activity raises BCL2L14's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.14× lower at baseline in the lines without PLAAT4 | 0.067 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises BCL2L14's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.59× lower at baseline in the lines without TMPRSS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises BCL2L14's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.42× lower at baseline in the lines without PLEKHG6 | 0.069 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises BCL2L14's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.43× lower at baseline in the lines without TJP3 | 0.0998 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 53.0); signed map (55.7, -1.6). **Vector** length 72.1, 14.7% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.51 to 4); *Aspirin ADME* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +8.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.5 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:12,049,844-12,211,084 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCLG, BCL-G |
| Gene groups (HGNC) | BCL2 family |
| Reactome | 3 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZR8](https://www.uniprot.org/uniprotkb/Q9BZR8) (Apoptosis facilitator Bcl-2-like protein 14):

> Plays a role in apoptosis.

**Summary**, from NCBI Gene [79370](https://www.ncbi.nlm.nih.gov/gene/79370):

> The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. Overexpression of this gene has been shown to induce apoptosis in cells. Three alternatively spliced transcript variants encoding two distinct isoforms have been reported for this gene. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:16657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16657) · Entrez [79370](https://www.ncbi.nlm.nih.gov/gene/79370) · UniProt [Q9BZR8](https://www.uniprot.org/uniprotkb/Q9BZR8) · Ensembl [ENSG00000121380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121380)

## Data

Gene col 4269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4269); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4269]; `tensor/DDL_lfc|DDL_z.npy` [4269]; `embed/gene_vectors.npy` [4269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4269 or target_col == 4269). Every well: [[BCL2L14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
