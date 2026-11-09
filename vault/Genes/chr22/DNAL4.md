---
symbol: "DNAL4"
type: "gene"
col: 1904
ensembl_id: "ENSG00000100246"
name: "dynein axonemal light chain 4"
location: "22q13.1"
module: 12
arm: "+"
pooled_cpm: 5.25
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DNAL4

*dynein axonemal light chain 4* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +8.0, q 5e-13, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.99× (z +5.9, q 8e-07, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.447× (z -6.9, q 3e-09, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB8]] (+0.73, fdr 7e-06), [[NUDT16L1]] (+0.72, fdr 7e-06), [[NFKBIL1]] (+0.72, fdr 7e-06); moves opposite to [[ADAT2]] (-0.62, fdr 1e-05), [[HNRNPA3]] (-0.62, fdr 7e-06), [[TXN]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MEGF11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.0 | 5e-13 | 5/8 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.4 | 4e-11 | 20/27 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +5.9 | 8e-07 | 32/45 (A498, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.73×** | +4.7 | 4e-04 | 17/32 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +4.6 | 6e-04 | 23/47 (KATO III, A498, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.69×** | +4.3 | 0.002 | 20/43 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.5 | 0.035 | 15/30 (LS 180, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +3.4 | 0.039 | 13/39 (A498, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.99×** | +3.4 | 0.039 | 11/35 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +3.4 | 0.042 | 12/46 (Hs 766T, SHP-77, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.32×** | +3.3 | 0.045 | 15/39 (NCI-H2030, LoVo, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.053 | 10/46 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.056 | 5/38 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.056 | 6/45 (KATO III, SW 900, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.89×** | +3.2 | 0.056 | 6/41 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.447×** | -6.9 | 3e-09 | 26/47 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.450×** | -6.8 | 3e-09 | 29/45 (HS-578T, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.258×** | -5.5 | 9e-06 | 29/41 (KATO III, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.262×** | -5.4 | 9e-06 | 21/38 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -4.8 | 2e-04 | 20/46 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -4.4 | 1e-03 | 19/45 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -4.1 | 0.003 | 20/40 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -3.4 | 0.045 | 15/47 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -3.3 | 0.053 | 11/45 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.057 | 15/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.690×** | -3.1 | 0.085 | 12/44 (SNU-423, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 7.95 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0817× (z -10.8) |
| [[KATO III (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 7.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.14× (z +9.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 3.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0600× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0703× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 5.80 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0927× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.96 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0636× (z -9.8) |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0507× (z -8.5) |
| [[A-172 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB8]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[NUDT16L1]] | +0.72 | +0.61 / +0.79 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MED19]] | +0.71 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[STK16]] | +0.70 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[TIMM17B]] ⚠ | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG11]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[MORN2]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.68 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[EMC9]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.66 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[NKAP]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT2]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[TXN]] | -0.62 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[LAPTM4B]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NAA50]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.61 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[RPSA]] | -0.60 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.59 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[NUP210]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[ADCY3]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MACROH2A1]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[HACD3]] | -0.57 | -0.66 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEGF11]] | B | MEGF11 activity raises DNAL4's level | lines that do not express MEGF11 (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without MEGF11 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLIP3, UNC5CL, ZNF385C; maybe low, not absent; its own permutation p |
| [[BTNL9]] | B | BTNL9 activity lowers DNAL4's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.16× higher at baseline in the lines without BTNL9 | 0.063 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.6, 0.8); signed map (-11.4, -2.3). **Vector** length 55.9, 8.62% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.9 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.1 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | +0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal light chain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,778,508-38,794,198 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ327J16, PIG27 |
| Gene groups (HGNC) | Dyneins, axonemal outer arm complex subunits; Dynein light chain LC8-type family |
| Reactome | 4 pathways, smallest: Retrograde neurotrophin signalling; Signaling by NTRK1 (TRKA); Signaling by NTRKs |
| Matched by | ensembl_id |

**Function**, from UniProt [O96015](https://www.uniprot.org/uniprotkb/O96015) (Dynein axonemal light chain 4):

> Force generating protein of respiratory cilia. Produces force towards the minus ends of microtubules. Dynein has ATPase activity (By similarity).

**Summary**, from NCBI Gene [10126](https://www.ncbi.nlm.nih.gov/gene/10126):

> This gene encodes an axonemal dynein light chain which functions as a component of the outer dynein arms complex. This complex acts as the molecular motor that provides the force to move cilia in an ATP-dependent manner. The encoded protein is expressed in tissues with motile cilia or flagella and may be involved in the movement of sperm flagella. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:2955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2955) · Entrez [10126](https://www.ncbi.nlm.nih.gov/gene/10126) · UniProt [O96015](https://www.uniprot.org/uniprotkb/O96015) · Ensembl [ENSG00000100246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100246)

## Data

Gene col 1904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1904); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1904]; `tensor/DDL_lfc|DDL_z.npy` [1904]; `embed/gene_vectors.npy` [1904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1904 or target_col == 1904). Every well: [[DNAL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
