---
symbol: "GTF2IP7"
type: "gene"
col: 13569
ensembl_id: "ENSG00000227038"
name: "general transcription factor IIi pseudogene 7"
location: "7q11.23"
module: 19
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 32
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 13
direction_downstream: 16
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GTF2IP7

*general transcription factor IIi pseudogene 7* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.27× (z +8.4, q 4e-14, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.549× (z -4.6, q 0.002, down in 15 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPIND1]] (+0.71, fdr 7e-06), [[UNC5D]] (+0.63, fdr 1e-05), [[SCUBE1]] (+0.63, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); 16 go from it, the strongest it → [[RABGEF1P3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +8.4 | 4e-14 | 1/6 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +7.4 | 4e-11 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +5.5 | 6e-06 | 16/29 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.8 | 2e-04 | 1/11 (Hs 766T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.26×** | +4.4 | 1e-03 | 1/5 (A549) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +3.3 | 0.078 | 2/25 (NCI-H1573, NCI-H2347) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.3 | 0.078 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.2 | 0.092 | 0/18 | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.18× | +3.1 | 0.12 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.05 µM |  | 1.49× | +3.0 | 0.14 | 1/19 (Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -4.6 | 0.002 | 15/28 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -4.3 | 0.004 | 12/25 (NCI-H1792, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -4.0 | 0.011 | 7/28 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.621×** | -3.7 | 0.036 | 12/25 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.629×** | -3.6 | 0.042 | 13/22 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.094 | 10/29 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.655×** | -3.2 | 0.094 | 13/27 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 0.673× | -3.0 | 0.17 | 2/22 (Hs 766T, SW 900) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 7.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0650× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 5.51 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -12.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 0.901 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.578 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.603 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.547 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.709 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.603 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPIND1]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[UNC5D]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SCUBE1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[CLDN10-AS1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[TMEM154]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SERPINB11]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CCDC68]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CA2]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PLAC4]] | +0.58 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[ITPRID2]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CDH11]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SERPINB2]] | +0.57 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity raises GTF2IP7's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without LINC02320 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[CLDN10-AS1]] | B | CLDN10-AS1 activity raises GTF2IP7's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without CLDN10-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[CREG2]] | B | CREG2 activity raises GTF2IP7's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without CREG2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[FAM107B]] | B | FAM107B activity raises GTF2IP7's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without FAM107B | 0.056 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[DIO3OS]] | B | DIO3OS activity raises GTF2IP7's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without DIO3OS | 0.060 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[HDAC6]] | B | HDAC6 activity raises GTF2IP7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CEMIP]] | B | CEMIP activity raises GTF2IP7's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without CEMIP | 0.072 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[ST6GAL2]] | B | ST6GAL2 activity raises GTF2IP7's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 1.66× lower at baseline in the lines without ST6GAL2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[SMOX]] | B | SMOX activity raises GTF2IP7's level | lines that do not express SMOX (6) vs lines expressing it (44) | 1.87× lower at baseline in the lines without SMOX | 0.090 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[NGEF]] | B | NGEF activity raises GTF2IP7's level | lines that do not express NGEF (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without NGEF | 0.099 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[VSIG1]] | C | VSIG1 activity raises GTF2IP7's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without VSIG1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |
| [[TFF1]] | C | TFF1 activity raises GTF2IP7's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without TFF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 11, C 5. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RABGEF1P3]] | B | GTF2IP7 activity raises RABGEF1P3's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without GTF2IP7 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[PLEK2]] | B | GTF2IP7 activity raises PLEK2's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without GTF2IP7 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[MYEOV]] | B | GTF2IP7 activity raises MYEOV's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without GTF2IP7 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[TMEM154]] | B | GTF2IP7 activity raises TMEM154's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without GTF2IP7 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[WNT7B]] | B | GTF2IP7 activity raises WNT7B's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.75× lower at baseline in the lines without GTF2IP7 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[DNPEP]] | B | GTF2IP7 activity lowers DNPEP's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 1.12× higher at baseline in the lines without GTF2IP7 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[CLDN10-AS1]] | B | GTF2IP7 activity raises CLDN10-AS1's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without GTF2IP7 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[ITPRID2]] | B | GTF2IP7 activity strengthens ITPRID2's drug response | lines that do not express GTF2IP7 (17) vs lines expressing it (31) | the lines without GTF2IP7 respond 0.56× as strongly (z diff +1.37); strongest at Homoharringtonine 5 µM: 0.79x vs 0.68x (z diff +3.0) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92; target measured in part of the lines; artifact flags |
| [[CREG2]] | B | GTF2IP7 activity raises CREG2's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without GTF2IP7 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[LAMC2]] | B | GTF2IP7 activity raises LAMC2's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without GTF2IP7 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[SYT13]] | B | GTF2IP7 activity raises SYT13's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without GTF2IP7 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[C6orf141]] | C | GTF2IP7 activity raises C6orf141's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 3.55× lower at baseline in the lines without GTF2IP7 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 16.3); signed map (17.6, 54.5). **Vector** length 46.6, 8.95% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +0.7 | +2.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +0.6 | +1.9 |
|  | [[Vilanterol (drug)]] 0.05 µM |  | +0.6 | +3.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIi pseudogene 7 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:76,099,440-76,101,408 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51720) · Entrez [101927126](https://www.ncbi.nlm.nih.gov/gene/101927126) · Ensembl [ENSG00000227038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227038)

## Data

Gene col 13569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13569); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13569]; `tensor/DDL_lfc|DDL_z.npy` [13569]; `embed/gene_vectors.npy` [13569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13569 or target_col == 13569). Every well: [[GTF2IP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
