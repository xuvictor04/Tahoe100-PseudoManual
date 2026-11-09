---
symbol: "WDR83"
type: "gene"
col: 4410
ensembl_id: "ENSG00000123154"
name: "WD repeat domain 83"
location: "19p13.13"
module: 107
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# WDR83

*WD repeat domain 83* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +15.5, q 0e+00, up in 32 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Penfluridol (drug)]] 0.5 µM in 1 line (RKO 0.0424×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0763×; ⚠ cell-cycle shift, explains ~21% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (HT-29 0.0531×; ⚠ cell-cycle shift, explains ~79% of this change); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (HS-578T 0.0644×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (SW 900 0.0657×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC3]] (+0.63, fdr 1e-05), [[ARL16]] (+0.61, fdr 2e-05), [[XAB2]] (+0.60, fdr 3e-05); moves opposite to [[CYCS]] (-0.56, fdr 3e-05), [[CEP83]] (-0.53, fdr 1e-04), [[EFR3A]] (-0.50, fdr 7e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +15.5 | 0e+00 | 32/41 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +14.9 | 0e+00 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.57×** | +13.2 | 3e-37 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.57×** | +13.1 | 3e-37 | 43/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +7.9 | 3e-13 | 20/40 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.80×** | +7.6 | 4e-12 | 10/16 (NCI-H460, HS-578T, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +6.8 | 6e-10 | 20/45 (SW480, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +6.7 | 1e-09 | 17/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +6.7 | 1e-09 | 14/46 (A498, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.62×** | +6.5 | 6e-09 | 1/10 (PANC-1) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.8 | 3e-07 | 14/37 (HS-578T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 2e-06 | 16/41 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.47×** | +5.4 | 3e-06 | 9/24 (SW480, RPMI-7951, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.0 | 2e-05 | 9/47 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 6e-05 | 13/44 (SW480, C32, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 1e-04 | 11/43 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +4.5 | 2e-04 | 10/44 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.001 | 3/35 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4410.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Penfluridol (drug)]] 0.5 µM in 1 line (RKO 0.0424×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0763×; ⚠ cell-cycle shift, explains ~21% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (HT-29 0.0531×; ⚠ cell-cycle shift, explains ~79% of this change); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (HS-578T 0.0644×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (SW 900 0.0657×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erythromycin (drug)]] 0.05 µM |  | 0.786× | -3.4 | 0.23 | 5/46 (J82, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.787× | -3.3 | 0.23 | 14/44 (RPMI-7951, HOP62, …) | all doses, flat | position effect removed |
| [[Adenine (drug)]] 5 µM |  | 0.850× | -3.1 | 0.34 | 9/47 (SNU-1, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.11 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0644× (z -9.6) |
| [[HT-29 (line)]] | alt | 3.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0531× (z -9.9) ⚠ cell-cycle shift, explains ~79% of this change |
| [[RKO (line)]] | wt | 5.78 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0424× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0763× (z -9.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW 900 (line)]] | alt | 4.24 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0657× (z -8.7) |
| [[A-172 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC3]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ARL16]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[XAB2]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 | same gene group; STRING 704 |
| [[PEX16]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TFPT]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ZNF446]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ZBTB49]] | +0.58 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[SLC25A38]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[BRMS1]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ZNF707]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[GTF3C5]] | +0.57 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYCS]] | -0.56 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[CEP83]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[EFR3A]] | -0.50 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[CHRAC1]] | -0.50 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[RBBP8]] | -0.49 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[DNAH14]] | -0.48 | -0.12 / -0.49 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WDR83's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.0, -2.0); signed map (-23.7, 0.6). **Vector** length 39.1, 3.77% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +15.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.8 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 83 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,666,802-12,675,832 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MORG1 |
| Gene groups (HGNC) | WD repeat domain containing; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: MAP2K and MAPK activation; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRX9](https://www.uniprot.org/uniprotkb/Q9BRX9) (WD repeat domain-containing protein 83):

> Molecular scaffold protein for various multimeric protein complexes. Acts as a module in the assembly of a multicomponent scaffold for the ERK pathway, linking ERK responses to specific agonists. At low concentrations it enhances ERK activation, whereas high concentrations lead to the inhibition of ERK activation. Also involved in response to hypoxia by acting as a negative regulator of HIF1A/HIF-1-alpha via its interaction with EGLN3/PHD3. May promote degradation of HIF1A. May act by …

**Summary**, from NCBI Gene [84292](https://www.ncbi.nlm.nih.gov/gene/84292):

> This gene encodes a member of the WD-40 protein family. The protein is proposed to function as a molecular scaffold for various multimeric protein complexes. The protein associates with several components of the extracellular signal-regulated kinase (ERK) pathway, and promotes ERK activity in response to serum or other signals. The protein also interacts with egl nine homolog 3 (EGLN3, also known as PHD3) and regulates expression of hypoxia-inducible factor 1, and has been purified as part of …

**Accessions** — [HGNC:32672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32672) · Entrez [84292](https://www.ncbi.nlm.nih.gov/gene/84292) · UniProt [Q9BRX9](https://www.uniprot.org/uniprotkb/Q9BRX9) · Ensembl [ENSG00000123154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123154)

## Data

Gene col 4410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4410); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4410]; `tensor/DDL_lfc|DDL_z.npy` [4410]; `embed/gene_vectors.npy` [4410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4410 or target_col == 4410). Every well: [[WDR83 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR83.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
