---
symbol: "VAMP4"
type: "gene"
col: 3923
ensembl_id: "ENSG00000117533"
name: "vesicle associated membrane protein 4"
location: "1q24.3"
module: 4
arm: "-"
pooled_cpm: 20.11
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# VAMP4

*vesicle associated membrane protein 4* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +8.6, q 5e-15, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.700× (z -6.9, q 3e-09, down in 22 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.721× (z -6.3, q 6e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGDS]] (+0.61, fdr 1e-05), [[TSNAX]] (+0.60, fdr 3e-05), [[ARV1]] (+0.59, fdr 2e-05); moves opposite to [[MRPS28]] (-0.53, fdr 1e-05), [[RRP7BP-1]] (-0.53, fdr 1e-05), [[POLR1A]] (-0.53, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +8.6 | 5e-15 | 25/46 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +6.4 | 4e-08 | 20/47 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +5.3 | 3e-05 | 17/46 (A-172, HS-578T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.004 | 11/48 (KATO III, LoVo, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.028 | 10/48 (LoVo, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.21 | 7/48 (A-427, RKO, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.35× | +3.0 | 0.21 | 5/46 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -6.9 | 3e-09 | 22/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.721×** | -6.3 | 6e-08 | 24/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.743×** | -5.8 | 1e-06 | 19/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.743×** | -5.8 | 1e-06 | 20/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -5.6 | 2e-06 | 25/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -4.9 | 1e-04 | 15/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.788×** | -4.6 | 3e-04 | 18/46 (NCI-H460, AsPC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -4.4 | 6e-04 | 16/48 (SW480, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.803×** | -4.1 | 0.003 | 21/43 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.812×** | -4.1 | 0.003 | 21/48 (NCI-H460, SW 1271, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.870× | -3.8 | 0.007 | 15/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -3.8 | 0.008 | 15/48 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.835× | -3.5 | 0.020 | 9/47 (hTERT-HPNE, SK-MEL-2, …) | two highest doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.851× | -3.1 | 0.070 | 10/48 (RKO, RPMI-7951, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.895× | -3.1 | 0.082 | 10/48 (SW480, NCI-H1792, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.855× | -3.0 | 0.085 | 5/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.897× | -3.0 | 0.096 | 11/48 (A-427, A498, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.099 | 3/48 (LoVo, A549, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.855× | -2.9 | 0.099 | 6/48 (NCI-H2347, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.4 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -12.7) |
| [[A-172 (line)]] | wt | 32.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 23.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.9) | — |
| [[A498 (line)]] | wt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.138× (z -8.8) |
| [[HOP62 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +16.0) | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.303× (z -10.1) |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGDS]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[TSNAX]] | +0.60 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[ARV1]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SEPSECS]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ACOT8]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[C14orf28]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PRKAB2]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MMUT]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[FBXO8]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HADHB]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CDK7]] | +0.52 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ACP6]] | +0.51 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS28]] | -0.53 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.53 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[INO80]] | -0.53 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PITPNB]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NOP56]] | -0.50 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[MFSD14CP-1]] | -0.50 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[NOP2]] | -0.50 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[STAG1]] | -0.49 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SNRPB]] | -0.49 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[WDR82]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TUBA8]] | -0.49 | -0.48 / -0.56 | both halves | 2e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.423). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.2, -6.5); signed map (-18.4, -12.9). **Vector** length 82.1, 15.0% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.7 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.6 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.2 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -3.0 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Mifepristone (drug)]] 0.5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:171,700,160-171,742,074 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Vesicle associated membrane proteins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 6 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75379](https://www.uniprot.org/uniprotkb/O75379) (Vesicle-associated membrane protein 4):

> SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) are essential proteins for intracellular membrane fusion. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four-helix bundle whose assembly releases energy that drives membrane fusion. The core SNARE complex typically consists of four alpha-helical domains, three from target membrane SNAREs (t-SNAREs) and one from a vesicle SNARE (v-SNARE). VAMP4 is a v-SNARE that …

**Summary**, from NCBI Gene [8674](https://www.ncbi.nlm.nih.gov/gene/8674):

> Synaptobrevins/VAMPs, syntaxins, and the 25-kD synaptosomal-associated protein SNAP25 are the main components of a protein complex involved in the docking and/or fusion of synaptic vesicles with the presynaptic membrane. The protein encoded by this gene is a member of the vesicle-associated membrane protein (VAMP)/synaptobrevin family. This protein may play a role in trans-Golgi network-to-endosome transport. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12645) · Entrez [8674](https://www.ncbi.nlm.nih.gov/gene/8674) · UniProt [O75379](https://www.uniprot.org/uniprotkb/O75379) · Ensembl [ENSG00000117533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117533)

## Data

Gene col 3923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3923); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3923]; `tensor/DDL_lfc|DDL_z.npy` [3923]; `embed/gene_vectors.npy` [3923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3923 or target_col == 3923). Every well: [[VAMP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
