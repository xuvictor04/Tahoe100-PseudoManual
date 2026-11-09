---
symbol: "CCNO-DT"
type: "gene"
col: 14754
ensembl_id: "ENSG00000251307"
name: "CCNO divergent transcript"
location: "5q11.2"
module: 21
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CCNO-DT

*CCNO divergent transcript* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.32× (z +31.8, q 0e+00, up in 38 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Brivudine (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0505×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.141×); [[Naproxen (drug)]] 5 µM in 1 line (SW1417 0.0850×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HRG-AS1]] (+0.78, fdr 7e-06), [[LANCL1-AS1]] (+0.77, fdr 1e-05), [[SPATA1]] (+0.75, fdr 1e-05); moves opposite to [[ZNF445]] (-0.60, fdr 3e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.32×** | +31.8 | 0e+00 | 38/39 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +12.4 | 5e-33 | 27/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +11.3 | 4e-27 | 29/39 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +10.2 | 2e-22 | 22/26 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +9.5 | 3e-19 | 9/16 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.0 | 1e-17 | 5/8 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +8.4 | 3e-15 | 29/44 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.0 | 2e-10 | 21/47 (A-172, HOP62, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 0.001 | 8/41 (HEC-1-A, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.0 | 0.004 | 10/28 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.005 | 8/46 (RKO, LoVo, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.007 | 7/42 (SW1417, KATO III, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.012 | 6/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.030 | 11/47 (LoVo, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.031 | 2/44 (A498, C32) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.036 | 3/35 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.036 | 5/45 (A-172, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14754.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Brivudine (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0505×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.141×); [[Naproxen (drug)]] 5 µM in 1 line (SW1417 0.0850×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.866× | -6.0 | 1e-06 | 21/48 (BT-474, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.44 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +14.9) | — |
| [[Hs 766T (line)]] | wt | 5.29 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +8.7) | [[Gallic acid (drug)]] 0.05 µM 0.0874× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 3.64 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +9.7) | [[Brivudine (drug)]] 0.05 µM 0.0505× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 5.27 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +8.8) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0913× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.16 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.88× (z +15.4) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.141× (z -9.3) |
| [[SW1417 (line)]] | alt | 3.66 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +9.9) | [[Naproxen (drug)]] 5 µM 0.0850× (z -8.9) |
| [[A-172 (line)]] | wt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.5) | — |
| [[A498 (line)]] | wt | 4.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +12.8) | — |
| [[A549 (line)]] | wt | 3.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 3.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.89× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 5.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 6.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.97× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 3.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 8.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.0) | — |
| [[J82 (line)]] | alt | 4.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +8.8) | — |
| [[LoVo (line)]] | wt | 7.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 8.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 3.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 5.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +11.9) | — |
| [[RKO (line)]] | wt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 4.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +10.3) | — |
| [[A-427 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HRG-AS1]] | +0.78 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.77 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.75 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.73 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.71 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.70 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.70 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ATXN7L3-AS1]] | +0.70 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[OXR1-AS1]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.70 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[ZNF460-AS1]] | +0.70 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SLC3A1]] | +0.70 | +0.53 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF445]] | -0.60 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCNO-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, 25.4); signed map (33.2, 1.1). **Vector** length 59.0, 8.37% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +31.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.1 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -2.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CCNO divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q11.2 — chr5:55,233,934-55,295,201 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55543) · Entrez [121009647](https://www.ncbi.nlm.nih.gov/gene/121009647) · Ensembl [ENSG00000251307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251307)

## Data

Gene col 14754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14754); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14754]; `tensor/DDL_lfc|DDL_z.npy` [14754]; `embed/gene_vectors.npy` [14754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14754 or target_col == 14754). Every well: [[CCNO-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNO-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
