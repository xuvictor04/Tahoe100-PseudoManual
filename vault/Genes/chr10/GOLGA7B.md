---
symbol: "GOLGA7B"
type: "gene"
col: 7881
ensembl_id: "ENSG00000155265"
name: "golgin A7 family member B"
location: "10q24.2"
module: 158
arm: "+"
pooled_cpm: 9.77
n_lines_expressing: 36
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# GOLGA7B

*golgin A7 family member B* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.34× (z +19.7, q 0e+00, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.625× (z -6.6, q 2e-08, down in 21 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIF]] (+0.66, fdr 7e-06), [[ICAM2]] (+0.64, fdr 1e-05), [[SLC45A3]] (+0.63, fdr 9e-06).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SPNS2]] → it (grade B ⚠); 6 go from it, the strongest it → [[WNT7B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.34×** | +19.7 | 0e+00 | 23/32 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +9.0 | 6e-17 | 22/33 (NCI-H460, HOP62, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +8.0 | 2e-13 | 14/32 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +8.0 | 2e-13 | 19/33 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.99×** | +7.9 | 3e-13 | 21/32 (A498, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.3 | 2e-08 | 17/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +6.0 | 1e-07 | 16/32 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.53×** | +4.9 | 7e-05 | 16/32 (SK-MEL-2, SW48, …) | all doses, flat | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.49×** | +4.4 | 7e-04 | 7/32 (SHP-77, C32, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.03×** | +4.3 | 0.001 | 16/31 (A498, A-172, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.7 | 0.013 | 6/16 (SW480, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.085 | 12/32 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, none with an alert; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.625×** | -6.6 | 2e-08 | 21/33 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.629×** | -6.6 | 2e-08 | 18/33 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.610×** | -6.3 | 4e-08 | 19/34 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.677×** | -5.1 | 5e-05 | 17/34 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.637×** | -5.1 | 5e-05 | 15/32 (SW48, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.654×** | -5.0 | 7e-05 | 13/33 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.667×** | -4.7 | 2e-04 | 14/33 (NCI-H2347, SW 900, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.677×** | -4.4 | 8e-04 | 20/32 (NCI-H1573, AsPC-1, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.681×** | -4.1 | 0.002 | 8/32 (SW480, SW48, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.701×** | -4.1 | 0.002 | 16/32 (SW 900, A498, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **0.779×** | -4.1 | 0.002 | 8/33 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.780×** | -4.1 | 0.002 | 12/33 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.710×** | -4.0 | 0.003 | 12/32 (NCI-H1573, SW480, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.545×** | -3.7 | 0.009 | 11/29 (A549, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.009 | 10/32 (SW 900, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 78.2 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -10.3) |
| [[A498 (line)]] | wt | 6.71 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 9.36 | 0 | 2 | — | [[Trametinib (drug)]] 0.5 µM 0.193× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 10.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.272× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 3.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Vilanterol (drug)]] 0.5 µM 0.121× (z -11.8) |
| [[SW48 (line)]] | wt | 40.5 | 0 | 2 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0778× (z -9.5) |
| [[SW480 (line)]] | alt | 11.3 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.205× (z -9.4) |
| [[A-172 (line)]] | wt | 8.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.2) | — |
| [[H4 (line)]] | wt | 8.73 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0645× (z -8.9) |
| [[HOP62 (line)]] | alt | 4.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 5.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +9.0) | — |
| [[A-427 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIF]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ICAM2]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[CYB5R2]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[HCG20]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[IL23A]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[STK10]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R18]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZNF697]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TRPV3]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[EHD1]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPNS2]] | B | SPNS2 activity raises GOLGA7B's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without SPNS2 | 0.030 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[NAV2]] | B | NAV2 activity raises GOLGA7B's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without NAV2 | 0.030 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[CEMIP]] | B | CEMIP activity raises GOLGA7B's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.08× lower at baseline in the lines without CEMIP | 0.042 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[WNT7B]] | B | WNT7B activity raises GOLGA7B's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without WNT7B | 0.045 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[LAMC2]] | B | LAMC2 activity raises GOLGA7B's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without LAMC2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[MAP2K1]] | B | MAP2K1 activity raises GOLGA7B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[GRB10]] | B | GRB10 activity raises GOLGA7B's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without GRB10 | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[GOLGA7B-DT]] | C | GOLGA7B-DT activity raises GOLGA7B's level | lines that do not express GOLGA7B-DT (12) vs lines expressing it (38) | 3.64× lower at baseline in the lines without GOLGA7B-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: GOLGA7B, BCL11B, GJB2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT7B]] | B | GOLGA7B activity raises WNT7B's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 2.24× lower at baseline in the lines without GOLGA7B | 0.051 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent |
| [[CYTH4]] | B | GOLGA7B activity raises CYTH4's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 1.79× lower at baseline in the lines without GOLGA7B | 0.060 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent |
| [[LAMC2]] | B | GOLGA7B activity raises LAMC2's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 2.07× lower at baseline in the lines without GOLGA7B | 0.063 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent |
| [[SYNJ2]] | B | GOLGA7B activity raises SYNJ2's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without GOLGA7B | 0.070 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent |
| [[PLEKHG3]] | B | GOLGA7B activity raises PLEKHG3's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 1.10× lower at baseline in the lines without GOLGA7B | 0.089 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent |
| [[GOLGA7B-DT]] | C | GOLGA7B activity raises GOLGA7B-DT's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without GOLGA7B | 0.006 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.7, 1.1); signed map (8.3, 38.7). **Vector** length 80.3, 17.9% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +19.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -6.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | golgin A7 family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,849,843-97,871,580 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA459F3.4, bA451M19.3; previously C10orf133, C10orf132 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAP0](https://www.uniprot.org/uniprotkb/Q2TAP0) (Golgin subfamily A member 7B):

> Play a role in cell adhesion by regulating the plasma membrane localization of the palmitoyltransferase ZDHHC5. May be involved in protein transport from Golgi to cell surface.

**Summary**, from NCBI Gene [401647](https://www.ncbi.nlm.nih.gov/gene/401647):

> Enables enzyme binding activity. Predicted to be involved in protein targeting to membrane. Predicted to be located in Golgi membrane and plasma membrane. Predicted to be part of palmitoyltransferase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31668) · Entrez [401647](https://www.ncbi.nlm.nih.gov/gene/401647) · UniProt [Q2TAP0](https://www.uniprot.org/uniprotkb/Q2TAP0) · Ensembl [ENSG00000155265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155265)

## Data

Gene col 7881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7881); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7881]; `tensor/DDL_lfc|DDL_z.npy` [7881]; `embed/gene_vectors.npy` [7881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7881 or target_col == 7881). Every well: [[GOLGA7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
