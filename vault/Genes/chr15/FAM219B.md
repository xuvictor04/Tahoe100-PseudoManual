---
symbol: "FAM219B"
type: "gene"
col: 10957
ensembl_id: "ENSG00000178761"
name: "family with sequence similarity 219 member B"
location: "15q24.1-q24.2"
module: 221
arm: "+"
pooled_cpm: 12.28
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 12
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# FAM219B

*family with sequence similarity 219 member B* — 15q24.1-q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.67× (z +7.4, q 7e-11, up in 29 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Lopinavir (drug)]] 5 µM: 1.38× (z +4.9, q 1e-04, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.315× (z -9.2, q 2e-17, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCBP4]] (+0.64, fdr 7e-06), [[FAHD2A]] (+0.62, fdr 1e-05), [[ULK3]] (+0.62, fdr 1e-05); moves opposite to [[HES1]] (-0.51, fdr 3e-05), [[SMARCA5]] (-0.50, fdr 3e-05), [[EID1]] (-0.49, fdr 3e-05).
> It is in [[Module 221]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +7.4 | 7e-11 | 29/40 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +5.4 | 2e-05 | 20/48 (A498, CFPAC-1, …) | rises with dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.2 | 5e-05 | 16/38 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +5.0 | 9e-05 | 17/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Lopinavir (drug)]] 5 µM |  | **1.38×** | +4.9 | 1e-04 | 16/47 (RKO, A549, …) | top dose only | position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 0.001 | 12/44 (LoVo, NCI-H460, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.1 | 0.004 | 10/25 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.005 | 10/47 (HOP62, LS 180, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.005 | 11/28 (LS 180, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.8 | 0.007 | 8/29 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.018 | 8/43 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.018 | 10/43 (KATO III, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.018 | 7/47 (Hs 766T, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.028 | 3/47 (A-427, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.040 | 7/46 (NCI-H460, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.043 | 8/43 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.048 | 7/43 (HS-578T, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.052 | 13/44 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.052 | 9/47 (HEC-1-A, KATO III, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.052 | 8/47 (NCI-H23, LoVo, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.053 | 6/43 (Hs 766T, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.058 | 9/47 (RKO, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.315×** | -9.2 | 2e-17 | 35/48 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.659×** | -9.0 | 8e-17 | 33/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.550×** | -8.8 | 3e-16 | 31/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.563×** | -8.7 | 3e-16 | 32/47 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -7.8 | 7e-13 | 30/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.602×** | -7.7 | 1e-12 | 28/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -6.2 | 4e-08 | 23/44 (A549, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -5.0 | 4e-05 | 21/45 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.767×** | -4.0 | 0.003 | 14/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -3.8 | 0.010 | 10/46 (KATO III, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -3.7 | 0.013 | 15/48 (Hs 766T, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.793×** | -3.6 | 0.018 | 12/45 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.665×** | -3.2 | 0.051 | 8/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.0) |
| [[SNU-423 (line)]] | alt | 8.31 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.2) |
| [[A549 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.9) |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.2) |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0997× (z -8.6) ⚠ toxic |
| [[C32 (line)]] | wt | 6.53 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0572× (z -9.8) |
| [[H4 (line)]] | wt | 13.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.113× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.9) |
| [[SW 900 (line)]] | alt | 9.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -9.8) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP4]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[FAHD2A]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ULK3]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 | STRING 569 |
| [[MORN4]] | +0.61 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ZDHHC24]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[DHRS1]] | +0.61 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SNHG1]] | +0.59 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[UCKL1]] | +0.59 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PAQR3]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.58 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[NAPB]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[UBE2Q2P1]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SMARCA5]] | -0.50 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[EID1]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CSNK1A1]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[THRAP3]] | -0.47 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[XRN1]] | -0.46 | -0.54 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.5, -10.5); signed map (-24.9, -1.1). **Vector** length 71.6, 12.1% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -1.2 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 219 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1-q24.2 — chr15:74,899,992-74,906,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00005; previously C15orf17 |
| Matched by | ensembl_id |

UniProt [Q5XKK7](https://www.uniprot.org/uniprotkb/Q5XKK7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24695) · Entrez [57184](https://www.ncbi.nlm.nih.gov/gene/57184) · UniProt [Q5XKK7](https://www.uniprot.org/uniprotkb/Q5XKK7) · Ensembl [ENSG00000178761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178761)

## Data

Gene col 10957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10957); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10957]; `tensor/DDL_lfc|DDL_z.npy` [10957]; `embed/gene_vectors.npy` [10957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10957 or target_col == 10957). Every well: [[FAM219B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM219B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
