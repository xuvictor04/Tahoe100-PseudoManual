---
symbol: "OTUD6B"
type: "gene"
col: 7872
ensembl_id: "ENSG00000155100"
name: "OTU deubiquitinase 6B"
location: "8q21.3"
module: 188
arm: "+"
pooled_cpm: 31.24
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# OTUD6B

*OTU deubiquitinase 6B* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (17 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.14× (z +11.2, q 1e-26, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.13× (z +11.2, q 1e-26, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Entrectinib (drug)]] 5 µM: 0.765× (z -4.0, q 0.030, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCSH]] (+0.72, fdr 7e-06), [[MRPS35]] (+0.69, fdr 7e-06), [[EEF1E1]] (+0.69, fdr 7e-06); moves opposite to [[OTUD5]] (-0.62, fdr 1e-05), [[TUT7]] (-0.62, fdr 1e-05), [[THUMPD3-AS1]] (-0.61, fdr 7e-06).
> It is in [[Module 188]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.14×** | +11.2 | 1e-26 | 45/47 (LoVo, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +11.2 | 1e-26 | 43/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +11.2 | 1e-26 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.98×** | +10.1 | 7e-22 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.77×** | +8.4 | 5e-15 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +7.5 | 7e-12 | 27/47 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +7.3 | 2e-11 | 30/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +7.3 | 2e-11 | 37/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +7.3 | 2e-11 | 28/47 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.63×** | +7.2 | 4e-11 | 35/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +7.1 | 5e-11 | 38/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +6.9 | 2e-10 | 33/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +6.7 | 1e-09 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 1e-09 | 34/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +6.0 | 1e-07 | 27/47 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.9 | 1e-07 | 31/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +5.7 | 4e-07 | 29/48 (KATO III, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +5.6 | 8e-07 | 29/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 9e-07 | 26/47 (PANC-1, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +4.5 | 2e-04 | 26/47 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 4e-04 | 21/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entrectinib (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.030 | 21/47 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.772×** | -3.9 | 0.030 | 15/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.032 | 17/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.032 | 17/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.803× | -3.3 | 0.10 | 8/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.804× | -3.3 | 0.10 | 10/47 (RKO, PANC-1, …) | two highest doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.812× | -3.1 | 0.12 | 8/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.747× | -3.1 | 0.12 | 21/48 (H4, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.807× | -3.1 | 0.12 | 15/47 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Posaconazole (drug)]] 5 µM |  | 0.808× | -3.1 | 0.12 | 12/48 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.4 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.60× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 23.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.75× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 43.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.73× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.3) | — |
| [[A498 (line)]] | wt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 28.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.9) | — |
| [[KATO III (line)]] | alt | 16.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +8.9) | — |
| [[LoVo (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.55× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.6) | — |
| [[SW48 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[A-172 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCSH]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[FAR1]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MRS2]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[RFXAP]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DTD2]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SORD]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUD5]] | -0.62 | -0.57 / -0.62 | both halves | 1e-05 | same gene group; STRING 650 |
| [[TUT7]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[C6orf62]] | -0.60 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[AP1G1]] | -0.57 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[RAB5A]] | -0.57 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[CYTH2]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[ZKSCAN1]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[NLGN3]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[INTS6]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.9, -12.3); signed map (-33.8, -18.7). **Vector** length 80.6, 19.6% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +7.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.4 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | +7.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -2.0 | -3.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:91,070,196-91,087,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-77, DUBA5 |
| Gene groups (HGNC) | OTU domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6M0](https://www.uniprot.org/uniprotkb/Q8N6M0) (Deubiquitinase OTUD6B):

> [Isoform 1]: Deubiquitinating enzyme that may play a role in the ubiquitin-dependent regulation of protein synthesis, downstream of mTORC1. May associate with the protein synthesis initiation complex and modify its ubiquitination to repress translation. May also repress DNA synthesis and modify different cellular targets thereby regulating cell growth and proliferation. May also play a role in proteasome assembly and function.; [Isoform 2]: Stimulates protein synthesis. Influences the …

**Summary**, from NCBI Gene [51633](https://www.ncbi.nlm.nih.gov/gene/51633):

> This gene encodes a member of the ovarian tumor domain (OTU)-containing subfamily of deubiquitinating enzymes. Deubiquitinating enzymes are primarily involved in removing ubiquitin from proteins targeted for degradation. This protein may function as a negative regulator of the cell cycle in B cells. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:24281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24281) · Entrez [51633](https://www.ncbi.nlm.nih.gov/gene/51633) · UniProt [Q8N6M0](https://www.uniprot.org/uniprotkb/Q8N6M0) · Ensembl [ENSG00000155100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155100)

## Data

Gene col 7872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7872); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7872]; `tensor/DDL_lfc|DDL_z.npy` [7872]; `embed/gene_vectors.npy` [7872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7872 or target_col == 7872). Every well: [[OTUD6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
