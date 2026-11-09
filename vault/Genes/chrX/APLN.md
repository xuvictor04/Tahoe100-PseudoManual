---
symbol: "APLN"
type: "gene"
col: 10100
ensembl_id: "ENSG00000171388"
name: "apelin"
location: "Xq26.1"
module: 103
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 37
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 18
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# APLN

*apelin* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.32× (z +8.7, q 2e-15, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +6.6, q 1e-08, up in 8 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.496× (z -7.4, q 6e-11, down in 22 of 25 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRN1]] (+0.53, fdr 1e-05), [[PIAS2]] (+0.52, fdr 2e-05), [[NOG]] (+0.52, fdr 1e-04); moves opposite to [[BAG1]] (-0.52, fdr 4e-05), [[ATP9B]] (-0.50, fdr 5e-05), [[TBL1X]] (-0.47, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01967]] → it (grade B ⚠); 18 go from it, the strongest it → [[TMEM39B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +8.7 | 2e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.6 | 1e-08 | 8/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.11×** | +5.6 | 3e-06 | 4/12 (Hs 766T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.4 | 1e-05 | 8/31 (Hs 766T, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +4.6 | 4e-04 | 2/9 (NCI-H460, SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +4.4 | 9e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.091 | 3/29 (NCI-H1792, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.55× | +3.0 | 0.16 | 5/17 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, none with an alert; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.496×** | -7.4 | 6e-11 | 22/25 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.411×** | -6.7 | 7e-09 | 16/20 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.420×** | -6.3 | 7e-08 | 20/30 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.442×** | -5.8 | 1e-06 | 16/26 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.467×** | -5.7 | 1e-06 | 19/31 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -5.6 | 2e-06 | 16/29 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.495×** | -5.3 | 1e-05 | 14/29 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.524×** | -4.9 | 9e-05 | 13/31 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.528×** | -4.8 | 1e-04 | 16/32 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -4.6 | 3e-04 | 13/33 (SNU-423, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.339×** | -4.2 | 0.001 | 16/30 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.584×** | -4.0 | 0.003 | 12/24 (PANC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.369×** | -3.9 | 0.004 | 7/26 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -3.7 | 0.008 | 13/27 (HOP62, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.724×** | -3.4 | 0.023 | 8/30 (NCI-H2030, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0227× (z -19.8) |
| [[RPMI-7951 (line)]] | alt | 7.84 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -12.9) |
| [[HOP62 (line)]] | alt | 6.44 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0553× (z -12.6) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0850× (z -10.5) |
| [[SW480 (line)]] | alt | 5.85 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0676× (z -13.9) |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0694× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0617× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 4.67 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0491× (z -9.1) |
| [[SNU-423 (line)]] | alt | 2.87 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0437× (z -8.7) |
| [[A-172 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.962 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.658 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.663 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.740 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRN1]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NOG]] | +0.52 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[SPAG4]] | +0.52 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[ISM2]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PPFIA4]] | +0.50 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[CA9]] | +0.50 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[SMAP2]] | +0.49 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[TMEM74B]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CRABP2]] | +0.48 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[CHSY1]] | +0.48 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[DIPK2A]] | +0.48 | +0.35 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAG1]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ATP9B]] | -0.50 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[TBL1X]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SPIRE2]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[RABGAP1L]] | -0.45 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PATJ]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PHYKPL]] | -0.42 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[DTNBP1]] | -0.41 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ATF6]] | -0.41 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[RMC1]] | -0.41 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[C11orf96]] | -0.41 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[LRRC28]] | -0.41 | -0.33 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01967]] | B | LINC01967 activity raises APLN's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 2.16× lower at baseline in the lines without LINC01967 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1 |
| [[FAM13C]] | B | FAM13C activity raises APLN's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without FAM13C | 0.009 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[FENDRR]] | B | FENDRR activity raises APLN's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 1.85× lower at baseline in the lines without FENDRR | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[NRN1]] | B | NRN1 activity raises APLN's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without NRN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[LRRC34]] | B | LRRC34 activity raises APLN's level | lines that do not express LRRC34 (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without LRRC34 | 0.066 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises APLN's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, GSK1059615, Rapamycin, Temsirolimus) | 50% of the class's compounds vs 4.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds |
| [[C11orf96]] | B | C11orf96 activity raises APLN's level | lines that do not express C11orf96 (17) vs lines expressing it (33) | 1.46× lower at baseline in the lines without C11orf96 | 0.079 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, ZNF569, PPP1R3C |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM39B]] | B | APLN activity raises TMEM39B's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without APLN | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[INAFM2]] | B | APLN activity raises INAFM2's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without APLN | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RABGAP1L]] | B | APLN activity lowers RABGAP1L's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.43× higher at baseline in the lines without APLN | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[R3HDM4]] | B | APLN activity lowers R3HDM4's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without APLN | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAP30-DT]] | B | APLN activity raises SAP30-DT's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.16× lower at baseline in the lines without APLN | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FAM13C]] | B | APLN activity raises FAM13C's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.77× lower at baseline in the lines without APLN | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[COL13A1]] | B | APLN activity raises COL13A1's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.42× lower at baseline in the lines without APLN | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TENT5A]] | B | APLN activity raises TENT5A's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without APLN | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CHSY1]] | B | APLN activity raises CHSY1's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without APLN | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NRN1]] | B | APLN activity raises NRN1's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without APLN | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM45A]] | B | APLN activity raises TMEM45A's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without APLN | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PIAS2]] | B | APLN activity raises PIAS2's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without APLN | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.7, -19.2); signed map (-30.9, 34.0). **Vector** length 50.9, 8.90% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | apelin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:129,645,259-129,654,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | apelin, XNPEP2 |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULZ1](https://www.uniprot.org/uniprotkb/Q9ULZ1) (Apelin):

> Peptide hormone that functions as endogenous ligand for the G protein-coupled apelin receptor (APLNR/APJ), that plays a role in cadiovascular homeostasis. Functions as a balanced agonist activating both G(i) protein pathway and beta-arrestin pathway of APLNR. Downstream G proteins activation, apelin can inhibit cAMP production and activate key intracellular effectors such as ERKs. On the other hand, APLNR activation induces beta-arrestin recruitment to the membrane leading to desensitization …

**Summary**, from NCBI Gene [8862](https://www.ncbi.nlm.nih.gov/gene/8862):

> This gene encodes a peptide that functions as an endogenous ligand for the G-protein coupled apelin receptor. The encoded preproprotein is proteolytically processed into biologically active C-terminal peptide fragments. These peptide fragments activate different tissue specific signaling pathways that regulate diverse biological functions including fluid homeostasis, cardiovascular function and insulin secretion. This protein also functions as a coreceptor for the human immunodeficiency virus …

**Accessions** — [HGNC:16665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16665) · Entrez [8862](https://www.ncbi.nlm.nih.gov/gene/8862) · UniProt [Q9ULZ1](https://www.uniprot.org/uniprotkb/Q9ULZ1) · Ensembl [ENSG00000171388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171388)

## Data

Gene col 10100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10100); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10100]; `tensor/DDL_lfc|DDL_z.npy` [10100]; `embed/gene_vectors.npy` [10100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10100 or target_col == 10100). Every well: [[APLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
