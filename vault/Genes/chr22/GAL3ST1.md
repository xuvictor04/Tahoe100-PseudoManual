---
symbol: "GAL3ST1"
type: "gene"
col: 4865
ensembl_id: "ENSG00000128242"
name: "galactose-3-O-sulfotransferase 1"
location: "22q12.2"
module: 38
arm: "+"
pooled_cpm: 4.55
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# GAL3ST1

*galactose-3-O-sulfotransferase 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +9.2, q 2e-17, up in 13 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.311× (z -11.1, q 7e-26, down in 27 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL20A1]] (+0.68, fdr 7e-06), [[ASIC4]] (+0.67, fdr 7e-06), [[TINCR]] (+0.65, fdr 7e-06); moves opposite to [[MED13L]] (-0.48, fdr 1e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TIMD4]] → it (grade B ⚠); 5 go from it, the strongest it → [[TPTE2P5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.2 | 2e-17 | 13/32 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.3 | 1e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +5.0 | 1e-04 | 9/30 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.005 | 11/32 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.006 | 5/29 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +3.5 | 0.046 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.086 | 3/25 (BT-474, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | 1.39× | +3.1 | 0.14 | 6/38 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.311×** | -11.1 | 7e-26 | 27/41 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.443×** | -7.7 | 3e-12 | 22/37 (A549, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.482×** | -7.0 | 7e-10 | 22/38 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.527×** | -5.9 | 5e-07 | 18/36 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.540×** | -5.9 | 5e-07 | 17/24 (A549, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.602×** | -4.8 | 1e-04 | 16/37 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -4.5 | 4e-04 | 15/39 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.640×** | -4.2 | 0.002 | 15/37 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.673×** | -3.8 | 0.010 | 10/39 (H4, HCT15, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.680×** | -3.7 | 0.013 | 8/39 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.018 | 11/39 (HEC-1-A, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.700×** | -3.4 | 0.032 | 8/38 (CFPAC-1, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 11.9 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0331× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0613× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0978× (z -9.5) |
| [[A498 (line)]] | wt | 38.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 3.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0516× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 4.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0547× (z -15.3) |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0344× (z -11.5) |
| [[SW480 (line)]] | alt | 3.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0993× (z -10.6) |
| [[A-172 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL20A1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ASIC4]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TINCR]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[RFPL3S]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[HPN]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[MYO15A]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CCNP]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ATP2A1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ARL9]] | +0.60 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TEX29]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SNED1-AS1]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13L]] | -0.48 | -0.34 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMD4]] | B | TIMD4 activity raises GAL3ST1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without TIMD4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA |
| [[DSCAML1]] | B | DSCAML1 activity raises GAL3ST1's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without DSCAML1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[MROH3P]] | B | MROH3P activity raises GAL3ST1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.81× lower at baseline in the lines without MROH3P | 0.018 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[HNF1B]] | B | HNF1B activity raises GAL3ST1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.73× lower at baseline in the lines without HNF1B | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[FCGBP]] | B | FCGBP activity raises GAL3ST1's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 1.38× lower at baseline in the lines without FCGBP | 0.082 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPTE2P5]] | B | GAL3ST1 activity raises TPTE2P5's level | lines that do not express GAL3ST1 (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without GAL3ST1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | GAL3ST1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express GAL3ST1 (5) vs lines expressing it (43) | the lines without GAL3ST1: 0.33× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| [[ERFL]] | B | GAL3ST1 activity raises ERFL's level | lines that do not express GAL3ST1 (5) vs lines expressing it (45) | 1.55× lower at baseline in the lines without GAL3ST1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 5 µM | B | GAL3ST1 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express GAL3ST1 (5) vs lines expressing it (43) | the lines without GAL3ST1: 0.25× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| [[SPON2]] | B | GAL3ST1 activity raises SPON2's level | lines that do not express GAL3ST1 (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without GAL3ST1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -19.1); signed map (14.0, 12.7). **Vector** length 69.7, 12.0% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.3 | +0.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | galactose-3-O-sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,554,635-30,574,665 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CST |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99999](https://www.uniprot.org/uniprotkb/Q99999) (Galactosylceramide sulfotransferase):

> Catalyzes the transfer of a sulfate group to position 3 of non-reducing beta-galactosyl residues in glycerolipids and sphingolipids, therefore participates in the biosynthesis of sulfoglycolipids. Catalyzes the synthesis of galactosylceramide sulfate (sulfatide), a major lipid component of the myelin sheath and of monogalactosylalkylacylglycerol sulfate (seminolipid), present in spermatocytes. Seems to prefer beta-glycosides at the non-reducing termini of sugar chains attached to a lipid …

**Summary**, from NCBI Gene [9514](https://www.ncbi.nlm.nih.gov/gene/9514):

> Sulfonation, an important step in the metabolism of many drugs, xenobiotics, hormones, and neurotransmitters, is catalyzed by sulfotransferases. This gene encodes galactosylceramide sulfotransferase, which catalyzes the sulfation of membrane glycolipids including the final step in the synthesis of sulfatide, a major lipid component of the myelin sheath. This gene exhibits elevated expression in ovarian epithelial carcinoma and the encoded enzyme exhibits elevated activity in renal cell …

**Accessions** — [HGNC:24240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24240) · Entrez [9514](https://www.ncbi.nlm.nih.gov/gene/9514) · UniProt [Q99999](https://www.uniprot.org/uniprotkb/Q99999) · Ensembl [ENSG00000128242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128242)

## Data

Gene col 4865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4865); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4865]; `tensor/DDL_lfc|DDL_z.npy` [4865]; `embed/gene_vectors.npy` [4865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4865 or target_col == 4865). Every well: [[GAL3ST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAL3ST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
