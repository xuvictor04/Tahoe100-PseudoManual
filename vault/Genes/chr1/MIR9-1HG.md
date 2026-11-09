---
symbol: "MIR9-1HG"
type: "gene"
col: 4621
ensembl_id: "ENSG00000125462"
name: "MIR9-1 host gene"
location: "1q22"
module: 53
arm: "+"
pooled_cpm: 6.68
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# MIR9-1HG

*MIR9-1 host gene* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.01× (z +17.3, q 0e+00, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.643× (z -3.9, q 0.054, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.83, fdr 7e-06), [[FNDC7]] (+0.81, fdr 7e-06), [[CPNE9]] (+0.81, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +17.3 | 0e+00 | 38/39 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +11.9 | 4e-30 | 27/38 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.45×** | +10.9 | 2e-25 | 32/41 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +8.0 | 1e-13 | 30/44 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.2 | 9e-11 | 5/10 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.2 | 6e-08 | 12/27 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.1 | 7e-08 | 20/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +5.8 | 5e-07 | 2/14 (NCI-H1573, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +5.7 | 8e-07 | 21/43 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.2 | 1e-05 | 19/40 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +4.9 | 4e-05 | 17/45 (SW 900, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +4.9 | 4e-05 | 20/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.7 | 1e-04 | 14/28 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.7 | 1e-04 | 15/38 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.6 | 2e-04 | 12/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.4 | 3e-04 | 16/44 (A-172, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.001 | 18/39 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.002 | 12/42 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.006 | 11/35 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.006 | 15/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4621.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.643×** | -3.9 | 0.054 | 14/43 (A-172, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.452×** | -3.7 | 0.070 | 10/31 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.580× | -3.4 | 0.15 | 11/42 (RPMI-7951, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | 0.500× | -3.2 | 0.17 | 7/29 (NCI-H1792, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.688× | -3.2 | 0.17 | 10/40 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.689× | -3.0 | 0.22 | 7/44 (SW48, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.04 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +11.5) | — |
| [[A-172 (line)]] | wt | 5.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +9.8) | — |
| [[A498 (line)]] | wt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.3) | — |
| [[A549 (line)]] | wt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 4.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 3.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +9.2) | — |
| [[LoVo (line)]] | wt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.5) | — |
| [[SW480 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.6) | — |
| [[A-427 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.83 | +0.82 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.81 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.80 | +0.73 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[LDHC]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CPT1C]] | +0.79 | +0.83 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SELPLG]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[PYGM]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[KIF17]] | +0.78 | +0.77 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R36]] | +0.78 | +0.64 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[VWCE]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIR9-1HG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GSTM3]] | B | GSTM3 activity strengthens MIR9-1HG's drug response | lines that do not express GSTM3 (14) vs lines expressing it (31) | the lines without GSTM3 respond 0.57× as strongly (z diff +1.37); strongest at Homoharringtonine 5 µM: 1.39x vs 2.96x (z diff +3.1) | 0.058 | ⚠ within organs, on part of the lines; also absent: ESYT3, CADM1, TGFB1I1; target measured in part of the lines; artifact flags |
| [[TMEM225B]] | B | TMEM225B activity lowers MIR9-1HG's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 1.20× higher at baseline in the lines without TMEM225B | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[DLG4]] | C | DLG4's natural level weakens MIR9-1HG's drug response | DLG4's natural level across 41 lines (lineage-adjusted; a glimpse) | r -0.74, reverse +0.10; direction not clear | 0.021 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ISY1-RAB43]] | C | ISY1-RAB43's natural level weakens MIR9-1HG's drug response | ISY1-RAB43's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.33; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, -16.2); signed map (16.5, 12.4). **Vector** length 82.1, 16.9% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +17.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | MIR9-1 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q22 — chr1:156,404,250-156,456,763 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CROC4; previously C1orf61 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13536](https://www.uniprot.org/uniprotkb/Q13536) (Protein CROC-4):

> May play a role in FOS signaling pathways involved in development and remodeling of neurons. Promotes transcription of the FOS promoter.

**Summary**, from NCBI Gene [10485](https://www.ncbi.nlm.nih.gov/gene/10485):

> Involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30780) · Entrez [10485](https://www.ncbi.nlm.nih.gov/gene/10485) · UniProt [Q13536](https://www.uniprot.org/uniprotkb/Q13536) · Ensembl [ENSG00000125462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125462)

## Data

Gene col 4621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4621); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4621]; `tensor/DDL_lfc|DDL_z.npy` [4621]; `embed/gene_vectors.npy` [4621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4621 or target_col == 4621). Every well: [[MIR9-1HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR9-1HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
