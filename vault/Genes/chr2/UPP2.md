---
symbol: "UPP2"
type: "gene"
col: 134
ensembl_id: "ENSG00000007001"
name: "uridine phosphorylase 2"
location: "2q24.1"
module: 15
arm: "+"
pooled_cpm: 3.61
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# UPP2

*uridine phosphorylase 2* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.42× (z +27.9, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.750× (z -3.8, q 0.081, down in 6 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0947×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (H4 0.0564×; ⚠ cell-cycle shift, explains ~77% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0740×; ⚠ transcription drop); [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H2347 0.0819×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS6-AS1]] (+0.80, fdr 7e-06), [[H2AZ1-DT]] (+0.77, fdr 7e-06), [[PIWIL2]] (+0.76, fdr 7e-06); moves opposite to [[SPIDR]] (-0.64, fdr 4e-05), [[PDHA1]] (-0.64, fdr 3e-05), [[PARP1]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.42×** | +27.9 | 0e+00 | 37/38 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.69×** | +15.5 | 0e+00 | 30/32 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.87×** | +12.0 | 4e-31 | 17/21 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.86×** | +12.0 | 4e-31 | 30/37 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +9.8 | 1e-20 | 21/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +9.3 | 1e-18 | 32/45 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.60×** | +8.8 | 9e-17 | 28/43 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **2.51×** | +8.5 | 1e-15 | 30/46 (A498, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.48×** | +8.4 | 3e-15 | 27/40 (LS 180, NCI-H23, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.2 | 2e-14 | 18/45 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.3 | 2e-11 | 6/16 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **3.88×** | +6.6 | 3e-09 | 18/38 (HEC-1-A, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.1 | 4e-08 | 2/7 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +5.5 | 1e-06 | 16/42 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.73×** | +5.1 | 1e-05 | 12/45 (HT-29, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.9 | 4e-05 | 12/37 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +4.7 | 7e-05 | 13/41 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.67×** | +4.7 | 8e-05 | 13/41 (A498, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 134.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0947×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (H4 0.0564×; ⚠ cell-cycle shift, explains ~77% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0740×; ⚠ transcription drop); [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H2347 0.0819×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -3.8 | 0.081 | 6/46 (NCI-H1573, J82, …) | all doses, flat | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.691× | -3.4 | 0.11 | 8/42 (SNU-423, SW48, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.677× | -3.4 | 0.11 | 11/42 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.706× | -3.2 | 0.11 | 11/45 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.707× | -3.2 | 0.11 | 3/45 (COLO 205, SHP-77, …) | all doses, flat | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.518× | -3.2 | 0.11 | 9/34 (H4, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.710× | -3.2 | 0.11 | 7/43 (RKO, SK-MEL-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.712× | -3.1 | 0.12 | 14/44 (H4, HT-29, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.717× | -3.1 | 0.12 | 0/45 | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.38 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 4.25 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +11.1) | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0564× (z -9.5) ⚠ cell-cycle shift, explains ~77% of this change |
| [[HOP62 (line)]] | alt | 4.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.89 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.3× (z +12.9) | — |
| [[SW480 (line)]] | alt | 1.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +11.5) | — |
| [[A-172 (line)]] | wt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +10.4) | — |
| [[A549 (line)]] | wt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.9× (z +10.2) | — |
| [[C32 (line)]] | wt | 2.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 5.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +9.2) | — |
| [[LoVo (line)]] | wt | 1.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0740× (z -9.4) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 3.58 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0819× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +10.7) | — |
| [[A-427 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6-AS1]] | +0.80 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.77 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[PSMD14-DT]] | +0.75 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[CASS4]] | +0.74 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[LRRC8C-DT]] | +0.74 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[ADCY10]] | +0.74 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[HLA-DMA]] | +0.73 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LINC02608]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MALINC1]] | +0.73 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[KLRD1]] | +0.72 | +0.71 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIDR]] | -0.64 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PDHA1]] | -0.64 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PARP1]] | -0.62 | -0.56 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UPP2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ANKRD7]] | B | ANKRD7 activity raises UPP2's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without ANKRD7 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (9.2, 22.2); signed map (28.5, -3.3). **Vector** length 81.6, 15.1% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +27.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | uridine phosphorylase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:157,876,679-158,136,154 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UPASE2, UP2, UDRPASE2 |
| Reactome | 5 pathways, smallest: Pyrimidine catabolism; Pyrimidine salvage; Nucleotide salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [O95045](https://www.uniprot.org/uniprotkb/O95045) (Uridine phosphorylase 2):

> Catalyzes the reversible phosphorylytic cleavage of uridine to uracil and ribose-1-phosphate which can then be utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis. Shows broad substrate specificity and can also accept deoxyuridine and other analogous compounds.

**Summary**, from NCBI Gene [151531](https://www.ncbi.nlm.nih.gov/gene/151531):

> Enables identical protein binding activity and pyrimidine-nucleoside phosphorylase activity. Involved in pyrimidine nucleoside monophosphate catabolic process; uridine catabolic process; and xenobiotic catabolic process. Acts upstream of or within dCMP catabolic process. Located in type III intermediate filament. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23061) · Entrez [151531](https://www.ncbi.nlm.nih.gov/gene/151531) · UniProt [O95045](https://www.uniprot.org/uniprotkb/O95045) · Ensembl [ENSG00000007001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007001)

## Data

Gene col 134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 134); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 134]; `tensor/DDL_lfc|DDL_z.npy` [134]; `embed/gene_vectors.npy` [134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 134 or target_col == 134). Every well: [[UPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
