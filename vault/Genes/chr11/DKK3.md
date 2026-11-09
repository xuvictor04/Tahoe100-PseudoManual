---
symbol: "DKK3"
type: "gene"
col: 561
ensembl_id: "ENSG00000050165"
name: "dickkopf Wnt signaling pathway inhibitor 3"
location: "11p15.3"
module: 13
arm: "+"
pooled_cpm: 24.49
n_lines_expressing: 21
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 58
direction_downstream: 65
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# DKK3

*dickkopf Wnt signaling pathway inhibitor 3* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.18× (z +18.1, q 0e+00, up in 14 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +9.3, q 3e-18, up in 14 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.607× (z -8.9, q 2e-16, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.75, fdr 7e-06), [[SCUBE3]] (+0.72, fdr 7e-06), [[PRSS23]] (+0.70, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[DENND2A]] → it (grade B ⚠); 65 go from it, the strongest it → [[PRSS23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.18×** | +18.1 | 0e+00 | 14/17 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +16.8 | 0e+00 | 10/12 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +9.4 | 7e-19 | 9/13 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +9.3 | 3e-18 | 14/19 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.2 | 7e-11 | 3/17 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +6.9 | 6e-10 | 8/18 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +5.4 | 5e-06 | 5/11 (HS-578T, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.6 | 3e-04 | 3/18 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **1.34×** | +3.7 | 0.012 | 1/15 (HOP62) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.013 | 6/19 (H4, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Erythromycin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.026 | 0/19 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.3 | 0.040 | 1/15 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.049 | 1/18 (SW 900) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.049 | 8/16 (H4, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.607×** | -8.9 | 2e-16 | 17/19 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -6.9 | 2e-09 | 17/19 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -6.7 | 5e-09 | 15/19 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -4.9 | 1e-04 | 17/18 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.685×** | -4.8 | 2e-04 | 11/19 (H4, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.750×** | -3.6 | 0.026 | 7/19 (H4, HOP62, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.755×** | -3.6 | 0.030 | 1/18 (SW 1271) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.758×** | -3.5 | 0.030 | 12/19 (NCI-H1792, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.761×** | -3.5 | 0.030 | 12/19 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.761×** | -3.5 | 0.030 | 0/19 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.768× | -3.1 | 0.11 | 1/19 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 81.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0853× (z -19.9) |
| [[HOP62 (line)]] | alt | 20.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.3) |
| [[PANC-1 (line)]] | alt | 34.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.0) |
| [[A-172 (line)]] | wt | 368 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.9) |
| [[Hs 766T (line)]] | wt | 87.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 73.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.7) |
| [[SW 1088 (line)]] | alt | 318 | 0 | 3 | — | [[Verteporfin (drug)]] 5 µM 0.0780× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 229 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.2) |
| [[A549 (line)]] | wt | 8.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 9.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -10.2) |
| [[A-427 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SCUBE3]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PRSS23]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SPARC]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[THBS2]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[COL1A2]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[NID2]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NMNAT2]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[COL6A1]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[COL6A3]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MMP2]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PCDHGC3]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 3, C 55. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND2A]] | B | DENND2A activity raises DKK3's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.67× lower at baseline in the lines without DENND2A | 0.091 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[RNF152]] | B | RNF152 activity raises DKK3's level | lines that do not express RNF152 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without RNF152 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, SNCAIP, OR9Q1; maybe low, not absent |
| [[SCARA3]] | B | SCARA3 activity raises DKK3's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 2.48× lower at baseline in the lines without SCARA3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[COL5A1]] | C | COL5A1 activity raises DKK3's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 8.47× lower at baseline in the lines without COL5A1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises DKK3's level | lines that do not express HHIP (33) vs lines expressing it (17) | 6.24× lower at baseline in the lines without HHIP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises DKK3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 11.34× lower at baseline in the lines without LINC01411 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises DKK3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 6.49× lower at baseline in the lines without ITGA11 | 0.003 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises DKK3's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 6.06× lower at baseline in the lines without INSYN2B | 0.003 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises DKK3's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 5.76× lower at baseline in the lines without PTGFR | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises DKK3's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 7.06× lower at baseline in the lines without SIRLNT | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises DKK3's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 6.37× lower at baseline in the lines without MMP2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises DKK3's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 3.84× lower at baseline in the lines without CSPG4 | 0.007 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |

### Downstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 12, C 53. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | DKK3 activity raises PRSS23's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without DKK3 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[LINC01119]] | B | DKK3 activity raises LINC01119's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without DKK3 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[LTBP1]] | B | DKK3 activity raises LTBP1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without DKK3 | 0.028 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[F2R]] | B | DKK3 activity raises F2R's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without DKK3 | 0.035 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[LINC01119]] | B | DKK3 activity strengthens LINC01119's drug response | lines that do not express DKK3 (24) vs lines expressing it (19) | the lines without DKK3 respond 0.57× as strongly (z diff +1.31); strongest at Panobinostat 0.5 µM: 0.63x vs 0.29x (z diff +2.9) | 0.042 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; target measured in part of the lines; artifact flags |
| [[PRAF2]] | B | DKK3 activity raises PRAF2's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without DKK3 | 0.053 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[SCARA3]] | B | DKK3 activity raises SCARA3's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without DKK3 | 0.054 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[CREB3L1]] | B | DKK3 activity raises CREB3L1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without DKK3 | 0.058 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[DENND2A]] | B | DKK3 activity raises DENND2A's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.41× lower at baseline in the lines without DKK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[FKBP7]] | B | DKK3 activity raises FKBP7's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without DKK3 | 0.074 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[ANXA6]] | B | DKK3 activity raises ANXA6's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without DKK3 | 0.080 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[CERCAM]] | B | DKK3 activity raises CERCAM's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.12× lower at baseline in the lines without DKK3 | 0.094 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.1, 19.1); signed map (24.5, 43.5). **Vector** length 67.2, 22.3% of its response variance represented; |z| ≥ 3 in 458 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen formation* (reactome, mean cos +0.51 to 12); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.53 to 10); *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.54 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | dickkopf Wnt signaling pathway inhibitor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:11,956,207-12,009,769 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REIC, RIG, CRRL |
| Gene groups (HGNC) | Dickkopf family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBP4](https://www.uniprot.org/uniprotkb/Q9UBP4) (Dickkopf-related protein 3):

> Antagonizes canonical Wnt signaling by inhibiting LRP5/6 interaction with Wnt and by forming a ternary complex with the transmembrane protein KREMEN that promotes internalization of LRP5/6. DKKs play an important role in vertebrate development, where they locally inhibit Wnt regulated processes such as antero-posterior axial patterning, limb development, somitogenesis and eye formation. In the adult, Dkks are implicated in bone formation and bone disease, cancer and Alzheimer disease (By …

**Summary**, from NCBI Gene [27122](https://www.ncbi.nlm.nih.gov/gene/27122):

> This gene encodes a protein that is a member of the dickkopf family. The secreted protein contains two cysteine rich regions and is involved in embryonic development through its interactions with the Wnt signaling pathway. The expression of this gene is decreased in a variety of cancer cell lines and it may function as a tumor suppressor gene. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2893) · Entrez [27122](https://www.ncbi.nlm.nih.gov/gene/27122) · UniProt [Q9UBP4](https://www.uniprot.org/uniprotkb/Q9UBP4) · Ensembl [ENSG00000050165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050165)

## Data

Gene col 561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 561); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 561]; `tensor/DDL_lfc|DDL_z.npy` [561]; `embed/gene_vectors.npy` [561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 561 or target_col == 561). Every well: [[DKK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DKK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
