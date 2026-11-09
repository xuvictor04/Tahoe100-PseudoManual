---
symbol: "MTUS2"
type: "gene"
col: 5392
ensembl_id: "ENSG00000132938"
name: "microtubule associated scaffold protein 2"
location: "13q12.3"
module: 165
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# MTUS2

*microtubule associated scaffold protein 2* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 6.68× (z +32.1, q 0e+00, up in 42 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.0394×, NCI-H1573 0.0517×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (BT-474 0.0502×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.117×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP2]] (+0.81, fdr 7e-06), [[RYR3]] (+0.76, fdr 1e-05), [[ATP8A2]] (+0.76, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AP3B2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **6.68×** | +32.1 | 0e+00 | 42/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.72×** | +29.5 | 0e+00 | 34/35 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **7.58×** | +24.2 | 0e+00 | 36/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.58×** | +21.6 | 0e+00 | 34/37 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.28×** | +19.9 | 0e+00 | 36/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **5.04×** | +19.3 | 0e+00 | 35/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.02×** | +16.6 | 0e+00 | 35/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.83×** | +16.1 | 0e+00 | 31/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.47×** | +14.9 | 0e+00 | 30/42 (C32, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.60×** | +14.7 | 0e+00 | 1/1 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +14.4 | 3e-45 | 15/20 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.05×** | +13.3 | 7e-39 | 35/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.82×** | +12.4 | 1e-33 | 25/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +12.1 | 5e-32 | 3/7 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.72×** | +11.5 | 6e-29 | 27/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +9.2 | 1e-18 | 15/32 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +8.5 | 9e-16 | 19/38 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.0 | 5e-08 | 12/45 (A-172, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5392.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.0394×, NCI-H1573 0.0517×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (BT-474 0.0502×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.117×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.825× | -3.2 | 0.71 | 11/44 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.89 | 9 | 0 | [[Tucidinostat (drug)]] 5 µM 20.2× (z +15.7) | — |
| [[LoVo (line)]] | wt | 10.9 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 7.09× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 2.46 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 12.4× (z +13.3) | — |
| [[SW480 (line)]] | alt | 2.79 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 28.5× (z +18.9) | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.4× (z +20.2) | [[Adagrasib (drug)]] 0.05 µM 0.561× (z -8.8) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 3.48 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.6× (z +16.6) | — |
| [[HT-29 (line)]] | alt | 2.76 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.74 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.72× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0517× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.116× (z -8.5) |
| [[A549 (line)]] | wt | 2.90 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 8.61 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.83× (z +9.3) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0502× (z -9.8) |
| [[C32 (line)]] | wt | 5.26 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 22.2× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 3.69 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.57× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 2.16 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +9.7) | — |
| [[J82 (line)]] | alt | 2.57 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 22.2× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.0× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0394× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.117× (z -9.2) |
| [[SW 900 (line)]] | alt | 2.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +11.3) | — |
| [[A-427 (line)]] | wt | 3.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.1× (z +11.2) | — |
| [[A498 (line)]] | wt | 1.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 5.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.5× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 7.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +10.1) | — |
| [[KATO III (line)]] | alt | 1.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 1.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.6× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.2× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.2× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 2.08 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP2]] | +0.81 | +0.71 / +0.84 | both halves | 7e-06 |  |
| [[RYR3]] | +0.76 | +0.55 / +0.82 | both halves | 1e-05 |  |
| [[ATP8A2]] | +0.76 | +0.66 / +0.83 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.75 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.74 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.73 | +0.60 / +0.82 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[PLD5]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[XKR4]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.71 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[NOS1]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SYN1]] | +0.71 | +0.55 / +0.85 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP3B2]] | B | AP3B2 activity strengthens MTUS2's drug response | lines that do not express AP3B2 (15) vs lines expressing it (31) | the lines without AP3B2 respond 0.57× as strongly (z diff +2.39); strongest at Panobinostat 5 µM: 3.07x vs 7.90x (z diff +3.2) | 0.012 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EBF2]] | B | EBF2 activity raises MTUS2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without EBF2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[HS6ST3]] | B | HS6ST3 activity raises MTUS2's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without HS6ST3 | 0.031 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[KCND3]] | B | KCND3 activity raises MTUS2's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.57× lower at baseline in the lines without KCND3 | 0.034 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MTUS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, 31.3); signed map (30.6, 17.3). **Vector** length 71.2, 12.1% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.9 | +32.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.0 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.9 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.8 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.6 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.4 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated scaffold protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:28,820,339-29,505,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIP150, CAZIP, ICIS; previously KIAA0774 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JR59](https://www.uniprot.org/uniprotkb/Q5JR59) (Microtubule-associated tumor suppressor candidate 2):

> Binds microtubules. Together with MAPRE1 may target the microtubule depolymerase KIF2C to the plus-end of microtubules. May regulate the dynamics of microtubules at their growing distal tip.

**Summary**, from NCBI Gene [23281](https://www.ncbi.nlm.nih.gov/gene/23281):

> Enables microtubule binding activity and protein homodimerization activity. Located in centrosome; cytoplasmic microtubule; and intercellular bridge. Part of nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20595) · Entrez [23281](https://www.ncbi.nlm.nih.gov/gene/23281) · UniProt [Q5JR59](https://www.uniprot.org/uniprotkb/Q5JR59) · Ensembl [ENSG00000132938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132938)

## Data

Gene col 5392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5392); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5392]; `tensor/DDL_lfc|DDL_z.npy` [5392]; `embed/gene_vectors.npy` [5392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5392 or target_col == 5392). Every well: [[MTUS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTUS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
