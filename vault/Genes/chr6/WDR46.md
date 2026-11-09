---
symbol: "WDR46"
type: "gene"
col: 13571
ensembl_id: "ENSG00000227057"
name: "WD repeat domain 46"
location: "6p21.32"
module: 1
arm: "+"
pooled_cpm: 12.88
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# WDR46

*WD repeat domain 46* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (20 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.33× (z +14.9, q 0e+00, up in 42 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +14.0, q 7e-42, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.758× (z -5.5, q 1e-05, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Afatinib (drug)]] 5 µM in 1 line (C-33 A 0.220×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AsPC-1 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBL3]] (+0.77, fdr 7e-06), [[NOL6]] (+0.76, fdr 7e-06), [[IPO4]] (+0.74, fdr 7e-06); moves opposite to [[MIF]] (-0.57, fdr 1e-04), [[PI4KAP1-1]] (-0.55, fdr 4e-05), [[GABARAPL2]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +14.9 | 0e+00 | 42/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +14.0 | 7e-42 | 33/46 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.48×** | +13.6 | 1e-39 | 35/44 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.14×** | +11.4 | 7e-28 | 28/38 (KATO III, H4, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +11.3 | 1e-27 | 33/46 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.08×** | +10.5 | 7e-24 | 16/21 (MIA PaCa-2, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +10.1 | 6e-22 | 24/32 (SK-MEL-2, A549, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +8.7 | 3e-16 | 34/47 (PANC-1, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +7.7 | 1e-12 | 31/44 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +6.6 | 3e-09 | 28/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.5 | 3e-09 | 20/42 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 3e-09 | 26/47 (LOX-IMVI, PANC-1, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +6.4 | 5e-09 | 10/20 (HS-578T, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.51×** | +5.9 | 1e-07 | 24/42 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +5.9 | 1e-07 | 24/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 1e-04 | 20/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 2e-04 | 12/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 6e-04 | 12/47 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.001 | 13/46 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.001 | 15/46 (SW480, A-172, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.008 | 10/46 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.008 | 8/45 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.011 | 2/46 (J82, HepG2/C3A) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13571.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Afatinib (drug)]] 5 µM in 1 line (C-33 A 0.220×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AsPC-1 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -5.5 | 1e-05 | 23/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -5.5 | 1e-05 | 24/46 (CHP-212, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.806× | -3.3 | 0.21 | 5/48 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.811× | -3.2 | 0.21 | 6/48 (HCT15, C-33 A, …) | rises with dose | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.809× | -3.1 | 0.21 | 6/46 (C32, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.863× | -3.1 | 0.21 | 13/48 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.57× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 6.04 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.102× (z -8.5) |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 1 | — | [[Afatinib (drug)]] 5 µM 0.220× (z -8.5) |
| [[HOP62 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.4) | — |
| [[KATO III (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.57× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +13.1) | — |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBL3]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[NOL6]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[IPO4]] | +0.74 | +0.67 / +0.75 | both halves | 7e-06 | STRING 518 |
| [[DPH2]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[UTP15]] | +0.71 | +0.71 / +0.57 | both halves | 9e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[MAPKAPK5]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[IMP4]] | +0.69 | +0.78 / +0.60 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[ABCF2]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PES1]] | +0.67 | +0.71 / +0.56 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 923 |
| [[METTL1]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 | STRING 438 |
| [[GRWD1]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 | same gene group; STRING 920 |
| [[CCDC86]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIF]] | -0.57 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[PI4KAP1-1]] | -0.55 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[GABARAPL2]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.54 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[RGL3]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A5]] | -0.54 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[COX7B]] | -0.54 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.0, -33.8); signed map (-4.2, -44.2). **Vector** length 64.6, 10.7% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.8 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -2.8 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -2.6 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,279,108-33,289,247 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BING4, UTP7; previously C6orf11 |
| Gene groups (HGNC) | WD repeat domain containing; SSU processome; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O15213](https://www.uniprot.org/uniprotkb/O15213) (WD repeat-containing protein 46):

> Scaffold component of the nucleolar structure. Required for localization of DDX21 and NUCLEOLIN to the granular compartment of the nucleolus. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [9277](https://www.ncbi.nlm.nih.gov/gene/9277):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Located in nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13923) · Entrez [9277](https://www.ncbi.nlm.nih.gov/gene/9277) · UniProt [O15213](https://www.uniprot.org/uniprotkb/O15213) · Ensembl [ENSG00000227057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227057)

## Data

Gene col 13571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13571); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13571]; `tensor/DDL_lfc|DDL_z.npy` [13571]; `embed/gene_vectors.npy` [13571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13571 or target_col == 13571). Every well: [[WDR46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
