---
symbol: "GIHCG"
type: "gene"
col: 15057
ensembl_id: "ENSG00000257698"
name: "GIHCG inhibitor of miR-200b/200a/429 expression"
location: "12q14.1"
module: 59
arm: "+"
pooled_cpm: 6.08
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 9
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# GIHCG

*GIHCG inhibitor of miR-200b/200a/429 expression* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +6.4, q 7e-08, up in 19 of 34 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.4, q 0.001, up in 13 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (SHP-77 0.0927×; ⚠ transcription drop); [[Cinacalcet (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0539×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM5]] (+0.62, fdr 7e-06), [[ATP23]] (+0.62, fdr 7e-06, ⚠ same locus), [[MITD1]] (+0.61, fdr 7e-06), [[CLK4]] (+0.61, fdr 1e-05); moves opposite to [[URB1]] (-0.64, fdr 1e-05), [[RNPS1]] (-0.63, fdr 9e-06), [[TCOF1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 9 go from it, the strongest it → [[DNAJC27]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.78×** | +6.4 | 7e-08 | 19/34 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +6.3 | 7e-08 | 12/14 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.20×** | +6.2 | 7e-08 | 14/19 (PANC-1, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.26×** | +6.2 | 7e-08 | 8/10 (PANC-1, A498, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.85×** | +4.9 | 1e-04 | 14/24 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.001 | 13/35 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +4.0 | 0.005 | 8/31 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.65×** | +3.8 | 0.010 | 15/37 (SW 900, A-172, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.32× | +3.1 | 0.14 | 15/38 (SHP-77, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (SHP-77 0.0927×; ⚠ transcription drop); [[Cinacalcet (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0539×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.624× | -3.7 | 0.10 | 15/38 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.473× | -3.1 | 0.38 | 11/32 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.662× | -3.1 | 0.38 | 13/37 (HOP62, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.36 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0539× (z -8.9) |
| [[SHP-77 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0927× (z -9.5) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ATP23]] | +0.62 | +0.67 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MITD1]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CLK4]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[TCEAL8]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[AKAP9]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.60 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[TERF2IP]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NKAP]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PIGP]] | +0.60 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[FMC1]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[DNAL4]] | +0.59 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[MORN2]] | +0.59 | +0.71 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.63 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[TCOF1]] | -0.62 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[TTL]] | -0.60 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.60 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.59 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NADK]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TATDN2]] | -0.57 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[RPSA]] | -0.57 | -0.57 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC27]] | B | GIHCG activity raises DNAJC27's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without GIHCG | 0.006 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[IFT22]] | B | GIHCG activity raises IFT22's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without GIHCG | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[MORN2]] | B | GIHCG activity raises MORN2's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without GIHCG | 0.036 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[SPACA9]] | B | GIHCG activity raises SPACA9's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without GIHCG | 0.049 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[MITD1]] | B | GIHCG activity raises MITD1's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without GIHCG | 0.051 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[ABCA5]] | B | GIHCG activity raises ABCA5's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without GIHCG | 0.064 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[LIPT1]] | B | GIHCG activity raises LIPT1's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without GIHCG | 0.072 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[TTL]] | B | GIHCG activity raises TTL's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without GIHCG | 0.080 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[ATP23]] | B | GIHCG activity raises ATP23's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without GIHCG | 0.093 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.0, -28.2); signed map (-7.0, 1.4). **Vector** length 45.6, 7.68% of its response variance represented; |z| ≥ 3 in 474 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.6 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.1 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.3 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.9 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | GIHCG inhibitor of miR-200b/200a/429 expression |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q14.1 — chr12:57,930,115-57,936,345 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncRNA-GIHCG |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52649) · Entrez [100506844](https://www.ncbi.nlm.nih.gov/gene/100506844) · Ensembl [ENSG00000257698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257698)

## Data

Gene col 15057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15057); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15057]; `tensor/DDL_lfc|DDL_z.npy` [15057]; `embed/gene_vectors.npy` [15057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15057 or target_col == 15057). Every well: [[GIHCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIHCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
