---
symbol: "CROCCP2-1"
type: "gene"
col: 16566
ensembl_id: "ENSG00000291072"
name: ""
location: ""
module: 20
arm: "-"
pooled_cpm: 17.33
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CROCCP2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +12.4, q 2e-32, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.12× (z +6.1, q 2e-07, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.281× (z -5.4, q 4e-05, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.126×, CFPAC-1 0.0942×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.144×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.208×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.76, fdr 7e-06), [[SMIM26]] (+0.75, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPS18C]] (+0.74, fdr 7e-06), [[EIF1B]] (+0.73, fdr 7e-06); moves opposite to [[BPNT2]] (-0.74, fdr 7e-06), [[PGAM1]] (-0.74, fdr 7e-06), [[TXNDC5]] (-0.73, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.93×** | +12.4 | 2e-32 | 46/47 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.54×** | +7.3 | 8e-11 | 44/47 (SW480, HS-578T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +6.1 | 2e-07 | 37/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.93×** | +5.4 | 1e-05 | 32/46 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.0 | 0.008 | 28/44 (Panc 03.27, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.086 | 25/48 (NCI-H1792, SW 900, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.086 | 25/47 (HCT15, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.47× | +3.1 | 0.11 | 19/46 (SW480, NCI-H23, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.47× | +3.1 | 0.11 | 19/47 (HS-578T, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16566.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.126×, CFPAC-1 0.0942×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.144×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.208×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -5.4 | 4e-05 | 41/48 (C32, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.552×** | -4.9 | 3e-04 | 36/48 (LOX-IMVI, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.405×** | -3.9 | 0.022 | 30/45 (HOP62, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.96 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 25.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -10.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 8.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0739× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 54.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +9.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.75 | +0.66 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PPIG]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PIAS4]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.70 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[GGNBP2]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ERVK3-1]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MAP2K7]] | +0.66 | +0.42 / +0.72 | both halves | 4e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT2]] | -0.74 | -0.69 / -0.77 | both halves | 7e-06 |  |
| [[PGAM1]] | -0.74 | -0.76 / -0.72 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.73 | -0.68 / -0.77 | both halves | 7e-06 |  |
| [[RPSA]] | -0.73 | -0.72 / -0.71 | both halves | 7e-06 |  |
| [[FKBP9]] | -0.71 | -0.70 / -0.72 | both halves | 7e-06 |  |
| [[ANKRD30BL]] | -0.70 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[RPN1]] | -0.70 | -0.64 / -0.72 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.69 | -0.72 / -0.69 | both halves | 7e-06 |  |
| [[ILF2]] | -0.69 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[EEF1A1]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[EMC1]] | -0.67 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[RPL10]] | -0.67 | -0.64 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.845). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.0, -23.4); signed map (-14.9, -0.5). **Vector** length 102, 29.2% of its response variance represented; |z| ≥ 3 in 574 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.0 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.9 | +7.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +2.9 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.4 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.7 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.2 |

## What is on record

> [!warning] No registry record
> CROCCP2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16566); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16566]; `tensor/DDL_lfc|DDL_z.npy` [16566]; `embed/gene_vectors.npy` [16566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16566 or target_col == 16566). Every well: [[CROCCP2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CROCCP2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
