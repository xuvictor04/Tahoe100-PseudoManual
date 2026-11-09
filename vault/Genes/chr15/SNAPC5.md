---
symbol: "SNAPC5"
type: "gene"
col: 10494
ensembl_id: "ENSG00000174446"
name: "small nuclear RNA activating complex polypeptide 5"
location: "15q22.31"
module: 83
arm: "+"
pooled_cpm: 9.59
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# SNAPC5

*small nuclear RNA activating complex polypeptide 5* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +15.7, q 0e+00, up in 38 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.178×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0871×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPDU1]] (+0.75, fdr 1e-05), [[PCBP1-AS1]] (+0.74, fdr 3e-05), [[UBE2D3-AS1]] (+0.73, fdr 1e-05); moves opposite to [[PLEKHH3]] (-0.73, fdr 1e-05), [[ARL3]] (-0.69, fdr 2e-05), [[SLC9A6]] (-0.65, fdr 6e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +15.7 | 0e+00 | 38/42 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.92×** | +15.2 | 0e+00 | 30/34 (CFPAC-1, NCI-H2030, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +14.7 | 0e+00 | 35/44 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.89×** | +14.5 | 3e-45 | 14/15 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +13.8 | 2e-41 | 24/26 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +10.9 | 9e-26 | 25/35 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +10.2 | 2e-22 | 34/42 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.2 | 1e-14 | 31/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +8.1 | 3e-14 | 33/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +7.8 | 3e-13 | 28/47 (HEC-1-A, HT-29, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +7.3 | 1e-11 | 24/45 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +6.6 | 2e-09 | 18/37 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +6.3 | 1e-08 | 21/47 (HT-29, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.9 | 1e-07 | 22/46 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.3 | 4e-06 | 15/44 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +5.2 | 7e-06 | 16/47 (LoVo, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.0 | 2e-05 | 16/48 (SK-MEL-2, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.001 | 15/47 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.046 | 10/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.060 | 4/44 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10494.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.178×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0871×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.793× | -3.3 | 0.55 | 5/47 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 7.94 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.8) | — |
| [[A498 (line)]] | wt | 7.75 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.178× (z -9.6) |
| [[C32 (line)]] | wt | 6.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 5.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +10.2) | — |
| [[LoVo (line)]] | wt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.00 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0871× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 6.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 7.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 9.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +11.9) | — |
| [[A-172 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPDU1]] | +0.75 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.74 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | +0.73 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.72 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[PARD6G-AS1]] | +0.70 | +0.73 / +0.38 | both halves | 6e-05 |  |
| [[C2orf49-DT]] | +0.70 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[SMIM15-AS1]] | +0.70 | +0.74 / +0.38 | both halves | 7e-05 |  |
| [[ZNF546]] | +0.69 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[EEF1AKMT1]] | +0.69 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[EMG1]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.69 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[FEM1A]] | +0.69 | +0.75 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | -0.73 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[ARL3]] | -0.69 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SLC9A6]] | -0.65 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[GMCL1]] | -0.65 | -0.77 / -0.32 | both halves | 1e-04 |  |
| [[STRN]] | -0.64 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[PCMT1]] | -0.64 | -0.69 / -0.29 | both halves | 3e-04 |  |
| [[COX6A1]] | -0.63 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TUBG2]] | -0.62 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[CARHSP1]] | -0.62 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[DNAJC1]] | -0.62 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[RAP1A]] | -0.61 | -0.74 / -0.31 | both halves | 2e-04 |  |
| [[RRAS]] | -0.61 | -0.64 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNAPC5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.0, 9.5); signed map (21.4, -3.3). **Vector** length 63.6, 9.99% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.9 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.9 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +7.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -2.3 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear RNA activating complex polypeptide 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,490,135-66,497,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP19 |
| Gene groups (HGNC) | SNAP complex ; MicroRNA protein coding host genes |
| Hallmark sets | DNA_REPAIR |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75971](https://www.uniprot.org/uniprotkb/O75971) (snRNA-activating protein complex subunit 5):

> Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box.

**Summary**, from NCBI Gene [10302](https://www.ncbi.nlm.nih.gov/gene/10302):

> This gene encodes a subunit of the small nuclear RNA (snRNA)-activating protein complex that plays a role in the transcription of snRNA genes. This complex binds to the promoters of snRNA genes transcribed by either RNA polymerase II or III and recruits other regulatory factors to activate snRNA gene transcription. The encoded protein may play a role in stabilizing this complex. A pseudogene of this gene has been identified on chromosome 6. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:15484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15484) · Entrez [10302](https://www.ncbi.nlm.nih.gov/gene/10302) · UniProt [O75971](https://www.uniprot.org/uniprotkb/O75971) · Ensembl [ENSG00000174446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174446)

## Data

Gene col 10494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10494); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10494]; `tensor/DDL_lfc|DDL_z.npy` [10494]; `embed/gene_vectors.npy` [10494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10494 or target_col == 10494). Every well: [[SNAPC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAPC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
