---
symbol: "RNF44"
type: "gene"
col: 7061
ensembl_id: "ENSG00000146083"
name: "ring finger protein 44"
location: "5q35.2"
module: 138
arm: "+"
pooled_cpm: 21.69
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# RNF44

*ring finger protein 44* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.70× (z +6.8, q 8e-09, up in 23 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +5.4, q 9e-06, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.624× (z -6.2, q 3e-07, down in 32 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.428× (z -5.9, q 1e-06, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF740]] (+0.67, fdr 7e-06), [[TEPSIN]] (+0.62, fdr 2e-05), [[FAM229A]] (+0.61, fdr 1e-05); moves opposite to [[ATP5PO]] (-0.49, fdr 3e-05, ⚠ ATP5PO in the vector space only through flagged drug-doses), [[BOLA3]] (-0.46, fdr 1e-04), [[AGGF1]] (-0.46, fdr 9e-05), [[CHD9]] (-0.45, fdr 1e-04).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.8 | 8e-09 | 23/32 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.7 | 3e-06 | 30/47 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.5 | 7e-06 | 27/41 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +5.4 | 9e-06 | 29/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.2 | 2e-05 | 24/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.6 | 4e-04 | 19/44 (LoVo, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.6 | 4e-04 | 20/36 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.4 | 8e-04 | 25/43 (A-172, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.39×** | +4.4 | 8e-04 | 23/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 9e-04 | 25/45 (PANC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.0 | 0.003 | 17/34 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.010 | 18/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.7 | 0.010 | 1/48 (hTERT-HPNE) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.015 | 14/46 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.015 | 15/47 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.017 | 9/47 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.033 | 17/44 (H4, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.035 | 15/46 (HCT15, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.624×** | -6.2 | 3e-07 | 32/47 (A498, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.428×** | -5.9 | 1e-06 | 29/45 (A-427, C-33 A, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -5.8 | 1e-06 | 25/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.439×** | -5.7 | 2e-06 | 31/46 (SNU-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -5.2 | 2e-05 | 24/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.577×** | -5.2 | 2e-05 | 24/48 (MIA PaCa-2, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.693×** | -4.9 | 1e-04 | 28/47 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.788×** | -4.5 | 6e-04 | 23/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.727×** | -4.2 | 0.002 | 24/47 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.566×** | -3.9 | 0.005 | 17/46 (A498, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.587×** | -3.7 | 0.012 | 20/48 (A498, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.595×** | -3.6 | 0.016 | 16/46 (H4, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.767×** | -3.5 | 0.020 | 21/48 (PANC-1, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.023 | 18/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.759×** | -3.4 | 0.023 | 18/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.780×** | -3.1 | 0.067 | 21/48 (A498, C-33 A, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.3) |
| [[PANC-1 (line)]] | alt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.8) |
| [[RKO (line)]] | wt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -9.3) |
| [[A-427 (line)]] | wt | 24.4 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0860× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +8.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -11.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0468× (z -11.2) |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF740]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TEPSIN]] | +0.62 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[FAM229A]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.61 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[LENG8]] | +0.59 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.57 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ZFTRAF1]] | +0.57 | +0.41 / +0.57 | both halves | 4e-05 | same gene group |
| [[CRTC2]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PCMTD2]] | +0.56 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[GIGYF1]] | +0.55 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[UCKL1]] | +0.55 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SBF1]] | +0.55 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5PO]] ⚠ | -0.49 | -0.49 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BOLA3]] | -0.46 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[AGGF1]] | -0.46 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[CHD9]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[HCFC2]] | -0.45 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[NDUFA7]] | -0.44 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[EBAG9]] | -0.43 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[SNAPIN]] | -0.43 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[KLHL9]] | -0.43 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.5, -23.0); signed map (3.3, -7.6). **Vector** length 98.7, 22.1% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +4.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.7 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.3 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.1 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.2 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.9 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -5.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,526,712-176,538,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1100 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q7L0R7](https://www.uniprot.org/uniprotkb/Q7L0R7) carries no function annotation.

**Summary**, from NCBI Gene [22838](https://www.ncbi.nlm.nih.gov/gene/22838):

> The protein encoded by this gene contains a RING finger, a motif present in a variety of functionally distinct proteins and known to be involved in protein-protein and protein-DNA interactions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19180) · Entrez [22838](https://www.ncbi.nlm.nih.gov/gene/22838) · UniProt [Q7L0R7](https://www.uniprot.org/uniprotkb/Q7L0R7) · Ensembl [ENSG00000146083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146083)

## Data

Gene col 7061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7061); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7061]; `tensor/DDL_lfc|DDL_z.npy` [7061]; `embed/gene_vectors.npy` [7061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7061 or target_col == 7061). Every well: [[RNF44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
