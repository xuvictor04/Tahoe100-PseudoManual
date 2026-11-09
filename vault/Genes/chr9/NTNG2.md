---
symbol: "NTNG2"
type: "gene"
col: 12184
ensembl_id: "ENSG00000196358"
name: "netrin G2"
location: "9q34.13"
module: 13
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 31
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 19
direction_downstream: 12
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NTNG2

*netrin G2* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.18× (z +21.8, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.05 µM: 0.559× (z -5.5, q 3e-05, down in 12 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF385D]] (+0.69, fdr 7e-06), [[GDNF-AS1]] (+0.68, fdr 1e-05), [[ANXA10]] (+0.68, fdr 1e-05); moves opposite to [[TTLL5]] (-0.53, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[RFX8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.18×** | +21.8 | 0e+00 | 16/19 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.3 | 3e-27 | 4/12 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +11.0 | 1e-25 | 3/8 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +9.9 | 5e-21 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +8.0 | 1e-13 | 7/22 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +6.7 | 3e-09 | 9/23 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.4 | 2e-08 | 14/26 (J82, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.2 | 1e-05 | 9/15 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.9 | 7e-05 | 5/26 (A-172, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +4.7 | 1e-04 | 1/13 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 0.001 | 6/19 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.006 | 5/20 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.018 | 2/22 (A-172, C32) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.5 | 0.020 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.075 | 5/27 (J82, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.097 | 8/23 (A-427, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.559×** | -5.5 | 3e-05 | 12/27 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -4.3 | 0.005 | 15/28 (H4, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.652×** | -4.0 | 0.010 | 9/23 (SHP-77, H4, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.661×** | -3.9 | 0.010 | 11/23 (SNU-423, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.664×** | -3.8 | 0.010 | 17/26 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.010 | 9/26 (PANC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -3.8 | 0.010 | 16/23 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.669×** | -3.6 | 0.021 | 12/25 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.037 | 13/24 (C-33 A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -3.4 | 0.038 | 13/26 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.711×** | -3.2 | 0.070 | 5/26 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.725× | -3.0 | 0.12 | 10/26 (SHP-77, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.167× (z -10.0) |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.204× (z -8.8) |
| [[A-172 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +11.7) | — |
| [[A498 (line)]] | wt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +8.9) | — |
| [[A549 (line)]] | wt | 5.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.5) | — |
| [[H4 (line)]] | wt | 7.84 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0638× (z -9.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0778× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.45 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.05 µM 0.0640× (z -8.7) |
| [[SNU-423 (line)]] | alt | 3.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +8.8) | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.993 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF385D]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[GDNF-AS1]] | +0.68 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ANXA10]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[IL11]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[VAT1L]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ITGA11]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[GDNF]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SYNDIG1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[GPR68]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PLXNA4]] | +0.61 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[IL1B]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 6, C 13. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NTNG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM200A]] | B | TMEM200A activity raises NTNG2's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without TMEM200A | 0.052 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[SAMD3]] | B | SAMD3 activity raises NTNG2's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without SAMD3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[RASGRF2]] | B | RASGRF2 activity raises NTNG2's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 1.53× lower at baseline in the lines without RASGRF2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[LINC02813]] | B | LINC02813 activity raises NTNG2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without LINC02813 | 0.078 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[PSMB5]] | B | PSMB5 activity raises NTNG2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[INSYN2B]] | C | INSYN2B activity raises NTNG2's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without INSYN2B | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises NTNG2's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.64× lower at baseline in the lines without PLEKHG4B | 0.007 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[SFRP1]] | C | SFRP1 activity raises NTNG2's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 2.36× lower at baseline in the lines without SFRP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises NTNG2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without ITGA11 | 0.009 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[RASSF8-AS1]] | C | RASSF8-AS1 activity raises NTNG2's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 2.84× lower at baseline in the lines without RASSF8-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804; co-absent with the target |
| [[ADAMTS18]] | C | ADAMTS18 activity raises NTNG2's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without ADAMTS18 | 0.043 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX8]] | B | NTNG2 activity raises RFX8's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.00× lower at baseline in the lines without NTNG2 | 0.084 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8 |
| [[TSHZ3]] | C | NTNG2 activity raises TSHZ3's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 6.90× lower at baseline in the lines without NTNG2 | 0.004 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[RASSF8-AS1]] | C | NTNG2 activity raises RASSF8-AS1's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.37× lower at baseline in the lines without NTNG2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[TSHZ3-AS1]] | C | NTNG2 activity raises TSHZ3-AS1's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.28× lower at baseline in the lines without NTNG2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[MRC2]] | C | NTNG2 activity raises MRC2's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 4.70× lower at baseline in the lines without NTNG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[INSYN2B]] | C | NTNG2 activity raises INSYN2B's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 4.38× lower at baseline in the lines without NTNG2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[PLEKHG4B]] | C | NTNG2 activity raises PLEKHG4B's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.82× lower at baseline in the lines without NTNG2 | 0.041 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[SFRP1]] | C | NTNG2 activity raises SFRP1's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.85× lower at baseline in the lines without NTNG2 | 0.056 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[VAT1L]] | C | NTNG2 activity raises VAT1L's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without NTNG2 | 0.086 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[NKAIN3]] | C | NTNG2 activity raises NKAIN3's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without NTNG2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[VSTM4]] | C | NTNG2 activity raises VSTM4's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 2.75× lower at baseline in the lines without NTNG2 | 0.095 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[FGF5]] | C | NTNG2 activity raises FGF5's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.08× lower at baseline in the lines without NTNG2 | 0.098 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.2, 14.0); signed map (18.6, 48.9). **Vector** length 58.8, 12.5% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +21.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | netrin G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,162,058-132,244,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1857, Lmnt2, NetrinG2; previously NTNG1 |
| Gene groups (HGNC) | Netrins |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CW9](https://www.uniprot.org/uniprotkb/Q96CW9) (Netrin-G2):

> Involved in controlling patterning and neuronal circuit formation at the laminar, cellular, subcellular and synaptic levels. Promotes neurite outgrowth of both axons and dendrites.

**Summary**, from NCBI Gene [84628](https://www.ncbi.nlm.nih.gov/gene/84628):

> Predicted to enable cell-cell adhesion mediator activity. Predicted to be involved in several processes, including regulation of cell projection organization; regulation of neuron migration; and synaptic membrane adhesion. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14288) · Entrez [84628](https://www.ncbi.nlm.nih.gov/gene/84628) · UniProt [Q96CW9](https://www.uniprot.org/uniprotkb/Q96CW9) · Ensembl [ENSG00000196358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196358)

## Data

Gene col 12184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12184); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12184]; `tensor/DDL_lfc|DDL_z.npy` [12184]; `embed/gene_vectors.npy` [12184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12184 or target_col == 12184). Every well: [[NTNG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTNG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
