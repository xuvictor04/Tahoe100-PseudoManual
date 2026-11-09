---
symbol: "SLF2"
type: "gene"
col: 4133
ensembl_id: "ENSG00000119906"
name: "SMC5/6 complex localization factor 2"
location: "10q24.31"
module: 57
arm: "-"
pooled_cpm: 85.0
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# SLF2

*SMC5/6 complex localization factor 2* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.53× (z +8.0, q 8e-13, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.289× (z -11.4, q 1e-27, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNTA]] (+0.60, fdr 1e-05), [[XIAP]] (+0.54, fdr 6e-05), [[NSL1]] (+0.51, fdr 1e-05); moves opposite to [[TANC1]] (-0.52, fdr 3e-05), [[ARSA]] (-0.50, fdr 5e-05), [[GALNT16]] (-0.48, fdr 8e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +8.0 | 8e-13 | 39/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +6.2 | 2e-07 | 31/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 8e-06 | 25/48 (BT-474, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.003 | 24/47 (HepG2/C3A, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.005 | 23/47 (RPMI-7951, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.005 | 23/48 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.027 | 18/48 (KATO III, H4, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.038 | 17/49 (A-172, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.289×** | -11.4 | 1e-27 | 47/49 (HOP62, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.324×** | -10.4 | 9e-23 | 45/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.648×** | -8.2 | 5e-14 | 38/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.651×** | -8.1 | 9e-14 | 40/48 (J82, A-172, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.702×** | -6.3 | 3e-08 | 32/48 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -5.9 | 4e-07 | 29/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -5.8 | 5e-07 | 26/47 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.5 | 4e-06 | 23/49 (SNU-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.588×** | -4.9 | 6e-05 | 21/37 (HOP62, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.767×** | -4.6 | 2e-04 | 28/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.5 | 4e-04 | 18/48 (A-427, PANC-1, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.808×** | -4.0 | 0.003 | 23/48 (Panc 03.27, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.656×** | -3.9 | 0.004 | 25/45 (SNU-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.808×** | -3.7 | 0.009 | 22/45 (A-172, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.827×** | -3.6 | 0.014 | 20/49 (NCI-H1792, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.014 | 20/49 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.050 | 22/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.0 | 0.075 | 12/49 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 119 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.263× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 191 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.6) |
| [[HOP62 (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.151× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 99.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.424× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 93.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.183× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 96.6 | 0 | 3 | — | [[PH-797804 (drug)]] 5 µM 0.126× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 93.8 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0912× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 88.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.420× (z -8.9) |
| [[SNU-1 (line)]] | wt | 61.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.9) |
| [[A-172 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[A-427 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.574× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 83.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 52.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 94.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[HCT15 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[hTERT-HPNE (line)]] | wt | 87.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.349× (z -9.0) |
| [[J82 (line)]] | alt | 59.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.339× (z -10.7) |
| [[KATO III (line)]] | alt | 51.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.426× (z -8.7) |
| [[LS 180 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 91.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 177 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.229× (z -8.6) |
| [[SW 1088 (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0856× (z -8.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 133 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 92.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 78.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNTA]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[XIAP]] | +0.54 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[NSL1]] | +0.51 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.50 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[THAP1]] | +0.50 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[FKBP15]] | +0.50 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[CEP135]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ST7L]] | +0.49 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ERCC6L2]] | +0.49 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[ZNF638]] | +0.49 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[CSTF3-DT]] | +0.49 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[BRCA2]] | +0.49 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANC1]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ARSA]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[GALNT16]] | -0.48 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[EIF3H]] | -0.48 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[PBXIP1]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ADA]] | -0.47 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[CASZ1]] | -0.47 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[TIMP2]] | -0.47 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[RAB6B]] | -0.46 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[SMG1P2]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[MMP15]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[NPDC1]] | -0.45 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.293). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-49.0, -39.3); signed map (4.0, -13.1). **Vector** length 126, 38.4% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.3 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.2 | +6.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +1.3 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -7.5 | -10.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.9 | -8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | SMC5/6 complex localization factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,912,963-100,965,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10512, FLJ25012, hNSE6; previously C10orf6, FAM178A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX21](https://www.uniprot.org/uniprotkb/Q8IX21) (SMC5-SMC6 complex localization factor protein 2):

> Plays a role in the DNA damage response (DDR) pathway by regulating postreplication repair of UV-damaged DNA and genomic stability maintenance. The SLF1-SLF2 complex acts to link RAD18 with the SMC5-SMC6 complex at replication-coupled interstrand cross-links (ICL) and DNA double-strand breaks (DSBs) sites on chromatin during DNA repair in response to stalled replication forks. Promotes the recruitment of the SMC5-SMC6 complex to DNA lesions. Plays a role in SMC5-SMC6 complex recruitment for …

**Summary**, from NCBI Gene [55719](https://www.ncbi.nlm.nih.gov/gene/55719):

> Enables ubiquitin protein ligase binding activity. Involved in several processes, including positive regulation of cellular component organization; positive regulation of double-strand break repair; and protein localization to site of double-strand break. Located in PML body; chromatin; and site of double-strand break. Implicated in mosaic variegated aneuploidy syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17814) · Entrez [55719](https://www.ncbi.nlm.nih.gov/gene/55719) · UniProt [Q8IX21](https://www.uniprot.org/uniprotkb/Q8IX21) · Ensembl [ENSG00000119906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119906)

## Data

Gene col 4133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4133); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4133]; `tensor/DDL_lfc|DDL_z.npy` [4133]; `embed/gene_vectors.npy` [4133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4133 or target_col == 4133). Every well: [[SLF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
