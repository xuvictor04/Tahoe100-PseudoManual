---
symbol: "BAK1"
type: "gene"
col: 396
ensembl_id: "ENSG00000030110"
name: "BCL2 antagonist/killer 1"
location: "6p21.31"
module: 23
arm: "-"
pooled_cpm: 7.67
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# BAK1

*BCL2 antagonist/killer 1* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.06× (z +8.9, q 3e-16, up in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.65× (z +6.2, q 6e-08, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.784× (z -4.3, q 0.009, down in 17 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.197×, A498 0.421×); [[Dinaciclib (drug)]] 5 µM in 2 lines (AsPC-1 0.130×, NCI-H2030 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LoVo 0.131×); [[Drospirenone (drug)]] 0.5 µM in 1 line (SW1417 0.0590×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUSC2]] (+0.59, fdr 3e-05), [[USB1]] (+0.58, fdr 4e-05), [[SPRYD3]] (+0.58, fdr 3e-05); moves opposite to [[ATRX]] (-0.58, fdr 1e-05), [[CYB5D2]] (-0.56, fdr 4e-05), [[ACADM]] (-0.53, fdr 6e-05).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.06×** | +8.9 | 3e-16 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.88×** | +7.8 | 2e-12 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.88×** | +7.7 | 2e-12 | 26/46 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +6.9 | 9e-10 | 21/37 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.70×** | +6.3 | 3e-08 | 18/33 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +6.2 | 6e-08 | 24/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +5.9 | 2e-07 | 18/43 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.58×** | +5.6 | 2e-06 | 16/40 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.6 | 2e-06 | 17/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.2 | 1e-05 | 14/45 (SW480, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.7 | 1e-04 | 16/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 3e-04 | 13/44 (A-427, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 7e-04 | 12/41 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +4.1 | 0.002 | 7/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 11/46 (A-172, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.009 | 9/43 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.019 | 9/46 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.030 | 2/44 (HOP62, SW48) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.054 | 9/48 (A-172, MIA PaCa-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 396.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.197×, A498 0.421×); [[Dinaciclib (drug)]] 5 µM in 2 lines (AsPC-1 0.130×, NCI-H2030 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (LoVo 0.131×); [[Drospirenone (drug)]] 0.5 µM in 1 line (SW1417 0.0590×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.784×** | -4.3 | 0.009 | 17/40 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.823× | -3.0 | 0.70 | 11/44 (BT-474, RKO, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.6) |
| [[HS-578T (line)]] | alt | 7.12 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.144× (z -8.5) |
| [[LoVo (line)]] | wt | 7.58 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.131× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 7.58 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.109× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 4.55 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.05 µM 0.0760× (z -8.7) |
| [[SW 900 (line)]] | alt | 5.59 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0741× (z -8.8) |
| [[SW1417 (line)]] | alt | 3.69 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0590× (z -9.8) |
| [[A-172 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUSC2]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[USB1]] | +0.58 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[SPRYD3]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ELOVL1]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SIPA1]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[CIB1]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ZNRD2]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[AP1S1]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[TRIM11]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[MKRN2]] | +0.52 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PI4K2A]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRX]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CYB5D2]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ACADM]] | -0.53 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[NUCKS1]] | -0.53 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ENOSF1]] | -0.53 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[PCM1]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RBMX]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[RBM3]] | -0.52 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[HP1BP3]] | -0.51 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[GABPB2]] | -0.51 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[THOC7]] | -0.50 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[ANKRD26]] | -0.49 | -0.60 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (14.2, -0.9); signed map (-40.0, 15.1). **Vector** length 71.5, 12.1% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.9 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.8 | +8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.6 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 antagonist/killer 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:33,572,547-33,580,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCL2L7, BAK; previously CDN1 |
| Gene groups (HGNC) | BCL2 family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, UV_RESPONSE_UP, P53_PATHWAY |
| Reactome | 7 pathways, smallest: Release of apoptotic factors from the mitochondria; Apoptotic factor-mediated response; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16611](https://www.uniprot.org/uniprotkb/Q16611) (Bcl-2 homologous antagonist/killer):

> Plays a role in the mitochondrial apoptotic process. Upon arrival of cell death signals, promotes mitochondrial outer membrane (MOM) permeabilization by oligomerizing to form pores within the MOM. This releases apoptogenic factors into the cytosol, including cytochrome c, promoting the activation of caspase 9 which in turn processes and activates the effector caspases.

**Summary**, from NCBI Gene [578](https://www.ncbi.nlm.nih.gov/gene/578):

> The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form oligomers or heterodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. This protein localizes to mitochondria, and functions to induce apoptosis. It interacts with and accelerates the opening of the mitochondrial voltage-dependent anion channel, which leads to a loss in membrane potential and the release of cytochrome c. This protein also …

**Accessions** — [HGNC:949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:949) · Entrez [578](https://www.ncbi.nlm.nih.gov/gene/578) · UniProt [Q16611](https://www.uniprot.org/uniprotkb/Q16611) · Ensembl [ENSG00000030110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000030110)

## Data

Gene col 396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 396); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 396]; `tensor/DDL_lfc|DDL_z.npy` [396]; `embed/gene_vectors.npy` [396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 396 or target_col == 396). Every well: [[BAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
