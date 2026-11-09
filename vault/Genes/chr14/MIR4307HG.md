---
symbol: "MIR4307HG"
type: "gene"
col: 15053
ensembl_id: "ENSG00000257612"
name: "MIR4307 host gene"
location: "14q12"
module: 9
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 15
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MIR4307HG

*MIR4307 host gene* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +10.6, q 2e-23, up in 4 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.535× (z -4.4, q 0.007, down in 4 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSR1]] (+0.68, fdr 1e-05), [[LINC02241]] (+0.65, fdr 1e-05), [[MARCHF1]] (+0.65, fdr 2e-05); moves opposite to [[LTBP3]] (-0.50, fdr 6e-05), [[ECE1]] (-0.49, fdr 5e-05), [[ABHD12]] (-0.48, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02945]] → it (grade C ⚠); 13 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +10.6 | 2e-23 | 4/10 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.94×** | +9.1 | 3e-17 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.88×** | +8.7 | 9e-16 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +8.0 | 2e-13 | 1/11 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +7.9 | 4e-13 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +6.1 | 1e-07 | 5/10 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.27×** | +5.7 | 1e-06 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.77×** | +5.0 | 4e-05 | 1/4 (NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +4.9 | 5e-05 | 5/13 (A-172, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.58×** | +4.4 | 6e-04 | 1/11 (SW1417) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +4.0 | 0.003 | 2/12 (SW1417, SHP-77) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.97×** | +3.9 | 0.004 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.015 | 0/13 | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.5 | 0.017 | 0/8 | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.59×** | +3.4 | 0.023 | 2/4 (SK-MEL-2, A-172) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.3 | 0.037 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.042 | 1/7 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.043 | 0/12 | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.073 | 1/8 (A-172) | inconsistent across doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.086 | 0/13 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.535×** | -4.4 | 0.007 | 4/13 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.521×** | -4.2 | 0.007 | 2/13 (SNU-423, NCI-H1573) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.498×** | -4.0 | 0.012 | 4/13 (KATO III, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.638× | -3.1 | 0.17 | 1/13 (SNU-423) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.615× | -3.1 | 0.17 | 0/13 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.617× | -3.1 | 0.17 | 1/13 (LS 180) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.738× | -3.0 | 0.21 | 6/12 (LOX-IMVI, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 69.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -19.1) |
| [[A-172 (line)]] | wt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.32 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0725× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0495× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.265 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSR1]] | +0.68 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.65 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LINC02945]] | +0.64 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[PHACTR1]] | +0.60 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[LINC01695]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[LINC02484]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC01320]] | +0.57 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ABCC9]] | +0.57 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[SYNE1]] | +0.56 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[GNGT1]] | +0.55 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[LURAP1L-AS1]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBP3]] | -0.50 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[ECE1]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ABHD12]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[TATDN2]] | -0.48 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[FAM20C]] | -0.47 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ACTL6A]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[SDHA]] | -0.47 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[POC1A]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[RRM2]] | -0.46 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[C21orf58]] | -0.46 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[SFXN2]] | -0.45 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[SDHAP4]] | -0.45 | -0.41 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02945]] | C | LINC02945 activity raises MIR4307HG's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 4.10× lower at baseline in the lines without LINC02945 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016; co-absent with the target |
| [[DDX43]] | C | DDX43 activity raises MIR4307HG's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without DDX43 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises MIR4307HG's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.14× lower at baseline in the lines without MIR99AHG | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[LINC02484]] | C | LINC02484 activity raises MIR4307HG's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 2.67× lower at baseline in the lines without LINC02484 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises MIR4307HG's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.55× lower at baseline in the lines without TENM1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | MIR4307HG activity raises LSAMP's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 3.00× lower at baseline in the lines without MIR4307HG | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |
| [[ANO3]] | B | MIR4307HG activity raises ANO3's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.76× lower at baseline in the lines without MIR4307HG | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |
| [[SMPD4]] | B | MIR4307HG activity lowers SMPD4's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.29× higher at baseline in the lines without MIR4307HG | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |
| [[KCP]] | B | MIR4307HG activity raises KCP's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.48× lower at baseline in the lines without MIR4307HG | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |
| [[TENM1]] | C | MIR4307HG activity raises TENM1's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 4.08× lower at baseline in the lines without MIR4307HG | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[MIR3171HG]] | C | MIR4307HG activity raises MIR3171HG's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 4.71× lower at baseline in the lines without MIR4307HG | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[GNGT1]] | C | MIR4307HG activity raises GNGT1's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 3.88× lower at baseline in the lines without MIR4307HG | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[KCNH5]] | C | MIR4307HG activity raises KCNH5's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 2.70× lower at baseline in the lines without MIR4307HG | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[NPFFR2]] | C | MIR4307HG activity raises NPFFR2's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 2.55× lower at baseline in the lines without MIR4307HG | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[MARCHF1]] | C | MIR4307HG activity raises MARCHF1's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 3.29× lower at baseline in the lines without MIR4307HG | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[NKAIN2]] | C | MIR4307HG activity raises NKAIN2's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 2.28× lower at baseline in the lines without MIR4307HG | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[LINP1]] | C | MIR4307HG activity raises LINP1's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.50× lower at baseline in the lines without MIR4307HG | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.5, 28.2); signed map (39.7, 27.2). **Vector** length 22.0, 3.83% of its response variance represented; |z| ≥ 3 in 301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +0.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.6 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | MIR4307 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q12 — chr14:26,873,092-26,918,594 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52004) · Entrez [101927081](https://www.ncbi.nlm.nih.gov/gene/101927081) · Ensembl [ENSG00000257612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257612)

## Data

Gene col 15053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15053); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15053]; `tensor/DDL_lfc|DDL_z.npy` [15053]; `embed/gene_vectors.npy` [15053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15053 or target_col == 15053). Every well: [[MIR4307HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4307HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
