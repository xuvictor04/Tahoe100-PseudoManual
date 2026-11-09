---
symbol: "COA7"
type: "gene"
col: 8504
ensembl_id: "ENSG00000162377"
name: "cytochrome c oxidase assembly factor 7"
location: "1p32.3"
module: 1
arm: "+"
pooled_cpm: 8.19
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 6
n_dd_up_clean: 23
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# COA7

*cytochrome c oxidase assembly factor 7* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.42× (z +21.2, q 0e+00, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.671× (z -6.9, q 3e-09, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH4]] (+0.80, fdr 7e-06), [[MGA]] (+0.79, fdr 7e-06), [[RRP15]] (+0.77, fdr 7e-06); moves opposite to [[KDELR1]] (-0.75, fdr 7e-06), [[NARF]] (-0.74, fdr 7e-06), [[DPM1]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.42×** | +21.2 | 0e+00 | 38/44 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.74×** | +19.0 | 0e+00 | 39/41 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.52×** | +18.4 | 0e+00 | 29/31 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.91×** | +17.5 | 0e+00 | 14/15 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.31×** | +14.6 | 0e+00 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +13.9 | 7e-42 | 17/21 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.47×** | +13.7 | 6e-41 | 37/44 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.32×** | +10.2 | 1e-22 | 39/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +8.6 | 5e-16 | 35/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +8.4 | 2e-15 | 31/46 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **2.09×** | +8.3 | 4e-15 | 24/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +8.3 | 4e-15 | 26/36 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +6.3 | 1e-08 | 23/46 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +6.2 | 2e-08 | 23/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +6.2 | 2e-08 | 21/47 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 9e-08 | 22/46 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.20×** | +5.0 | 2e-05 | 12/41 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.03×** | +4.5 | 2e-04 | 13/42 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +4.4 | 3e-04 | 13/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 3e-04 | 14/46 (SW480, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -6.9 | 3e-09 | 26/43 (NCI-H23, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.473×** | -4.8 | 5e-04 | 17/41 (SHP-77, A549, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.792×** | -4.1 | 0.009 | 16/47 (SNU-1, KATO III, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.072 | 14/41 (NCI-H23, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.086 | 16/46 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.827×** | -3.3 | 0.089 | 6/47 (SHP-77, SNU-423, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.0 | 0.19 | 7/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 11.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 9.56 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +16.0) | — |
| [[PANC-1 (line)]] | alt | 11.8 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.37× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 5.67 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 11.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.1) |
| [[SW480 (line)]] | alt | 12.5 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.67× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 6.71 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.18× (z +9.0) | — |
| [[KATO III (line)]] | alt | 6.82 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.58× (z +9.4) | — |
| [[LoVo (line)]] | wt | 10.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.91× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 5.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 9.01 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +9.6) | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0966× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 6.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.87× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 8.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.14× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 5.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +10.6) | — |
| [[A498 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | +0.80 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[MGA]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[RRP15]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[POGK]] | +0.76 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.75 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[NOP14]] | +0.74 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[UTP20]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[RRS1]] | +0.73 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR1]] | -0.75 | -0.75 / -0.71 | both halves | 7e-06 |  |
| [[NARF]] | -0.74 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[DPM1]] | -0.71 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[APAF1]] | -0.71 | -0.73 / -0.64 | both halves | 7e-06 |  |
| [[MED26]] | -0.70 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[ZNF710-AS1]] | -0.69 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.69 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.69 | -0.75 / -0.60 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.68 | -0.73 / -0.65 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.67 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.67 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.67 | -0.70 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.3, -37.1); signed map (0.9, -41.9). **Vector** length 98.6, 22.6% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.52 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +19.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +18.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +10.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +4.5 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.3 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -4.8 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,684,449-52,698,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12439, RESA1; previously C1orf163, SELRC1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BR5](https://www.uniprot.org/uniprotkb/Q96BR5) (Cytochrome c oxidase assembly factor 7):

> Required for assembly of mitochondrial respiratory chain complex I and complex IV.

**Summary**, from NCBI Gene [65260](https://www.ncbi.nlm.nih.gov/gene/65260):

> Enables protein-disulfide reductase activity. Involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrion. Is active in mitochondrial intermembrane space. Implicated in autosomal recessive spinocerebellar ataxia with axonal neuropathy 3. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25716) · Entrez [65260](https://www.ncbi.nlm.nih.gov/gene/65260) · UniProt [Q96BR5](https://www.uniprot.org/uniprotkb/Q96BR5) · Ensembl [ENSG00000162377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162377)

## Data

Gene col 8504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8504); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8504]; `tensor/DDL_lfc|DDL_z.npy` [8504]; `embed/gene_vectors.npy` [8504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8504 or target_col == 8504). Every well: [[COA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
