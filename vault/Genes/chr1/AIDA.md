---
symbol: "AIDA"
type: "gene"
col: 11772
ensembl_id: "ENSG00000186063"
name: "axin interactor, dorsalization associated"
location: "1q41"
module: 25
arm: "+"
pooled_cpm: 38.94
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AIDA

*axin interactor, dorsalization associated* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +13.1, q 2e-36, up in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.9, q 1e-09, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.649× (z -8.9, q 5e-16, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.66, fdr 2e-05), [[IQGAP1]] (+0.66, fdr 7e-06), [[STYX]] (+0.65, fdr 4e-05); moves opposite to [[SMIM26]] (-0.58, fdr 4e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (-0.58, fdr 5e-05), [[ZNF316]] (-0.57, fdr 1e-05), [[ZNF10]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +13.1 | 2e-36 | 42/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +12.6 | 8e-34 | 31/35 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.9 | 1e-09 | 34/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.8 | 1e-09 | 31/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.4 | 2e-08 | 34/48 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.3 | 1e-05 | 27/39 (SHP-77, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.038 | 21/47 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -8.9 | 5e-16 | 31/47 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -5.6 | 6e-06 | 25/46 (SW 900, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.653×** | -4.8 | 3e-04 | 30/47 (hTERT-HPNE, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.012 | 18/48 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.023 | 22/48 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.843× | -3.4 | 0.055 | 17/48 (LoVo, A498, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.745×** | -3.3 | 0.070 | 20/48 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.811×** | -3.3 | 0.070 | 21/48 (A-172, H4, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.755×** | -3.2 | 0.099 | 17/48 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.13 | 10/48 (A-172, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.13 | 15/48 (BT-474, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 89.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.207× (z -15.3) |
| [[A-427 (line)]] | wt | 35.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -14.0) |
| [[J82 (line)]] | alt | 42.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 39.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 61.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.3) |
| [[A549 (line)]] | wt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0887× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 57.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.3) |
| [[C32 (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.7) |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 52.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.8) |
| [[Hs 766T (line)]] | wt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.4) |
| [[KATO III (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 45.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 50.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.5) |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -8.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.66 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[IQGAP1]] | +0.66 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[STYX]] | +0.65 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[ATL3]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[TLN1]] | +0.64 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[VAMP3]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[PGRMC1]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[DR1]] | +0.62 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[MMGT1]] | +0.61 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[TWF1]] | +0.60 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[STRADB]] | +0.60 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[ZMPSTE24]] | +0.59 | +0.29 / +0.67 | both halves | 3e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.58 | -0.41 / -0.60 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | -0.58 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[ZNF316]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZNF10]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[MAP2K7]] | -0.57 | -0.24 / -0.61 | both halves | 5e-04 |  |
| [[MRPL14]] | -0.56 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[LIME1]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RPAIN]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.54 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[ZNF503]] | -0.54 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[MROH6]] | -0.53 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.53 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[PIAS4]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AIDA's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.0, -21.1); signed map (-18.3, -36.3). **Vector** length 119, 32.1% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.7 | +2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -8.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.8 | -4.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.5 | -2.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | axin interactor, dorsalization associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,668,013-222,713,210 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12806; previously C1orf80 |
| Gene groups (HGNC) | C2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BJ3](https://www.uniprot.org/uniprotkb/Q96BJ3) (Axin interactor, dorsalization-associated protein):

> Acts as a ventralizing factor during embryogenesis. Inhibits axin-mediated JNK activation by binding axin and disrupting axin homodimerization. This in turn antagonizes a Wnt/beta-catenin-independent dorsalization pathway activated by AXIN/JNK-signaling (By similarity).

**Summary**, from NCBI Gene [64853](https://www.ncbi.nlm.nih.gov/gene/64853):

> Predicted to enable phosphatidylinositol binding activity. Acts upstream of or within negative regulation of JUN kinase activity. Predicted to be located in cytoplasm. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25761) · Entrez [64853](https://www.ncbi.nlm.nih.gov/gene/64853) · UniProt [Q96BJ3](https://www.uniprot.org/uniprotkb/Q96BJ3) · Ensembl [ENSG00000186063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186063)

## Data

Gene col 11772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11772); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11772]; `tensor/DDL_lfc|DDL_z.npy` [11772]; `embed/gene_vectors.npy` [11772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11772 or target_col == 11772). Every well: [[AIDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
