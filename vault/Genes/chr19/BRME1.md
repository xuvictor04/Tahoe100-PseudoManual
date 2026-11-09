---
symbol: "BRME1"
type: "gene"
col: 5270
ensembl_id: "ENSG00000132016"
name: "break repair meiotic recombinase recruitment factor 1"
location: "19p13.12"
module: 6
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 16
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# BRME1

*break repair meiotic recombinase recruitment factor 1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +8.5, q 1e-14, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (drug)]] 0.05 µM: 1.43× (z +3.3, q 0.059, up in 2 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.466× (z -7.1, q 7e-10, down in 20 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F2]] (+0.73, fdr 1e-05), [[E2F1]] (+0.73, fdr 7e-06), [[DMC1]] (+0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[YBX2]] → it (grade B ⚠); 16 go from it, the strongest it → [[RBL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.5 | 1e-14 | 3/6 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.4 | 1e-14 | 1/2 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +7.5 | 1e-11 | 0/3 | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.93×** | +6.2 | 1e-07 | 12/38 (SW480, A-427, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.90×** | +6.0 | 2e-07 | 13/41 (SNU-1, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.84×** | +5.5 | 4e-06 | 5/11 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.52×** | +3.9 | 0.007 | 9/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.059 | 2/30 (C32, SNU-1) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.42×** | +3.3 | 0.059 | 3/40 (SW480, C32, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.059 | 7/40 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.2 | 0.072 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.40×** | +3.2 | 0.074 | 1/42 (SW480) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.466×** | -7.1 | 7e-10 | 20/37 (A-427, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -5.5 | 1e-05 | 21/42 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.616×** | -4.5 | 0.001 | 8/40 (C-33 A, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -3.9 | 0.017 | 8/17 (A-172, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.018 | 11/38 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -3.7 | 0.020 | 12/38 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.680×** | -3.4 | 0.049 | 8/34 (LS 180, NCI-H1792, …) | rises with dose | position effect removed |
| [[palbociclib (drug)]] 0.5 µM |  | **0.612×** | -3.2 | 0.072 | 3/40 (A-172, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -3.2 | 0.072 | 10/32 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.05 µM |  | **0.688×** | -3.2 | 0.072 | 6/32 (RPMI-7951, SNU-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.708×** | -3.2 | 0.072 | 5/36 (NCI-H23, LS 180, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -3.1 | 0.081 | 8/34 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.707×** | -3.1 | 0.089 | 5/40 (HOP62, SW48, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -3.1 | 0.090 | 6/23 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 3.97 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0743× (z -8.7) |
| [[SHP-77 (line)]] | alt | 4.88 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0779× (z -8.5) |
| [[SW480 (line)]] | alt | 1.83 | 0 | 1 | — | [[Penfluridol (drug)]] 0.05 µM 0.0641× (z -8.6) |
| [[A-172 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.630 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.671 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F2]] | +0.73 | +0.57 / +0.80 | both halves | 1e-05 |  |
| [[E2F1]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[DMC1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RNASEH2A]] | +0.70 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.69 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[MCM2]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.67 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[DDX11-AS1]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[EXO1]] | +0.67 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[TLCD3B]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[HELLS]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[WDR76]] | +0.66 | +0.48 / +0.77 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises BRME1's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without YBX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers BRME1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CDC25A]] | B | CDC25A activity raises BRME1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without CDC25A | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBL1]] | C | BRME1 activity strengthens RBL1's drug response | lines that do not express BRME1 (4) vs lines expressing it (44) | the lines without BRME1 respond 0.87× as strongly (z diff +0.63); strongest at Idarubicin (hydrochloride) 5 µM: 1.09x vs 0.67x (z diff +5.6) | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ZGRF1]] | C | BRME1 activity raises ZGRF1's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without BRME1 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[XRCC3]] | C | BRME1 activity raises XRCC3's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without BRME1 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[RBL1]] | C | BRME1 activity raises RBL1's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.27× lower at baseline in the lines without BRME1 | 0.040 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[CDC6]] | C | BRME1 activity raises CDC6's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without BRME1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[FAM111B]] | C | BRME1 activity raises FAM111B's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.56× lower at baseline in the lines without BRME1 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[CENPU]] | C | BRME1 activity raises CENPU's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without BRME1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[RAD54L]] | C | BRME1 activity raises RAD54L's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without BRME1 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[CDC7]] | C | BRME1 activity raises CDC7's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without BRME1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent; co-absent with the target |
| [[GINS3]] | C | BRME1 activity raises GINS3's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without BRME1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[CDC45]] | C | BRME1 activity raises CDC45's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without BRME1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[E2F1]] | C | BRME1 activity raises E2F1's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without BRME1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.9, -44.0); signed map (-38.5, -46.5). **Vector** length 42.8, 5.21% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.50 to 65); *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.1 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +2.1 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +0.8 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +1.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -5.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | break repair meiotic recombinase recruitment factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:13,882,348-13,906,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11271, MEIOK21; previously C19orf57 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VDD7](https://www.uniprot.org/uniprotkb/Q0VDD7) (Break repair meiotic recombinase recruitment factor 1):

> Meiotic recombination factor component of recombination bridges involved in meiotic double-strand break repair. Modulates the localization of recombinases DMC1:RAD51 to meiotic double-strand break (DSB) sites through the interaction with and stabilization of the BRCA2:HSF2BP complex during meiotic recombination. Indispensable for the DSB repair, homologous synapsis, and crossover formation that are needed for progression past metaphase I, is essential for spermatogenesis and male fertility.

**Summary**, from NCBI Gene [79173](https://www.ncbi.nlm.nih.gov/gene/79173):

> Predicted to enable damaged DNA binding activity. Predicted to be involved in meiosis I; protein localization to site of double-strand break; and spermatogenesis. Predicted to be located in chromosome. Predicted to be active in site of double-strand break. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:28153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28153) · Entrez [79173](https://www.ncbi.nlm.nih.gov/gene/79173) · UniProt [Q0VDD7](https://www.uniprot.org/uniprotkb/Q0VDD7) · Ensembl [ENSG00000132016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132016)

## Data

Gene col 5270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5270); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5270]; `tensor/DDL_lfc|DDL_z.npy` [5270]; `embed/gene_vectors.npy` [5270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5270 or target_col == 5270). Every well: [[BRME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
