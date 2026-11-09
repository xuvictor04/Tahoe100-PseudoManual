---
symbol: "SYN2"
type: "gene"
col: 8045
ensembl_id: "ENSG00000157152"
name: "synapsin II"
location: "3p25.2"
module: 102
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 27
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SYN2

*synapsin II* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.89× (z +20.2, q 0e+00, up in 11 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Pexidartinib (hydrochloride) (drug)]] 5 µM: 0.545× (z -6.2, q 4e-07, down in 13 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEGF11]] (+0.68, fdr 7e-06), [[RASGEF1C]] (+0.67, fdr 7e-06), [[GRID1]] (+0.64, fdr 7e-06); moves opposite to [[COG4]] (-0.47, fdr 1e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[KCNQ2]] → it (grade B ⚠); 4 go from it, the strongest it → [[LPAR3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +20.2 | 0e+00 | 11/18 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +11.4 | 1e-27 | 15/23 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +10.6 | 8e-24 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +9.1 | 2e-17 | 3/12 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +8.2 | 3e-14 | 13/22 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.20×** | +7.8 | 5e-13 | 9/22 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +7.2 | 5e-11 | 1/7 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +7.1 | 7e-11 | 13/22 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +7.0 | 2e-10 | 15/23 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +6.3 | 2e-08 | 13/22 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.6 | 9e-07 | 3/10 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +4.3 | 8e-04 | 6/16 (A549, H4, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.1 | 0.002 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.004 | 15/23 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Flutamide (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.006 | 3/21 (NCI-H2347, LOX-IMVI, …) | two highest doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.034 | 2/19 (LOX-IMVI, LoVo) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.035 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.046 | 1/20 (CHP-212) | inconsistent across doses |  |
| [[Vemurafenib (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.048 | 2/23 (NCI-H2347, SW48) | inconsistent across doses | position effect removed |
| [[Orlistat (drug)]] 0.05 µM |  | **1.34×** | +2.8 | 0.096 | 1/17 (SW1417) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.33×** | +2.8 | 0.098 | 5/20 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -6.2 | 4e-07 | 13/23 (A-427, C-33 A, …) | rises with dose | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **0.699×** | -5.4 | 2e-05 | 13/23 (A-427, C-33 A, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -4.0 | 0.013 | 9/22 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.704×** | -3.6 | 0.051 | 10/20 (A-427, NCI-H1792, …) | top dose only | position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | 0.564× | -3.2 | 0.18 | 5/23 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Proglumide (drug)]] 0.5 µM |  | 0.752× | -3.0 | 0.24 | 2/22 (HS-578T, LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 83.9 | 0 | 12 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0600× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Terfenadine (drug)]] 5 µM 0.254× (z -15.6) |
| [[PANC-1 (line)]] | alt | 11.8 | 5 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.39× (z +10.3) | [[Terfenadine (drug)]] 5 µM 0.341× (z -9.1) |
| [[C-33 A (line)]] | alt | 49.9 | 0 | 2 (1 ⚠) | — | [[Terfenadine (drug)]] 5 µM 0.260× (z -10.5) |
| [[H4 (line)]] | wt | 33.0 | 0 | 2 (1 ⚠) | — | [[Terfenadine (drug)]] 5 µM 0.218× (z -10.0) |
| [[SW480 (line)]] | alt | 2.07 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.26× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 1 | — | [[Terfenadine (drug)]] 5 µM 0.278× (z -9.3) |
| [[A-172 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.992 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEGF11]] | +0.68 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[RASGEF1C]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[GRID1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CDH23]] | +0.64 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TEX15]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MED12L]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[C12orf56]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LPAR3]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[GNAO1]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[LINC00937]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[KCNQ2]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 | pathway: Neuronal System |
| [[BRSK2]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG4]] | -0.47 | -0.34 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ2]] | B | KCNQ2 activity raises SYN2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without KCNQ2 | 0.027 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[PDZD4]] | B | PDZD4 activity raises SYN2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without PDZD4 | 0.039 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[GBX1]] | B | GBX1 activity raises SYN2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without GBX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[ASNSP1]] | B | ASNSP1 activity raises SYN2's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 2.07× lower at baseline in the lines without ASNSP1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[CACNA2D2]] | B | CACNA2D2 activity raises SYN2's level | lines that do not express CACNA2D2 (17) vs lines expressing it (33) | 2.21× lower at baseline in the lines without CACNA2D2 | 0.094 | ⚠ within organs, on part of the lines; also absent: JPH3, MIR9-3HG, CELF4; maybe low, not absent |
| [[NFASC]] | B | NFASC activity raises SYN2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without NFASC | 0.097 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[ELFN1]] | C | ELFN1 activity raises SYN2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without ELFN1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises SYN2's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.67× lower at baseline in the lines without CTNNA2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[WT1-AS]] | C | WT1-AS activity raises SYN2's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 2.20× lower at baseline in the lines without WT1-AS | 0.043 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR3]] | B | SYN2 activity raises LPAR3's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without SYN2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |
| [[SUGCT]] | B | SYN2 activity raises SUGCT's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without SYN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |
| [[MCOLN2]] | B | SYN2 activity raises MCOLN2's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without SYN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |
| [[C12orf56]] | B | SYN2 activity raises C12orf56's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without SYN2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.2, 37.8); signed map (27.5, 25.9). **Vector** length 38.6, 5.98% of its response variance represented; |z| ≥ 3 in 651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +20.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -2.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | synapsin II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,004,388-12,192,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYNII, SYNIIa, SYNIIb |
| Gene groups (HGNC) | Synapsins |
| Reactome | 5 pathways, smallest: Serotonin Neurotransmitter Release Cycle; Dopamine Neurotransmitter Release Cycle; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92777](https://www.uniprot.org/uniprotkb/Q92777) (Synapsin-2):

> Neuronal phosphoprotein that coats synaptic vesicles, binds to the cytoskeleton, and is believed to function in the regulation of neurotransmitter release. May play a role in noradrenaline secretion by sympathetic neurons (By similarity).

**Summary**, from NCBI Gene [6854](https://www.ncbi.nlm.nih.gov/gene/6854):

> This gene is a member of the synapsin gene family. Synapsins encode neuronal phosphoproteins which associate with the cytoplasmic surface of synaptic vesicles. Family members are characterized by common protein domains, and they are implicated in synaptogenesis and the modulation of neurotransmitter release, suggesting a potential role in several neuropsychiatric diseases. This member of the synapsin family encodes a neuron-specific phosphoprotein that selectively binds to small synaptic …

**Accessions** — [HGNC:11495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11495) · Entrez [6854](https://www.ncbi.nlm.nih.gov/gene/6854) · UniProt [Q92777](https://www.uniprot.org/uniprotkb/Q92777) · Ensembl [ENSG00000157152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157152)

## Data

Gene col 8045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8045); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8045]; `tensor/DDL_lfc|DDL_z.npy` [8045]; `embed/gene_vectors.npy` [8045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8045 or target_col == 8045). Every well: [[SYN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
