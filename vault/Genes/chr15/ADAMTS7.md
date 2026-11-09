---
symbol: "ADAMTS7"
type: "gene"
col: 5857
ensembl_id: "ENSG00000136378"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 7"
location: "15q25.1"
module: 62
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 33
n_dd_up: 44
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ADAMTS7

*ADAM metallopeptidase with thrombospondin type 1 motif 7* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +17.3, q 0e+00, up in 15 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.184×, LoVo 0.310×); [[Vortioxetine (drug)]] 5 µM in 1 line (NCI-H23 0.0643×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.154×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF423]] (+0.72, fdr 7e-06), [[PINCR]] (+0.71, fdr 1e-05), [[ADGRA2]] (+0.66, fdr 1e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[GLIPR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +17.3 | 0e+00 | 15/20 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +11.9 | 2e-30 | 14/28 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.23×** | +11.8 | 7e-30 | 18/29 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.01×** | +11.1 | 2e-26 | 15/29 (RPMI-7951, Hs 766T, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +11.0 | 6e-26 | 12/17 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.90×** | +10.7 | 6e-25 | 14/27 (SW480, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.87×** | +10.6 | 2e-24 | 14/28 (SW 900, Hs 766T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.81×** | +10.0 | 1e-21 | 1/3 (HOP62) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.5 | 1e-15 | 11/28 (A498, A549, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.42×** | +8.2 | 9e-15 | 1/5 (A549) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +7.8 | 3e-13 | 10/23 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.14×** | +6.0 | 8e-08 | 6/24 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.81×** | +5.8 | 3e-07 | 7/18 (A498, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.48×** | +5.6 | 9e-07 | 9/27 (A549, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.73×** | +5.5 | 1e-06 | 10/29 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.61×** | +4.8 | 6e-05 | 8/29 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 1e-04 | 7/20 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 8/28 (A498, NCI-H460, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.001 | 8/27 (NCI-H460, A498, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.012 | 5/26 (A-172, A549, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.012 | 2/29 (LoVo, A498) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.012 | 4/18 (Hs 766T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5857.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.184×, LoVo 0.310×); [[Vortioxetine (drug)]] 5 µM in 1 line (NCI-H23 0.0643×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.154×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 0.5 µM |  | 0.729× | -3.2 | 0.59 | 3/28 (SW480, LoVo, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 7.77 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +12.6) | — |
| [[LoVo (line)]] | wt | 8.80 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +18.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.5) |
| [[A498 (line)]] | wt | 7.82 | 3 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 2.47 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +13.7) | — |
| [[Hs 766T (line)]] | wt | 3.03 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +8.7) | [[Nimesulide (drug)]] 0.05 µM 0.0422× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 5.85 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0643× (z -9.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.924 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF423]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PINCR]] | +0.71 | +0.56 / +0.76 | both halves | 1e-05 | **novel candidate** |
| [[ADGRA2]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[GRIN2C]] | +0.64 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[PURPL]] | +0.63 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[SPATA18]] | +0.62 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ACTA2]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ZMAT3]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[GAS6-AS1]] | +0.61 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[EDA2R]] | +0.60 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[FDXR]] | +0.60 | +0.46 / +0.62 | both halves | 3e-05 | pathway: Diseases of metabolism |
| [[HES2]] | +0.60 | +0.48 / +0.71 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAMTS7's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.6% of all compounds | 0.011 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PURPL]] | B | PURPL activity raises ADAMTS7's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without PURPL | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[RTN4RL1]] | B | RTN4RL1 activity raises ADAMTS7's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without RTN4RL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[GLIPR2]] | B | GLIPR2 activity raises ADAMTS7's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without GLIPR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[MIR3659HG]] | B | MIR3659HG activity raises ADAMTS7's level | lines that do not express MIR3659HG (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without MIR3659HG | 0.094 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| [[ADGRA2]] | C | ADGRA2 activity raises ADAMTS7's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without ADGRA2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIPR2]] | B | ADAMTS7 activity raises GLIPR2's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 2.62× lower at baseline in the lines without ADAMTS7 | 0.005 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[MIR3659HG]] | B | ADAMTS7 activity raises MIR3659HG's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.57× lower at baseline in the lines without ADAMTS7 | 0.031 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[PINCR]] | B | ADAMTS7 activity raises PINCR's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without ADAMTS7 | 0.063 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[CACNA1C]] | B | ADAMTS7 activity raises CACNA1C's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without ADAMTS7 | 0.074 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[GAS6]] | B | ADAMTS7 activity raises GAS6's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.22× lower at baseline in the lines without ADAMTS7 | 0.087 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[NCS1]] | B | ADAMTS7 activity raises NCS1's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without ADAMTS7 | 0.093 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[SLC16A10]] | B | ADAMTS7 activity raises SLC16A10's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without ADAMTS7 | 0.0999 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[ADGRA2]] | C | ADAMTS7 activity raises ADGRA2's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 2.45× lower at baseline in the lines without ADAMTS7 | 0.038 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 37.5); signed map (44.0, -23.8). **Vector** length 53.1, 10.1% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.50 to 6); *apoptosis* (hallmark, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +17.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +8.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +3.3 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | +0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -1.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,759,206-78,811,464 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADAM-TS7, DKFZp434H204 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKP4](https://www.uniprot.org/uniprotkb/Q9UKP4) (A disintegrin and metalloproteinase with thrombospondin motifs 7):

> Metalloprotease. Was previously shown to degrade COMP. However, a later study found no activity against COMP.

**Summary**, from NCBI Gene [11173](https://www.ncbi.nlm.nih.gov/gene/11173):

> The protein encoded by this gene is a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) family. Members of this family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to …

**Accessions** — [HGNC:223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:223) · Entrez [11173](https://www.ncbi.nlm.nih.gov/gene/11173) · UniProt [Q9UKP4](https://www.uniprot.org/uniprotkb/Q9UKP4) · Ensembl [ENSG00000136378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136378)

## Data

Gene col 5857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5857); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5857]; `tensor/DDL_lfc|DDL_z.npy` [5857]; `embed/gene_vectors.npy` [5857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5857 or target_col == 5857). Every well: [[ADAMTS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
