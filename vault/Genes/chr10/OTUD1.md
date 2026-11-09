---
symbol: "OTUD1"
type: "gene"
col: 9106
ensembl_id: "ENSG00000165312"
name: "OTU deubiquitinase 1"
location: "10p12.2"
module: 69
arm: "+"
pooled_cpm: 7.74
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 18
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# OTUD1

*OTU deubiquitinase 1* — 10p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +10.7, q 8e-24, up in 25 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.388× (z -13.6, q 2e-39, down in 35 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.491× (z -7.3, q 9e-11, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2A]] (+0.64, fdr 1e-05), [[ZBTB10]] (+0.64, fdr 1e-05), [[FBXO32]] (+0.60, fdr 1e-05); moves opposite to [[RNGTT]] (-0.62, fdr 7e-06), [[RABEPK]] (-0.54, fdr 1e-05), [[NCLN]] (-0.53, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +10.7 | 8e-24 | 25/40 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.6 | 2e-08 | 15/44 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 2e-08 | 17/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +5.4 | 7e-06 | 16/44 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.4 | 7e-06 | 6/25 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 7e-06 | 14/42 (LoVo, SW 900, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.3 | 9e-06 | 10/33 (NCI-H2030, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.2 | 1e-05 | 13/39 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 5e-04 | 12/45 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +4.2 | 0.001 | 12/46 (SW 900, NCI-H460, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 0.05 µM |  | **1.33×** | +4.1 | 0.002 | 3/43 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.003 | 6/45 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.012 | 9/45 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.018 | 8/33 (LOX-IMVI, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.018 | 6/46 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.034 | 5/40 (HEC-1-A, LS 180, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.043 | 6/45 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.1 | 0.050 | 2/44 (RKO, A498) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.388×** | -13.6 | 2e-39 | 35/46 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.491×** | -7.3 | 9e-11 | 26/46 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.663×** | -5.7 | 3e-06 | 14/39 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.480×** | -5.5 | 5e-06 | 17/42 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.484×** | -5.4 | 6e-06 | 15/40 (KATO III, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.502×** | -5.2 | 2e-05 | 12/35 (A549, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -4.8 | 1e-04 | 15/43 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.547×** | -4.5 | 4e-04 | 14/38 (J82, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.718×** | -4.5 | 5e-04 | 12/42 (HOP62, SW48, …) | all doses, flat | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.666×** | -4.2 | 0.002 | 11/42 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.760×** | -3.9 | 0.005 | 13/37 (NCI-H23, SW1417, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.685×** | -3.9 | 0.005 | 10/43 (A-427, KATO III, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **0.779×** | -3.6 | 0.016 | 13/41 (LOX-IMVI, RKO, …) | two highest doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | **0.785×** | -3.5 | 0.022 | 6/45 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.794×** | -3.3 | 0.038 | 9/43 (AsPC-1, HepG2/C3A, …) | two highest doses | position effect removed |
| [[Ritonavir (drug)]] 5 µM |  | 0.850× | -3.3 | 0.039 | 3/44 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.047 | 18/42 (SNU-423, J82, …) | top dose only |  |
| [[Everolimus (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.049 | 6/43 (NCI-H23, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.666×** | -3.0 | 0.068 | 12/34 (KATO III, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +21.1) | — |
| [[HT-29 (line)]] | alt | 7.11 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0495× (z -13.0) |
| [[J82 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 9.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +18.3) | — |
| [[A-172 (line)]] | wt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0841× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.24 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0848× (z -8.5) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 6.87 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.110× (z -10.0) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0552× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2A]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ZBTB10]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[FBXO32]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GABARAPL1]] | +0.60 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[CITED2]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SWAP70]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PHF3]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[RNF103]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[OPTN]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | pathway: Death Receptor Signaling |
| [[DLX2]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.62 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[RABEPK]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NCLN]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[EARS2]] | -0.52 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[EIPR1]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SNRNP40]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NSUN2]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[NUP205]] | -0.50 | -0.43 / -0.52 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[FUBP3]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PDSS1]] | -0.50 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[HARS1]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.2, -38.8); signed map (-9.7, 12.3). **Vector** length 79.4, 14.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +5.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +6.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -13.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -5.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.2 — chr10:23,439,075-23,442,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DUBA7; previously OTDC1 |
| Gene groups (HGNC) | OTU domain containing |
| Reactome | 5 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VV17](https://www.uniprot.org/uniprotkb/Q5VV17) (OTU domain-containing protein 1):

> Deubiquitinating enzyme that specifically hydrolyzes 'Lys-63'-linked polyubiquitin to monoubiquitin. Required for the stability and translation of a subset mRNAs with a high abundance of rare codons by mediating deubiquitination of 40S ribosomal protein RPS10/eS10, thereby antagonizing ZNF598-mediated 40S ubiquitination. The abundance of rare codons in mRNAs can limit the translation rate and can lead to ribosome collisions that trigger activation of ribosome quality control (RQC) pathway by …

**Summary**, from NCBI Gene [220213](https://www.ncbi.nlm.nih.gov/gene/220213):

> Deubiquitinating enzymes (DUBs; see MIM 603478) are proteases that specifically cleave ubiquitin (MIM 191339) linkages, negating the action of ubiquitin ligases. DUBA7 belongs to a DUB subfamily characterized by an ovarian tumor (OTU) domain.[supplied by OMIM, May 2008]

**Accessions** — [HGNC:27346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27346) · Entrez [220213](https://www.ncbi.nlm.nih.gov/gene/220213) · UniProt [Q5VV17](https://www.uniprot.org/uniprotkb/Q5VV17) · Ensembl [ENSG00000165312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165312)

## Data

Gene col 9106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9106); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9106]; `tensor/DDL_lfc|DDL_z.npy` [9106]; `embed/gene_vectors.npy` [9106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9106 or target_col == 9106). Every well: [[OTUD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
