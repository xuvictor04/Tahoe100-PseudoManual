---
symbol: "PNPLA2"
type: "gene"
col: 10847
ensembl_id: "ENSG00000177666"
name: "patatin like domain 2, triacylglycerol lipase"
location: "11p15.5"
module: 69
arm: "+"
pooled_cpm: 19.16
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PNPLA2

*patatin like domain 2, triacylglycerol lipase* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +20.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.573× (z -7.5, q 3e-11, down in 30 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.575× (z -5.3, q 3e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC5]] (+0.67, fdr 1e-05), [[LRCH4]] (+0.67, fdr 7e-06), [[NATD1]] (+0.63, fdr 7e-06); moves opposite to [[PA2G4]] (-0.56, fdr 2e-05), [[TIMM21]] (-0.54, fdr 5e-05), [[ORC2]] (-0.54, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +20.0 | 0e+00 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +12.5 | 2e-33 | 41/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +11.8 | 4e-30 | 45/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.0 | 2e-21 | 26/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +9.8 | 8e-21 | 28/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +8.8 | 1e-16 | 20/27 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +8.0 | 7e-14 | 30/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +7.4 | 1e-11 | 34/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.2 | 3e-11 | 8/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.7 | 1e-09 | 19/32 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +5.9 | 2e-07 | 24/48 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +5.7 | 5e-07 | 24/43 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 9e-05 | 24/42 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.7 | 1e-04 | 22/46 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 20/48 (RKO, CFPAC-1, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 2e-04 | 24/46 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.023 | 15/46 (RKO, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.023 | 13/44 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.78×** | +3.3 | 0.031 | 11/44 (NCI-H2347, J82, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.035 | 8/46 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.037 | 13/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.573×** | -7.5 | 3e-11 | 30/48 (Hs 766T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.575×** | -5.3 | 3e-05 | 24/48 (HT-29, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.484×** | -4.1 | 0.007 | 19/45 (H4, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.736×** | -3.9 | 0.011 | 17/47 (LoVo, HCT15, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.505×** | -3.9 | 0.011 | 15/44 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.509×** | -3.8 | 0.011 | 15/44 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.549×** | -3.4 | 0.053 | 11/45 (HT-29, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.777×** | -3.2 | 0.089 | 15/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.789× | -3.0 | 0.15 | 10/48 (A549, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.43 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 28.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +22.0) | — |
| [[A-172 (line)]] | wt | 17.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +12.9) | — |
| [[SW480 (line)]] | alt | 17.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 9.70 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +10.5) | — |
| [[RKO (line)]] | wt | 17.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.18× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 39.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.2) | — |
| [[A498 (line)]] | wt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.4) | — |
| [[A549 (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +12.5) | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 9.20 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0906× (z -8.7) |
| [[C32 (line)]] | wt | 8.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +9.7) | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0851× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.8) | — |
| [[J82 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.1) | — |
| [[LoVo (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 5.73 | 0 | 1 | — | [[Trifluridine (drug)]] 0.05 µM 0.0707× (z -9.4) |
| [[SNU-423 (line)]] | alt | 21.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.9) | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[LRCH4]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NATD1]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[DDAH2]] | +0.60 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CTDSP2]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PLXNB2]] | +0.59 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[JUND]] | +0.58 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[SLC9A3R1]] | +0.57 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[GPR108]] | +0.57 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[NUDT14]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TP53INP2]] | +0.56 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[CKB]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PA2G4]] | -0.56 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TIMM21]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ORC2]] | -0.54 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[BCCIP]] | -0.54 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RABEPK]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TSR1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[CDC123]] | -0.53 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[APTX]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PCOLCE2]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[FASTKD1]] | -0.51 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ADAT2]] | -0.51 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[PARGP1]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.1, -36.0); signed map (-6.5, 20.1). **Vector** length 101, 23.7% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +20.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +8.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +5.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.3 | +4.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +1.6 |
|  | [[Alpelisib (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -7.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | patatin like domain 2, triacylglycerol lipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:818,914-825,573 (+) |
| Ensembl biotype | protein_coding |
| Also known as | desnutrin, TTS-2.2, ATGL, FP17548, iPLA2zeta |
| Gene groups (HGNC) | Lipases; Patatin like phospholipase domain containing |
| Reactome | 11 pathways, smallest: Acyl chain remodeling of DAG and TAG; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes; Epigenetic regulation of gene expression by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AD5](https://www.uniprot.org/uniprotkb/Q96AD5) (Patatin-like phospholipase domain-containing protein 2):

> Catalyzes the initial step in triglyceride hydrolysis in adipocyte and non-adipocyte lipid droplets. Exhibits a strong preference for the hydrolysis of long-chain fatty acid esters at the sn-2 position of the glycerol backbone and acts coordinately with LIPE/HLS and DGAT2 within the lipolytic cascade (By similarity). Also possesses acylglycerol transacylase and phospholipase A2 activities. Transfers fatty acid from triglyceride to retinol, hydrolyzes retinylesters, and generates …

**Summary**, from NCBI Gene [57104](https://www.ncbi.nlm.nih.gov/gene/57104):

> This gene encodes an enzyme which catalyzes the first step in the hydrolysis of triglycerides in adipose tissue. Mutations in this gene are associated with neutral lipid storage disease with myopathy. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:30802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30802) · Entrez [57104](https://www.ncbi.nlm.nih.gov/gene/57104) · UniProt [Q96AD5](https://www.uniprot.org/uniprotkb/Q96AD5) · Ensembl [ENSG00000177666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177666)

## Data

Gene col 10847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10847); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10847]; `tensor/DDL_lfc|DDL_z.npy` [10847]; `embed/gene_vectors.npy` [10847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10847 or target_col == 10847). Every well: [[PNPLA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPLA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
