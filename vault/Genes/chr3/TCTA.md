---
symbol: "TCTA"
type: "gene"
col: 6952
ensembl_id: "ENSG00000145022"
name: "T cell leukemia translocation altered"
location: "3p21.31"
module: 35
arm: "+"
pooled_cpm: 6.54
n_lines_expressing: 50
n_dd_up: 48
n_dd_down: 5
n_dd_up_clean: 41
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TCTA

*T cell leukemia translocation altered* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.40× (z +15.8, q 0e+00, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +9.8, q 1e-20, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.636× (z -6.1, q 5e-07, down in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0828×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-1 0.0568×); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0963×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (C32 0.0754×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD6IP]] (+0.64, fdr 1e-05), [[ZSCAN30]] (+0.58, fdr 1e-05), [[RNF10]] (+0.58, fdr 3e-05); moves opposite to [[BLM]] (-0.53, fdr 3e-05), [[CKLF]] (-0.52, fdr 6e-05), [[CDCA4]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.40×** | +15.8 | 0e+00 | 11/12 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +15.0 | 0e+00 | 26/29 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +10.8 | 8e-25 | 16/20 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.8 | 1e-20 | 24/41 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.97×** | +9.1 | 1e-17 | 35/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.98×** | +8.8 | 9e-17 | 30/43 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.42×** | +6.7 | 2e-09 | 23/48 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +6.6 | 2e-09 | 23/45 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.6 | 3e-09 | 20/39 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +6.5 | 4e-09 | 14/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.1 | 4e-08 | 18/41 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.57×** | +6.0 | 8e-08 | 19/47 (A-172, HOP62, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.51×** | +6.0 | 1e-07 | 18/48 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.9 | 2e-07 | 20/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 6e-07 | 14/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 3e-06 | 9/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.53×** | +5.2 | 5e-06 | 10/47 (NCI-H460, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 3e-05 | 15/46 (HOP62, CHP-212, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6952.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0828×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-1 0.0568×); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0963×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (C32 0.0754×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -6.1 | 5e-07 | 24/46 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -4.7 | 9e-04 | 18/46 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.713×** | -4.6 | 9e-04 | 16/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.729×** | -4.3 | 0.002 | 13/47 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.763×** | -3.7 | 0.027 | 16/42 (SNU-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.646× | -3.1 | 0.18 | 9/41 (NCI-H460, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 2 (1 ⚠) | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0568× (z -11.5) |
| [[C32 (line)]] | wt | 5.84 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0754× (z -8.9) |
| [[HS-578T (line)]] | alt | 9.04 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0828× (z -12.1) |
| [[KATO III (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 6.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 9.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.22× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6IP]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZSCAN30]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RNF10]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[DNAJC27-AS1]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DCTN2]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[THBS3]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[UBE2A]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RAB21]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[WASHC3]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[RNF11]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RNF32]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PIGP]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLM]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CKLF]] | -0.52 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[CDCA4]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CCDC138]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ETV5]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ASB13]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SNRPD1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ETV4]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[KLHL8]] | -0.50 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[RFC4]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MNX1]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DSCC1]] | -0.49 | -0.49 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.3, 8.2); signed map (20.7, -21.3). **Vector** length 63.9, 9.49% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.6 | +8.8 |
|  | [[Trametinib (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +6.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +6.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | T cell leukemia translocation altered |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,412,212-49,416,476 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [P57738](https://www.uniprot.org/uniprotkb/P57738) (T-cell leukemia translocation-altered gene protein):

> May be required for cellular fusion during osteoclastogenesis.

**Summary**, from NCBI Gene [6988](https://www.ncbi.nlm.nih.gov/gene/6988):

> Involved in negative regulation of osteoclast differentiation and osteoclast fusion. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11692) · Entrez [6988](https://www.ncbi.nlm.nih.gov/gene/6988) · UniProt [P57738](https://www.uniprot.org/uniprotkb/P57738) · Ensembl [ENSG00000145022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145022)

## Data

Gene col 6952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6952); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6952]; `tensor/DDL_lfc|DDL_z.npy` [6952]; `embed/gene_vectors.npy` [6952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6952 or target_col == 6952). Every well: [[TCTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
