---
symbol: "GPRIN3"
type: "gene"
col: 11682
ensembl_id: "ENSG00000185477"
name: "GPRIN family member 3"
location: "4q22.1"
module: 19
arm: "+"
pooled_cpm: 31.82
n_lines_expressing: 15
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 12
direction_downstream: 23
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GPRIN3

*GPRIN family member 3* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.92× (z +8.8, q 1e-15, up in 8 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.339× (z -10.2, q 1e-21, down in 12 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK4]] (+0.69, fdr 7e-06), [[SMOC1]] (+0.66, fdr 7e-06), [[LINC01508]] (+0.65, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PDE10A]] → it (grade B ⚠); 23 go from it, the strongest it → [[SFMBT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +8.8 | 1e-15 | 8/13 (A498, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.0 | 3e-13 | 1/12 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +7.6 | 6e-12 | 2/11 (LoVo, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.008 | 8/13 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +3.9 | 0.010 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.8 | 0.015 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.50×** | +3.6 | 0.027 | 4/13 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.061 | 7/13 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.339×** | -10.2 | 1e-21 | 12/13 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.553×** | -7.9 | 9e-13 | 12/13 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.515×** | -6.2 | 8e-08 | 10/13 (A549, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -6.0 | 2e-07 | 13/13 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -5.6 | 2e-06 | 8/13 (A549, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.561×** | -5.4 | 5e-06 | 10/13 (A498, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.610×** | -4.7 | 3e-04 | 8/13 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -4.4 | 7e-04 | 9/13 (SHP-77, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.411×** | -4.4 | 8e-04 | 11/13 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.631×** | -4.2 | 0.002 | 10/13 (C32, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.656×** | -4.0 | 0.004 | 10/13 (A498, C32, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.456×** | -3.9 | 0.005 | 10/13 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.666×** | -3.8 | 0.006 | 10/13 (C32, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.012 | 12/13 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.590×** | -3.5 | 0.015 | 0/13 | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.688×** | -3.5 | 0.016 | 10/13 (C32, LS 180, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.494×** | -3.5 | 0.017 | 12/13 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.689×** | -3.4 | 0.023 | 8/13 (CFPAC-1, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 231 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -26.9) |
| [[NCI-H460 (line)]] | wt | 297 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0340× (z -26.6) |
| [[A549 (line)]] | wt | 230 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -19.0) |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0974× (z -11.7) |
| [[C32 (line)]] | wt | 31.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -14.9) |
| [[A498 (line)]] | wt | 13.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0304× (z -17.7) |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.121× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0978× (z -8.7) |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0688× (z -9.7) |
| [[LoVo (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.8) |
| [[A-172 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK4]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SMOC1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC01508]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CPS1]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LIN7A]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GTF2I-AS1]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ADGRD1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[TARID]] | +0.62 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[WDR72]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[LINC01035]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TRPA1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE10A]] | B | PDE10A activity raises GPRIN3's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without PDE10A | 0.079 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[NRCAM]] | C | NRCAM activity raises GPRIN3's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 4.28× lower at baseline in the lines without NRCAM | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[SPP1]] | C | SPP1 activity raises GPRIN3's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 3.54× lower at baseline in the lines without SPP1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises GPRIN3's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.05× lower at baseline in the lines without DPP10 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[FGG]] | C | FGG activity raises GPRIN3's level | lines that do not express FGG (42) vs lines expressing it (8) | 4.79× lower at baseline in the lines without FGG | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises GPRIN3's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.59× lower at baseline in the lines without LIN7A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[SMOC1]] | C | SMOC1 activity raises GPRIN3's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 3.61× lower at baseline in the lines without SMOC1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[PDK4]] | C | PDK4 activity raises GPRIN3's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.64× lower at baseline in the lines without PDK4 | 0.053 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA; co-absent with the target |
| [[LAMB4]] | C | LAMB4 activity raises GPRIN3's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.74× lower at baseline in the lines without LAMB4 | 0.054 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[GDA]] | C | GDA activity raises GPRIN3's level | lines that do not express GDA (35) vs lines expressing it (15) | 2.18× lower at baseline in the lines without GDA | 0.062 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises GPRIN3's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 4.02× lower at baseline in the lines without GLP2R | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises GPRIN3's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without NCKAP5-AS2 | 0.097 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 7, C 16. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFMBT2]] | B | GPRIN3 activity raises SFMBT2's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without GPRIN3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[PBX1]] | B | GPRIN3 activity raises PBX1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.82× lower at baseline in the lines without GPRIN3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[PDE4D]] | B | GPRIN3 activity raises PDE4D's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without GPRIN3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[SLC39A8]] | B | GPRIN3 activity raises SLC39A8's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without GPRIN3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[SPTLC3]] | B | GPRIN3 activity raises SPTLC3's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 1.21× lower at baseline in the lines without GPRIN3 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[PDE10A]] | B | GPRIN3 activity raises PDE10A's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without GPRIN3 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[TMEM178B]] | B | GPRIN3 activity raises TMEM178B's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.42× lower at baseline in the lines without GPRIN3 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[CACNB2]] | C | GPRIN3 activity raises CACNB2's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 4.15× lower at baseline in the lines without GPRIN3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[SPP1]] | C | GPRIN3 activity raises SPP1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 4.02× lower at baseline in the lines without GPRIN3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[PLA2G4A]] | C | GPRIN3 activity raises PLA2G4A's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.45× lower at baseline in the lines without GPRIN3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[CLDN10-AS1]] | C | GPRIN3 activity raises CLDN10-AS1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.13× lower at baseline in the lines without GPRIN3 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[TARID]] | C | GPRIN3 activity raises TARID's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without GPRIN3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 37.6); signed map (44.8, 43.7). **Vector** length 74.0, 30.7% of its response variance represented; |z| ≥ 3 in 514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.9 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -6.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | GPRIN family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:89,236,383-89,307,937 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRIN3, FLJ42625 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZVF9](https://www.uniprot.org/uniprotkb/Q6ZVF9) (G protein-regulated inducer of neurite outgrowth 3):

> May be involved in neurite outgrowth.

**Summary**, from NCBI Gene [285513](https://www.ncbi.nlm.nih.gov/gene/285513):

> Predicted to be involved in neuron projection development. Predicted to act upstream of or within several processes, including excitatory chemical synaptic transmission; neuronal action potential; and vitamin D receptor signaling pathway. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:27733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27733) · Entrez [285513](https://www.ncbi.nlm.nih.gov/gene/285513) · UniProt [Q6ZVF9](https://www.uniprot.org/uniprotkb/Q6ZVF9) · Ensembl [ENSG00000185477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185477)

## Data

Gene col 11682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11682); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11682]; `tensor/DDL_lfc|DDL_z.npy` [11682]; `embed/gene_vectors.npy` [11682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11682 or target_col == 11682). Every well: [[GPRIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
