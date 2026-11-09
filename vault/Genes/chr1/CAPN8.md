---
symbol: "CAPN8"
type: "gene"
col: 12777
ensembl_id: "ENSG00000203697"
name: "calpain 8"
location: "1q41"
module: 31
arm: "+"
pooled_cpm: 20.53
n_lines_expressing: 15
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 75
direction_downstream: 81
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CAPN8

*calpain 8* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.83× (z +19.3, q 0e+00, up in 4 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.567× (z -5.3, q 5e-05, down in 6 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC2]] (+0.80, fdr 7e-06), [[MST1R]] (+0.74, fdr 7e-06), [[CEACAM6]] (+0.73, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 81 go from it, the strongest it → [[SDCBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +19.3 | 0e+00 | 4/13 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +15.7 | 0e+00 | 7/9 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.47×** | +15.2 | 0e+00 | 6/12 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.44×** | +14.0 | 3e-42 | 7/11 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +7.7 | 2e-12 | 10/13 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +7.1 | 1e-10 | 3/13 (SHP-77, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +7.0 | 2e-10 | 0/13 | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +6.5 | 5e-09 | 1/13 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.6 | 1e-06 | 4/13 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +4.8 | 1e-04 | 1/13 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 9e-04 | 8/13 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.001 | 2/13 (SW480, NCI-H2347) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.007 | 1/13 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.007 | 4/13 (LoVo, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.7 | 0.008 | 1/13 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.027 | 2/13 (NCI-H1573, Hs 766T) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.028 | 2/13 (NCI-H2347, SW480) | two highest doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.068 | 9/13 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.079 | 1/13 (Hs 766T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -5.3 | 5e-05 | 6/13 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -5.2 | 6e-05 | 8/13 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.729×** | -4.5 | 0.001 | 7/13 (LoVo, BT-474, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -4.4 | 0.001 | 9/13 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.684×** | -3.9 | 0.013 | 7/13 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.689×** | -3.8 | 0.014 | 7/13 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **0.721×** | -3.3 | 0.069 | 1/13 (Hs 766T) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.696×** | -3.3 | 0.076 | 7/13 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.12 | 6/13 (BT-474, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.799× | -3.1 | 0.12 | 7/13 (BT-474, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.726× | -3.0 | 0.13 | 0/13 | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.770× | -3.0 | 0.13 | 8/13 (BT-474, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 57.0 | 0 | 18 (1 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.100× (z -12.9) |
| [[LS 180 (line)]] | wt | 78.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.1) |
| [[KATO III (line)]] | alt | 326 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 40.3 | 5 | 0 | [[Dexamethasone (drug)]] 0.05 µM 5.54× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.5) |
| [[HT-29 (line)]] | alt | 194 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -11.2) |
| [[LoVo (line)]] | wt | 26.0 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.116× (z -8.5) |
| [[SW480 (line)]] | alt | 10.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.35× (z +9.3) | — |
| [[A-172 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC2]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM6]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[KRT8]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM5]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ABCC3]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KRT18]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TNS4]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CTSE]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ACSL5]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TMEM30B]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[MUC5AC]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 4, C 71. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CAPN8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SDCBP2]] | B | SDCBP2 activity raises CAPN8's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 3.29× lower at baseline in the lines without SDCBP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[HDAC6]] | B | HDAC6 activity raises CAPN8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF860]] | B | ZNF860 activity raises CAPN8's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without ZNF860 | 0.087 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[CEACAM5]] | C | CEACAM5 activity raises CAPN8's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 13.61× lower at baseline in the lines without CEACAM5 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises CAPN8's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 12.68× lower at baseline in the lines without FAM3D | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises CAPN8's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 7.12× lower at baseline in the lines without ST6GALNAC1 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises CAPN8's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 4.87× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises CAPN8's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 7.01× lower at baseline in the lines without GPX2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises CAPN8's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 3.66× lower at baseline in the lines without LINC00589 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises CAPN8's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.99× lower at baseline in the lines without C1orf116 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[KCNH8]] | C | KCNH8 activity raises CAPN8's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 3.40× lower at baseline in the lines without KCNH8 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22; co-absent with the target |

### Downstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 18, C 63. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDCBP2]] | B | CAPN8 activity raises SDCBP2's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 4.81× lower at baseline in the lines without CAPN8 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[LMO7]] | B | CAPN8 activity raises LMO7's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 4.52× lower at baseline in the lines without CAPN8 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[GAREM1]] | B | CAPN8 activity raises GAREM1's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.32× lower at baseline in the lines without CAPN8 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[TJP2]] | B | CAPN8 activity raises TJP2's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 2.84× lower at baseline in the lines without CAPN8 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[ABHD11]] | B | CAPN8 activity raises ABHD11's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without CAPN8 | 0.019 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[TMEM184A]] | B | CAPN8 activity raises TMEM184A's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 2.63× lower at baseline in the lines without CAPN8 | 0.023 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[KRT8]] | B | CAPN8 activity raises KRT8's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 4.03× lower at baseline in the lines without CAPN8 | 0.026 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[ARMC7]] | B | CAPN8 activity raises ARMC7's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 1.50× lower at baseline in the lines without CAPN8 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[CEMIP]] | B | CAPN8 activity raises CEMIP's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 4.80× lower at baseline in the lines without CAPN8 | 0.035 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[PPARG]] | B | CAPN8 activity raises PPARG's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.81× lower at baseline in the lines without CAPN8 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[KIF13B]] | B | CAPN8 activity raises KIF13B's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 2.13× lower at baseline in the lines without CAPN8 | 0.050 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[EPS8L1]] | B | CAPN8 activity raises EPS8L1's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.33× lower at baseline in the lines without CAPN8 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.0, 50.7); signed map (66.8, 10.2). **Vector** length 79.5, 35.3% of its response variance represented; |z| ≥ 3 in 454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -5.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -5.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | calpain 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:223,538,007-223,665,723 (-) |
| Ensembl biotype | protein_coding |
| Also known as | nCL-2 |
| Gene groups (HGNC) | EF-hand domain containing; Calpains |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NHC0](https://www.uniprot.org/uniprotkb/A6NHC0) (Calpain-8):

> Calcium-regulated non-lysosomal thiol-protease. Involved in membrane trafficking in the gastric surface mucus cells (pit cells) and may involve the membrane trafficking of mucus cells via interactions with coat protein. Proteolytically cleaves the beta-subunit of coatomer complex (By similarity).

**Summary**, from NCBI Gene [388743](https://www.ncbi.nlm.nih.gov/gene/388743):

> Predicted to enable calcium-dependent cysteine-type endopeptidase activity and identical protein binding activity. Predicted to be involved in proteolysis. Predicted to act upstream of or within calcium-dependent self proteolysis. Predicted to be located in Golgi apparatus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1485) · Entrez [388743](https://www.ncbi.nlm.nih.gov/gene/388743) · UniProt [A6NHC0](https://www.uniprot.org/uniprotkb/A6NHC0) · Ensembl [ENSG00000203697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203697)

## Data

Gene col 12777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12777); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12777]; `tensor/DDL_lfc|DDL_z.npy` [12777]; `embed/gene_vectors.npy` [12777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12777 or target_col == 12777). Every well: [[CAPN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
