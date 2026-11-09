---
symbol: "DUSP7"
type: "gene"
col: 8861
ensembl_id: "ENSG00000164086"
name: "dual specificity phosphatase 7"
location: "3p21.2"
module: 141
arm: "+"
pooled_cpm: 6.79
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# DUSP7

*dual specificity phosphatase 7* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.85× (z +7.9, q 1e-12, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.614× (z -5.9, q 2e-06, down in 18 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOWAHC]] (+0.61, fdr 1e-05), [[PLXNA1]] (+0.58, fdr 3e-05), [[ARHGDIA]] (+0.57, fdr 2e-05); moves opposite to [[SEM1]] (-0.55, fdr 3e-05), [[SNX13]] (-0.55, fdr 6e-05), [[EFCAB7]] (-0.55, fdr 1e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01204]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +7.9 | 1e-12 | 24/38 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.54×** | +7.8 | 1e-12 | 20/39 (C32, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.58×** | +5.8 | 1e-06 | 18/45 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.8 | 1e-06 | 11/31 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.2 | 3e-05 | 17/45 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.46×** | +4.9 | 1e-04 | 14/32 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.5 | 5e-04 | 15/42 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.3 | 0.001 | 8/39 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.1 | 0.002 | 13/40 (A549, SW48, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.33×** | +3.6 | 0.015 | 13/46 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.34×** | +3.6 | 0.015 | 11/33 (AsPC-1, A-172, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.31×** | +3.4 | 0.032 | 12/45 (A-427, HEC-1-A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.064 | 6/37 (Hs 766T, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -5.9 | 2e-06 | 18/42 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -5.3 | 3e-05 | 16/46 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -5.2 | 4e-05 | 14/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -5.1 | 6e-05 | 16/44 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.481×** | -4.9 | 9e-05 | 15/36 (AsPC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.753×** | -4.4 | 0.001 | 13/44 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.727×** | -4.1 | 0.003 | 9/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.727×** | -4.1 | 0.003 | 10/43 (LS 180, SHP-77, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.731×** | -3.9 | 0.006 | 17/42 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.815×** | -3.6 | 0.016 | 9/47 (Hs 766T, MIA PaCa-2, …) | all doses, flat |  |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.051 | 8/41 (A549, HOP62, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.778×** | -3.3 | 0.051 | 6/41 (SHP-77, SW 900, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (drug)]] 5 µM |  | 0.838× | -3.2 | 0.051 | 6/46 (SHP-77, HCT15, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.781×** | -3.2 | 0.057 | 9/46 (AsPC-1, MIA PaCa-2, …) | two highest doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.629×** | -3.1 | 0.067 | 7/42 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Capmatinib (drug)]] 5 µM |  | **0.637×** | -3.0 | 0.084 | 4/33 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.789×** | -2.9 | 0.099 | 8/43 (H4, HOP62, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.797×** | -2.9 | 0.099 | 5/42 (J82, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 5 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.450× (z -15.6) ⚠ position not correctable · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.209× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.240× (z -9.1) |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0578× (z -8.7) |
| [[KATO III (line)]] | alt | 3.80 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0752× (z -9.2) |
| [[LS 180 (line)]] | wt | 4.19 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0544× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0919× (z -8.6) |
| [[A498 (line)]] | wt | 4.73 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0790× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 6.96 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0710× (z -9.0) |
| [[LoVo (line)]] | wt | 4.48 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0491× (z -12.6) |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOWAHC]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PLXNA1]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ARHGDIA]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CAPRIN2]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[BMP2K]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SPRY4]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[EHD1]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[RIN1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MFSD2A]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[PXN]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TOR4A]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEM1]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 | pathway: MAPK family signaling cascades |
| [[SNX13]] | -0.55 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[EFCAB7]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CSDE1]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[UBE4B]] | -0.54 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CEP126]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RNPC3]] | -0.52 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[FAM151B-DT]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[CWF19L2]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZNF148]] | -0.51 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[PFDN5]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RABGAP1]] | -0.50 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01204]] | B | LINC01204 activity raises DUSP7's level | lines that do not express LINC01204 (22) vs lines expressing it (28) | 1.56× lower at baseline in the lines without LINC01204 | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC00460, WNT5A, LNCOG; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises DUSP7's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 5.3); signed map (6.9, 46.3). **Vector** length 72.7, 11.6% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.3 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | +2.8 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +1.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.9 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:52,048,919-52,056,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MKP-X, PYST2 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Reactome | 36 pathways, smallest: Signaling by MAPK mutants; ERKs are inactivated; ERK/MAPK targets |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16829](https://www.uniprot.org/uniprotkb/Q16829) (Dual specificity protein phosphatase 7):

> Dual specificity protein phosphatase. Shows high activity towards MAPK1/ERK2. Also has lower activity towards MAPK14 and MAPK8. In arrested oocytes, plays a role in meiotic resumption (By similarity). Promotes nuclear envelope breakdown and activation of the CDK1/Cyclin-B complex in oocytes, probably by dephosphorylating and inactivating the conventional protein kinase C (cPKC) isozyme PRKCB (By similarity). May also inactivate PRKCA and/or PRKCG (By similarity). Also important in oocytes for …

**Summary**, from NCBI Gene [1849](https://www.ncbi.nlm.nih.gov/gene/1849):

> Dual-specificity phosphatases (DUSPs) constitute a large heterogeneous subgroup of the type I cysteine-based protein-tyrosine phosphatase superfamily. DUSPs are characterized by their ability to dephosphorylate both tyrosine and serine/threonine residues. DUSP7 belongs to a class of DUSPs, designated MKPs, that dephosphorylate MAPK (mitogen-activated protein kinase) proteins ERK (see MIM 601795), JNK (see MIM 601158), and p38 (see MIM 600289) with specificity distinct from that of individual …

**Accessions** — [HGNC:3073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3073) · Entrez [1849](https://www.ncbi.nlm.nih.gov/gene/1849) · UniProt [Q16829](https://www.uniprot.org/uniprotkb/Q16829) · Ensembl [ENSG00000164086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164086)

## Data

Gene col 8861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8861); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8861]; `tensor/DDL_lfc|DDL_z.npy` [8861]; `embed/gene_vectors.npy` [8861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8861 or target_col == 8861). Every well: [[DUSP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
