---
symbol: "SPTBN5"
type: "gene"
col: 6090
ensembl_id: "ENSG00000137877"
name: "spectrin beta, non-erythrocytic 5"
location: "15q21"
module: 47
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SPTBN5

*spectrin beta, non-erythrocytic 5* — 15q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.44× (z +5.6, q 1e-05, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +5.0, q 1e-04, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.414× (z -5.8, q 4e-06, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02236]] (+0.78, fdr 7e-06), [[MPP4]] (+0.77, fdr 7e-06), [[MSANTD1]] (+0.76, fdr 7e-06); moves opposite to [[RCOR3]] (-0.62, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SCAT1]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC22A20P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +5.6 | 1e-05 | 1/7 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.17×** | +5.1 | 1e-04 | 21/42 (NCI-H460, J82, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.0 | 1e-04 | 13/34 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +4.6 | 5e-04 | 3/11 (RPMI-7951, HOP62, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +4.4 | 0.001 | 9/32 (COLO 205, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.81×** | +3.9 | 0.010 | 3/19 (NCI-H2030, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.71×** | +3.5 | 0.037 | 12/40 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -5.8 | 4e-06 | 24/42 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.243×** | -4.8 | 4e-04 | 19/36 (LOX-IMVI, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -4.7 | 5e-04 | 18/29 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.258×** | -4.6 | 5e-04 | 16/27 (RPMI-7951, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -4.5 | 9e-04 | 21/38 (SK-MEL-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.571×** | -3.7 | 0.022 | 14/41 (NCI-H2030, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.576×** | -3.6 | 0.024 | 12/42 (H4, KATO III, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.046 | 13/41 (A549, Panc 03.27, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.617×** | -3.2 | 0.093 | 15/41 (H4, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -3.1 | 0.095 | 14/38 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.716×** | -3.1 | 0.095 | 8/42 (hTERT-HPNE, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 6.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0405× (z -10.0) |
| [[SW1417 (line)]] | alt | 5.45 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0858× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02236]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MPP4]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[HPX]] | +0.75 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CHADL]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.74 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[MMP25]] | +0.74 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[TTC36]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAT1]] | B | SCAT1 activity raises SPTBN5's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without SCAT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises SPTBN5's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without SEMA4A | 0.041 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[HAS3]] | B | HAS3 activity raises SPTBN5's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 1.09× lower at baseline in the lines without HAS3 | 0.063 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent |
| [[VSIG1]] | B | VSIG1 activity raises SPTBN5's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.24× lower at baseline in the lines without VSIG1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises SPTBN5's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without C21orf91-OT1 | 0.083 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[ABL1]] | B | ABL1 activity raises SPTBN5's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.5% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC03004]] | B | LINC03004 activity raises SPTBN5's level | lines that do not express LINC03004 (22) vs lines expressing it (28) | 1.47× lower at baseline in the lines without LINC03004 | 0.084 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, OR4F15, ADAM12; maybe low, not absent |
| [[SSUH2]] | C | SSUH2 activity raises SPTBN5's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without SSUH2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A20P]] | C | SPTBN5 activity raises SLC22A20P's level | lines that do not express SPTBN5 (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without SPTBN5 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TUBA8]] | C | SPTBN5 activity lowers TUBA8's level | lines that do not express SPTBN5 (3) vs lines expressing it (47) | 1.73× higher at baseline in the lines without SPTBN5 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, -14.5); signed map (17.8, 11.9). **Vector** length 77.4, 13.7% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.4 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.1 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -4.5 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | spectrin beta, non-erythrocytic 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21 — chr15:41,848,146-41,894,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUSPECV, BSPECV, HUBSPECV |
| Gene groups (HGNC) | Spectrins; MicroRNA protein coding host genes |
| Reactome | 14 pathways, smallest: Interaction between L1 and Ankyrins; NCAM signaling for neurite out-growth; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

UniProt [Q9NRC6](https://www.uniprot.org/uniprotkb/Q9NRC6) carries no function annotation.

**Summary**, from NCBI Gene [51332](https://www.ncbi.nlm.nih.gov/gene/51332):

> Enables cytoskeletal protein binding activity; dynein intermediate chain binding activity; and identical protein binding activity. Acts upstream of or within Golgi organization and lysosomal transport. Located in cytoplasm; photoreceptor connecting cilium; and photoreceptor disc membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15680) · Entrez [51332](https://www.ncbi.nlm.nih.gov/gene/51332) · UniProt [Q9NRC6](https://www.uniprot.org/uniprotkb/Q9NRC6) · Ensembl [ENSG00000137877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137877)

## Data

Gene col 6090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6090); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6090]; `tensor/DDL_lfc|DDL_z.npy` [6090]; `embed/gene_vectors.npy` [6090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6090 or target_col == 6090). Every well: [[SPTBN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTBN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
