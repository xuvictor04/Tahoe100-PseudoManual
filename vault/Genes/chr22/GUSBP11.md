---
symbol: "GUSBP11"
type: "gene"
col: 13635
ensembl_id: "ENSG00000228315"
name: "GUSB pseudogene 11"
location: "22q11.23"
module: 172
arm: "+"
pooled_cpm: 34.56
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# GUSBP11

*GUSB pseudogene 11* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +4.7, q 7e-04, up in 26 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 1.24× (z +4.6, q 7e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.345× (z -8.6, q 3e-15, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A7]] (+0.66, fdr 7e-06), [[PPP6R2]] (+0.64, fdr 1e-05), [[ZNF254]] (+0.59, fdr 1e-05); moves opposite to [[PKM]] (-0.54, fdr 2e-05), [[SCOC]] (-0.53, fdr 4e-05), [[ANXA2]] (-0.52, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +4.7 | 7e-04 | 26/47 (LS 180, RKO, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.24×** | +4.6 | 7e-04 | 25/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.6 | 7e-04 | 21/48 (LoVo, PANC-1, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 1e-03 | 26/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +4.2 | 0.003 | 21/48 (J82, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.007 | 23/48 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.011 | 21/47 (NCI-H460, HCT15, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.012 | 20/48 (KATO III, SW 900, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +3.7 | 0.012 | 16/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.19× | +3.7 | 0.012 | 14/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.014 | 17/48 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 14/48 (COLO 205, J82, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.036 | 11/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.036 | 16/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.039 | 15/48 (RKO, SW480, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.039 | 17/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.039 | 11/48 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | 1.16× | +3.2 | 0.043 | 9/49 (SNU-423, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -8.6 | 3e-15 | 41/49 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -8.3 | 3e-14 | 34/48 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.692×** | -5.7 | 2e-06 | 28/45 (C-33 A, SHP-77, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -5.7 | 2e-06 | 32/48 (SNU-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -5.5 | 5e-06 | 25/44 (C32, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.737×** | -4.8 | 2e-04 | 22/48 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.730×** | -4.7 | 2e-04 | 21/40 (HepG2/C3A, HCT15, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.624×** | -3.8 | 0.009 | 14/33 (HepG2/C3A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.807×** | -3.3 | 0.053 | 22/47 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | 0.820× | -3.1 | 0.10 | 21/46 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.684× | -3.1 | 0.10 | 14/47 (RPMI-7951, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 33.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -12.2) |
| [[SNU-423 (line)]] | alt | 43.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.2) |
| [[A-427 (line)]] | wt | 41.9 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C-33 A (line)]] | alt | 66.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0904× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[MIA PaCa-2 (line)]] | alt | 71.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 35.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0985× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0934× (z -10.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0841× (z -10.3) |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 25.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -11.0) |
| [[KATO III (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H23 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[RKO (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -11.0) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0710× (z -9.6) |
| [[SW1417 (line)]] | alt | 49.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.4) |
| [[SW48 (line)]] | wt | 54.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.3) |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A7]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PPP6R2]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZNF254]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NCBP3]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LMF1]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[PHYKPL]] | +0.57 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[TRIR]] ⚠ | +0.55 | +0.54 / +0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC66A1]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZFYVE26]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[YBEY]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[GPATCH3]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[MAU2]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[KMT2B]] | +0.53 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKM]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SCOC]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ANXA2]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RAB11A]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MDH1]] | -0.50 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[SMAP2]] | -0.47 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[BOLA3]] | -0.47 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[YWHAZ]] | -0.47 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[GLUD1]] | -0.45 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[POGLUT2]] | -0.45 | -0.59 / -0.20 | both halves | 7e-04 |  |
| [[PRCP]] | -0.44 | -0.24 / -0.50 | both halves | 5e-04 |  |
| [[HERC3]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers GUSBP11's level | compounds that target MTOR: 4 of 8 raise it (Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 4.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.9, 12.4); signed map (-2.3, -11.0). **Vector** length 94.5, 22.2% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +4.2 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | GUSB pseudogene 11 |
| Locus type | pseudogene |
| Location | 22q11.23 — chr22:23,638,487-23,717,356 (-) |
| Ensembl biotype | lncRNA |
| Matched by | symbol |

UniProt [Q6P575](https://www.uniprot.org/uniprotkb/Q6P575) carries no function annotation.

**Summary**, from NCBI Gene [91316](https://www.ncbi.nlm.nih.gov/gene/91316):

> This transcribed pseudogene is similar to two functional genes. The 5' portion of the pseudogene is related to glucuronidase, beta, and the 3' portion is related to immunoglobulin lambda-like polypeptide 1. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:42325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42325) · Entrez [91316](https://www.ncbi.nlm.nih.gov/gene/91316) · UniProt [Q6P575](https://www.uniprot.org/uniprotkb/Q6P575) · Ensembl [ENSG00000228315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228315)

## Data

Gene col 13635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13635); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13635]; `tensor/DDL_lfc|DDL_z.npy` [13635]; `embed/gene_vectors.npy` [13635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13635 or target_col == 13635). Every well: [[GUSBP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUSBP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
