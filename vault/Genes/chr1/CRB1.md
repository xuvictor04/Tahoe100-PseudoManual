---
symbol: "CRB1"
type: "gene"
col: 5558
ensembl_id: "ENSG00000134376"
name: "crumbs cell polarity complex component 1"
location: "1q31.3"
module: 10
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 44
n_dd_up: 34
n_dd_down: 11
n_dd_up_clean: 31
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CRB1

*crumbs cell polarity complex component 1* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.48× (z +17.7, q 0e+00, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.392× (z -6.3, q 2e-07, down in 24 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRIQ3]] (+0.73, fdr 7e-06), [[USP38-DT]] (+0.71, fdr 7e-06), [[UNC79]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DGKB]] → it (grade B ⚠); 8 go from it, the strongest it → [[PSMD7-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.48×** | +17.7 | 0e+00 | 24/28 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +7.2 | 2e-10 | 18/27 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +6.7 | 3e-09 | 17/23 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +5.8 | 8e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.24×** | +5.4 | 8e-06 | 20/39 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.74×** | +5.1 | 3e-05 | 16/39 (A-427, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +4.9 | 8e-05 | 18/38 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.07×** | +4.9 | 8e-05 | 10/38 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **2.06×** | +4.7 | 2e-04 | 16/30 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +4.5 | 4e-04 | 11/38 (A-172, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.61×** | +4.4 | 6e-04 | 15/36 (A498, SK-MEL-2, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +4.3 | 7e-04 | 16/36 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.93×** | +4.2 | 1e-03 | 12/32 (A498, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +4.2 | 0.001 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.85×** | +4.1 | 0.001 | 12/33 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.004 | 11/35 (SK-MEL-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.78×** | +3.8 | 0.004 | 5/35 (A498, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.392×** | -6.3 | 2e-07 | 24/38 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.367×** | -6.1 | 3e-07 | 20/35 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.486×** | -4.9 | 2e-04 | 19/37 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -4.8 | 2e-04 | 14/22 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.505×** | -4.6 | 4e-04 | 18/40 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.506×** | -4.6 | 4e-04 | 15/33 (NCI-H23, RKO, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.513×** | -4.2 | 0.002 | 16/34 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.504×** | -4.2 | 0.002 | 12/32 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.563×** | -3.9 | 0.007 | 11/40 (C32, SNU-1, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.581×** | -3.7 | 0.015 | 16/37 (SHP-77, C32, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.629×** | -3.1 | 0.092 | 14/40 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Asciminib (drug)]] 0.05 µM |  | 0.640× | -3.0 | 0.13 | 9/36 (NCI-H1792, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.59 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0524× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 9.65 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0959× (z -8.6) |
| [[A-172 (line)]] | wt | 1.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +8.7) | — |
| [[A498 (line)]] | wt | 9.04 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0290× (z -10.9) |
| [[C32 (line)]] | wt | 14.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0534× (z -10.2) |
| [[PANC-1 (line)]] | alt | 1.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.883 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.862 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.797 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRIQ3]] | +0.73 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[USP38-DT]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[UNC79]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[ZRANB2-DT]] | +0.69 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[LINC01013]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[CFAP418-AS1]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MAD2L1-DT]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[GAS2]] | +0.67 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[STPG2]] | +0.67 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.67 | +0.69 / +0.57 | both halves | 8e-06 |  |
| [[KATNAL2]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKB]] | B | DGKB activity raises CRB1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without DGKB | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CRB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SAMD11]] | B | SAMD11 activity raises CRB1's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.93× lower at baseline in the lines without SAMD11 | 0.067 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[PSMB5]] | B | PSMB5 activity raises CRB1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMD7-DT]] | B | CRB1 activity raises PSMD7-DT's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without CRB1 | 0.017 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[SPATA17]] | B | CRB1 activity raises SPATA17's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without CRB1 | 0.023 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[LRRIQ3]] | B | CRB1 activity raises LRRIQ3's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without CRB1 | 0.036 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[EFCAB6]] | B | CRB1 activity raises EFCAB6's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without CRB1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[DRAIC]] | B | CRB1 activity raises DRAIC's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without CRB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[EPM2A-DT]] | B | CRB1 activity raises EPM2A-DT's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CRB1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | CRB1 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express CRB1 (6) vs lines expressing it (42) | the lines without CRB1: 0.88× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[FBXO15]] | C | CRB1 activity raises FBXO15's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without CRB1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.8, 17.4); signed map (29.9, -9.2). **Vector** length 56.9, 9.97% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -4.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +1.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | crumbs cell polarity complex component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:197,268,204-197,478,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LCA8; previously RP12 |
| Gene groups (HGNC) | Crumbs complex components |
| Matched by | ensembl_id |

**Function**, from UniProt [P82279](https://www.uniprot.org/uniprotkb/P82279) (Protein crumbs homolog 1):

> Plays a role in photoreceptor morphogenesis in the retina (By similarity). May maintain cell polarization and adhesion (By similarity).

**Summary**, from NCBI Gene [23418](https://www.ncbi.nlm.nih.gov/gene/23418):

> This gene encodes a protein which is similar to the Drosophila crumbs protein and localizes to the inner segment of mammalian photoreceptors. In Drosophila crumbs localizes to the stalk of the fly photoreceptor and may be a component of the molecular scaffold that controls proper development of polarity in the eye. Mutations in this gene are associated with a severe form of retinitis pigmentosa, RP12, and with Leber congenital amaurosis. Alternate splicing results in multiple transcript …

**Accessions** — [HGNC:2343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2343) · Entrez [23418](https://www.ncbi.nlm.nih.gov/gene/23418) · UniProt [P82279](https://www.uniprot.org/uniprotkb/P82279) · Ensembl [ENSG00000134376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134376)

## Data

Gene col 5558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5558); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5558]; `tensor/DDL_lfc|DDL_z.npy` [5558]; `embed/gene_vectors.npy` [5558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5558 or target_col == 5558). Every well: [[CRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
