---
symbol: "CCNDBP1"
type: "gene"
col: 9393
ensembl_id: "ENSG00000166946"
name: "cyclin D1 binding protein 1"
location: "15q15.2"
module: 74
arm: "+"
pooled_cpm: 23.1
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 33
n_dd_up_clean: 4
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CCNDBP1

*cyclin D1 binding protein 1* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 1.88× (z +5.1, q 2e-04, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.391× (z -13.3, q 1e-37, down in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -11.7, q 5e-29, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YPEL3]] (+0.71, fdr 7e-06), [[ABTB1]] (+0.68, fdr 7e-06), [[CALCOCO1]] (+0.65, fdr 1e-05); moves opposite to [[PAICS]] (-0.55, fdr 6e-05), [[CDC7]] (-0.51, fdr 3e-05), [[KTN1-AS1]] (-0.50, fdr 5e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.88×** | +5.1 | 2e-04 | 27/46 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.5 | 0.002 | 26/48 (Panc 03.27, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.023 | 17/47 (SNU-423, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.7 | 0.023 | 13/32 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.7 | 0.023 | 16/40 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.035 | 18/47 (A-427, HOP62, …) | top dose only |  |
| [[DTP3 (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.042 | 15/45 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.14 | 12/45 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.391×** | -13.3 | 1e-37 | 42/48 (HT-29, LoVo, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -11.7 | 5e-29 | 41/47 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -10.7 | 2e-24 | 37/47 (AsPC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -10.3 | 1e-22 | 42/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -8.9 | 5e-17 | 35/46 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -7.6 | 4e-12 | 36/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.367×** | -7.1 | 1e-10 | 38/46 (RKO, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -7.0 | 2e-10 | 32/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.613×** | -6.7 | 2e-09 | 30/47 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -6.2 | 3e-08 | 29/47 (HOP62, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.8 | 4e-07 | 28/48 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.7 | 7e-07 | 29/46 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.663×** | -5.6 | 1e-06 | 28/46 (H4, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.472×** | -5.3 | 5e-06 | 30/46 (RPMI-7951, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.487×** | -5.1 | 1e-05 | 25/44 (AsPC-1, A549, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.666×** | -4.9 | 3e-05 | 26/48 (LoVo, RKO, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.500×** | -4.9 | 3e-05 | 27/46 (HT-29, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.542×** | -4.3 | 4e-04 | 19/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 37.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.0) |
| [[HT-29 (line)]] | alt | 40.4 | 0 | 6 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -14.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.5) |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.5) |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.291× (z -9.6) |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0281× (z -11.1) |
| [[LoVo (line)]] | wt | 34.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -10.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -10.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.311× (z -9.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.7) |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.4) |
| [[SW480 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.393× (z -9.2) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.404× (z -8.9) |
| [[A498 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -9.7) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -15.0) |
| [[H4 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0942× (z -10.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.6) |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.253× (z -10.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[RKO (line)]] | wt | 24.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0231× (z -11.6) |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL3]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[CALCOCO1]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.63 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[SPSB3]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SYF2]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 | STRING 970 |
| [[HEBP2]] | +0.60 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ZNHIT3]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RETREG3]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[SLU7]] | +0.59 | +0.39 / +0.71 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAICS]] | -0.55 | -0.39 / -0.65 | both halves | 6e-05 |  |
| [[CDC7]] | -0.51 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[KTN1-AS1]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[UBE2G2]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[LMNB2]] | -0.48 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.0, -46.5); signed map (-19.0, 10.7). **Vector** length 80.6, 17.7% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +4.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.3 | +5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -13.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -5.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin D1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:43,185,118-43,197,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIP1, GCIP, HHM |
| Matched by | ensembl_id |

**Function**, from UniProt [O95273](https://www.uniprot.org/uniprotkb/O95273) (Cyclin-D1-binding protein 1):

> May negatively regulate cell cycle progression. May act at least in part via inhibition of the cyclin-D1/CDK4 complex, thereby preventing phosphorylation of RB1 and blocking E2F-dependent transcription.

**Summary**, from NCBI Gene [23582](https://www.ncbi.nlm.nih.gov/gene/23582):

> This gene was identified by the interaction of its gene product with Grap2, a leukocyte-specific adaptor protein important for immune cell signaling. The protein encoded by this gene was shown to interact with cyclin D. Transfection of this gene in cells was reported to reduce the phosphorylation of Rb gene product by cyclin D-dependent protein kinase, and inhibit E2F1-mediated transcription activity. This protein was also found to interact with helix-loop-helix protein E12 and is thought to be …

**Accessions** — [HGNC:1587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1587) · Entrez [23582](https://www.ncbi.nlm.nih.gov/gene/23582) · UniProt [O95273](https://www.uniprot.org/uniprotkb/O95273) · Ensembl [ENSG00000166946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166946)

## Data

Gene col 9393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9393); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9393]; `tensor/DDL_lfc|DDL_z.npy` [9393]; `embed/gene_vectors.npy` [9393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9393 or target_col == 9393). Every well: [[CCNDBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNDBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
