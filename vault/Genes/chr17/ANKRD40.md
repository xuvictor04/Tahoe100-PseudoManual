---
symbol: "ANKRD40"
type: "gene"
col: 7857
ensembl_id: "ENSG00000154945"
name: "ankyrin repeat domain 40"
location: "17q21.33"
module: 5
arm: "+"
pooled_cpm: 31.38
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ANKRD40

*ankyrin repeat domain 40* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +9.9, q 4e-20, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.816× (z -4.0, q 0.044, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.384×, SHP-77 0.298×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.216×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (A-172 0.295×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF2]] (+0.76, fdr 7e-06), [[ZMYND11]] (+0.73, fdr 7e-06), [[ZNF507]] (+0.72, fdr 7e-06); moves opposite to [[ABCB9]] (-0.67, fdr 1e-05), [[ANKRD37]] (-0.66, fdr 1e-05), [[DPM1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TCHP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +9.9 | 4e-20 | 34/48 (LS 180, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +9.5 | 4e-19 | 25/39 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +9.1 | 2e-17 | 34/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.8 | 2e-16 | 36/45 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +6.2 | 5e-08 | 29/47 (A549, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 1e-07 | 23/47 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +5.8 | 5e-07 | 24/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 3e-05 | 23/48 (LoVo, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +5.0 | 3e-05 | 25/42 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.9 | 4e-05 | 24/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 5e-05 | 22/48 (SW480, BT-474, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 8e-05 | 21/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.6 | 2e-04 | 21/47 (H4, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +4.5 | 3e-04 | 20/47 (Panc 03.27, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.3 | 6e-04 | 24/46 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 8e-04 | 21/47 (CFPAC-1, SK-MEL-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 8e-04 | 20/47 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.002 | 17/48 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.005 | 16/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.012 | 14/48 (SNU-1, SW 900, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.027 | 11/47 (SW 900, H4, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7857.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.384×, SHP-77 0.298×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.216×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (A-172 0.295×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.816×** | -4.0 | 0.044 | 16/48 (SW1417, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.883× | -3.5 | 0.15 | 10/48 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.856× | -3.0 | 0.43 | 16/48 (SHP-77, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.1) ⚠ toxic; transcription drop | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.295× (z -10.7) |
| [[SNU-423 (line)]] | alt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -13.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 85.0 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.58× (z +9.4) | — |
| [[LoVo (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0932× (z -9.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.461× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF2]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ZMYND11]] | +0.73 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.72 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZMPSTE24]] | +0.71 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PRRC2B]] | +0.71 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.68 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TOR1A]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SNX19]] | +0.68 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[RCN1]] | +0.67 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[WASH8P]] ⚠ | +0.67 | +0.51 / +0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF142]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB9]] | -0.67 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.66 | -0.64 / -0.54 | both halves | 1e-05 | same gene group |
| [[DPM1]] | -0.66 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[AFMID]] | -0.65 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.63 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RFX2]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DDT]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SELENOW]] | -0.61 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.61 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[FBXO33]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCHP]] | C | TCHP's natural level weakens ANKRD40's drug response | TCHP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.13; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.7, -27.8); signed map (-7.2, -38.8). **Vector** length 100, 21.8% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +9.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.1 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,693,198-50,707,914 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15396 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q6AI12](https://www.uniprot.org/uniprotkb/Q6AI12) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28233) · Entrez [91369](https://www.ncbi.nlm.nih.gov/gene/91369) · UniProt [Q6AI12](https://www.uniprot.org/uniprotkb/Q6AI12) · Ensembl [ENSG00000154945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154945)

## Data

Gene col 7857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7857); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7857]; `tensor/DDL_lfc|DDL_z.npy` [7857]; `embed/gene_vectors.npy` [7857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7857 or target_col == 7857). Every well: [[ANKRD40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
