---
symbol: "AP4B1"
type: "gene"
col: 5533
ensembl_id: "ENSG00000134262"
name: "adaptor related protein complex 4 subunit beta 1"
location: "1p13.2"
module: 72
arm: "+"
pooled_cpm: 8.63
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# AP4B1

*adaptor related protein complex 4 subunit beta 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.25× (z +10.6, q 2e-23, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.469× (z -10.5, q 5e-23, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.566× (z -7.9, q 5e-13, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM161A]] (+0.59, fdr 2e-05), [[NAPG]] (+0.58, fdr 5e-05), [[MINDY4]] (+0.58, fdr 1e-05); moves opposite to [[BMPR2]] (-0.55, fdr 1e-05), [[CERT1]] (-0.55, fdr 1e-04), [[EP300]] (-0.53, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.25×** | +10.6 | 2e-23 | 32/45 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.06×** | +10.0 | 5e-21 | 31/45 (A498, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +8.9 | 8e-17 | 28/46 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +7.8 | 6e-13 | 27/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.8 | 7e-07 | 24/47 (RKO, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +5.8 | 7e-07 | 20/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.5 | 4e-06 | 20/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.3 | 8e-06 | 20/47 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.1 | 2e-05 | 11/29 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.44×** | +5.0 | 3e-05 | 16/47 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.7 | 1e-04 | 15/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tadalafil (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.002 | 9/46 (KATO III, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.006 | 9/47 (RKO, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.013 | 11/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.020 | 6/45 (SNU-423, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.053 | 9/41 (LoVo, SW1417, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.067 | 3/48 (NCI-H1573, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -10.5 | 5e-23 | 30/45 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -8.6 | 2e-15 | 21/32 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -7.9 | 5e-13 | 27/48 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -6.2 | 1e-07 | 12/21 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.691×** | -5.1 | 3e-05 | 19/47 (HCT15, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -4.6 | 5e-04 | 12/15 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.728×** | -4.4 | 8e-04 | 19/46 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.743×** | -4.1 | 0.003 | 18/40 (HS-578T, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.843× | -3.4 | 0.047 | 20/43 (NCI-H1792, SK-MEL-2, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.063 | 9/43 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.785×** | -3.2 | 0.063 | 17/37 (HCT15, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 3 (2 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.178× (z -9.7) |
| [[A498 (line)]] | wt | 10.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -11.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0722× (z -14.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.10 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0769× (z -12.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0687× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 9.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.57 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0921× (z -10.3) |
| [[PANC-1 (line)]] | alt | 8.63 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0946× (z -11.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.122× (z -9.6) |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 16.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0881× (z -9.3) |
| [[A-172 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM161A]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[NAPG]] | +0.58 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[MINDY4]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DGKG]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PSMD13]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[SLC10A7]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[DELE1]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[DCAF13]] | +0.56 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[NUDC]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CCT3]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PLAA]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CCT6A]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMPR2]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CERT1]] | -0.55 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[EP300]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.53 | -0.60 / -0.32 | both halves | 1e-04 |  |
| [[ASH1L]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DNAI4]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[UBXN2A]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[KAT2B]] | -0.51 | -0.56 / -0.21 | both halves | 7e-04 |  |
| [[CHD2]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NIFK-AS1]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RRAGC-DT]] | -0.50 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[YY1AP1]] | -0.50 | -0.37 / -0.48 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.5, -32.3); signed map (-30.6, -31.6). **Vector** length 74.6, 12.5% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.1 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.1 | +1.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 4 subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,894,194-113,905,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BETA-4; previously SPG47 |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 4 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 5 pathways, smallest: Lysosome Vesicle Biogenesis; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6B7](https://www.uniprot.org/uniprotkb/Q9Y6B7) (AP-4 complex subunit beta-1):

> Component of the adaptor protein complex 4 (AP-4). Adaptor protein complexes are vesicle coat components involved both in vesicle formation and cargo selection. They control the vesicular transport of proteins in different trafficking pathways. AP-4 forms a non clathrin-associated coat on vesicles departing the trans-Golgi network (TGN) and may be involved in the targeting of proteins from the trans-Golgi network (TGN) to the endosomal-lysosomal system. It is also involved in protein sorting to …

**Summary**, from NCBI Gene [10717](https://www.ncbi.nlm.nih.gov/gene/10717):

> This gene encodes a subunit of a heterotetrameric adapter-like complex 4 that is involved in targeting proteins from the trans-Golgi network to the endosomal-lysosomal system. Mutations in this gene are associated with cerebral palsy spastic quadriplegic type 5 (CPSQ5) disorder. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:572) · Entrez [10717](https://www.ncbi.nlm.nih.gov/gene/10717) · UniProt [Q9Y6B7](https://www.uniprot.org/uniprotkb/Q9Y6B7) · Ensembl [ENSG00000134262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134262)

## Data

Gene col 5533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5533); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5533]; `tensor/DDL_lfc|DDL_z.npy` [5533]; `embed/gene_vectors.npy` [5533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5533 or target_col == 5533). Every well: [[AP4B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP4B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
