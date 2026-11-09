---
symbol: "PNPLA6"
type: "gene"
col: 406
ensembl_id: "ENSG00000032444"
name: "patatin like domain 6, lysophospholipase"
location: "19p13.2"
module: 2
arm: "+"
pooled_cpm: 17.56
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PNPLA6

*patatin like domain 6, lysophospholipase* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.57× (z +9.2, q 3e-17, up in 29 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.30× (z +3.8, q 0.021, up in 10 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.487× (z -11.7, q 5e-29, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB2]] (+0.63, fdr 1e-05), [[HMG20B]] (+0.62, fdr 1e-05), [[TMEM259]] (+0.61, fdr 3e-05); moves opposite to [[FBXO45]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.2 | 3e-17 | 29/42 (LS 180, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +8.8 | 3e-16 | 20/30 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +8.3 | 2e-14 | 20/37 (HS-578T, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.021 | 10/45 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.033 | 16/44 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | 1.36× | +3.2 | 0.12 | 6/45 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.21× | +3.1 | 0.17 | 8/47 (HS-578T, J82, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.487×** | -11.7 | 5e-29 | 35/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -11.5 | 6e-28 | 34/47 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.603×** | -10.3 | 2e-22 | 32/47 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.707×** | -10.0 | 3e-21 | 31/47 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.768×** | -7.6 | 4e-12 | 27/47 (SNU-1, AsPC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.719×** | -6.7 | 2e-09 | 23/47 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.741×** | -6.1 | 1e-07 | 23/48 (SW480, NCI-H2030, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.713×** | -5.5 | 3e-06 | 23/47 (SNU-1, H4, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.594×** | -5.4 | 4e-06 | 15/48 (SNU-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.766×** | -5.4 | 4e-06 | 21/46 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.722×** | -5.3 | 5e-06 | 18/48 (C-33 A, SNU-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -5.3 | 7e-06 | 21/48 (SNU-1, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.788×** | -4.8 | 6e-05 | 17/47 (SW480, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.793×** | -4.7 | 9e-05 | 19/47 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.764×** | -4.4 | 4e-04 | 18/42 (LOX-IMVI, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.662×** | -4.3 | 6e-04 | 11/45 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.784×** | -4.0 | 0.002 | 16/47 (HepG2/C3A, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.843× | -3.5 | 0.015 | 5/48 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | 0.849× | -3.3 | 0.025 | 9/48 (SW 900, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.068 | 12/48 (SHP-77, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0360× (z -17.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -12.4) |
| [[A-427 (line)]] | wt | 32.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.265× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.180× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.215× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0978× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.125× (z -8.8) |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -8.5) |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -10.2) ⚠ cell-cycle shift, explains ~99% of this change |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -8.8) |
| [[RKO (line)]] | wt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -11.0) |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.109× (z -11.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB2]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[HMG20B]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.61 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[TRAF7]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MED16]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[GDI1]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LZTS3]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SBF1]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 | pathway: PI Metabolism |
| [[DDA1]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[LENG8]] | +0.55 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[GET4]] | +0.54 | +0.27 / +0.64 | both halves | 3e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO45]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.5, -21.9); signed map (-28.3, -0.7). **Vector** length 68.0, 10.8% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +2.3 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | -0.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.3 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | patatin like domain 6, lysophospholipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,534,004-7,561,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTE, sws, iPLA2delta, SPG39 |
| Gene groups (HGNC) | Patatin like phospholipase domain containing |
| Reactome | 4 pathways, smallest: Glycerophospholipid catabolism; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY17](https://www.uniprot.org/uniprotkb/Q8IY17) (Patatin-like phospholipase domain-containing protein 6):

> Phospholipase B that deacylates intracellular phosphatidylcholine (PtdCho), generating glycerophosphocholine (GroPtdCho). This deacylation occurs at both sn-2 and sn-1 positions of PtdCho. Catalyzes the hydrolysis of several naturally occurring membrane-associated lipids. Hydrolyzes lysophospholipids and monoacylglycerols, preferring the 1-acyl to the 2-acyl isomer. Does not catalyze hydrolysis of di- or triacylglycerols or fatty acid amides.

**Summary**, from NCBI Gene [10908](https://www.ncbi.nlm.nih.gov/gene/10908):

> This gene encodes a phospholipase that deacetylates intracellular phosphatidylcholine to produce glycerophosphocholine. It is thought to function in neurite outgrowth and process elongation during neuronal differentiation. The protein is anchored to the cytoplasmic face of the endoplasmic reticulum in both neurons and non-neuronal cells. Mutations in this gene result in autosomal recessive spastic paraplegia, and the protein is the target for neurodegeneration induced by organophosphorus …

**Accessions** — [HGNC:16268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16268) · Entrez [10908](https://www.ncbi.nlm.nih.gov/gene/10908) · UniProt [Q8IY17](https://www.uniprot.org/uniprotkb/Q8IY17) · Ensembl [ENSG00000032444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000032444)

## Data

Gene col 406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 406); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 406]; `tensor/DDL_lfc|DDL_z.npy` [406]; `embed/gene_vectors.npy` [406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 406 or target_col == 406). Every well: [[PNPLA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPLA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
