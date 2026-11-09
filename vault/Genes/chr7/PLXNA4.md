---
symbol: "PLXNA4"
type: "gene"
col: 13309
ensembl_id: "ENSG00000221866"
name: "plexin A4"
location: "7q32.3"
module: 165
arm: "+"
pooled_cpm: 4.81
n_lines_expressing: 41
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# PLXNA4

*plexin A4* — 7q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.54× (z +23.6, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.675× (z -4.3, q 0.009, down in 10 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (HOP62 0.438×, NCI-H1792 0.356×; ⚠ position not correctable); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0704×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Peretinoin (drug)]] 5 µM in 1 line (A-172 0.107×); [[Auranofin (drug)]] 0.05 µM in 1 line (A498 0.0666×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0344×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZPLD1]] (+0.69, fdr 1e-05), [[PECAM1]] (+0.69, fdr 7e-06), [[RELN]] (+0.67, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CAVIN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.54×** | +23.6 | 0e+00 | 22/26 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +15.4 | 0e+00 | 13/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +14.1 | 1e-42 | 2/7 (A498, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.63×** | +10.7 | 2e-24 | 16/32 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +9.9 | 4e-21 | 2/8 (SHP-77, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +9.2 | 4e-18 | 4/14 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +8.6 | 6e-16 | 11/27 (A549, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +8.6 | 7e-16 | 20/37 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +7.2 | 5e-11 | 11/29 (A498, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +7.1 | 6e-11 | 10/28 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.8 | 5e-10 | 4/36 (NCI-H460, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +6.7 | 1e-09 | 8/29 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.1 | 2e-05 | 7/21 (A498, H4, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.3 | 8e-04 | 3/17 (SNU-423, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.1 | 0.001 | 1/8 (A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.011 | 4/21 (NCI-H460, A-172, …) | all doses, flat | low cells (technical?) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.023 | 2/21 (Hs 766T, HOP62) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.024 | 5/31 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.061 | 2/20 (HOP62, C32) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.088 | 5/34 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13309.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (HOP62 0.438×, NCI-H1792 0.356×; ⚠ position not correctable); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0704×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Peretinoin (drug)]] 5 µM in 1 line (A-172 0.107×); [[Auranofin (drug)]] 0.05 µM in 1 line (A498 0.0666×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0344×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.675×** | -4.3 | 0.009 | 10/31 (SHP-77, J82, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.791×** | -3.7 | 0.058 | 6/35 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.793×** | -3.6 | 0.058 | 12/35 (Panc 03.27, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.759× | -3.0 | 0.31 | 9/32 (BT-474, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.87 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +10.6) | [[Peretinoin (drug)]] 5 µM 0.107× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.5) | — |
| [[A498 (line)]] | wt | 1.85 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0666× (z -8.8) |
| [[A549 (line)]] | wt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 5.76 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.438× (z -10.4) ⚠ position not correctable |
| [[J82 (line)]] | alt | 10.3 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.127× (z -8.5) |
| [[LoVo (line)]] | wt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.356× (z -10.2) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 5.44 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0344× (z -8.6) |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.988 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZPLD1]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[PECAM1]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RELN]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[RERGL]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[FGF1]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[GRM8]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SLC4A10]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NTNG2]] | +0.61 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ZNF385D]] | +0.61 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[CSMD2]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLXNA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01287]] | B | LINC01287 activity raises PLXNA4's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.38× lower at baseline in the lines without LINC01287 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[FRMPD4]] | B | FRMPD4 activity raises PLXNA4's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without FRMPD4 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[ADAMTSL1]] | B | ADAMTSL1 activity raises PLXNA4's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without ADAMTSL1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[SNCAIP]] | B | SNCAIP activity raises PLXNA4's level | lines that do not express SNCAIP (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without SNCAIP | 0.078 | ⚠ within organs, on part of the lines; also absent: LIMCH1, RNF152, FLT1 |
| [[SETBP1]] | B | SETBP1 activity raises PLXNA4's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without SETBP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3 |
| [[PAEP]] | B | PAEP activity raises PLXNA4's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without PAEP | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAVIN4]] | B | PLXNA4 activity raises CAVIN4's level | lines that do not express PLXNA4 (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without PLXNA4 | 0.087 | ⚠ within organs, on part of the lines; also absent: ASAP3, PRDM6, PRKAR2B; maybe low, not absent |
| [[SCHIP1]] | B | PLXNA4 activity raises SCHIP1's level | lines that do not express PLXNA4 (9) vs lines expressing it (41) | 2.54× lower at baseline in the lines without PLXNA4 | 0.091 | ⚠ within organs, on part of the lines; also absent: ASAP3, PRDM6, PRKAR2B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.9, 31.1); signed map (31.7, 17.3). **Vector** length 54.6, 8.76% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +23.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.3 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.8 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | plexin A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.3 — chr7:132,123,340-132,648,688 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1550, DKFZp434G0625PRO34003, FAYV2820; previously PLXNA4A, PLXNA4B |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Reactome | 9 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; CRMPs in Sema3A signaling; Other semaphorin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCM2](https://www.uniprot.org/uniprotkb/Q9HCM2) (Plexin-A4):

> Coreceptor for SEMA3A. Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance in the developing nervous system. Class 3 semaphorins bind to a complex composed of a neuropilin and a plexin. The plexin modulates the affinity of the complex for specific semaphorins, and its cytoplasmic domain is required for the activation of down-stream signaling events in the cytoplasm (By similarity).

**Summary**, from NCBI Gene [91584](https://www.ncbi.nlm.nih.gov/gene/91584):

> Predicted to enable semaphorin receptor activity. Predicted to be involved in nervous system development; regulation of cell migration; and semaphorin-plexin signaling pathway. Predicted to act upstream of or within nervous system development; regulation of axon extension involved in axon guidance; and regulation of negative chemotaxis. Predicted to be located in membrane. Predicted to be part of semaphorin receptor complex. Predicted to be active in plasma membrane. [provided by Alliance of …

**Accessions** — [HGNC:9102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9102) · Entrez [91584](https://www.ncbi.nlm.nih.gov/gene/91584) · UniProt [Q9HCM2](https://www.uniprot.org/uniprotkb/Q9HCM2) · Ensembl [ENSG00000221866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221866)

## Data

Gene col 13309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13309); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13309]; `tensor/DDL_lfc|DDL_z.npy` [13309]; `embed/gene_vectors.npy` [13309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13309 or target_col == 13309). Every well: [[PLXNA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
