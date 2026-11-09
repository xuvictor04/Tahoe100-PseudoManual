---
symbol: "PSTK"
type: "gene"
col: 11074
ensembl_id: "ENSG00000179988"
name: "phosphoseryl-tRNA kinase"
location: "10q26.13"
module: 4
arm: "+"
pooled_cpm: 12.62
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PSTK

*phosphoseryl-tRNA kinase* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.25× (z +13.8, q 2e-40, up in 15 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +5.3, q 3e-05, up in 13 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.575× (z -9.8, q 1e-19, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP6]] (+0.63, fdr 1e-05), [[RBM45]] (+0.57, fdr 2e-05), [[PGGT1B]] (+0.57, fdr 2e-05); moves opposite to [[MTM1]] (-0.48, fdr 1e-04), [[CDKL5]] (-0.47, fdr 1e-04), [[ZNHIT1]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +13.8 | 2e-40 | 15/18 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +10.0 | 5e-21 | 21/37 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.3 | 3e-05 | 13/47 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.004 | 6/39 (SW480, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.1 | 0.004 | 15/39 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.010 | 6/44 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.010 | 7/45 (SW48, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.2 | 0.11 | 4/47 (A-427, NCI-H2347, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 1.40× | +3.1 | 0.11 | 3/41 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.11 | 10/47 (NCI-H2347, KATO III, …) | top dose only | low cells (technical?) |
| [[Saquinavir (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.13 | 6/44 (HOP62, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -9.8 | 1e-19 | 29/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -7.0 | 1e-09 | 24/46 (NCI-H23, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -6.5 | 1e-08 | 22/45 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -5.5 | 6e-06 | 19/43 (SW48, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.735×** | -5.4 | 7e-06 | 16/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.766×** | -4.7 | 3e-04 | 20/46 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.832×** | -4.6 | 4e-04 | 17/45 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.790×** | -4.2 | 0.002 | 15/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.003 | 13/44 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.817×** | -3.6 | 0.020 | 9/46 (H4, NCI-H23, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.817×** | -3.6 | 0.020 | 11/46 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.696×** | -3.3 | 0.037 | 6/47 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.037 | 2/46 (LS 180, Panc 03.27) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.832×** | -3.2 | 0.049 | 9/47 (SW 1088, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.2 | 0.050 | 11/47 (SHP-77, A-427, …) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.881× | -3.1 | 0.059 | 7/47 (A-427, LOX-IMVI, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.069 | 12/45 (SW48, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -17.1) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 21.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -11.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.4) |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.120× (z -10.3) |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0747× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0719× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.246× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP6]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RBM45]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[PGGT1B]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MRPL3]] | +0.57 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DHX9]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SREK1]] | +0.56 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[SAAL1]] | +0.56 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[QDPR]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 | pathway: Metabolism of amino acids and derivatives |
| [[SARS2]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 | STRING 989 |
| [[RAD51D]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[COG2]] | +0.55 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTM1]] | -0.48 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CDKL5]] | -0.47 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ZNHIT1]] | -0.46 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[CLDN7]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.2, 1.2); signed map (11.6, -39.4). **Vector** length 56.6, 7.46% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.3 | -3.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphoseryl-tRNA kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,954,381-122,997,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35392; previously C10orf89 |
| Gene groups (HGNC) | RNA kinases |
| Reactome | 3 pathways, smallest: Selenocysteine synthesis; Selenoamino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV42](https://www.uniprot.org/uniprotkb/Q8IV42) (L-seryl-tRNA(Sec) kinase):

> Specifically phosphorylates seryl-tRNA(Sec) to O-phosphoseryl-tRNA(Sec), an activated intermediate for selenocysteine biosynthesis. No activity with other tRNAs has been detected.

**Summary**, from NCBI Gene [118672](https://www.ncbi.nlm.nih.gov/gene/118672):

> Predicted to enable kinase activity and tRNA binding activity. Predicted to be involved in translation. Predicted to act upstream of or within selenocysteine incorporation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28578) · Entrez [118672](https://www.ncbi.nlm.nih.gov/gene/118672) · UniProt [Q8IV42](https://www.uniprot.org/uniprotkb/Q8IV42) · Ensembl [ENSG00000179988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179988)

## Data

Gene col 11074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11074); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11074]; `tensor/DDL_lfc|DDL_z.npy` [11074]; `embed/gene_vectors.npy` [11074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11074 or target_col == 11074). Every well: [[PSTK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSTK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
