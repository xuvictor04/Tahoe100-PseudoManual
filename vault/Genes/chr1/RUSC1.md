---
symbol: "RUSC1"
type: "gene"
col: 8377
ensembl_id: "ENSG00000160753"
name: "RUN and SH3 domain containing 1"
location: "1q22"
module: 2
arm: "+"
pooled_cpm: 11.84
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RUSC1

*RUN and SH3 domain containing 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.01× (z +8.6, q 5e-15, up in 12 of 22 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +8.2, q 5e-14, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.458× (z -10.0, q 1e-20, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMF2]] (+0.66, fdr 7e-06), [[TMUB1]] (+0.65, fdr 7e-06), [[SLC25A1]] (+0.64, fdr 1e-05); moves opposite to [[JPX]] (-0.60, fdr 2e-05), [[ERCC6]] (-0.57, fdr 1e-05), [[RGS5]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.01×** | +8.6 | 5e-15 | 12/22 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.2 | 5e-14 | 28/45 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.85×** | +7.9 | 7e-13 | 25/34 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.1 | 5e-05 | 19/41 (AsPC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.44×** | +4.4 | 0.001 | 16/39 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +4.2 | 0.002 | 13/46 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.002 | 16/43 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.37×** | +4.0 | 0.005 | 15/47 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.35×** | +3.7 | 0.013 | 16/44 (LS 180, NCI-H460, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.33×** | +3.6 | 0.015 | 14/47 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.018 | 4/37 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.32×** | +3.3 | 0.053 | 14/29 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.055 | 10/43 (SW1417, A498, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.29×** | +3.1 | 0.080 | 10/40 (PANC-1, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -10.0 | 1e-20 | 31/44 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -8.3 | 4e-14 | 32/44 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -4.8 | 3e-04 | 23/45 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -4.5 | 8e-04 | 20/43 (hTERT-HPNE, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.030 | 18/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -3.0 | 0.22 | 12/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.791× | -3.0 | 0.22 | 12/45 (SW480, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 11.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.6) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.2) |
| [[A498 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 7.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -8.9) |
| [[RKO (line)]] | wt | 9.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -8.6) |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMF2]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TMUB1]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ZFYVE21]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[RNF38]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[GIT1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MICA]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TP53I13]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD9]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DCUN1D4]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPX]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[RGS5]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MDM4]] | -0.53 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[DDX18]] | -0.53 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[CHURC1]] | -0.53 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[CWC22]] | -0.52 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[USP40]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ZNF121]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[COMMD10]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CAAP1]] | -0.51 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[ZNF780B]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.9, -20.3); signed map (-40.0, -0.9). **Vector** length 68.1, 12.3% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.1 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.4 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +5.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | RUN and SH3 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,320,894-155,331,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NESCA |
| Gene groups (HGNC) | RUN domain containing; RUN and SH3 domain containing family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVN2](https://www.uniprot.org/uniprotkb/Q9BVN2) (AP-4 complex accessory subunit RUSC1):

> Associates with the adapter-like complex 4 (AP-4) and may therefore play a role in vesicular trafficking of proteins at the trans-Golgi network. Signaling adapter which plays a role in neuronal differentiation. Involved in regulation of NGF-dependent neurite outgrowth. May play a role in neuronal vesicular trafficking, specifically involving pre-synaptic membrane proteins (By similarity). Seems to be involved in signaling pathways that are regulated by the prolonged activation of MAPK. Can …

**Summary**, from NCBI Gene [23623](https://www.ncbi.nlm.nih.gov/gene/23623):

> Predicted to enable actin binding activity. Involved in protein polyubiquitination. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17153) · Entrez [23623](https://www.ncbi.nlm.nih.gov/gene/23623) · UniProt [Q9BVN2](https://www.uniprot.org/uniprotkb/Q9BVN2) · Ensembl [ENSG00000160753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160753)

## Data

Gene col 8377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8377); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8377]; `tensor/DDL_lfc|DDL_z.npy` [8377]; `embed/gene_vectors.npy` [8377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8377 or target_col == 8377). Every well: [[RUSC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUSC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
