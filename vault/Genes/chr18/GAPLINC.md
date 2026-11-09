---
symbol: "GAPLINC"
type: "gene"
col: 15498
ensembl_id: "ENSG00000266835"
name: "gastric adenocarcinoma associated, positive CD44 regulator, long intergenic non-coding RNA"
location: "18p11.31"
module: 35
arm: "+"
pooled_cpm: 2.26
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# GAPLINC

*gastric adenocarcinoma associated, positive CD44 regulator, long intergenic non-coding RNA* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.87× (z +17.3, q 0e+00, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.367× (z -9.1, q 8e-17, down in 26 of 42 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.551× (z -5.4, q 1e-05, down in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 0.0432×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0874×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0680×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM184B]] (+0.67, fdr 1e-05), [[DDX19A-DT]] (+0.64, fdr 2e-05), [[BAAT]] (+0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPOCK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.87×** | +17.3 | 0e+00 | 21/27 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +8.2 | 7e-14 | 10/45 (NCI-H2347, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.94×** | +5.7 | 3e-06 | 15/38 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.6 | 3e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.5 | 7e-04 | 8/35 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +4.3 | 0.001 | 10/36 (NCI-H460, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 11/46 (NCI-H460, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.9 | 0.008 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +3.6 | 0.018 | 7/33 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.4 | 0.035 | 2/5 (NCI-H2030, A-427) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.083 | 6/34 (A-172, HOP62, …) | top dose only |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.93×** | +3.1 | 0.083 | 1/44 (A-427) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.39× | +3.0 | 0.11 | 10/33 (HOP62, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15498.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 0.0432×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0874×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0680×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.367×** | -9.1 | 8e-17 | 26/42 (NCI-H23, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.404×** | -8.2 | 7e-14 | 22/46 (A-427, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.551×** | -5.4 | 1e-05 | 16/43 (PANC-1, SW 900, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.602×** | -4.6 | 7e-04 | 15/44 (NCI-H23, NCI-H2347, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.612×** | -4.4 | 0.001 | 15/42 (A-427, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.668×** | -3.6 | 0.026 | 9/44 (A-427, AsPC-1, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.675×** | -3.4 | 0.063 | 9/36 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | 0.691× | -3.2 | 0.11 | 6/13 (PANC-1, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 1.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 5.38 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0874× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 5.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0680× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.08 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0432× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.933 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.672 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.855 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.608 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.585 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM184B]] | +0.67 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DDX19A-DT]] | +0.64 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[BAAT]] | +0.63 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[OOEP]] | +0.63 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[HEATR4]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[NIPBL-DT]] | +0.61 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[HOXB-AS3]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SPATA1]] | +0.61 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[CPEB2-DT]] | +0.61 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[RELA-DT]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[RSPH9]] | +0.59 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[SAXO1]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK2]] | B | SPOCK2 activity raises GAPLINC's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without SPOCK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises GAPLINC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (12.7, 22.6); signed map (30.1, 0.7). **Vector** length 51.9, 7.09% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +5.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.0 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -1.9 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.8 | -9.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.7 | -8.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | gastric adenocarcinoma associated, positive CD44 regulator, long intergenic non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18p11.31 — chr18:3,466,250-3,487,045 (+) |
| Ensembl biotype | lncRNA |
| Also known as | TCONS_00026238, lncRNA-uc002kmd.1, RP11-838N2.4; previously LINC01540 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51308) · Entrez [100505592](https://www.ncbi.nlm.nih.gov/gene/100505592) · Ensembl [ENSG00000266835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266835)

## Data

Gene col 15498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15498); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15498]; `tensor/DDL_lfc|DDL_z.npy` [15498]; `embed/gene_vectors.npy` [15498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15498 or target_col == 15498). Every well: [[GAPLINC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAPLINC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
