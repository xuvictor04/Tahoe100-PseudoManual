---
symbol: "CBR3"
type: "gene"
col: 8235
ensembl_id: "ENSG00000159231"
name: "carbonyl reductase 3"
location: "21q22.12"
module: 20
arm: "-"
pooled_cpm: 7.65
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CBR3

*carbonyl reductase 3* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +10.0, q 7e-21, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.496× (z -6.7, q 9e-09, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIX1]] (+0.56, fdr 3e-05), [[UBB]] (+0.53, fdr 2e-05), [[ING2]] (+0.53, fdr 1e-04); moves opposite to [[FAM91A1]] (-0.58, fdr 3e-05), [[SPCS3]] (-0.57, fdr 3e-05), [[MMGT1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HNRNPA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.0 | 7e-21 | 30/36 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.09×** | +7.1 | 3e-10 | 23/37 (HOP62, LoVo, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.56×** | +6.1 | 2e-07 | 18/37 (NCI-H1573, HS-578T, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +5.4 | 8e-06 | 21/39 (COLO 205, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +5.0 | 8e-05 | 20/38 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.67×** | +4.8 | 1e-04 | 15/38 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.5 | 5e-04 | 19/40 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.008 | 16/40 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +3.8 | 0.009 | 12/37 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.012 | 14/39 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.056 | 10/34 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.2 | 0.056 | 10/30 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.081 | 12/41 (HS-578T, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -6.7 | 9e-09 | 25/38 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -5.9 | 1e-06 | 20/38 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -4.9 | 2e-04 | 23/35 (C32, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.014 | 19/41 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.697×** | -3.4 | 0.064 | 12/40 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.710× | -3.3 | 0.10 | 14/38 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | 0.718× | -3.2 | 0.13 | 13/42 (Hs 766T, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0956× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0578× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 8.19 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 5.36 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0829× (z -8.9) |
| [[SW48 (line)]] | wt | 66.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.3) |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX1]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[UBB]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ING2]] | +0.53 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[PDLIM2]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[USP27X]] | +0.53 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[NEURL3]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TUBA4A]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[CAVIN3]] | +0.52 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[EAPP]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DYNLL1]] | +0.51 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[KDM2B]] | +0.51 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[LRRC37B]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM91A1]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[SPCS3]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[MMGT1]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CPSF6]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[VMA21]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[POFUT1]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[UBE2G2]] | -0.50 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[PDHA1]] | -0.50 | -0.27 / -0.53 | both halves | 3e-04 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[EIF4EBP2]] | -0.50 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[HNRNPA3]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[TXNDC5]] | -0.49 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[PABIR2]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CBR3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNRNPA3]] | B | CBR3 activity lowers HNRNPA3's level | lines that do not express CBR3 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without CBR3 | 0.089 | ⚠ within organs, on part of the lines; also absent: MYO10, CDKL5, KLF2; its own permutation p |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.8, -57.1); signed map (-0.8, 11.7). **Vector** length 73.6, 15.1% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.6 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.1 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -3.1 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -6.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | carbonyl reductase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:36,135,079-36,146,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR21C2 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O75828](https://www.uniprot.org/uniprotkb/O75828) (Carbonyl reductase):

> Catalyzes the NADPH-dependent reduction of carbonyl compounds to their corresponding alcohols. Has low NADPH-dependent oxidoreductase activity. Acts on several orthoquinones, acts as well on non-quinone compounds, such as isatin or on the anticancer drug oracin. Best substrates for CBR3 is 1,2- naphthoquinone, hence could play a role in protection against cytotoxicity of exogenous quinones. Exerts activity toward ortho-quinones but not paraquinones. No endogenous substrate for CBR3 except …

**Summary**, from NCBI Gene [874](https://www.ncbi.nlm.nih.gov/gene/874):

> Carbonyl reductase 3 catalyzes the reduction of a large number of biologically and pharmacologically active carbonyl compounds to their corresponding alcohols. The enzyme is classified as a monomeric NADPH-dependent oxidoreductase. CBR3 contains three exons spanning 11.2 kilobases and is closely linked to another carbonyl reductase gene - CBR1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1549) · Entrez [874](https://www.ncbi.nlm.nih.gov/gene/874) · UniProt [O75828](https://www.uniprot.org/uniprotkb/O75828) · Ensembl [ENSG00000159231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159231)

## Data

Gene col 8235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8235); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8235]; `tensor/DDL_lfc|DDL_z.npy` [8235]; `embed/gene_vectors.npy` [8235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8235 or target_col == 8235). Every well: [[CBR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
