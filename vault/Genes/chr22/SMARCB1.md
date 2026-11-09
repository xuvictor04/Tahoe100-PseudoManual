---
symbol: "SMARCB1"
type: "gene"
col: 1835
ensembl_id: "ENSG00000099956"
name: "SWI/SNF related BAF chromatin remodeling complex subunit B1"
location: "22q11.23"
module: 51
arm: "+"
pooled_cpm: 37.07
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SMARCB1

*SWI/SNF related BAF chromatin remodeling complex subunit B1* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.34× (z +6.2, q 4e-07, up in 18 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.20× (z +3.9, q 0.020, up in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 2.41×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.431× (z -26.1, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YTHDC2]] (+0.74, fdr 7e-06), [[EPC2]] (+0.70, fdr 7e-06), [[TXNRD2]] (+0.69, fdr 7e-06); moves opposite to [[HDAC3]] (-0.62, fdr 3e-05), [[NDRG1]] (-0.61, fdr 2e-05), [[RNMT]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 2.41×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.2 | 4e-07 | 18/40 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.2 | 5e-05 | 23/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.020 | 16/48 (RKO, PANC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.8 | 0.024 | 13/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.029 | 22/48 (HEC-1-A, RKO, …) | rises with dose | composition shift |
| [[Clotrimazole (drug)]] 5 µM |  | 1.11× | +3.4 | 0.068 | 6/48 (J82, H4, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.19 | 4/48 (HEC-1-A, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.431×** | -26.1 | 0e+00 | 45/48 (SNU-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.350×** | -23.1 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.383×** | -21.1 | 0e+00 | 47/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.420×** | -19.1 | 0e+00 | 47/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.471×** | -16.5 | 0e+00 | 47/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.539×** | -13.6 | 5e-40 | 43/48 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -13.5 | 8e-40 | 39/47 (SK-MEL-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.680×** | -12.0 | 3e-31 | 44/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -9.2 | 2e-18 | 37/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.454×** | -9.1 | 6e-18 | 41/48 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.678×** | -8.6 | 6e-16 | 33/48 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -7.7 | 7e-13 | 29/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.770×** | -5.7 | 4e-07 | 24/48 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -5.2 | 9e-06 | 21/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.790×** | -5.2 | 9e-06 | 22/46 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -4.7 | 8e-05 | 15/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.684×** | -4.4 | 4e-04 | 23/48 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.5 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -17.7) |
| [[LS 180 (line)]] | wt | 46.4 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -13.2) |
| [[SW480 (line)]] | alt | 56.5 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.305× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 63.5 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 45.1 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.8) |
| [[LoVo (line)]] | wt | 40.4 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.269× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 6 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 37.8 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 46.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -12.3) |
| [[PANC-1 (line)]] | alt | 29.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -12.3) |
| [[SW48 (line)]] | wt | 53.0 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -12.7) |
| [[A-427 (line)]] | wt | 28.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.230× (z -13.0) |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -10.4) |
| [[C-33 A (line)]] | alt | 56.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.232× (z -11.7) |
| [[C32 (line)]] | wt | 34.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -12.4) |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -25.1) |
| [[HOP62 (line)]] | alt | 27.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -12.1) |
| [[RKO (line)]] | wt | 35.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.4) |
| [[SW1417 (line)]] | alt | 53.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -10.1) |
| [[A498 (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -17.1) |
| [[HS-578T (line)]] | alt | 50.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -14.3) |
| [[J82 (line)]] | alt | 24.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.7) |
| [[KATO III (line)]] | alt | 43.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 30.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.247× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -10.4) |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.176× (z -12.9) |
| [[A-172 (line)]] | wt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.5) |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0635× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.4) |
| [[HCT15 (line)]] | alt | 50.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.2) |
| [[SNU-423 (line)]] | alt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -12.4) |
| [[A549 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | +0.74 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[EPC2]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TXNRD2]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DLG5]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SRCAP]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 | STRING 432 |
| [[ANAPC7]] | +0.65 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[FKRP]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PYM1]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PBRM1]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[ZNF414]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PIGO]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | -0.62 | -0.43 / -0.67 | both halves | 3e-05 | pathway: Chromatin modifying enzymes |
| [[NDRG1]] | -0.61 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[RNMT]] | -0.60 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[INSIG2]] | -0.59 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[SAP30-DT]] | -0.59 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[DPM1]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[ANKRD37]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RAB11FIP5]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FAM210A]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[BMT2]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[RAB8B]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMARCB1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-17.7, 5.4); signed map (10.1, -34.3). **Vector** length 97.5, 24.4% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +8.2 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -6.2 | -16.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -26.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -9.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.3 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,786,931-23,838,009 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAF47, Ini1, INI-1, Snr1, hSNFS, Sfh1p, RDT, PPP1R144; previously SNF5L1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; BAF complex subunits; PBAF complex subunits |
| Reactome | 21 pathways, smallest: Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12824](https://www.uniprot.org/uniprotkb/Q12824) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily B member 1):

> Core component of the BAF (hSWI/SNF) complex. This ATP-dependent chromatin-remodeling complex plays important roles in cell proliferation and differentiation, in cellular antiviral activities and inhibition of tumor formation. The BAF complex is able to create a stable, altered form of chromatin that constrains fewer negative supercoils than normal. This change in supercoiling would be due to the conversion of up to one-half of the nucleosomes on polynucleosomal arrays into asymmetric …

**Summary**, from NCBI Gene [6598](https://www.ncbi.nlm.nih.gov/gene/6598):

> The protein encoded by this gene is part of a complex that relieves repressive chromatin structures, allowing the transcriptional machinery to access its targets more effectively. The encoded nuclear protein may also bind to and enhance the DNA joining activity of HIV-1 integrase. This gene has been found to be a tumor suppressor, and mutations in it have been associated with malignant rhabdoid tumors. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:11103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11103) · Entrez [6598](https://www.ncbi.nlm.nih.gov/gene/6598) · UniProt [Q12824](https://www.uniprot.org/uniprotkb/Q12824) · Ensembl [ENSG00000099956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099956)

## Data

Gene col 1835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1835); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1835]; `tensor/DDL_lfc|DDL_z.npy` [1835]; `embed/gene_vectors.npy` [1835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1835 or target_col == 1835). Every well: [[SMARCB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
