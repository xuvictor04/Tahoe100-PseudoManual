---
symbol: "COQ7"
type: "gene"
col: 9431
ensembl_id: "ENSG00000167186"
name: "coenzyme Q7, hydroxylase"
location: "16p12.3"
module: 51
arm: "+"
pooled_cpm: 10.22
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# COQ7

*coenzyme Q7, hydroxylase* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +8.2, q 2e-13, up in 11 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.31× (z +6.1, q 1e-07, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.525× (z -10.1, q 2e-21, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM23]] (+0.77, fdr 7e-06), [[TRMO]] (+0.77, fdr 7e-06), [[LYRM2]] (+0.75, fdr 7e-06); moves opposite to [[RGS10]] (-0.68, fdr 1e-05), [[PIGF]] (-0.66, fdr 1e-05), [[RPS24]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.2 | 2e-13 | 11/22 (NCI-H2030, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +7.4 | 5e-11 | 14/28 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +6.3 | 6e-08 | 5/48 (Hs 766T, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +6.1 | 1e-07 | 17/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.6 | 3e-06 | 12/33 (Panc 03.27, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.007 | 11/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.031 | 9/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.060 | 9/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.061 | 4/47 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.12 | 6/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.22× | +3.0 | 0.13 | 14/46 (NCI-H1573, A498, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -10.1 | 2e-21 | 33/47 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.616×** | -7.6 | 9e-12 | 26/44 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.623×** | -7.4 | 2e-11 | 28/47 (AsPC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -7.1 | 2e-10 | 29/47 (NCI-H2347, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -6.9 | 6e-10 | 25/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -6.8 | 1e-09 | 21/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.691×** | -5.8 | 6e-07 | 21/45 (Hs 766T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.702×** | -5.5 | 2e-06 | 20/47 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.798×** | -5.0 | 4e-05 | 20/48 (SW 1271, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.730×** | -4.9 | 5e-05 | 17/46 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -4.8 | 1e-04 | 19/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.731×** | -4.7 | 1e-04 | 12/43 (A-427, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -4.7 | 1e-04 | 18/38 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.753×** | -4.4 | 4e-04 | 13/47 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -4.4 | 5e-04 | 14/46 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.075 | 8/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.690×** | -3.0 | 0.080 | 11/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.099 | 4/47 (Hs 766T, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 6.49 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0853× (z -9.8) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.174× (z -10.1) |
| [[A-427 (line)]] | wt | 9.76 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.112× (z -10.0) |
| [[C32 (line)]] | wt | 7.21 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.100× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.115× (z -9.2) |
| [[HOP62 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.287× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 8.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 9.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.2) | — |
| [[RKO (line)]] | wt | 6.58 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0854× (z -8.9) |
| [[SW480 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -13.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | +0.77 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TRMO]] | +0.77 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[LYRM2]] | +0.75 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[EPC2]] | +0.74 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TOR1AIP1]] | +0.71 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[SP2]] | +0.70 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[PMF1]] | +0.70 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[YJU2]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[USP16]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[AP5S1]] | +0.68 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[ZNF644]] | +0.68 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS10]] | -0.68 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[PIGF]] | -0.66 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[RPS24]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PALS2]] | -0.64 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.63 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[METAP1]] | -0.63 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.63 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[HEBP1]] | -0.63 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TRABD]] | -0.62 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[FAM24B]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RPS21]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.0, 11.1); signed map (12.0, -29.8). **Vector** length 63.9, 9.39% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.8 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.2 | +3.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q7, hydroxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,067,614-19,080,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLK-1, CAT5 |
| Gene groups (HGNC) | Oxygenases |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99807](https://www.uniprot.org/uniprotkb/Q99807) (NADPH-dependent 3-demethoxyubiquinone 3-hydroxylase, mitochondrial):

> Catalyzes the hydroxylation of the 5-methoxy-2-methyl-3-(all-trans-polyprenyl)benzoquinone at the C6 position and participates in the biosynthesis of ubiquinone (Probable). Catalyzes the reaction through a substrate-mediated reduction pathway, whereby NADH shuttles electrons to 5-methoxy-2-methyl-3-(all-trans-decaprenyl)benzoquinone, which then transfers the electrons to the two Fe(3+) centers. The binding of 5-methoxy-2-methyl-3-(all-trans-polyprenyl)benzoquinone (DMQn) mediates reduction of …

**Summary**, from NCBI Gene [10229](https://www.ncbi.nlm.nih.gov/gene/10229):

> The protein encoded by this gene is similar to a mitochondrial di-iron containing hydroxylase in Saccharomyces cerevisiae that is involved with ubiquinone biosynthesis. Mutations in the yeast gene lead to slower development and longer life span. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:2244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2244) · Entrez [10229](https://www.ncbi.nlm.nih.gov/gene/10229) · UniProt [Q99807](https://www.uniprot.org/uniprotkb/Q99807) · Ensembl [ENSG00000167186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167186)

## Data

Gene col 9431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9431); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9431]; `tensor/DDL_lfc|DDL_z.npy` [9431]; `embed/gene_vectors.npy` [9431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9431 or target_col == 9431). Every well: [[COQ7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
