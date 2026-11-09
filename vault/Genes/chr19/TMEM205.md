---
symbol: "TMEM205"
type: "gene"
col: 2615
ensembl_id: "ENSG00000105518"
name: "transmembrane protein 205"
location: "19p13.2"
module: 24
arm: "+"
pooled_cpm: 14.0
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TMEM205

*transmembrane protein 205* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +7.4, q 1e-10, up in 27 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +3.6, q 0.019, up in 25 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 8.56×, PANC-1 3.17×, A-172 3.89×; ⚠ cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 7.56×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 6.13×; ⚠ cell-cycle shift, explains ~46% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.278× (z -4.1, q 0.026, down in 28 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (RPMI-7951 0.101×; ⚠ toxic; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM17B]] (+0.70, fdr 7e-06, ⚠ TIMM17B in the vector space only through flagged drug-doses), [[KRTCAP2]] (+0.69, fdr 7e-06), [[MED19]] (+0.68, fdr 7e-06), [[METTL23]] (+0.67, fdr 7e-06); moves opposite to [[RNPS1]] (-0.69, fdr 7e-06), [[RPSA]] (-0.65, fdr 7e-06), [[METTL3]] (-0.65, fdr 8e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01273]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 8.56×, PANC-1 3.17×, A-172 3.89×; ⚠ cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 7.56×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 6.13×; ⚠ cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.98×** | +7.4 | 1e-10 | 27/35 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.09×** | +7.0 | 7e-10 | 33/46 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.68×** | +6.4 | 3e-08 | 38/47 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.56×** | +6.1 | 2e-07 | 16/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.32×** | +5.7 | 2e-06 | 38/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.02×** | +4.7 | 2e-04 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.90×** | +4.3 | 0.001 | 26/41 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.76×** | +3.8 | 0.009 | 26/47 (LoVo, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.019 | 25/45 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.70×** | +3.6 | 0.019 | 27/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.046 | 23/45 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | 1.56× | +3.0 | 0.13 | 21/46 (NCI-H1573, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (RPMI-7951 0.101×; ⚠ toxic; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.278×** | -4.1 | 0.026 | 28/43 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.347× | -3.4 | 0.21 | 24/48 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.376× | -3.1 | 0.31 | 23/46 (HT-29, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.623× | -3.1 | 0.31 | 22/47 (NCI-H661, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.1) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[AsPC-1 (line)]] | alt | 5.58 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +9.8) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[PANC-1 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.3) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM17B]] ⚠ | +0.70 | +0.62 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[KRTCAP2]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[MED19]] | +0.68 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[METTL23]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.67 | +0.58 / +0.71 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.66 | +0.40 / +0.78 | both halves | 5e-05 |  |
| [[MIEN1]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SELENOM]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.64 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NUDT16L1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[POLR2J]] ⚠ | +0.63 | +0.46 / +0.72 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANKRD12]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SMDT1]] | +0.63 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PIM3]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPS1]] | -0.69 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[RPSA]] | -0.65 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[METTL3]] | -0.65 | -0.60 / -0.57 | both halves | 8e-06 |  |
| [[AHSA1]] | -0.63 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.62 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.61 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.61 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[NAA50]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.60 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[THOC5]] | -0.60 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[NPEPL1]] | -0.59 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[C1orf198]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01273]] | B | LINC01273 activity raises TMEM205's level | lines that do not express LINC01273 (12) vs lines expressing it (38) | 1.30× lower at baseline in the lines without LINC01273 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287263, A4GALT, TRIM7; maybe low, not absent; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity lowers TMEM205's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.5, -15.9); signed map (-12.3, -1.9). **Vector** length 72.9, 19.4% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +6.5 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.0 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.6 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | +2.0 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[palbociclib (drug)]] 5 µM |  | +1.0 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -3.6 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 205 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,342,776-11,346,518 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ501, MBC3205 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UW68](https://www.uniprot.org/uniprotkb/Q6UW68) (Transmembrane protein 205):

> In cancer cells, plays a role in resistance to the chemotherapeutic agent cisplatin.

**Summary**, from NCBI Gene [374882](https://www.ncbi.nlm.nih.gov/gene/374882):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29631) · Entrez [374882](https://www.ncbi.nlm.nih.gov/gene/374882) · UniProt [Q6UW68](https://www.uniprot.org/uniprotkb/Q6UW68) · Ensembl [ENSG00000105518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105518)

## Data

Gene col 2615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2615); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2615]; `tensor/DDL_lfc|DDL_z.npy` [2615]; `embed/gene_vectors.npy` [2615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2615 or target_col == 2615). Every well: [[TMEM205 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM205.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
