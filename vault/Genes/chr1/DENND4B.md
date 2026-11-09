---
symbol: "DENND4B"
type: "gene"
col: 12700
ensembl_id: "ENSG00000198837"
name: "DENN domain containing 4B"
location: "1q21.3"
module: 2
arm: "+"
pooled_cpm: 18.79
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DENND4B

*DENN domain containing 4B* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.38× (z +6.1, q 5e-07, up in 22 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 1.58× (z +4.5, q 0.002, up in 13 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 1.81×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.503× (z -13.0, q 6e-36, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM65]] (+0.53, fdr 2e-05), [[LZTR1]] (+0.49, fdr 4e-05), [[PKN3]] (+0.48, fdr 4e-05); moves opposite to [[BBS9]] (-0.48, fdr 1e-04), [[RAB2A]] (-0.47, fdr 1e-04), [[CRIPT]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12700.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 1.81×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.1 | 5e-07 | 22/47 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.58×** | +4.5 | 0.002 | 13/44 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.12 | 8/45 (Hs 766T, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -13.0 | 6e-36 | 41/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.589×** | -10.0 | 3e-21 | 37/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -7.9 | 8e-13 | 30/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -6.5 | 1e-08 | 28/47 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -5.9 | 5e-07 | 23/48 (COLO 205, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -5.7 | 1e-06 | 22/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -5.2 | 2e-05 | 20/48 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -5.1 | 3e-05 | 18/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -5.0 | 3e-05 | 21/45 (C-33 A, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -5.0 | 3e-05 | 19/47 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -4.6 | 2e-04 | 20/46 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.801×** | -4.2 | 0.001 | 15/47 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.799×** | -4.1 | 0.002 | 21/44 (SHP-77, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.800×** | -3.9 | 0.004 | 17/36 (A549, LS 180, …) | inconsistent across doses | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.004 | 14/47 (A-427, SW48, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | 0.835× | -3.2 | 0.043 | 16/45 (KATO III, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.8 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.266× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.312× (z -12.5) |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0781× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.5) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.306× (z -8.9) |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0806× (z -9.1) |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0871× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0937× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM65]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LZTR1]] | +0.49 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[PKN3]] | +0.48 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[ULK3]] | +0.48 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[MTCH2]] | +0.47 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[IRAK1]] | +0.47 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[MAN2A2]] | +0.47 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[PATZ1]] | +0.46 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[GLOD4]] | +0.46 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[SGSH]] | +0.46 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[IPO13]] | +0.46 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[TBC1D9B]] | +0.46 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS9]] | -0.48 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[RAB2A]] | -0.47 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[CRIPT]] | -0.47 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[C18orf32]] | -0.43 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[OSBPL9]] | -0.43 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[NDFIP2]] | -0.43 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SARAF]] | -0.42 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[TMCO1]] | -0.42 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[HSBP1]] | -0.42 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[GOLM2]] | -0.41 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[LMBRD1]] | -0.41 | -0.24 / -0.36 | both halves | 5e-04 |  |
| [[TALAM1]] | -0.41 | -0.27 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.190). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.0, -26.6); signed map (5.8, -3.4). **Vector** length 70.9, 11.3% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +3.1 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -1.9 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Hydroxyurea (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,929,501-153,946,718 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0476 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O75064](https://www.uniprot.org/uniprotkb/O75064) (DENN domain-containing protein 4B):

> Guanine nucleotide exchange factor (GEF) which may activate RAB10. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form.

**Summary**, from NCBI Gene [9909](https://www.ncbi.nlm.nih.gov/gene/9909):

> Enables guanyl-nucleotide exchange factor activity. Involved in regulation of Rab protein signal transduction. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29044) · Entrez [9909](https://www.ncbi.nlm.nih.gov/gene/9909) · UniProt [O75064](https://www.uniprot.org/uniprotkb/O75064) · Ensembl [ENSG00000198837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198837)

## Data

Gene col 12700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12700); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12700]; `tensor/DDL_lfc|DDL_z.npy` [12700]; `embed/gene_vectors.npy` [12700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12700 or target_col == 12700). Every well: [[DENND4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
