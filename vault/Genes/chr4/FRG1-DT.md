---
symbol: "FRG1-DT"
type: "gene"
col: 14440
ensembl_id: "ENSG00000245685"
name: "FRG1 divergent transcript"
location: "4q35.2"
module: 10
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 43
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FRG1-DT

*FRG1 divergent transcript* — 4q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.84× (z +6.5, q 4e-08, up in 18 of 39 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +5.1, q 7e-05, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.390× (z -7.1, q 5e-10, down in 26 of 40 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.394× (z -7.1, q 5e-10, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD31]] (+0.76, fdr 7e-06), [[DPH6-DT]] (+0.72, fdr 1e-05), [[CNTLN]] (+0.70, fdr 1e-05); moves opposite to [[LCMT1]] (-0.64, fdr 9e-05), [[GMCL1]] (-0.62, fdr 4e-05), [[MPG]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC00886]] → it (grade B ⚠); 11 go from it, the strongest it → [[CCDC171]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.84×** | +6.5 | 4e-08 | 18/39 (LS 180, NCI-H460, …) | rises with dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +5.8 | 2e-06 | 6/9 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +5.1 | 7e-05 | 19/35 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.5 | 8e-04 | 12/35 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.3 | 0.002 | 11/40 (A-172, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.73×** | +4.1 | 0.003 | 16/38 (NCI-H2030, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +4.1 | 0.003 | 4/11 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.012 | 14/40 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.76×** | +3.6 | 0.017 | 12/37 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +3.3 | 0.048 | 11/20 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.065 | 7/40 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.078 | 8/39 (C32, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.390×** | -7.1 | 5e-10 | 26/40 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.394×** | -7.1 | 5e-10 | 26/38 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.400×** | -6.9 | 8e-10 | 27/38 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.504×** | -5.2 | 3e-05 | 20/32 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.563×** | -4.4 | 0.002 | 20/39 (AN3 CA, NCI-H2030, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.577×** | -4.2 | 0.003 | 19/38 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.533×** | -4.0 | 0.004 | 14/39 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.608×** | -3.8 | 0.012 | 21/39 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -3.6 | 0.018 | 12/38 (A498, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -3.4 | 0.038 | 14/39 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.649×** | -3.3 | 0.055 | 8/37 (SNU-1, NCI-H23, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.742×** | -3.2 | 0.068 | 12/39 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.452×** | -3.1 | 0.073 | 16/38 (LoVo, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -3.1 | 0.079 | 13/33 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.622×** | -3.1 | 0.085 | 6/39 (SW 1271, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0335× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.0505× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 39.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 7.81 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0961× (z -8.8) |
| [[A498 (line)]] | wt | 3.62 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0530× (z -8.8) |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0477× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 6.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +8.6) | — |
| [[LoVo (line)]] | wt | 2.51 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0491× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.95 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0842× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 9.61 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0534× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 5.11 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +11.3) | — |
| [[A-172 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD31]] | +0.76 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.72 | +0.74 / +0.51 | both halves | 1e-05 | same gene group |
| [[CNTLN]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.70 | +0.68 / +0.50 | both halves | 1e-05 | same gene group |
| [[PCNX4-DT]] | +0.70 | +0.68 / +0.49 | both halves | 1e-05 | same gene group |
| [[EIF1B-AS1]] | +0.70 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[MAD2L1-DT]] | +0.68 | +0.73 / +0.36 | both halves | 1e-04 | same gene group |
| [[ANKRD18B]] | +0.68 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[ANKS1B]] | +0.68 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[KATNAL2]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[FTCDNL1]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[GTF3C6]] | +0.67 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.64 | -0.62 / -0.37 | both halves | 9e-05 |  |
| [[GMCL1]] | -0.62 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[MPG]] | -0.60 | -0.69 / -0.30 | both halves | 2e-04 |  |
| [[SLC17A5]] | -0.59 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[KLHL7]] | -0.58 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00886]] | B | LINC00886 activity raises FRG1-DT's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.75× lower at baseline in the lines without LINC00886 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[PCDHA6]] | B | PCDHA6 activity raises FRG1-DT's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.27× lower at baseline in the lines without PCDHA6 | 0.021 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[ANKRD18B]] | B | ANKRD18B activity raises FRG1-DT's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without ANKRD18B | 0.030 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[ANKS1B]] | B | ANKS1B activity raises FRG1-DT's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without ANKS1B | 0.086 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[LINC01088]] | B | LINC01088 activity raises FRG1-DT's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without LINC01088 | 0.098 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |
| [[PARD3B]] | B | PARD3B activity lowers FRG1-DT's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 1.10× higher at baseline in the lines without PARD3B | 0.098 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC171]] | B | FRG1-DT activity raises CCDC171's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without FRG1-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[CTBP1-DT]] | B | FRG1-DT activity raises CTBP1-DT's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.37× lower at baseline in the lines without FRG1-DT | 0.043 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[KIAA0825]] | B | FRG1-DT activity raises KIAA0825's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 2.23× lower at baseline in the lines without FRG1-DT | 0.047 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[LINC01515]] | B | FRG1-DT activity raises LINC01515's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.11× lower at baseline in the lines without FRG1-DT | 0.049 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[MYL5]] | B | FRG1-DT activity raises MYL5's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without FRG1-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[ANKRD18B]] | B | FRG1-DT activity raises ANKRD18B's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.05× lower at baseline in the lines without FRG1-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[SNHG14]] | B | FRG1-DT activity raises SNHG14's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.31× lower at baseline in the lines without FRG1-DT | 0.074 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[CCDC171]] | B | FRG1-DT activity strengthens CCDC171's drug response | lines that do not express FRG1-DT (6) vs lines expressing it (39) | the lines without FRG1-DT respond 0.83× as strongly (z diff +1.78); strongest at Digitoxin 5 µM: 0.50x vs 0.19x (z diff +5.3) | 0.086 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC01341]] | B | FRG1-DT activity raises LINC01341's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without FRG1-DT | 0.090 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[HHAT]] | C | FRG1-DT activity raises HHAT's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.40× lower at baseline in the lines without FRG1-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent; co-absent with the target |
| [[CNTLN]] | C | FRG1-DT activity raises CNTLN's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 4.50× lower at baseline in the lines without FRG1-DT | 0.078 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.2, 16.4); signed map (34.3, -10.1). **Vector** length 69.5, 13.7% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | FRG1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q35.2 — chr4:189,764,391-189,940,733 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51590) · Entrez [728339](https://www.ncbi.nlm.nih.gov/gene/728339) · Ensembl [ENSG00000245685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245685)

## Data

Gene col 14440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14440); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14440]; `tensor/DDL_lfc|DDL_z.npy` [14440]; `embed/gene_vectors.npy` [14440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14440 or target_col == 14440). Every well: [[FRG1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
