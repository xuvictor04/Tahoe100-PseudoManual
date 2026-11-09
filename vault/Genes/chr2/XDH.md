---
symbol: "XDH"
type: "gene"
col: 8135
ensembl_id: "ENSG00000158125"
name: "xanthine dehydrogenase"
location: "2p23.1"
module: 8
arm: "+"
pooled_cpm: 22.35
n_lines_expressing: 28
n_dd_up: 4
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 52
direction_downstream: 34
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# XDH

*xanthine dehydrogenase* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +9.9, q 2e-20, up in 16 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.442× (z -10.5, q 6e-23, down in 24 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARID]] (+0.65, fdr 7e-06), [[CYP24A1]] (+0.63, fdr 1e-05), [[SLC28A3]] (+0.63, fdr 7e-06); moves opposite to [[TET1]] (-0.45, fdr 4e-05), [[FAM228B]] (-0.44, fdr 5e-05), [[PKD1L1-AS1]] (-0.43, fdr 3e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[SPATA6L]] → it (grade B ⚠); 34 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +9.9 | 2e-20 | 16/26 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +7.1 | 3e-10 | 12/25 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.8 | 0.028 | 0/16 | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.085 | 1/23 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.25 | 8/25 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.442×** | -10.5 | 6e-23 | 24/25 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.503×** | -8.8 | 4e-16 | 19/24 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.514×** | -8.5 | 3e-15 | 23/25 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.520×** | -7.8 | 1e-12 | 12/25 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.555×** | -7.6 | 5e-12 | 16/25 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.589×** | -6.8 | 1e-09 | 17/25 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -6.8 | 1e-09 | 16/24 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -5.8 | 4e-07 | 22/27 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.635×** | -5.8 | 4e-07 | 18/26 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.677×** | -5.0 | 3e-05 | 5/24 (SHP-77, A549, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -4.7 | 1e-04 | 17/24 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.692×** | -4.7 | 1e-04 | 16/26 (A549, CFPAC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -4.7 | 1e-04 | 17/25 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.781×** | -4.5 | 3e-04 | 14/26 (COLO 205, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.723×** | -4.3 | 6e-04 | 13/27 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.741×** | -3.8 | 0.004 | 9/25 (LS 180, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 158 | 0 | 19 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0197× (z -23.4) |
| [[A549 (line)]] | wt | 77.0 | 0 | 16 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -30.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.111× (z -15.5) |
| [[HT-29 (line)]] | alt | 61.2 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0400× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.109× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 59.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 43.4 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -10.6) |
| [[LS 180 (line)]] | wt | 54.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.211× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -18.8) |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.218× (z -8.6) |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.123× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 8.31 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0960× (z -10.5) |
| [[BT-474 (line)]] | alt | 11.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 0.5 µM 0.0347× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.239× (z -9.4) |
| [[KATO III (line)]] | alt | 13.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.51× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.487× (z -9.1) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 14.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.44× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 6.96 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.4) |
| [[A-172 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARID]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[CYP24A1]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[SLC28A3]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Azathioprine ADME |
| [[HSH2D]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LINC00540]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GPR141]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[RGS6]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SIPA1L2]] | +0.57 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[LIPH]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ST6GAL2]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CATSPERB]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TET1]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[FAM228B]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[PKD1L1-AS1]] | -0.43 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[LINC02226]] | -0.43 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 22, C 30. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA6L]] | B | SPATA6L activity raises XDH's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.40× lower at baseline in the lines without SPATA6L | 0.006 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[LINC01348]] | B | LINC01348 activity raises XDH's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 2.92× lower at baseline in the lines without LINC01348 | 0.009 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[SLC28A3]] | B | SLC28A3 activity raises XDH's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without SLC28A3 | 0.010 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[SRMS]] | B | SRMS activity raises XDH's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.26× lower at baseline in the lines without SRMS | 0.019 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[IL1RN]] | B | IL1RN activity raises XDH's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without IL1RN | 0.022 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises XDH's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.85× lower at baseline in the lines without ELF3-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises XDH's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without NOSTRIN | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[ADCY4]] | B | ADCY4 activity raises XDH's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.62× lower at baseline in the lines without ADCY4 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[UPK1B]] | B | UPK1B activity raises XDH's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without UPK1B | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent |
| [[RAB27B]] | B | RAB27B activity raises XDH's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.91× lower at baseline in the lines without RAB27B | 0.039 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[CEACAM1]] | B | CEACAM1 activity raises XDH's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.88× lower at baseline in the lines without CEACAM1 | 0.053 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[RBM47]] | B | RBM47 activity raises XDH's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.97× lower at baseline in the lines without RBM47 | 0.057 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 16, C 18. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | XDH activity raises FAM83E's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.25× lower at baseline in the lines without XDH | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[FRMD4B]] | B | XDH activity raises FRMD4B's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without XDH | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[INPP4B]] | B | XDH activity weakens INPP4B's drug response | lines that do not express XDH (16) vs lines expressing it (23) | the lines without XDH respond 0.79× as strongly (z diff +0.96); strongest at Selinexor 0.5 µM: 2.34x vs 1.55x (z diff -3.3) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564; target measured in part of the lines; both ways; artifact flags |
| [[TET1]] | B | XDH activity lowers TET1's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.96× higher at baseline in the lines without XDH | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[FAM228B]] | B | XDH activity lowers FAM228B's level | lines that do not express XDH (22) vs lines expressing it (28) | 1.54× higher at baseline in the lines without XDH | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[SLC28A3]] | B | XDH activity raises SLC28A3's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without XDH | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[ELF3-AS1]] | B | XDH activity raises ELF3-AS1's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without XDH | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[ABCC3]] | B | XDH activity raises ABCC3's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.96× lower at baseline in the lines without XDH | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[KLF5]] | B | XDH activity raises KLF5's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.73× lower at baseline in the lines without XDH | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[PTK6]] | B | XDH activity raises PTK6's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.54× lower at baseline in the lines without XDH | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[PI3]] | B | XDH activity raises PI3's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without XDH | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[FAM228B]] | B | XDH activity weakens FAM228B's drug response | lines that do not express XDH (22) vs lines expressing it (27) | the lines without XDH respond 1.39× as strongly (z diff -1.47); strongest at Digitoxin 5 µM: 0.32x vs 0.44x (z diff -2.0) | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.9, 45.8); signed map (52.8, 25.1). **Vector** length 87.6, 23.4% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.6 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -7.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -7.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | xanthine dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:31,334,321-31,414,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XOR, XO, XDH/XO |
| Gene groups (HGNC) | Flavoproteins; Xanthine dehydrogenase/aldehyde oxidase family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 7 pathways, smallest: Butyrophilin (BTN) family interactions; Purine catabolism; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P47989](https://www.uniprot.org/uniprotkb/P47989) (Xanthine dehydrogenase/oxidase):

> Key enzyme in purine degradation. Catalyzes the oxidation of hypoxanthine to xanthine. Catalyzes the oxidation of xanthine to uric acid. Contributes to the generation of reactive oxygen species. Has also low oxidase activity towards aldehydes (in vitro).

**Summary**, from NCBI Gene [7498](https://www.ncbi.nlm.nih.gov/gene/7498):

> Xanthine dehydrogenase belongs to the group of molybdenum-containing hydroxylases involved in the oxidative metabolism of purines. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. Xanthine dehydrogenase can be converted to xanthine oxidase by reversible sulfhydryl oxidation or by irreversible proteolytic modification. Defects in xanthine dehydrogenase cause xanthinuria, may contribute to adult respiratory …

**Accessions** — [HGNC:12805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12805) · Entrez [7498](https://www.ncbi.nlm.nih.gov/gene/7498) · UniProt [P47989](https://www.uniprot.org/uniprotkb/P47989) · Ensembl [ENSG00000158125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158125)

## Data

Gene col 8135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8135); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8135]; `tensor/DDL_lfc|DDL_z.npy` [8135]; `embed/gene_vectors.npy` [8135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8135 or target_col == 8135). Every well: [[XDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
