---
symbol: "CISD3"
type: "gene"
col: 15902
ensembl_id: "ENSG00000277972"
name: "CDGSH iron sulfur domain 3"
location: "17q12"
module: 33
arm: "+"
pooled_cpm: 7.92
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# CISD3

*CDGSH iron sulfur domain 3* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.85× (z +11.5, q 8e-28, up in 25 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.51× (z +3.5, q 0.035, up in 16 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.644× (z -5.3, q 6e-05, down in 21 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (BT-474 0.251×, LS 180 0.187×, SW480 0.277×, KATO III 0.251×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.161×; ⚠ cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0879×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (AsPC-1 0.0644×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL12]] (+0.70, fdr 1e-05), [[ANTKMT]] (+0.68, fdr 4e-05), [[C20orf27]] (+0.67, fdr 7e-06); moves opposite to [[GNAS]] (-0.56, fdr 4e-05), [[USP34-DT]] (-0.53, fdr 3e-04), [[SEC24B-AS1]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KRT18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.85×** | +11.5 | 8e-28 | 25/26 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +11.1 | 5e-26 | 15/15 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +8.1 | 1e-13 | 20/22 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.87×** | +5.3 | 1e-05 | 19/35 (A-427, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.62×** | +3.9 | 0.009 | 17/35 (A549, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.7 | 0.022 | 11/33 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.035 | 16/43 (RKO, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +3.4 | 0.049 | 13/45 (NCI-H2030, Panc 03.27, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +3.2 | 0.099 | 11/33 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +3.1 | 0.099 | 9/41 (PANC-1, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15902.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (BT-474 0.251×, LS 180 0.187×, SW480 0.277×, KATO III 0.251×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.161×; ⚠ cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0879×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (AsPC-1 0.0644×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.644×** | -5.3 | 6e-05 | 21/41 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -3.8 | 0.042 | 21/44 (BT-474, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.703× | -3.0 | 0.48 | 12/47 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0644× (z -9.1) |
| [[BT-474 (line)]] | alt | 50.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.3) |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 6.20 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0879× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 5.64 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 5.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 7.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.6) |
| [[A-172 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL12]] | +0.70 | +0.52 / +0.73 | both halves | 1e-05 | STRING 540 |
| [[ANTKMT]] | +0.68 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[C20orf27]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DCTPP1]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TIMM8A]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[POLR3K]] | +0.62 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[HMBS]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NPM3]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 | STRING 498 |
| [[MRPL24]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 | STRING 704 |
| [[HAGHL]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[CKMT1A]] | +0.58 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[USP34-DT]] | -0.53 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[SEC24B-AS1]] | -0.49 | -0.31 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT18]] | B | KRT18 activity raises CISD3's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without KRT18 | 0.050 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[CKMT1B]] | B | CKMT1B activity raises CISD3's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.45× lower at baseline in the lines without CKMT1B | 0.077 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[SLC29A2]] | B | SLC29A2 activity raises CISD3's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without SLC29A2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN |
| [[FGFR4]] | B | FGFR4 activity raises CISD3's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without FGFR4 | 0.096 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.3, -42.3); signed map (-10.9, -53.2). **Vector** length 47.5, 6.94% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.7 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CDGSH iron sulfur domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,730,341-38,735,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Miner2, MiNT |
| Gene groups (HGNC) | CDGSH iron sulfur domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C7P0](https://www.uniprot.org/uniprotkb/P0C7P0) (CDGSH iron-sulfur domain-containing protein 3, mitochondrial):

> Can transfer its iron-sulfur clusters to the apoferrodoxins FDX1 and FDX2. Contributes to mitochondrial iron homeostasis and in maintaining normal levels of free iron and reactive oxygen species, and thereby contributes to normal mitochondrial function.

**Summary**, from NCBI Gene [284106](https://www.ncbi.nlm.nih.gov/gene/284106):

> CISD3 is a member of the CDGSH domain-containing family, which may play a role in regulating electron transport and oxidative phosphorylation (Wiley et al., 2007 [PubMed 17376863]).[supplied by OMIM, Apr 2008]

**Accessions** — [HGNC:27578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27578) · Entrez [284106](https://www.ncbi.nlm.nih.gov/gene/284106) · UniProt [P0C7P0](https://www.uniprot.org/uniprotkb/P0C7P0) · Ensembl [ENSG00000277972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277972)

## Data

Gene col 15902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15902); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15902]; `tensor/DDL_lfc|DDL_z.npy` [15902]; `embed/gene_vectors.npy` [15902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15902 or target_col == 15902). Every well: [[CISD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CISD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
