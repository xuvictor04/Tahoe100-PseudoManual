---
symbol: "NCALD"
type: "gene"
col: 2466
ensembl_id: "ENSG00000104490"
name: "neurocalcin delta"
location: "8q22.3"
module: 27
arm: "+"
pooled_cpm: 10.7
n_lines_expressing: 32
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 24
direction_downstream: 23
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NCALD

*neurocalcin delta* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.11× (z +24.0, q 0e+00, up in 20 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.536× (z -7.5, q 5e-11, down in 22 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPEAR]] (+0.71, fdr 7e-06), [[ZNF503-AS1]] (+0.68, fdr 7e-06), [[LINC01811]] (+0.66, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[SLC24A3]] → it (grade B ⚠); 23 go from it, the strongest it → [[BCAR3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.11×** | +24.0 | 0e+00 | 20/28 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.90×** | +18.0 | 0e+00 | 25/29 (SW1417, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +13.1 | 4e-37 | 13/28 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +12.3 | 2e-32 | 21/29 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +11.3 | 2e-27 | 6/14 (A549, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +10.9 | 1e-25 | 18/28 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.04×** | +8.6 | 8e-16 | 17/29 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.01×** | +8.1 | 5e-14 | 7/11 (BT-474, NCI-H2347, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +8.0 | 9e-14 | 19/29 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.0 | 1e-13 | 9/30 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +7.7 | 5e-13 | 8/28 (C32, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.3 | 2e-11 | 10/28 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.75×** | +6.7 | 9e-10 | 5/21 (NCI-H2347, HT-29, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.68×** | +6.2 | 2e-08 | 16/29 (A549, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +5.8 | 2e-07 | 17/29 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +4.2 | 7e-04 | 11/28 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.002 | 9/28 (LoVo, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.035 | 8/29 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.051 | 3/28 (SHP-77, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2466.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -7.5 | 5e-11 | 22/29 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -5.8 | 1e-06 | 10/28 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -5.8 | 1e-06 | 16/28 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.663×** | -4.9 | 1e-04 | 17/29 (KATO III, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.683×** | -4.6 | 6e-04 | 6/29 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -4.5 | 6e-04 | 11/28 (LOX-IMVI, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -3.8 | 0.011 | 9/29 (RPMI-7951, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.745×** | -3.5 | 0.029 | 11/28 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.820×** | -3.4 | 0.044 | 9/29 (NCI-H460, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -3.4 | 0.044 | 16/27 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.760×** | -3.3 | 0.053 | 9/28 (RPMI-7951, SW480, …) | two highest doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.077 | 8/28 (LoVo, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 72.5 | 0 | 9 (4 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.00724× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 2.83 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 166 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0608× (z -22.7) |
| [[LS 180 (line)]] | wt | 29.3 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.12× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 15.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0852× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -8.8) |
| [[A549 (line)]] | wt | 9.35 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +9.6) | — |
| [[C32 (line)]] | wt | 3.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.180× (z -11.1) |
| [[A498 (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +8.7) | — |
| [[LoVo (line)]] | wt | 9.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 6.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.132× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 10.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.87× (z +11.6) | — |
| [[A-172 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPEAR]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ZNF503-AS1]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC01811]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ENTREP2]] | +0.65 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[LINC00299]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[LINC01814]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PDE11A]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 | **novel candidate** |
| [[CACNA1E]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 | same gene group; pathway: Neuronal System |
| [[ADAMTS19]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[DNAH6]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC01622]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 19, C 5. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC24A3]] | B | SLC24A3 activity raises NCALD's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 2.62× lower at baseline in the lines without SLC24A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[NOD2]] | B | NOD2 activity raises NCALD's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without NOD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[TOP2A]] | B | TOP2A activity lowers NCALD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00299]] | B | LINC00299 activity raises NCALD's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without LINC00299 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[SMOC2]] | B | SMOC2 activity raises NCALD's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without SMOC2 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises NCALD's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.26× lower at baseline in the lines without LINC01814 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[TSHZ2]] | B | TSHZ2 activity raises NCALD's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.25× lower at baseline in the lines without TSHZ2 | 0.046 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[LINC01091]] | B | LINC01091 activity raises NCALD's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without LINC01091 | 0.052 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[XYLT1]] | B | XYLT1 activity raises NCALD's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without XYLT1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[ST18]] | B | ST18 activity raises NCALD's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.74× lower at baseline in the lines without ST18 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent |
| [[VSNL1]] | B | VSNL1 activity raises NCALD's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without VSNL1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[LINC02253]] | B | LINC02253 activity raises NCALD's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 2.21× lower at baseline in the lines without LINC02253 | 0.074 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349 |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 18, C 5. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3-AS1]] | B | NCALD activity raises BCAR3-AS1's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.56× lower at baseline in the lines without NCALD | 0.043 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[NOD2]] | B | NCALD activity raises NOD2's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.64× lower at baseline in the lines without NCALD | 0.059 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[CCDC170]] | B | NCALD activity raises CCDC170's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without NCALD | 0.059 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[CLRN3]] | B | NCALD activity raises CLRN3's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without NCALD | 0.061 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[USH1C]] | B | NCALD activity raises USH1C's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.72× lower at baseline in the lines without NCALD | 0.061 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[DIP2C-AS1]] | B | NCALD activity raises DIP2C-AS1's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without NCALD | 0.074 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| cells under [[Everolimus (drug)]] 5 µM | B | NCALD activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express NCALD (18) vs lines expressing it (30) | the lines without NCALD: 1.08× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[TSHZ2]] | B | NCALD activity raises TSHZ2's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.61× lower at baseline in the lines without NCALD | 0.076 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[RNF43]] | B | NCALD activity raises RNF43's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without NCALD | 0.076 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[PROX1-AS1]] | B | NCALD activity raises PROX1-AS1's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without NCALD | 0.083 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[PLB1]] | B | NCALD activity raises PLB1's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without NCALD | 0.085 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[SCIN]] | B | NCALD activity raises SCIN's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without NCALD | 0.086 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 40.8); signed map (55.5, 15.9). **Vector** length 67.1, 14.8% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +8.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +8.3 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +24.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | neurocalcin delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:101,686,542-102,124,907 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 6 pathways, smallest: Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors; Activation of kainate receptors upon glutamate binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P61601](https://www.uniprot.org/uniprotkb/P61601) (Neurocalcin-delta):

> May be involved in the calcium-dependent regulation of rhodopsin phosphorylation. Binds three calcium ions.

**Summary**, from NCBI Gene [83988](https://www.ncbi.nlm.nih.gov/gene/83988):

> This gene encodes a member of the neuronal calcium sensor (NCS) family of calcium-binding proteins. The protein contains an N-terminal myristoylation signal and four EF-hand calcium binding loops. The protein is cytosolic at resting calcium levels; however, elevated intracellular calcium levels induce a conformational change that exposes the myristoyl group, resulting in protein association with membranes and partial co-localization with the perinuclear trans-golgi network. The protein is …

**Accessions** — [HGNC:7655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7655) · Entrez [83988](https://www.ncbi.nlm.nih.gov/gene/83988) · UniProt [P61601](https://www.uniprot.org/uniprotkb/P61601) · Ensembl [ENSG00000104490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104490)

## Data

Gene col 2466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2466); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2466]; `tensor/DDL_lfc|DDL_z.npy` [2466]; `embed/gene_vectors.npy` [2466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2466 or target_col == 2466). Every well: [[NCALD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCALD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
