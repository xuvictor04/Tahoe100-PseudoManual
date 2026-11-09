---
symbol: "EVA1A"
type: "gene"
col: 3664
ensembl_id: "ENSG00000115363"
name: "eva-1 homolog A, regulator of programmed cell death"
location: "2p12"
module: 13
arm: "+"
pooled_cpm: 13.59
n_lines_expressing: 29
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 3
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 38
direction_downstream: 31
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# EVA1A

*eva-1 homolog A, regulator of programmed cell death* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.50× (z +7.7, q 7e-12, up in 12 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.280× (z -17.1, q 0e+00, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00973]] (+0.74, fdr 7e-06), [[SAMD3]] (+0.70, fdr 7e-06), [[GPR68]] (+0.70, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.59, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[SHC3]] → it (grade B ⚠); 31 go from it, the strongest it → [[PTPRE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +7.7 | 7e-12 | 12/27 (HS-578T, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +5.7 | 3e-06 | 8/26 (A498, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +5.0 | 1e-04 | 12/26 (NCI-H2347, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +4.8 | 2e-04 | 12/26 (HS-578T, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +3.5 | 0.046 | 8/25 (H4, SW 900, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | 1.57× | +3.1 | 0.16 | 4/26 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | 1.26× | +3.0 | 0.20 | 5/25 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 1 with an alert ⚠; shown: the 15 strongest. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.280×** | -17.1 | 0e+00 | 25/27 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.285×** | -16.8 | 0e+00 | 23/27 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.345×** | -14.2 | 1e-43 | 24/27 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.645×** | -7.2 | 9e-11 | 16/27 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.613×** | -6.6 | 6e-09 | 15/27 (A-172, SW 1088, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -6.2 | 4e-08 | 14/27 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.652×** | -6.1 | 9e-08 | 16/27 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.734×** | -5.9 | 3e-07 | 15/27 (LOX-IMVI, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.642×** | -5.7 | 7e-07 | 15/26 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.508×** | -4.7 | 1e-04 | 14/27 (A-172, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.703×** | -4.7 | 1e-04 | 13/27 (HOP62, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.728×** | -4.7 | 1e-04 | 13/27 (A-172, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.761×** | -4.5 | 4e-04 | 11/27 (COLO 205, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.718×** | -4.4 | 4e-04 | 13/26 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.718×** | -4.4 | 4e-04 | 10/26 (A498, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0885× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.130× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -11.7) |
| [[HOP62 (line)]] | alt | 82.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0653× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.166× (z -16.0) |
| [[SNU-423 (line)]] | alt | 41.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0809× (z -15.9) |
| [[SW 900 (line)]] | alt | 43.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.11× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.124× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.2) |
| [[HS-578T (line)]] | alt | 29.1 | 1 | 2 | [[Selinexor (drug)]] 5 µM 3.19× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.141× (z -10.8) |
| [[A498 (line)]] | wt | 26.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -11.8) |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 4.88 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0373× (z -11.7) |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -14.2) |
| [[SW480 (line)]] | alt | 7.05 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -8.8) |
| [[COLO 205 (line)]] | alt | 8.62 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0652× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 8.33 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0477× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.3) |
| [[A-427 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00973]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[GPR68]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[FGF5]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.67 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[RDUR]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MIR4280HG]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FRMD4A]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CDH13]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ADAMTS12]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DOCK2]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 11, C 27. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHC3]] | B | SHC3 activity raises EVA1A's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without SHC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[PTPRE]] | B | PTPRE activity raises EVA1A's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.90× lower at baseline in the lines without PTPRE | 0.056 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[NR3C1]] | B | NR3C1 activity lowers EVA1A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PRSS23]] | B | PRSS23 activity raises EVA1A's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without PRSS23 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[NALF1]] | B | NALF1 activity raises EVA1A's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without NALF1 | 0.066 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837 |
| [[FGF5]] | B | FGF5 activity raises EVA1A's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.76× lower at baseline in the lines without FGF5 | 0.066 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[ZNF385D]] | B | ZNF385D activity raises EVA1A's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without ZNF385D | 0.075 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises EVA1A's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.36× lower at baseline in the lines without APCDD1L-DT | 0.080 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[PTHLH]] | B | PTHLH activity raises EVA1A's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.74× lower at baseline in the lines without PTHLH | 0.081 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[PINLYP]] | B | PINLYP activity raises EVA1A's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 3.10× lower at baseline in the lines without PINLYP | 0.093 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises EVA1A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[TMEM200A]] | C | TMEM200A activity raises EVA1A's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 3.48× lower at baseline in the lines without TMEM200A | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 12, C 19. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRE]] | B | EVA1A activity raises PTPRE's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without EVA1A | 0.010 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[RUNX1]] | B | EVA1A activity raises RUNX1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without EVA1A | 0.015 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[DCBLD2]] | B | EVA1A activity raises DCBLD2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.78× lower at baseline in the lines without EVA1A | 0.022 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[SHC3]] | B | EVA1A activity raises SHC3's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without EVA1A | 0.035 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[ZNF697]] | B | EVA1A activity raises ZNF697's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without EVA1A | 0.037 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[SH3RF1]] | B | EVA1A activity raises SH3RF1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.58× lower at baseline in the lines without EVA1A | 0.041 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[SYNJ2]] | B | EVA1A activity raises SYNJ2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.88× lower at baseline in the lines without EVA1A | 0.062 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[RFTN1]] | B | EVA1A activity raises RFTN1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.85× lower at baseline in the lines without EVA1A | 0.068 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[GPR68]] | B | EVA1A activity raises GPR68's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without EVA1A | 0.082 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[PDE4DIPP2]] | B | EVA1A activity raises PDE4DIPP2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without EVA1A | 0.086 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[DOCK2]] | B | EVA1A activity raises DOCK2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without EVA1A | 0.099 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[ANGPTL2]] | B | EVA1A activity raises ANGPTL2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without EVA1A | 0.099 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 13.8); signed map (18.7, 47.2). **Vector** length 89.0, 24.6% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +3.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.4 | -6.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.9 | -4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -7.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | eva-1 homolog A, regulator of programmed cell death |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:75,469,302-75,569,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13391; previously TMEM166, FAM176A |
| Gene groups (HGNC) | EVA1 family |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8M9](https://www.uniprot.org/uniprotkb/Q9H8M9) (Protein eva-1 homolog A):

> Acts as a regulator of programmed cell death, mediating both autophagy and apoptosis.

**Summary**, from NCBI Gene [84141](https://www.ncbi.nlm.nih.gov/gene/84141):

> Predicted to act upstream of or within several processes, including TOR signaling; cardiac left ventricle morphogenesis; and connective tissue replacement. Predicted to be located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25816) · Entrez [84141](https://www.ncbi.nlm.nih.gov/gene/84141) · UniProt [Q9H8M9](https://www.uniprot.org/uniprotkb/Q9H8M9) · Ensembl [ENSG00000115363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115363)

## Data

Gene col 3664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3664); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3664]; `tensor/DDL_lfc|DDL_z.npy` [3664]; `embed/gene_vectors.npy` [3664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3664 or target_col == 3664). Every well: [[EVA1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVA1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
