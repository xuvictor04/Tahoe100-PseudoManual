---
symbol: "TMEM18"
type: "gene"
col: 7511
ensembl_id: "ENSG00000151353"
name: "transmembrane protein 18"
location: "2p25.3"
module: 51
arm: "+"
pooled_cpm: 16.48
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TMEM18

*transmembrane protein 18* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.52× (z +5.9, q 2e-06, up in 22 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Carbamazepine (drug)]] 5 µM: 1.28× (z +3.5, q 0.076, up in 9 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.480× (z -10.3, q 3e-22, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2]] (+0.60, fdr 1e-05), [[INO80]] (+0.58, fdr 1e-05), [[LANCL2]] (+0.58, fdr 1e-05); moves opposite to [[FKBP1A]] (-0.49, fdr 8e-05), [[MXRA7]] (-0.49, fdr 5e-05), [[TMEM87B]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.9 | 2e-06 | 22/39 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.48×** | +5.6 | 6e-06 | 24/41 (NCI-H2347, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.076 | 9/46 (SW1417, PANC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.076 | 9/47 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.11 | 0/47 | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | 1.62× | +3.1 | 0.16 | 5/43 (NCI-H1573, A549, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.57× | +3.0 | 0.18 | 7/43 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7511.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.480×** | -10.3 | 3e-22 | 42/46 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.513×** | -9.4 | 2e-18 | 42/47 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.529×** | -9.0 | 6e-17 | 33/45 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.570×** | -7.9 | 4e-13 | 39/47 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.583×** | -7.6 | 4e-12 | 39/47 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -6.3 | 3e-08 | 28/46 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.734×** | -6.1 | 7e-08 | 28/47 (J82, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.687×** | -5.3 | 1e-05 | 22/47 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.690×** | -5.2 | 1e-05 | 20/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.495×** | -4.5 | 3e-04 | 23/47 (SNU-1, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.007 | 17/46 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.761×** | -3.7 | 0.010 | 16/46 (J82, NCI-H661, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -3.7 | 0.010 | 17/45 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.773×** | -3.6 | 0.013 | 19/45 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.013 | 16/45 (MIA PaCa-2, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -3.5 | 0.017 | 19/46 (SW480, HCT15, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.795×** | -3.2 | 0.041 | 13/46 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.802×** | -3.1 | 0.062 | 11/46 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.145× (z -11.7) |
| [[A-427 (line)]] | wt | 29.1 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.315× (z -12.9) |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.8) |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[LoVo (line)]] | wt | 18.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.244× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0733× (z -8.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.155× (z -9.3) |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[INO80]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LANCL2]] | +0.58 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[HMGXB4]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[THG1L]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TPGS1]] | +0.53 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[EPC2]] | +0.52 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[RBM10]] | +0.52 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[MCRS1]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[MRPL38]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[ING3]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[YJU2]] | +0.49 | +0.47 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP1A]] | -0.49 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[MXRA7]] | -0.49 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TMEM87B]] | -0.49 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[PTBP3]] | -0.48 | -0.53 / -0.43 | both halves | 4e-05 |  |
| [[GLUD1]] | -0.45 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[LAPTM4A]] | -0.44 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[NDFIP1]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[C12orf75]] | -0.43 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TMEM30A]] | -0.42 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[ITM2C]] | -0.42 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[ATP6AP2]] | -0.42 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[GDPGP1]] | -0.41 | -0.40 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.3, 12.3); signed map (12.6, -31.3). **Vector** length 58.7, 9.40% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.7 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.9 | -6.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:663,877-677,406 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434C1714, lncND |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B42](https://www.uniprot.org/uniprotkb/Q96B42) (Transmembrane protein 18):

> Transcription repressor. Sequence-specific ssDNA and dsDNA binding protein, with preference for GCT end CTG repeats. Cell migration modulator which enhances the glioma-specific migration ability of neural stem cells (NSC) and neural precursor cells (NPC).

**Summary**, from NCBI Gene [129787](https://www.ncbi.nlm.nih.gov/gene/129787):

> Predicted to enable DNA binding activity. Involved in cell migration. Located in nuclear membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25257) · Entrez [129787](https://www.ncbi.nlm.nih.gov/gene/129787) · UniProt [Q96B42](https://www.uniprot.org/uniprotkb/Q96B42) · Ensembl [ENSG00000151353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151353)

## Data

Gene col 7511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7511); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7511]; `tensor/DDL_lfc|DDL_z.npy` [7511]; `embed/gene_vectors.npy` [7511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7511 or target_col == 7511). Every well: [[TMEM18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
