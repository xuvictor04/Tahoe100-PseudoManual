---
symbol: "FOXD1"
type: "gene"
col: 14769
ensembl_id: "ENSG00000251493"
name: "forkhead box D1"
location: "5q13.2"
module: 20
arm: "-"
pooled_cpm: 19.2
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# FOXD1

*forkhead box D1* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +6.8, q 5e-09, up in 26 of 37 measured lines) ⚠ cell-cycle shift, explains ~91% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.96× (z +5.0, q 1e-04, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.421× (z -7.8, q 3e-12, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXA2]] (+0.66, fdr 1e-05), [[EID2]] (+0.65, fdr 1e-05), [[KCTD11]] (+0.65, fdr 7e-06); moves opposite to [[DFFB]] (-0.57, fdr 1e-05), [[AGO1]] (-0.57, fdr 2e-05), [[CNPY3]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SPHK1]] → it (grade B ⚠); 5 go from it, the strongest it → [[DDX50]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.70×** | +6.8 | 5e-09 | 26/37 (AsPC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.86×** | +5.6 | 6e-06 | 26/37 (PANC-1, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.0 | 1e-04 | 25/37 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +4.7 | 5e-04 | 22/37 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.64×** | +4.5 | 8e-04 | 22/37 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.58×** | +4.2 | 0.003 | 23/37 (LOX-IMVI, PANC-1, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.005 | 17/35 (SW1417, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.55×** | +3.8 | 0.010 | 20/36 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.49×** | +3.6 | 0.018 | 19/38 (SW1417, LOX-IMVI, …) | two highest doses | composition shift |
| [[Bendamustine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.071 | 14/37 (LOX-IMVI, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.421×** | -7.8 | 3e-12 | 33/38 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -6.2 | 2e-07 | 27/38 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -6.1 | 2e-07 | 27/37 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.642×** | -4.0 | 0.009 | 23/37 (HOP62, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -3.5 | 0.058 | 10/22 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.695×** | -3.3 | 0.100 | 16/37 (RPMI-7951, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.157× (z -14.8) |
| [[HOP62 (line)]] | alt | 47.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -11.0) |
| [[RKO (line)]] | wt | 69.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 31.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.2) ⚠ cell-cycle shift, explains ~91% of this change | [[Dinaciclib (drug)]] 5 µM 0.153× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +8.6) ⚠ cell-cycle shift, explains ~91% of this change | [[Panobinostat (drug)]] 5 µM 0.188× (z -9.1) |
| [[J82 (line)]] | alt | 37.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -13.0) |
| [[A-427 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.65× (z +8.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[A498 (line)]] | wt | 6.47 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +10.1) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[A549 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +10.0) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[COLO 205 (line)]] | alt | 6.37 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +9.3) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +9.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.8) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0956× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.0) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -9.4) |
| [[A-172 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXA2]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 | same gene group; STRING 480 |
| [[EID2]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[KCTD11]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[METTL23]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[REST]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[C14orf119]] | +0.59 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PURA]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZNF503]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[IMP3]] | +0.58 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[ERVK3-1]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TOPORS]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DFFB]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[AGO1]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CNPY3]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RNPEP]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PABIR2]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RPA1]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[EIF3H]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[FKBP9]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[RPSA]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[UBQLN1]] | -0.53 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPHK1]] | B | SPHK1 activity raises FOXD1's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 3.07× lower at baseline in the lines without SPHK1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[DLX2]] | B | DLX2 activity raises FOXD1's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 3.58× lower at baseline in the lines without DLX2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises FOXD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX50]] | B | FOXD1 activity raises DDX50's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without FOXD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |
| [[ZNF281]] | B | FOXD1 activity raises ZNF281's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without FOXD1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |
| [[LRCH3]] | B | FOXD1 activity raises LRCH3's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without FOXD1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |
| [[CAMSAP2]] | B | FOXD1 activity raises CAMSAP2's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without FOXD1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |
| [[CAVIN1]] | B | FOXD1 activity raises CAVIN1's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 3.40× lower at baseline in the lines without FOXD1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.9, 4.4); signed map (-3.5, 9.4). **Vector** length 88.8, 24.5% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +5.7 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.8 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +3.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.8 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:73,444,827-73,448,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FREAC4; previously FKHL8 |
| Gene groups (HGNC) | Forkhead boxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16676](https://www.uniprot.org/uniprotkb/Q16676) (Forkhead box protein D1):

> Transcription factor involved in regulation of gene expression in a variety of processes, including formation of positional identity in the developing retina, regionalization of the optic chiasm, morphogenesis of the kidney, and neuralization of ectodermal cells (By similarity). Involved in transcriptional activation of PGF and C3 genes.

**Summary**, from NCBI Gene [2297](https://www.ncbi.nlm.nih.gov/gene/2297):

> This gene belongs to the forkhead family of transcription factors which are characterized by a distinct forkhead domain. Studies of the orthologous mouse protein indicate that it functions in kidney development by promoting nephron progenitor differentiation, and it also functions in the development of the retina and optic chiasm. It may also regulate inflammatory reactions and prevent autoimmunity. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:3802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3802) · Entrez [2297](https://www.ncbi.nlm.nih.gov/gene/2297) · UniProt [Q16676](https://www.uniprot.org/uniprotkb/Q16676) · Ensembl [ENSG00000251493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251493)

## Data

Gene col 14769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14769); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14769]; `tensor/DDL_lfc|DDL_z.npy` [14769]; `embed/gene_vectors.npy` [14769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14769 or target_col == 14769). Every well: [[FOXD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
