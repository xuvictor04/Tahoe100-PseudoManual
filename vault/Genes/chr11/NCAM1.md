---
symbol: "NCAM1"
type: "gene"
col: 7362
ensembl_id: "ENSG00000149294"
name: "neural cell adhesion molecule 1"
location: "11q23.2"
module: 9
arm: "+"
pooled_cpm: 38.57
n_lines_expressing: 16
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NCAM1

*neural cell adhesion molecule 1* — 11q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.00× (z +25.0, q 0e+00, up in 14 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.671× (z -4.4, q 0.004, down in 0 of 14 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRXN3]] (+0.63, fdr 1e-05), [[UNC5D]] (+0.62, fdr 1e-05), [[PKIA]] (+0.61, fdr 1e-04); moves opposite to [[AKAP8]] (-0.53, fdr 8e-05), [[FAM185A]] (-0.52, fdr 5e-04), [[UQCC1]] (-0.52, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZMAT4]] → it (grade C ⚠); 7 go from it, the strongest it → [[WDR81]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.00×** | +25.0 | 0e+00 | 14/14 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **6.55×** | +20.6 | 0e+00 | 14/14 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.52×** | +16.5 | 0e+00 | 14/14 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.91×** | +14.9 | 0e+00 | 14/14 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +14.2 | 2e-43 | 3/14 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.52×** | +13.8 | 3e-41 | 14/14 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.96×** | +11.9 | 9e-31 | 14/14 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +11.0 | 2e-26 | 2/14 (SW 900, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.6 | 4e-20 | 3/12 (CHP-212, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.66×** | +7.8 | 3e-13 | 7/14 (A-172, SW480, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.59×** | +7.3 | 1e-11 | 14/14 (SW480, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.71×** | +5.9 | 2e-07 | 7/13 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 4e-06 | 11/14 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.68×** | +5.3 | 5e-06 | 1/12 (SW 900) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.001 | 4/12 (C32, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.003 | 1/16 (H4) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.003 | 1/13 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.029 | 7/14 (A-172, SHP-77, …) | rises with dose |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.043 | 0/14 | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.044 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.671×** | -4.4 | 0.004 | 0/14 | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.651×** | -4.3 | 0.004 | 1/14 (SW 1088) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.679×** | -4.2 | 0.004 | 2/14 (A498, NCI-H460) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.692×** | -4.0 | 0.008 | 5/14 (A498, NCI-H460, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.722×** | -3.4 | 0.068 | 0/13 | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 0.812× | -3.2 | 0.12 | 8/14 (A-172, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.816× | -3.1 | 0.12 | 0/14 | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.737× | -3.1 | 0.12 | 3/12 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.587× | -3.1 | 0.12 | 0/14 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.758× | -3.0 | 0.12 | 7/14 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Budesonide (drug)]] 5 µM |  | 0.758× | -3.0 | 0.12 | 6/14 (A498, NCI-H460, …) | top dose only |  |
| [[Tucatinib (drug)]] 0.5 µM |  | 0.679× | -3.0 | 0.12 | 0/14 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 49.4 | 8 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.75× (z +14.3) | [[Selinexor (drug)]] 5 µM 0.290× (z -13.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A498 (line)]] | wt | 103 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 3.70× (z +11.9) | [[Clobetasol propionate (drug)]] 0.5 µM 0.392× (z -8.5) |
| [[C32 (line)]] | wt | 64.4 | 4 | 2 | [[Tucidinostat (drug)]] 5 µM 4.55× (z +15.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.279× (z -9.1) |
| [[SW480 (line)]] | alt | 18.8 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +23.8) | — |
| [[H4 (line)]] | wt | 68.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 16.7× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 35.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 5.10× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 290 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -14.9) |
| [[SNU-423 (line)]] | alt | 16.6 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 9.30× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 327 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +13.7) | — |
| [[CHP-212 (line)]] | wt | 85.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.68× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 27.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.54× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 381 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.79 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRXN3]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 | STRING 538 |
| [[UNC5D]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[PKIA]] | +0.61 | +0.60 / +0.34 | both halves | 1e-04 | pathway: HALLMARK_MYOGENESIS |
| [[MARCHF1]] | +0.61 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[SUSD4]] | +0.59 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[GAP43]] | +0.59 | +0.37 / +0.54 | both halves | 9e-05 | pathway: L1CAM interactions; STRING 831 |
| [[ZMAT4]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CA8]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ATP1A3]] | +0.57 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[AFDN]] | +0.56 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[LINC01885]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SYT11]] | +0.56 | +0.28 / +0.56 | both halves | 3e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP8]] | -0.53 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[FAM185A]] | -0.52 | -0.24 / -0.36 | both halves | 5e-04 |  |
| [[UQCC1]] | -0.52 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[KANSL2]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ACAD9]] | -0.50 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[CWF19L1]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RCC1L]] | -0.49 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[MED24]] | -0.49 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[DDX59]] | -0.49 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[SPRYD4]] | -0.49 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[MAIP1]] | -0.49 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[ANKAR]] | -0.48 | -0.21 / -0.33 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT4]] | C | ZMAT4 activity raises NCAM1's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 5.36× lower at baseline in the lines without ZMAT4 | 0.040 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[SNAP25]] | C | SNAP25 activity raises NCAM1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 4.57× lower at baseline in the lines without SNAP25 | 0.060 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR81]] | B | NCAM1 activity raises WDR81's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without NCAM1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11 |
| [[OBSL1]] | B | NCAM1 activity raises OBSL1's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without NCAM1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11 |
| [[ZMAT4]] | C | NCAM1 activity raises ZMAT4's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 3.56× lower at baseline in the lines without NCAM1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |
| [[SNAP25]] | C | NCAM1 activity raises SNAP25's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 5.13× lower at baseline in the lines without NCAM1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |
| [[SCUBE1]] | C | NCAM1 activity raises SCUBE1's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without NCAM1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |
| [[CAMK4]] | C | NCAM1 activity raises CAMK4's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 4.58× lower at baseline in the lines without NCAM1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |
| [[INHBA]] | C | NCAM1 activity raises INHBA's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 3.38× lower at baseline in the lines without NCAM1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.9, 32.0); signed map (33.3, 33.3). **Vector** length 51.0, 13.4% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +25.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.2 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -1.9 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -4.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | neural cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.2 — chr11:112,961,275-113,278,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCAM, CD56 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | MYOGENESIS |
| Reactome | 14 pathways, smallest: Signal transduction by L1; NCAM1 interactions; NCAM signaling for neurite out-growth |
| Matched by | ensembl_id |

