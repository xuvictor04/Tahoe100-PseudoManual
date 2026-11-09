---
symbol: "UBAC1"
type: "gene"
col: 5084
ensembl_id: "ENSG00000130560"
name: "UBA domain containing 1"
location: "9q34.3"
module: 57
arm: "+"
pooled_cpm: 21.5
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# UBAC1

*UBA domain containing 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +11.8, q 1e-29, up in 33 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.21× (z +4.6, q 5e-04, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 2.86×, LS 180 3.06×, LoVo 3.12×, SW480 2.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 4.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -12.8, q 2e-34, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.77, fdr 7e-06), [[SKP2]] (+0.72, fdr 1e-05), [[HACE1]] (+0.71, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.68, fdr 7e-05), [[MIRLET7IHG]] (-0.65, fdr 5e-05), [[WARS2-AS1]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5084.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 2.86×, LS 180 3.06×, LoVo 3.12×, SW480 2.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 4.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.00×** | +11.8 | 1e-29 | 33/41 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.84×** | +10.0 | 7e-21 | 26/32 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.56×** | +6.9 | 9e-10 | 23/35 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.37×** | +5.3 | 1e-05 | 23/43 (BT-474, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.7 | 3e-04 | 17/48 (RKO, SW480, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.6 | 5e-04 | 20/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.25×** | +3.8 | 0.011 | 19/48 (SW480, RKO, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **1.25×** | +3.7 | 0.018 | 17/44 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.21×** | +3.3 | 0.056 | 12/47 (SW480, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.22×** | +3.3 | 0.056 | 15/46 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.058 | 11/48 (C32, SW 1088, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.0 | 0.12 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -12.8 | 2e-34 | 34/47 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -8.6 | 2e-15 | 30/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.674×** | -6.5 | 2e-08 | 27/47 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.756×** | -4.8 | 3e-04 | 20/47 (SW480, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.091 | 10/47 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.827× | -3.2 | 0.11 | 6/47 (C32, SW480, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.1 | 0.16 | 10/48 (NCI-H1573, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.1) |
| [[SW480 (line)]] | alt | 23.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.8) |
| [[Hs 766T (line)]] | wt | 43.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.6) |
| [[LS 180 (line)]] | wt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.9) |
| [[A-427 (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.6) |
| [[A498 (line)]] | wt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.4) |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[LoVo (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 9.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.2) |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.6) |
| [[A-172 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.77 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[SKP2]] | +0.72 | +0.73 / +0.55 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[HACE1]] | +0.71 | +0.71 / +0.55 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SLC9A6]] | +0.70 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[VDAC3]] | +0.70 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.69 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MRI1]] | +0.68 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[STX7]] | +0.68 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[USP48]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 | STRING 625 |
| [[NUDT21]] | +0.67 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.68 | -0.72 / -0.38 | both halves | 7e-05 |  |
| [[MIRLET7IHG]] | -0.65 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[WARS2-AS1]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[ANGPT2]] | -0.64 | -0.67 / -0.39 | both halves | 5e-05 |  |
| [[RAB30-DT]] | -0.64 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[NEPRO-AS1]] | -0.64 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[HELQ]] | -0.63 | -0.69 / -0.38 | both halves | 7e-05 |  |
| [[CFLAR-AS1]] | -0.63 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[FKRP]] | -0.62 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R1C]] | -0.62 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | -0.62 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[TUT7]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.771). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.1, -9.1); signed map (-36.9, -12.2). **Vector** length 69.2, 12.6% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.5 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.5 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.3 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +2.6 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | UBA domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:135,932,969-135,961,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GBDR1, KPC2; previously UBADC1 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSL1](https://www.uniprot.org/uniprotkb/Q9BSL1) (Ubiquitin-associated domain-containing protein 1):

> Non-catalytic component of the KPC complex, a E3 ubiquitin-protein ligase complex that mediates polyubiquitination of target proteins, such as CDKN1B and NFKB1. The KPC complex catalyzes polyubiquitination and proteasome-mediated degradation of CDKN1B during G1 phase of the cell cycle. The KPC complex also acts as a key regulator of the NF-kappa-B signaling by promoting maturation of the NFKB1 component of NF-kappa-B by catalyzing ubiquitination of the NFKB1 p105 precursor. Within the KPC …

**Summary**, from NCBI Gene [10422](https://www.ncbi.nlm.nih.gov/gene/10422):

> Enables polyubiquitin modification-dependent protein binding activity and proteasome binding activity. Involved in protein maturation and protein ubiquitination. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30221) · Entrez [10422](https://www.ncbi.nlm.nih.gov/gene/10422) · UniProt [Q9BSL1](https://www.uniprot.org/uniprotkb/Q9BSL1) · Ensembl [ENSG00000130560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130560)

## Data

Gene col 5084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5084); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5084]; `tensor/DDL_lfc|DDL_z.npy` [5084]; `embed/gene_vectors.npy` [5084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5084 or target_col == 5084). Every well: [[UBAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
