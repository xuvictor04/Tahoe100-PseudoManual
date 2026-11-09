---
symbol: "CRNKL1"
type: "gene"
col: 2119
ensembl_id: "ENSG00000101343"
name: "crooked neck pre-mRNA splicing factor 1"
location: "20p11.23"
module: 7
arm: "+"
pooled_cpm: 38.33
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CRNKL1

*crooked neck pre-mRNA splicing factor 1* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +17.4, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.712× (z -7.6, q 2e-11, down in 34 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.768× (z -5.9, q 1e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IK]] (+0.73, fdr 7e-06), [[ZMAT2]] (+0.70, fdr 7e-06), [[ZNF830]] (+0.67, fdr 7e-06); moves opposite to [[ATP1B3]] (-0.56, fdr 4e-05), [[CORO7]] (-0.54, fdr 2e-05), [[FAM20B]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +17.4 | 0e+00 | 42/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.19×** | +16.7 | 0e+00 | 44/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +12.2 | 5e-32 | 46/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +10.7 | 2e-24 | 35/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.56×** | +9.5 | 3e-19 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.5 | 6e-12 | 35/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.1 | 8e-08 | 26/47 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +5.9 | 2e-07 | 23/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +5.9 | 2e-07 | 26/48 (HEC-1-A, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +5.6 | 1e-06 | 22/48 (A498, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.5 | 2e-06 | 20/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +4.2 | 0.001 | 18/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.20× | +4.1 | 0.002 | 16/48 (A549, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | 1.19× | +3.9 | 0.005 | 18/47 (HOP62, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.015 | 8/48 (COLO 205, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.078 | 12/47 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.078 | 12/47 (PANC-1, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -7.6 | 2e-11 | 34/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -5.9 | 1e-06 | 27/48 (RKO, SNU-423, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -4.0 | 0.011 | 14/48 (A-172, CFPAC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.015 | 17/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.015 | 18/48 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.015 | 12/48 (SW 1271, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.799×** | -3.6 | 0.030 | 11/48 (PANC-1, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -3.4 | 0.038 | 14/47 (NCI-H2347, C-33 A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.038 | 14/48 (SW48, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.4 | 0.038 | 14/48 (SW 1088, NCI-H2347, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.861× | -3.3 | 0.045 | 4/48 (J82, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 55.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.9) | — |
| [[A549 (line)]] | wt | 43.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 45.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 32.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.416× (z -9.0) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 34.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 40.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 43.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +8.5) | — |
| [[KATO III (line)]] | alt | 67.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 36.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.8) | — |
| [[RKO (line)]] | wt | 49.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.10× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.194× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 43.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.163× (z -8.8) |
| [[H4 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[LoVo (line)]] | wt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.53× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.97× (z +8.8) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 31.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.76× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 32.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.60× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 90.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.78× (z +8.5) | — |
| [[A-172 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IK]] | +0.73 | +0.83 / +0.71 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 458 |
| [[ZMAT2]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 914 |
| [[ZNF830]] | +0.67 | +0.78 / +0.60 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 969 |
| [[ASB8]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[RBM22]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[SNW1]] | +0.66 | +0.75 / +0.61 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[FBXO38]] | +0.66 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.65 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[TBCC]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.65 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[PHAX]] | +0.64 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ZNF350]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1B3]] | -0.56 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[CORO7]] | -0.54 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[FAM20B]] | -0.54 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[LIMK1]] | -0.54 | -0.59 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.2, 2.7); signed map (1.3, -17.0). **Vector** length 97.5, 21.7% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +16.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +17.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | crooked neck pre-mRNA splicing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:20,034,368-20,056,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRN, CLF, SYF3, Clf1 |
| Gene groups (HGNC) | Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZJ0](https://www.uniprot.org/uniprotkb/Q9BZJ0) (Crooked neck-like protein 1):

> Involved in pre-mRNA splicing process. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [51340](https://www.ncbi.nlm.nih.gov/gene/51340):

> The crooked neck (crn) gene of Drosophila is essential for embryogenesis and is thought to be involved in cell cycle progression and pre-mRNA splicing. A protein encoded by this human locus has been found to localize to pre-mRNA splicing complexes in the nucleus and is necessary for pre-mRNA splicing. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:15762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15762) · Entrez [51340](https://www.ncbi.nlm.nih.gov/gene/51340) · UniProt [Q9BZJ0](https://www.uniprot.org/uniprotkb/Q9BZJ0) · Ensembl [ENSG00000101343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101343)

## Data

Gene col 2119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2119); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2119]; `tensor/DDL_lfc|DDL_z.npy` [2119]; `embed/gene_vectors.npy` [2119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2119 or target_col == 2119). Every well: [[CRNKL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRNKL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
