---
symbol: "MTFR1L"
type: "gene"
col: 3937
ensembl_id: "ENSG00000117640"
name: "mitochondrial fission regulator 1 like"
location: "1p36.11"
module: 25
arm: "+"
pooled_cpm: 10.12
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MTFR1L

*mitochondrial fission regulator 1 like* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +9.2, q 1e-17, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.429× (z -13.4, q 6e-38, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.504× (z -10.8, q 9e-25, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF167]] (+0.65, fdr 1e-05), [[MEN1]] (+0.60, fdr 1e-05), [[SNX17]] (+0.58, fdr 1e-05); moves opposite to [[BTNL9]] (-0.48, fdr 6e-05), [[COX5A]] (-0.45, fdr 3e-04, ⚠ COX5A in the vector space only through flagged drug-doses).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.2 | 1e-17 | 27/44 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.6 | 3e-15 | 13/22 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.1 | 2e-13 | 18/35 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +7.5 | 1e-11 | 24/47 (A-427, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +6.5 | 8e-09 | 21/48 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +4.4 | 8e-04 | 11/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +4.1 | 0.004 | 16/41 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.7 | 0.017 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +3.5 | 0.032 | 11/45 (A498, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.050 | 3/48 (SW1417, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **1.25×** | +3.2 | 0.060 | 9/29 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.10 | 7/41 (Hs 766T, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Procainamide (hydrochloride) (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.11 | 6/46 (J82, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -13.4 | 6e-38 | 32/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.504×** | -10.8 | 9e-25 | 39/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -10.5 | 2e-23 | 35/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.527×** | -10.1 | 8e-22 | 31/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.758×** | -6.2 | 8e-08 | 28/47 (SK-MEL-2, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.685×** | -6.0 | 2e-07 | 23/47 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -5.6 | 2e-06 | 16/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.755×** | -4.4 | 7e-04 | 15/43 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -4.3 | 0.001 | 19/40 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.780×** | -3.9 | 0.005 | 10/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.787×** | -3.8 | 0.009 | 10/47 (SW 1271, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.731×** | -3.5 | 0.021 | 9/48 (PANC-1, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.061 | 7/44 (SW480, COLO 205, …) | top dose only |  |
| [[Orlistat (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.065 | 10/43 (LS 180, NCI-H2030, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.826× | -3.0 | 0.10 | 9/47 (HT-29, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.21 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.158× (z -13.7) |
| [[BT-474 (line)]] | alt | 7.31 | 0 | 3 | — | [[Talc (drug)]] 0.05 µM 0.0665× (z -10.6) |
| [[LoVo (line)]] | wt | 8.60 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0595× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 2 | — | [[PF-06260933 (drug)]] 5 µM 0.0553× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 8.52 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0685× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.266× (z -9.0) |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.198× (z -8.6) |
| [[COLO 205 (line)]] | alt | 9.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0339× (z -12.9) |
| [[H4 (line)]] | wt | 9.50 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0792× (z -8.8) |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.165× (z -8.7) |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -8.7) ⚠ cell-cycle shift, explains ~99% of this change |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SNU-423 (line)]] | alt | 8.99 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.104× (z -11.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 9.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0689× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF167]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[MEN1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SNX17]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[MAGED2]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TINF2]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[PEX19]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[RRAGA]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[MDH1]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[GTF3C1]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.55 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[COPS6]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTNL9]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[COX5A]] ⚠ | -0.45 | -0.44 / -0.28 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.6, -22.9); signed map (-16.5, -30.0). **Vector** length 52.8, 6.59% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +4.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -10.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -10.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.1 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial fission regulator 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,818,640-25,832,942 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM54B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H019](https://www.uniprot.org/uniprotkb/Q9H019) (Mitochondrial fission regulator 1-like):

> Mitochondrial protein required for adaptation of mitochondrial dynamics to metabolic changes. Regulates mitochondrial morphology at steady state and mediates AMPK-dependent stress-induced mitochondrial fragmentation via the control of OPA1 levels.

**Summary**, from NCBI Gene [56181](https://www.ncbi.nlm.nih.gov/gene/56181):

> Predicted to be involved in aerobic respiration and mitochondrial fission. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28836) · Entrez [56181](https://www.ncbi.nlm.nih.gov/gene/56181) · UniProt [Q9H019](https://www.uniprot.org/uniprotkb/Q9H019) · Ensembl [ENSG00000117640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117640)

## Data

Gene col 3937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3937); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3937]; `tensor/DDL_lfc|DDL_z.npy` [3937]; `embed/gene_vectors.npy` [3937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3937 or target_col == 3937). Every well: [[MTFR1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTFR1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
