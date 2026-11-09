---
symbol: "SLC41A3"
type: "gene"
col: 3564
ensembl_id: "ENSG00000114544"
name: "solute carrier family 41 member 3"
location: "3q21.2-q21.3"
module: 2
arm: "+"
pooled_cpm: 12.25
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SLC41A3

*solute carrier family 41 member 3* — 3q21.2-q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +6.9, q 3e-09, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -22.3, q 0e+00, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CROCCP3-1]] (+0.67, fdr 7e-06), [[GPAT4]] (+0.64, fdr 1e-05), [[DUSP22]] (+0.62, fdr 1e-05); moves opposite to [[CREB3]] (-0.61, fdr 1e-05), [[TRIP11]] (-0.60, fdr 1e-05), [[DZIP3]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.9 | 3e-09 | 16/44 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 9e-06 | 17/45 (HT-29, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.2 | 0.005 | 16/40 (HCT15, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.025 | 2/47 (MIA PaCa-2, A-427) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.031 | 13/46 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.039 | 8/46 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.071 | 4/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.14 | 8/19 (HOP62, MIA PaCa-2, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.0 | 0.16 | 6/45 (HS-578T, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -22.3 | 0e+00 | 36/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.535×** | -11.5 | 6e-28 | 31/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -8.7 | 5e-16 | 25/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -6.1 | 2e-07 | 18/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -4.7 | 3e-04 | 16/45 (A-427, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.641×** | -4.6 | 5e-04 | 10/46 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | **0.805×** | -4.3 | 0.002 | 8/46 (SW480, J82, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.810×** | -4.1 | 0.003 | 10/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.864× | -4.1 | 0.003 | 8/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dexmedetomidine (drug)]] 5 µM |  | **0.804×** | -4.0 | 0.004 | 5/46 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Glasdegib (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.799×** | -4.0 | 0.004 | 3/47 (SW 900, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.876× | -3.7 | 0.012 | 5/48 (J82, SW480, …) | two highest doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.838× | -3.2 | 0.053 | 13/45 (NCI-H23, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 7.49 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.4) |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -20.5) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 7.72 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0668× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -9.2) |
| [[A-172 (line)]] | wt | 9.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.7) |
| [[A549 (line)]] | wt | 9.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 6.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -8.7) |
| [[C32 (line)]] | wt | 8.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.1) |
| [[COLO 205 (line)]] | alt | 9.88 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.115× (z -9.0) |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.143× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.8) |
| [[Hs 766T (line)]] | wt | 7.89 | 0 | 1 | — | [[Pimitespib (drug)]] 0.05 µM 0.0549× (z -12.0) |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.7) |
| [[J82 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.9) |
| [[KATO III (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 7.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0749× (z -18.5) |
| [[RKO (line)]] | wt | 10.7 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0670× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.2) |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GPAT4]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[DUSP22]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CERS2]] | +0.62 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.62 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[SMARCD2]] | +0.62 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[CMTM4]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NUTF2]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[POMGNT1]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CROCCP3]] | +0.61 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[STIM1]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NTAQ1]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB3]] | -0.61 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.60 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.60 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[GORAB]] | -0.59 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[GOLGB1]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[LARP7]] | -0.58 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.57 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[RBM23]] | -0.57 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[FCF1]] | -0.56 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[ASF1A]] | -0.55 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[DARS1]] | -0.55 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[UBXN4]] | -0.54 | -0.62 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.4, -22.4); signed map (-45.7, -6.1). **Vector** length 68.7, 10.9% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.8 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -22.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 41 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2-q21.3 — chr3:126,006,357-126,101,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20473 |
| Gene groups (HGNC) | Solute carrier family 41 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GZ6](https://www.uniprot.org/uniprotkb/Q96GZ6) (Solute carrier family 41 member 3):

> Na(+)/Mg(2+) ion exchanger that acts as a predominant Mg(2+) efflux system at the mitochondrial inner membrane.

**Summary**, from NCBI Gene [54946](https://www.ncbi.nlm.nih.gov/gene/54946):

> Enables magnesium:sodium antiporter activity. Involved in mitochondrial magnesium ion transmembrane transport. Located in mitochondrial inner membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31046) · Entrez [54946](https://www.ncbi.nlm.nih.gov/gene/54946) · UniProt [Q96GZ6](https://www.uniprot.org/uniprotkb/Q96GZ6) · Ensembl [ENSG00000114544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114544)

## Data

Gene col 3564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3564); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3564]; `tensor/DDL_lfc|DDL_z.npy` [3564]; `embed/gene_vectors.npy` [3564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3564 or target_col == 3564). Every well: [[SLC41A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC41A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
