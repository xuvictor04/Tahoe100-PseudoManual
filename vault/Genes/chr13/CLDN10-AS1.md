---
symbol: "CLDN10-AS1"
type: "gene"
col: 13338
ensembl_id: "ENSG00000223392"
name: "CLDN10 antisense RNA 1"
location: "13q32.1"
module: 19
arm: "+"
pooled_cpm: 9.88
n_lines_expressing: 19
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 15
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CLDN10-AS1

*CLDN10 antisense RNA 1* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +12.5, q 4e-33, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.376× (z -7.5, q 5e-11, down in 11 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHC4]] (+0.65, fdr 7e-06), [[CLDN10]] (+0.64, fdr 7e-06, ⚠ same locus), [[PLAC4]] (+0.64, fdr 1e-05), [[DUSP4]] (+0.63, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[CHN2]] → it (grade B ⚠); 12 go from it, the strongest it → [[CLDN10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +12.5 | 4e-33 | 2/15 (HEC-1-A, PANC-1) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +8.9 | 2e-16 | 1/13 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +6.9 | 1e-09 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +5.5 | 6e-06 | 6/15 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +4.1 | 0.004 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.1 | 0.005 | 5/15 (HepG2/C3A, SW 900, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.048 | 2/16 (SHP-77, HepG2/C3A) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.2 | 0.083 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.28× | +3.0 | 0.17 | 1/15 (HT-29) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, none with an alert; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.376×** | -7.5 | 5e-11 | 11/15 (SHP-77, C32, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.463×** | -6.3 | 6e-08 | 13/15 (SHP-77, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.529×** | -5.9 | 6e-07 | 12/15 (SHP-77, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -5.9 | 6e-07 | 12/15 (NCI-H1792, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.503×** | -5.5 | 5e-06 | 11/16 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.519×** | -5.4 | 6e-06 | 13/16 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.566×** | -4.7 | 2e-04 | 12/15 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -4.4 | 8e-04 | 10/15 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.636×** | -4.2 | 0.002 | 11/16 (SHP-77, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.682×** | -4.0 | 0.003 | 11/15 (SHP-77, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.632×** | -3.8 | 0.008 | 12/15 (SHP-77, C32, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.728×** | -3.6 | 0.013 | 6/15 (SHP-77, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.648×** | -3.6 | 0.016 | 3/16 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -3.3 | 0.033 | 10/15 (NCI-H460, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.666×** | -3.3 | 0.033 | 13/16 (SHP-77, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 168 | 0 | 28 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -24.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.0261× (z -24.2) |
| [[SW 900 (line)]] | alt | 139 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -20.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0553× (z -15.7) |
| [[C32 (line)]] | wt | 20.2 | 0 | 12 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0301× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 33.7 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0318× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0236× (z -17.1) |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0167× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 4.65 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0592× (z -8.6) |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHC4]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CLDN10]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PLAC4]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[DUSP4]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GTF2IP7]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[RHOH]] | +0.63 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[ZG16B]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SERPIND1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ETV4]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PAK3]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SERPINB11]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 4, C 11. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHN2]] | B | CHN2 activity raises CLDN10-AS1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without CHN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises CLDN10-AS1's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without GTF2IP7 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[FST]] | B | FST activity raises CLDN10-AS1's level | lines that do not express FST (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without FST | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2 |
| [[MAP2K1]] | B | MAP2K1 activity raises CLDN10-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[DPP10]] | C | DPP10 activity raises CLDN10-AS1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.51× lower at baseline in the lines without DPP10 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[ADGRD1]] | C | ADGRD1 activity raises CLDN10-AS1's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 3.65× lower at baseline in the lines without ADGRD1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises CLDN10-AS1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.13× lower at baseline in the lines without GPRIN3 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[CCDC152]] | C | CCDC152 activity raises CLDN10-AS1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without CCDC152 | 0.024 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises CLDN10-AS1's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without LINC00589 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[SYTL5]] | C | SYTL5 activity raises CLDN10-AS1's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without SYTL5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400; co-absent with the target |
| [[TREM1]] | C | TREM1 activity raises CLDN10-AS1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without TREM1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF; co-absent with the target |
| [[LINC02320]] | C | LINC02320 activity raises CLDN10-AS1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.69× lower at baseline in the lines without LINC02320 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN10]] | B | CLDN10-AS1 activity raises CLDN10's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without CLDN10-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[ZG16B]] | B | CLDN10-AS1 activity raises ZG16B's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without CLDN10-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[MANSC1]] | B | CLDN10-AS1 activity raises MANSC1's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without CLDN10-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[GTF2IP7]] | B | CLDN10-AS1 activity raises GTF2IP7's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without CLDN10-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[ST3GAL1]] | B | CLDN10-AS1 activity raises ST3GAL1's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without CLDN10-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[RDH10]] | B | CLDN10-AS1 activity raises RDH10's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.04× lower at baseline in the lines without CLDN10-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM | B | CLDN10-AS1 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express CLDN10-AS1 (31) vs lines expressing it (17) | the lines without CLDN10-AS1: 0.74× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| cells under [[Afatinib (drug)]] 0.05 µM | B | CLDN10-AS1 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express CLDN10-AS1 (31) vs lines expressing it (17) | the lines without CLDN10-AS1: 1.09× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[CHN2]] | B | CLDN10-AS1 activity raises CHN2's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without CLDN10-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[TMEM154]] | C | CLDN10-AS1 activity raises TMEM154's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without CLDN10-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1; co-absent with the target |
| [[ST8SIA4]] | C | CLDN10-AS1 activity raises ST8SIA4's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.17× lower at baseline in the lines without CLDN10-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1; co-absent with the target |
| [[ADGRD1]] | C | CLDN10-AS1 activity raises ADGRD1's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.39× lower at baseline in the lines without CLDN10-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 16.3); signed map (17.3, 54.4). **Vector** length 67.9, 22.0% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.0 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.0 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | CLDN10 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q32.1 — chr13:95,479,444-95,533,910 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39907) · Entrez [100874194](https://www.ncbi.nlm.nih.gov/gene/100874194) · Ensembl [ENSG00000223392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223392)

## Data

Gene col 13338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13338); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13338]; `tensor/DDL_lfc|DDL_z.npy` [13338]; `embed/gene_vectors.npy` [13338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13338 or target_col == 13338). Every well: [[CLDN10-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN10-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
