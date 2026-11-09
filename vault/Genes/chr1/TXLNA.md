---
symbol: "TXLNA"
type: "gene"
col: 1404
ensembl_id: "ENSG00000084652"
name: "taxilin alpha"
location: "1p35.2"
module: 59
arm: "-"
pooled_cpm: 56.73
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TXLNA

*taxilin alpha* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.62× (z +8.9, q 2e-16, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.52× (z +7.7, q 3e-12, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.459×, A-427 0.557×; ⚠ cell-cycle shift, explains ~59% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0965×; ⚠ toxic; cell-cycle shift, explains ~35% of this change); [[Acetohexamide (drug)]] 0.5 µM in 1 line (NCI-H661 0.0521×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP7]] (+0.67, fdr 7e-06), [[GRWD1]] (+0.67, fdr 7e-06), [[ABCF2]] (+0.62, fdr 1e-05); moves opposite to [[PIAS1]] (-0.66, fdr 1e-05), [[CERT1]] (-0.63, fdr 1e-05), [[KMT2E]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +8.9 | 2e-16 | 45/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.7 | 3e-12 | 37/48 (SW480, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.35×** | +5.5 | 5e-06 | 38/48 (SW480, KATO III, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.31×** | +4.8 | 2e-04 | 27/47 (SW480, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 0.001 | 25/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.009 | 21/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.017 | 19/48 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.22×** | +3.6 | 0.019 | 21/48 (SW480, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.027 | 16/48 (LoVo, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +3.4 | 0.035 | 22/48 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.085 | 21/48 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.0 | 0.12 | 11/48 (LoVo, SNU-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.459×, A-427 0.557×; ⚠ cell-cycle shift, explains ~59% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0965×; ⚠ toxic; cell-cycle shift, explains ~35% of this change); [[Acetohexamide (drug)]] 0.5 µM in 1 line (NCI-H661 0.0521×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -4.6 | 0.003 | 16/48 (SHP-77, A498, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.834× | -3.4 | 0.16 | 20/48 (SW 1088, RKO, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.882× | -3.3 | 0.16 | 18/48 (C-33 A, A-427, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.3 | 0.16 | 22/48 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.16 | 19/47 (A-172, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.791× | -3.1 | 0.16 | 15/48 (LoVo, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.728× | -3.1 | 0.16 | 15/47 (AN3 CA, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 74.6 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HepG2_C3A (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0965× (z -17.8) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.462× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 52.2 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0521× (z -11.3) |
| [[RKO (line)]] | wt | 89.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.44× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.115× (z -10.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 56.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.17× (z +9.9) | — |
| [[A-172 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP7]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PSME3]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NOLC1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ARMC6]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[C19orf48]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRRC59]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PYGO2]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS1]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[CERT1]] | -0.63 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ARID4A]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[SPTBN1-AS2]] | -0.57 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZNF821]] | -0.57 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[MICU1]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.56 | -0.49 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB9A]] | -0.56 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.56 | -0.44 / -0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM59]] | -0.56 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[KBTBD3]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-15.8, -34.3); signed map (-6.3, -43.0). **Vector** length 103, 24.9% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.0 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.9 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.9 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | taxilin alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,179,675-32,198,285 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp451J0118, IL-14, IL14 |
| Reactome | 3 pathways, smallest: Other interleukin signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P40222](https://www.uniprot.org/uniprotkb/P40222) (Alpha-taxilin):

> May be involved in intracellular vesicle traffic and potentially in calcium-dependent exocytosis in neuroendocrine cells.

**Summary**, from NCBI Gene [200081](https://www.ncbi.nlm.nih.gov/gene/200081):

> Predicted to be involved in exocytosis. Predicted to act upstream of or within B cell activation. Located in cytoplasm. Implicated in Sjogren's syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30685) · Entrez [200081](https://www.ncbi.nlm.nih.gov/gene/200081) · UniProt [P40222](https://www.uniprot.org/uniprotkb/P40222) · Ensembl [ENSG00000084652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084652)

## Data

Gene col 1404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1404); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1404]; `tensor/DDL_lfc|DDL_z.npy` [1404]; `embed/gene_vectors.npy` [1404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1404 or target_col == 1404). Every well: [[TXLNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXLNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
