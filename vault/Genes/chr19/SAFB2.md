---
symbol: "SAFB2"
type: "gene"
col: 5040
ensembl_id: "ENSG00000130254"
name: "scaffold attachment factor B2"
location: "19p13.3"
module: 41
arm: "+"
pooled_cpm: 107.44
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SAFB2

*scaffold attachment factor B2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.04× (z +19.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.669× (z -5.2, q 9e-05, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.713× (z -4.6, q 0.001, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZRSR2]] (+0.74, fdr 7e-06), [[TMF1]] (+0.70, fdr 7e-06), [[CCDC186]] (+0.68, fdr 7e-06); moves opposite to [[PHB1]] (-0.59, fdr 1e-05), [[EXT2]] (-0.57, fdr 8e-05), [[GLO1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +19.1 | 0e+00 | 48/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.63×** | +13.1 | 8e-37 | 48/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +10.2 | 3e-22 | 46/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.4 | 3e-11 | 39/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +5.8 | 1e-06 | 34/48 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 6e-06 | 31/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 1e-05 | 38/48 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.005 | 30/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.007 | 36/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.067 | 24/48 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -5.2 | 9e-05 | 31/44 (AsPC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.713×** | -4.6 | 0.001 | 40/48 (A498, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.733×** | -3.9 | 0.018 | 27/45 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Megestrol (drug)]] 0.05 µM |  | **0.765×** | -3.6 | 0.038 | 28/48 (H4, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.768×** | -3.6 | 0.040 | 30/49 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.042 | 30/48 (RKO, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.776×** | -3.4 | 0.043 | 31/48 (SW 900, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.777×** | -3.4 | 0.043 | 25/49 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.073 | 23/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.790×** | -3.2 | 0.077 | 26/48 (H4, HT-29, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.794×** | -3.1 | 0.091 | 26/48 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.796×** | -3.1 | 0.091 | 23/49 (H4, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 134 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -10.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 84.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +14.1) | — |
| [[LoVo (line)]] | wt | 138 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +19.8) | — |
| [[NCI-H460 (line)]] | wt | 72.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.7) | — |
| [[SNU-1 (line)]] | wt | 108 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +17.1) | — |
| [[SW480 (line)]] | alt | 119 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.3) | — |
| [[C-33 A (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 80.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 92.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 113 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +16.1) | — |
| [[SHP-77 (line)]] | alt | 89.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | — |
| [[SW48 (line)]] | wt | 145 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.1) | — |
| [[A498 (line)]] | wt | 113 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.0) | — |
| [[C32 (line)]] | wt | 86.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 77.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 95.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +17.2) | — |
| [[H4 (line)]] | wt | 126 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 108 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +16.6) | — |
| [[HOP62 (line)]] | alt | 81.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 99.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +14.0) | — |
| [[KATO III (line)]] | alt | 80.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +17.3) | — |
| [[RKO (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 70.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.8) | — |
| [[A-172 (line)]] | wt | 85.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[A-427 (line)]] | wt | 98.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 85.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.2) | — |
| [[J82 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.0) | — |
| [[SK-MEL-2 (line)]] | alt | 74.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0495× (z -10.6) |
| [[SW 900 (line)]] | alt | 135 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.1) | — |
| [[A549 (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRSR2]] | +0.74 | +0.78 / +0.64 | both halves | 7e-06 | same gene group |
| [[TMF1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CCDC186]] | +0.68 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[CCDC9]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GOLGA1]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SPTY2D1]] | +0.63 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[UFL1]] | +0.63 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[AKAP9]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.62 | +0.69 / +0.51 | both halves | 1e-05 | same gene group |
| [[ARFIP2]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB1]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[EXT2]] | -0.57 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[GLO1]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[VMA21]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[GOT2]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TMEM33]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[CDYL]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PTK2]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[C1QBP]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.9, -37.9); signed map (-50.1, 15.9). **Vector** length 98.2, 32.8% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +19.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | -5.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | -1.1 |
|  | [[Trimetrexate (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.5 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | +5.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -4.6 |
|  | [[Adenine (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | scaffold attachment factor B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,586,999-5,624,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0138 |
| Gene groups (HGNC) | RNA binding motif containing; Scaffold attachment factor B family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14151](https://www.uniprot.org/uniprotkb/Q14151) (Scaffold attachment factor B2):

> Binds to scaffold/matrix attachment region (S/MAR) DNA. Can function as an estrogen receptor corepressor and can also inhibit cell proliferation.

**Summary**, from NCBI Gene [9667](https://www.ncbi.nlm.nih.gov/gene/9667):

> The protein encoded by this gene, along with its paralog (scaffold attachment factor B1), is a repressor of estrogen receptor alpha. The encoded protein binds scaffold/matrix attachment region (S/MAR) DNA and is involved in cell cycle regulation, apoptosis, differentiation, the stress response, and regulation of immune genes. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:21605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21605) · Entrez [9667](https://www.ncbi.nlm.nih.gov/gene/9667) · UniProt [Q14151](https://www.uniprot.org/uniprotkb/Q14151) · Ensembl [ENSG00000130254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130254)

## Data

Gene col 5040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5040); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5040]; `tensor/DDL_lfc|DDL_z.npy` [5040]; `embed/gene_vectors.npy` [5040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5040 or target_col == 5040). Every well: [[SAFB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAFB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
