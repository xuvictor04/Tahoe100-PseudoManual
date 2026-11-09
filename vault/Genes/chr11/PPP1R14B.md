---
symbol: "PPP1R14B"
type: "gene"
col: 10388
ensembl_id: "ENSG00000173457"
name: "protein phosphatase 1 regulatory inhibitor subunit 14B"
location: "11q13.1"
module: 48
arm: "+"
pooled_cpm: 24.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# PPP1R14B

*protein phosphatase 1 regulatory inhibitor subunit 14B* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +7.3, q 1e-10, up in 39 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 5.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -7.1, q 7e-10, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GAT3]] (+0.68, fdr 1e-05), [[CCDC85B]] (+0.68, fdr 7e-06), [[ATP5F1E]] (+0.64, fdr 1e-05); moves opposite to [[ZXDB]] (-0.61, fdr 3e-05), [[GLUL]] (-0.61, fdr 1e-05), [[PPP2CA]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10388.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 5.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +7.3 | 1e-10 | 39/40 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +6.1 | 3e-07 | 31/33 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.16×** | +4.7 | 4e-04 | 40/46 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **2.12×** | +4.6 | 5e-04 | 40/44 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +4.4 | 0.001 | 29/36 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.36× | +3.1 | 0.19 | 33/44 (A-427, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -7.1 | 7e-10 | 41/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.349×** | -6.5 | 3e-08 | 44/48 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -6.0 | 5e-07 | 42/48 (SW48, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -5.2 | 3e-05 | 40/48 (AN3 CA, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.629×** | -4.0 | 0.006 | 33/48 (HCT15, H4, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.331×** | -3.6 | 0.036 | 39/48 (SNU-1, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.567×** | -3.5 | 0.040 | 33/48 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.352×** | -3.4 | 0.052 | 33/46 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.562×** | -3.3 | 0.052 | 30/48 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.594×** | -3.2 | 0.079 | 26/47 (LoVo, RPMI-7951, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.611× | -3.0 | 0.12 | 28/48 (AsPC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.588× | -3.0 | 0.12 | 34/47 (LoVo, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.85 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 17.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.9) |
| [[SW48 (line)]] | wt | 24.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0822× (z -10.1) |
| [[SW480 (line)]] | alt | 14.7 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 5.75× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -8.5) |
| [[BT-474 (line)]] | alt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -8.9) |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.152× (z -10.4) ⚠ cell-cycle shift, explains ~76% of this change |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.7) |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0467× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 21.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.0) |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -8.7) |
| [[A-172 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GAT3]] | +0.68 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CCDC85B]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ATP5F1E]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[COX17]] | +0.64 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[SNHG9]] | +0.63 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[SEC61G]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.62 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SSR4]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ATP5MK]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[RPL36]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.61 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[GLUL]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.60 | -0.53 / -0.47 | both halves | 2e-05 | STRING 553 |
| [[CCT7]] | -0.59 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[GPN1]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[UBQLN1]] | -0.58 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[XRCC6]] | -0.57 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MRPL9]] | -0.57 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[ZNF460]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[API5]] | -0.56 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[KAT7]] | -0.56 | -0.25 / -0.60 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-42.7, -19.6); signed map (-31.5, 11.8). **Vector** length 65.4, 18.8% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.51 to 7); *Cristae formation* (reactome, mean cos +0.51 to 7); *Mitochondrial biogenesis* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.0 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.5 | +1.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.3 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -3.1 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | +0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 14B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,244,479-64,246,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SOM172, PNG, PHI-1; previously PLCB3N |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C90](https://www.uniprot.org/uniprotkb/Q96C90) (Protein phosphatase 1 regulatory subunit 14B):

> Inhibitor of PPP1CA. Has over 50-fold higher inhibitory activity when phosphorylated (By similarity).

**Summary**, from NCBI Gene [26472](https://www.ncbi.nlm.nih.gov/gene/26472):

> Predicted to enable protein serine/threonine phosphatase inhibitor activity. Predicted to be involved in innate immune response. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9057) · Entrez [26472](https://www.ncbi.nlm.nih.gov/gene/26472) · UniProt [Q96C90](https://www.uniprot.org/uniprotkb/Q96C90) · Ensembl [ENSG00000173457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173457)

## Data

Gene col 10388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10388); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10388]; `tensor/DDL_lfc|DDL_z.npy` [10388]; `embed/gene_vectors.npy` [10388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10388 or target_col == 10388). Every well: [[PPP1R14B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R14B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
