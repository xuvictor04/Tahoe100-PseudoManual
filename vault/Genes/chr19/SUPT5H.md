---
symbol: "SUPT5H"
type: "gene"
col: 12162
ensembl_id: "ENSG00000196235"
name: "SPT5 homolog, DSIF elongation factor subunit"
location: "19q13.2"
module: 41
arm: "+"
pooled_cpm: 189.61
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SUPT5H

*SPT5 homolog, DSIF elongation factor subunit* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +11.9, q 1e-29, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.331×; ⚠ cell-cycle shift, explains ~4% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B2]] (+0.69, fdr 7e-06), [[CCDC9]] (+0.64, fdr 1e-05), [[SART1]] (+0.62, fdr 3e-05); moves opposite to [[EIF5AL1]] (-0.58, fdr 3e-05), [[GSTCD]] (-0.54, fdr 1e-05), [[E2F3]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +11.9 | 1e-29 | 44/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.43×** | +9.4 | 2e-18 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.4 | 1e-14 | 41/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.2 | 4e-14 | 44/49 (NCI-H23, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +6.2 | 5e-08 | 38/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 1e-04 | 30/44 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 8e-04 | 31/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.3 | 1e-03 | 29/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.2 | 0.001 | 31/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.1 | 0.002 | 33/45 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.004 | 28/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.007 | 33/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.011 | 26/49 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.067 | 29/48 (SW480, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12162.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.331×; ⚠ cell-cycle shift, explains ~4% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.797× | -3.3 | 0.29 | 26/48 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.802× | -3.2 | 0.29 | 32/49 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.805× | -3.2 | 0.29 | 27/49 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1,079 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.4) | — |
| [[A-427 (line)]] | wt | 91.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 86.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.6) | — |
| [[SW480 (line)]] | alt | 120 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.17× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 178 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +20.6) | — |
| [[H4 (line)]] | wt | 190 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LoVo (line)]] | wt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.10× (z +8.5) | — |
| [[RKO (line)]] | wt | 113 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.95× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.69× (z +8.5) | — |
| [[A-172 (line)]] | wt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.7) | — |
| [[A549 (line)]] | wt | 200 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 98.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 129 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 136 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.29× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 164 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 157 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 142 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.5) | — |
| [[J82 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 149 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.32× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +16.6) | — |
| [[NCI-H2030 (line)]] | alt | 171 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +14.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.5) | — |
| [[A498 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 143 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 445 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B2]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 | STRING 454 |
| [[CCDC9]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SART1]] | +0.62 | +0.72 / +0.46 | both halves | 3e-05 | STRING 467 |
| [[PRPF6]] | +0.59 | +0.73 / +0.39 | both halves | 6e-05 |  |
| [[ZNF417]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CDK5RAP3]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SAFB2]] | +0.58 | +0.68 / +0.50 | both halves | 1e-05 | STRING 457 |
| [[PPIL4]] | +0.58 | +0.75 / +0.39 | both halves | 5e-05 |  |
| [[C12orf73]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[AAAS]] | +0.57 | +0.64 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[PRPF3]] | +0.57 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5AL1]] | -0.58 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[GSTCD]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[E2F3]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SIGMAR1]] | -0.50 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[FANCC]] | -0.49 | -0.58 / -0.37 | both halves | 7e-05 | pathway: TP53 Regulates Transcription of DNA Repair Genes |
| [[ATR]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 | pathway: Affinity selection of immunoglobulins; STRING 538 |
| [[DIAPH2]] | -0.48 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TXN]] | -0.48 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[SLC35B4]] | -0.48 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[PDE12]] | -0.47 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TUBA1B]] | -0.47 | -0.62 / -0.37 | both halves | 8e-05 | pathway: Affinity selection of immunoglobulins |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.3, -49.8); signed map (-50.4, 16.9). **Vector** length 123, 43.3% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +11.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.4 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +3.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.3 | -3.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -4.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | +4.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -3.6 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.4 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +0.4 |
|  | [[Thymol (drug)]] 5 µM |  | -2.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SPT5 homolog, DSIF elongation factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,436,156-39,476,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPT5H, SPT5, FLJ34157 |
| Hallmark sets | DNA_REPAIR |
| Reactome | 30 pathways, smallest: Abortive elongation of HIV-1 transcript in the absence of Tat; RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE |
| Matched by | ensembl_id |

**Function**, from UniProt [O00267](https://www.uniprot.org/uniprotkb/O00267) (Transcription elongation factor SPT5):

> Component of the DRB sensitivity-inducing factor complex (DSIF complex), which regulates mRNA processing and transcription elongation by RNA polymerase II. DSIF positively regulates mRNA capping by stimulating the mRNA guanylyltransferase activity of RNGTT/CAP1A. DSIF also acts cooperatively with the negative elongation factor complex (NELF complex) to enhance transcriptional pausing at sites proximal to the promoter. Transcriptional pausing may facilitate the assembly of an elongation …

**Summary**, from NCBI Gene [6829](https://www.ncbi.nlm.nih.gov/gene/6829):

> Enables enzyme binding activity and protein heterodimerization activity. Contributes to RNA polymerase inhibitor activity. Involved in positive regulation of macroautophagy; regulation of DNA-templated transcription; and transcription by RNA polymerase II. Located in nucleoplasm. Part of DSIF complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11469) · Entrez [6829](https://www.ncbi.nlm.nih.gov/gene/6829) · UniProt [O00267](https://www.uniprot.org/uniprotkb/O00267) · Ensembl [ENSG00000196235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196235)

## Data

Gene col 12162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12162); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12162]; `tensor/DDL_lfc|DDL_z.npy` [12162]; `embed/gene_vectors.npy` [12162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12162 or target_col == 12162). Every well: [[SUPT5H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT5H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
