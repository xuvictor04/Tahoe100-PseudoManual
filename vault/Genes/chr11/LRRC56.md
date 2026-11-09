---
symbol: "LRRC56"
type: "gene"
col: 8430
ensembl_id: "ENSG00000161328"
name: "leucine rich repeat containing 56"
location: "11p15.5"
module: 53
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# LRRC56

*leucine rich repeat containing 56* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.20× (z +17.3, q 0e+00, up in 22 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0586×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.122×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.170×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERD]] (+0.67, fdr 1e-05), [[AZU1]] (+0.66, fdr 7e-06), [[GRIK5]] (+0.66, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGB2]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Everolimus (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.20×** | +17.3 | 0e+00 | 22/25 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.18×** | +14.0 | 8e-42 | 23/31 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.41×** | +10.5 | 3e-23 | 34/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +10.4 | 3e-23 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +7.6 | 4e-12 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +7.2 | 5e-11 | 23/38 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +6.3 | 3e-08 | 9/21 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.9 | 2e-07 | 5/40 (A498, J82, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.9 | 3e-07 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +5.4 | 3e-06 | 7/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +4.9 | 6e-05 | 8/28 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.81×** | +4.7 | 1e-04 | 1/6 (HT-29) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 7/40 (NCI-H1573, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.014 | 8/33 (NCI-H460, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.51×** | +3.5 | 0.016 | 10/37 (LS 180, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.026 | 1/16 (SW480) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.4 | 0.026 | 9/41 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.49×** | +3.1 | 0.051 | 2/14 (HOP62, NCI-H23) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.079 | 3/16 (J82, AsPC-1, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.46×** | +3.0 | 0.079 | 1/17 (A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8430.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0586×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.122×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.170×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.651× | -3.6 | 0.11 | 14/37 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.659× | -3.6 | 0.11 | 7/43 (AsPC-1, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.673× | -3.4 | 0.14 | 19/39 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.91 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -15.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 1.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 0.692 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +10.1) | — |
| [[A498 (line)]] | wt | 1.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 1.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +10.1) | — |
| [[A-172 (line)]] | wt | 0.895 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.937 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.555 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.784 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.657 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERD]] | +0.67 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[AZU1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.62 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[FLRT1]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[RYR1]] | +0.61 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[MEI1]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MMP25]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[COL11A2]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[GAL3ST2]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MYH7B]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB2]] | B | ITGB2 activity raises LRRC56's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.16× lower at baseline in the lines without ITGB2 | 0.011 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRRC56's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRK1]] | B | KLRK1 activity raises LRRC56's level | lines that do not express KLRK1 (29) vs lines expressing it (21) | 1.27× lower at baseline in the lines without KLRK1 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Everolimus (drug)]] 5 µM | C | LRRC56 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express LRRC56 (3) vs lines expressing it (45) | the lines without LRRC56: 1.33× the cells of the other lines | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: NMRAL1, LMNTD2, ENSG00000205890; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | LRRC56 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express LRRC56 (3) vs lines expressing it (45) | the lines without LRRC56: 0.67× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: NMRAL1, LMNTD2, ENSG00000205890; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, -13.3); signed map (22.5, 12.3). **Vector** length 44.0, 5.07% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.7 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 56 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:537,527-554,912 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00101, oda8, DKFZp761L1518, DNAAF12 |
| Gene groups (HGNC) | Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYG6](https://www.uniprot.org/uniprotkb/Q8IYG6) (Leucine-rich repeat-containing protein 56):

> Required for the assembly of dynein arms.

**Summary**, from NCBI Gene [115399](https://www.ncbi.nlm.nih.gov/gene/115399):

> Predicted to be located in cilium. Implicated in primary ciliary dyskinesia 39. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25430) · Entrez [115399](https://www.ncbi.nlm.nih.gov/gene/115399) · UniProt [Q8IYG6](https://www.uniprot.org/uniprotkb/Q8IYG6) · Ensembl [ENSG00000161328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161328)

## Data

Gene col 8430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8430); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8430]; `tensor/DDL_lfc|DDL_z.npy` [8430]; `embed/gene_vectors.npy` [8430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8430 or target_col == 8430). Every well: [[LRRC56 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC56.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
