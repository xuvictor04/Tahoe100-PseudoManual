---
symbol: "LAMTOR5-AS1"
type: "gene"
col: 13415
ensembl_id: "ENSG00000224699"
name: "LAMTOR5 and SLC16A4 antisense RNA 1"
location: "1p13.3"
module: 15
arm: "+"
pooled_cpm: 28.7
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# LAMTOR5-AS1

*LAMTOR5 and SLC16A4 antisense RNA 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.42× (z +21.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.725× (z -3.9, q 0.052, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.368×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (BT-474 0.181×; ⚠ transcription drop); [[Capmatinib (drug)]] 5 µM in 1 line (SNU-1 0.0575×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A4-AS1]] (+0.85, fdr 7e-06), [[DIDO1]] (+0.75, fdr 1e-04), [[ZNF460-AS1]] (+0.70, fdr 2e-05); moves opposite to [[SERPINB1]] (-0.60, fdr 3e-05), [[ALAS1]] (-0.59, fdr 4e-05), [[MRPL17]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01139]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +21.0 | 0e+00 | 46/47 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.32×** | +10.2 | 8e-22 | 45/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.59×** | +9.6 | 1e-19 | 44/48 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.20×** | +9.5 | 2e-19 | 42/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.16×** | +9.0 | 3e-17 | 40/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +8.8 | 2e-16 | 34/48 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.5 | 1e-15 | 36/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +7.9 | 2e-13 | 35/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +6.8 | 6e-10 | 36/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-08 | 31/48 (HOP62, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.68×** | +6.2 | 3e-08 | 34/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.2 | 3e-08 | 32/46 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.4 | 4e-06 | 26/44 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.60×** | +5.3 | 4e-06 | 29/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.3 | 5e-06 | 30/48 (LoVo, LS 180, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +4.9 | 3e-05 | 29/48 (LoVo, RKO, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +4.4 | 4e-04 | 25/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13415.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.368×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (BT-474 0.181×; ⚠ transcription drop); [[Capmatinib (drug)]] 5 µM in 1 line (SNU-1 0.0575×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -3.9 | 0.052 | 18/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.773× | -3.1 | 0.45 | 11/47 (hTERT-HPNE, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 148 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 36.0 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.41× (z +11.2) | — |
| [[LoVo (line)]] | wt | 26.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 23.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 19.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +11.6) | [[Pimozide (drug)]] 0.5 µM 0.181× (z -8.9) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 15.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 24.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +8.8) | — |
| [[A-172 (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +11.2) | — |
| [[A498 (line)]] | wt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.8) | — |
| [[A549 (line)]] | wt | 9.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.04× (z +15.6) | — |
| [[C32 (line)]] | wt | 23.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 45.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 23.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +12.5) | — |
| [[J82 (line)]] | alt | 44.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[KATO III (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 29.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +16.2) | — |
| [[RKO (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 58.0 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0575× (z -8.8) |
| [[SNU-423 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.6) | — |
| [[SW48 (line)]] | wt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.7) | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A4-AS1]] | +0.85 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[DIDO1]] | +0.75 | +0.36 / +0.72 | both halves | 1e-04 |  |
| [[ZNF460-AS1]] | +0.70 | +0.49 / +0.47 | both halves | 2e-05 | same gene group |
| [[GTF3C2-AS2]] | +0.69 | +0.45 / +0.54 | both halves | 3e-05 | same gene group |
| [[ZNF213-AS1]] | +0.67 | +0.48 / +0.52 | both halves | 2e-05 | same gene group |
| [[SNHG10]] | +0.67 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CDK2AP1]] | +0.67 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[ANXA2R-OT1]] | +0.67 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[EIF3F]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ZNF718]] | +0.66 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.66 | +0.52 / +0.46 | both halves | 2e-05 | same gene group |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.65 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB1]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ALAS1]] | -0.59 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MRPL17]] | -0.58 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[CEP290]] | -0.57 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[POLM]] | -0.57 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[VEZT]] | -0.57 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SNAPIN]] | -0.57 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[DPF1]] | -0.56 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[STUB1]] | -0.56 | -0.22 / -0.29 | both halves | 6e-04 |  |
| [[MAP1S]] | -0.55 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01139]] | B | LINC01139 activity raises LAMTOR5-AS1's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.41× lower at baseline in the lines without LINC01139 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[HOXB6]] | B | HOXB6 activity lowers LAMTOR5-AS1's level | lines that do not express HOXB6 (11) vs lines expressing it (39) | 1.44× higher at baseline in the lines without HOXB6 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HOXB3, HOXB8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.4, 22.4); signed map (31.5, -17.9). **Vector** length 104, 27.4% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +21.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +4.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | LAMTOR5 and SLC16A4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p13.3 — chr1:110,347,116-110,443,817 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SLC16A4-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40823) · Entrez [101410535](https://www.ncbi.nlm.nih.gov/gene/101410535) · Ensembl [ENSG00000224699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224699)

## Data

Gene col 13415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13415); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13415]; `tensor/DDL_lfc|DDL_z.npy` [13415]; `embed/gene_vectors.npy` [13415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13415 or target_col == 13415). Every well: [[LAMTOR5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMTOR5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
