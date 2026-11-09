---
symbol: "VAMP1"
type: "gene"
col: 6276
ensembl_id: "ENSG00000139190"
name: "vesicle associated membrane protein 1"
location: "12p13.31"
module: 11
arm: "-"
pooled_cpm: 6.78
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# VAMP1

*vesicle associated membrane protein 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.33× (z +17.2, q 0e+00, up in 40 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.5 µM in 1 line (HOP62 0.0788×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.0777×; ⚠ cell-cycle shift, explains ~0% of this change); [[Nimesulide (drug)]] 5 µM in 1 line (HEC-1-A 0.0929×; ⚠ toxic; unreliable plate only); [[Fulvestrant (drug)]] 0.5 µM in 1 line (RKO 0.0669×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.177×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAT]] (+0.62, fdr 1e-05), [[KLHL15]] (+0.61, fdr 8e-06), [[RPL10]] (+0.61, fdr 1e-05); moves opposite to [[ERCC4]] (-0.63, fdr 3e-05), [[GPATCH8]] (-0.63, fdr 1e-05), [[RPP14]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.33×** | +17.2 | 0e+00 | 40/40 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.81×** | +14.6 | 1e-45 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.08×** | +11.7 | 3e-29 | 43/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.45×** | +10.3 | 1e-22 | 42/47 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +9.9 | 7e-21 | 32/38 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +9.0 | 2e-17 | 27/43 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +8.2 | 2e-14 | 32/47 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +8.2 | 2e-14 | 30/41 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.43×** | +7.4 | 1e-11 | 29/46 (A-427, HOP62, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +5.9 | 2e-07 | 31/48 (HT-29, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +5.4 | 3e-06 | 29/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.3 | 5e-06 | 24/48 (HOP62, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +5.1 | 2e-05 | 23/47 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +3.6 | 0.011 | 6/16 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.013 | 15/46 (KATO III, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.017 | 9/47 (MIA PaCa-2, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.5 µM in 1 line (HOP62 0.0788×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.0777×; ⚠ cell-cycle shift, explains ~0% of this change); [[Nimesulide (drug)]] 5 µM in 1 line (HEC-1-A 0.0929×; ⚠ toxic; unreliable plate only); [[Fulvestrant (drug)]] 0.5 µM in 1 line (RKO 0.0669×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.653× | -3.6 | 0.16 | 16/48 (SK-MEL-2, SW1417, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.667× | -3.4 | 0.16 | 13/47 (C32, HCT15, …) | inconsistent across doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.683× | -3.2 | 0.16 | 16/46 (A-427, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Rosiglitazone (drug)]] 5 µM |  | 0.676× | -3.2 | 0.16 | 13/43 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | 0.690× | -3.1 | 0.16 | 10/48 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.692× | -3.1 | 0.16 | 10/46 (AN3 CA, SW1417, …) | rises with dose |  |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | 0.678× | -3.1 | 0.16 | 14/45 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.777× | -3.0 | 0.18 | 9/47 (NCI-H23, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.83 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.41× (z +11.7) | [[Vilanterol (drug)]] 0.5 µM 0.0788× (z -9.9) |
| [[SW480 (line)]] | alt | 11.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.65× (z +11.6) | — |
| [[A-427 (line)]] | wt | 14.7 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 6.20× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -8.5) |
| [[A549 (line)]] | wt | 4.87 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 12.2× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0777× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +10.5) | — |
| [[RKO (line)]] | wt | 5.26 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +9.8) | [[Fulvestrant (drug)]] 0.5 µM 0.0669× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0929× (z -8.5) ⚠ toxic; unreliable plate only |
| [[Hs 766T (line)]] | wt | 9.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +9.2) | — |
| [[J82 (line)]] | alt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +8.6) | — |
| [[LoVo (line)]] | wt | 5.09 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 7.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 5.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAT]] | +0.62 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[KLHL15]] | +0.61 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[RPL10]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[STK35]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CTSV]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[HSPE1-MOB4]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[POLR2A]] | +0.59 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[GNAS]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[NXF1]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.57 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CRELD1]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CSRP2]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC4]] | -0.63 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[GPATCH8]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[RPP14]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[EIF5B]] | -0.60 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.59 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[METTL2A]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[REXO4]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[BRIX1]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SDAD1]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MRM2]] | -0.56 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VAMP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.4, -1.2); signed map (1.6, 15.8). **Vector** length 73.8, 13.9% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +17.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | +9.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,462,237-6,470,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VAMP-1; previously SYB1 |
| Gene groups (HGNC) | Vesicle associated membrane proteins |
| Reactome | 6 pathways, smallest: Toxicity of botulinum toxin type D (botD); Toxicity of botulinum toxin type F (botF); Toxicity of botulinum toxin type G (botG) |
| Matched by | ensembl_id |

**Function**, from UniProt [P23763](https://www.uniprot.org/uniprotkb/P23763) (Vesicle-associated membrane protein 1):

> Involved in the targeting and/or fusion of transport vesicles to their target membrane.

**Summary**, from NCBI Gene [6843](https://www.ncbi.nlm.nih.gov/gene/6843):

> Synapotobrevins, syntaxins, and the synaptosomal-associated protein SNAP25 are the main components of a protein complex involved in the docking and/or fusion of synaptic vesicles with the presynaptic membrane. The protein encoded by this gene is a member of the vesicle-associated membrane protein (VAMP)/synaptobrevin family. Mutations in this gene are associated with autosomal dominant spastic ataxia 1. Multiple alternative splice variants have been described, but the full-length nature of some …

**Accessions** — [HGNC:12642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12642) · Entrez [6843](https://www.ncbi.nlm.nih.gov/gene/6843) · UniProt [P23763](https://www.uniprot.org/uniprotkb/P23763) · Ensembl [ENSG00000139190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139190)

## Data

Gene col 6276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6276); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6276]; `tensor/DDL_lfc|DDL_z.npy` [6276]; `embed/gene_vectors.npy` [6276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6276 or target_col == 6276). Every well: [[VAMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
