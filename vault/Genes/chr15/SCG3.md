---
symbol: "SCG3"
type: "gene"
col: 2415
ensembl_id: "ENSG00000104112"
name: "secretogranin III"
location: "15q21.2"
module: 61
arm: "+"
pooled_cpm: 7.27
n_lines_expressing: 11
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SCG3

*secretogranin III* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.23× (z +11.3, q 1e-26, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +5.8, q 7e-07, up in 2 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHGB]] (+0.66, fdr 1e-05), [[VGF]] (+0.61, fdr 4e-05), [[SH3GL2]] (+0.57, fdr 4e-05); moves opposite to [[SLC15A5]] (-0.48, fdr 0.001, ⚠ one half only (not replicated)), [[NSMAF]] (-0.47, fdr 1e-04), [[DHX35]] (-0.46, fdr 1e-04), [[NACC2]] (-0.44, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TMEM92-AS1]] → it (grade B ⚠); 12 go from it, the strongest it → [[SRRM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.23×** | +11.3 | 1e-26 | 3/3 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.08×** | +10.7 | 2e-24 | 3/3 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.92×** | +8.4 | 9e-15 | 3/3 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.65×** | +7.9 | 5e-13 | 2/5 (SW480, NCI-H460) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +5.8 | 7e-07 | 2/6 (C32, NCI-H460) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +4.8 | 2e-04 | 3/4 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +4.7 | 2e-04 | 6/8 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +4.6 | 3e-04 | 6/6 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.09×** | +4.2 | 0.002 | 1/5 (NCI-H460) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.02×** | +4.0 | 0.003 | 1/4 (NCI-H460) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.008 | 5/6 (NCI-H460, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.35×** | +3.6 | 0.015 | 1/4 (SW480) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.016 | 1/8 (SW480) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.84×** | +3.5 | 0.020 | 1/6 (C-33 A) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.31×** | +3.4 | 0.025 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.058 | 1/6 (SW1417) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +3.1 | 0.059 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.10×** | +3.0 | 0.078 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.548× | -3.2 | 0.48 | 0/7 | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | 0.575× | -3.1 | 0.48 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHGB]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 | same gene group; pathway: Post-translational protein phosphorylation; STRING 937 |
| [[VGF]] | +0.61 | +0.55 / +0.41 | both halves | 4e-05 | same gene group; pathway: Post-translational protein phosphorylation; STRING 661 |
| [[SH3GL2]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ADAM7-AS1]] | +0.55 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[SRRM3]] | +0.54 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[SYP]] | +0.50 | +0.37 / +0.41 | both halves | 8e-05 | STRING 411 |
| [[CHST8]] | +0.50 | +0.57 / +0.27 | both halves | 3e-04 |  |
| [[LINC00408]] | +0.49 | +0.47 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[CYP2U1-AS1]] | +0.48 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[SMPD3]] | +0.47 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[RAP1B]] | +0.47 | +0.35 / +0.39 | both halves | 1e-04 | pathway: Platelet activation, signaling and aggregation |
| [[EPHB1]] | +0.47 | +0.26 / +0.37 | both halves | 3e-04 |  |
| [[NFASC]] | +0.46 | +0.32 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A5]] | -0.48 | -0.55 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[NSMAF]] | -0.47 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[DHX35]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ZNF346]] | -0.44 | -0.39 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[NACC2]] | -0.44 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[MCM9]] | -0.43 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[COLGALT2]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.43 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[KCTD15]] | -0.42 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[TRAPPC13]] | -0.42 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[PDE3B]] | -0.41 | -0.32 / -0.24 | both halves | 4e-04 |  |
| [[ZFYVE9]] | -0.41 | -0.39 / -0.26 | both halves | 3e-04 |  |
| [[MKRN5P]] | -0.41 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[LIG3]] | -0.40 | -0.34 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity lowers SCG3's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 2.13× higher at baseline in the lines without TMEM92-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[UBBP4-1]] | C | UBBP4-1 activity raises SCG3's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without UBBP4-1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises SCG3's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without CCDC144NL-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[VGF]] | C | VGF activity raises SCG3's level | lines that do not express VGF (32) vs lines expressing it (18) | 2.74× lower at baseline in the lines without VGF | 0.010 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises SCG3's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without NFASC | 0.020 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[CHGB]] | C | CHGB activity raises SCG3's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.80× lower at baseline in the lines without CHGB | 0.029 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[ENPP2]] | C | ENPP2 activity raises SCG3's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without ENPP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[LINC01194]] | C | LINC01194 activity raises SCG3's level | lines that do not express LINC01194 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without LINC01194 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC00470, ENSG00000259929, ENSG00000249174; co-absent with the target |
| [[LINC00408]] | C | LINC00408 activity raises SCG3's level | lines that do not express LINC00408 (38) vs lines expressing it (12) | 1.92× lower at baseline in the lines without LINC00408 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000287861, ANKRD20A9P, PHF2P2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | SCG3 activity raises SRRM3's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 3.33× lower at baseline in the lines without SCG3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[SMPD3]] | B | SCG3 activity raises SMPD3's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 1.89× lower at baseline in the lines without SCG3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[SYP]] | B | SCG3 activity raises SYP's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.51× lower at baseline in the lines without SCG3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[ARC]] | B | SCG3 activity raises ARC's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 1.90× lower at baseline in the lines without SCG3 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[SYN1]] | B | SCG3 activity raises SYN1's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 1.46× lower at baseline in the lines without SCG3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[NRXN1]] | B | SCG3 activity raises NRXN1's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.88× lower at baseline in the lines without SCG3 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[VGF]] | C | SCG3 activity raises VGF's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 5.53× lower at baseline in the lines without SCG3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[ENPP2]] | C | SCG3 activity raises ENPP2's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.11× lower at baseline in the lines without SCG3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[CHL1]] | C | SCG3 activity raises CHL1's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 3.42× lower at baseline in the lines without SCG3 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[PCSK2]] | C | SCG3 activity raises PCSK2's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.23× lower at baseline in the lines without SCG3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[CHGB]] | C | SCG3 activity raises CHGB's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 3.53× lower at baseline in the lines without SCG3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[COLGALT2]] | C | SCG3 activity raises COLGALT2's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.76× lower at baseline in the lines without SCG3 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.489). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 34.4); signed map (7.7, 30.3). **Vector** length 17.7, 5.04% of its response variance represented; |z| ≥ 3 in 129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.5 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.4 | -0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.4 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.4 | +1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.4 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.4 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.3 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.3 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | secretogranin III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,681,492-51,721,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SgIII, FLJ90833 |
| Gene groups (HGNC) | Granins |
| Hallmark sets | SPERMATOGENESIS, COMPLEMENT, KRAS_SIGNALING_UP |
| Reactome | 6 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXD2](https://www.uniprot.org/uniprotkb/Q8WXD2) (Secretogranin-3):

> Member of the granin protein family that regulates the biogenesis of secretory granules. Acts as a sorting receptor for intragranular proteins including chromogranin A/CHGA (By similarity). May also play a role in angiogenesis. Promotes endothelial proliferation, migration and tube formation through MEK/ERK signaling pathway.

**Summary**, from NCBI Gene [29106](https://www.ncbi.nlm.nih.gov/gene/29106):

> The protein encoded by this gene is a member of the chromogranin/secretogranin family of neuroendocrine secretory proteins. Granins may serve as precursors for biologically active peptides. Some granins have been shown to function as helper proteins in sorting and proteolytic processing of prohormones; however, the function of this protein is unknown. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:13707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13707) · Entrez [29106](https://www.ncbi.nlm.nih.gov/gene/29106) · UniProt [Q8WXD2](https://www.uniprot.org/uniprotkb/Q8WXD2) · Ensembl [ENSG00000104112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104112)

## Data

Gene col 2415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2415); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2415]; `tensor/DDL_lfc|DDL_z.npy` [2415]; `embed/gene_vectors.npy` [2415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2415 or target_col == 2415). Every well: [[SCG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
