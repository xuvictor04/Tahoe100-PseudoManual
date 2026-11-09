---
symbol: "TNFSF9"
type: "gene"
col: 4641
ensembl_id: "ENSG00000125657"
name: "TNF superfamily member 9"
location: "19p13.3"
module: 93
arm: "+"
pooled_cpm: 6.02
n_lines_expressing: 44
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# TNFSF9

*TNF superfamily member 9* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.03× (z +17.2, q 0e+00, up in 17 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.86× (z +14.9, q 0e+00, up in 26 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (Hs 766T 0.0428×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAI1]] (+0.65, fdr 7e-06), [[LGMN]] (+0.62, fdr 1e-05), [[ACHE]] (+0.56, fdr 1e-05); moves opposite to [[C1orf109]] (-0.53, fdr 4e-05), [[ORC5]] (-0.51, fdr 1e-05), [[ARMC8]] (-0.51, fdr 6e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NDRG4]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMEM132A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.03×** | +17.2 | 0e+00 | 17/19 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.86×** | +14.9 | 0e+00 | 26/32 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **5.44×** | +13.2 | 1e-37 | 38/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +12.0 | 6e-31 | 27/31 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.85×** | +11.9 | 2e-30 | 4/8 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.34×** | +11.5 | 2e-28 | 35/38 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +9.9 | 3e-21 | 34/38 (HT-29, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.51×** | +9.8 | 6e-21 | 32/38 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.49×** | +9.4 | 4e-19 | 24/36 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.02×** | +8.6 | 3e-16 | 34/38 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.95×** | +7.8 | 3e-13 | 8/13 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.65×** | +7.6 | 1e-12 | 33/38 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.48×** | +7.1 | 5e-11 | 25/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +7.0 | 7e-11 | 22/36 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +6.5 | 3e-09 | 26/37 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.37×** | +6.4 | 6e-09 | 26/37 (CFPAC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +5.0 | 2e-05 | 16/39 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 3e-04 | 14/39 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.18×** | +4.4 | 3e-04 | 14/38 (CFPAC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.0 | 0.001 | 13/34 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (Hs 766T 0.0428×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adenosine (drug)]] 0.5 µM |  | 0.673× | -3.1 | 0.70 | 7/39 (LoVo, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.03 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 15.6× (z +12.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 3.43 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +15.9) | — |
| [[A498 (line)]] | wt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +13.4) | — |
| [[C32 (line)]] | wt | 3.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 6.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 4.76 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0428× (z -9.3) |
| [[HS-578T (line)]] | alt | 3.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +9.9) | — |
| [[LoVo (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 8.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 5.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 5.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +8.8) | — |
| [[SW480 (line)]] | alt | 2.53 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.5× (z +9.3) | — |
| [[A-172 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAI1]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LGMN]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ACHE]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FBXO2]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[HSPA2]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[TMEM132A]] | +0.55 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PLEKHO2]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.53 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[PPM1N]] | +0.53 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[NEAT1]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[TM7SF2]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[RND1]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf109]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ORC5]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ARMC8]] | -0.51 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[TMEM209]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[UTP15]] | -0.50 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[SCO1]] | -0.49 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[ZBTB24]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[UMPS]] | -0.48 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[NAF1]] | -0.48 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[LTV1]] | -0.48 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[URB2]] | -0.48 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[MAPKAPK5]] | -0.47 | -0.31 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG4]] | B | NDRG4 activity lowers TNFSF9's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.83× higher at baseline in the lines without NDRG4 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM132A]] | B | TNFSF9 activity lowers TMEM132A's level | lines that do not express TNFSF9 (6) vs lines expressing it (44) | 2.27× higher at baseline in the lines without TNFSF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI1; its own permutation p |
| [[SAMD14]] | B | TNFSF9 activity lowers SAMD14's level | lines that do not express TNFSF9 (6) vs lines expressing it (44) | 2.26× higher at baseline in the lines without TNFSF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI1; its own permutation p |
| [[NOTCH3]] | B | TNFSF9 activity lowers NOTCH3's level | lines that do not express TNFSF9 (6) vs lines expressing it (44) | 3.74× higher at baseline in the lines without TNFSF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: SNAI1; its own permutation p |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, -27.5); signed map (1.6, 18.1). **Vector** length 67.9, 13.3% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +17.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.8 | +11.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +4.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF superfamily member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,531,026-6,535,924 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 4-1BB-L, 4-1BBL, CD137L |
| Gene groups (HGNC) | Tumor necrosis factor superfamily |
| Hallmark sets | INFLAMMATORY_RESPONSE, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P41273](https://www.uniprot.org/uniprotkb/P41273) (Tumor necrosis factor ligand superfamily member 9):

> Cytokine that binds to TNFRSF9. Induces the proliferation of activated peripheral blood T-cells. May have a role in activation-induced cell death (AICD). May play a role in cognate interactions between T-cells and B-cells/macrophages.

**Summary**, from NCBI Gene [8744](https://www.ncbi.nlm.nih.gov/gene/8744):

> The protein encoded by this gene is a cytokine that belongs to the tumor necrosis factor (TNF) ligand family. This transmembrane cytokine is a bidirectional signal transducer that acts as a ligand for TNFRSF9/4-1BB, which is a costimulatory receptor molecule in T lymphocytes. This cytokine and its receptor are involved in the antigen presentation process and in the generation of cytotoxic T cells. The receptor TNFRSF9/4-1BB is absent from resting T lymphocytes but rapidly expressed upon …

**Accessions** — [HGNC:11939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11939) · Entrez [8744](https://www.ncbi.nlm.nih.gov/gene/8744) · UniProt [P41273](https://www.uniprot.org/uniprotkb/P41273) · Ensembl [ENSG00000125657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125657)

## Data

Gene col 4641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4641); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4641]; `tensor/DDL_lfc|DDL_z.npy` [4641]; `embed/gene_vectors.npy` [4641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4641 or target_col == 4641). Every well: [[TNFSF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFSF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
