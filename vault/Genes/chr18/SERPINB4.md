---
symbol: "SERPINB4"
type: "gene"
col: 13031
ensembl_id: "ENSG00000206073"
name: "serpin family B member 4"
location: "18q21.33"
module: 155
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 11
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# SERPINB4

*serpin family B member 4* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.86× (z +8.7, q 2e-15, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.27× (z +5.2, q 2e-05, up in 8 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.00279×, CFPAC-1 0.0252×); [[Selinexor (drug)]] 5 µM in 1 line (BT-474 0.0120×; ⚠ cell-cycle shift, explains ~21% of this change); [[Filgotinib (drug)]] 5 µM in 1 line (BT-474 0.00205×); [[Tofacitinib (drug)]] 0.5 µM in 1 line (BT-474 0.00290×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB3]] (+0.98, fdr 7e-06, ⚠ same locus), [[FGB]] (+0.84, fdr 7e-06), [[S100A9]] (+0.84, fdr 7e-06), [[S100A8]] (+0.78, fdr 7e-06); moves opposite to [[PGR]] (-0.49, fdr 4e-05), [[ANKRD30A]] (-0.42, fdr 4e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SERPINB3]] → it (grade C ⚠); 14 go from it, the strongest it → [[LINC01348]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.86×** | +8.7 | 2e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.08×** | +8.1 | 1e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.19×** | +6.9 | 1e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +5.2 | 2e-05 | 8/9 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +4.9 | 9e-05 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.22×** | +4.7 | 3e-04 | 1/4 (A549) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.83×** | +4.3 | 0.001 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.57×** | +4.3 | 0.001 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.47×** | +4.1 | 0.003 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +4.0 | 0.003 | 6/8 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.9 | 0.004 | 0/7 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.27×** | +3.7 | 0.011 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.68×** | +3.2 | 0.059 | 1/4 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.2 | 0.059 | 0/8 | top dose only | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.64×** | +3.2 | 0.059 | 0/8 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **2.09×** | +3.1 | 0.075 | 1/7 (NCI-H1792) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 20 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.00279×, CFPAC-1 0.0252×); [[Selinexor (drug)]] 5 µM in 1 line (BT-474 0.0120×; ⚠ cell-cycle shift, explains ~21% of this change); [[Filgotinib (drug)]] 5 µM in 1 line (BT-474 0.00205×); [[Tofacitinib (drug)]] 0.5 µM in 1 line (BT-474 0.00290×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.494× | -3.2 | 0.59 | 1/9 (BT-474) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.278× | -3.0 | 0.59 | 2/9 (BT-474, HT-29) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 84.1 | 0 | 42 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00279× (z -21.5) |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0252× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0259× (z -11.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A549 (line)]] | wt | 3.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0501× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 2.77 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.0623× (z -8.8) |
| [[A-172 (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.143 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.127 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.160 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.150 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.175 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.135 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.158 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.146 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 0.664 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.129 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.158 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.165 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB3]] | +0.98 | +0.98 / +0.98 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (10.9 kb, same strand: neighbours can correlate without regulation) |
| [[FGB]] | +0.84 | +0.78 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.84 | +0.80 / +0.84 | both halves | 7e-06 | STRING 486 |
| [[S100A8]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 | STRING 436 |
| [[LINC01440]] | +0.73 | +0.79 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GSDMC]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[C2CD4A]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LINC02015]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FLRT3]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[FGG]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CES1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ADAM28]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TCIM]] | +0.61 | +0.62 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ANKRD30A]] | -0.42 | -0.25 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB3]] | C | SERPINB3 activity raises SERPINB4's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.68× lower at baseline in the lines without SERPINB3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises SERPINB4's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.27× lower at baseline in the lines without TMEM163 | 0.039 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[CP]] | C | CP activity raises SERPINB4's level | lines that do not express CP (39) vs lines expressing it (11) | 1.67× lower at baseline in the lines without CP | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |
| [[LINC02015]] | C | LINC02015 activity raises SERPINB4's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without LINC02015 | 0.073 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01348]] | B | SERPINB4 activity raises LINC01348's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.12× lower at baseline in the lines without SERPINB4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9 |
| [[LURAP1]] | B | SERPINB4 activity raises LURAP1's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 1.56× lower at baseline in the lines without SERPINB4 | 0.079 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9 |
| [[SERPINB3]] | C | SERPINB4 activity raises SERPINB3's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 4.33× lower at baseline in the lines without SERPINB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[TMC5]] | C | SERPINB4 activity raises TMC5's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 3.23× lower at baseline in the lines without SERPINB4 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[TSPAN1]] | C | SERPINB4 activity raises TSPAN1's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.87× lower at baseline in the lines without SERPINB4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[TMEM163]] | C | SERPINB4 activity raises TMEM163's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 3.02× lower at baseline in the lines without SERPINB4 | 0.016 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[MUC5AC]] | C | SERPINB4 activity raises MUC5AC's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 4.03× lower at baseline in the lines without SERPINB4 | 0.019 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[ADAM28]] | C | SERPINB4 activity raises ADAM28's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 3.92× lower at baseline in the lines without SERPINB4 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[PDZK1IP1]] | C | SERPINB4 activity raises PDZK1IP1's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without SERPINB4 | 0.033 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[SERPINB7]] | C | SERPINB4 activity raises SERPINB7's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.62× lower at baseline in the lines without SERPINB4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[ST8SIA6]] | C | SERPINB4 activity raises ST8SIA6's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.81× lower at baseline in the lines without SERPINB4 | 0.089 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[CP]] | C | SERPINB4 activity raises CP's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.97× lower at baseline in the lines without SERPINB4 | 0.092 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.907). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, 48.3); signed map (54.6, 23.6). **Vector** length 62.1, 28.9% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.79 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.79 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.79 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Isocorydine (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,637,259-63,644,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PI11, LEUPIN, SCCA-2, SCCA1; previously SCCA2 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Matched by | ensembl_id |

**Function**, from UniProt [P48594](https://www.uniprot.org/uniprotkb/P48594) (Serpin B4):

> May act as a protease inhibitor to modulate the host immune response against tumor cells.

**Summary**, from NCBI Gene [6318](https://www.ncbi.nlm.nih.gov/gene/6318):

> The protein encoded by this gene is a member of the serpin family of serine protease inhibitors. The encoded protein is highly expressed in many tumor cells and can inactivate granzyme M, an enzyme that kills tumor cells. This protein, along with serpin B3, can be processed into smaller fragments that aggregate to form an autoantigen in psoriasis, probably by causing chronic inflammation. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:10570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10570) · Entrez [6318](https://www.ncbi.nlm.nih.gov/gene/6318) · UniProt [P48594](https://www.uniprot.org/uniprotkb/P48594) · Ensembl [ENSG00000206073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206073)

## Data

Gene col 13031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13031); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13031]; `tensor/DDL_lfc|DDL_z.npy` [13031]; `embed/gene_vectors.npy` [13031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13031 or target_col == 13031). Every well: [[SERPINB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
