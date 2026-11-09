---
symbol: "RFESD"
type: "gene"
col: 10610
ensembl_id: "ENSG00000175449"
name: "Rieske Fe-S domain containing"
location: "5q15"
module: 5
arm: "-"
pooled_cpm: 2.35
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 12
n_dd_up_clean: 23
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RFESD

*Rieske Fe-S domain containing* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.66× (z +15.4, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.643× (z -5.2, q 9e-05, down in 12 of 41 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP3]] (+0.54, fdr 8e-05), [[RYBP]] (+0.53, fdr 7e-05), [[LINC00408]] (+0.52, fdr 1e-04); moves opposite to [[GNAQ]] (-0.58, fdr 1e-05), [[MFSD14CP-1]] (-0.53, fdr 1e-04), [[ATP11C]] (-0.53, fdr 5e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.66×** | +15.4 | 0e+00 | 42/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +15.4 | 0e+00 | 33/43 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.45×** | +14.7 | 0e+00 | 36/42 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +10.8 | 4e-25 | 26/43 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +9.3 | 1e-18 | 14/32 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.3 | 2e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +8.6 | 9e-16 | 21/45 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +8.3 | 5e-15 | 16/36 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.9 | 2e-13 | 12/30 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +7.2 | 3e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +7.0 | 1e-10 | 8/13 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.2 | 9e-06 | 10/44 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.50×** | +4.9 | 5e-05 | 7/44 (NCI-H2347, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +4.4 | 4e-04 | 5/38 (J82, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.002 | 2/31 (SW480, NCI-H1792) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 8/40 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.004 | 4/28 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.007 | 9/40 (NCI-H2030, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.643×** | -5.2 | 9e-05 | 12/41 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -5.1 | 1e-04 | 11/37 (SNU-423, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -4.8 | 3e-04 | 7/36 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.679×** | -4.4 | 0.002 | 8/36 (NCI-H2030, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -4.0 | 0.007 | 13/39 (PANC-1, RKO, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -3.8 | 0.012 | 12/47 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -3.8 | 0.012 | 14/41 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.015 | 9/45 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.061 | 7/45 (SNU-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.061 | 7/42 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | **0.749×** | -3.2 | 0.075 | 5/32 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Captopril (drug)]] 0.5 µM |  | **0.770×** | -3.1 | 0.084 | 2/39 (SW1417, SHP-77) | inconsistent across doses | position effect removed |
| [[Malotilate (drug)]] 0.5 µM |  | **0.770×** | -3.1 | 0.084 | 4/37 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.72 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0628× (z -9.4) |
| [[A-172 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.929 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | +0.54 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[RYBP]] | +0.53 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[LINC00408]] | +0.52 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[XRRA1]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FKBP15]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PPP2R2A]] | +0.50 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[HILPDA]] | +0.49 | +0.12 / +0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[NR1D1]] | +0.49 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[ARFGEF3]] | +0.49 | +0.18 / +0.40 | ⚠ not reproduced | 0.001 |  |
| [[YEATS2]] | +0.48 | +0.10 / +0.40 | ⚠ not reproduced | 0.003 |  |
| [[WDR89]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ZNF571]] | +0.48 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CLEC4A]] | +0.47 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[CYTH4]] | +0.47 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[SNAPC1]] | +0.47 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAQ]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | -0.53 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ATP11C]] | -0.53 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[NCOA2]] | -0.51 | -0.24 / -0.63 | both halves | 4e-04 |  |
| [[XNDC1N]] | -0.50 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[C1orf159]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[APH1A]] | -0.49 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[COP1]] | -0.49 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.48 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SNTB2]] | -0.48 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[MAVS]] | -0.47 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[NPLOC4]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.232). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (16.2, -12.5); signed map (-9.0, 16.8). **Vector** length 38.9, 4.00% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.2 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Rieske Fe-S domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:95,646,777-95,684,773 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q8TAC1](https://www.uniprot.org/uniprotkb/Q8TAC1) carries no function annotation.

**Summary**, from NCBI Gene [317671](https://www.ncbi.nlm.nih.gov/gene/317671):

> Predicted to enable 2 iron, 2 sulfur cluster binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29587) · Entrez [317671](https://www.ncbi.nlm.nih.gov/gene/317671) · UniProt [Q8TAC1](https://www.uniprot.org/uniprotkb/Q8TAC1) · Ensembl [ENSG00000175449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175449)

## Data

Gene col 10610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10610); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10610]; `tensor/DDL_lfc|DDL_z.npy` [10610]; `embed/gene_vectors.npy` [10610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10610 or target_col == 10610). Every well: [[RFESD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFESD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
