---
symbol: "MTFMT"
type: "gene"
col: 2392
ensembl_id: "ENSG00000103707"
name: "mitochondrial methionyl-tRNA formyltransferase"
location: "15q22.31"
module: 198
arm: "+"
pooled_cpm: 18.96
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# MTFMT

*mitochondrial methionyl-tRNA formyltransferase* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.30× (z +14.2, q 6e-43, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.701× (z -6.1, q 8e-07, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD3]] (+0.70, fdr 7e-06), [[FBXL4]] (+0.66, fdr 1e-05), [[DENND10]] (+0.65, fdr 7e-06); moves opposite to [[PITRM1-AS1]] (-0.59, fdr 1e-05), [[ETF1]] (-0.58, fdr 2e-05), [[CCDC144CP]] (-0.58, fdr 2e-04).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +14.2 | 6e-43 | 44/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +12.1 | 2e-31 | 36/47 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +11.6 | 5e-29 | 37/44 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +11.3 | 2e-27 | 41/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.4 | 2e-11 | 25/47 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +7.0 | 2e-10 | 27/48 (NCI-H1573, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.9 | 4e-07 | 27/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 16/48 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.33×** | +4.9 | 7e-05 | 20/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +4.5 | 4e-04 | 18/47 (NCI-H23, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.5 | 4e-04 | 14/48 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 6e-04 | 14/44 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +4.3 | 8e-04 | 16/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +4.2 | 9e-04 | 18/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.2 | 1e-03 | 12/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.006 | 12/48 (A-427, HOP62, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.010 | 9/47 (J82, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.026 | 9/47 (KATO III, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.030 | 7/46 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -6.1 | 8e-07 | 22/47 (SHP-77, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.584×** | -4.8 | 4e-04 | 22/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.780×** | -4.1 | 0.007 | 19/46 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.788×** | -4.1 | 0.007 | 16/39 (Panc 03.27, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.012 | 18/45 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.697× | -3.2 | 0.12 | 17/46 (A-172, SNU-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.288× (z -9.0) |
| [[A498 (line)]] | wt | 12.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.59× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -12.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.6) |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0702× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 21.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 18.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD3]] | +0.70 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[FBXL4]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[DENND10]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TAB1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | STRING 419 |
| [[TRIM13]] | +0.65 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ZNF786]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TATDN3]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ANGEL1]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.61 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[CDAN1]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITRM1-AS1]] | -0.59 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ETF1]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[CCDC144CP]] | -0.58 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[PPP1R10]] | -0.54 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[C5AR1]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MYH15]] | -0.53 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[MPP4]] | -0.53 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[PHEX]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[HPX]] | -0.53 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[SYAP1]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HAPSTR1]] | -0.52 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[C19orf38]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.3, -0.8); signed map (-16.2, -14.3). **Vector** length 78.8, 14.9% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.5 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial methionyl-tRNA formyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,001,512-65,029,639 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FMT1 |
| Reactome | 3 pathways, smallest: Mitochondrial translation initiation; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DP5](https://www.uniprot.org/uniprotkb/Q96DP5) (Methionyl-tRNA formyltransferase, mitochondrial):

> Methionyl-tRNA formyltransferase that formylates methionyl-tRNA in mitochondria and is crucial for translation initiation.

**Summary**, from NCBI Gene [123263](https://www.ncbi.nlm.nih.gov/gene/123263):

> The protein encoded by this nuclear gene localizes to the mitochondrion, where it catalyzes the formylation of methionyl-tRNA. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:29666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29666) · Entrez [123263](https://www.ncbi.nlm.nih.gov/gene/123263) · UniProt [Q96DP5](https://www.uniprot.org/uniprotkb/Q96DP5) · Ensembl [ENSG00000103707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103707)

## Data

Gene col 2392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2392); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2392]; `tensor/DDL_lfc|DDL_z.npy` [2392]; `embed/gene_vectors.npy` [2392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2392 or target_col == 2392). Every well: [[MTFMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTFMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
