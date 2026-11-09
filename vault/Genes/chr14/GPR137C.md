---
symbol: "GPR137C"
type: "gene"
col: 11154
ensembl_id: "ENSG00000180998"
name: "G protein-coupled receptor 137C"
location: "14q22.1"
module: 26
arm: "+"
pooled_cpm: 8.07
n_lines_expressing: 48
n_dd_up: 44
n_dd_down: 3
n_dd_up_clean: 33
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# GPR137C

*G protein-coupled receptor 137C* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.92× (z +32.3, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.900× (z -4.2, q 0.019, down in 8 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pemetrexed (drug)]] 5 µM: 0.721× (z -3.7, q 0.055, down in 11 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO48]] (+0.63, fdr 1e-05), [[SGO1-AS1]] (+0.60, fdr 1e-05), [[LNC-LBCS]] (+0.59, fdr 1e-05); moves opposite to [[UBAC2]] (-0.65, fdr 1e-05), [[PIGU]] (-0.62, fdr 2e-05), [[TBC1D14]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.92×** | +32.3 | 0e+00 | 37/40 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.19×** | +23.9 | 0e+00 | 39/42 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.66×** | +22.4 | 0e+00 | 44/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.86×** | +20.9 | 0e+00 | 44/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.76×** | +20.7 | 0e+00 | 43/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.69×** | +15.4 | 0e+00 | 42/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +14.1 | 2e-43 | 30/40 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.44×** | +14.0 | 1e-42 | 37/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +13.9 | 4e-42 | 37/42 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +12.8 | 8e-36 | 33/41 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.79×** | +12.1 | 4e-32 | 35/44 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.73×** | +11.9 | 1e-30 | 35/42 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.43×** | +10.5 | 6e-24 | 17/31 (HEC-1-A, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.34×** | +9.3 | 6e-19 | 15/20 (HEC-1-A, SW480, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.48×** | +9.2 | 9e-19 | 37/44 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.8 | 2e-13 | 28/46 (NCI-H460, A498, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.1 | 3e-11 | 21/46 (BT-474, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -4.2 | 0.019 | 8/46 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 5 µM |  | **0.721×** | -3.7 | 0.055 | 11/43 (H4, hTERT-HPNE, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.556×** | -3.6 | 0.055 | 6/40 (HEC-1-A, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.750×** | -3.4 | 0.100 | 13/44 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.607× | -3.1 | 0.21 | 7/37 (SHP-77, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.764× | -3.1 | 0.21 | 2/45 (HS-578T, SNU-1) | inconsistent across doses | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.8 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.99× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 11.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +15.4) | — |
| [[A498 (line)]] | wt | 3.20 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +13.0) | — |
| [[LoVo (line)]] | wt | 3.27 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.2× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 5.96 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 35.4 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 5.56 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 5.32 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.88 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 19.7× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 4.27 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +10.1) | [[Ferulic acid (drug)]] 0.5 µM 0.0724× (z -8.7) |
| [[SW48 (line)]] | wt | 10.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 5.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +11.2) | — |
| [[J82 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 4.11 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 2.89 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 26.7× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 7.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 3.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +11.4) | — |
| [[A-172 (line)]] | wt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.1) | — |
| [[C32 (line)]] | wt | 3.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 8.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 8.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +8.8) | — |
| [[KATO III (line)]] | alt | 5.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 5.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 3.03 | 0 | 1 | — | [[Tolcapone (drug)]] 0.5 µM 0.0553× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 9.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +12.8) | — |
| [[A-427 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO48]] | +0.63 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | +0.60 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[LNC-LBCS]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[GRK4]] | +0.56 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[DPY19L2P2]] | +0.56 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[LINC01135]] | +0.55 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[UNC79]] | +0.55 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[RUNDC3B]] | +0.54 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[LYST]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[NID1]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[NPHS1]] | +0.54 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[CHODL]] | +0.54 | +0.70 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBAC2]] | -0.65 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[PIGU]] | -0.62 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[TBC1D14]] | -0.62 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[ERI3]] | -0.61 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[IQCB1]] | -0.58 | -0.60 / -0.42 | both halves | 4e-05 | STRING 415 |
| [[CDK5RAP1]] | -0.57 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[WDR3]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TTLL4]] | -0.56 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[URB1]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZNF692]] | -0.55 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[CTU1]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MRPS27]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPR137C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-8.9, -31.3); signed map (26.7, 1.2). **Vector** length 63.4, 11.2% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +32.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.1 | +10.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +3.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +7.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.1 | +3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 137C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:52,552,836-52,637,713 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762F0713, TM7SF1L2 |
| Gene groups (HGNC) | 7TM uncharacterized proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3F9](https://www.uniprot.org/uniprotkb/Q8N3F9) (Integral membrane protein GPR137C):

> Lysosomal integral membrane protein that may regulate MTORC1 complex translocation to lysosomes.

**Summary**, from NCBI Gene [283554](https://www.ncbi.nlm.nih.gov/gene/283554):

> Predicted to be involved in positive regulation of TORC1 signaling. Located in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25445) · Entrez [283554](https://www.ncbi.nlm.nih.gov/gene/283554) · UniProt [Q8N3F9](https://www.uniprot.org/uniprotkb/Q8N3F9) · Ensembl [ENSG00000180998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180998)

## Data

Gene col 11154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11154); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11154]; `tensor/DDL_lfc|DDL_z.npy` [11154]; `embed/gene_vectors.npy` [11154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11154 or target_col == 11154). Every well: [[GPR137C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR137C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
