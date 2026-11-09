---
symbol: "CNPPD1"
type: "gene"
col: 3705
ensembl_id: "ENSG00000115649"
name: "cyclin Pas1/PHO80 domain containing 1"
location: "2q35"
module: 24
arm: "+"
pooled_cpm: 13.85
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CNPPD1

*cyclin Pas1/PHO80 domain containing 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.76× (z +8.9, q 3e-16, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.498× (z -5.7, q 3e-06, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RETREG2]] (+0.58, fdr 1e-05, ⚠ same locus), [[SIRT7]] (+0.55, fdr 2e-05), [[FBXW5]] (+0.53, fdr 3e-05), [[DNAJB2]] (+0.53, fdr 4e-05); moves opposite to [[C1QBP]] (-0.50, fdr 3e-05), [[SNRPF]] (-0.45, fdr 8e-05), [[COA1]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.9 | 3e-16 | 35/47 (LoVo, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.5 | 2e-08 | 3/48 (J82, HepG2/C3A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.9 | 2e-04 | 17/37 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.5 | 9e-04 | 16/42 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.31×** | +4.0 | 0.006 | 14/46 (J82, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.007 | 16/47 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.012 | 13/47 (LOX-IMVI, J82, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.25×** | +3.5 | 0.034 | 8/45 (NCI-H460, A549, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.040 | 8/47 (A549, SW480, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.040 | 8/47 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.043 | 5/44 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.043 | 13/44 (COLO 205, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.11 | 10/48 (PANC-1, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -5.7 | 3e-06 | 23/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.696×** | -5.7 | 3e-06 | 21/46 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -5.7 | 3e-06 | 22/47 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -5.6 | 3e-06 | 19/48 (CFPAC-1, J82, …) | rises with dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.755×** | -4.4 | 0.001 | 17/44 (COLO 205, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Furosemide (drug)]] 0.5 µM |  | **0.757×** | -4.4 | 0.001 | 16/45 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.832×** | -4.1 | 0.003 | 20/47 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.772×** | -4.1 | 0.003 | 16/48 (NCI-H23, HS-578T, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.015 | 17/44 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.796×** | -3.6 | 0.020 | 14/47 (A-172, A549, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.803×** | -3.4 | 0.029 | 10/47 (J82, SK-MEL-2, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.860× | -3.4 | 0.037 | 7/48 (LS 180, HS-578T, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.815×** | -3.2 | 0.056 | 15/47 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.810×** | -3.2 | 0.058 | 14/45 (HS-578T, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.695×** | -3.0 | 0.099 | 11/38 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.099 | 11/47 (A549, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.5) |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.6) |
| [[J82 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -8.5) |
| [[LoVo (line)]] | wt | 10.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.60× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.4) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RETREG2]] | +0.58 | +0.53 / +0.65 | both halves | 1e-05 | STRING 516; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SIRT7]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[FBXW5]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[DNAJB2]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZFP90]] | +0.53 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[RCE1]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TRADD]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[MIEF2]] | +0.51 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[RRAGC]] | +0.50 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[DUSP18]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[DYNC1I2]] | +0.49 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[CIDECP1]] | +0.49 | +0.26 / +0.46 | both halves | 4e-04 |  |
| [[VPS35]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QBP]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SNRPF]] | -0.45 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[COA1]] | -0.45 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CDC7]] | -0.45 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CTSC]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[MRPS27]] | -0.44 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ERH]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SLC19A3]] | -0.44 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[R3HDM1]] | -0.43 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PPA2]] | -0.43 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ADGRA3]] | -0.43 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[SNRPD1]] | -0.42 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.221). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.0, -15.7); signed map (-23.4, 7.7). **Vector** length 67.4, 11.0% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.6 | +4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +2.6 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin Pas1/PHO80 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,171,897-219,178,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-57; previously C2orf24 |
| Matched by | ensembl_id |

UniProt [Q9BV87](https://www.uniprot.org/uniprotkb/Q9BV87) carries no function annotation.

**Summary**, from NCBI Gene [27013](https://www.ncbi.nlm.nih.gov/gene/27013):

> Predicted to enable cyclin-dependent protein serine/threonine kinase regulator activity. Predicted to be located in membrane. Predicted to be part of cyclin-dependent protein kinase holoenzyme complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25220) · Entrez [27013](https://www.ncbi.nlm.nih.gov/gene/27013) · UniProt [Q9BV87](https://www.uniprot.org/uniprotkb/Q9BV87) · Ensembl [ENSG00000115649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115649)

## Data

Gene col 3705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3705); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3705]; `tensor/DDL_lfc|DDL_z.npy` [3705]; `embed/gene_vectors.npy` [3705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3705 or target_col == 3705). Every well: [[CNPPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNPPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
