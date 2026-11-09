---
symbol: "STX4"
type: "gene"
col: 2374
ensembl_id: "ENSG00000103496"
name: "syntaxin 4"
location: "16p11.2"
module: 96
arm: "+"
pooled_cpm: 22.65
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# STX4

*syntaxin 4* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +11.9, q 8e-30, up in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.89× (z +10.5, q 1e-23, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.639× (z -7.4, q 9e-11, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT1S1]] (+0.66, fdr 7e-06), [[WBP2]] (+0.64, fdr 7e-06), [[CDK3]] (+0.62, fdr 7e-06); moves opposite to [[MTERF3]] (-0.63, fdr 7e-06), [[NDC1]] (-0.57, fdr 2e-05), [[POGLUT2]] (-0.57, fdr 2e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.67×** | +11.9 | 8e-30 | 34/47 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +11.6 | 6e-29 | 36/42 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +10.5 | 1e-23 | 24/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +10.5 | 1e-23 | 42/48 (NCI-H23, SK-MEL-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +7.9 | 3e-13 | 28/36 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.2 | 5e-08 | 21/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.45×** | +6.1 | 1e-07 | 27/44 (LS 180, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.42×** | +5.5 | 2e-06 | 22/48 (PANC-1, HEC-1-A, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +5.3 | 8e-06 | 24/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 2e-04 | 18/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 16/47 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +3.8 | 0.006 | 20/47 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.006 | 16/48 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.014 | 15/44 (A-427, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.3 | 0.035 | 15/46 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Saquinavir (drug)]] 5 µM |  | 1.14× | +3.0 | 0.080 | 12/48 (NCI-H2347, SHP-77, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.099 | 10/47 (KATO III, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.639×** | -7.4 | 9e-11 | 30/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -7.1 | 2e-10 | 32/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.649×** | -7.1 | 2e-10 | 31/48 (A498, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -6.0 | 2e-07 | 25/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.694×** | -6.0 | 2e-07 | 26/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.705×** | -5.8 | 8e-07 | 27/48 (AN3 CA, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.748×** | -4.6 | 3e-04 | 19/46 (A498, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.830×** | -4.4 | 9e-04 | 23/47 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -4.2 | 0.002 | 18/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.764×** | -4.2 | 0.002 | 19/47 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.694×** | -3.1 | 0.085 | 6/48 (A498, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Torkinib (drug)]] 0.05 µM |  | 0.824× | -3.0 | 0.12 | 6/48 (A-427, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +11.1) ⚠ cell-cycle shift, explains ~49% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 22.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 42.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +14.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 36.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 27.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.305× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 21.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.01× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +8.5) | — |
| [[A549 (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 34.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0547× (z -13.3) |
| [[HOP62 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1S1]] | +0.66 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[WBP2]] | +0.64 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[CDK3]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GRIPAP1]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB4]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SYNGAP1]] | +0.59 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[GAS8]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MOB3C]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.58 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SMCR8]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[STAT6]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTERF3]] | -0.63 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[NDC1]] | -0.57 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[POMGNT2]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PREP]] | -0.54 | -0.40 / -0.59 | both halves | 5e-05 | pathway: HALLMARK_COMPLEMENT |
| [[NT5M]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NME2]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TAF5L]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PRDX4]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[EEF1AKMT4]] | -0.51 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[L2HGDH]] | -0.51 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[METAP1]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.475). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.4, -17.1); signed map (9.7, -19.5). **Vector** length 83.2, 16.8% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.8 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -7.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,032,889-31,042,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p35-2; previously STX4A |
| Gene groups (HGNC) | Syntaxins |
| Hallmark sets | COMPLEMENT, APICAL_JUNCTION |
| Reactome | 15 pathways, smallest: Disinhibition of SNARE formation; Other interleukin signaling; Translocation of SLC2A4 (GLUT4) to the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12846](https://www.uniprot.org/uniprotkb/Q12846) (Syntaxin-4):

> Plasma membrane t-SNARE that mediates docking of transport vesicles (By similarity). Necessary for the translocation of SLC2A4 from intracellular vesicles to the plasma membrane (By similarity). In neurons, recruited at neurite tips to membrane domains rich in the phospholipid 1-oleoyl-2-palmitoyl-PC (OPPC) which promotes neurite tip surface expression of the dopamine transporter SLC6A3/DAT by facilitating fusion of SLC6A3-containing transport vesicles with the plasma membrane (By similarity). …

**Summary**, from NCBI Gene [6810](https://www.ncbi.nlm.nih.gov/gene/6810):

> Enables sphingomyelin phosphodiesterase activator activity. Involved in several processes, including cornified envelope assembly; positive regulation of immune effector process; and positive regulation of protein localization. Located in several cellular components, including basolateral plasma membrane; cytoplasmic vesicle; and obsolete extracellular space. Part of SNARE complex. Is active in glutamatergic synapse and postsynapse. Implicated in autosomal recessive nonsyndromic deafness. …

**Accessions** — [HGNC:11439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11439) · Entrez [6810](https://www.ncbi.nlm.nih.gov/gene/6810) · UniProt [Q12846](https://www.uniprot.org/uniprotkb/Q12846) · Ensembl [ENSG00000103496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103496)

## Data

Gene col 2374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2374); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2374]; `tensor/DDL_lfc|DDL_z.npy` [2374]; `embed/gene_vectors.npy` [2374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2374 or target_col == 2374). Every well: [[STX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
