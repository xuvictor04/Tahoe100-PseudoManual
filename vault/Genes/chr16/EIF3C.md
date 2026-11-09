---
symbol: "EIF3C"
type: "gene"
col: 11491
ensembl_id: "ENSG00000184110"
name: "eukaryotic translation initiation factor 3 subunit C"
location: "16p11.2"
module: 25
arm: "+"
pooled_cpm: 8.09
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# EIF3C

*eukaryotic translation initiation factor 3 subunit C* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.47× (z +17.0, q 0e+00, up in 16 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +8.9, q 9e-17, up in 25 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 2 lines (NCI-H23 0.0846×, CFPAC-1 0.0829×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0586×); [[Bimatoprost (drug)]] 0.5 µM in 1 line (HT-29 0.0708×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN1]] (+0.70, fdr 1e-05), [[EIF4H]] (+0.68, fdr 1e-05), [[EEF1A1]] (+0.67, fdr 8e-06); moves opposite to [[COX7A2]] (-0.61, fdr 2e-05, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[TRAPPC4]] (-0.57, fdr 3e-05), [[RPL36AL]] (-0.55, fdr 8e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[TUBB4B]] (-0.52, fdr 6e-05), [[C4orf3]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +17.0 | 0e+00 | 16/16 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +15.0 | 0e+00 | 30/31 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +9.8 | 2e-20 | 23/23 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +8.9 | 9e-17 | 25/45 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +7.5 | 1e-11 | 30/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +6.6 | 3e-09 | 24/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +6.2 | 5e-08 | 26/47 (PANC-1, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +5.9 | 2e-07 | 26/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +5.5 | 2e-06 | 17/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +5.4 | 5e-06 | 15/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 1e-05 | 19/43 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 2e-05 | 17/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.9 | 4e-05 | 20/43 (SHP-77, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +4.9 | 4e-05 | 16/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 4e-05 | 15/46 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.4 | 3e-04 | 14/44 (MIA PaCa-2, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.4 | 3e-04 | 14/45 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +4.4 | 3e-04 | 19/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 12/47 (A-427, BT-474, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.002 | 12/46 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11491.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 2 lines (NCI-H23 0.0846×, CFPAC-1 0.0829×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0586×); [[Bimatoprost (drug)]] 0.5 µM in 1 line (HT-29 0.0708×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | 0.805× | -3.6 | 0.14 | 9/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.812× | -3.5 | 0.14 | 10/48 (AsPC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.753× | -3.4 | 0.14 | 18/43 (NCI-H23, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | 0.833× | -3.1 | 0.30 | 8/48 (NCI-H2347, A-172, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 9.47 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0586× (z -12.8) |
| [[SW480 (line)]] | alt | 8.81 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.55 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0951× (z -9.3) |
| [[A549 (line)]] | wt | 8.97 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.134× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 6.43 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0829× (z -10.0) |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0708× (z -9.6) |
| [[LoVo (line)]] | wt | 7.36 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 7.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 6.77 | 0 | 1 | — | [[Flutamide (drug)]] 5 µM 0.0709× (z -8.8) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN1]] | +0.70 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 710 |
| [[EEF1A1]] | +0.67 | +0.57 / +0.63 | both halves | 8e-06 | STRING 537 |
| [[EIF4B]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 813 |
| [[DBN1]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CIZ1]] | +0.62 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[SBDSP1]] | +0.61 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[SGPL1]] | +0.61 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[BMS1P20]] | +0.61 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[NONO]] | +0.60 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[DHFR]] | +0.60 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[HNRNPA1L3]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX7A2]] ⚠ | -0.61 | -0.48 / -0.59 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC4]] | -0.57 | -0.44 / -0.57 | both halves | 3e-05 | same gene group |
| [[RPL36AL]] ⚠ | -0.55 | -0.37 / -0.50 | both halves | 8e-05 | pathway: Cap-dependent Translation Initiation; ⚠ in the vector space only through flagged drug-doses |
| [[MRPL51]] ⚠ | -0.52 | -0.38 / -0.50 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TUBB4B]] | -0.52 | -0.38 / -0.50 | both halves | 6e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[C4orf3]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[UQCR10]] ⚠ | -0.51 | -0.34 / -0.50 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC25A4]] | -0.51 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TMEM258]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 | same gene group |
| [[SEC61G]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[LAMTOR5]] | -0.50 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[PIM2]] | -0.50 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[RBX1]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[COX8A]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.7, -24.3); signed map (-20.7, -35.4). **Vector** length 54.4, 6.88% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -1.8 | +4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.1 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.6 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | +4.4 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Allantoin (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.0 | +1.1 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,688,558-28,735,727 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-p110; previously EIF3S8 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits; MicroRNA protein coding host genes |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99613](https://www.uniprot.org/uniprotkb/Q99613) (Eukaryotic translation initiation factor 3 subunit C):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [8663](https://www.ncbi.nlm.nih.gov/gene/8663):

> Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of translation and translational initiation. Located in cytosol. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3279) · Entrez [8663](https://www.ncbi.nlm.nih.gov/gene/8663) · UniProt [Q99613](https://www.uniprot.org/uniprotkb/Q99613) · Ensembl [ENSG00000184110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184110)

## Data

Gene col 11491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11491); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11491]; `tensor/DDL_lfc|DDL_z.npy` [11491]; `embed/gene_vectors.npy` [11491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11491 or target_col == 11491). Every well: [[EIF3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
