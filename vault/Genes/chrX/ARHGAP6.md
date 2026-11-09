---
symbol: "ARHGAP6"
type: "gene"
col: 523
ensembl_id: "ENSG00000047648"
name: "Rho GTPase activating protein 6"
location: "Xp22.2"
module: 73
arm: "+"
pooled_cpm: 17.64
n_lines_expressing: 18
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 13
direction_downstream: 14
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# ARHGAP6

*Rho GTPase activating protein 6* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +18.1, q 0e+00, up in 10 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.708× (z -4.1, q 0.020, down in 1 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.122×, KATO III 0.324×); [[Panobinostat (drug)]] 5 µM in 2 lines (LS 180 0.0865×, KATO III 0.111×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.182×, KATO III 0.179×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.161×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.222×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP10B]] (+0.63, fdr 7e-06), [[LDLRAD4]] (+0.62, fdr 1e-05), [[CD200]] (+0.61, fdr 2e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[EDNRB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +18.1 | 0e+00 | 10/15 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +13.3 | 7e-38 | 1/10 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +11.1 | 4e-26 | 10/16 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +9.5 | 4e-19 | 1/10 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.3 | 2e-18 | 2/13 (BT-474, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +7.6 | 3e-12 | 8/15 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +7.1 | 8e-11 | 7/13 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.1 | 9e-11 | 9/16 (SNU-423, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.7 | 1e-09 | 5/14 (A498, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +5.0 | 4e-05 | 6/15 (NCI-H2030, A-427, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 7e-05 | 4/16 (CHP-212, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.6 | 2e-04 | 2/12 (SNU-423, BT-474) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.5 | 3e-04 | 8/15 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.3 | 7e-04 | 3/12 (A-172, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.011 | 0/15 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.048 | 2/15 (BT-474, NCI-H2030) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.048 | 4/15 (A-172, A498, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.066 | 0/15 | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +3.0 | 0.090 | 4/15 (hTERT-HPNE, A-172, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 523.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.122×, KATO III 0.324×); [[Panobinostat (drug)]] 5 µM in 2 lines (LS 180 0.0865×, KATO III 0.111×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.182×, KATO III 0.179×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.161×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.222×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.708×** | -4.1 | 0.020 | 1/15 (C32) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.756×** | -3.6 | 0.081 | 7/15 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -3.4 | 0.14 | 1/16 (H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 264 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -24.4) |
| [[KATO III (line)]] | alt | 116 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -11.4) |
| [[C32 (line)]] | wt | 112 | 0 | 5 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0770× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.122× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 7.06 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.16× (z +9.8) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0887× (z -9.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 14.5 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +12.5) | — |
| [[A-427 (line)]] | wt | 4.53 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.20× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.136× (z -8.8) |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 4.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +9.8) | — |
| [[A-172 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP10B]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LDLRAD4]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 | same gene group |
| [[CD200]] | +0.61 | +0.59 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[LEF1-AS1]] | +0.56 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SAMMSON]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PLEKHS1]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[MIR3681HG]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CADPS]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[FLT1]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[MUC17]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[NPSR1]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARHGAP6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPON1]] | C | SPON1 activity raises ARHGAP6's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.06× lower at baseline in the lines without SPON1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises ARHGAP6's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without UGT1A1 | 0.039 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises ARHGAP6's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.60× lower at baseline in the lines without EDNRB | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises ARHGAP6's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.75× lower at baseline in the lines without TPTEP1-1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises ARHGAP6's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 3.69× lower at baseline in the lines without MUC17 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises ARHGAP6's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.35× lower at baseline in the lines without LINC02474 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises ARHGAP6's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.38× lower at baseline in the lines without CFTR | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises ARHGAP6's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.05× lower at baseline in the lines without AGR3 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises ARHGAP6's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.54× lower at baseline in the lines without DSG4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises ARHGAP6's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.25× lower at baseline in the lines without UGT1A6 | 0.068 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[CD200]] | C | CD200 activity raises ARHGAP6's level | lines that do not express CD200 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CD200 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, DSCAM, SIGLEC15; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDNRB]] | C | ARHGAP6 activity raises EDNRB's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without ARHGAP6 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[DAAM2]] | C | ARHGAP6 activity raises DAAM2's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.76× lower at baseline in the lines without ARHGAP6 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[COL19A1]] | C | ARHGAP6 activity raises COL19A1's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without ARHGAP6 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[GPA33]] | C | ARHGAP6 activity raises GPA33's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.15× lower at baseline in the lines without ARHGAP6 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[CD200]] | C | ARHGAP6 activity raises CD200's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without ARHGAP6 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[CADPS]] | C | ARHGAP6 activity raises CADPS's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.21× lower at baseline in the lines without ARHGAP6 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[IGFL2]] | C | ARHGAP6 activity raises IGFL2's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.15× lower at baseline in the lines without ARHGAP6 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[HEPH]] | C | ARHGAP6 activity raises HEPH's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.32× lower at baseline in the lines without ARHGAP6 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[AEBP1]] | C | ARHGAP6 activity raises AEBP1's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without ARHGAP6 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[LEF1-AS1]] | C | ARHGAP6 activity raises LEF1-AS1's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.48× lower at baseline in the lines without ARHGAP6 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[SPON1]] | C | ARHGAP6 activity raises SPON1's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.16× lower at baseline in the lines without ARHGAP6 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[ATP10B]] | C | ARHGAP6 activity raises ATP10B's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.26× lower at baseline in the lines without ARHGAP6 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 58.1); signed map (67.2, 2.4). **Vector** length 51.1, 14.3% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +7.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +0.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:11,117,651-11,665,920 (-) |
| Ensembl biotype | protein_coding |
| Also known as | rhoGAPX-1 |
| Gene groups (HGNC) | Rho GTPase activating proteins; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: RAC3 GTPase cycle; RHOA GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O43182](https://www.uniprot.org/uniprotkb/O43182) (Rho GTPase-activating protein 6):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state. Could regulate the interactions of signaling molecules with the actin cytoskeleton. Promotes continuous elongation of cytoplasmic processes during cell motility and simultaneous retraction of the cell body changing the cell morphology.

**Summary**, from NCBI Gene [395](https://www.ncbi.nlm.nih.gov/gene/395):

> This gene encodes a member of the rhoGAP family of proteins which play a role in the regulation of actin polymerization at the plasma membrane during several cellular processes. This protein is thought to have two independent functions, one as a GTPase-activating protein with specificity for RhoA, and another as a cytoskeletal protein that promotes actin remodeling. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:676) · Entrez [395](https://www.ncbi.nlm.nih.gov/gene/395) · UniProt [O43182](https://www.uniprot.org/uniprotkb/O43182) · Ensembl [ENSG00000047648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047648)

## Data

Gene col 523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 523); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 523]; `tensor/DDL_lfc|DDL_z.npy` [523]; `embed/gene_vectors.npy` [523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 523 or target_col == 523). Every well: [[ARHGAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
