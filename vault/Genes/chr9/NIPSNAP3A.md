---
symbol: "NIPSNAP3A"
type: "gene"
col: 5902
ensembl_id: "ENSG00000136783"
name: "nipsnap homolog 3A"
location: "9q31.1"
module: 47
arm: "+"
pooled_cpm: 9.32
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# NIPSNAP3A

*nipsnap homolog 3A* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +8.0, q 1e-12, up in 20 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Lidocaine (hydrochloride) (drug)]] 0.05 µM: 1.32× (z +3.3, q 0.085, up in 8 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.355× (z -16.8, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANGEL2]] (+0.58, fdr 4e-05), [[SETMAR]] (+0.56, fdr 3e-05), [[RWDD4]] (+0.56, fdr 3e-05); moves opposite to [[FOS]] (-0.56, fdr 1e-05), [[FOSB]] (-0.53, fdr 1e-05), [[NPAS1]] (-0.52, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.0 | 1e-12 | 20/31 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.8 | 2e-12 | 14/20 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.7 | 2e-06 | 10/24 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.6 | 6e-04 | 15/35 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.29×** | +4.2 | 0.004 | 9/47 (J82, HS-578T, …) | top dose only | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.085 | 8/40 (RKO, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.31× | +3.1 | 0.13 | 8/47 (A498, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.30× | +3.1 | 0.15 | 7/44 (SNU-423, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.355×** | -16.8 | 0e+00 | 41/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.336×** | -13.1 | 2e-36 | 39/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.381×** | -11.5 | 2e-28 | 37/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.385×** | -11.4 | 5e-28 | 38/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -11.3 | 1e-27 | 36/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.483×** | -8.4 | 6e-15 | 32/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -8.2 | 2e-14 | 29/43 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.521×** | -7.8 | 5e-13 | 26/47 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.550×** | -7.1 | 6e-11 | 27/43 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.362×** | -6.4 | 1e-08 | 27/41 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.599×** | -6.1 | 5e-08 | 28/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.626×** | -5.6 | 1e-06 | 24/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.723×** | -5.2 | 9e-06 | 20/48 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -5.1 | 2e-05 | 23/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -5.0 | 2e-05 | 20/45 (Hs 766T, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -4.8 | 6e-05 | 20/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.673×** | -4.7 | 8e-05 | 20/42 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -4.7 | 1e-04 | 19/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.5) |
| [[J82 (line)]] | alt | 18.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -19.5) |
| [[SW480 (line)]] | alt | 9.36 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.9) |
| [[A498 (line)]] | wt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.1) |
| [[A549 (line)]] | wt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.2) |
| [[LoVo (line)]] | wt | 5.74 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.106× (z -8.6) |
| [[HOP62 (line)]] | alt | 7.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -14.9) |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -8.6) |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -10.4) |
| [[KATO III (line)]] | alt | 8.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.9) |
| [[LS 180 (line)]] | wt | 7.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 6.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.4) |
| [[PANC-1 (line)]] | alt | 6.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.9) |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.5) |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.7) |
| [[SW1417 (line)]] | alt | 6.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0778× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL2]] | +0.58 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[SETMAR]] | +0.56 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[RWDD4]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[WASH2P-1]] | +0.56 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[PIGC]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[ZBTB26]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HGSNAT]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[ZNF708]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TMEM128]] | +0.54 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[SEC22C]] | +0.53 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[RBM45]] | +0.52 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[INTS12]] | +0.50 | +0.36 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOS]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FOSB]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NPAS1]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TINCR]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HAL]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[FAM222A]] | -0.51 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PRKCG]] | -0.49 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CPNE9]] | -0.48 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[HES1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[SRSF9]] ⚠ | -0.48 | -0.43 / -0.33 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LDHC]] | -0.47 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[FGF18]] | -0.47 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[TNIK]] | -0.46 | -0.23 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction -0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.8, 20.8); signed map (12.3, -42.5). **Vector** length 65.0, 11.0% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.1 | -7.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | nipsnap homolog 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:104,747,683-104,760,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564D177, FLJ13953, HSPC299, MGC14553, NIPSNAP4, TassC |
| Matched by | ensembl_id |

UniProt [Q9UFN0](https://www.uniprot.org/uniprotkb/Q9UFN0) carries no function annotation.

**Summary**, from NCBI Gene [25934](https://www.ncbi.nlm.nih.gov/gene/25934):

> NIPSNAP3A belongs to a family of proteins with putative roles in vesicular transport (Buechler et al., 2004 [PubMed 15177564]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23619) · Entrez [25934](https://www.ncbi.nlm.nih.gov/gene/25934) · UniProt [Q9UFN0](https://www.uniprot.org/uniprotkb/Q9UFN0) · Ensembl [ENSG00000136783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136783)

## Data

Gene col 5902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5902); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5902]; `tensor/DDL_lfc|DDL_z.npy` [5902]; `embed/gene_vectors.npy` [5902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5902 or target_col == 5902). Every well: [[NIPSNAP3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPSNAP3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
