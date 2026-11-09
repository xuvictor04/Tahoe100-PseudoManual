---
symbol: "CHPF2"
type: "gene"
col: 411
ensembl_id: "ENSG00000033100"
name: "chondroitin polymerizing factor 2"
location: "7q36.1"
module: 52
arm: "+"
pooled_cpm: 11.77
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# CHPF2

*chondroitin polymerizing factor 2* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.7, q 6e-06, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.415× (z -9.4, q 2e-18, down in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SK-MEL-2 0.243×, C32 0.296×, AsPC-1 0.285×; ⚠ cell-cycle shift, explains ~37% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.0857×, BT-474 0.114×; ⚠ cell-cycle shift, explains ~47% of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (H4 0.0732×, RPMI-7951 0.147×); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.209×, A-172 0.137×); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0812×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGAP1]] (+0.72, fdr 7e-06), [[RER1]] (+0.70, fdr 7e-06), [[NT5DC2]] (+0.63, fdr 7e-06); moves opposite to [[SMC3]] (-0.54, fdr 3e-05), [[YEATS4]] (-0.51, fdr 3e-05), [[LRRCC1]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.7 | 6e-06 | 27/44 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.5 | 1e-05 | 15/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.2 | 0.004 | 20/42 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.004 | 16/46 (Hs 766T, HOP62, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.006 | 18/44 (NCI-H1792, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.006 | 17/45 (PANC-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.006 | 13/41 (Hs 766T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.006 | 14/45 (J82, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.9 | 0.006 | 11/30 (BT-474, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +3.7 | 0.010 | 11/45 (SW480, COLO 205, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +3.6 | 0.018 | 11/43 (HOP62, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.032 | 13/48 (SW48, A498, …) | top dose only | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.048 | 16/44 (SW 900, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SK-MEL-2 0.243×, C32 0.296×, AsPC-1 0.285×; ⚠ cell-cycle shift, explains ~37% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.0857×, BT-474 0.114×; ⚠ cell-cycle shift, explains ~47% of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (H4 0.0732×, RPMI-7951 0.147×); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.209×, A-172 0.137×); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0812×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.415×** | -9.4 | 2e-18 | 36/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.570×** | -8.9 | 2e-16 | 33/46 (SK-MEL-2, C32, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -5.1 | 8e-05 | 24/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.704×** | -3.9 | 0.012 | 19/48 (NCI-H460, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.744× | -3.2 | 0.17 | 17/40 (LoVo, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -11.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 10.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C32 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 15.3 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0732× (z -9.7) |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0812× (z -11.3) |
| [[J82 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 7.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 7.03 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -9.2) |
| [[RKO (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.147× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 6.99 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.106× (z -8.5) |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0857× (z -10.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0654× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP1]] | +0.72 | +0.73 / +0.75 | both halves | 7e-06 | same gene group |
| [[RER1]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[NT5DC2]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GMPPB]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ZNF587]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[SLC35C1]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SYVN1]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 | same gene group |
| [[B4GALT7]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_GLYCOLYSIS; STRING 656 |
| [[CXXC1]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A44]] | +0.58 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TMED7-TICAM2]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[YKT6]] | +0.58 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC3]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[YEATS4]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LRRCC1]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RAD21]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.8, -28.1); signed map (-50.8, 2.9). **Vector** length 87.0, 17.5% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +4.2 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.6 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.2 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.2 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.2 | -8.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Afatinib (drug)]] 0.05 µM |  | -1.7 | -0.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin polymerizing factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,232,483-151,240,979 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1402, ChSy-3, CSGlcA-T |
| Gene groups (HGNC) | Beta 4-glycosyltransferases; Beta 3-glycosyltransferases; MicroRNA protein coding host genes |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2E5](https://www.uniprot.org/uniprotkb/Q9P2E5) (Chondroitin polymerizing factor 2, non-catalytic subunit):

> Non-catalytic component of CHSY1-CHPF2 and CHSY3-CHPF2 chondroitin sulfate synthase complexes. CHPF2 associates with catalytically active chondroitin synthases (CHSY1/3) within heterodimeric complexes. Plays an essential role for the formation of a stable and functional chondroitin sulfate polymerase complexes.

**Summary**, from NCBI Gene [54480](https://www.ncbi.nlm.nih.gov/gene/54480):

> Enables N-acetylgalactosaminyl-proteoglycan 3-beta-glucuronosyltransferase activity. Involved in chondroitin sulfate proteoglycan biosynthetic process. Located in membrane. Is active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29270) · Entrez [54480](https://www.ncbi.nlm.nih.gov/gene/54480) · UniProt [Q9P2E5](https://www.uniprot.org/uniprotkb/Q9P2E5) · Ensembl [ENSG00000033100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033100)

## Data

Gene col 411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 411); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 411]; `tensor/DDL_lfc|DDL_z.npy` [411]; `embed/gene_vectors.npy` [411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 411 or target_col == 411). Every well: [[CHPF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHPF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
