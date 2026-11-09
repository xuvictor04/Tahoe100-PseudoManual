---
symbol: "ABHD8"
type: "gene"
col: 4795
ensembl_id: "ENSG00000127220"
name: "abhydrolase domain containing 8"
location: "19p13.11"
module: 30
arm: "+"
pooled_cpm: 6.92
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ABHD8

*abhydrolase domain containing 8* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.58× (z +12.6, q 1e-33, up in 9 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.33× (z +8.7, q 7e-16, up in 36 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0690×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0774×); [[Resveratrol (drug)]] 0.05 µM in 1 line (Hs 766T 0.0871×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN6-DT]] (+0.71, fdr 7e-06), [[ZNF552]] (+0.66, fdr 1e-05), [[TMEM219]] (+0.64, fdr 1e-05); moves opposite to [[EIF4G1]] (-0.65, fdr 7e-06), [[CCT7]] (-0.61, fdr 8e-06), [[XRCC5]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAMSAP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.58×** | +12.6 | 1e-33 | 9/12 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +10.8 | 2e-24 | 20/28 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +8.7 | 7e-16 | 36/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +8.5 | 3e-15 | 9/20 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +8.2 | 4e-14 | 33/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +6.8 | 8e-10 | 28/46 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.4 | 4e-06 | 26/47 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.3 | 7e-06 | 17/43 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.6 | 3e-04 | 15/29 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 7e-04 | 18/43 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.3 | 8e-04 | 15/39 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 17/45 (HOP62, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.006 | 16/41 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.5 | 0.020 | 11/42 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.055 | 6/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.055 | 6/38 (SNU-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0690×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0774×); [[Resveratrol (drug)]] 0.05 µM in 1 line (Hs 766T 0.0871×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 0.788× | -3.5 | 0.27 | 13/47 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.38 | 9/46 (SW48, Panc 03.27, …) | two highest doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.731× | -3.1 | 0.41 | 10/47 (COLO 205, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 11.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.1× (z +14.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 7.09 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0774× (z -9.1) |
| [[PANC-1 (line)]] | alt | 5.29 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.01× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 8.98 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0690× (z -9.5) |
| [[SHP-77 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 8.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.10× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | +0.71 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ZNF552]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TMEM219]] | +0.64 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[FAM182B]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[EFCAB14-AS1]] | +0.62 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[FAM229B]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[LINC00674]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CSKMT]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SYP]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RN7SL2]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[SLC17A7]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[AQP11]] | +0.61 | +0.39 / +0.68 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CCT7]] | -0.61 | -0.58 / -0.57 | both halves | 8e-06 |  |
| [[XRCC5]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.58 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[CYREN]] | -0.58 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[UTP15]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[VARS1]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TASOR]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[WDR27]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SF3B3]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.55 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMSAP3]] | B | CAMSAP3 activity raises ABHD8's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without CAMSAP3 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.6, -11.0); signed map (-31.1, -2.9). **Vector** length 63.7, 10.6% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,292,131-17,310,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11743, MGC14280, MGC2512 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I13](https://www.uniprot.org/uniprotkb/Q96I13) (Protein ABHD8):

> Negatively regulates NLRP3-driven inflammation. Promotes NLRP3 degradation through the chaperone-mediated autophagy (CMA) pathway, hence attenuating inflammasome activation and IL1B secretion. Acts by recruiting palmitoyltransferase ZDHHC12 to NLRP3, facilitating NLRP3 palmitoylation and subsequent degradation.

**Summary**, from NCBI Gene [79575](https://www.ncbi.nlm.nih.gov/gene/79575):

> This gene is upstream of, and in a head-to-head orientation with the gene for the mitochondrial ribosomal protein L34. The predicted protein contains alpha/beta hydrolase fold and secretory lipase domains. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23759) · Entrez [79575](https://www.ncbi.nlm.nih.gov/gene/79575) · UniProt [Q96I13](https://www.uniprot.org/uniprotkb/Q96I13) · Ensembl [ENSG00000127220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127220)

## Data

Gene col 4795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4795); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4795]; `tensor/DDL_lfc|DDL_z.npy` [4795]; `embed/gene_vectors.npy` [4795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4795 or target_col == 4795). Every well: [[ABHD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
