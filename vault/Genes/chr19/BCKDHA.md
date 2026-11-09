---
symbol: "BCKDHA"
type: "gene"
col: 14517
ensembl_id: "ENSG00000248098"
name: "branched chain keto acid dehydrogenase E1 subunit alpha"
location: "19q13.2"
module: 144
arm: "+"
pooled_cpm: 22.85
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# BCKDHA

*branched chain keto acid dehydrogenase E1 subunit alpha* — 19q13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.388× (z -16.1, q 0e+00, down in 40 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.548× (z -10.6, q 4e-24, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NARF]] (+0.66, fdr 7e-06), [[PDPR]] (+0.64, fdr 7e-06), [[XAB2]] (+0.63, fdr 7e-06); moves opposite to [[DNAH14]] (-0.55, fdr 2e-05), [[RABGAP1L]] (-0.55, fdr 7e-06), [[ZDHHC21]] (-0.53, fdr 1e-04).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.388×** | -16.1 | 0e+00 | 40/46 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.470×** | -13.4 | 3e-38 | 44/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -10.6 | 4e-24 | 34/47 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -9.9 | 6e-21 | 45/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -9.8 | 1e-20 | 26/33 (A549, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.674×** | -9.8 | 1e-20 | 36/47 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -9.4 | 6e-19 | 30/38 (H4, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.592×** | -9.3 | 1e-18 | 31/42 (C32, LoVo, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.699×** | -8.9 | 3e-17 | 38/48 (Hs 766T, C-33 A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.441×** | -7.6 | 2e-12 | 29/45 (SK-MEL-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.495×** | -6.5 | 4e-09 | 30/46 (NCI-H1792, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.503×** | -6.4 | 9e-09 | 29/46 (Hs 766T, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.698×** | -6.4 | 9e-09 | 24/48 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.721×** | -5.8 | 3e-07 | 24/47 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.731×** | -5.5 | 1e-06 | 20/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.553×** | -5.5 | 2e-06 | 25/46 (KATO III, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.808×** | -5.3 | 4e-06 | 25/48 (HS-578T, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.566×** | -5.3 | 4e-06 | 26/47 (SHP-77, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.731×** | -5.2 | 6e-06 | 24/48 (SW 900, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.741×** | -5.1 | 1e-05 | 18/46 (A-427, HepG2/C3A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -5.1 | 1e-05 | 21/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.751×** | -4.9 | 3e-05 | 21/48 (PANC-1, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 33.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -15.1) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.276× (z -10.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.8) |
| [[HOP62 (line)]] | alt | 38.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -12.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.357× (z -8.9) |
| [[A-172 (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -10.5) |
| [[A549 (line)]] | wt | 44.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -23.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 37.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -9.9) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -11.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 15.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -10.0) ⚠ toxic |
| [[H4 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0872× (z -13.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -9.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.388× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.345× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -9.2) ⚠ toxic |
| [[RKO (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.259× (z -8.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.7) |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -9.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[PDPR]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[XAB2]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[VDAC1P8]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[HINFP]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[EMSY]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ANKZF1]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ZER1]] | +0.59 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[GPR146]] | +0.58 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[PEX13]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PEX3]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH14]] | -0.55 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[RABGAP1L]] | -0.55 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ZDHHC21]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[AGPS]] | -0.50 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[PSEN2]] | -0.49 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[AP1S3]] | -0.48 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[RAB10]] | -0.48 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[GALNT10]] | -0.48 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.1, -40.2); signed map (-29.9, 27.3). **Vector** length 99.6, 22.6% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | -0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -13.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.7 | -16.1 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -8.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | branched chain keto acid dehydrogenase E1 subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,397,808-41,425,002 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSU; previously OVD1A |
| Gene groups (HGNC) | Branched chain alpha-keto acid dehydrogenase complex subunits; Oxidoreductases |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 11 pathways, smallest: Loss-of-function mutations in BCKDHA or BCKDHB cause MSUD; BCKDH synthesizes BCAA-CoA from KIC, KMVA, KIV; Loss-of-function mutations in DBT cause MSUD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P12694](https://www.uniprot.org/uniprotkb/P12694) (2-oxoisovalerate dehydrogenase subunit alpha, mitochondrial):

> Together with BCKDHB forms the heterotetrameric E1 subunit of the mitochondrial branched-chain alpha-ketoacid dehydrogenase (BCKD) complex. The BCKD complex catalyzes the multi-step oxidative decarboxylation of alpha-ketoacids derived from the branched-chain amino-acids valine, leucine and isoleucine producing CO2 and acyl-CoA which is subsequently utilized to produce energy. The E1 subunit catalyzes the first step with the decarboxylation of the alpha-ketoacid forming an enzyme-product …

**Summary**, from NCBI Gene [593](https://www.ncbi.nlm.nih.gov/gene/593):

> The branched-chain alpha-keto acid (BCAA) dehydrogenase (BCKD) complex is an innter mitochondrial enzyme complex that catalyzes the second major step in the catabolism of the branched-chain amino acids leucine, isoleucine, and valine. The BCKD complex consists of three catalytic components: a heterotetrameric (alpha2-beta2) branched-chain alpha-keto acid decarboxylase (E1), a dihydrolipoyl transacylase (E2), and a dihydrolipoamide dehydrogenase (E3). This gene encodes the alpha subunit of the …

**Accessions** — [HGNC:986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:986) · Entrez [593](https://www.ncbi.nlm.nih.gov/gene/593) · UniProt [P12694](https://www.uniprot.org/uniprotkb/P12694) · Ensembl [ENSG00000248098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248098)

## Data

Gene col 14517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14517); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14517]; `tensor/DDL_lfc|DDL_z.npy` [14517]; `embed/gene_vectors.npy` [14517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14517 or target_col == 14517). Every well: [[BCKDHA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCKDHA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
