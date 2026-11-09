---
symbol: "DIRC3-AS1"
type: "gene"
col: 13890
ensembl_id: "ENSG00000233143"
name: "testicular germ cell expressed HSF2 interacting lncRNA"
location: "2q35"
module: 165
arm: "+"
pooled_cpm: 13.91
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# DIRC3-AS1

*testicular germ cell expressed HSF2 interacting lncRNA* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +15.4, q 0e+00, up in 27 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.696× (z -4.4, q 0.006, down in 12 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP8A2]] (+0.69, fdr 7e-06), [[DELEC1]] (+0.67, fdr 7e-06), [[CACNA1A]] (+0.67, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[DSCAM]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DELEC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +15.4 | 0e+00 | 27/40 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +12.4 | 4e-33 | 21/29 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.48×** | +11.1 | 4e-26 | 30/42 (SW480, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +10.4 | 3e-23 | 7/13 (BT-474, SW1417, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +9.6 | 1e-19 | 14/22 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +8.5 | 2e-15 | 24/44 (SW480, SW1417, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +8.3 | 1e-14 | 18/39 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +6.0 | 1e-07 | 17/42 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 7e-04 | 13/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Afatinib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.006 | 5/43 (HCT15, HOP62, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.008 | 12/40 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.008 | 8/45 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.018 | 5/42 (KATO III, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +3.4 | 0.030 | 14/45 (SW480, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +3.2 | 0.052 | 11/39 (SW1417, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -4.4 | 0.006 | 12/42 (H4, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -4.1 | 0.010 | 11/42 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.703×** | -4.0 | 0.011 | 12/44 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -3.9 | 0.011 | 11/44 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.750×** | -3.5 | 0.049 | 7/45 (LOX-IMVI, NCI-H1573, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.739×** | -3.5 | 0.049 | 9/45 (LOX-IMVI, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **0.750×** | -3.4 | 0.056 | 9/42 (A549, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.758×** | -3.4 | 0.056 | 11/44 (NCI-H1573, C32, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.082 | 13/42 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.773× | -3.1 | 0.10 | 7/43 (H4, NCI-H2030, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.837× | -3.1 | 0.12 | 1/45 (NCI-H1792) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.33 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 30.7× (z +15.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 7.96× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 6.53 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 90.8× (z +13.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 20.3× (z +13.1) | — |
| [[C32 (line)]] | wt | 103 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.130× (z -10.6) |
| [[H4 (line)]] | wt | 39.0 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0644× (z -11.9) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 8.50 | 1 | 2 | [[Auranofin (drug)]] 5 µM 8.98× (z +8.8) | [[Pimozide (drug)]] 0.05 µM 0.0895× (z -9.7) |
| [[A-172 (line)]] | wt | 7.82 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.78× (z +10.0) | — |
| [[KATO III (line)]] | alt | 4.20 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 12.7× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.83× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 7.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 3.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -8.9) |
| [[SNU-423 (line)]] | alt | 8.90 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.127× (z -8.5) |
| [[A-427 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8A2]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[DELEC1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[CACNA1A]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC8A1-AS1]] | +0.64 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[FGF1]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MIR3681HG]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CNTN4]] | +0.62 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[SETBP1]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DOCK2]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ZPLD1]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCAM]] | B | DSCAM activity raises DIRC3-AS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without DSCAM | 0.007 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[LINC01812]] | B | LINC01812 activity raises DIRC3-AS1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.84× lower at baseline in the lines without LINC01812 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[LINC02934]] | B | LINC02934 activity lowers DIRC3-AS1's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 1.99× higher at baseline in the lines without LINC02934 | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IGFBP5]] | B | IGFBP5 activity raises DIRC3-AS1's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without IGFBP5 | 0.060 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[NETO1]] | B | NETO1 activity raises DIRC3-AS1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 2.42× lower at baseline in the lines without NETO1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[NOL4]] | B | NOL4 activity raises DIRC3-AS1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without NOL4 | 0.069 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent |
| [[PI15]] | B | PI15 activity raises DIRC3-AS1's level | lines that do not express PI15 (36) vs lines expressing it (14) | 2.79× lower at baseline in the lines without PI15 | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC02566, ENSG00000275016, ASCL1 |
| [[ZNF521]] | B | ZNF521 activity raises DIRC3-AS1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without ZNF521 | 0.094 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |
| [[MIR646HG]] | B | MIR646HG activity raises DIRC3-AS1's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.62× lower at baseline in the lines without MIR646HG | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DELEC1]] | C | DIRC3-AS1 activity raises DELEC1's level | lines that do not express DIRC3-AS1 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without DIRC3-AS1 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC00298, LYG1, IQCM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.6, 11.6); signed map (26.1, 36.3). **Vector** length 86.3, 16.9% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +15.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | testicular germ cell expressed HSF2 interacting lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q35 — chr2:216,694,404-217,336,120 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously DIRC3-AS1, LINC01921 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52740) · Entrez [101928327](https://www.ncbi.nlm.nih.gov/gene/101928327) · Ensembl [ENSG00000233143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233143)

## Data

Gene col 13890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13890); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13890]; `tensor/DDL_lfc|DDL_z.npy` [13890]; `embed/gene_vectors.npy` [13890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13890 or target_col == 13890). Every well: [[DIRC3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIRC3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
