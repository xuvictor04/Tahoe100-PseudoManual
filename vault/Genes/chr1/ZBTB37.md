---
symbol: "ZBTB37"
type: "gene"
col: 11654
ensembl_id: "ENSG00000185278"
name: "zinc finger and BTB domain containing 37"
location: "1q25.1"
module: 25
arm: "+"
pooled_cpm: 24.31
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ZBTB37

*zinc finger and BTB domain containing 37* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.36× (z +3.9, q 0.052, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.335× (z -13.8, q 2e-40, down in 43 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.349× (z -13.3, q 8e-38, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG10B]] (+0.67, fdr 7e-06), [[HDHD2]] (+0.64, fdr 1e-05), [[PSME3IP1]] (+0.64, fdr 1e-05); moves opposite to [[DTX2P1-UPK3BP1-PMS2P11]] (-0.61, fdr 1e-05), [[COX6C]] (-0.59, fdr 2e-05), [[UBL5]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.052 | 21/48 (A-427, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.32× | +3.3 | 0.27 | 15/46 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.0 | 0.49 | 17/48 (COLO 205, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.335×** | -13.8 | 2e-40 | 43/46 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.349×** | -13.3 | 8e-38 | 47/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.442×** | -10.3 | 2e-22 | 44/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.471×** | -9.5 | 3e-19 | 39/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.484×** | -9.2 | 6e-18 | 39/47 (PANC-1, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.575×** | -7.0 | 3e-10 | 39/47 (J82, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -6.8 | 7e-10 | 33/44 (LOX-IMVI, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.598×** | -6.5 | 7e-09 | 34/47 (J82, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -6.3 | 2e-08 | 29/47 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.612×** | -6.2 | 4e-08 | 34/48 (HS-578T, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.627×** | -5.9 | 2e-07 | 32/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.620×** | -5.8 | 3e-07 | 30/46 (C-33 A, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.723×** | -5.8 | 3e-07 | 28/47 (COLO 205, NCI-H1792, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -5.5 | 2e-06 | 31/48 (SNU-1, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.640×** | -5.3 | 4e-06 | 31/48 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.587×** | -3.5 | 0.012 | 21/45 (SNU-1, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.696×** | -3.2 | 0.040 | 15/46 (LOX-IMVI, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.839× | -3.1 | 0.045 | 18/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.791×** | -2.9 | 0.072 | 15/46 (H4, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.640×** | -2.9 | 0.072 | 19/47 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 31.7 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -15.4) |
| [[PANC-1 (line)]] | alt | 30.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.175× (z -15.5) |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 49.2 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0597× (z -12.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -11.1) |
| [[SW480 (line)]] | alt | 19.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -12.8) |
| [[HOP62 (line)]] | alt | 22.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 42.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 42.0 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -12.0) |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Allantoin (drug)]] 0.5 µM 0.183× (z -9.0) |
| [[CHP-212 (line)]] | wt | 74.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0623× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 22.1 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.0824× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0990× (z -11.1) |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0645× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.6) |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -11.1) |
| [[LoVo (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 26.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0825× (z -17.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.5) ⚠ cell-cycle shift, explains ~73% of this change |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -8.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.185× (z -9.7) |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -9.2) |
| [[A498 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10B]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.64 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[GTF2A1]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ERMARD]] | +0.62 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[PNPO]] | +0.62 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[IMPACT]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[PUS7L]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF252P]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MRPL30]] | +0.60 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[COX6C]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[UBL5]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[TRIM62]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CMTM8]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NENF]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[NDUFA4]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ATOX1]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | -0.55 | -0.55 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD9]] | -0.54 | -0.36 / -0.50 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.7, -17.0); signed map (0.7, -36.1). **Vector** length 78.6, 17.1% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.3 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +5.2 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -10.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.4 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:173,868,082-173,903,547 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2629, ZNF908 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TC79](https://www.uniprot.org/uniprotkb/Q5TC79) (Zinc finger and BTB domain-containing protein 37):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [84614](https://www.ncbi.nlm.nih.gov/gene/84614):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Predicted to be located in chromatin. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28365) · Entrez [84614](https://www.ncbi.nlm.nih.gov/gene/84614) · UniProt [Q5TC79](https://www.uniprot.org/uniprotkb/Q5TC79) · Ensembl [ENSG00000185278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185278)

## Data

Gene col 11654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11654); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11654]; `tensor/DDL_lfc|DDL_z.npy` [11654]; `embed/gene_vectors.npy` [11654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11654 or target_col == 11654). Every well: [[ZBTB37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
