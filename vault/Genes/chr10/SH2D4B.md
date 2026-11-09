---
symbol: "SH2D4B"
type: "gene"
col: 10909
ensembl_id: "ENSG00000178217"
name: "SH2 domain containing 4B"
location: "10q23.1"
module: 47
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SH2D4B

*SH2 domain containing 4B* — 10q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.62× (z +16.8, q 0e+00, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.504× (z -6.3, q 2e-07, down in 20 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP25]] (+0.81, fdr 7e-06), [[PITRM1-AS1]] (+0.80, fdr 7e-06), [[LINC02236]] (+0.79, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LSMEM2]] → it (grade B ⚠); 8 go from it, the strongest it → [[GRIK5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +16.8 | 0e+00 | 27/31 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +15.0 | 0e+00 | 21/31 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.60×** | +11.4 | 1e-27 | 1/3 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +10.7 | 2e-24 | 8/12 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.22×** | +7.3 | 2e-11 | 17/42 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +7.3 | 2e-11 | 16/32 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +6.7 | 2e-09 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +6.5 | 6e-09 | 14/41 (CFPAC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +6.5 | 7e-09 | 14/35 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +5.9 | 2e-07 | 14/40 (SW480, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.3 | 6e-06 | 10/36 (HCT15, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.72×** | +4.7 | 1e-04 | 9/37 (A549, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +4.6 | 2e-04 | 9/39 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.001 | 9/42 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 3/40 (A-172, SW48, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.005 | 5/38 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.039 | 3/31 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.041 | 8/34 (C32, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.504×** | -6.3 | 2e-07 | 20/37 (BT-474, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.541×** | -5.7 | 4e-06 | 16/41 (HCT15, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -4.6 | 7e-04 | 15/35 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.645×** | -4.0 | 0.008 | 7/40 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -3.3 | 0.099 | 12/39 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.706× | -3.2 | 0.13 | 5/41 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 0.711× | -3.1 | 0.14 | 8/37 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.526× | -3.1 | 0.14 | 6/23 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.721× | -3.0 | 0.16 | 16/25 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 7.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +8.9) | — |
| [[SW480 (line)]] | alt | 2.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +8.8) | — |
| [[A-172 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP25]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.80 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GARIN1B]] | +0.79 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.75 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[DPYS]] | +0.75 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[CHADL]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.74 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PILRA]] | +0.74 | +0.76 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSMEM2]] | B | LSMEM2 activity raises SH2D4B's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without LSMEM2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SH2D4B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GPRC5D-AS1]] | B | GPRC5D-AS1 activity raises SH2D4B's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without GPRC5D-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK5]] | C | SH2D4B activity lowers GRIK5's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.26× higher at baseline in the lines without SH2D4B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[SYT5]] | C | SH2D4B activity lowers SYT5's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.22× higher at baseline in the lines without SH2D4B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[ADAM32]] | C | SH2D4B activity raises ADAM32's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without SH2D4B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[MYH3]] | C | SH2D4B activity lowers MYH3's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 1.41× higher at baseline in the lines without SH2D4B | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent |
| [[ELAVL3]] | C | SH2D4B activity lowers ELAVL3's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.76× higher at baseline in the lines without SH2D4B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[ADAP1]] | C | SH2D4B activity raises ADAP1's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.74× lower at baseline in the lines without SH2D4B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[CPT1C]] | C | SH2D4B activity lowers CPT1C's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 1.71× higher at baseline in the lines without SH2D4B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[C11orf91]] | C | SH2D4B activity raises C11orf91's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without SH2D4B | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.8, -14.4); signed map (18.3, 11.7). **Vector** length 57.6, 8.62% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -5.7 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SH2 domain containing 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1 — chr10:80,537,902-80,646,560 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing |
| Matched by | ensembl_id |

UniProt [Q5SQS7](https://www.uniprot.org/uniprotkb/Q5SQS7) carries no function annotation.

**Summary**, from NCBI Gene [387694](https://www.ncbi.nlm.nih.gov/gene/387694):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31440) · Entrez [387694](https://www.ncbi.nlm.nih.gov/gene/387694) · UniProt [Q5SQS7](https://www.uniprot.org/uniprotkb/Q5SQS7) · Ensembl [ENSG00000178217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178217)

## Data

Gene col 10909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10909); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10909]; `tensor/DDL_lfc|DDL_z.npy` [10909]; `embed/gene_vectors.npy` [10909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10909 or target_col == 10909). Every well: [[SH2D4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2D4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
