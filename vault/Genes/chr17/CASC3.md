---
symbol: "CASC3"
type: "gene"
col: 2935
ensembl_id: "ENSG00000108349"
name: "CASC3 exon junction complex subunit"
location: "17q21.1"
module: 65
arm: "+"
pooled_cpm: 97.54
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# CASC3

*CASC3 exon junction complex subunit* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.24× (z +10.0, q 8e-21, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.646× (z -7.5, q 3e-11, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARNT]] (+0.65, fdr 7e-06), [[NDUFV2]] (+0.64, fdr 9e-06), [[PRMT9]] (+0.63, fdr 1e-05); moves opposite to [[PRORP]] (-0.59, fdr 1e-05), [[SETX]] (-0.57, fdr 1e-05), [[TUT7]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.24×** | +10.0 | 8e-21 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.4 | 5e-11 | 40/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +6.4 | 3e-08 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 9e-07 | 35/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +4.0 | 0.006 | 30/49 (NCI-H2030, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.047 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.060 | 26/49 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.14 | 25/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.15 | 23/48 (CFPAC-1, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -7.5 | 3e-11 | 39/49 (NCI-H23, SNU-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.705×** | -4.2 | 0.009 | 27/44 (SNU-1, C-33 A, …) | rises with dose | composition shift |
| [[Afatinib (drug)]] 0.5 µM |  | **0.800×** | -3.7 | 0.042 | 35/49 (NCI-H1792, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.751×** | -3.5 | 0.042 | 29/49 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.042 | 26/48 (HS-578T, A-427, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.756×** | -3.5 | 0.042 | 28/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.756×** | -3.5 | 0.042 | 29/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.042 | 27/48 (SHP-77, Panc 03.27, …) | rises with dose | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **0.761×** | -3.4 | 0.046 | 28/47 (HOP62, A-427, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.046 | 29/48 (C32, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.056 | 25/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -3.1 | 0.089 | 22/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.835× | -3.1 | 0.089 | 23/48 (CHP-212, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.781×** | -3.1 | 0.089 | 23/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.786×** | -3.0 | 0.100 | 26/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -3.0 | 0.100 | 22/48 (C32, HOP62, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.100 | 23/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 116 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -14.7) |
| [[PANC-1 (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +15.9) | — |
| [[SW480 (line)]] | alt | 70.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.6) | — |
| [[LoVo (line)]] | wt | 52.3 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 79.9 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.6) |
| [[A-427 (line)]] | wt | 116 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[KATO III (line)]] | alt | 54.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 80.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 98.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +11.9) | — |
| [[RKO (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.3) |
| [[SNU-1 (line)]] | wt | 169 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.1) |
| [[C32 (line)]] | wt | 79.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -10.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[COLO 205 (line)]] | alt | 80.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 87.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.4) |
| [[A-172 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 169 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[NDUFV2]] | +0.64 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[PRMT9]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.61 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.60 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ALG9]] | +0.60 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[AUH]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[FIP1L1]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[NAPB]] | +0.58 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.57 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[PCCB]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.57 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRORP]] | -0.59 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[SETX]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TUT7]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[SGMS2]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[BIN3]] | -0.53 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[CYTOR]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RAB7A]] | -0.52 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[E2F3]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[BACH1]] | -0.52 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[CDK12]] | -0.51 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MIR4435-2HG]] | -0.51 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ATP6V1D]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.6, -9.7); signed map (-29.5, -13.6). **Vector** length 103, 34.2% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +5.6 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.3 | -2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | -0.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.3 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | CASC3 exon junction complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,140,318-40,172,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLN51, BTZ |
| Gene groups (HGNC) | Exon junction complex; MicroRNA protein coding host genes |
| Reactome | 13 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [O15234](https://www.uniprot.org/uniprotkb/O15234) (Protein CASC3):

> Required for pre-mRNA splicing as component of the spliceosome. Core component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junctions on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either during EJC assembly or during subsequent mRNA metabolism. The EJC marks the position of the exon-exon junction in the mature mRNA for the gene …

**Summary**, from NCBI Gene [22794](https://www.ncbi.nlm.nih.gov/gene/22794):

> The product of this gene is a core component of the exon junction complex (EJC), a protein complex that is deposited on spliced mRNAs at exon-exon junctions and functions in nonsense-mediated mRNA decay (NMD). The encoded protein binds RNA and interacts with two other EJC core components. It is predominantly located in the cytoplasm, but shuttles into the nucleus where it localizes to nuclear speckles. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17040) · Entrez [22794](https://www.ncbi.nlm.nih.gov/gene/22794) · UniProt [O15234](https://www.uniprot.org/uniprotkb/O15234) · Ensembl [ENSG00000108349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108349)

## Data

Gene col 2935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2935); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2935]; `tensor/DDL_lfc|DDL_z.npy` [2935]; `embed/gene_vectors.npy` [2935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2935 or target_col == 2935). Every well: [[CASC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
