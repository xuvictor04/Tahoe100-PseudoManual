---
symbol: "SNRPD1"
type: "gene"
col: 9412
ensembl_id: "ENSG00000167088"
name: "small nuclear ribonucleoprotein D1 polypeptide"
location: "18q11.2"
module: 4
arm: "+"
pooled_cpm: 43.77
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SNRPD1

*small nuclear ribonucleoprotein D1 polypeptide* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.54× (z +8.9, q 4e-16, up in 37 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.30× (z +8.3, q 2e-14, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.629× (z -4.2, q 0.013, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.749× (z -4.0, q 0.013, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COA1]] (+0.79, fdr 7e-06), [[SNRPE]] (+0.77, fdr 7e-06), [[EXOSC2]] (+0.72, fdr 7e-06); moves opposite to [[YPEL5]] (-0.70, fdr 7e-06), [[OSER1-DT]] (-0.63, fdr 1e-05), [[OPTN]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.54×** | +8.9 | 4e-16 | 37/40 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.37×** | +8.5 | 4e-15 | 39/45 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.30×** | +8.3 | 2e-14 | 48/48 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.12×** | +7.4 | 2e-11 | 41/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.88×** | +5.8 | 8e-07 | 38/45 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.82×** | +5.2 | 2e-05 | 35/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.60×** | +4.7 | 3e-04 | 34/46 (BT-474, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +4.6 | 3e-04 | 33/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.6 | 3e-04 | 31/46 (C32, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.003 | 36/48 (HOP62, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.003 | 35/47 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.03×** | +4.0 | 0.004 | 34/48 (HOP62, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **2.20×** | +3.9 | 0.004 | 34/46 (HOP62, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.47×** | +3.9 | 0.005 | 26/48 (NCI-H1792, C32, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +3.6 | 0.011 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.045 | 22/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.045 | 25/47 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.054 | 23/47 (A498, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.069 | 22/48 (NCI-H1792, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.629×** | -4.2 | 0.013 | 33/48 (LoVo, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -4.0 | 0.013 | 26/48 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.659×** | -3.9 | 0.013 | 27/47 (NCI-H23, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.748×** | -3.9 | 0.013 | 31/48 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.471×** | -3.7 | 0.023 | 30/48 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.687×** | -3.4 | 0.064 | 29/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.535× | -3.1 | 0.16 | 21/48 (LoVo, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.4 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.07× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[A-172 (line)]] | wt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[A-427 (line)]] | wt | 76.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.8) |
| [[A549 (line)]] | wt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[HEC-1-A (line)]] | alt | 54.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[NCI-H1792 (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[HT-29 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[KATO III (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[RKO (line)]] | wt | 82.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -13.0) |
| [[SNU-1 (line)]] | wt | 45.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[A498 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA1]] | +0.79 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[SNRPE]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[EXOSC2]] | +0.72 | +0.71 / +0.74 | both halves | 7e-06 | STRING 425 |
| [[URB2]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LCLAT1]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[NOL10]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CSTF2]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 590 |
| [[CLYBL]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PDSS1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.70 | -0.67 / -0.67 | both halves | 7e-06 |  |
| [[OSER1-DT]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[OPTN]] | -0.61 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[MAP1LC3B]] | -0.59 | -0.54 / -0.64 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[ATOSA]] | -0.58 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ERO1B]] | -0.57 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[WBP1]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.57 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ADCY10]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[HLA-E]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.6, -42.2); signed map (-9.6, -48.6). **Vector** length 89.3, 29.6% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -4.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.5 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein D1 polypeptide |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:21,612,314-21,633,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT2456, Sm-D1; previously SNRPD |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 20 pathways, smallest: SARS-CoV-2 modulates host translation machinery; mRNA Splicing - Minor Pathway; Metabolism of non-coding RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P62314](https://www.uniprot.org/uniprotkb/P62314) (Small nuclear ribonucleoprotein Sm D1):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. May act as a charged protein scaffold to promote snRNP assembly or strengthen snRNP-snRNP interactions through non-specific …

**Summary**, from NCBI Gene [6632](https://www.ncbi.nlm.nih.gov/gene/6632):

> This gene encodes a small nuclear ribonucleoprotein that belongs to the SNRNP core protein family. The protein may act as a charged protein scaffold to promote SNRNP assembly or strengthen SNRNP-SNRNP interactions through nonspecific electrostatic contacts with RNA. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:11158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11158) · Entrez [6632](https://www.ncbi.nlm.nih.gov/gene/6632) · UniProt [P62314](https://www.uniprot.org/uniprotkb/P62314) · Ensembl [ENSG00000167088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167088)

## Data

Gene col 9412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9412); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9412]; `tensor/DDL_lfc|DDL_z.npy` [9412]; `embed/gene_vectors.npy` [9412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9412 or target_col == 9412). Every well: [[SNRPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
