---
symbol: "LRRC8E"
type: "gene"
col: 10040
ensembl_id: "ENSG00000171017"
name: "leucine rich repeat containing 8 VRAC subunit E"
location: "19p13.2"
module: 20
arm: "-"
pooled_cpm: 5.26
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# LRRC8E

*leucine rich repeat containing 8 VRAC subunit E* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +10.9, q 5e-25, up in 22 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -5.2, q 1e-04, down in 17 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP1S]] (+0.64, fdr 2e-05), [[TUBB2A]] (+0.63, fdr 7e-06), [[SLC66A1]] (+0.63, fdr 7e-06); moves opposite to [[STT3B]] (-0.65, fdr 1e-05), [[HNRNPA3]] (-0.63, fdr 1e-05), [[ANP32A]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[A4GALT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PLIN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +10.9 | 5e-25 | 22/34 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +8.4 | 7e-15 | 27/39 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +8.4 | 7e-15 | 21/32 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.7 | 3e-12 | 26/41 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +6.9 | 5e-10 | 21/38 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.1 | 9e-08 | 12/24 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.0 | 1e-07 | 20/41 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +4.7 | 1e-04 | 13/41 (SW480, HCT15, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.4 | 7e-04 | 14/32 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.3 | 0.001 | 5/42 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.002 | 15/38 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 12/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 7/39 (SW 900, KATO III, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.9 | 0.004 | 8/26 (NCI-H1573, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.004 | 12/38 (A-172, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.004 | 7/37 (NCI-H2030, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.015 | 8/35 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.024 | 6/37 (LoVo, NCI-H460, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.042 | 3/34 (LoVo, A-427, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -5.2 | 1e-04 | 17/36 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.656×** | -4.7 | 8e-04 | 16/38 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -4.3 | 0.004 | 11/37 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 5 µM |  | 0.761× | -3.0 | 0.29 | 9/38 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.832× | -3.0 | 0.29 | 4/40 (PANC-1, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.0 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +19.3) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.342× (z -9.9) |
| [[A498 (line)]] | wt | 12.6 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +19.1) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 7.37 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0710× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.30 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0793× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.62 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0890× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 3.42 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.116× (z -8.7) |
| [[RKO (line)]] | wt | 8.67 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0765× (z -10.1) |
| [[SNU-423 (line)]] | alt | 9.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +11.9) | — |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1S]] | +0.64 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TUBB2A]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SLC66A1]] | +0.63 | +0.66 / +0.68 | both halves | 7e-06 | pathway: Miscellaneous transport and binding events |
| [[PWWP2B]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZDHHC18]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZNF316]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM70]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[RCE1]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[JUND]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SPATA2L]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PIAS4]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ANP32A]] | -0.62 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DDOST]] | -0.62 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[MSL3]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[DHFR]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PRDX3]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CRTAP]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TM9SF3]] | -0.58 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[TMEM30A]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.58 | -0.50 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[A4GALT]] | B | A4GALT activity raises LRRC8E's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without A4GALT | 0.090 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN3]] | B | LRRC8E activity raises PLIN3's level | lines that do not express LRRC8E (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without LRRC8E | 0.089 | ⚠ within organs, on part of the lines; also absent: ITPR3, SQOR, BIRC3; its own permutation p |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-47.0, 15.9); signed map (-0.9, -11.9). **Vector** length 63.1, 10.6% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -0.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 8 VRAC subunit E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,888,505-7,902,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23420 |
| Gene groups (HGNC) | Volume regulated anion channel subunits |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NSJ5](https://www.uniprot.org/uniprotkb/Q6NSJ5) (Volume-regulated anion channel subunit LRRC8E):

> Non-essential component of the volume-regulated anion channel (VRAC, also named VSOAC channel), an anion channel required to maintain a constant cell volume in response to extracellular or intracellular osmotic changes. The VRAC channel conducts iodide better than chloride and can also conduct organic osmolytes like taurine. Mediates efflux of amino acids, such as aspartate, in response to osmotic stress. The VRAC channel also mediates transport of immunoreactive cyclic dinucleotide GMP-AMP …

**Summary**, from NCBI Gene [80131](https://www.ncbi.nlm.nih.gov/gene/80131):

> This gene encodes a member of a small, conserved family of proteins with similar structure, including a string of extracellular leucine-rich repeats. A related protein was shown to be involved in B-cell development. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:26272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26272) · Entrez [80131](https://www.ncbi.nlm.nih.gov/gene/80131) · UniProt [Q6NSJ5](https://www.uniprot.org/uniprotkb/Q6NSJ5) · Ensembl [ENSG00000171017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171017)

## Data

Gene col 10040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10040); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10040]; `tensor/DDL_lfc|DDL_z.npy` [10040]; `embed/gene_vectors.npy` [10040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10040 or target_col == 10040). Every well: [[LRRC8E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC8E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
