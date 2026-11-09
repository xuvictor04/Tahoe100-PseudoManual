---
symbol: "AMZ2P1"
type: "gene"
col: 13179
ensembl_id: "ENSG00000214174"
name: "AMZ2 pseudogene 1"
location: "17q24.1"
module: 28
arm: "+"
pooled_cpm: 3.23
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AMZ2P1

*AMZ2 pseudogene 1* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +8.2, q 1e-13, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.518× (z -6.5, q 4e-08, down in 18 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.593× (z -5.2, q 7e-05, down in 17 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0881×; ⚠ cell-cycle shift, explains ~36% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMZ2P1-1]] (+0.72, fdr 7e-06, ⚠ same locus), [[RAD52]] (+0.64, fdr 7e-06), [[IFT46]] (+0.61, fdr 2e-05), [[KCTD18]] (+0.61, fdr 1e-05); moves opposite to [[FARP2]] (-0.56, fdr 3e-05), [[ARPC5L]] (-0.55, fdr 3e-05), [[PGP]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OGFRL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +8.2 | 1e-13 | 23/38 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.70×** | +7.4 | 5e-11 | 18/46 (A-427, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.6 | 9e-04 | 13/44 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.5 | 9e-04 | 14/36 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.46×** | +3.7 | 0.022 | 8/42 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.022 | 10/43 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.031 | 7/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.045 | 6/46 (KATO III, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +3.3 | 0.057 | 7/39 (A498, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.3 | 0.057 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.087 | 4/36 (A-172, CHP-212, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.092 | 3/46 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13179.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0881×; ⚠ cell-cycle shift, explains ~36% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.518×** | -6.5 | 4e-08 | 18/31 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.593×** | -5.2 | 7e-05 | 17/43 (C-33 A, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.619×** | -4.8 | 4e-04 | 16/43 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.631×** | -4.6 | 7e-04 | 13/46 (SW480, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.679×** | -3.8 | 0.014 | 17/44 (LS 180, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.709× | -3.2 | 0.15 | 10/43 (COLO 205, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.38 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0881× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMZ2P1-1]] | +0.72 | +0.80 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RAD52]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[IFT46]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[KCTD18]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZSCAN21]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[COQ5]] | +0.60 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[GIN1]] | +0.60 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[ZXDA]] | +0.60 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[MDM2]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[FRG1BP]] | +0.57 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[TAB3]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PHYH]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARP2]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ARPC5L]] | -0.55 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[PGP]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | -0.54 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[RAB5IF]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[HIRA]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[VKORC1L1]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SLC27A4]] | -0.52 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[TRAPPC4]] | -0.51 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[NFATC2IP]] | -0.51 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[RTL10]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[SRGAP2C]] | -0.51 | -0.55 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OGFRL1]] | B | OGFRL1 activity raises AMZ2P1's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without OGFRL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[NGFR]] | B | NGFR activity raises AMZ2P1's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.20× lower at baseline in the lines without NGFR | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[DCP1B]] | C | DCP1B activity raises AMZ2P1's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.9, 6.6); signed map (7.2, -23.0). **Vector** length 50.2, 5.84% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.8 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -2.6 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.3 | -4.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.0 | -0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | AMZ2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 17q24.1 — chr17:64,968,222-64,973,517 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ32065 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26491) · Entrez [201283](https://www.ncbi.nlm.nih.gov/gene/201283) · Ensembl [ENSG00000214174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214174)

## Data

Gene col 13179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13179); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13179]; `tensor/DDL_lfc|DDL_z.npy` [13179]; `embed/gene_vectors.npy` [13179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13179 or target_col == 13179). Every well: [[AMZ2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMZ2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
