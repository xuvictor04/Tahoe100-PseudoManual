---
symbol: "SEMA4C"
type: "gene"
col: 9691
ensembl_id: "ENSG00000168758"
name: "semaphorin 4C"
location: "2q11.2"
module: 29
arm: "-"
pooled_cpm: 10.92
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SEMA4C

*semaphorin 4C* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 2.19× (z +5.2, q 9e-05, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.239× (z -15.6, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2B]] (+0.65, fdr 7e-06), [[TBX2]] (+0.63, fdr 9e-06), [[ZCCHC3]] (+0.62, fdr 3e-05); moves opposite to [[TMED7]] (-0.63, fdr 5e-05), [[DSG2]] (-0.57, fdr 2e-05), [[PGAM1]] (-0.55, fdr 6e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.19×** | +5.2 | 9e-05 | 26/41 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +4.4 | 0.003 | 17/40 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.82×** | +4.0 | 0.012 | 13/43 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.78×** | +3.9 | 0.016 | 12/43 (C32, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 1.23× | +3.2 | 0.13 | 7/46 (SHP-77, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.33× | +3.2 | 0.14 | 15/44 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.59× | +3.1 | 0.14 | 11/42 (NCI-H23, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.58× | +3.1 | 0.14 | 9/40 (NCI-H1792, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.57× | +3.0 | 0.14 | 7/43 (NCI-H460, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.0 | 0.14 | 8/45 (NCI-H460, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.239×** | -15.6 | 0e+00 | 44/45 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.242×** | -15.5 | 0e+00 | 44/45 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.294×** | -13.4 | 2e-38 | 42/45 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.521×** | -7.1 | 2e-10 | 31/45 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.391×** | -5.0 | 7e-05 | 23/46 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.643×** | -4.6 | 4e-04 | 20/45 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.744×** | -4.6 | 4e-04 | 23/46 (C32, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.609×** | -4.5 | 5e-04 | 15/25 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -4.4 | 5e-04 | 20/44 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.669×** | -4.4 | 7e-04 | 17/45 (LS 180, SW 900, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.684×** | -4.0 | 0.004 | 14/44 (RKO, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -3.9 | 0.004 | 20/45 (Panc 03.27, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -3.7 | 0.011 | 15/45 (A498, PANC-1, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -3.6 | 0.014 | 16/42 (LS 180, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.724×** | -3.5 | 0.016 | 15/33 (MIA PaCa-2, SW 900, …) | inconsistent across doses | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.680×** | -3.5 | 0.019 | 17/45 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.704×** | -3.2 | 0.054 | 15/45 (HOP62, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -3.1 | 0.062 | 10/46 (NCI-H1792, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 17.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -11.9) |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -10.1) |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.150× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0956× (z -13.3) |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0797× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.148× (z -9.5) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -11.6) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 6.94 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -9.5) |
| [[PANC-1 (line)]] | alt | 9.96 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.52× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0854× (z -10.7) |
| [[SNU-423 (line)]] | alt | 7.91 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0796× (z -9.7) |
| [[A-427 (line)]] | wt | 7.66 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -9.0) |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0965× (z -9.4) |
| [[C32 (line)]] | wt | 16.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -8.6) |
| [[H4 (line)]] | wt | 13.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0879× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.229× (z -8.5) |
| [[LoVo (line)]] | wt | 5.96 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -8.6) |
| [[RKO (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2B]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TBX2]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[ZCCHC3]] | +0.62 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[FBXL6]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LIME1]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ARRDC2]] | +0.61 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ZNF316]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[EGLN2]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SIX5]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ARMC5]] | +0.59 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[ZBTB7A]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[TLE3]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED7]] | -0.63 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[DSG2]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PGAM1]] | -0.55 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[FAM91A1]] | -0.54 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[TWF1]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[OPA1]] | -0.53 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ACP1]] | -0.53 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[DPM2]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ADAM9]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[CYB5R4]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[TMEM30A]] | -0.52 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[TMX1]] | -0.51 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-32.4, 19.2); signed map (1.8, -10.8). **Vector** length 72.6, 14.5% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.7 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,859,718-96,870,757 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Semacl1, Semaf; previously SEMAI |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Semaphorins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0C4](https://www.uniprot.org/uniprotkb/Q9C0C4) (Semaphorin-4C):

> Cell surface receptor for PLXNB2 that plays an important role in cell-cell signaling. PLXNB2 binding promotes downstream activation of RHOA and phosphorylation of ERBB2 at 'Tyr-1248'. Required for normal brain development, axon guidance and cell migration (By similarity). Probable signaling receptor which may play a role in myogenic differentiation through activation of the stress-activated MAPK cascade.

**Summary**, from NCBI Gene [54910](https://www.ncbi.nlm.nih.gov/gene/54910):

> Predicted to enable chemorepellent activity; neuropilin binding activity; and semaphorin receptor binding activity. Involved in muscle cell differentiation and positive regulation of stress-activated MAPK cascade. Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10731) · Entrez [54910](https://www.ncbi.nlm.nih.gov/gene/54910) · UniProt [Q9C0C4](https://www.uniprot.org/uniprotkb/Q9C0C4) · Ensembl [ENSG00000168758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168758)

## Data

Gene col 9691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9691); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9691]; `tensor/DDL_lfc|DDL_z.npy` [9691]; `embed/gene_vectors.npy` [9691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9691 or target_col == 9691). Every well: [[SEMA4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
