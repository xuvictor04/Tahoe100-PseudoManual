---
symbol: "ASAH2B"
type: "gene"
col: 12819
ensembl_id: "ENSG00000204147"
name: "N-acylsphingosine amidohydrolase 2B"
location: "10q11.23"
module: 1
arm: "+"
pooled_cpm: 7.3
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ASAH2B

*N-acylsphingosine amidohydrolase 2B* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.66× (z +6.2, q 3e-07, up in 7 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 1.65× (z +6.1, q 3e-07, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.379× (z -12.5, q 5e-33, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYM1]] (+0.61, fdr 1e-05), [[LINC00467]] (+0.59, fdr 2e-05), [[PPIL1]] (+0.59, fdr 1e-05); moves opposite to [[GNB2]] (-0.56, fdr 1e-04), [[VAT1]] (-0.56, fdr 2e-05), [[ULK1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.2 | 3e-07 | 7/14 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.65×** | +6.1 | 3e-07 | 19/45 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.0 | 4e-07 | 18/47 (NCI-H460, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 3e-04 | 13/41 (NCI-H2347, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.6 | 6e-04 | 11/28 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.002 | 9/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +4.3 | 0.002 | 15/42 (A-172, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.8 | 0.009 | 11/46 (HEC-1-A, A-172, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.037 | 1/35 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.046 | 13/45 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.084 | 9/45 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -12.5 | 5e-33 | 38/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -8.7 | 6e-16 | 30/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.570×** | -7.2 | 9e-11 | 23/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -6.7 | 4e-09 | 24/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.627×** | -6.0 | 2e-07 | 20/46 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -5.4 | 7e-06 | 20/37 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -4.7 | 2e-04 | 16/45 (SW480, LoVo, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.715×** | -4.3 | 0.001 | 13/46 (C-33 A, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.763×** | -3.5 | 0.032 | 16/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -3.4 | 0.045 | 15/44 (H4, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.616×** | -3.3 | 0.059 | 9/38 (SHP-77, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.778×** | -3.2 | 0.060 | 15/43 (SW1417, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.796×** | -3.1 | 0.076 | 12/47 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.62 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -13.2) |
| [[PANC-1 (line)]] | alt | 5.63 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.180× (z -9.9) |
| [[SW480 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -9.0) |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.167× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 3.48 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0612× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 7.75 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.109× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYM1]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[LINC00467]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PPIL1]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MAK16]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[HSD17B2-AS1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CHAMP1]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[SCO1]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZNF195]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[ZNF620]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[ZNF239]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[AGAP13P]] | +0.54 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[MFAP3]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB2]] | -0.56 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[VAT1]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ULK1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CBFA2T2]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RTN3]] | -0.54 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[PSAP]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R12B]] | -0.53 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[MICU1]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[KIF13A]] | -0.53 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[RFX2]] | -0.52 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[FBXL20]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[NPC2]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.8, -35.4); signed map (0.6, -43.5). **Vector** length 62.9, 9.04% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -12.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | N-acylsphingosine amidohydrolase 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:50,739,318-50,816,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA449O16.3, ASAH2L, bA98I6.3; previously ASAH2C |
| Matched by | ensembl_id |

UniProt [P0C7U1](https://www.uniprot.org/uniprotkb/P0C7U1) carries no function annotation.

**Summary**, from NCBI Gene [653308](https://www.ncbi.nlm.nih.gov/gene/653308):

> Predicted to enable N-acylsphingosine amidohydrolase activity. Predicted to be involved in ceramide biosynthetic process; ceramide catabolic process; and sphingosine biosynthetic process. Predicted to be located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23456) · Entrez [653308](https://www.ncbi.nlm.nih.gov/gene/653308) · UniProt [P0C7U1](https://www.uniprot.org/uniprotkb/P0C7U1) · Ensembl [ENSG00000204147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204147)

## Data

Gene col 12819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12819); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12819]; `tensor/DDL_lfc|DDL_z.npy` [12819]; `embed/gene_vectors.npy` [12819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12819 or target_col == 12819). Every well: [[ASAH2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASAH2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
