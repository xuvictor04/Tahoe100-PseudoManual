---
symbol: "TEFM"
type: "gene"
col: 10219
ensembl_id: "ENSG00000172171"
name: "transcription elongation factor, mitochondrial"
location: "17q11.2"
module: 89
arm: "+"
pooled_cpm: 14.63
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TEFM

*transcription elongation factor, mitochondrial* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.51× (z +9.7, q 1e-19, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.673× (z -6.3, q 9e-08, down in 25 of 43 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.136×, NCI-H460 0.154×, HEC-1-A 0.173×, HT-29 0.155×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.112×, HOP62 0.265×, Hs 766T 0.186×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.143×, C32 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH1]] (+0.76, fdr 7e-06), [[ALKBH4]] (+0.76, fdr 7e-06), [[SLC25A17]] (+0.72, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.61, fdr 1e-05), [[RBBP7]] (-0.59, fdr 1e-05), [[GOLIM4]] (-0.59, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAFIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +9.7 | 1e-19 | 31/48 (A498, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +9.0 | 9e-17 | 35/41 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.0 | 5e-10 | 26/47 (LoVo, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.1 | 5e-05 | 18/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.0 | 8e-05 | 19/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.9 | 8e-05 | 21/47 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.002 | 15/47 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.026 | 5/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.031 | 13/48 (HS-578T, PANC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.031 | 11/44 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.041 | 8/47 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.048 | 3/47 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.048 | 11/43 (NCI-H2030, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.058 | 6/47 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.060 | 9/47 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.071 | 5/48 (LS 180, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10219.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.136×, NCI-H460 0.154×, HEC-1-A 0.173×, HT-29 0.155×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.112×, HOP62 0.265×, Hs 766T 0.186×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.143×, C32 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -6.3 | 9e-08 | 25/43 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -6.3 | 9e-08 | 17/25 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.686×** | -6.2 | 9e-08 | 20/36 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.4 | 0.11 | 10/48 (SW1417, NCI-H661, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.819× | -3.3 | 0.11 | 12/47 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 17.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.19× (z +8.8) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.222× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 12.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.48× (z +9.5) | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -9.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 9.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -17.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH1]] | +0.76 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.76 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[SLC25A17]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[POLL]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[TIMM29]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.70 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[SETDB1]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[NGDN]] | +0.69 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[ZCCHC10]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZNF573]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[SNRNP35]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.59 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[GOLIM4]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TFRC]] | -0.58 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[EZH2]] | -0.57 | -0.54 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFIP]] | B | MAFIP activity raises TEFM's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without MAFIP | 0.025 | ⚠ within organs, on part of the lines |
| [[ZNF461]] | B | ZNF461 activity raises TEFM's level | lines that do not express ZNF461 (7) vs lines expressing it (43) | 1.20× lower at baseline in the lines without ZNF461 | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF567, ZNF529-AS1, ZNF571 |
| [[ZNF573]] | C | ZNF573 activity raises TEFM's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.40× lower at baseline in the lines without ZNF573 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.870). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.4, 7.6); signed map (-8.8, -15.5). **Vector** length 83.1, 15.8% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.3 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.1 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.5 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.9 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,897,336-30,906,238 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22729; previously C17orf42 |
| Reactome | 1 pathways, smallest: Mitochondrial transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QE5](https://www.uniprot.org/uniprotkb/Q96QE5) (Transcription elongation factor, mitochondrial):

> Transcription elongation factor which increases mitochondrial RNA polymerase processivity. Regulates transcription of the mitochondrial genome, including genes important for the oxidative phosphorylation machinery.

**Summary**, from NCBI Gene [79736](https://www.ncbi.nlm.nih.gov/gene/79736):

> Enables transcription elongation factor activity. Involved in positive regulation of mitochondrial transcription and regulation of oxidative phosphorylation. Located in mitochondrial nucleoid. Part of ribonucleoprotein complex. Implicated in combined oxidative phosphorylation deficiency. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26223) · Entrez [79736](https://www.ncbi.nlm.nih.gov/gene/79736) · UniProt [Q96QE5](https://www.uniprot.org/uniprotkb/Q96QE5) · Ensembl [ENSG00000172171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172171)

## Data

Gene col 10219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10219); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10219]; `tensor/DDL_lfc|DDL_z.npy` [10219]; `embed/gene_vectors.npy` [10219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10219 or target_col == 10219). Every well: [[TEFM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEFM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
