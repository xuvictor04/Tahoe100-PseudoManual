---
symbol: "ATP6V0C"
type: "gene"
col: 11747
ensembl_id: "ENSG00000185883"
name: "ATPase H+ transporting V0 subunit c"
location: "16p13.3"
module: 59
arm: "+"
pooled_cpm: 53.74
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ATP6V0C

*ATPase H+ transporting V0 subunit c* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (19 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.42× (z +10.7, q 6e-24, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.03× (z +6.2, q 5e-08, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD63]] (+0.68, fdr 7e-06), [[NEU1]] (+0.65, fdr 1e-05), [[DAZAP2]] (+0.64, fdr 7e-06); moves opposite to [[NSUN2]] (-0.60, fdr 1e-05), [[MCMBP]] (-0.58, fdr 2e-05), [[TRAP1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 20 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.42×** | +10.7 | 6e-24 | 48/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.26×** | +10.3 | 2e-22 | 45/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.86×** | +8.8 | 3e-16 | 38/41 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.69×** | +8.6 | 9e-16 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.84×** | +7.5 | 8e-12 | 41/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +7.2 | 4e-11 | 43/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.11×** | +6.5 | 6e-09 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +6.2 | 5e-08 | 45/48 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.14×** | +6.1 | 6e-08 | 37/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.90×** | +5.6 | 1e-06 | 43/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-05 | 38/48 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.75×** | +4.8 | 6e-05 | 41/48 (SW480, A549, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.67×** | +4.3 | 8e-04 | 35/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +4.2 | 1e-03 | 35/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.60×** | +4.1 | 0.002 | 36/48 (SW480, A549, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.033 | 29/48 (A-172, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.080 | 22/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.083 | 26/48 (SK-MEL-2, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11747.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.701× | -3.0 | 0.76 | 26/48 (SNU-423, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.6 | 10 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +14.6) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[SW480 (line)]] | alt | 39.3 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.99× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 28.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1573 (line)]] | alt | 78.8 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.93× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 49.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A549 (line)]] | wt | 30.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[C32 (line)]] | wt | 49.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[COLO 205 (line)]] | alt | 58.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[HEC-1-A (line)]] | alt | 42.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 65.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A498 (line)]] | wt | 80.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 52.4 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.06× (z +10.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-427 (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[BT-474 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.77× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[J82 (line)]] | alt | 67.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 78.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +9.2) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.6) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[LS 180 (line)]] | wt | 73.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.2) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[NCI-H23 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.14× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 59.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.62× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 80.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.11× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 67.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.37× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD63]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[NEU1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[DAZAP2]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TP53INP2]] | +0.61 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[RFX1]] | +0.58 | +0.70 / +0.36 | both halves | 1e-04 |  |
| [[EIF1B]] | +0.57 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[MICU1]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MYL6]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RRAGC-DT]] | +0.56 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[GABARAP]] ⚠ | +0.55 | +0.48 / +0.57 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GNG5]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[NPC2]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ATP6V1G1]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 996 |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN2]] | -0.60 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[MCMBP]] | -0.58 | -0.62 / -0.49 | both halves | 2e-05 |  |
| [[TRAP1]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[UCHL5]] | -0.57 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PAICS]] | -0.57 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[RPIA]] | -0.56 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[PRIM1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[NUP205]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[WDR3]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[TUBGCP3]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[GMPS]] | -0.54 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TRIM27]] | -0.54 | -0.57 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.4, -46.9); signed map (-8.9, 7.6). **Vector** length 67.7, 22.2% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.6 | +8.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.1 | +10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.2 | +7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.8 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | -0.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.4 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | -1.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.0 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit c |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,513,952-2,520,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VATL, Vma3; previously ATPL, ATP6C, ATP6L |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 17 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P27449](https://www.uniprot.org/uniprotkb/P27449) (V-type proton ATPase 16 kDa proteolipid subunit c):

> Proton-conducting pore forming subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments, and in some cell types, it is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also …

**Summary**, from NCBI Gene [527](https://www.ncbi.nlm.nih.gov/gene/527):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:855) · Entrez [527](https://www.ncbi.nlm.nih.gov/gene/527) · UniProt [P27449](https://www.uniprot.org/uniprotkb/P27449) · Ensembl [ENSG00000185883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185883)

## Data

Gene col 11747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11747); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11747]; `tensor/DDL_lfc|DDL_z.npy` [11747]; `embed/gene_vectors.npy` [11747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11747 or target_col == 11747). Every well: [[ATP6V0C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
