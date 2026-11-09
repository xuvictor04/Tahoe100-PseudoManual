---
symbol: "DPM2"
type: "gene"
col: 5936
ensembl_id: "ENSG00000136908"
name: "dolichyl-phosphate mannosyltransferase subunit 2, regulatory"
location: "9q34.11"
module: 20
arm: "+"
pooled_cpm: 13.97
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DPM2

*dolichyl-phosphate mannosyltransferase subunit 2, regulatory* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.02× (z +11.3, q 1e-26, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.47× (z +6.2, q 5e-08, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.913× (z -4.9, q 6e-04, down in 8 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.704× (z -4.0, q 0.011, down in 15 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPS1]] (+0.70, fdr 1e-05), [[MLX]] (+0.61, fdr 1e-05), [[BLTP2]] (+0.60, fdr 3e-05); moves opposite to [[TERF2IP]] (-0.65, fdr 8e-06), [[YTHDC1]] (-0.59, fdr 2e-05), [[WBP4]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.02×** | +11.3 | 1e-26 | 37/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.87×** | +10.0 | 5e-21 | 28/36 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.84×** | +9.8 | 3e-20 | 39/47 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.76×** | +8.7 | 6e-16 | 17/27 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.71×** | +8.6 | 1e-15 | 34/47 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.63×** | +7.3 | 4e-11 | 18/32 (SW480, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 5e-08 | 23/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.49×** | +6.1 | 7e-08 | 20/41 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.9 | 2e-07 | 21/47 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +5.4 | 4e-06 | 17/47 (NCI-H2030, NCI-H460, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +5.1 | 2e-05 | 18/43 (A-172, A498, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.1 | 2e-05 | 19/47 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.37×** | +5.0 | 2e-05 | 15/47 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.27×** | +3.9 | 0.004 | 13/47 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.7 | 0.009 | 15/43 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.011 | 6/47 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.024 | 8/44 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -4.9 | 6e-04 | 8/48 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -4.5 | 0.002 | 19/46 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.704×** | -4.0 | 0.011 | 15/41 (LoVo, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.842× | -3.9 | 0.013 | 19/46 (PANC-1, SHP-77, …) | top dose only | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.633×** | -3.8 | 0.014 | 10/43 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.638×** | -3.8 | 0.016 | 12/43 (LOX-IMVI, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 0.871× | -3.1 | 0.13 | 11/45 (AN3 CA, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.691× | -3.1 | 0.14 | 18/47 (RKO, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 15.8 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.165× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.112× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.47× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.1) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPS1]] | +0.70 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MLX]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.60 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[G6PD]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TMED7]] | +0.59 | +0.53 / +0.47 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[TTLL12]] | +0.57 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | +0.57 | +0.51 / +0.41 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation; STRING 444; ⚠ same locus (18.1 kb, same strand: neighbours can correlate without regulation) |
| [[RPE]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SIGMAR1]] | +0.56 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[PHB1]] | +0.56 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[MAPKAPK3]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TALDO1]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 | pathway: Diseases of metabolism |
| [[PSMG1]] | +0.55 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.65 | -0.57 / -0.60 | both halves | 8e-06 |  |
| [[YTHDC1]] | -0.59 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[WBP4]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[HNRNPH1]] | -0.59 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[PABPN1]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[UNK]] | -0.56 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[RSF1]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[PNISR]] | -0.56 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[CHKB]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SRSF11]] ⚠ | -0.55 | -0.52 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TNRC6C]] | -0.54 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[C1orf56]] | -0.54 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.447). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.1, -31.5); signed map (-27.0, -43.8). **Vector** length 64.0, 9.95% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +2.6 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +2.5 | +7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.8 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | dolichyl-phosphate mannosyltransferase subunit 2, regulatory |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,935,099-127,937,854 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21559, MGC111193 |
| Gene groups (HGNC) | Dolichyl-phosphate mannosyltransferase subunits; Glycosylphosphatidylinositol-N-acetylglucosaminyltransferase complex |
| Reactome | 16 pathways, smallest: Defective DPM1 causes DPM1-CDG; Defective DPM2 causes DPM2-CDG; Defective DPM3 causes DPM3-CDG |
| Matched by | ensembl_id |

**Function**, from UniProt [O94777](https://www.uniprot.org/uniprotkb/O94777) (Dolichol phosphate-mannose biosynthesis regulatory protein):

> Regulates the biosynthesis of dolichol phosphate-mannose. Regulatory subunit of the dolichol-phosphate mannose (DPM) synthase complex; essential for the ER localization and stable expression of DPM1. Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis. May act by regulating the GPI-GNT complex.

**Summary**, from NCBI Gene [8818](https://www.ncbi.nlm.nih.gov/gene/8818):

> Dolichol-phosphate mannose (Dol-P-Man) serves as a donor of mannosyl residues on the lumenal side of the endoplasmic reticulum (ER). Lack of Dol-P-Man results in defective surface expression of GPI-anchored proteins. Dol-P-Man is synthesized from GDP-mannose and dolichol-phosphate on the cytosolic side of the ER by the enzyme dolichyl-phosphate mannosyltransferase. The protein encoded by this gene is a hydrophobic protein that contains 2 predicted transmembrane domains and a putative ER …

**Accessions** — [HGNC:3006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3006) · Entrez [8818](https://www.ncbi.nlm.nih.gov/gene/8818) · UniProt [O94777](https://www.uniprot.org/uniprotkb/O94777) · Ensembl [ENSG00000136908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136908)

## Data

Gene col 5936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5936); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5936]; `tensor/DDL_lfc|DDL_z.npy` [5936]; `embed/gene_vectors.npy` [5936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5936 or target_col == 5936). Every well: [[DPM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
