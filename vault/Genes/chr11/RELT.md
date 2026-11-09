---
symbol: "RELT"
type: "gene"
col: 617
ensembl_id: "ENSG00000054967"
name: "RELT TNF receptor"
location: "11q13.4"
module: 198
arm: "+"
pooled_cpm: 23.07
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# RELT

*RELT TNF receptor* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +13.5, q 7e-39, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 0.583× (z -5.1, q 2e-04, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH1]] (+0.57, fdr 2e-05), [[CCDC200]] (+0.56, fdr 3e-05), [[LINC01128]] (+0.56, fdr 1e-05); moves opposite to [[FBXO9]] (-0.62, fdr 7e-06), [[ANKRD13C]] (-0.56, fdr 1e-05), [[MRPL44]] (-0.55, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +13.5 | 7e-39 | 43/47 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.69×** | +12.2 | 2e-31 | 44/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +10.5 | 2e-23 | 41/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.51×** | +8.6 | 1e-15 | 43/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +6.7 | 2e-09 | 37/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +6.3 | 2e-08 | 35/47 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +5.9 | 3e-07 | 36/46 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +5.8 | 5e-07 | 32/47 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.48×** | +5.2 | 2e-05 | 26/46 (J82, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +4.8 | 1e-04 | 33/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.35×** | +4.2 | 0.002 | 29/44 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.002 | 27/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 25/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.52×** | +3.9 | 0.004 | 24/48 (PANC-1, Panc 03.27, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.005 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.009 | 24/46 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.037 | 21/48 (PANC-1, NCI-H2030, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.043 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.049 | 20/47 (NCI-H1573, HCT15, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 617.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.583×** | -5.1 | 2e-04 | 33/46 (HOP62, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.598×** | -4.8 | 4e-04 | 32/48 (A-427, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.647×** | -3.9 | 0.016 | 25/46 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.669×** | -3.8 | 0.022 | 26/46 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.768×** | -3.4 | 0.071 | 23/48 (SW480, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.717× | -3.1 | 0.15 | 20/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.791× | -3.1 | 0.15 | 21/48 (SW480, NCI-H23, …) | all doses, flat | position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.796× | -3.1 | 0.15 | 20/48 (NCI-H23, SHP-77, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.700× | -3.0 | 0.15 | 18/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 18.3 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +19.0) | — |
| [[SW480 (line)]] | alt | 18.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.88× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 16.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +11.4) | — |
| [[KATO III (line)]] | alt | 15.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.99× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 27.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.52× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.23× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.16× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.84× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 7.13 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.5) | — |
| [[A498 (line)]] | wt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 76.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +9.3) | — |
| [[C32 (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 6.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +9.6) | — |
| [[J82 (line)]] | alt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.57× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +14.7) | — |
| [[SW 900 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +9.9) | — |
| [[SW48 (line)]] | wt | 24.4 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.103× (z -9.4) |
| [[A-172 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH1]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CCDC200]] | +0.56 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[LINC01128]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CSRP2]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MICALL2]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SH3D21]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PNP]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.53 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SMTN]] | +0.52 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[MIR30DHG]] | +0.52 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHO2]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CYCS]] | +0.52 | +0.37 / +0.51 | both halves | 7e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO9]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[ANKRD13C]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MRPL44]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PSMG2]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GUSBP2-1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CWC15]] | -0.53 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[TNRC6A]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CLPX]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[DHX29]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SETD2]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction -0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.4, 15.9); signed map (1.4, 20.6). **Vector** length 90.9, 24.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.2 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.2 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -0.4 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.6 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +1.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.9 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | RELT TNF receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,376,399-73,397,474 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14993; previously TNFRSF19L |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily; RELT family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969Z4](https://www.uniprot.org/uniprotkb/Q969Z4) (Tumor necrosis factor receptor superfamily member 19L):

> May play a role in apoptosis. Induces activation of MAPK14/p38 and MAPK8/JNK MAPK cascades, when overexpressed. Involved in dental enamel formation.

**Summary**, from NCBI Gene [84957](https://www.ncbi.nlm.nih.gov/gene/84957):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor is especially abundant in hematologic tissues. It has been shown to activate the NF-kappaB pathway and selectively bind TNF receptor-associated factor 1 (TRAF1). This receptor is capable of stimulating T-cell proliferation in the presence of CD3 signaling, which suggests its regulatory role in immune response. Two alternatively spliced transcript variants of this gene encoding the same protein have been …

**Accessions** — [HGNC:13764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13764) · Entrez [84957](https://www.ncbi.nlm.nih.gov/gene/84957) · UniProt [Q969Z4](https://www.uniprot.org/uniprotkb/Q969Z4) · Ensembl [ENSG00000054967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054967)

## Data

Gene col 617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 617); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 617]; `tensor/DDL_lfc|DDL_z.npy` [617]; `embed/gene_vectors.npy` [617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 617 or target_col == 617). Every well: [[RELT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
