---
symbol: "FGF14"
type: "gene"
col: 2250
ensembl_id: "ENSG00000102466"
name: "fibroblast growth factor 14"
location: "13q33.1"
module: 108
arm: "+"
pooled_cpm: 26.44
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 14
direction_downstream: 6
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# FGF14

*fibroblast growth factor 14* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +12.2, q 3e-31, up in 5 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.614× (z -5.0, q 3e-04, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH10]] (+0.76, fdr 7e-06), [[KCNH5]] (+0.76, fdr 7e-06), [[TCF4]] (+0.70, fdr 7e-06).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[PDE4D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +12.2 | 3e-31 | 5/20 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +10.1 | 1e-21 | 6/17 (RPMI-7951, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +6.3 | 6e-08 | 2/16 (NCI-H23, NCI-H1792) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.9 | 5e-07 | 7/20 (C32, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +5.6 | 2e-06 | 6/20 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.4 | 5e-06 | 2/14 (J82, NCI-H1792) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 4/20 (SW 900, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.025 | 2/20 (C32, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.039 | 6/19 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.046 | 5/20 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.054 | 5/20 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.34× | +3.0 | 0.12 | 1/20 (HOP62) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -5.0 | 3e-04 | 15/20 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -4.6 | 0.001 | 14/20 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.651×** | -4.4 | 0.002 | 12/19 (A-427, NCI-H460, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.738×** | -4.4 | 0.002 | 13/20 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.540× | -3.3 | 0.11 | 11/20 (NCI-H1573, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.727× | -3.3 | 0.11 | 9/20 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.739× | -3.1 | 0.15 | 11/20 (A-427, NCI-H460, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.740× | -3.1 | 0.15 | 9/19 (A-427, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 136 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.1) |
| [[SHP-77 (line)]] | alt | 666 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0450× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0896× (z -12.5) |
| [[CHP-212 (line)]] | wt | 97.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0235× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H1573 (line)]] | alt | 57.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0763× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 45.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 2 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0355× (z -13.6) |
| [[C32 (line)]] | wt | 7.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[J82 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW 900 (line)]] | alt | 43.9 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -9.7) |
| [[A-172 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH10]] | +0.76 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[KCNH5]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TCF4]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LGSN]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ADARB2]] | +0.68 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SCN2A]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Cardiac conduction; STRING 771 |
| [[MGAT4C]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[SLITRK5]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[PDE4B]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[LINC01035]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CDH12]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LINC02197]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FGF14's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TCF4]] | C | TCF4 activity raises FGF14's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.95× lower at baseline in the lines without TCF4 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[NOL4]] | C | NOL4 activity raises FGF14's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 3.98× lower at baseline in the lines without NOL4 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[EDARADD]] | C | EDARADD activity raises FGF14's level | lines that do not express EDARADD (26) vs lines expressing it (24) | 3.07× lower at baseline in the lines without EDARADD | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000239268, NOL4, ASXL3; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises FGF14's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.03× lower at baseline in the lines without LINC02492 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises FGF14's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 7.48× lower at baseline in the lines without NETO1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises FGF14's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.64× lower at baseline in the lines without KCNH5 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises FGF14's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without NKAIN2 | 0.048 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises FGF14's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 3.12× lower at baseline in the lines without ASXL3 | 0.053 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[ACSS3]] | C | ACSS3 activity raises FGF14's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without ACSS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[GRIA2]] | C | GRIA2 activity raises FGF14's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 4.34× lower at baseline in the lines without GRIA2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[EYA2]] | C | EYA2 activity raises FGF14's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without EYA2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4D]] | B | FGF14 activity raises PDE4D's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without FGF14 | 0.088 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2 |
| [[LGSN]] | C | FGF14 activity raises LGSN's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without FGF14 | 0.048 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[TBX18]] | C | FGF14 activity raises TBX18's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 4.69× lower at baseline in the lines without FGF14 | 0.053 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[NKAIN3]] | C | FGF14 activity raises NKAIN3's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without FGF14 | 0.075 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[PTPRD]] | C | FGF14 activity raises PTPRD's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 6.09× lower at baseline in the lines without FGF14 | 0.076 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[EYA2]] | C | FGF14 activity raises EYA2's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 2.87× lower at baseline in the lines without FGF14 | 0.094 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 33.3); signed map (40.5, 36.7). **Vector** length 73.2, 26.1% of its response variance represented; |z| ≥ 3 in 477 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | -0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | +0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:101,710,804-102,402,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FHF4, SCA27 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Fibroblast growth factor family |
| Reactome | 3 pathways, smallest: Phase 0 - rapid depolarisation; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92915](https://www.uniprot.org/uniprotkb/Q92915) (Fibroblast growth factor 14):

> Probably involved in nervous system development and function.

**Summary**, from NCBI Gene [2259](https://www.ncbi.nlm.nih.gov/gene/2259):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth and invasion. A mutation in this gene is associated with autosomal dominant cerebral ataxia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul …

**Accessions** — [HGNC:3671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3671) · Entrez [2259](https://www.ncbi.nlm.nih.gov/gene/2259) · UniProt [Q92915](https://www.uniprot.org/uniprotkb/Q92915) · Ensembl [ENSG00000102466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102466)

## Data

Gene col 2250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2250); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2250]; `tensor/DDL_lfc|DDL_z.npy` [2250]; `embed/gene_vectors.npy` [2250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2250 or target_col == 2250). Every well: [[FGF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
