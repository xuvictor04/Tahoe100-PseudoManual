---
symbol: "SETD6"
type: "gene"
col: 2307
ensembl_id: "ENSG00000103037"
name: "SET domain containing 6, protein lysine methyltransferase"
location: "16q21"
module: 5
arm: "+"
pooled_cpm: 8.56
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SETD6

*SET domain containing 6, protein lysine methyltransferase* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +12.1, q 4e-31, up in 11 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +10.6, q 3e-24, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.635× (z -6.8, q 5e-09, down in 25 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.752× (z -6.0, q 4e-07, down in 21 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.120×, NCI-H460 0.270×, NCI-H23 0.247×, SW48 0.235×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.255×, RPMI-7951 0.0833×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (RKO 0.0640×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.163×); [[Idoxuridine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0751×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TWNK]] (+0.66, fdr 7e-06), [[EMSLR]] (+0.62, fdr 7e-06), [[DDX31]] (+0.60, fdr 1e-05); moves opposite to [[MAGT1]] (-0.49, fdr 3e-05), [[COX7B]] (-0.49, fdr 4e-05), [[SERF2]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +12.1 | 4e-31 | 11/15 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +11.0 | 1e-25 | 24/32 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +10.8 | 4e-25 | 28/36 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +10.6 | 3e-24 | 25/42 (A498, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +7.8 | 9e-13 | 17/23 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +5.7 | 1e-06 | 18/46 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +5.6 | 2e-06 | 20/46 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +5.1 | 2e-05 | 15/46 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.9 | 7e-05 | 11/45 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +4.5 | 5e-04 | 14/45 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.3 | 8e-04 | 14/46 (SK-MEL-2, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.2 | 0.001 | 2/21 (BT-474, A-427) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +4.1 | 0.002 | 9/46 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.004 | 11/45 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.006 | 5/44 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.010 | 4/37 (SK-MEL-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.010 | 6/44 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.120×, NCI-H460 0.270×, NCI-H23 0.247×, SW48 0.235×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.255×, RPMI-7951 0.0833×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (RKO 0.0640×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.163×); [[Idoxuridine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0751×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -6.8 | 5e-09 | 25/42 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -6.0 | 4e-07 | 21/41 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.011 | 18/46 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.810× | -3.2 | 0.15 | 10/45 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.863× | -3.1 | 0.15 | 12/46 (LoVo, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.812× | -3.1 | 0.15 | 8/45 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 0.799× | -3.1 | 0.15 | 4/45 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.83 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.163× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.7) |
| [[RKO (line)]] | wt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 2 (1 ⚠) | — | [[Idoxuridine (drug)]] 0.5 µM 0.0751× (z -9.1) |
| [[C32 (line)]] | wt | 7.08 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0973× (z -9.0) |
| [[KATO III (line)]] | alt | 5.44 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.31× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 4.60 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0735× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.7) |
| [[SW48 (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.0) |
| [[A-172 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWNK]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[EMSLR]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[DDX31]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[CHCHD4]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.60 | +0.64 / +0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NOP16]] | +0.59 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MYBBP1A]] | +0.57 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[DTD2]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DHX33]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[WDR4]] | +0.57 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[ALKBH2]] | +0.57 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[BYSL]] | +0.56 | +0.68 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGT1]] | -0.49 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[COX7B]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SERF2]] | -0.49 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[AHCYL1]] | -0.49 | -0.49 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.7, -39.7); signed map (-1.9, -48.8). **Vector** length 54.9, 7.63% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.3 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 6, protein lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,515,479-58,523,842 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21148 |
| Gene groups (HGNC) | SET domain containing; Non-histone lysine methyltransferases |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBK2](https://www.uniprot.org/uniprotkb/Q8TBK2) (N-lysine methyltransferase SETD6):

> Protein-lysine N-methyltransferase. Monomethylates 'Lys-310' of the RELA subunit of NF-kappa-B complex, leading to down-regulation of NF-kappa-B transcription factor activity. Monomethylates 'Lys-8' of H2AZ (H2AZK8me1). Required for the maintenance of embryonic stem cell self-renewal (By similarity). Methylates PAK4.

**Summary**, from NCBI Gene [79918](https://www.ncbi.nlm.nih.gov/gene/79918):

> This gene encodes a methyltransferase that adds a methyl group to the histone H2AZ, which is involved in nuclear receptor-dependent transcription. The protein also interacts with several endogenous proteins which are involved in nuclear hormone receptor signaling. A related pseudogene is located on chromosome 2. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:26116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26116) · Entrez [79918](https://www.ncbi.nlm.nih.gov/gene/79918) · UniProt [Q8TBK2](https://www.uniprot.org/uniprotkb/Q8TBK2) · Ensembl [ENSG00000103037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103037)

## Data

Gene col 2307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2307); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2307]; `tensor/DDL_lfc|DDL_z.npy` [2307]; `embed/gene_vectors.npy` [2307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2307 or target_col == 2307). Every well: [[SETD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
