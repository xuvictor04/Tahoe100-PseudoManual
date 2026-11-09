---
symbol: "RPS9"
type: "gene"
col: 10019
ensembl_id: "ENSG00000170889"
name: "ribosomal protein S9"
location: "19q13.42"
module: 43
arm: "+"
pooled_cpm: 70.36
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS9

*ribosomal protein S9* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +9.5, q 1e-18, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.40× (z +9.1, q 3e-17, up in 46 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[OTS514 (drug)]] 5 µM in 1 line (H4 0.0693×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4B]] (+0.62, fdr 7e-06), [[EEF1B2]] (+0.60, fdr 1e-05), [[RPL14]] (+0.59, fdr 1e-05); moves opposite to [[DDX52]] (-0.49, fdr 1e-04), [[LRRC57]] (-0.47, fdr 4e-05), [[CMTR2]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +9.5 | 1e-18 | 45/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.40×** | +9.1 | 3e-17 | 46/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +8.0 | 3e-13 | 41/45 (KATO III, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +7.4 | 3e-11 | 34/48 (NCI-H1792, C32, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.1 | 2e-10 | 35/43 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +6.2 | 7e-08 | 41/48 (HT-29, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.5 | 3e-06 | 39/48 (HT-29, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +5.4 | 4e-06 | 34/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.46×** | +5.4 | 5e-06 | 33/47 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.99×** | +5.1 | 2e-05 | 37/48 (Panc 03.27, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.43×** | +5.0 | 2e-05 | 30/48 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.9 | 4e-05 | 34/47 (SHP-77, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.90×** | +4.8 | 7e-05 | 31/48 (A549, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.85×** | +4.6 | 2e-04 | 37/48 (A549, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +4.5 | 3e-04 | 31/48 (NCI-H460, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.004 | 26/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.005 | 28/48 (SW1417, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.026 | 24/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.066 | 20/49 (MIA PaCa-2, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.081 | 11/48 (NCI-H2347, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10019.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[OTS514 (drug)]] 5 µM in 1 line (H4 0.0693×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.849× | -3.3 | 0.64 | 19/48 (SW480, SNU-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 49.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +16.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 60.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 96.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 70.1 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0693× (z -8.6) |
| [[Hs 766T (line)]] | wt | 57.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 62.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 78.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 83.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.17× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +21.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 71.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[Panc 03.27 (line)]] | alt | 68.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 63.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.17× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 69.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4B]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 655 |
| [[EEF1B2]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 976 |
| [[RPL14]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL3]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[SNHG29]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PCBP2]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 | pathway: SARS-CoV-1 Infection |
| [[NPM1]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 813 |
| [[RPL39]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[SLC25A6]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 | pathway: Influenza Infection |
| [[RPL27A]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS2]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[SNHG16]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX52]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 860 |
| [[LRRC57]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CMTR2]] | -0.44 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[REST]] | -0.43 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[RO60]] | -0.42 | -0.44 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.441). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.0, -31.0); signed map (-23.4, -33.3). **Vector** length 84.5, 21.3% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.3 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.6 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,200,809-54,249,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S9, uS4 |
| Gene groups (HGNC) | S ribosomal proteins |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 52 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P46781](https://www.uniprot.org/uniprotkb/P46781) (Small ribosomal subunit protein uS4):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6203](https://www.ncbi.nlm.nih.gov/gene/6203):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S4P family of ribosomal proteins. It is located in the cytoplasm. Variable expression of this gene in colorectal cancers compared to adjacent normal tissues has been …

**Accessions** — [HGNC:10442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10442) · Entrez [6203](https://www.ncbi.nlm.nih.gov/gene/6203) · UniProt [P46781](https://www.uniprot.org/uniprotkb/P46781) · Ensembl [ENSG00000170889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170889)

## Data

Gene col 10019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10019); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10019]; `tensor/DDL_lfc|DDL_z.npy` [10019]; `embed/gene_vectors.npy` [10019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10019 or target_col == 10019). Every well: [[RPS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
