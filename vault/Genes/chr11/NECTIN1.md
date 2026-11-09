---
symbol: "NECTIN1"
type: "gene"
col: 3135
ensembl_id: "ENSG00000110400"
name: "nectin cell adhesion molecule 1"
location: "11q23.3"
module: 34
arm: "+"
pooled_cpm: 24.03
n_lines_expressing: 42
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# NECTIN1

*nectin cell adhesion molecule 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +19.5, q 0e+00, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.561× (z -4.7, q 0.002, down in 14 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.191×, AsPC-1 0.304×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.198×); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.190×; ⚠ cell-cycle shift, explains ~41% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.278×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3PXD2A]] (+0.66, fdr 1e-05), [[EFNB1]] (+0.65, fdr 7e-06), [[SOX13]] (+0.61, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KIAA0040]] → it (grade B ⚠); 8 go from it, the strongest it → [[TGFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +19.5 | 0e+00 | 22/37 (Panc 03.27, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +15.9 | 0e+00 | 22/36 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.32×** | +13.3 | 6e-38 | 28/39 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.01×** | +11.0 | 4e-26 | 19/40 (NCI-H2030, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +11.0 | 4e-26 | 25/40 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +9.6 | 6e-20 | 26/37 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.1 | 8e-18 | 22/40 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +9.1 | 8e-18 | 20/39 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.75×** | +8.8 | 8e-17 | 20/40 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +5.9 | 3e-07 | 12/39 (SW480, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +4.8 | 8e-05 | 8/40 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.37×** | +4.8 | 8e-05 | 11/37 (C32, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.5 | 3e-04 | 9/28 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 3e-04 | 12/40 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.30×** | +4.0 | 0.003 | 9/32 (HEC-1-A, RPMI-7951, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.004 | 4/40 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.040 | 7/35 (SW480, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.075 | 5/40 (LS 180, HEC-1-A, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.078 | 8/38 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.090 | 2/35 (RKO, HEC-1-A) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3135.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.191×, AsPC-1 0.304×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.198×); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.190×; ⚠ cell-cycle shift, explains ~41% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.278×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.561×** | -4.7 | 0.002 | 14/32 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.4 | 0.12 | 2/40 (HOP62, HCT15) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.810× | -3.4 | 0.12 | 9/38 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.811× | -3.3 | 0.12 | 8/38 (KATO III, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.817× | -3.2 | 0.13 | 15/38 (SW480, A-172, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.820× | -3.2 | 0.13 | 9/38 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | 0.855× | -3.2 | 0.13 | 9/38 (C-33 A, CHP-212, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.760× | -3.1 | 0.13 | 8/37 (AsPC-1, C32, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.829× | -3.0 | 0.17 | 15/38 (KATO III, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 92.1 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.6) |
| [[Hs 766T (line)]] | wt | 186 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 12.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.37× (z +9.2) ⚠ cell-cycle shift, explains ~41% of this change | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.255× (z -8.6) ⚠ toxic |
| [[A498 (line)]] | wt | 6.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +11.8) | — |
| [[KATO III (line)]] | alt | 60.6 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.317× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 35.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +17.8) | — |
| [[SW480 (line)]] | alt | 34.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.107× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.65× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 45.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.6) | — |
| [[RKO (line)]] | wt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0842× (z -8.6) |
| [[SW 900 (line)]] | alt | 6.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 54.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.9) | — |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2A]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[EFNB1]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SOX13]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[NGEF]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[GRK5]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[IGSF9B]] | +0.54 | +0.47 / +0.46 | both halves | 2e-05 | same gene group |
| [[PLK3]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SDC1]] | +0.52 | +0.46 / +0.55 | both halves | 2e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0040]] | B | KIAA0040 activity raises NECTIN1's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.90× lower at baseline in the lines without KIAA0040 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[MAOB]] | B | MAOB activity raises NECTIN1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 3.09× lower at baseline in the lines without MAOB | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[SERPINB5]] | B | SERPINB5 activity raises NECTIN1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without SERPINB5 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[PCDH1]] | B | PCDH1 activity raises NECTIN1's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without PCDH1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[ANO1]] | B | ANO1 activity raises NECTIN1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without ANO1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[SLC52A3]] | B | SLC52A3 activity raises NECTIN1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without SLC52A3 | 0.047 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[PKP1]] | B | PKP1 activity raises NECTIN1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without PKP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[LINC00659]] | B | LINC00659 activity raises NECTIN1's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without LINC00659 | 0.060 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[LYPD3]] | B | LYPD3 activity raises NECTIN1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without LYPD3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[FERMT1]] | B | FERMT1 activity raises NECTIN1's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without FERMT1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFA]] | B | NECTIN1 activity raises TGFA's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 4.29× lower at baseline in the lines without NECTIN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[LYPD3]] | B | NECTIN1 activity raises LYPD3's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.06× lower at baseline in the lines without NECTIN1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[KIAA0040]] | B | NECTIN1 activity raises KIAA0040's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 3.82× lower at baseline in the lines without NECTIN1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[GSKIP]] | B | NECTIN1 activity raises GSKIP's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without NECTIN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[PCDH1]] | B | NECTIN1 activity raises PCDH1's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without NECTIN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[EPHB3]] | B | NECTIN1 activity raises EPHB3's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.72× lower at baseline in the lines without NECTIN1 | 0.066 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[SLC52A3]] | B | NECTIN1 activity raises SLC52A3's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without NECTIN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[LSR]] | B | NECTIN1 activity raises LSR's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 3.86× lower at baseline in the lines without NECTIN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, 49.3); signed map (-0.2, 40.7). **Vector** length 92.4, 21.1% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +19.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.3 | -1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.0 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nectin cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,623,408-119,729,200 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRR, PRR1, PVRR1, SK-12, HIgR, CLPED1, CD111, OFC7; previously HVEC, ED4, PVRL1 |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: Nectin/Necl  trans heterodimerization; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15223](https://www.uniprot.org/uniprotkb/Q15223) (Nectin-1):

> Cell adhesion molecule that promotes cell-cell contacts and plays important roles in the development of the nervous system. Acts by forming homophilic or heterophilic trans-dimers. Heterophilic interactions have been detected between NECTIN1 and NECTIN3 and between NECTIN1 and NECTIN4 (By similarity). Involved in axon guidance by promoting contacts between the commissural axons and the floor plate cells (By similarity). Involved in synaptogegesis (By similarity). Has some neurite …

**Summary**, from NCBI Gene [5818](https://www.ncbi.nlm.nih.gov/gene/5818):

> This gene encodes an adhesion protein that plays a role in the organization of adherens junctions and tight junctions in epithelial and endothelial cells. The protein is a calcium(2+)-independent cell-cell adhesion molecule that belongs to the immunoglobulin superfamily and has 3 extracellular immunoglobulin-like loops, a single transmembrane domain (in some isoforms), and a cytoplasmic region. This protein acts as a receptor for glycoprotein D (gD) of herpes simplex viruses 1 and 2 (HSV-1, …

**Accessions** — [HGNC:9706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9706) · Entrez [5818](https://www.ncbi.nlm.nih.gov/gene/5818) · UniProt [Q15223](https://www.uniprot.org/uniprotkb/Q15223) · Ensembl [ENSG00000110400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110400)

## Data

Gene col 3135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3135); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3135]; `tensor/DDL_lfc|DDL_z.npy` [3135]; `embed/gene_vectors.npy` [3135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3135 or target_col == 3135). Every well: [[NECTIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECTIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
