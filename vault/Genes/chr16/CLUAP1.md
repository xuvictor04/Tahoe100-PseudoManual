---
symbol: "CLUAP1"
type: "gene"
col: 2357
ensembl_id: "ENSG00000103351"
name: "intraflagellar transport 38"
location: "16p13.3"
module: 28
arm: "+"
pooled_cpm: 23.12
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CLUAP1

*intraflagellar transport 38* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +11.8, q 4e-29, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.681× (z -6.2, q 3e-07, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM4]] (+0.70, fdr 7e-06), [[OSCP1]] (+0.68, fdr 7e-06), [[INTU]] (+0.67, fdr 7e-06); moves opposite to [[RELL1]] (-0.62, fdr 1e-05), [[SPCS3]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +11.8 | 4e-29 | 36/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +10.1 | 1e-21 | 29/43 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.7 | 2e-12 | 25/36 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +7.6 | 5e-12 | 29/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +7.1 | 1e-10 | 24/41 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +7.0 | 2e-10 | 35/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.1 | 8e-08 | 28/48 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +6.0 | 1e-07 | 27/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 8e-07 | 28/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.2 | 1e-05 | 27/48 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 8e-05 | 21/48 (AsPC-1, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.4 | 6e-04 | 22/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.2 | 9e-04 | 19/44 (A-427, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.001 | 16/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.002 | 16/47 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 18/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.008 | 20/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.011 | 18/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.029 | 16/48 (HOP62, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -6.2 | 3e-07 | 26/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.709×** | -5.6 | 7e-06 | 27/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.778×** | -4.1 | 0.009 | 17/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.785×** | -3.9 | 0.011 | 18/47 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.786×** | -3.9 | 0.011 | 19/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -3.0 | 0.25 | 11/48 (MIA PaCa-2, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 24.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.31× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) | — |
| [[LoVo (line)]] | wt | 21.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.99× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -10.4) |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.115× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 10.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.171× (z -9.8) |
| [[C32 (line)]] | wt | 21.6 | 0 | 2 (2 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.160× (z -10.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H2030 (line)]] | alt | 22.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.36× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.6) | — |
| [[A-427 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -10.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0805× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.147× (z -9.0) |
| [[LS 180 (line)]] | wt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.253× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -8.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.226× (z -9.9) |
| [[A-172 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | +0.70 | +0.82 / +0.61 | both halves | 7e-06 |  |
| [[OSCP1]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[INTU]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RNF214]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SETD2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.63 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[SMARCE1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PMPCB]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.62 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.61 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[LARP7]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SNW1]] | +0.60 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.62 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[SPCS3]] | -0.53 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.7, 2.5); signed map (6.5, -26.6). **Vector** length 81.5, 16.2% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,500,976-3,539,048 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13297, KIAA0643, FAP22, CFAP22; previously CLUAP1 |
| Gene groups (HGNC) | Cilia and flagella associated; IFT-B2 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AJ1](https://www.uniprot.org/uniprotkb/Q96AJ1) (Intraflagellar transport protein 38):

> Component of the intraflagellar transport (IFT) complex B required for transport of proteins in the motile cilium. Plays an essential role in ciliogenesis and in peripheral subcomplex construction (By similarity).

**Summary**, from NCBI Gene [23059](https://www.ncbi.nlm.nih.gov/gene/23059):

> The protein encoded by this gene contains a single coiled-coil region. Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:19009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19009) · Entrez [23059](https://www.ncbi.nlm.nih.gov/gene/23059) · UniProt [Q96AJ1](https://www.uniprot.org/uniprotkb/Q96AJ1) · Ensembl [ENSG00000103351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103351)

## Data

Gene col 2357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2357); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2357]; `tensor/DDL_lfc|DDL_z.npy` [2357]; `embed/gene_vectors.npy` [2357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2357 or target_col == 2357). Every well: [[CLUAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLUAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
