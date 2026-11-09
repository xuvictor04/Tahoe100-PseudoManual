---
symbol: "CISD2"
type: "gene"
col: 6980
ensembl_id: "ENSG00000145354"
name: "CDGSH iron sulfur domain 2"
location: "4q24"
module: 29
arm: "+"
pooled_cpm: 29.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CISD2

*CDGSH iron sulfur domain 2* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +11.9, q 4e-30, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.32× (z +5.8, q 7e-07, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.823× (z -9.8, q 7e-20, down in 33 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.661× (z -6.0, q 4e-07, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.298×, HT-29 0.483×, SNU-1 0.312×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.114×; ⚠ cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (C-33 A 0.0980×; ⚠ toxic); [[Artemether (drug)]] 0.5 µM in 1 line (AN3 CA 0.0729×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM106B]] (+0.59, fdr 3e-05), [[NT5DC1]] (+0.57, fdr 1e-05), [[PREPL]] (+0.56, fdr 1e-05); moves opposite to [[DMPK]] (-0.61, fdr 1e-05), [[ZNF324]] (-0.58, fdr 3e-05), [[MLXIP]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +11.9 | 4e-30 | 41/44 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +11.1 | 6e-26 | 35/37 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +8.0 | 3e-13 | 30/41 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.8 | 1e-09 | 29/44 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.8 | 7e-07 | 28/48 (PANC-1, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.9 | 7e-05 | 31/48 (A-172, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.002 | 22/48 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.003 | 19/48 (HS-578T, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.019 | 14/48 (A-172, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.26×** | +3.4 | 0.036 | 19/46 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.039 | 15/48 (PANC-1, HepG2/C3A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.071 | 8/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6980.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.298×, HT-29 0.483×, SNU-1 0.312×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.114×; ⚠ cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (C-33 A 0.0980×; ⚠ toxic); [[Artemether (drug)]] 0.5 µM in 1 line (AN3 CA 0.0729×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.823×** | -9.8 | 7e-20 | 33/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.661×** | -6.0 | 4e-07 | 34/47 (HEC-1-A, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.801× | -3.2 | 0.23 | 15/48 (RPMI-7951, A-172, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.808× | -3.0 | 0.38 | 15/48 (SW 1088, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 23.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0729× (z -8.9) |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0980× (z -9.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106B]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[NT5DC1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PREPL]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[STRADB]] | +0.56 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[MANEA]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[FBXO7]] | +0.54 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TMEM237]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SLC35G1]] | +0.53 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[SLC35A5]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TSNAX]] | +0.53 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[LRRC58]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMPK]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MLXIP]] | -0.58 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[FBXL18]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SAP30BP]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PCSK7]] | -0.57 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[CHMP1A]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PPRC1]] | -0.54 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ZNF276]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[RAB35]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.52 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ZNF787]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.9, -13.5); signed map (-15.0, -40.3). **Vector** length 79.6, 16.8% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CDGSH iron sulfur domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:102,868,974-102,892,807 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Miner1, ERIS, NAF-1; previously ZCD2, WFS2 |
| Gene groups (HGNC) | CDGSH iron sulfur domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5K1](https://www.uniprot.org/uniprotkb/Q8N5K1) (CDGSH iron-sulfur domain-containing protein 2):

> Regulator of autophagy that contributes to antagonize BECN1-mediated cellular autophagy at the endoplasmic reticulum. Participates in the interaction of BCL2 with BECN1 and is required for BCL2-mediated depression of endoplasmic reticulum Ca(2+) stores during autophagy. Contributes to BIK-initiated autophagy, while it is not involved in BIK-dependent activation of caspases. Involved in life span control, probably via its function as regulator of autophagy.

**Summary**, from NCBI Gene [493856](https://www.ncbi.nlm.nih.gov/gene/493856):

> The protein encoded by this gene is a zinc finger protein that localizes to the endoplasmic reticulum. The encoded protein binds an iron/sulfur cluster and may be involved in calcium homeostasis. Defects in this gene are a cause of Wolfram syndrome 2. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:24212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24212) · Entrez [493856](https://www.ncbi.nlm.nih.gov/gene/493856) · UniProt [Q8N5K1](https://www.uniprot.org/uniprotkb/Q8N5K1) · Ensembl [ENSG00000145354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145354)

## Data

Gene col 6980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6980); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6980]; `tensor/DDL_lfc|DDL_z.npy` [6980]; `embed/gene_vectors.npy` [6980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6980 or target_col == 6980). Every well: [[CISD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CISD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