**Function**, from UniProt [P13591](https://www.uniprot.org/uniprotkb/P13591) (Neural cell adhesion molecule 1):

> This protein is a cell adhesion molecule involved in neuron-neuron adhesion, neurite fasciculation, outgrowth of neurites, etc.; (Microbial infection) Acts as a receptor for rabies virus.; (Microbial infection) Acts as a receptor for Zika virus.

**Summary**, from NCBI Gene [4684](https://www.ncbi.nlm.nih.gov/gene/4684):

> This gene encodes a cell adhesion protein which is a member of the immunoglobulin superfamily. The encoded protein is involved in cell-to-cell interactions as well as cell-matrix interactions during development and differentiation. The encoded protein plays a role in the development of the nervous system by regulating neurogenesis, neurite outgrowth, and cell migration. This protein is also involved in the expansion of T lymphocytes, B lymphocytes and natural killer (NK) cells which play an …

**Accessions** — [HGNC:7656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7656) · Entrez [4684](https://www.ncbi.nlm.nih.gov/gene/4684) · UniProt [P13591](https://www.uniprot.org/uniprotkb/P13591) · Ensembl [ENSG00000149294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149294)

## Data

Gene col 7362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7362); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7362]; `tensor/DDL_lfc|DDL_z.npy` [7362]; `embed/gene_vectors.npy` [7362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7362 or target_col == 7362). Every well: [[NCAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
