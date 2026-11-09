---
symbol: "PDCD2L"
type: "gene"
col: 4726
ensembl_id: "ENSG00000126249"
name: "programmed cell death 2 like"
location: "19q13.11"
module: 33
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PDCD2L

*programmed cell death 2 like* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.29× (z +8.1, q 2e-13, up in 29 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.87× (z +6.4, q 5e-08, up in 27 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.0841×, HEC-1-A 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.151×, RKO 0.199×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 0.0685×, NCI-H2030 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS26]] (+0.66, fdr 1e-05), [[SNHG15]] (+0.65, fdr 7e-06), [[C6orf136]] (+0.59, fdr 1e-05); moves opposite to [[IGF2R]] (-0.55, fdr 1e-05), [[M6PR]] (-0.53, fdr 4e-05), [[EIF4EBP2]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +8.1 | 2e-13 | 29/37 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +6.4 | 5e-08 | 27/43 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +5.4 | 1e-05 | 23/43 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.0 | 1e-04 | 19/35 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +4.7 | 3e-04 | 20/46 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +4.6 | 3e-04 | 23/46 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +4.6 | 3e-04 | 18/47 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +4.6 | 3e-04 | 17/47 (HT-29, A498, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.52×** | +4.3 | 0.001 | 19/47 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.002 | 18/46 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.002 | 20/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +3.8 | 0.007 | 13/45 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.43×** | +3.6 | 0.012 | 10/47 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.6 | 0.013 | 6/18 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.5 | 0.020 | 3/48 (HOP62, KATO III, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.023 | 13/46 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.031 | 8/47 (HCT15, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4726.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.0841×, HEC-1-A 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.151×, RKO 0.199×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 0.0685×, NCI-H2030 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.782× | -3.6 | 0.20 | 19/47 (A498, H4, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.808× | -3.1 | 0.54 | 9/47 (HS-578T, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.89× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 5.63 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0440× (z -8.7) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 6.47 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0685× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 7.32 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.100× (z -9.4) |
| [[RKO (line)]] | wt | 9.79 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.282× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -11.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS26]] | +0.66 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SNHG15]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[C6orf136]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MON1A]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PSMG3]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[FXN]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TADA1]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ZNF30]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HDHD5]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SLX9]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2R]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[M6PR]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[EIF4EBP2]] | -0.53 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[TRIP12]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[WSB2]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[SERINC3]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ATP6V1D]] | -0.46 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SPTLC1]] | -0.45 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[CD164]] | -0.45 | -0.36 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.0, -45.7); signed map (-24.6, -18.9). **Vector** length 76.3, 14.2% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +4.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,404,399-34,426,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13096 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRP1](https://www.uniprot.org/uniprotkb/Q9BRP1) (uS5 assembly chaperone PDCD2L):

> May function as a chaperone for ribosomal protein uS5; its function appears redundant to PDCD2.

**Summary**, from NCBI Gene [84306](https://www.ncbi.nlm.nih.gov/gene/84306):

> Predicted to be involved in apoptotic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28194) · Entrez [84306](https://www.ncbi.nlm.nih.gov/gene/84306) · UniProt [Q9BRP1](https://www.uniprot.org/uniprotkb/Q9BRP1) · Ensembl [ENSG00000126249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126249)

## Data

Gene col 4726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4726); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4726]; `tensor/DDL_lfc|DDL_z.npy` [4726]; `embed/gene_vectors.npy` [4726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4726 or target_col == 4726). Every well: [[PDCD2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
