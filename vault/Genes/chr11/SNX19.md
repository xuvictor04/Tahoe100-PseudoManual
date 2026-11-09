---
symbol: "SNX19"
type: "gene"
col: 4184
ensembl_id: "ENSG00000120451"
name: "sorting nexin 19"
location: "11q24.3-q25"
module: 5
arm: "+"
pooled_cpm: 30.62
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SNX19

*sorting nexin 19* — 11q24.3-q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.98× (z +8.4, q 2e-14, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.578× (z -6.8, q 6e-09, down in 27 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 0.749× (z -3.6, q 0.097, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 7 lines (PANC-1 0.250×, LoVo 0.269×, NCI-H460 0.241×, SW1417 0.318×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.264×, NCI-H460 0.259×; ⚠ toxic; cell-cycle shift, explains ~12% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0734×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0573×); [[Resveratrol (drug)]] 0.05 µM in 1 line (CHP-212 0.0597×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAP1]] (+0.69, fdr 7e-06), [[ANKRD40]] (+0.68, fdr 7e-06), [[SLC35F6]] (+0.68, fdr 7e-06); moves opposite to [[AFMID]] (-0.70, fdr 7e-06), [[SRP54-AS1]] (-0.68, fdr 7e-06), [[LMBR1L]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +8.4 | 2e-14 | 36/46 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.9 | 9e-13 | 26/34 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +6.6 | 7e-09 | 34/46 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.0 | 3e-07 | 29/42 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +6.0 | 3e-07 | 26/45 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.9 | 3e-07 | 32/46 (A498, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.5 | 3e-06 | 27/45 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.0 | 4e-05 | 22/37 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 9e-04 | 23/46 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.002 | 21/46 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 22/46 (NCI-H2030, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 26/46 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 24/46 (HOP62, HCT15, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +3.6 | 0.013 | 21/46 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.020 | 17/46 (A498, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.020 | 13/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.027 | 20/45 (A498, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.037 | 18/45 (A498, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 7 lines (PANC-1 0.250×, LoVo 0.269×, NCI-H460 0.241×, SW1417 0.318×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.264×, NCI-H460 0.259×; ⚠ toxic; cell-cycle shift, explains ~12% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0734×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0573×); [[Resveratrol (drug)]] 0.05 µM in 1 line (CHP-212 0.0597×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -6.8 | 6e-09 | 27/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.097 | 18/46 (RPMI-7951, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 2 | — | [[Resveratrol (drug)]] 0.05 µM 0.0597× (z -10.7) |
| [[LoVo (line)]] | wt | 38.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -10.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 49.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -13.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.108× (z -9.0) |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0573× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 19.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 16.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0734× (z -11.9) |
| [[J82 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.264× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[RKO (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 1 | — | [[Tranilast (drug)]] 0.05 µM 0.0776× (z -8.5) |
| [[SW1417 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.318× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAP1]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD40]] | +0.68 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[SLC35F6]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[DPP8]] | +0.67 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[TRIM44]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PPP2CA]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ZNF518B]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PURB]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFMID]] | -0.70 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.68 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[LMBR1L]] | -0.66 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[NRTN]] | -0.63 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.61 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[RFX2]] | -0.61 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ANKRD37]] | -0.61 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.61 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[PLEKHH3]] | -0.60 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[TESK2]] | -0.60 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ELP2]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.59 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.0, -28.0); signed map (-7.1, -38.8). **Vector** length 103, 27.0% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -6.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3-q25 — chr11:130,866,250-130,916,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0254, CHET8 |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92543](https://www.uniprot.org/uniprotkb/Q92543) (Sorting nexin-19):

> Plays a role in intracellular vesicle trafficking and exocytosis. May play a role in maintaining insulin-containing dense core vesicles in pancreatic beta-cells and in preventing their degradation. May play a role in insulin secretion. Interacts with membranes containing phosphatidylinositol 3-phosphate (PtdIns(3P)) (By similarity).

**Summary**, from NCBI Gene [399979](https://www.ncbi.nlm.nih.gov/gene/399979):

> Islet antigen-2 (IA-2) is an autoantigen in type 1 diabetes and plays a role in insulin secretion. IA-2 is found in dense-core secretory vesicles and interacts with the product of this gene, a sorting nexin. In mouse pancreatic beta-cells, the encoded protein influenced insulin secretion by stabilizing the number of dense-core secretory vesicles. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:21532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21532) · Entrez [399979](https://www.ncbi.nlm.nih.gov/gene/399979) · UniProt [Q92543](https://www.uniprot.org/uniprotkb/Q92543) · Ensembl [ENSG00000120451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120451)

## Data

Gene col 4184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4184); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4184]; `tensor/DDL_lfc|DDL_z.npy` [4184]; `embed/gene_vectors.npy` [4184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4184 or target_col == 4184). Every well: [[SNX19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
