---
symbol: "MAGEA1"
type: "gene"
col: 12640
ensembl_id: "ENSG00000198681"
name: "MAGE family member A1"
location: "Xq28"
module: 16
arm: "+"
pooled_cpm: 2.87
n_lines_expressing: 13
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MAGEA1

*MAGE family member A1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.23× (z +11.2, q 3e-26, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.35× (z +4.7, q 3e-04, up in 9 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGEB2]] (+0.69, fdr 7e-06), [[MAGEA10]] (+0.61, fdr 6e-05), [[SOHLH2]] (+0.51, fdr 3e-05); moves opposite to [[SEC61A2]] (-0.48, fdr 5e-05), [[SETD3]] (-0.47, fdr 4e-05), [[GNRH1]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PNLIPRP3]] → it (grade C ⚠); 5 go from it, the strongest it → [[LRRC27]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.23×** | +11.2 | 3e-26 | 5/5 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.48×** | +10.3 | 2e-22 | 6/6 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.81×** | +8.0 | 2e-13 | 5/6 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.32×** | +6.4 | 3e-08 | 7/7 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.85×** | +5.5 | 3e-06 | 3/7 (NCI-H1573, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +4.7 | 3e-04 | 9/9 (NCI-H460, H4, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +4.3 | 0.002 | 3/11 (NCI-H1573, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.17×** | +4.2 | 0.002 | 3/6 (NCI-H460, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.08×** | +4.0 | 0.004 | 6/7 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.0 | 0.004 | 3/7 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.06×** | +3.9 | 0.005 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.06×** | +3.8 | 0.007 | 8/11 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.97×** | +3.7 | 0.009 | 1/7 (SK-MEL-2) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +3.6 | 0.015 | 6/10 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.3 | 0.036 | 1/8 (NCI-H2030) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.059 | 1/7 (LOX-IMVI) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.526× | -3.3 | 0.51 | 0/11 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.241 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEB2]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; STRING 435 |
| [[MAGEA10]] | +0.61 | +0.38 / +0.60 | both halves | 6e-05 | same gene group; STRING 520 |
| [[SOHLH2]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SRRD]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[TAFA5]] | +0.49 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[MRFAP1]] | +0.47 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LINC01592]] | +0.45 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[DNAH14]] | +0.45 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[MIR4527HG]] | +0.45 | +0.59 / +0.23 | both halves | 5e-04 |  |
| [[PCSK2]] | +0.44 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[LINC02930]] | +0.44 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[SLC35A4]] | +0.43 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SETD3]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[GNRH1]] | -0.45 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GET1-SH3BGR]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SPAST]] | -0.44 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[UPK1B]] | -0.42 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[KDELR1]] | -0.42 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[RAP2A]] | -0.42 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[WHAMMP1]] | -0.42 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TMEM50B]] | -0.41 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[LRRC27]] | -0.41 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[UBTD1]] | -0.41 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNLIPRP3]] | C | PNLIPRP3 activity raises MAGEA1's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without PNLIPRP3 | 0.076 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC27]] | B | MAGEA1 activity strengthens LRRC27's drug response | lines that do not express MAGEA1 (36) vs lines expressing it (11) | the lines without MAGEA1 respond 0.64× as strongly (z diff +1.52); strongest at Niclosamide (olamine) 5 µM: 0.50x vs 0.26x (z diff +3.5) | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; target measured in part of the lines; artifact flags |
| [[CCL3]] | C | MAGEA1 activity raises CCL3's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 1.97× lower at baseline in the lines without MAGEA1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |
| [[MIR4527HG]] | C | MAGEA1 activity raises MIR4527HG's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 3.72× lower at baseline in the lines without MAGEA1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |
| [[LINC02267]] | C | MAGEA1 activity raises LINC02267's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 2.50× lower at baseline in the lines without MAGEA1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |
| [[MAGEB2]] | C | MAGEA1 activity raises MAGEB2's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 2.67× lower at baseline in the lines without MAGEA1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.387). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (34.2, 33.4); signed map (30.8, 34.9). **Vector** length 24.0, 6.69% of its response variance represented; |z| ≥ 3 in 186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +0.8 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +0.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.7 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.6 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.5 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.4 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | -0.2 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -0.3 | -0.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.3 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.3 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,179,284-153,183,880 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9326, CT1.1; previously MAGE1 |
| Gene groups (HGNC) | MAGE family |
| Matched by | ensembl_id |

**Function**, from UniProt [P43355](https://www.uniprot.org/uniprotkb/P43355) (Melanoma-associated antigen 1):

> May be involved in transcriptional regulation through interaction with SNW1 and recruiting histone deactelyase HDAC1. May inhibit notch intracellular domain (NICD) transactivation. May play a role in embryonal development and tumor transformation or aspects of tumor progression. Antigen recognized on a melanoma by autologous cytolytic T-lymphocytes.

**Summary**, from NCBI Gene [4100](https://www.ncbi.nlm.nih.gov/gene/4100):

> This gene is a member of the MAGEA gene family. The members of this family encode proteins with 50 to 80% sequence identity to each other. The promoters and first exons of the MAGEA genes show considerable variability, suggesting that the existence of this gene family enables the same function to be expressed under different transcriptional controls. The MAGEA genes are clustered at chromosomal location Xq28. They have been implicated in some hereditary disorders, such as dyskeratosis …

**Accessions** — [HGNC:6796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6796) · Entrez [4100](https://www.ncbi.nlm.nih.gov/gene/4100) · UniProt [P43355](https://www.uniprot.org/uniprotkb/P43355) · Ensembl [ENSG00000198681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198681)

## Data

Gene col 12640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12640); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12640]; `tensor/DDL_lfc|DDL_z.npy` [12640]; `embed/gene_vectors.npy` [12640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12640 or target_col == 12640). Every well: [[MAGEA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
