---
symbol: "MRPL52"
type: "gene"
col: 10272
ensembl_id: "ENSG00000172590"
name: "mitochondrial ribosomal protein L52"
location: "14q11.2"
module: 58
arm: "+"
pooled_cpm: 21.31
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# MRPL52

*mitochondrial ribosomal protein L52* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +10.5, q 7e-23, up in 36 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.48× (z +3.9, q 0.010, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 4.45×, NCI-H2030 3.41×, LOX-IMVI 4.05×, SW480 2.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LOX-IMVI 4.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.639× (z -6.2, q 3e-07, down in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.192×, SK-MEL-2 0.227×, NCI-H1573 0.288×); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGF]] (+0.60, fdr 3e-05), [[GSTO1]] (+0.59, fdr 1e-05), [[NDUFS8]] (+0.59, fdr 1e-05); moves opposite to [[SRRM2]] (-0.59, fdr 1e-05), [[SRSF3]] (-0.58, fdr 2e-05), [[CHD3]] (-0.56, fdr 5e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 4.45×, NCI-H2030 3.41×, LOX-IMVI 4.05×, SW480 2.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LOX-IMVI 4.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.88×** | +10.5 | 7e-23 | 36/40 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.35×** | +7.9 | 9e-13 | 29/33 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.67×** | +5.1 | 7e-05 | 31/44 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.60×** | +4.3 | 0.002 | 23/38 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.003 | 26/42 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.010 | 25/47 (NCI-H2030, COLO 205, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.52×** | +3.8 | 0.010 | 26/46 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.40×** | +3.4 | 0.052 | 23/46 (HCT15, SW480, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +3.2 | 0.083 | 18/46 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.092 | 21/47 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.13 | 19/48 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.192×, SK-MEL-2 0.227×, NCI-H1573 0.288×); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -6.2 | 3e-07 | 35/47 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.655× | -3.5 | 0.11 | 21/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.518× | -3.0 | 0.35 | 14/47 (LS 180, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.717× | -3.0 | 0.35 | 16/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.9) |
| [[H4 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.105× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.4) |
| [[SW480 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGF]] | +0.60 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[GSTO1]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NDUFS8]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TRPC4AP]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ATOX1]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[NBPF15]] | +0.57 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[C19orf53]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[COG5]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PRELID1]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MPG]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RABEPK]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CIAO2B]] | +0.55 | +0.39 / +0.59 | both halves | 6e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM2]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CHD3]] | -0.56 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[HNRNPH2]] | -0.55 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[PAF1]] | -0.54 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[HNRNPL]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[FOSL2]] | -0.52 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[DDX3X]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RBM23]] | -0.52 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[CELSR3]] | -0.52 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[YWHAE]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.3, 3.3); signed map (-39.1, 7.2). **Vector** length 55.4, 10.9% of its response variance represented; |z| ≥ 3 in 548 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,829,879-22,835,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mL52 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q86TS9](https://www.uniprot.org/uniprotkb/Q86TS9) carries no function annotation.

**Summary**, from NCBI Gene [122704](https://www.ncbi.nlm.nih.gov/gene/122704):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16655) · Entrez [122704](https://www.ncbi.nlm.nih.gov/gene/122704) · UniProt [Q86TS9](https://www.uniprot.org/uniprotkb/Q86TS9) · Ensembl [ENSG00000172590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172590)

## Data

Gene col 10272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10272); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10272]; `tensor/DDL_lfc|DDL_z.npy` [10272]; `embed/gene_vectors.npy` [10272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10272 or target_col == 10272). Every well: [[MRPL52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
