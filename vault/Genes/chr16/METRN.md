---
symbol: "METRN"
type: "gene"
col: 2346
ensembl_id: "ENSG00000103260"
name: "meteorin, glial cell differentiation regulator"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 6.35
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# METRN

*meteorin, glial cell differentiation regulator* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.33× (z +11.1, q 4e-26, up in 25 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +3.8, q 0.008, up in 22 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.497× (z -6.2, q 3e-07, down in 28 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (J82 0.0541×, NCI-H2030 0.129×, PANC-1 0.287×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0264×); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H460 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Canagliflozin (drug)]] 5 µM in 1 line (J82 0.0817×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICOS13]] (+0.76, fdr 7e-06), [[GLRX5]] (+0.74, fdr 2e-05), [[MHENCR]] (+0.73, fdr 7e-06); moves opposite to [[ZXDB]] (-0.76, fdr 7e-06), [[RNF6]] (-0.75, fdr 1e-05), [[ZXDA]] (-0.70, fdr 1e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FKBP7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **6.33×** | +11.1 | 4e-26 | 25/27 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.81×** | +9.5 | 6e-19 | 8/11 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.23×** | +6.8 | 2e-09 | 14/15 (C32, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.68×** | +6.2 | 9e-08 | 34/44 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.40×** | +5.5 | 5e-06 | 25/44 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.29×** | +5.2 | 2e-05 | 22/29 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.15×** | +4.8 | 1e-04 | 21/37 (PANC-1, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.4 | 8e-04 | 12/28 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.92×** | +4.1 | 0.002 | 23/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.008 | 22/38 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.54×** | +3.8 | 0.008 | 14/33 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +3.7 | 0.008 | 14/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.73×** | +3.3 | 0.039 | 12/33 (A549, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.049 | 14/38 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.050 | 9/34 (J82, NCI-H2030, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2346.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (J82 0.0541×, NCI-H2030 0.129×, PANC-1 0.287×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0264×); [[Selinexor (drug)]] 5 µM in 1 line (NCI-H460 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Canagliflozin (drug)]] 5 µM in 1 line (J82 0.0817×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -6.2 | 3e-07 | 28/38 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.383×** | -6.0 | 5e-07 | 26/36 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 6.40 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0541× (z -15.2) |
| [[PANC-1 (line)]] | alt | 14.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.8) |
| [[C32 (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 7.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0264× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 7.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 4.49 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.177× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICOS13]] | +0.76 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[GLRX5]] | +0.74 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[MHENCR]] | +0.73 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TMEM276]] | +0.73 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.73 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.73 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MZT2B]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ATOX1]] | +0.72 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[TMEM160]] | +0.71 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.71 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[C4orf48]] | +0.70 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[BBLN]] | +0.70 | +0.57 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.76 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[RNF6]] | -0.75 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[ZXDA]] | -0.70 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ZNF564]] | -0.66 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[POLR2M]] | -0.66 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[ZNF543]] | -0.65 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[KRR1]] | -0.64 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PSMC3]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.63 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.63 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CARD8]] | -0.63 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[EIF5]] | -0.63 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP7]] | B | FKBP7 activity raises METRN's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without FKBP7 | 0.078 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 9.0); signed map (-32.6, 6.7). **Vector** length 55.5, 9.58% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.3 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.2 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.1 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.5 | +4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.1 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | meteorin, glial cell differentiation regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:715,118-719,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2601; previously C16orf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJH8](https://www.uniprot.org/uniprotkb/Q9UJH8) (Meteorin):

> Involved in both glial cell differentiation and axonal network formation during neurogenesis. Promotes astrocyte differentiation and transforms cerebellar astrocytes into radial glia. Also induces axonal extension in small and intermediate neurons of sensory ganglia by activating nearby satellite glia (By similarity).

**Summary**, from NCBI Gene [79006](https://www.ncbi.nlm.nih.gov/gene/79006):

> Meteorin regulates glial cell differentiation and promotes the formation of axonal networks during neurogenesis (Nishino et al., 2004 [PubMed 15085178]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14151) · Entrez [79006](https://www.ncbi.nlm.nih.gov/gene/79006) · UniProt [Q9UJH8](https://www.uniprot.org/uniprotkb/Q9UJH8) · Ensembl [ENSG00000103260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103260)

## Data

Gene col 2346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2346); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2346]; `tensor/DDL_lfc|DDL_z.npy` [2346]; `embed/gene_vectors.npy` [2346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2346 or target_col == 2346). Every well: [[METRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
