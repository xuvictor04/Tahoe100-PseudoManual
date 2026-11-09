---
symbol: "A1BG-AS1"
type: "gene"
col: 15610
ensembl_id: "ENSG00000268895"
name: "A1BG antisense RNA 1"
location: "19q13.43"
module: 3
arm: "+"
pooled_cpm: 4.85
n_lines_expressing: 32
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# A1BG-AS1

*A1BG antisense RNA 1* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.80× (z +10.8, q 2e-24, up in 28 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.656× (z -4.4, q 0.005, down in 14 of 29 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.505× (z -3.8, q 0.044, down in 8 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.173×, HS-578T 0.179×, PANC-1 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0808×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.205×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.64, fdr 4e-05), [[PSMD9]] (+0.62, fdr 4e-05), [[MEX3D]] (+0.61, fdr 3e-05); moves opposite to [[AKAP11]] (-0.57, fdr 1e-05), [[CCT7]] (-0.55, fdr 3e-05), [[SEPTIN11]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[SUMO3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.80×** | +10.8 | 2e-24 | 28/29 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.49×** | +9.6 | 4e-19 | 25/28 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +9.4 | 1e-18 | 23/28 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.6 | 3e-06 | 9/21 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +5.5 | 4e-06 | 14/23 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.4 | 0.001 | 12/29 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.006 | 5/25 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.053 | 1/25 (SW 900) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.074 | 4/29 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.23× | +3.1 | 0.11 | 7/25 (PANC-1, RKO, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.34× | +3.1 | 0.11 | 8/26 (NCI-H460, RPMI-7951, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.34× | +3.1 | 0.11 | 2/28 (HOP62, A-172) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.50× | +3.0 | 0.11 | 2/25 (NCI-H2347, SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.173×, HS-578T 0.179×, PANC-1 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0808×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.205×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.656×** | -4.4 | 0.005 | 14/29 (HepG2/C3A, BT-474, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -3.8 | 0.044 | 8/27 (A-172, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.7 | 0.044 | 9/29 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -3.5 | 0.057 | 11/25 (A-172, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.742× | -3.2 | 0.18 | 7/29 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.727× | -3.1 | 0.18 | 5/23 (PANC-1, H4, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 8.45 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.83× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 6.70 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0808× (z -10.7) |
| [[A-427 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.743 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.64 | +0.40 / +0.64 | both halves | 4e-05 |  |
| [[PSMD9]] | +0.62 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[MEX3D]] | +0.61 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[A1BG]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[BRI3]] | +0.60 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZNF611]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ATG4B]] | +0.59 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | +0.58 | +0.45 / +0.59 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SIRT7]] | +0.58 | +0.32 / +0.59 | both halves | 1e-04 |  |
| [[MIGA2]] | +0.57 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[DUSP18]] | +0.57 | +0.32 / +0.59 | both halves | 1e-04 |  |
| [[ENDOV]] | +0.56 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[SELENOO]] | +0.56 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[TIMM29]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CCT7]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.55 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[SUCLG2]] | -0.55 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[PNPO]] | -0.53 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[TWF1]] | -0.52 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[PFKM]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.52 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[PAICS]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[CBX5]] | -0.51 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[MRPL30]] | -0.51 | -0.29 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers A1BG-AS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[A1BG]] | C | A1BG activity raises A1BG-AS1's level | lines that do not express A1BG (17) vs lines expressing it (33) | 3.79× lower at baseline in the lines without A1BG | 0.012 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1; co-absent with the target |
| [[GLIS1]] | C | GLIS1 activity raises A1BG-AS1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.89× lower at baseline in the lines without GLIS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUMO3]] | B | A1BG-AS1 activity lowers SUMO3's level | lines that do not express A1BG-AS1 (18) vs lines expressing it (32) | 1.10× higher at baseline in the lines without A1BG-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: A1BG, DZIP1, RNF150 |
| [[A1BG]] | C | A1BG-AS1 activity raises A1BG's level | lines that do not express A1BG-AS1 (18) vs lines expressing it (32) | 3.39× lower at baseline in the lines without A1BG-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: A1BG, DZIP1, RNF150; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.5, -18.1); signed map (-26.8, 8.0). **Vector** length 43.1, 7.18% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +1.6 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.6 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +10.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.5 | +9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -3.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Folic acid (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | A1BG antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.43 — chr19:58,347,718-58,355,455 (+) |
| Ensembl biotype | lncRNA |
| Also known as | A1BGAS1, FLJ23569; previously NCRNA00181, A1BGAS, A1BG-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37133) · Entrez [503538](https://www.ncbi.nlm.nih.gov/gene/503538) · Ensembl [ENSG00000268895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268895)

## Data

Gene col 15610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15610); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15610]; `tensor/DDL_lfc|DDL_z.npy` [15610]; `embed/gene_vectors.npy` [15610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15610 or target_col == 15610). Every well: [[A1BG-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A1BG-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
