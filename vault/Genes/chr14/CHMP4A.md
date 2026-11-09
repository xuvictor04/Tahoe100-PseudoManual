---
symbol: "CHMP4A"
type: "gene"
col: 14876
ensembl_id: "ENSG00000254505"
name: "charged multivesicular body protein 4A"
location: "14q12"
module: 170
arm: "+"
pooled_cpm: 31.29
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# CHMP4A

*charged multivesicular body protein 4A* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +15.4, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +11.2, q 5e-27, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.477× (z -5.4, q 5e-05, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCIAD1]] (+0.72, fdr 7e-06), [[ZNF764]] (+0.71, fdr 7e-06), [[NFKBIB]] (+0.71, fdr 7e-06); moves opposite to [[METAP1]] (-0.69, fdr 7e-06), [[HACD3]] (-0.68, fdr 7e-06), [[GRB2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 170]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +15.4 | 0e+00 | 44/44 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +14.2 | 5e-43 | 37/38 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +11.2 | 5e-27 | 43/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +9.2 | 7e-18 | 35/41 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +8.8 | 2e-16 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.4 | 1e-08 | 35/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.6 | 2e-06 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.39×** | +4.5 | 4e-04 | 22/45 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 8e-04 | 25/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.7 | 0.011 | 22/45 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -5.4 | 5e-05 | 34/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.027 | 18/48 (H4, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.027 | 23/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.795× | -3.2 | 0.17 | 16/48 (SW1417, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.796× | -3.2 | 0.17 | 18/47 (SW480, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 45.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 28.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 33.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.7) | — |
| [[A498 (line)]] | wt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.7) | — |
| [[LoVo (line)]] | wt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 34.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 43.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.7) | — |
| [[A-427 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.77× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.51× (z +11.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +11.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.344× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | +0.72 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.71 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[NFKBIB]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[LINC00174]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[ZNF554]] | +0.70 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[LZIC]] | +0.69 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[LARP7]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[UPF3B]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[CIRBP]] | +0.68 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[TRMT10B]] | +0.66 | +0.79 / +0.58 | both halves | 8e-06 |  |
| [[CCAR1]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.69 | -0.78 / -0.58 | both halves | 7e-06 |  |
| [[HACD3]] | -0.68 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[GRB2]] | -0.68 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[LRRC20]] | -0.67 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[RNF4]] | -0.66 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[LDHB]] | -0.66 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[SKP2]] | -0.66 | -0.77 / -0.57 | both halves | 1e-05 |  |
| [[NME2]] | -0.65 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[TMEM97]] | -0.64 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[NDC1]] | -0.64 | -0.74 / -0.53 | both halves | 1e-05 | pathway: HCMV Infection |
| [[POMGNT2]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[ARHGEF26]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-25.6, 9.1); signed map (9.6, -19.7). **Vector** length 86.9, 21.4% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.3 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,209,615-24,213,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC134, VPS32A, hSnf7-1, Snf7-1; previously C14orf123 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY43](https://www.uniprot.org/uniprotkb/Q9BY43) (Charged multivesicular body protein 4a):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [29082](https://www.ncbi.nlm.nih.gov/gene/29082):

> CHMP4A belongs to the chromatin-modifying protein/charged multivesicular body protein (CHMP) family. These proteins are components of ESCRT-III (endosomal sorting complex required for transport III), a complex involved in degradation of surface receptor proteins and formation of endocytic multivesicular bodies (MVBs). Some CHMPs have both nuclear and cytoplasmic/vesicular distributions, and one such CHMP, CHMP1A (MIM 164010), is required for both MVB formation and regulation of cell cycle …

**Accessions** — [HGNC:20274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20274) · Entrez [29082](https://www.ncbi.nlm.nih.gov/gene/29082) · UniProt [Q9BY43](https://www.uniprot.org/uniprotkb/Q9BY43) · Ensembl [ENSG00000254505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254505)

## Data

Gene col 14876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14876); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14876]; `tensor/DDL_lfc|DDL_z.npy` [14876]; `embed/gene_vectors.npy` [14876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14876 or target_col == 14876). Every well: [[CHMP4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
