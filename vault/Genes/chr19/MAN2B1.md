---
symbol: "MAN2B1"
type: "gene"
col: 2496
ensembl_id: "ENSG00000104774"
name: "mannosidase alpha class 2B member 1"
location: "19p13.13"
module: 4
arm: "-"
pooled_cpm: 18.58
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MAN2B1

*mannosidase alpha class 2B member 1* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.73× (z +18.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.785× (z -4.5, q 0.004, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[XRK3F2 (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0634×); [[Docetaxel (drug)]] 0.05 µM in 1 line (HCT15 0.0807×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1792 0.288×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRY2]] (+0.60, fdr 7e-06), [[TMEM63B]] (+0.52, fdr 2e-05), [[UNKL]] (+0.51, fdr 3e-05); moves opposite to [[GNL3]] (-0.50, fdr 3e-05), [[MGA]] (-0.47, fdr 1e-04), [[KAT14]] (-0.47, fdr 4e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.73×** | +18.6 | 0e+00 | 45/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.50×** | +16.1 | 0e+00 | 47/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +15.9 | 0e+00 | 41/46 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +14.5 | 3e-45 | 43/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +14.1 | 3e-43 | 42/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +13.9 | 9e-42 | 39/48 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +13.7 | 7e-41 | 34/46 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.09×** | +13.7 | 7e-41 | 44/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +12.9 | 2e-36 | 43/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.57×** | +8.1 | 3e-14 | 23/30 (LoVo, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +7.7 | 7e-13 | 29/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.49×** | +7.4 | 4e-12 | 27/41 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.52×** | +7.2 | 2e-11 | 24/36 (SW480, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +6.7 | 7e-10 | 29/47 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.3 | 1e-08 | 24/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 1e-07 | 21/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.006 | 3/48 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.022 | 7/45 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.096 | 9/45 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2496.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[XRK3F2 (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0634×); [[Docetaxel (drug)]] 0.05 µM in 1 line (HCT15 0.0807×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1792 0.288×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -4.5 | 0.004 | 18/48 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.849× | -4.3 | 0.005 | 15/48 (SW 1088, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.9 | 0.019 | 16/47 (SNU-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.820×** | -3.7 | 0.034 | 20/46 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.827×** | -3.4 | 0.080 | 15/45 (AN3 CA, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.2 | 0.14 | 0/48 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.844× | -3.0 | 0.20 | 8/47 (A-172, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 29.9 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.2) | — |
| [[SW480 (line)]] | alt | 15.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 17.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +27.1) | — |
| [[A-172 (line)]] | wt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 19.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.77× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.56× (z +11.5) | — |
| [[A498 (line)]] | wt | 19.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.94× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 28.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.6) | — |
| [[A549 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0807× (z -12.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.4) | — |
| [[J82 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 18.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.04× (z +9.8) | — |
| [[RKO (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0634× (z -12.5) |
| [[SW48 (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.8) | — |
| [[A-427 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRY2]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TMEM63B]] | +0.52 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[UNKL]] | +0.51 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ACOX1]] | +0.50 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[BBS1]] | +0.50 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[DDA1]] | +0.49 | +0.53 / +0.37 | both halves | 7e-05 |  |
| [[SAMD4B]] | +0.49 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[MAP2K2]] | +0.48 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[FLYWCH1]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[HELB]] | +0.48 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[UBE4B]] | +0.48 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[PSMD8]] | +0.48 | +0.49 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3]] | -0.50 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MGA]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[KAT14]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[HERPUD2-AS1]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[PRPF4]] | -0.46 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[RAB4A-AS1]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[FAM120C]] | -0.45 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[DKC1]] | -0.45 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[POLR1G]] | -0.45 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DMAC1]] | -0.44 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[TFAM]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[SERBP1]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.234). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (7.9, -50.3); signed map (-9.8, 10.6). **Vector** length 83.9, 17.4% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +16.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +18.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.7 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.1 | +7.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 2B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,646,511-12,666,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAMAN; previously MANB |
| Gene groups (HGNC) | Mannosidases alpha class 2 |
| Reactome | 4 pathways, smallest: Lysosomal oligosaccharide catabolism; Metabolism of carbohydrates and carbohydrate derivatives; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00754](https://www.uniprot.org/uniprotkb/O00754) (Lysosomal alpha-mannosidase):

> Can hydrolyze a variety of glycan substrates containing terminal alpha-mannosidic linkages. Cleaves alpha 1,2-, alpha 1,3-, and alpha 1,6-linked mannose residues on oligosaccharides generated by N-glycoprotein degradation pathways.

**Summary**, from NCBI Gene [4125](https://www.ncbi.nlm.nih.gov/gene/4125):

> This gene encodes an enzyme that hydrolyzes terminal, non-reducing alpha-D-mannose residues in alpha-D-mannosides. Its activity is necessary for the catabolism of N-linked carbohydrates released during glycoprotein turnover and it is member of family 38 of glycosyl hydrolases. The full length protein is processed in two steps. First, a 49 aa leader sequence is cleaved off and the remainder of the protein is processed into 3 peptides of 70 kDa, 42 kDa (D) and 13/15 kDa (E). Next, the 70 kDa …

**Accessions** — [HGNC:6826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6826) · Entrez [4125](https://www.ncbi.nlm.nih.gov/gene/4125) · UniProt [O00754](https://www.uniprot.org/uniprotkb/O00754) · Ensembl [ENSG00000104774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104774)

## Data

Gene col 2496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2496); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2496]; `tensor/DDL_lfc|DDL_z.npy` [2496]; `embed/gene_vectors.npy` [2496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2496 or target_col == 2496). Every well: [[MAN2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
