---
symbol: "DCK"
type: "gene"
col: 7951
ensembl_id: "ENSG00000156136"
name: "deoxycytidine kinase"
location: "4q13.3"
module: 6
arm: "+"
pooled_cpm: 24.64
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DCK

*deoxycytidine kinase* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +14.4, q 2e-44, up in 36 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.30× (z +6.8, q 9e-10, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.781× (z -6.4, q 8e-08, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MANEA]] (+0.72, fdr 7e-06), [[ERLIN1]] (+0.69, fdr 7e-06), [[CHEK1]] (+0.69, fdr 7e-06); moves opposite to [[CTBP1-AS]] (-0.52, fdr 3e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[UBE2CP5]] (-0.51, fdr 2e-05), [[LINC02804]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.20×** | +14.4 | 2e-44 | 36/42 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.01×** | +12.3 | 2e-32 | 33/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +9.0 | 4e-17 | 6/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.68×** | +8.8 | 2e-16 | 27/41 (NCI-H2347, J82, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +6.8 | 9e-10 | 28/48 (J82, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 4e-08 | 24/47 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.6 | 2e-06 | 23/45 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 3e-05 | 24/48 (HEC-1-A, SW1417, …) | two highest doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +3.7 | 0.016 | 9/48 (H4, HEC-1-A, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.21×** | +3.5 | 0.027 | 16/46 (LS 180, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.13× | +3.2 | 0.061 | 7/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.13× | +3.1 | 0.078 | 11/48 (SW1417, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.781×** | -6.4 | 8e-08 | 22/48 (H4, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.772×** | -4.5 | 0.002 | 20/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.808×** | -3.9 | 0.017 | 19/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.816×** | -3.7 | 0.026 | 18/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.878× | -3.4 | 0.079 | 11/48 (Hs 766T, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 26.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0721× (z -9.2) |
| [[H4 (line)]] | wt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0434× (z -14.3) |
| [[HOP62 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.193× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANEA]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ERLIN1]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CHEK1]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MAD2L1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SGCB]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[TMEM237]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TIMELESS]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TMEM109]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[CENPH]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[HELLS]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[HADH]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FANCG]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTBP1-AS]] ⚠ | -0.52 | -0.54 / -0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UBE2CP5]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[LINC02804]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises DCK's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises DCK's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without TCF19 | 0.080 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PBK]] | C | PBK activity raises DCK's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without PBK | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.8, -40.0); signed map (-31.8, -42.3). **Vector** length 79.7, 15.7% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.4 | +12.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.8 | +14.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.6 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | deoxycytidine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:70,992,538-71,030,914 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Deoxyribonucleoside kinases |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: Pyrimidine salvage; Purine salvage; Nucleotide salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [P27707](https://www.uniprot.org/uniprotkb/P27707) (Deoxycytidine kinase):

> Phosphorylates the deoxyribonucleosides deoxycytidine, deoxyguanosine and deoxyadenosine. Has broad substrate specificity, and does not display selectivity based on the chirality of the substrate. It is also an essential enzyme for the phosphorylation of numerous nucleoside analogs widely employed as antiviral and chemotherapeutic agents.

**Summary**, from NCBI Gene [1633](https://www.ncbi.nlm.nih.gov/gene/1633):

> Deoxycytidine kinase (DCK) is required for the phosphorylation of several deoxyribonucleosides and their nucleoside analogs. Deficiency of DCK is associated with resistance to antiviral and anticancer chemotherapeutic agents. Conversely, increased deoxycytidine kinase activity is associated with increased activation of these compounds to cytotoxic nucleoside triphosphate derivatives. DCK is clinically important because of its relationship to drug resistance and sensitivity. [provided by RefSeq, …

**Accessions** — [HGNC:2704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2704) · Entrez [1633](https://www.ncbi.nlm.nih.gov/gene/1633) · UniProt [P27707](https://www.uniprot.org/uniprotkb/P27707) · Ensembl [ENSG00000156136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156136)

## Data

Gene col 7951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7951); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7951]; `tensor/DDL_lfc|DDL_z.npy` [7951]; `embed/gene_vectors.npy` [7951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7951 or target_col == 7951). Every well: [[DCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
