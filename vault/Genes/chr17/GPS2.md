---
symbol: "GPS2"
type: "gene"
col: 5333
ensembl_id: "ENSG00000132522"
name: "G protein pathway suppressor 2"
location: "17p13.1"
module: 12
arm: "+"
pooled_cpm: 34.77
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GPS2

*G protein pathway suppressor 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.77× (z +13.4, q 5e-38, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +7.8, q 1e-12, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMAT2]] (+0.62, fdr 1e-05), [[PAF1]] (+0.61, fdr 7e-06), [[CHMP4A]] (+0.60, fdr 2e-05); moves opposite to [[ASIC1]] (-0.58, fdr 3e-05), [[BRI3BP]] (-0.57, fdr 4e-05), [[TUFM]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.77×** | +13.4 | 5e-38 | 44/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.20×** | +11.3 | 6e-27 | 34/37 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.42×** | +8.2 | 3e-14 | 39/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.8 | 1e-12 | 38/47 (SW 900, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.71×** | +7.6 | 3e-12 | 41/48 (SW 900, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.02×** | +7.1 | 1e-10 | 44/48 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.99×** | +6.9 | 4e-10 | 45/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.87×** | +6.3 | 2e-08 | 42/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.84×** | +6.1 | 6e-08 | 38/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +6.0 | 8e-08 | 36/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.72×** | +5.3 | 7e-06 | 36/48 (NCI-H2030, SW 900, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.2 | 1e-05 | 33/47 (SW 900, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.55×** | +4.2 | 0.001 | 33/48 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +4.1 | 0.002 | 29/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.010 | 27/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.040 | 23/48 (LS 180, CFPAC-1, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.063 | 21/48 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.74×** | +2.9 | 0.095 | 16/48 (HS-578T, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 42.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[LoVo (line)]] | wt | 39.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 43.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 22.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 53.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 31.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.8) | — |
| [[A-427 (line)]] | wt | 45.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[HEC-1-A (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[RPMI-7951 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMAT2]] | +0.62 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[PAF1]] | +0.61 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.60 | +0.73 / +0.47 | both halves | 2e-05 | pathway: HCMV Infection |
| [[DNAJB2]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[OPTN]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[SNRNP27]] | +0.56 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[DNAL4]] | +0.56 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[MED29]] | +0.55 | +0.70 / +0.45 | both halves | 3e-05 | pathway: PPARA activates gene expression |
| [[CREB3]] | +0.55 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[FAM161B]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD49]] | +0.55 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[UBXN1]] | +0.55 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASIC1]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[BRI3BP]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[TUFM]] | -0.57 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[TMEM97]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LDHB]] | -0.54 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[ADAT2]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[UCK2]] | -0.53 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[HACD3]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TMEM248]] | -0.53 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[EEF1E1]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[C1QBP]] | -0.52 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ALG3]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-11.2, 5.2); signed map (10.1, -19.2). **Vector** length 46.0, 8.82% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.0 | +5.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | -0.8 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.5 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.3 | -1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | +0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.9 | +3.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein pathway suppressor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,311,324-7,315,564 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NCoR/SMRT transcriptional repression complex subunits |
| Reactome | 24 pathways, smallest: Loss of MECP2 binding ability to the NCoR/SMRT complex; Disorders of Nervous System Development; Loss of function of MECP2 in Rett syndrome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13227](https://www.uniprot.org/uniprotkb/Q13227) (G protein pathway suppressor 2):

> Key regulator of inflammation, lipid metabolism and mitochondrion homeostasis that acts by inhibiting the activity of the ubiquitin-conjugating enzyme UBE2N/Ubc13, thereby inhibiting 'Lys-63'-linked ubiquitination (By similarity). In the nucleus, can both acts as a corepressor and coactivator of transcription, depending on the context. Acts as a transcription coactivator in adipocytes by promoting the recruitment of PPARG to promoters: acts by inhibiting the activity of the …

**Summary**, from NCBI Gene [2874](https://www.ncbi.nlm.nih.gov/gene/2874):

> This gene encodes a protein involved in G protein-mitogen-activated protein kinase (MAPK) signaling cascades. When overexpressed in mammalian cells, this gene could potently suppress a RAS- and MAPK-mediated signal and interfere with JNK activity, suggesting that the function of this gene may be signal repression. The encoded protein is an integral subunit of the NCOR1-HDAC3 (nuclear receptor corepressor 1-histone deacetylase 3) complex, and it was shown that the complex inhibits JNK activation …

**Accessions** — [HGNC:4550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4550) · Entrez [2874](https://www.ncbi.nlm.nih.gov/gene/2874) · UniProt [Q13227](https://www.uniprot.org/uniprotkb/Q13227) · Ensembl [ENSG00000132522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132522)

## Data

Gene col 5333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5333); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5333]; `tensor/DDL_lfc|DDL_z.npy` [5333]; `embed/gene_vectors.npy` [5333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5333 or target_col == 5333). Every well: [[GPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
