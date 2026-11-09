---
symbol: "BLCAP"
type: "gene"
col: 9339
ensembl_id: "ENSG00000166619"
name: "BLCAP apoptosis inducing factor"
location: "20q11.23"
module: 52
arm: "+"
pooled_cpm: 74.87
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# BLCAP

*BLCAP apoptosis inducing factor* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +10.3, q 6e-22, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.538× (z -11.4, q 2e-27, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM104]] (+0.66, fdr 7e-06), [[NDEL1]] (+0.63, fdr 7e-06), [[RER1]] (+0.62, fdr 7e-06); moves opposite to [[SLX4IP]] (-0.50, fdr 3e-05), [[CHIC1]] (-0.50, fdr 4e-05), [[SUZ12]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +10.3 | 6e-22 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.5 | 5e-19 | 35/49 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +6.7 | 4e-09 | 33/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.6 | 4e-09 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 6e-04 | 23/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.005 | 21/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.017 | 14/48 (LoVo, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.5 | 0.039 | 20/48 (MIA PaCa-2, SW480, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | 1.37× | +3.1 | 0.11 | 10/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -11.4 | 2e-27 | 35/48 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -8.3 | 3e-14 | 26/41 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -6.7 | 5e-09 | 28/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.710×** | -6.6 | 7e-09 | 28/49 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -5.7 | 2e-06 | 25/48 (LoVo, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -3.8 | 0.015 | 20/49 (NCI-H1792, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.813×** | -3.7 | 0.020 | 21/43 (RKO, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.704×** | -3.5 | 0.030 | 20/45 (SK-MEL-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.834× | -3.5 | 0.032 | 21/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.845× | -3.1 | 0.11 | 17/48 (A-427, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 146 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.305× (z -11.8) |
| [[LoVo (line)]] | wt | 102 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.391× (z -9.5) |
| [[A498 (line)]] | wt | 78.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +11.5) ⚠ cell-cycle shift, explains ~50% of this change | [[Harringtonine (drug)]] 5 µM 0.233× (z -13.8) |
| [[Hs 766T (line)]] | wt | 480 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.271× (z -13.3) |
| [[KATO III (line)]] | alt | 104 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +17.8) | — |
| [[J82 (line)]] | alt | 98.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.413× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 32.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.2) | — |
| [[SW480 (line)]] | alt | 62.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HT-29 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 43.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +12.7) | [[Harringtonine (drug)]] 5 µM 0.485× (z -8.7) |
| [[RKO (line)]] | wt | 67.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SNU-1 (line)]] | wt | 69.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.1) | — |
| [[A549 (line)]] | wt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 45.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.125× (z -8.9) |
| [[C32 (line)]] | wt | 36.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 65.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 46.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -10.6) |
| [[HS-578T (line)]] | alt | 72.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.314× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 58.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -9.4) |
| [[LS 180 (line)]] | wt | 137 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.416× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -17.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 65.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.334× (z -8.8) |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0797× (z -9.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 39.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM104]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[RER1]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.62 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[OSBPL2]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RNF139-DT]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SENP5]] | +0.60 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[BET1L]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[DPP9]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.59 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PDCD6]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[DHDDS]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX4IP]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[CHIC1]] | -0.50 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[SUZ12]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers BLCAP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.9, -27.9); signed map (-49.7, 3.7). **Vector** length 111, 29.8% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +4.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.2 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | -0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.0 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -6.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.4 | -1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | BLCAP apoptosis inducing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,492,472-37,527,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BC10 |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [P62952](https://www.uniprot.org/uniprotkb/P62952) (Apoptosis inducing factor BLCAP):

> Acts as a tumor suppressor; induces growth arrest at G(1)/S checkpoint and apoptosis via RB1-dependent and p53/TP53- and NF-kappa-B-independent mechanisms. Modulates expression of genes involved in the regulation of proliferation, cell cycle and apoptosis.

**Summary**, from NCBI Gene [10904](https://www.ncbi.nlm.nih.gov/gene/10904):

> This gene encodes a protein that reduces cell growth by stimulating apoptosis. Alternative splicing and the use of alternative promoters result in multiple transcript variants encoding the same protein. This gene is imprinted in brain where different transcript variants are expressed from each parental allele. Transcript variants initiating from the upstream promoter are expressed preferentially from the maternal allele, while transcript variants initiating downstream of the interspersed NNAT …

**Accessions** — [HGNC:1055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1055) · Entrez [10904](https://www.ncbi.nlm.nih.gov/gene/10904) · UniProt [P62952](https://www.uniprot.org/uniprotkb/P62952) · Ensembl [ENSG00000166619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166619)

## Data

Gene col 9339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9339); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9339]; `tensor/DDL_lfc|DDL_z.npy` [9339]; `embed/gene_vectors.npy` [9339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9339 or target_col == 9339). Every well: [[BLCAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLCAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
