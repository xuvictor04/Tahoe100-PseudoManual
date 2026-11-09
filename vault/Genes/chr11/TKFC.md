---
symbol: "TKFC"
type: "gene"
col: 7375
ensembl_id: "ENSG00000149476"
name: "triokinase and FMN cyclase"
location: "11q12.2"
module: 96
arm: "+"
pooled_cpm: 8.8
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# TKFC

*triokinase and FMN cyclase* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.88× (z +12.5, q 6e-33, up in 11 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.53× (z +3.7, q 0.031, up in 8 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.318× (z -14.1, q 2e-42, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROS]] (+0.73, fdr 7e-06), [[ADAMTS13]] (+0.65, fdr 1e-05), [[PIGO]] (+0.64, fdr 1e-05); moves opposite to [[SELENOK]] (-0.57, fdr 2e-05), [[FTL]] (-0.54, fdr 2e-05), [[MED31]] (-0.51, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +12.5 | 6e-33 | 11/15 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +12.0 | 1e-30 | 30/34 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +10.9 | 4e-25 | 20/25 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.031 | 8/35 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.059 | 9/45 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.068 | 6/44 (PANC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.3 | 0.081 | 9/38 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.28× | +3.0 | 0.17 | 5/46 (SW480, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.318×** | -14.1 | 2e-42 | 41/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -11.8 | 8e-30 | 32/44 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.518×** | -11.5 | 4e-28 | 28/42 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.460×** | -9.6 | 2e-19 | 34/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -9.3 | 2e-18 | 31/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -9.2 | 2e-18 | 36/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.468×** | -8.8 | 9e-17 | 31/43 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.556×** | -7.2 | 3e-11 | 23/45 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -5.9 | 3e-07 | 24/44 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -5.3 | 7e-06 | 22/45 (SW480, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.672×** | -4.9 | 5e-05 | 20/45 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -4.4 | 5e-04 | 17/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -3.7 | 0.010 | 15/44 (NCI-H23, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -3.5 | 0.018 | 11/43 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.582×** | -3.5 | 0.018 | 13/29 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.693×** | -3.2 | 0.044 | 10/46 (Hs 766T, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.0 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -16.0) |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -16.4) |
| [[LoVo (line)]] | wt | 11.3 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0442× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0911× (z -12.6) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0726× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -10.1) |
| [[KATO III (line)]] | alt | 18.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +8.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 0.5 µM 0.196× (z -9.8) |
| [[HOP62 (line)]] | alt | 7.39 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -9.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.135× (z -9.4) |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Oxaprozin (drug)]] 0.5 µM 0.105× (z -9.4) |
| [[A-172 (line)]] | wt | 7.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 9.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -8.8) |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0656× (z -11.9) |
| [[C32 (line)]] | wt | 6.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0977× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 6.58 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0715× (z -8.5) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 9.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 5.04 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0891× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 8.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 7.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.104× (z -9.2) |
| [[SNU-1 (line)]] | wt | 7.62 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0693× (z -9.0) |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -14.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROS]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[ADAMTS13]] | +0.65 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[PIGO]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SPATA20]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ARPIN]] | +0.64 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[D2HGDH]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[PRRC2A]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[FTCDNL1]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[IMPACT]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[IDUA]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PCYOX1L]] | +0.59 | +0.71 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FTL]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MED31]] | -0.51 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[MFSD11]] | -0.51 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[TULP3]] | -0.51 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[ABHD3]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RAB4B]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[HLA-F-AS1]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ATP6V0B]] | -0.49 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[C9orf24]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-28.2, 23.7); signed map (16.3, -42.8). **Vector** length 56.4, 8.22% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +12.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -9.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | triokinase and FMN cyclase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,333,220-61,353,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586B1621, NET45; previously DAK |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 12 pathways, smallest: Fructose metabolism; SARS-CoV-1 activates/modulates innate immune responses; DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3LXA3](https://www.uniprot.org/uniprotkb/Q3LXA3) (Triokinase/FMN cyclase):

> Catalyzes both the phosphorylation of dihydroxyacetone and of glyceraldehyde, and the splitting of ribonucleoside diphosphate-X compounds among which FAD is the best substrate. Represses IFIH1-mediated cellular antiviral response.

**Summary**, from NCBI Gene [26007](https://www.ncbi.nlm.nih.gov/gene/26007):

> This gene is a member of the family of dihydroxyacetone kinases, which have a protein structure distinct from other kinases. The product of this gene phosphorylates dihydroxyacetone, and also catalyzes the formation of riboflavin 4',5'-phosphate (aka cyclin FMN) from FAD. Several alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:24552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24552) · Entrez [26007](https://www.ncbi.nlm.nih.gov/gene/26007) · UniProt [Q3LXA3](https://www.uniprot.org/uniprotkb/Q3LXA3) · Ensembl [ENSG00000149476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149476)

## Data

Gene col 7375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7375); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7375]; `tensor/DDL_lfc|DDL_z.npy` [7375]; `embed/gene_vectors.npy` [7375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7375 or target_col == 7375). Every well: [[TKFC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TKFC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
