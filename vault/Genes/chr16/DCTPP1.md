---
symbol: "DCTPP1"
type: "gene"
col: 11071
ensembl_id: "ENSG00000179958"
name: "dCTP pyrophosphatase 1"
location: "16p11.2"
module: 33
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# DCTPP1

*dCTP pyrophosphatase 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +7.5, q 4e-11, up in 21 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.14× (z +5.7, q 1e-06, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.478× (z -7.9, q 2e-12, down in 32 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.139×, RKO 0.148×, SW480 0.231×, LoVo 0.183×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL4]] (+0.74, fdr 7e-06), [[ALDH1B1]] (+0.72, fdr 7e-06), [[MRPL12]] (+0.71, fdr 1e-05); moves opposite to [[GNAS]] (-0.63, fdr 2e-05), [[KMT2E-AS1]] (-0.59, fdr 1e-04), [[LHFPL3]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.69×** | +7.5 | 4e-11 | 21/28 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.77×** | +7.4 | 4e-11 | 6/9 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.42×** | +6.7 | 4e-09 | 35/46 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.30×** | +6.3 | 5e-08 | 31/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.14×** | +5.7 | 1e-06 | 27/45 (A549, J82, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **2.08×** | +5.3 | 1e-05 | 22/33 (A549, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.11×** | +5.2 | 2e-05 | 11/16 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.92×** | +4.9 | 6e-05 | 31/46 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.5 | 5e-04 | 24/34 (J82, SHP-77, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +4.4 | 6e-04 | 23/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.35×** | +4.0 | 0.004 | 14/39 (NCI-H460, PANC-1, …) | all doses, flat | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.9 | 0.005 | 11/48 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.54×** | +3.6 | 0.015 | 13/38 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +3.4 | 0.023 | 5/31 (MIA PaCa-2, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +3.3 | 0.036 | 11/42 (J82, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.22×** | +3.1 | 0.066 | 6/37 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.066 | 14/46 (PANC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.21×** | +3.0 | 0.066 | 4/42 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.069 | 12/46 (MIA PaCa-2, PANC-1, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.90×** | +3.0 | 0.073 | 3/40 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.17×** | +3.0 | 0.074 | 5/35 (J82, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.093 | 4/40 (RKO, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11071.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.139×, RKO 0.148×, SW480 0.231×, LoVo 0.183×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.478×** | -7.9 | 2e-12 | 32/42 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.652× | -3.2 | 0.28 | 7/47 (SK-MEL-2, SW48, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.439× | -3.2 | 0.28 | 19/43 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.2) |
| [[LoVo (line)]] | wt | 5.73 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.0) |
| [[RKO (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.5) |
| [[SW480 (line)]] | alt | 9.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.3) |
| [[A-172 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL4]] | +0.74 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ALDH1B1]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MRPL12]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[POLR3K]] | +0.69 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[C20orf27]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[PHB1]] | +0.67 | +0.71 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[HAUS7]] | +0.67 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CISD3]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[RPP40]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SLC39A3]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.63 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[KMT2E-AS1]] | -0.59 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[LHFPL3]] | -0.58 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[USP34-DT]] | -0.58 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.57 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[C12orf57]] | -0.57 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CROCC]] | -0.56 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[CHD3]] | -0.55 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[C12orf73]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[FAM120AOS]] | -0.55 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[RYR2]] | -0.54 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CYB5D2]] | -0.54 | -0.37 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.3, -42.3); signed map (-11.0, -53.1). **Vector** length 68.1, 14.0% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +3.8 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.4 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.3 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.2 | -0.3 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dCTP pyrophosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,423,615-30,430,030 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5627, RS21C6, CDA03, XTP3TPA |
| Hallmark sets | MYC_TARGETS_V2, E2F_TARGETS |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H773](https://www.uniprot.org/uniprotkb/Q9H773) (dCTP pyrophosphatase 1):

> Hydrolyzes deoxynucleoside triphosphates (dNTPs) to the corresponding nucleoside monophosphates. Has a strong preference for dCTP and its analogs including 5-iodo-dCTP and 5-methyl-dCTP for which it may even have a higher efficiency. May protect DNA or RNA against the incorporation of these genotoxic nucleotide analogs through their catabolism.

**Summary**, from NCBI Gene [79077](https://www.ncbi.nlm.nih.gov/gene/79077):

> The protein encoded by this gene is dCTP pyrophosphatase, which converts dCTP to dCMP and inorganic pyrophosphate. The encoded protein also displays weak activity against dTTP and dATP, but none against dGTP. This protein may be responsible for eliminating excess dCTP after DNA synthesis and may prevent overmethylation of CpG islands. Three transcript variants, one protein-coding and the other two non-protein coding, have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:28777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28777) · Entrez [79077](https://www.ncbi.nlm.nih.gov/gene/79077) · UniProt [Q9H773](https://www.uniprot.org/uniprotkb/Q9H773) · Ensembl [ENSG00000179958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179958)

## Data

Gene col 11071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11071); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11071]; `tensor/DDL_lfc|DDL_z.npy` [11071]; `embed/gene_vectors.npy` [11071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11071 or target_col == 11071). Every well: [[DCTPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
