---
symbol: "FBXO36"
type: "gene"
col: 7743
ensembl_id: "ENSG00000153832"
name: "F-box protein 36"
location: "2q36.3"
module: 185
arm: "+"
pooled_cpm: 10.61
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# FBXO36

*F-box protein 36* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.55× (z +13.3, q 9e-38, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.414× (z -11.7, q 5e-29, down in 30 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.680× (z -7.8, q 2e-12, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNIP]] (+0.67, fdr 7e-06), [[MEF2B]] (+0.66, fdr 7e-06), [[RAB28]] (+0.65, fdr 1e-05); moves opposite to [[RYBP]] (-0.54, fdr 1e-05), [[IMPA1]] (-0.49, fdr 3e-05), [[IFRD1]] (-0.49, fdr 5e-05).
> It is in [[Module 185]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.55×** | +13.3 | 9e-38 | 42/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +12.1 | 3e-31 | 36/47 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.13×** | +10.1 | 7e-22 | 38/46 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +9.8 | 1e-20 | 32/47 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +8.4 | 5e-15 | 33/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.79×** | +7.9 | 2e-13 | 31/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +7.5 | 4e-12 | 31/47 (HOP62, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.0 | 1e-10 | 25/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +6.9 | 3e-10 | 25/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +6.9 | 3e-10 | 23/46 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.34×** | +6.3 | 1e-08 | 20/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +6.3 | 1e-08 | 23/46 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +5.8 | 3e-07 | 19/47 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.7 | 5e-07 | 9/26 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +4.7 | 8e-05 | 10/46 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 16/47 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.414×** | -11.7 | 5e-29 | 30/42 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.680×** | -7.8 | 2e-12 | 31/48 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -7.0 | 4e-10 | 23/46 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.658×** | -6.0 | 3e-07 | 21/44 (Hs 766T, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.705×** | -5.0 | 7e-05 | 22/47 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.716×** | -4.8 | 2e-04 | 19/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.735×** | -4.4 | 9e-04 | 16/47 (NCI-H1573, LoVo, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.728×** | -4.2 | 0.002 | 15/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.744×** | -4.2 | 0.002 | 8/47 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.748×** | -3.9 | 0.005 | 9/47 (A498, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -3.9 | 0.006 | 15/47 (A-172, A-427, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.013 | 9/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -3.4 | 0.025 | 14/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.636×** | -3.4 | 0.031 | 10/44 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 24.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.6) | [[Tucidinostat (drug)]] 5 µM 0.414× (z -9.2) |
| [[A-172 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -10.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.111× (z -14.1) |
| [[J82 (line)]] | alt | 7.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 5.31 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0808× (z -9.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.6) | — |
| [[RKO (line)]] | wt | 5.98 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0600× (z -9.3) |
| [[SW 900 (line)]] | alt | 7.94 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0824× (z -9.2) ⚠ toxic |
| [[A498 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNIP]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[MEF2B]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RAB28]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LIN52]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PSMB3]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ERCC8]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[KPNA6]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.56 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[IFT43]] | +0.55 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ULK4]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SYMPK]] | +0.54 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[PROSER3]] | +0.53 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.54 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[IMPA1]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[IFRD1]] | -0.49 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[SH3BGR]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[SNHG1]] | -0.48 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[TRIM36]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RETSAT]] | -0.47 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[SLC25A30]] | -0.46 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[COQ10A]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[OGFRL1]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[RAB33B]] | -0.44 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[BCL2L11]] | -0.44 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.5, -1.8); signed map (-18.2, -26.2). **Vector** length 86.8, 17.0% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +7.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[Dihydroartemisinin (drug)]] 0.05 µM |  | +1.2 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:229,922,302-230,013,119 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Fbx36, FLJ37592 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEA4](https://www.uniprot.org/uniprotkb/Q8NEA4) (F-box only protein 36):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [130888](https://www.ncbi.nlm.nih.gov/gene/130888):

> Members of the F-box protein family, such as FBXO36, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:27020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27020) · Entrez [130888](https://www.ncbi.nlm.nih.gov/gene/130888) · UniProt [Q8NEA4](https://www.uniprot.org/uniprotkb/Q8NEA4) · Ensembl [ENSG00000153832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153832)

## Data

Gene col 7743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7743); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7743]; `tensor/DDL_lfc|DDL_z.npy` [7743]; `embed/gene_vectors.npy` [7743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7743 or target_col == 7743). Every well: [[FBXO36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
