---
symbol: "C1orf54"
type: "gene"
col: 3979
ensembl_id: "ENSG00000118292"
name: "chromosome 1 open reading frame 54"
location: "1q21.2"
module: 35
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# C1orf54

*chromosome 1 open reading frame 54* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.61× (z +22.7, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.340× (z -13.5, q 2e-38, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN7L3-AS1]] (+0.77, fdr 1e-05), [[MED28-DT]] (+0.72, fdr 3e-05), [[ATXN1L]] (+0.71, fdr 1e-05); moves opposite to [[CEP57L1]] (-0.60, fdr 5e-05), [[ARL6]] (-0.60, fdr 5e-05), [[GPSM2]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02257]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +22.7 | 0e+00 | 32/35 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.89×** | +11.3 | 6e-27 | 22/43 (A-172, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.54×** | +11.2 | 8e-27 | 22/29 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +9.8 | 2e-20 | 19/34 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +8.1 | 6e-14 | 21/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +7.7 | 2e-12 | 22/42 (C32, HCT15, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +7.0 | 2e-10 | 23/45 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +6.8 | 6e-10 | 20/41 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.4 | 1e-08 | 13/27 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.66×** | +6.3 | 1e-08 | 16/42 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.2 | 3e-08 | 2/12 (SNU-423, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.0 | 3e-05 | 1/9 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.8 | 7e-05 | 12/36 (C32, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.7 | 1e-04 | 2/14 (HEC-1-A, LoVo) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.6 | 1e-04 | 10/34 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.43×** | +4.5 | 2e-04 | 12/45 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 5e-04 | 13/44 (C32, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 11/37 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.001 | 14/41 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 10/46 (HEC-1-A, A-172, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.005 | 3/45 (hTERT-HPNE, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.340×** | -13.5 | 2e-38 | 32/45 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.404×** | -11.3 | 4e-27 | 29/45 (LS 180, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.467×** | -9.5 | 5e-19 | 28/45 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.596×** | -9.1 | 1e-17 | 27/45 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.505×** | -8.5 | 2e-15 | 26/44 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.577×** | -6.8 | 7e-10 | 20/42 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.389×** | -6.1 | 7e-08 | 19/41 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.657×** | -5.2 | 1e-05 | 19/35 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 13.6 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0625× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 8.77 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.0659× (z -15.5) |
| [[COLO 205 (line)]] | alt | 11.3 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 9.57× (z +8.5) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.0813× (z -9.8) |
| [[HOP62 (line)]] | alt | 2.55 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +9.1) | [[Tucidinostat (drug)]] 5 µM 0.144× (z -9.2) |
| [[LoVo (line)]] | wt | 5.87 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 7.17× (z +8.7) ⚠ toxic | [[Belinostat (drug)]] 0.5 µM 0.0789× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 2.48 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +10.3) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.108× (z -8.6) |
| [[C32 (line)]] | wt | 4.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.16× (z +10.3) | — |
| [[KATO III (line)]] | alt | 4.29 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0948× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0711× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 6.06 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0966× (z -9.2) |
| [[PANC-1 (line)]] | alt | 1.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.67× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0404× (z -10.9) |
| [[A-172 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L3-AS1]] | +0.77 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MED28-DT]] | +0.72 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ATXN1L]] | +0.71 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.71 | +0.47 / +0.43 | both halves | 4e-05 |  |
| [[ZHX2]] | +0.69 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.68 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | +0.68 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[CIBAR1-DT]] | +0.68 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[MYLK4]] | +0.68 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[SMG1-DT]] | +0.67 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[LINC01090]] | +0.67 | +0.48 / +0.36 | both halves | 9e-05 |  |
| [[SPATA1]] | +0.67 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP57L1]] | -0.60 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[ARL6]] | -0.60 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[GPSM2]] | -0.59 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[SSX2IP]] | -0.57 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[SDHAF3]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02257]] | B | LINC02257 activity raises C1orf54's level | lines that do not express LINC02257 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without LINC02257 | 0.024 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers C1orf54's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRKCH]] | B | PRKCH activity raises C1orf54's level | lines that do not express PRKCH (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without PRKCH | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000258989, ENSG00000284686, APBA1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises C1orf54's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises C1orf54's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises C1orf54's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without ZNF341-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.7, 21.4); signed map (29.1, -1.2). **Vector** length 77.7, 13.3% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +22.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -13.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 1 open reading frame 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,268,200-150,280,916 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23221 |
| Matched by | ensembl_id |

UniProt [Q8WWF1](https://www.uniprot.org/uniprotkb/Q8WWF1) carries no function annotation.

**Summary**, from NCBI Gene [79630](https://www.ncbi.nlm.nih.gov/gene/79630):

> Predicted to be involved in phosphatidylinositol 3-kinase/protein kinase B signal transduction. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26258) · Entrez [79630](https://www.ncbi.nlm.nih.gov/gene/79630) · UniProt [Q8WWF1](https://www.uniprot.org/uniprotkb/Q8WWF1) · Ensembl [ENSG00000118292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118292)

## Data

Gene col 3979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3979); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3979]; `tensor/DDL_lfc|DDL_z.npy` [3979]; `embed/gene_vectors.npy` [3979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3979 or target_col == 3979). Every well: [[C1orf54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
