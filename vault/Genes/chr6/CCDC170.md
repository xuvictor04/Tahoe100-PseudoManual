---
symbol: "CCDC170"
type: "gene"
col: 4172
ensembl_id: "ENSG00000120262"
name: "coiled-coil domain containing 170"
location: "6q25.1"
module: 75
arm: "+"
pooled_cpm: 2.96
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# CCDC170

*coiled-coil domain containing 170* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 13.7× (z +37.4, q 0e+00, up in 29 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (HCT15 0.0917×; ⚠ transcription drop); [[5-Azacytidine (drug)]] 5 µM in 1 line (SW480 0.193×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.195×; ⚠ cell-cycle shift, explains ~29% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO3B]] (+0.75, fdr 7e-06), [[LINC02694]] (+0.74, fdr 7e-06), [[DLEU7]] (+0.74, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C1QTNF1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **13.7×** | +37.4 | 0e+00 | 29/29 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.51×** | +17.9 | 0e+00 | 22/28 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.21×** | +17.7 | 0e+00 | 1/2 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +15.9 | 0e+00 | 8/15 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.84×** | +13.1 | 7e-37 | 12/22 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.90×** | +12.7 | 6e-35 | 1/5 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.43×** | +12.7 | 8e-35 | 30/39 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.31×** | +11.9 | 6e-31 | 16/40 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.35×** | +11.7 | 5e-30 | 15/29 (HT-29, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.16×** | +11.6 | 2e-29 | 19/36 (A-172, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.83×** | +10.5 | 6e-24 | 25/33 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +8.7 | 2e-16 | 4/14 (SW1417, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +7.7 | 4e-13 | 12/29 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +6.2 | 2e-08 | 13/35 (C32, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +5.8 | 3e-07 | 6/39 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +5.5 | 2e-06 | 12/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.1 | 1e-05 | 6/41 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.49×** | +4.0 | 0.002 | 4/39 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.003 | 8/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4172.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (HCT15 0.0917×; ⚠ transcription drop); [[5-Azacytidine (drug)]] 5 µM in 1 line (SW480 0.193×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.195×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.791× | -3.4 | 0.25 | 4/40 (C32, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.712× | -3.3 | 0.25 | 12/39 (LS 180, PANC-1, …) | rises with dose | position effect removed |
| [[LB-100 (drug)]] 0.05 µM |  | 0.725× | -3.1 | 0.28 | 3/41 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.742× | -3.0 | 0.28 | 11/39 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.811× | -3.0 | 0.28 | 3/43 (KATO III, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.0 | 0 | 3 (2 ⚠) | — | [[5-Azacytidine (drug)]] 5 µM 0.193× (z -9.2) |
| [[LoVo (line)]] | wt | 1.68 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +9.2) | — |
| [[A-172 (line)]] | wt | 1.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.7× (z +10.6) | — |
| [[A498 (line)]] | wt | 1.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +9.1) | — |
| [[C32 (line)]] | wt | 1.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0917× (z -9.6) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 1.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.1× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 5.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 1.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.5× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.1) | — |
| [[KATO III (line)]] | alt | 1.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 1.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 1.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 0.917 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.8× (z +10.1) | — |
| [[A-427 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.866 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.814 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO3B]] | +0.75 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[LINC02694]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.74 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[GRM8]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[GRM7]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ERICH2-DT]] | +0.70 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[LINC01811]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.68 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC02006]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[DPP6]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[G2E3-AS1]] | +0.67 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QTNF1-AS1]] | B | C1QTNF1-AS1 activity raises CCDC170's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without C1QTNF1-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC170's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NCALD]] | B | NCALD activity raises CCDC170's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without NCALD | 0.059 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[MKX]] | B | MKX activity raises CCDC170's level | lines that do not express MKX (32) vs lines expressing it (18) | 1.54× lower at baseline in the lines without MKX | 0.072 | ⚠ within organs, on part of the lines; also absent: FGF20, ENSG00000251652, SPINK13 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.7, 26.8); signed map (35.1, 12.8). **Vector** length 60.4, 9.84% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +37.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +17.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +17.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +11.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | +5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 170 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:151,494,017-151,621,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23305, bA282P11.1; previously C6orf97 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYT3](https://www.uniprot.org/uniprotkb/Q8IYT3) (Coiled-coil domain-containing protein 170):

> Plays a role in Golgi-associated microtubules organization and stabilization.

**Summary**, from NCBI Gene [80129](https://www.ncbi.nlm.nih.gov/gene/80129):

> The function of this gene and its encoded protein is not known. Several genome-wide association studies have implicated the region around this gene to be involved in breast cancer and bone mineral density, but no link to this specific gene has been found. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:21177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21177) · Entrez [80129](https://www.ncbi.nlm.nih.gov/gene/80129) · UniProt [Q8IYT3](https://www.uniprot.org/uniprotkb/Q8IYT3) · Ensembl [ENSG00000120262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120262)

## Data

Gene col 4172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4172); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4172]; `tensor/DDL_lfc|DDL_z.npy` [4172]; `embed/gene_vectors.npy` [4172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4172 or target_col == 4172). Every well: [[CCDC170 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC170.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
