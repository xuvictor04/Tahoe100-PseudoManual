---
symbol: "PRPF19"
type: "gene"
col: 3117
ensembl_id: "ENSG00000110107"
name: "pre-mRNA processing factor 19"
location: "11q12.2"
module: 4
arm: "+"
pooled_cpm: 19.61
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PRPF19

*pre-mRNA processing factor 19* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.02× (z +11.5, q 7e-28, up in 32 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.57× (z +7.4, q 9e-12, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.933× (z -3.7, q 0.068, down in 4 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.652× (z -3.7, q 0.068, down in 15 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (COLO 205 0.0946×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (H4 0.114×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFAS]] (+0.75, fdr 7e-06), [[MYBBP1A]] (+0.75, fdr 7e-06), [[MRPL3]] (+0.74, fdr 7e-06); moves opposite to [[SELENOK]] (-0.70, fdr 1e-05), [[ARID4B]] (-0.65, fdr 1e-05), [[ING2]] (-0.64, fdr 9e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.02×** | +11.5 | 7e-28 | 32/41 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.86×** | +10.2 | 8e-22 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.81×** | +9.7 | 6e-20 | 42/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.90×** | +9.7 | 6e-20 | 32/37 (A-172, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.83×** | +9.5 | 2e-19 | 21/33 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.68×** | +8.5 | 2e-15 | 36/47 (HOP62, AsPC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +7.9 | 2e-13 | 35/47 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.4 | 9e-12 | 32/47 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.57×** | +7.1 | 9e-11 | 27/44 (SW480, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +6.5 | 3e-09 | 28/48 (HT-29, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +6.0 | 9e-08 | 25/45 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.46×** | +5.9 | 1e-07 | 28/47 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.9 | 2e-07 | 24/47 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.42×** | +5.7 | 5e-07 | 24/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +5.4 | 3e-06 | 27/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 3e-06 | 25/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +5.3 | 5e-06 | 22/45 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 20/47 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.007 | 12/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.021 | 10/44 (PANC-1, BT-474, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.036 | 5/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.060 | 12/46 (A498, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.061 | 13/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (COLO 205 0.0946×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (H4 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.7 | 0.068 | 4/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.652×** | -3.7 | 0.068 | 15/46 (Hs 766T, A549, …) | top dose only | noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.877× | -3.1 | 0.40 | 15/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.89× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0946× (z -9.9) |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.114× (z -9.1) |
| [[LoVo (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.6) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFAS]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.75 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.74 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[PRPS1]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.73 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[CAD]] | +0.73 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.71 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[ELAC2]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[WDR77]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[RPE]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ATIC]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.70 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.65 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[ING2]] | -0.64 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[TESK2]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[LINC00685]] | -0.63 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.63 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[SPATC1]] | -0.62 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[NDUFC1]] | -0.62 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[TRNAU1AP]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[MSX1]] | -0.60 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[MICU1]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[STX5-DT]] | -0.59 | -0.52 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.9, -35.0); signed map (-15.5, -45.8). **Vector** length 77.2, 14.8% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8); *tRNA processing* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.6 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.4 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.4 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:60,890,547-60,906,585 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBOX4, NMP200, PSO4, hPSO4, SNEV; previously PRP19 |
| Gene groups (HGNC) | WD repeat domain containing; U-box domain containing; NineTeen complex; Spliceosomal C complex |
| Reactome | 13 pathways, smallest: Formation of TC-NER Pre-Incision Complex; Gap-filling DNA repair synthesis and ligation in TC-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMS4](https://www.uniprot.org/uniprotkb/Q9UMS4) (Pre-mRNA-processing factor 19):

> Ubiquitin-protein ligase which is a core component of several complexes mainly involved pre-mRNA splicing and DNA repair. Required for pre-mRNA splicing as component of the spliceosome. Core component of the PRP19C/Prp19 complex/NTC/Nineteen complex which is part of the spliceosome and participates in its assembly, its remodeling and is required for its activity. During assembly of the spliceosome, mediates 'Lys-63'-linked polyubiquitination of the U4 spliceosomal protein PRPF3. Ubiquitination …

**Summary**, from NCBI Gene [27339](https://www.ncbi.nlm.nih.gov/gene/27339):

> Enables identical protein binding activity and ubiquitin-ubiquitin ligase activity. Involved in several processes, including DNA damage checkpoint signaling; mRNA splicing, via spliceosome; and protein K63-linked ubiquitination. Acts upstream of or within protein polyubiquitination. Located in cytoplasm; nuclear lumen; and site of double-strand break. Part of Prp19 complex and U2-type catalytic step 2 spliceosome. Implicated in syndromic intellectual disability. [provided by Alliance of Genome …

**Accessions** — [HGNC:17896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17896) · Entrez [27339](https://www.ncbi.nlm.nih.gov/gene/27339) · UniProt [Q9UMS4](https://www.uniprot.org/uniprotkb/Q9UMS4) · Ensembl [ENSG00000110107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110107)

## Data

Gene col 3117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3117); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3117]; `tensor/DDL_lfc|DDL_z.npy` [3117]; `embed/gene_vectors.npy` [3117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3117 or target_col == 3117). Every well: [[PRPF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
