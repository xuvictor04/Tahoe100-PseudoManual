---
symbol: "CSF3"
type: "gene"
col: 2933
ensembl_id: "ENSG00000108342"
name: "colony stimulating factor 3"
location: "17q21.1"
module: 14
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 23
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 11
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CSF3

*colony stimulating factor 3* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 14.7× (z +17.6, q 0e+00, up in 17 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0550×; ⚠ toxic); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.491×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0792×; ⚠ toxic; transcription drop); [[NG25 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.00960×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.226×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBI3]] (+0.78, fdr 7e-06), [[CCL20]] (+0.65, fdr 7e-06), [[ZC3H12C]] (+0.65, fdr 7e-06); moves opposite to [[BSCL2]] (-0.50, fdr 1e-04), [[SLIT3]] (-0.48, fdr 5e-05), [[TMED4]] (-0.47, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); 11 go from it, the strongest it → [[CXCL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **14.7×** | +17.6 | 0e+00 | 17/19 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **29.4×** | +15.0 | 0e+00 | 20/20 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **17.6×** | +13.3 | 6e-38 | 15/15 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **10.0×** | +10.7 | 2e-24 | 19/20 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.62×** | +7.7 | 2e-12 | 0/7 | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +7.5 | 9e-12 | 10/11 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.81×** | +7.3 | 3e-11 | 19/20 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.07×** | +6.9 | 3e-10 | 2/7 (HOP62, J82) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **3.33×** | +5.6 | 2e-06 | 15/19 (A498, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **3.23×** | +5.4 | 3e-06 | 16/20 (HOP62, A-172, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.21×** | +5.4 | 3e-06 | 11/17 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.17×** | +5.3 | 4e-06 | 1/10 (LOX-IMVI) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.22×** | +5.2 | 8e-06 | 12/21 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **2.12×** | +4.9 | 3e-05 | 6/21 (LOX-IMVI, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.53×** | +4.3 | 7e-04 | 11/19 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +4.3 | 7e-04 | 4/16 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.45×** | +4.1 | 0.001 | 7/18 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **2.43×** | +4.1 | 0.001 | 14/19 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.41×** | +4.1 | 0.001 | 10/15 (HOP62, LOX-IMVI, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0550×; ⚠ toxic); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.491×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0792×; ⚠ toxic; transcription drop); [[NG25 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.00960×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.226×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.490× | -3.0 | 0.34 | 2/20 (MIA PaCa-2, NCI-H1573) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.521× | -3.0 | 0.34 | 4/20 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0550× (z -11.2) ⚠ toxic · without an alert: [[NG25 (drug)]] 5 µM 0.00960× (z -9.8) |
| [[A498 (line)]] | wt | 2.79 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 290× (z +11.9) | — |
| [[A549 (line)]] | wt | 4.10 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 97.9× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 13.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 89.3× (z +18.4) | — |
| [[A-172 (line)]] | wt | 1.38 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.1× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 5.93 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 410× (z +18.1) | — |
| [[J82 (line)]] | alt | 5.67 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 96.8× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 1.16 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 120× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 7.56 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 31.1× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 2.02 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 81.0× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 773× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.7× (z +12.8) | — |
| [[A-427 (line)]] | wt | 0.147 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.162 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.777 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.188 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBI3]] | +0.78 | +0.72 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[CCL20]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 799 |
| [[ZC3H12C]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[FOXC2]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SRGN]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PTX3]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CEBPB]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 | STRING 508 |
| [[ZC3H12A]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TNFAIP3]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[BIRC3]] | +0.58 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[IRX3]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[MT1M]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSCL2]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[SLIT3]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TMED4]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[P3H1]] | -0.47 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[TPST2]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GDAP2]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[FAM227A]] | -0.46 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[TM9SF2]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ARHGEF6]] | -0.46 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[EDIL3]] | -0.46 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[ALKBH5]] | -0.45 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises CSF3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CSF3 activity raises CXCL3's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 3.09× lower at baseline in the lines without CSF3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[ZC3H12A]] | B | CSF3 activity raises ZC3H12A's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without CSF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[TNIP1]] | B | CSF3 activity raises TNIP1's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without CSF3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[CXCL2]] | B | CSF3 activity raises CXCL2's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without CSF3 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[IL4R]] | B | CSF3 activity raises IL4R's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without CSF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[TP53I3]] | B | CSF3 activity raises TP53I3's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.42× lower at baseline in the lines without CSF3 | 0.077 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[PCCA-DT]] | B | CSF3 activity lowers PCCA-DT's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.67× higher at baseline in the lines without CSF3 | 0.084 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[PAXIP1-DT]] | B | CSF3 activity lowers PAXIP1-DT's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.61× higher at baseline in the lines without CSF3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[G0S2]] | C | CSF3 activity raises G0S2's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 4.15× lower at baseline in the lines without CSF3 | 0.059 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD; co-absent with the target |
| [[PID1]] | C | CSF3 activity raises PID1's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 3.95× lower at baseline in the lines without CSF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD; co-absent with the target |
| [[IL1R1]] | C | CSF3 activity raises IL1R1's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 4.08× lower at baseline in the lines without CSF3 | 0.087 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 10.2); signed map (13.7, 29.4). **Vector** length 66.2, 20.9% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +15.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.1 | +4.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | colony stimulating factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,015,361-40,017,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45931; previously GCSF, G-CSF, C17orf33 |
| Gene groups (HGNC) | Receptor ligands; Colony stimulating factors |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 6 pathways, smallest: Other interleukin signaling; Inactivation of CSF3 (G-CSF) signaling; Signaling by CSF3 (G-CSF) |
| Matched by | ensembl_id |

**Function**, from UniProt [P09919](https://www.uniprot.org/uniprotkb/P09919) (Granulocyte colony-stimulating factor):

> Granulocyte/macrophage colony-stimulating factors are cytokines that act in hematopoiesis by controlling the production, differentiation, and function of 2 related white cell populations of the blood, the granulocytes and the monocytes-macrophages. This CSF induces granulocytes.

**Summary**, from NCBI Gene [1440](https://www.ncbi.nlm.nih.gov/gene/1440):

> This gene encodes a member of the IL-6 superfamily of cytokines. The encoded cytokine controls the production, differentiation, and function of granulocytes. Granulocytes are a type of white blood cell that are part of the innate immune response. A modified form of this protein is commonly administered to manage chemotherapy-induced neutropenia. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, May 2020]

**Accessions** — [HGNC:2438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2438) · Entrez [1440](https://www.ncbi.nlm.nih.gov/gene/1440) · UniProt [P09919](https://www.uniprot.org/uniprotkb/P09919) · Ensembl [ENSG00000108342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108342)

## Data

Gene col 2933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2933); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2933]; `tensor/DDL_lfc|DDL_z.npy` [2933]; `embed/gene_vectors.npy` [2933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2933 or target_col == 2933). Every well: [[CSF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
