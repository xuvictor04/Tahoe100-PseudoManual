---
symbol: "PDE4DIPP2"
type: "gene"
col: 15843
ensembl_id: "ENSG00000275131"
name: "PDE4DIP pseudogene 2"
location: "1p11.2"
module: 13
arm: "+"
pooled_cpm: 17.68
n_lines_expressing: 42
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 22
direction_downstream: 1
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PDE4DIPP2

*PDE4DIP pseudogene 2* — 1p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +7.4, q 1e-10, up in 20 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.648× (z -5.8, q 4e-06, down in 19 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE4DIP]] (+0.77, fdr 7e-06), [[NLRP3]] (+0.65, fdr 7e-06), [[ADAMTS6]] (+0.64, fdr 7e-06); moves opposite to [[NCOA2]] (-0.45, fdr 4e-05), [[KDM3B]] (-0.45, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[FAM167A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PDE4DIP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.4 | 1e-10 | 20/40 (RKO, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 6e-09 | 18/38 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +5.3 | 2e-05 | 13/40 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.035 | 9/40 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.047 | 10/39 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.067 | 6/40 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.089 | 6/39 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 1.57× | +3.1 | 0.11 | 3/39 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.26× | +3.1 | 0.11 | 6/38 (H4, Hs 766T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.26× | +3.1 | 0.11 | 12/40 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.11 | 7/38 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.11 | 10/40 (NCI-H1573, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.54× | +3.0 | 0.11 | 8/40 (HOP62, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.11 | 10/40 (RPMI-7951, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -5.8 | 4e-06 | 19/40 (SNU-1, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -5.5 | 1e-05 | 20/39 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.723×** | -4.3 | 0.003 | 17/28 (A-172, SNU-423, …) | inconsistent across doses | composition shift; position effect removed |
| [[Thymol (drug)]] 5 µM |  | **0.800×** | -4.2 | 0.003 | 14/40 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.744×** | -3.9 | 0.009 | 13/40 (NCI-H23, H4, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -3.8 | 0.013 | 16/31 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.668×** | -3.6 | 0.025 | 13/37 (SK-MEL-2, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.766×** | -3.6 | 0.026 | 10/40 (HCT15, NCI-H1573, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.771×** | -3.5 | 0.033 | 11/40 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.778×** | -3.4 | 0.044 | 16/39 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.690×** | -3.3 | 0.045 | 8/37 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.792×** | -3.1 | 0.087 | 12/37 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 132 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.619× (z -10.9) ⚠ position not correctable · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.254× (z -8.7) |
| [[SNU-423 (line)]] | alt | 56.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.171× (z -8.9) |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.101× (z -10.0) |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE4DIP]] | +0.77 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[NLRP3]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[RGMB]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[RPSAP52]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[FGF5]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SPOCK1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RFX8]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ENTPD7]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CSMD2]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA2]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[KDM3B]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM167A]] | B | FAM167A activity raises PDE4DIPP2's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without FAM167A | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[MME]] | B | MME activity raises PDE4DIPP2's level | lines that do not express MME (30) vs lines expressing it (20) | 2.91× lower at baseline in the lines without MME | 0.008 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[RFX8]] | B | RFX8 activity raises PDE4DIPP2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.24× lower at baseline in the lines without RFX8 | 0.021 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[SIGLEC15]] | B | SIGLEC15 activity raises PDE4DIPP2's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without SIGLEC15 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |
| [[IL11]] | B | IL11 activity raises PDE4DIPP2's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without IL11 | 0.032 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[RPSAP52]] | B | RPSAP52 activity raises PDE4DIPP2's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without RPSAP52 | 0.036 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[CDH13]] | B | CDH13 activity raises PDE4DIPP2's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.64× lower at baseline in the lines without CDH13 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[LINC01411]] | B | LINC01411 activity raises PDE4DIPP2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.31× lower at baseline in the lines without LINC01411 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[NLRP3]] | B | NLRP3 activity raises PDE4DIPP2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without NLRP3 | 0.044 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[TMEM200A]] | B | TMEM200A activity raises PDE4DIPP2's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TMEM200A | 0.052 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[LINC02970]] | B | LINC02970 activity raises PDE4DIPP2's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without LINC02970 | 0.054 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595 |
| [[RDUR]] | B | RDUR activity raises PDE4DIPP2's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.47× lower at baseline in the lines without RDUR | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4DIP]] | B | PDE4DIPP2 activity raises PDE4DIP's level | lines that do not express PDE4DIPP2 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without PDE4DIPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: INTS6L, IQCJ-SCHIP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 13.2); signed map (17.7, 47.4). **Vector** length 76.0, 15.2% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +3.0 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -5.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PDE4DIP pseudogene 2 |
| Locus type | pseudogene |
| Location | 1p11.2 — chr1:120,489,860-120,701,289 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55081) · Entrez [100996724](https://www.ncbi.nlm.nih.gov/gene/100996724) · Ensembl [ENSG00000275131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275131)

## Data

Gene col 15843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15843); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15843]; `tensor/DDL_lfc|DDL_z.npy` [15843]; `embed/gene_vectors.npy` [15843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15843 or target_col == 15843). Every well: [[PDE4DIPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE4DIPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
