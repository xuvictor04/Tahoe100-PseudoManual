---
symbol: "HIP1R"
type: "gene"
col: 5128
ensembl_id: "ENSG00000130787"
name: "huntingtin interacting protein 1 related"
location: "12q24.31"
module: 97
arm: "+"
pooled_cpm: 16.05
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# HIP1R

*huntingtin interacting protein 1 related* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +15.3, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.928× (z -4.5, q 0.004, down in 3 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.769× (z -4.3, q 0.004, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0673×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.208×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP1A1]] (+0.61, fdr 1e-05), [[TEAD3]] (+0.61, fdr 1e-05), [[NCOR2]] (+0.60, fdr 1e-05); moves opposite to [[TOGARAM1]] (-0.50, fdr 3e-05), [[GORAB]] (-0.49, fdr 1e-04), [[HELQ]] (-0.48, fdr 8e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +15.3 | 0e+00 | 38/46 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +13.8 | 5e-41 | 38/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +13.8 | 5e-41 | 42/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +13.6 | 7e-40 | 42/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +11.5 | 1e-28 | 40/48 (HOP62, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +11.4 | 5e-28 | 40/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +11.2 | 5e-27 | 36/47 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +10.0 | 2e-21 | 37/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +7.9 | 1e-13 | 30/46 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.39×** | +7.5 | 3e-12 | 31/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +6.5 | 4e-09 | 24/46 (NCI-H460, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +6.1 | 4e-08 | 21/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.8 | 3e-07 | 22/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.6 | 2e-04 | 14/44 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.29×** | +4.3 | 8e-04 | 13/47 (COLO 205, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.016 | 16/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.024 | 12/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +3.2 | 0.037 | 9/47 (NCI-H2347, A549, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.047 | 10/48 (SW 900, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5128.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0673×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.208×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.5 | 0.004 | 3/48 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.3 | 0.004 | 15/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.7 | 0.047 | 17/47 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.740×** | -3.6 | 0.053 | 7/44 (SHP-77, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 0.816× | -3.2 | 0.13 | 9/46 (A498, HCT15, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.774× | -3.0 | 0.23 | 10/45 (SW48, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.2 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.71× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +10.0) | — |
| [[LoVo (line)]] | wt | 24.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.1) | — |
| [[A-172 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 7.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.56× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0673× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TEAD3]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[NCOR2]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ADAM15]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GPC1]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[CDC42BPB]] | +0.54 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[ASAP3]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SORT1]] | +0.53 | +0.54 / +0.60 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis; STRING 514 |
| [[ABHD12]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[STK24]] | +0.53 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[TMEM164]] | +0.52 | +0.58 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOGARAM1]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GORAB]] | -0.49 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[HELQ]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[SPEF2]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[OSCP1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[GOSR1]] | -0.45 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[HMGXB4]] | -0.45 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[DNTTIP1]] | -0.45 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MRPS33]] | -0.45 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[CPT2]] | -0.45 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[ZNF140]] | -0.45 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[DCP1A]] | -0.45 | -0.34 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.8, -2.0); signed map (-12.1, 29.5). **Vector** length 75.7, 13.8% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.7 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.6 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +7.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.1 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | huntingtin interacting protein 1 related |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,834,453-122,862,961 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0655, HIP3, HIP12, FLJ14000, ILWEQ |
| Reactome | 5 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75146](https://www.uniprot.org/uniprotkb/O75146) (Huntingtin-interacting protein 1-related protein):

> Component of clathrin-coated pits and vesicles, that may link the endocytic machinery to the actin cytoskeleton. Binds 3-phosphoinositides (via ENTH domain). May act through the ENTH domain to promote cell survival by stabilizing receptor tyrosine kinases following ligand-induced endocytosis.

**Summary**, from NCBI Gene [9026](https://www.ncbi.nlm.nih.gov/gene/9026):

> Enables several functions, including actin filament binding activity; anion binding activity; and protein homodimerization activity. Involved in several processes, including positive regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway; positive regulation of signal transduction; and protein stabilization. Located in clathrin-coated vesicle; cytosol; and ruffle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18415) · Entrez [9026](https://www.ncbi.nlm.nih.gov/gene/9026) · UniProt [O75146](https://www.uniprot.org/uniprotkb/O75146) · Ensembl [ENSG00000130787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130787)

## Data

Gene col 5128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5128); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5128]; `tensor/DDL_lfc|DDL_z.npy` [5128]; `embed/gene_vectors.npy` [5128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5128 or target_col == 5128). Every well: [[HIP1R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIP1R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
