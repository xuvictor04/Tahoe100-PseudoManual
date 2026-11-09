---
symbol: "SLC6A15"
type: "gene"
col: 1000
ensembl_id: "ENSG00000072041"
name: "solute carrier family 6 member 15"
location: "12q21.31"
module: 9
arm: "+"
pooled_cpm: 8.38
n_lines_expressing: 18
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SLC6A15

*solute carrier family 6 member 15* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +12.8, q 8e-35, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +10.1, q 8e-22, up in 11 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 0.300×, SK-MEL-2 0.342×, NCI-H23 0.303×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.243×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.233×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANGPT1]] (+0.63, fdr 1e-05), [[KCTD8]] (+0.60, fdr 1e-05), [[ZNF208]] (+0.54, fdr 1e-05); moves opposite to [[SHPK]] (-0.43, fdr 1e-04), [[TRPV1]] (-0.43, fdr 3e-04), [[DZANK1]] (-0.42, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SNCA]] → it (grade C ⚠); 2 go from it, the strongest it → [[GPR63]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +12.8 | 8e-35 | 7/11 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +12.4 | 1e-32 | 6/9 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +10.1 | 8e-22 | 11/15 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +8.5 | 3e-15 | 4/10 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +7.3 | 4e-11 | 11/15 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.0 | 2e-10 | 6/13 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.7 | 8e-07 | 9/15 (HOP62, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.9 | 7e-05 | 7/13 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.6 | 3e-04 | 6/15 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.8 | 0.008 | 1/14 (H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.011 | 1/13 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.7 | 0.011 | 0/9 | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.011 | 0/15 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.6 | 0.013 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.014 | 3/15 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.019 | 3/14 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.028 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.037 | 2/15 (NCI-H2030, NCI-H661) | inconsistent across doses | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.041 | 4/15 (H4, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.041 | 2/15 (NCI-H460, LOX-IMVI) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.042 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.042 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 0.300×, SK-MEL-2 0.342×, NCI-H23 0.303×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.243×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.233×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 5.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.582 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGPT1]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KCTD8]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF208]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[UNC5C]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[GRIA2]] | +0.53 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CDH10]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[FRG1FP]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TMEM64]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[KHDRBS2]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[FAM230C]] | +0.51 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[NELL2]] | +0.51 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[EDNRB]] | +0.50 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPK]] | -0.43 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TRPV1]] | -0.43 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[DZANK1]] | -0.42 | -0.26 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNCA]] | C | SNCA activity raises SLC6A15's level | lines that do not express SNCA (29) vs lines expressing it (21) | 6.20× lower at baseline in the lines without SNCA | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises SLC6A15's level | lines that do not express BCHE (35) vs lines expressing it (15) | 7.11× lower at baseline in the lines without BCHE | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises SLC6A15's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 5.00× lower at baseline in the lines without CDH18 | 0.038 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises SLC6A15's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.42× lower at baseline in the lines without EPHA5 | 0.049 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises SLC6A15's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 3.62× lower at baseline in the lines without JAKMIP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises SLC6A15's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without ASXL3 | 0.079 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR63]] | B | SLC6A15 activity raises GPR63's level | lines that do not express SLC6A15 (32) vs lines expressing it (18) | 1.75× lower at baseline in the lines without SLC6A15 | 0.067 | ⚠ within organs, on part of the lines; also absent: PAX3, CNKSR2, ENSG00000286251 |
| [[CCND2]] | C | SLC6A15 activity raises CCND2's level | lines that do not express SLC6A15 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without SLC6A15 | 0.085 | ⚠ within organs, on part of the lines; also absent: PAX3, CNKSR2, ENSG00000286251; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 36.7); signed map (43.2, 34.9). **Vector** length 45.0, 13.0% of its response variance represented; |z| ≥ 3 in 327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -0.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:84,859,491-84,913,629 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hv7-3, NTT73, FLJ10316, V7-3, SBAT1 |
| Gene groups (HGNC) | Solute carrier family 6 |
| Reactome | 5 pathways, smallest: SLC-mediated transport of neurotransmitters; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2J7](https://www.uniprot.org/uniprotkb/Q9H2J7) (Sodium-dependent neutral amino acid transporter B(0)AT2):

> Functions as a sodium-dependent neutral amino acid transporter. Exhibits preference for the branched-chain amino acids, particularly leucine, valine and isoleucine and methionine. Can also transport low-affinity substrates such as alanine, phenylalanine, glutamine and pipecolic acid. Mediates the saturable, pH-sensitive and electrogenic cotransport of proline and sodium ions with a stoichiometry of 1:1. May have a role as transporter for neurotransmitter precursors into neurons. In contrast to …

**Summary**, from NCBI Gene [55117](https://www.ncbi.nlm.nih.gov/gene/55117):

> This gene encodes a member of the solute carrier family 6 protein family which transports neutral amino acids. The encoded protein is thought to play a role in neuronal amino acid transport (PMID: 16185194) and may be associated with major depression (PMID: 21521612). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:13621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13621) · Entrez [55117](https://www.ncbi.nlm.nih.gov/gene/55117) · UniProt [Q9H2J7](https://www.uniprot.org/uniprotkb/Q9H2J7) · Ensembl [ENSG00000072041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072041)

## Data

Gene col 1000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1000); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1000]; `tensor/DDL_lfc|DDL_z.npy` [1000]; `embed/gene_vectors.npy` [1000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1000 or target_col == 1000). Every well: [[SLC6A15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
