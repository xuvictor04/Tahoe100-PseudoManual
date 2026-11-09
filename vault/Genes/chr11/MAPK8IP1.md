---
symbol: "MAPK8IP1"
type: "gene"
col: 4284
ensembl_id: "ENSG00000121653"
name: "mitogen-activated protein kinase 8 interacting protein 1"
location: "11p11.2"
module: 53
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# MAPK8IP1

*mitogen-activated protein kinase 8 interacting protein 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.31× (z +19.2, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Megestrol (drug)]] 5 µM: 0.706× (z -5.6, q 1e-05, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Trimetrexate (drug)]] 0.05 µM in 1 line (SHP-77 0.0816×); [[Radotinib (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0714×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A-427 0.106×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAP1GAP]] (+0.70, fdr 7e-06), [[SYT5]] (+0.66, fdr 1e-05), [[CPNE9]] (+0.62, fdr 1e-05); moves opposite to [[TRMT61B]] (-0.53, fdr 4e-05), [[C2orf42]] (-0.51, fdr 2e-04), [[UMPS]] (-0.49, fdr 1e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFAP45]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.31×** | +19.2 | 0e+00 | 45/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.39×** | +17.0 | 0e+00 | 39/44 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.63×** | +15.6 | 0e+00 | 25/35 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.42×** | +14.1 | 4e-43 | 40/45 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +10.8 | 4e-25 | 23/34 (A498, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +8.2 | 3e-14 | 24/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.7 | 1e-12 | 10/18 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +6.8 | 9e-10 | 18/41 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.3 | 2e-08 | 1/4 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +6.1 | 6e-08 | 11/39 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.1 | 7e-08 | 15/44 (PANC-1, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.6 | 1e-06 | 1/6 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +5.6 | 1e-06 | 15/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 3e-06 | 11/32 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +5.0 | 3e-05 | 7/39 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.005 | 7/36 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.020 | 4/37 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.020 | 4/41 (HOP62, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4284.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Trimetrexate (drug)]] 0.05 µM in 1 line (SHP-77 0.0816×); [[Radotinib (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0714×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A-427 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 5 µM |  | **0.706×** | -5.6 | 1e-05 | 14/45 (A498, Hs 766T, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.736× | -3.5 | 0.11 | 4/45 (CFPAC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.741× | -3.4 | 0.11 | 11/46 (NCI-H1573, A498, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.759× | -3.2 | 0.22 | 9/43 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.600× | -3.1 | 0.24 | 4/29 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +8.9) | — |
| [[A-427 (line)]] | wt | 5.66 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.106× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 4.23 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0714× (z -9.7) |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0816× (z -10.7) |
| [[A498 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.990 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1GAP]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SYT5]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CPNE9]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[LZTS3]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DDAH2]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MYO7A]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[DLGAP4]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TMEM25]] | +0.59 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[DNAI7]] | +0.57 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[BMP8A]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[LSMEM2]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[HCN2]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61B]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[C2orf42]] | -0.51 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[UMPS]] | -0.49 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PKD2]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[LINC01515]] | -0.48 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[MGME1]] | -0.48 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[PAAF1]] | -0.48 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[DHX35]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TMEM209]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ECHDC1]] | -0.47 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[BMS1P1]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[KLHL42]] | -0.47 | -0.27 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP45]] | B | CFAP45 activity lowers MAPK8IP1's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.90× higher at baseline in the lines without CFAP45 | 0.092 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.0, -17.0); signed map (-2.7, 24.0). **Vector** length 52.3, 6.30% of its response variance represented; |z| ≥ 3 in 1,221 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +15.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +19.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[NG25 (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 8 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,885,651-45,906,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IB1, JIP-1, JIP1; previously PRKM8IP |
| Gene groups (HGNC) | SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQF2](https://www.uniprot.org/uniprotkb/Q9UQF2) (C-Jun-amino-terminal kinase-interacting protein 1):

> The JNK-interacting protein (JIP) group of scaffold proteins selectively mediates JNK signaling by aggregating specific components of the MAPK cascade to form a functional JNK signaling module. Required for JNK activation in response to excitotoxic stress. Cytoplasmic MAPK8IP1 causes inhibition of JNK-regulated activity by retaining JNK in the cytoplasm and inhibiting JNK phosphorylation of c-Jun. May also participate in ApoER2-specific reelin signaling. Directly, or indirectly, regulates GLUT2 …

**Summary**, from NCBI Gene [9479](https://www.ncbi.nlm.nih.gov/gene/9479):

> This gene encodes a regulator of the pancreatic beta-cell function. It is highly similar to JIP-1, a mouse protein known to be a regulator of c-Jun amino-terminal kinase (Mapk8). This protein has been shown to prevent MAPK8 mediated activation of transcription factors, and to decrease IL-1 beta and MAP kinase kinase 1 (MEKK1) induced apoptosis in pancreatic beta cells. This protein also functions as a DNA-binding transactivator of the glucose transporter GLUT2. RE1-silencing transcription …

**Accessions** — [HGNC:6882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6882) · Entrez [9479](https://www.ncbi.nlm.nih.gov/gene/9479) · UniProt [Q9UQF2](https://www.uniprot.org/uniprotkb/Q9UQF2) · Ensembl [ENSG00000121653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121653)

## Data

Gene col 4284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4284); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4284]; `tensor/DDL_lfc|DDL_z.npy` [4284]; `embed/gene_vectors.npy` [4284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4284 or target_col == 4284). Every well: [[MAPK8IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK8IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
