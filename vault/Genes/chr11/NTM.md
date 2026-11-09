---
symbol: "NTM"
type: "gene"
col: 11312
ensembl_id: "ENSG00000182667"
name: "neurotrimin"
location: "11q25"
module: 13
arm: "+"
pooled_cpm: 22.25
n_lines_expressing: 17
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 27
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NTM

*neurotrimin* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.11× (z +17.7, q 0e+00, up in 5 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Triamcinolone (drug)]] 5 µM: 0.758× (z -4.3, q 0.008, down in 7 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0446×, SW480 0.165×, HOP62 0.202×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0502×; ⚠ cell-cycle shift, explains ~12% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.0536×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.165×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0351×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS18]] (+0.73, fdr 7e-06), [[SAMD3]] (+0.66, fdr 7e-06), [[NETO1]] (+0.61, fdr 1e-05); moves opposite to [[IQSEC2]] (-0.42, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 27 go from it, the strongest it → [[HDAC2-AS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +17.7 | 0e+00 | 5/15 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.71×** | +17.0 | 0e+00 | 7/11 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.89×** | +14.4 | 2e-44 | 5/9 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +8.9 | 8e-17 | 6/11 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.7 | 1e-06 | 3/15 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 7e-06 | 1/15 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.3 | 8e-06 | 4/12 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.9 | 6e-05 | 4/15 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.37×** | +3.5 | 0.035 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.036 | 6/14 (LOX-IMVI, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.072 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.077 | 3/13 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.1 | 0.077 | 1/9 (A-172) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11312.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0446×, SW480 0.165×, HOP62 0.202×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0502×; ⚠ cell-cycle shift, explains ~12% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.0536×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.165×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0351×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 5 µM |  | **0.758×** | -4.3 | 0.008 | 7/15 (HOP62, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.747× | -3.2 | 0.35 | 6/14 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 5 µM |  | 0.733× | -3.0 | 0.44 | 5/15 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 532 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0446× (z -26.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0536× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 49.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.87× (z +8.6) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 26.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 26.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 2 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0351× (z -11.7) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 472 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.94 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS18]] | +0.73 | +0.80 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NETO1]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[TMEM200A]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RDUR]] | +0.60 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[DSCAM]] | +0.59 | +0.41 / +0.67 | both halves | 4e-05 | same gene group |
| [[DOCK2]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[VEPH1]] | +0.58 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[FGF5]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[EVA1A]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MAP3K7CL]] | +0.57 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[MIR4280HG]] | +0.56 | +0.41 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQSEC2]] | -0.42 | -0.37 / -0.38 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NTM's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDK15]] | C | CDK15 activity raises NTM's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 3.88× lower at baseline in the lines without CDK15 | 0.006 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent; co-absent with the target |
| [[ROBO2]] | C | ROBO2 activity raises NTM's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.47× lower at baseline in the lines without ROBO2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises NTM's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.33× lower at baseline in the lines without ADAMTS6 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[LINC02899]] | C | LINC02899 activity raises NTM's level | lines that do not express LINC02899 (40) vs lines expressing it (10) | 4.27× lower at baseline in the lines without LINC02899 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC02999, MUC6, SIM1; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises NTM's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 3.63× lower at baseline in the lines without TENM2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises NTM's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 4.28× lower at baseline in the lines without SLC25A24P1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises NTM's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without CTHRC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises NTM's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.96× lower at baseline in the lines without CDH13 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 6, C 21. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC2-AS2]] | B | NTM activity raises HDAC2-AS2's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.45× lower at baseline in the lines without NTM | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[NMNAT2]] | B | NTM activity weakens NMNAT2's drug response | lines that do not express NTM (17) vs lines expressing it (12) | the lines without NTM respond 2.19× as strongly (z diff -1.93); strongest at Tucidinostat 0.5 µM: 4.01x vs 1.97x (z diff -3.8) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; target measured in part of the lines; artifact flags |
| [[SSC5D]] | B | NTM activity raises SSC5D's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without NTM | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[SCHIP1]] | B | NTM activity raises SCHIP1's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without NTM | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[MGAT5B]] | B | NTM activity raises MGAT5B's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without NTM | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[REP15]] | B | NTM activity raises REP15's level | lines that do not express NTM (33) vs lines expressing it (17) | 1.47× lower at baseline in the lines without NTM | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[CDH13]] | C | NTM activity raises CDH13's level | lines that do not express NTM (33) vs lines expressing it (17) | 10.38× lower at baseline in the lines without NTM | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[ROBO2]] | C | NTM activity raises ROBO2's level | lines that do not express NTM (33) vs lines expressing it (17) | 3.40× lower at baseline in the lines without NTM | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[ADAMTS6]] | C | NTM activity raises ADAMTS6's level | lines that do not express NTM (33) vs lines expressing it (17) | 5.52× lower at baseline in the lines without NTM | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[RFX8]] | C | NTM activity raises RFX8's level | lines that do not express NTM (33) vs lines expressing it (17) | 6.03× lower at baseline in the lines without NTM | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[TENM2]] | C | NTM activity raises TENM2's level | lines that do not express NTM (33) vs lines expressing it (17) | 5.36× lower at baseline in the lines without NTM | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[HS3ST3A1]] | C | NTM activity raises HS3ST3A1's level | lines that do not express NTM (33) vs lines expressing it (17) | 6.63× lower at baseline in the lines without NTM | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.8, 13.7); signed map (18.9, 46.8). **Vector** length 56.4, 19.0% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.2 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | neurotrimin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:131,370,478-132,336,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNT, NTRI, IGLON2, CEPU-1 |
| Gene groups (HGNC) | I-set domain containing; IgLON cell adhesion molecules |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P121](https://www.uniprot.org/uniprotkb/Q9P121) (Neurotrimin):

> Neural cell adhesion molecule.

**Summary**, from NCBI Gene [50863](https://www.ncbi.nlm.nih.gov/gene/50863):

> This gene encodes a member of the IgLON (LAMP, OBCAM, Ntm) family of immunoglobulin (Ig) domain-containing glycosylphosphatidylinositol (GPI)-anchored cell adhesion molecules. The encoded protein may promote neurite outgrowth and adhesion via a homophilic mechanism. This gene is closely linked to a related family member, opioid binding protein/cell adhesion molecule-like (OPCML), on chromosome 11. Multiple transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:17941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17941) · Entrez [50863](https://www.ncbi.nlm.nih.gov/gene/50863) · UniProt [Q9P121](https://www.uniprot.org/uniprotkb/Q9P121) · Ensembl [ENSG00000182667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182667)

## Data

Gene col 11312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11312); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11312]; `tensor/DDL_lfc|DDL_z.npy` [11312]; `embed/gene_vectors.npy` [11312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11312 or target_col == 11312). Every well: [[NTM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
