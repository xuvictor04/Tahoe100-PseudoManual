---
symbol: "CHST10"
type: "gene"
col: 3690
ensembl_id: "ENSG00000115526"
name: "carbohydrate sulfotransferase 10"
location: "2q11.2"
module: 33
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 38
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# CHST10

*carbohydrate sulfotransferase 10* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +6.8, q 8e-09, up in 14 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.385× (z -14.1, q 1e-42, down in 22 of 27 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.560× (z -8.6, q 3e-15, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF692]] (+0.73, fdr 7e-06), [[FXN]] (+0.69, fdr 7e-06), [[ASB13]] (+0.68, fdr 1e-05); moves opposite to [[TSPAN31]] (-0.60, fdr 1e-05), [[ZCWPW2]] (-0.54, fdr 5e-05), [[PPP1R11]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 2 go from it, the strongest it → [[TMSB15B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.8 | 8e-09 | 14/34 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +6.2 | 1e-07 | 14/34 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.49×** | +5.9 | 7e-07 | 7/34 (NCI-H2347, SW480, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.8 | 1e-06 | 8/15 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +4.8 | 2e-04 | 9/34 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +4.6 | 3e-04 | 3/34 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.1 | 0.004 | 3/15 (J82, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.44×** | +3.8 | 0.010 | 8/34 (HOP62, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.86×** | +3.4 | 0.045 | 0/7 | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.3 | 0.060 | 0/9 | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +3.2 | 0.061 | 1/26 (HOP62) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.066 | 8/32 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.086 | 4/34 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.091 | 7/29 (PANC-1, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.385×** | -14.1 | 1e-42 | 22/27 (PANC-1, J82, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -8.6 | 3e-15 | 19/26 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -6.5 | 1e-08 | 12/25 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -6.4 | 3e-08 | 10/28 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.592×** | -5.3 | 2e-05 | 16/32 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.650×** | -4.5 | 6e-04 | 13/34 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -4.1 | 0.003 | 8/23 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -3.9 | 0.007 | 10/34 (H4, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.025 | 11/21 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.532×** | -3.4 | 0.032 | 7/31 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -3.1 | 0.087 | 7/28 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.731×** | -3.1 | 0.092 | 8/31 (CFPAC-1, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.86 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -19.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -12.9) |
| [[J82 (line)]] | alt | 3.69 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Valdecoxib (drug)]] 0.5 µM 0.0903× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 6.53 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 5.96 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 4.06 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 2.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.10 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.05 µM 0.0626× (z -9.3) |
| [[A-427 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.895 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF692]] | +0.73 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[FXN]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ASB13]] | +0.68 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.67 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.66 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[AADAT]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ZNF232]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ZFP69]] | +0.65 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[PACC1]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PTPN20]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NLE1]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN31]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ZCWPW2]] | -0.54 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PPP1R11]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[DLEU7]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[USP49]] | -0.53 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[LINC01135]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[KDM4C]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TTC41P]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ALOX12-AS1]] | -0.52 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[FANK1]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[MAP3K20-AS1]] | -0.52 | -0.46 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises CHST10's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without GNAZ | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises CHST10's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[TOP2A]] | B | TOP2A activity raises CHST10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRAME]] | B | PRAME activity raises CHST10's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without PRAME | 0.019 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[LAMC3]] | B | LAMC3 activity raises CHST10's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without LAMC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[RASGEF1A]] | B | RASGEF1A activity raises CHST10's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without RASGEF1A | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[ARHGEF25]] | C | ARHGEF25 activity raises CHST10's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without ARHGEF25 | 0.012 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises CHST10's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.49× lower at baseline in the lines without VASH1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[FAM124A]] | C | FAM124A activity raises CHST10's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without FAM124A | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMSB15B]] | B | CHST10 activity raises TMSB15B's level | lines that do not express CHST10 (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without CHST10 | 0.062 | ⚠ within organs, on part of the lines; also absent: SNRPN, DNAAF9, ENSG00000268163; its own permutation p |
| [[ARHGEF25]] | C | CHST10 activity raises ARHGEF25's level | lines that do not express CHST10 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without CHST10 | 0.062 | ⚠ within organs, on part of the lines; also absent: SNRPN, DNAAF9, ENSG00000268163; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-36.9, 23.6); signed map (-8.8, -53.7). **Vector** length 50.8, 7.92% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.9 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.6 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.0 | -14.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.0 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -8.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:100,391,860-100,417,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HNK-1ST |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 7 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; Matriglycan biosynthesis on DAG1; DAG1 glycosylations |
| Matched by | ensembl_id |

**Function**, from UniProt [O43529](https://www.uniprot.org/uniprotkb/O43529) (Carbohydrate sulfotransferase 10):

> Catalyzes the transfer of sulfate from 3'-phosphoadenylyl sulfate (PAPS) to position 3 of terminal glucuronic acid of both protein- and lipid-linked oligosaccharides. Participates in biosynthesis of HNK-1 carbohydrate structure 3-O-sulfo-beta-D-GlcA-(1->3)-beta-D-Gal-(1->4)-D-GlcNAc-R, a sulfated glucuronyl-lactosaminyl residue carried by many neural recognition molecules, which is involved in cell interactions during ontogenetic development and in synaptic plasticity in the adult. May be …

**Summary**, from NCBI Gene [9486](https://www.ncbi.nlm.nih.gov/gene/9486):

> This protein encoded by this gene transfers sulfate to the C-3 hydroxyl of terminal glucuronic acid of protein- and lipid-linked oligosaccharides. This protein was first identified as a sulfotransferase that acts on the human natural killer-1 (HNK-1) glycan; HNK-1 is a carbohydrate involved in neurodevelopment and synaptic plasticity.[provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:19650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19650) · Entrez [9486](https://www.ncbi.nlm.nih.gov/gene/9486) · UniProt [O43529](https://www.uniprot.org/uniprotkb/O43529) · Ensembl [ENSG00000115526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115526)

## Data

Gene col 3690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3690); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3690]; `tensor/DDL_lfc|DDL_z.npy` [3690]; `embed/gene_vectors.npy` [3690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3690 or target_col == 3690). Every well: [[CHST10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
