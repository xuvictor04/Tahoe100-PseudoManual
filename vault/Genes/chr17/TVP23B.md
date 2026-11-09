---
symbol: "TVP23B"
type: "gene"
col: 10185
ensembl_id: "ENSG00000171928"
name: "trans-golgi network vesicle protein 23 homolog B"
location: "17p11.2"
module: 41
arm: "+"
pooled_cpm: 37.35
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TVP23B

*trans-golgi network vesicle protein 23 homolog B* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 4.88× (z +14.0, q 8e-42, up in 48 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 8 lines (A498 8.87×, SW480 7.71×, HS-578T 8.31×, HOP62 6.09×, …); [[PH-797804 (drug)]] 5 µM in 4 lines (SW480 7.68×, HS-578T 7.51×, HOP62 6.01×, HEC-1-A 7.80×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.501× (z -11.6, q 2e-28, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSR2]] (+0.69, fdr 7e-06), [[SRP54]] (+0.68, fdr 7e-06), [[ACBD3]] (+0.68, fdr 7e-06); moves opposite to [[IDH3A]] (-0.57, fdr 3e-05), [[DIAPH1]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10185.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 8 lines (A498 8.87×, SW480 7.71×, HS-578T 8.31×, HOP62 6.09×, …); [[PH-797804 (drug)]] 5 µM in 4 lines (SW480 7.68×, HS-578T 7.51×, HOP62 6.01×, HEC-1-A 7.80×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.88×** | +14.0 | 8e-42 | 48/49 (A498, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.52×** | +11.1 | 3e-26 | 40/48 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.33× | +3.4 | 0.11 | 13/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.30 | 13/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.501×** | -11.6 | 2e-28 | 43/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.502×** | -11.6 | 2e-28 | 39/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.511×** | -11.3 | 3e-27 | 45/48 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.558×** | -9.8 | 2e-20 | 37/47 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -9.3 | 1e-18 | 28/38 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.617×** | -8.1 | 6e-14 | 38/48 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -7.8 | 5e-13 | 36/48 (A498, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.628×** | -7.8 | 5e-13 | 38/48 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -7.4 | 8e-12 | 30/41 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.769×** | -6.2 | 3e-08 | 25/47 (NCI-H1792, NCI-H2347, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.742×** | -5.0 | 3e-05 | 28/48 (KATO III, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -4.0 | 0.003 | 23/48 (HS-578T, SW 900, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.656×** | -3.7 | 0.010 | 17/48 (H4, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.747×** | -3.5 | 0.021 | 12/48 (Hs 766T, CHP-212, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.815×** | -3.4 | 0.027 | 16/48 (RKO, SW480, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.874× | -3.1 | 0.056 | 15/48 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.056 | 16/48 (LoVo, SW48, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.082 | 15/48 (CHP-212, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 57.2 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.61× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.7) |
| [[HOP62 (line)]] | alt | 45.4 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 6.09× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.409× (z -9.1) |
| [[LoVo (line)]] | wt | 40.9 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.23× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.347× (z -9.6) |
| [[A498 (line)]] | wt | 52.5 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 8.87× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.394× (z -9.6) |
| [[KATO III (line)]] | alt | 71.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.332× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 43.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.49× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.31× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.342× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.324× (z -11.4) |
| [[SW 900 (line)]] | alt | 53.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.71× (z +11.2) | — |
| [[A-427 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.123× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -21.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.341× (z -8.6) |
| [[HCT15 (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 30.7 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.80× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.286× (z -9.0) |
| [[LS 180 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0559× (z -20.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -16.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.43× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSR2]] | +0.69 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[SRP54]] | +0.68 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.68 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[USPL1]] | +0.67 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.67 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ECD]] | +0.67 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.66 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MED6]] | +0.64 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[GMPPA]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3A]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.54 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.5, -35.0); signed map (-49.8, 12.5). **Vector** length 88.7, 20.1% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +14.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | trans-golgi network vesicle protein 23 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,781,111-18,806,714 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-148, YDR084C; previously FAM18B, FAM18B1 |
| Matched by | ensembl_id |

UniProt [Q9NYZ1](https://www.uniprot.org/uniprotkb/Q9NYZ1) carries no function annotation.

**Summary**, from NCBI Gene [51030](https://www.ncbi.nlm.nih.gov/gene/51030):

> Predicted to be involved in protein secretion and vesicle-mediated transport. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20399) · Entrez [51030](https://www.ncbi.nlm.nih.gov/gene/51030) · UniProt [Q9NYZ1](https://www.uniprot.org/uniprotkb/Q9NYZ1) · Ensembl [ENSG00000171928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171928)

## Data

Gene col 10185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10185); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10185]; `tensor/DDL_lfc|DDL_z.npy` [10185]; `embed/gene_vectors.npy` [10185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10185 or target_col == 10185). Every well: [[TVP23B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TVP23B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
