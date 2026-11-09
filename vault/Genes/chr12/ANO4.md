---
symbol: "ANO4"
type: "gene"
col: 7536
ensembl_id: "ENSG00000151572"
name: "anoctamin 4"
location: "12q23.1"
module: 27
arm: "+"
pooled_cpm: 8.43
n_lines_expressing: 20
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ANO4

*anoctamin 4* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.11× (z +29.6, q 0e+00, up in 9 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.207×, J82 0.406×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.112×, SK-MEL-2 0.227×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.157×, J82 0.257×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.131×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.64, fdr 1e-05), [[OPRD1]] (+0.63, fdr 3e-05), [[FGF19]] (+0.61, fdr 1e-05); moves opposite to [[RIN2]] (-0.41, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[DKK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.11×** | +29.6 | 0e+00 | 9/13 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.86×** | +25.8 | 0e+00 | 5/13 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.33×** | +13.8 | 6e-41 | 12/16 (NCI-H1573, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +11.5 | 3e-28 | 3/13 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.58×** | +11.0 | 7e-26 | 7/14 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.52×** | +10.7 | 2e-24 | 3/13 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +10.5 | 6e-24 | 0/5 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +10.3 | 6e-23 | 6/16 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +10.2 | 1e-22 | 0/5 | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +9.9 | 4e-21 | 1/8 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +9.7 | 2e-20 | 5/11 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.2 | 2e-14 | 5/16 (HEC-1-A, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +7.7 | 5e-13 | 9/14 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +5.2 | 9e-06 | 5/17 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.7 | 8e-05 | 1/11 (SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.015 | 3/12 (A-427, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.024 | 1/10 (HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.034 | 0/14 | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.039 | 3/16 (HOP62, CHP-212, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.207×, J82 0.406×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.112×, SK-MEL-2 0.227×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.157×, J82 0.257×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.741× | -3.5 | 0.10 | 2/17 (CHP-212, H4) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.745× | -3.4 | 0.10 | 4/15 (A-427, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.700× | -3.4 | 0.10 | 2/16 (H4, RPMI-7951) | inconsistent across doses | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 5 µM |  | 0.752× | -3.3 | 0.10 | 3/17 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.752× | -3.3 | 0.10 | 2/16 (J82, SK-MEL-2) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.825× | -3.2 | 0.13 | 2/17 (SNU-423, J82) | all doses, flat | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.17 | 0/15 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.9 | 0 | 16 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0681× (z -14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.6) |
| [[J82 (line)]] | alt | 149 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 86.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 2.21 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 18.8× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[OPRD1]] | +0.63 | +0.44 / +0.51 | both halves | 3e-05 | **novel candidate** |
| [[FGF19]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PSG1]] | +0.57 | +0.65 / +0.24 | both halves | 4e-04 | **novel candidate** |
| [[VWA2]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[JAKMIP2-AS1]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[GJB1]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ST18]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[TRPV4]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 | pathway: Ion channel transport |
| [[EPB41L4A]] | +0.56 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[F10]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIN2]] | -0.41 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANO4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACNA2D4]] | B | CACNA2D4 activity raises ANO4's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without CACNA2D4 | 0.076 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[PSG1]] | C | PSG1 activity raises ANO4's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 4.61× lower at baseline in the lines without PSG1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[SHISA9]] | C | SHISA9 activity raises ANO4's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without SHISA9 | 0.023 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises ANO4's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.31× lower at baseline in the lines without FKBP9P1-1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[SDK1]] | C | SDK1 activity raises ANO4's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without SDK1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises ANO4's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 1.91× lower at baseline in the lines without KRT5 | 0.044 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises ANO4's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.64× lower at baseline in the lines without MIR3667HG | 0.053 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[F5]] | C | F5 activity raises ANO4's level | lines that do not express F5 (39) vs lines expressing it (11) | 1.33× lower at baseline in the lines without F5 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[EPB41L4A]] | C | EPB41L4A activity raises ANO4's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.53× lower at baseline in the lines without EPB41L4A | 0.067 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P; co-absent with the target |
| [[LINC00923]] | C | LINC00923 activity raises ANO4's level | lines that do not express LINC00923 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without LINC00923 | 0.069 | ⚠ within organs, on part of the lines; also absent: TM4SF4, SLC25A24P1, ENSG00000283633; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DKK2]] | B | ANO4 activity raises DKK2's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without ANO4 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[LINC03042]] | B | ANO4 activity raises LINC03042's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without ANO4 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[SLIT1]] | B | ANO4 activity raises SLIT1's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.56× lower at baseline in the lines without ANO4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[PKHD1]] | B | ANO4 activity raises PKHD1's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.27× lower at baseline in the lines without ANO4 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[PHACTR3]] | B | ANO4 activity raises PHACTR3's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.01× lower at baseline in the lines without ANO4 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[NELL2]] | C | ANO4 activity raises NELL2's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 3.91× lower at baseline in the lines without ANO4 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[EPB41L4A]] | C | ANO4 activity raises EPB41L4A's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without ANO4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | ANO4 activity raises CSMD3's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 3.24× lower at baseline in the lines without ANO4 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[SMOC2]] | C | ANO4 activity raises SMOC2's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without ANO4 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[APCDD1]] | C | ANO4 activity raises APCDD1's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ANO4 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[SCN5A]] | C | ANO4 activity raises SCN5A's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without ANO4 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[PWWP3B]] | C | ANO4 activity raises PWWP3B's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without ANO4 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 42.4); signed map (64.3, 16.6). **Vector** length 46.1, 11.4% of its response variance represented; |z| ≥ 3 in 454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +29.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +10.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[vincristine (drug)]] 5 µM |  | +1.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,717,526-101,128,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34221, FLJ34272, FLJ35277; previously TMEM16D |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 8 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32M45](https://www.uniprot.org/uniprotkb/Q32M45) (Anoctamin-4):

> Has calcium-dependent phospholipid scramblase activity; scrambles phosphatidylserine, phosphatidylcholine and galactosylceramide (By similarity). Does not exhibit calcium-activated chloride channel (CaCC) activity (By similarity).

**Summary**, from NCBI Gene [121601](https://www.ncbi.nlm.nih.gov/gene/121601):

> Enables intracellularly calcium-gated chloride channel activity. Involved in chloride transmembrane transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23837) · Entrez [121601](https://www.ncbi.nlm.nih.gov/gene/121601) · UniProt [Q32M45](https://www.uniprot.org/uniprotkb/Q32M45) · Ensembl [ENSG00000151572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151572)

## Data

Gene col 7536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7536); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7536]; `tensor/DDL_lfc|DDL_z.npy` [7536]; `embed/gene_vectors.npy` [7536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7536 or target_col == 7536). Every well: [[ANO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
