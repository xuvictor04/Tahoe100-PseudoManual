---
symbol: "TSTD1"
type: "gene"
col: 13278
ensembl_id: "ENSG00000215845"
name: "thiosulfate sulfurtransferase like domain containing 1"
location: "1q23.3"
module: 58
arm: "+"
pooled_cpm: 10.75
n_lines_expressing: 31
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TSTD1

*thiosulfate sulfurtransferase like domain containing 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +6.9, q 3e-09, up in 23 of 24 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 10.2×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.382× (z -8.2, q 2e-13, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNNI3]] (+0.74, fdr 7e-06), [[GCHFR]] (+0.72, fdr 7e-06), [[MIEN1]] (+0.71, fdr 1e-05); moves opposite to [[EWSR1]] (-0.61, fdr 3e-05), [[PSMD11]] (-0.60, fdr 1e-05), [[PSMC3]] (-0.59, fdr 1e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GCHFR]] → it (grade C ⚠); 4 go from it, the strongest it → [[TRPT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13278.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 10.2×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +6.9 | 3e-09 | 23/24 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.35×** | +4.8 | 4e-04 | 14/17 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.95×** | +4.1 | 0.009 | 18/27 (J82, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.382×** | -8.2 | 2e-13 | 23/27 (SW 900, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -5.5 | 1e-05 | 23/26 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.499×** | -3.9 | 0.016 | 19/27 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -3.8 | 0.021 | 17/29 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -3.6 | 0.038 | 20/28 (BT-474, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.300×** | -3.5 | 0.038 | 22/28 (LS 180, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.558×** | -3.5 | 0.039 | 19/27 (SNU-423, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -3.2 | 0.089 | 16/29 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.572×** | -3.2 | 0.098 | 13/27 (LS 180, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.350× | -3.1 | 0.11 | 18/27 (SHP-77, A498, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 0.351× | -3.1 | 0.11 | 15/29 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.34 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0685× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 57.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -12.9) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -8.9) |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -14.4) |
| [[A-172 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNNI3]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GCHFR]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.71 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.71 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TMEM191A-1]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.67 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[DCTN6-DT]] | +0.67 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[NDUFA3]] | +0.67 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[LAGE3]] | +0.66 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[NDUFA2]] | +0.66 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[DPM3]] | +0.65 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CYBA]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[PSMD11]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[PSMC3]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[PDAP1]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[WASH8P]] ⚠ | -0.59 | -0.42 / -0.58 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[U2AF2]] | -0.59 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[EIF4G2]] | -0.58 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[CAPRIN1]] | -0.57 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[CCT7]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PSME3]] | -0.57 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[ILF3]] | -0.57 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MCM3AP]] | -0.57 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCHFR]] | C | GCHFR activity raises TSTD1's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without GCHFR | 0.024 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent; co-absent with the target |
| [[CRB3]] | C | CRB3 activity raises TSTD1's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 3.49× lower at baseline in the lines without CRB3 | 0.038 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPT1]] | B | TSTD1 activity raises TRPT1's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without TSTD1 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12 |
| [[AFAP1-AS1]] | B | TSTD1 activity raises AFAP1-AS1's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without TSTD1 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12 |
| [[ADGRL3-AS1]] | B | TSTD1 activity raises ADGRL3-AS1's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 1.00× lower at baseline in the lines without TSTD1 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12 |
| [[DNAJA4]] | C | TSTD1 activity raises DNAJA4's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 2.93× lower at baseline in the lines without TSTD1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12; co-absent with the target |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.3, -17.5); signed map (-31.8, 6.6). **Vector** length 51.5, 15.2% of its response variance represented; |z| ≥ 3 in 334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | -0.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | thiosulfate sulfurtransferase like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,037,631-161,038,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KAT |
| Reactome | 4 pathways, smallest: Sulfide oxidation to sulfate; Degradation of cysteine and homocysteine; Sulfur amino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFU3](https://www.uniprot.org/uniprotkb/Q8NFU3) (Thiosulfate:glutathione sulfurtransferase):

> Thiosulfate:glutathione sulfurtransferase (TST) required to produce S-sulfanylglutathione (GSS(-)), a central intermediate in hydrogen sulfide metabolism. Provides the link between the first step in mammalian H(2)S metabolism performed by the sulfide:quinone oxidoreductase (SQOR) which catalyzes the conversion of H(2)S to thiosulfate, and the sulfur dioxygenase (SDO) which uses GSS(-) as substrate. The thermodynamic coupling of the irreversible SDO and reversible TST reactions provides a model …

**Summary**, from NCBI Gene [100131187](https://www.ncbi.nlm.nih.gov/gene/100131187):

> Predicted to enable thiosulfate-thiol sulfurtransferase activity. Predicted to be involved in sulfide oxidation, using sulfide:quinone oxidoreductase. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:35410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35410) · Entrez [100131187](https://www.ncbi.nlm.nih.gov/gene/100131187) · UniProt [Q8NFU3](https://www.uniprot.org/uniprotkb/Q8NFU3) · Ensembl [ENSG00000215845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215845)

## Data

Gene col 13278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13278); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13278]; `tensor/DDL_lfc|DDL_z.npy` [13278]; `embed/gene_vectors.npy` [13278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13278 or target_col == 13278). Every well: [[TSTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
