---
symbol: "GPN1"
type: "gene"
col: 12609
ensembl_id: "ENSG00000198522"
name: "GPN-loop GTPase 1"
location: "2p23.3"
module: 25
arm: "+"
pooled_cpm: 21.27
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GPN1

*GPN-loop GTPase 1* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.56× (z +15.1, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.796× (z -5.2, q 9e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.79, fdr 7e-06), [[NUDC]] (+0.75, fdr 7e-06), [[AP3M1]] (+0.75, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.73, fdr 7e-06), [[POLR2L]] (-0.64, fdr 7e-06), [[ACAP1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.56×** | +15.1 | 0e+00 | 44/47 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.51×** | +14.8 | 0e+00 | 45/48 (A498, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.47×** | +13.7 | 3e-40 | 43/48 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +11.2 | 4e-27 | 39/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +9.2 | 6e-18 | 20/30 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.96×** | +9.1 | 8e-18 | 35/40 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +8.1 | 4e-14 | 40/48 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.5 | 5e-12 | 27/42 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.91×** | +7.4 | 8e-12 | 33/48 (CFPAC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +6.6 | 3e-09 | 22/37 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +5.9 | 1e-07 | 27/45 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.9 | 2e-07 | 25/45 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.7 | 5e-07 | 26/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.4 | 3e-06 | 24/48 (NCI-H1573, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +4.2 | 0.001 | 19/48 (A549, RPMI-7951, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.001 | 13/48 (SNU-423, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.005 | 14/47 (A498, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.013 | 13/48 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.017 | 7/47 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.071 | 5/47 (A498, A-172, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +2.9 | 0.074 | 13/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -5.2 | 9e-05 | 24/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.744×** | -4.8 | 4e-04 | 25/48 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.717×** | -3.8 | 0.023 | 13/45 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.810×** | -3.4 | 0.071 | 14/48 (SW 1088, SK-MEL-2, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.744×** | -3.4 | 0.071 | 16/48 (KATO III, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.759× | -3.2 | 0.13 | 14/47 (HCT15, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.828× | -3.1 | 0.17 | 13/48 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.92× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.99× (z +9.8) | — |
| [[A-172 (line)]] | wt | 21.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.21× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.71× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.65× (z +9.4) | — |
| [[RKO (line)]] | wt | 26.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 25.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.66× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.59× (z +9.2) | — |
| [[C32 (line)]] | wt | 14.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.55× (z +9.5) | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.111× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 18.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.17× (z +9.2) | — |
| [[KATO III (line)]] | alt | 22.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.30× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.33× (z +9.0) | — |
| [[SW480 (line)]] | alt | 26.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +8.5) | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.79 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[NUDC]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[AP3M1]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[CRYZ]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[STIP1]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CCT3]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TCP1]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 | STRING 549 |
| [[API5]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[GFM2]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[FKBP4]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[STX16]] | +0.70 | +0.56 / +0.75 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.73 | -0.72 / -0.70 | both halves | 7e-06 |  |
| [[POLR2L]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 | STRING 648 |
| [[ACAP1]] | -0.62 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.62 | -0.52 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX5A]] ⚠ | -0.59 | -0.60 / -0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | -0.59 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | -0.59 | -0.50 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FOXA2]] | -0.59 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[POLR1H]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PPP1R14B]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.58 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[NBPF19]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.7, -13.2); signed map (-28.7, -29.1). **Vector** length 91.2, 19.6% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.3 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +14.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.7 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | GPN-loop GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,628,247-27,651,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTPBP, MBDIN, ATPBD1A, RPAP4; previously XAB1 |
| Gene groups (HGNC) | GPN-loop GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCN4](https://www.uniprot.org/uniprotkb/Q9HCN4) (GPN-loop GTPase 1):

> Small GTPase involved in the correct assembly of RNA polymerase II (RNAPII) complex, ensuring proper nuclear import of RNAPII. In vitro, exhibits a chaperone-like activity and a chaperone substrate protein can stimulate its GTPase activity. It is proposed to bind exposed hydrophobic peptide regions of newly synthesized RNAP II subunit, triggering the opening of a hydrophobic pocket in its GDP-bound state. This interaction likely traps exposed hydrophobic regions, preventing misassembly and …

**Summary**, from NCBI Gene [11321](https://www.ncbi.nlm.nih.gov/gene/11321):

> This gene encodes a guanosine triphosphatase enzyme. The encoded protein may play a role in DNA repair and may function in activation of transcription. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:17030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17030) · Entrez [11321](https://www.ncbi.nlm.nih.gov/gene/11321) · UniProt [Q9HCN4](https://www.uniprot.org/uniprotkb/Q9HCN4) · Ensembl [ENSG00000198522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198522)

## Data

Gene col 12609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12609); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12609]; `tensor/DDL_lfc|DDL_z.npy` [12609]; `embed/gene_vectors.npy` [12609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12609 or target_col == 12609). Every well: [[GPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
