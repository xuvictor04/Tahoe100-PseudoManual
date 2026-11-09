---
symbol: "LSAMP"
type: "gene"
col: 11697
ensembl_id: "ENSG00000185565"
name: "limbic system associated membrane protein"
location: "3q13.31"
module: 19
arm: "+"
pooled_cpm: 105.8
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 22
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LSAMP

*limbic system associated membrane protein* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +14.3, q 1e-43, up in 20 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +13.0, q 6e-36, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.674× (z -6.1, q 5e-07, down in 19 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH15]] (+0.73, fdr 7e-06), [[NKAIN2]] (+0.68, fdr 1e-05), [[TENM1]] (+0.68, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[POU6F2]] → it (grade B ⚠); 10 go from it, the strongest it → [[AGBL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +14.3 | 1e-43 | 20/29 (A-427, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +13.0 | 6e-36 | 16/30 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +10.0 | 3e-21 | 14/25 (HS-578T, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +9.1 | 1e-17 | 13/25 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.5 | 4e-06 | 12/29 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.3 | 9e-06 | 12/31 (HS-578T, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 13/29 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 6e-05 | 9/29 (A549, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.32×** | +4.3 | 1e-03 | 6/28 (A549, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.018 | 6/29 (A549, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.4 | 0.035 | 9/28 (C32, COLO 205, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.2 | 0.065 | 8/30 (CFPAC-1, C32, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.11 | 1/29 (HepG2/C3A) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -6.1 | 5e-07 | 19/29 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.805×** | -4.8 | 5e-04 | 9/29 (LS 180, SHP-77, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.744×** | -4.6 | 7e-04 | 16/29 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.746×** | -4.6 | 7e-04 | 14/29 (LOX-IMVI, CHP-212, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.4 | 0.001 | 0/31 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.852× | -3.5 | 0.039 | 8/29 (LS 180, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.045 | 10/29 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.071 | 3/29 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 0.814× | -3.1 | 0.13 | 10/29 (NCI-H460, C32, …) | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 1,617 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 816 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -14.3) |
| [[C32 (line)]] | wt | 196 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~96% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.254× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 433 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 1,220 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.7) |
| [[A-427 (line)]] | wt | 28.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 54.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.0549× (z -11.9) |
| [[SHP-77 (line)]] | alt | 451 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 50.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 40.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 25.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH15]] | +0.73 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[NKAIN2]] | +0.68 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[TENM1]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CASC15]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[IQCM]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[CDH7]] | +0.66 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[KCNJ6]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[MSR1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PCDH9]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[RIMS1]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[KCNMB2]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 19, C 3. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU6F2]] | B | POU6F2 activity raises LSAMP's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.35× lower at baseline in the lines without POU6F2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[FGF13]] | B | FGF13 activity raises LSAMP's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 3.32× lower at baseline in the lines without FGF13 | 0.008 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[MIR4307HG]] | B | MIR4307HG activity raises LSAMP's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 3.00× lower at baseline in the lines without MIR4307HG | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |
| [[DPP10]] | B | DPP10 activity raises LSAMP's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.96× lower at baseline in the lines without DPP10 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[NKAIN2]] | B | NKAIN2 activity raises LSAMP's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 3.29× lower at baseline in the lines without NKAIN2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent |
| [[KCNH5]] | B | KCNH5 activity raises LSAMP's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.13× lower at baseline in the lines without KCNH5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D |
| [[ADGRL3]] | B | ADGRL3 activity raises LSAMP's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without ADGRL3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[LINC01257]] | B | LINC01257 activity raises LSAMP's level | lines that do not express LINC01257 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without LINC01257 | 0.034 | ⚠ within organs, on part of the lines; also absent: MIR3667HG, LINC01446, NAA11; maybe low, not absent |
| [[NKAIN2]] | B | NKAIN2 activity weakens LSAMP's drug response | lines that do not express NKAIN2 (19) vs lines expressing it (12) | (z diff -3.94); strongest at Idarubicin (hydrochloride) 5 µM: 1.51x vs 0.47x (z diff -8.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PDE1A]] | B | PDE1A activity raises LSAMP's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.49× lower at baseline in the lines without PDE1A | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[GSG1L2]] | B | GSG1L2 activity raises LSAMP's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.61× lower at baseline in the lines without GSG1L2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[LINC03000]] | B | LINC03000 activity raises LSAMP's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 4.41× lower at baseline in the lines without LINC03000 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGBL1]] | B | LSAMP activity raises AGBL1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without LSAMP | 0.037 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[NCKAP5]] | B | LSAMP activity raises NCKAP5's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without LSAMP | 0.049 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[SERPINB2]] | B | LSAMP activity raises SERPINB2's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.87× lower at baseline in the lines without LSAMP | 0.062 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[FBXL7]] | B | LSAMP activity raises FBXL7's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 3.67× lower at baseline in the lines without LSAMP | 0.073 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[KCNH5]] | B | LSAMP activity raises KCNH5's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LSAMP | 0.077 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[NTNG1]] | B | LSAMP activity raises NTNG1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LSAMP | 0.090 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[TNFRSF19]] | B | LSAMP activity raises TNFRSF19's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without LSAMP | 0.097 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[PRKG1]] | B | LSAMP activity raises PRKG1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without LSAMP | 0.099 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[PCDH9]] | C | LSAMP activity raises PCDH9's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 3.96× lower at baseline in the lines without LSAMP | 0.007 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent; co-absent with the target |
| [[IGSF1]] | C | LSAMP activity raises IGSF1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 4.09× lower at baseline in the lines without LSAMP | 0.075 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, 34.0); signed map (42.0, 39.3). **Vector** length 79.2, 18.0% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.3 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | limbic system associated membrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:115,802,374-117,139,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAMP, IGLON3 |
| Gene groups (HGNC) | I-set domain containing; IgLON cell adhesion molecules |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13449](https://www.uniprot.org/uniprotkb/Q13449) (Limbic system-associated membrane protein):

> Mediates selective neuronal growth and axon targeting. Contributes to the guidance of developing axons and remodeling of mature circuits in the limbic system. Essential for normal growth of the hippocampal mossy fiber projection (By similarity).

**Summary**, from NCBI Gene [4045](https://www.ncbi.nlm.nih.gov/gene/4045):

> This gene encodes a member of the immunoglobulin LAMP, OBCAM and neurotrimin (IgLON) family of proteins. The encoded preproprotein is proteolytically processed to generate a neuronal surface glycoprotein. This protein may act as a selective homophilic adhesion molecule during axon guidance and neuronal growth in the developing limbic system. The encoded protein may also function as a tumor suppressor and may play a role in neuropsychiatric disorders. Alternative splicing results in multiple …

**Accessions** — [HGNC:6705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6705) · Entrez [4045](https://www.ncbi.nlm.nih.gov/gene/4045) · UniProt [Q13449](https://www.uniprot.org/uniprotkb/Q13449) · Ensembl [ENSG00000185565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185565)

## Data

Gene col 11697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11697); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11697]; `tensor/DDL_lfc|DDL_z.npy` [11697]; `embed/gene_vectors.npy` [11697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11697 or target_col == 11697). Every well: [[LSAMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSAMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
